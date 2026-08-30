import base64
import hashlib
import hmac
import os
import re
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from db import get_conn
from agents.license_manager import create_license

_DISCOUNT_CODE_RE = re.compile(r"^[A-Z0-9_\-]{1,64}$")


PRODUCT_CODE = "yoonbot"
ORDER_STATUSES = {"payment_pending", "paid", "license_issued", "canceled", "refunded"}
TOSS_CONFIRM_URL = "https://api.tosspayments.com/v1/payments/confirm"
PLANS = {
    "trial": {
        "code": "trial",
        "name": "Trial",
        "amount_krw": 0,
        "license_days": 7,
        "description": "운영자 승인 후 7일 테스트 라이선스를 발급합니다.",
    },
    "monthly": {
        "code": "monthly",
        "name": "Monthly",
        "amount_krw": 99000,
        "license_days": 31,
        "description": "1개월 단위로 YOONBOT을 사용합니다.",
    },
    "yearly": {
        "code": "yearly",
        "name": "Yearly",
        "amount_krw": 990000,
        "license_days": 365,
        "description": "12개월 라이선스를 한 번에 발급합니다.",
    },
}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def _secret(name: str) -> bytes:
    # Fail-closed: no predictable dev fallback secret.
    raw = os.getenv(name) or os.getenv("CODE_SECRET_KEY") or ""
    if not raw:
        raise RuntimeError(f"{name} 또는 CODE_SECRET_KEY가 설정되지 않았습니다.")
    return raw.encode("utf-8")


def _hmac(name: str, value: str) -> str:
    return hmac.new(_secret(name), value.encode("utf-8"), hashlib.sha256).hexdigest()


def _payment_key_fingerprint(payment_key: str) -> str:
    """HMAC fingerprint of the Toss paymentKey — the raw key is never persisted,
    returned, or logged. Fail-closed: requires CODE_SECRET_KEY.
    Same pattern as the education payment flow."""
    secret = os.getenv("CODE_SECRET_KEY", "")
    if not secret:
        raise RuntimeError("온라인 결제 설정이 완료되지 않았습니다.")
    digest = hmac.new(secret.encode("utf-8"), f"yoonbot-payment:{payment_key}".encode("utf-8"), hashlib.sha256).hexdigest()
    return f"toss:{digest[:48]}"


def _normalize_email(value: str | None) -> str:
    return (value or "").strip().lower()


def _normalize_phone(value: str | None) -> str:
    return re.sub(r"\D", "", value or "")


def _mask_email(email: str) -> str:
    if "@" not in email:
        return ""
    local, domain = email.split("@", 1)
    visible = local[:2] if len(local) >= 2 else local[:1]
    return f"{visible}{'*' * max(3, len(local) - len(visible))}@{domain}"


def _mask_phone(phone: str) -> str:
    if not phone:
        return ""
    if len(phone) < 7:
        return f"{phone[:3]}****"
    return f"{phone[:3]}-{'*' * max(3, len(phone) - 7)}-{phone[-4:]}"


def _plan(plan_code: str) -> dict:
    plan = PLANS.get((plan_code or "").strip().lower())
    if not plan:
        raise ValueError("지원하지 않는 YOONBOT 플랜입니다.")
    return plan


def _toss_ready() -> bool:
    config = get_toss_payment_config()
    return (
        config["provider"] == "toss_payments"
        and config["client_key_set"]
        and config["secret_key_set"]
    )


def products() -> dict:
    ready = _toss_ready()
    return {
        "product": {
            "code": PRODUCT_CODE,
            "name": "YOONBOT",
            "payment_mode": "toss_payments" if ready else "manual_bank_transfer",
            "auto_charge": ready,
        },
        "plans": list(PLANS.values()),
    }


def _payment_ref(order_id: str) -> str:
    return f"YB-{order_id.replace('-', '')[:8].upper()}"


def _row_to_public(row: Any) -> dict | None:
    if not row:
        return None
    data = dict(row)
    final_amount = int(data["amount_krw"] or 0)
    original_amount = int(data["original_amount_krw"] or 0) if data.get("original_amount_krw") is not None else final_amount
    discount_amount = int(data.get("discount_amount_krw") or 0)
    return {
        "id": data["id"],
        "buyer_name": data["buyer_name"],
        "buyer_email_masked": data.get("buyer_email_masked") or "",
        "buyer_phone_masked": data.get("buyer_phone_masked") or "",
        "product_code": data.get("product_code") or PRODUCT_CODE,
        "plan_code": data["plan_code"],
        "amount_krw": final_amount,
        "original_amount_krw": original_amount,
        "discount_code": data.get("discount_code") or None,
        "discount_label": data.get("discount_label") or None,
        "discount_amount_krw": discount_amount,
        "status": data["status"],
        "payment_provider": data.get("payment_provider") or "manual_bank_transfer",
        "payment_ref": data.get("payment_ref") or "",
        "member_id": data.get("member_id"),
        "license_id": data.get("license_id"),
        "license_key_hint": data.get("license_key_hint"),
        "license_status": data.get("license_status"),
        "note": data.get("note"),
        "customer_message": data.get("customer_message"),
        "paid_at": data.get("paid_at"),
        "canceled_at": data.get("canceled_at"),
        "refunded_at": data.get("refunded_at"),
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
    }


def _select_orders(where: str = "", params: list[Any] | None = None) -> list[dict]:
    clause = f"WHERE {where}" if where else ""
    conn = get_conn()
    try:
        rows = conn.execute(
            f"""
            SELECT o.*, l.license_key_hint, l.status AS license_status
            FROM orders o
            LEFT JOIN licenses l ON l.id=o.license_id
            {clause}
            ORDER BY o.created_at DESC
            """,
            params or [],
        ).fetchall()
        return [_row_to_public(row) for row in rows]
    finally:
        conn.close()


def get_order(order_id: str) -> dict | None:
    rows = _select_orders("o.id=?", [order_id])
    return rows[0] if rows else None


def get_order_by_toss_order_id(toss_order_id: str) -> dict | None:
    rows = _select_orders("o.toss_order_id=?", [toss_order_id])
    return rows[0] if rows else None


def list_orders(status: str | None = None, plan_code: str | None = None) -> list[dict]:
    clauses = []
    params: list[Any] = []
    if status:
        clauses.append("o.status=?")
        params.append(status)
    if plan_code:
        clauses.append("o.plan_code=?")
        params.append(plan_code)
    return _select_orders(" AND ".join(clauses), params)


def order_summary() -> dict:
    conn = get_conn()
    try:
        rows = conn.execute("SELECT status, COUNT(*) AS count FROM orders GROUP BY status").fetchall()
        counts = {row["status"]: row["count"] for row in rows}
        return {
            "total": sum(counts.values()),
            "payment_pending": counts.get("payment_pending", 0),
            "paid": counts.get("paid", 0),
            "license_issued": counts.get("license_issued", 0),
            "canceled": counts.get("canceled", 0),
            "refunded": counts.get("refunded", 0),
        }
    finally:
        conn.close()


def _normalize_discount_code(code: str | None) -> str:
    """Trim and uppercase discount code. Validation happens against the full value."""
    if not code:
        return ""
    return code.strip().upper()


def _validate_and_apply_discount(
    plan_code: str,
    original_amount: int,
    code_raw: str | None,
    conn: "sqlite3.Connection",
    now_iso: str,
) -> tuple[int, int, str | None, str | None]:
    """Validate discount code and compute final amount.

    Returns (final_amount, discount_amount, code_normalized, label).
    Raises ValueError with user-facing message if invalid.
    Atomically increments redeemed_count if valid (caller must commit).
    """
    import sqlite3  # local to avoid top-level cycle issues

    code = _normalize_discount_code(code_raw)
    if not code:
        return original_amount, 0, None, None
    if not _DISCOUNT_CODE_RE.match(code):
        raise ValueError("할인 코드 형식이 올바르지 않습니다.")

    row = conn.execute(
        "SELECT * FROM yoonbot_discount_codes WHERE code=?",
        (code,),
    ).fetchone()
    if not row:
        raise ValueError("유효하지 않은 할인 코드입니다.")
    row = dict(row)

    if not row.get("enabled", 1):
        raise ValueError("사용 중지된 할인 코드입니다.")
    if row.get("starts_at") and now_iso < row["starts_at"]:
        raise ValueError("아직 사용 기간이 시작되지 않은 할인 코드입니다.")
    if row.get("expires_at") and now_iso > row["expires_at"]:
        raise ValueError("만료된 할인 코드입니다.")
    if row.get("plan_code") and row["plan_code"] != plan_code:
        raise ValueError("이 플랜에는 적용할 수 없는 할인 코드입니다.")

    max_red = row.get("max_redemptions")
    redeemed = int(row.get("redeemed_count") or 0)
    if max_red is not None and max_red > 0 and redeemed >= max_red:
        raise ValueError("이미 사용 횟수가 소진된 할인 코드입니다.")

    dtype = (row.get("discount_type") or "").strip().lower()
    dvalue = int(row.get("discount_value") or 0)
    label = (row.get("label") or code).strip()[:120]

    if dtype == "percent":
        pct = max(1, min(100, dvalue))
        discount_amount = int(original_amount * pct / 100)
    elif dtype == "amount":
        discount_amount = min(dvalue, original_amount)
    elif dtype == "override_amount":
        discount_amount = max(0, original_amount - dvalue)
    else:
        raise ValueError("지원하지 않는 할인 유형입니다.")

    final_amount = max(0, original_amount - discount_amount)

    cursor = conn.execute(
        """
        UPDATE yoonbot_discount_codes
        SET redeemed_count=redeemed_count+1, updated_at=?
        WHERE code=?
          AND enabled=1
          AND (max_redemptions IS NULL OR max_redemptions <= 0 OR redeemed_count < max_redemptions)
        """,
        (now_iso, code),
    )
    if cursor.rowcount != 1:
        raise ValueError("이미 사용 횟수가 소진된 할인 코드입니다.")
    return final_amount, discount_amount, code, label


def create_order(
    *,
    buyer_name: str,
    buyer_email: str | None = None,
    buyer_phone: str | None = None,
    product_code: str = PRODUCT_CODE,
    plan_code: str = "monthly",
    customer_message: str | None = None,
    consent_privacy: bool = False,
    consent_terms: bool = False,
    discount_code: str | None = None,
) -> dict:
    if (product_code or PRODUCT_CODE).strip().lower() != PRODUCT_CODE:
        raise ValueError("지원하지 않는 상품입니다.")
    plan = _plan(plan_code)
    name = (buyer_name or "").strip()[:80]
    if not name:
        raise ValueError("구매자 이름을 입력하세요.")
    email = _normalize_email(buyer_email)
    phone = _normalize_phone(buyer_phone)
    if not email and not phone:
        raise ValueError("연락 가능한 이메일 또는 전화번호가 필요합니다.")
    if not consent_privacy or not consent_terms:
        raise ValueError("개인정보 수집과 결제 안내에 동의해야 합니다.")

    created = _iso(_now())
    order_id = str(uuid.uuid4())
    toss_order_id = generate_toss_order_id(order_id)
    original_amount = plan["amount_krw"]
    conn = get_conn()
    try:
        final_amount, discount_amount, d_code, d_label = _validate_and_apply_discount(
            plan["code"], original_amount, discount_code, conn, created
        )
        conn.execute(
            """
            INSERT INTO orders (
                id, buyer_name, buyer_email_hash, buyer_email_masked,
                buyer_phone_hash, buyer_phone_masked, product_code, plan_code,
                amount_krw, original_amount_krw, discount_code, discount_label,
                discount_amount_krw, status, payment_provider, payment_ref,
                toss_order_id, customer_message, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'payment_pending', 'manual_bank_transfer', ?, ?, ?, ?, ?)
            """,
            (
                order_id,
                name,
                _hmac("EMAIL_SECRET_KEY", f"order-email:{email}") if email else None,
                _mask_email(email),
                _hmac("PHONE_SECRET_KEY", f"order-phone:{phone}") if phone else None,
                _mask_phone(phone),
                PRODUCT_CODE,
                plan["code"],
                final_amount,
                original_amount,
                d_code,
                d_label,
                discount_amount,
                _payment_ref(order_id),
                toss_order_id,
                (customer_message or "").strip()[:1000] or None,
                created,
                created,
            ),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return {"ok": True, "data": get_order(order_id), "payment": manual_payment_payload(order_id)}


def manual_payment_payload(order_id: str | None = None) -> dict:
    return {
        "mode": "manual_bank_transfer",
        "auto_charge": False,
        "payment_ref": _payment_ref(order_id) if order_id else "",
        "message": "관리자가 구매 내용을 확인한 뒤 입금 안내와 라이선스 발급을 수동으로 진행합니다.",
    }


# ── Toss Payments ────────────────────────────────────────────────────────────

def generate_toss_order_id(order_id: str) -> str:
    """Convert internal UUID order_id to a Toss-compatible orderId.

    Toss orderId: 6-64 chars, letters/digits/-/_ only.
    Format: yb-{uuid without dashes, truncated to 30 chars} → max 33 chars, always valid.
    """
    sanitized = re.sub(r"[^A-Za-z0-9]", "", order_id)[:30]
    return f"yb-{sanitized}"


def get_toss_payment_config() -> dict:
    """Read Toss Payments configuration from environment variables.

    Returns a dict with keys: provider, client_key_set, secret_key_set, base_url.
    Never returns raw key values — only boolean indicators for the secret key.
    """
    provider = os.getenv("YOONBOT_PAYMENT_PROVIDER", "manual_bank_transfer")
    client_key = os.getenv("TOSS_PAYMENTS_CLIENT_KEY", "")
    secret_key = os.getenv("TOSS_PAYMENTS_SECRET_KEY", "")
    base_url = os.getenv("YOONBOT_PUBLIC_BASE_URL", "https://apply.arsen-ai.com")
    return {
        "provider": provider,
        "client_key": client_key,           # safe: client key is browser-public
        "client_key_set": bool(client_key),
        "secret_key_set": bool(secret_key),
        "base_url": base_url,
    }


def build_toss_payment_payload(order: dict) -> dict:
    """Build a browser-safe Toss Payments payload for the frontend SDK.

    Never includes the secret key. Returns mode=toss_payments when configured,
    falls back to manual_bank_transfer otherwise.
    """
    config = get_toss_payment_config()
    if (
        config["provider"] != "toss_payments"
        or not config["client_key_set"]
        or not config["secret_key_set"]
    ):
        if config["provider"] == "toss_payments":
            payload = manual_payment_payload(order.get("id"))
            payload["message"] = "온라인 결제 설정 확인 중이라 수동 결제 안내로 진행합니다."
            return payload
        return manual_payment_payload(order.get("id"))

    toss_order_id = generate_toss_order_id(order["id"])
    base_url = config["base_url"].rstrip("/")
    return {
        "mode": "toss_payments",
        "auto_charge": True,
        "client_key": config["client_key"],
        "toss_order_id": toss_order_id,
        "order_name": f"YOONBOT {order.get('plan_code', 'monthly').capitalize()} 라이선스",
        "amount": {"value": int(order.get("amount_krw") or 0), "currency": "KRW"},
        "success_url": f"{base_url}/frontend/yoonbot.html?payment=success",
        "fail_url": f"{base_url}/frontend/yoonbot.html?payment=fail",
        "customer_name": order.get("buyer_name", ""),
        "customer_email": "",   # not stored in plain form
    }


class TossConfirmClient:
    """Thin HTTP client for the Toss Payments confirm endpoint.

    Designed so tests can inject a stub via the confirm_client parameter
    in confirm_toss_payment() without making real network calls.
    """

    def confirm(self, payment_key: str, order_id: str, amount: int) -> dict:
        """Call Toss confirm endpoint. Returns parsed JSON or raises on failure."""
        import urllib.request
        import urllib.error
        import json as _json

        secret_key = os.getenv("TOSS_PAYMENTS_SECRET_KEY", "")
        if not secret_key:
            raise RuntimeError("TOSS_PAYMENTS_SECRET_KEY is not configured")

        credentials = base64.b64encode(f"{secret_key}:".encode()).decode()
        payload = _json.dumps({
            "paymentKey": payment_key,
            "orderId": order_id,
            "amount": amount,
        }).encode("utf-8")
        req = urllib.request.Request(
            TOSS_CONFIRM_URL,
            data=payload,
            headers={
                "Authorization": f"Basic {credentials}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return _json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            # Never surface or log the upstream response body — status code only.
            raise RuntimeError(f"Toss 결제 확인에 실패했습니다. (HTTP {exc.code})") from exc


def confirm_toss_payment(
    order_id: str,
    payment_key: str,
    client_amount: int,
    toss_order_id: str,
    confirm_client: TossConfirmClient | None = None,
) -> dict:
    """Validate and confirm a Toss Payments transaction.

    Validation steps (in order):
    1. Order exists → raises ValueError (404-worthy)
    2. Order is YOONBOT product → raises ValueError (400)
    3. Order status is payment_pending → raises ValueError if already done (400)
    4. toss_order_id matches server-computed value → raises ValueError (400)
    5. client_amount matches server-stored amount_krw → raises ValueError (400)
    6. TOSS_PAYMENTS_SECRET_KEY configured → raises RuntimeError (503)
    7. Calls Toss confirm endpoint via confirm_client
    8. Marks order paid on success

    Does NOT issue a license — that remains a manual admin step.
    """
    order = get_order(order_id)
    if not order:
        raise ValueError("주문을 찾을 수 없습니다.")

    if order.get("product_code", PRODUCT_CODE) != PRODUCT_CODE:
        raise ValueError("YOONBOT 주문이 아닙니다.")

    status = order.get("status", "")
    if status in {"canceled", "refunded"}:
        raise ValueError("취소/환불된 주문은 결제 확인할 수 없습니다.")
    fingerprint = _payment_key_fingerprint(payment_key)
    if status in {"paid", "license_issued"}:
        # Idempotent: already paid — same payment matches by fingerprint only
        stored_ref = order.get("payment_ref", "")
        if stored_ref and hmac.compare_digest(stored_ref, fingerprint):
            return {"ok": True, "data": order, "idempotent": True}
        raise ValueError("이미 결제 처리된 주문입니다.")

    expected_toss_order_id = generate_toss_order_id(order_id)
    if toss_order_id != expected_toss_order_id:
        raise ValueError("orderId가 서버 값과 일치하지 않습니다.")

    server_amount = int(order.get("amount_krw") or 0)
    if int(client_amount) != server_amount:
        raise ValueError("결제 금액이 주문 금액과 일치하지 않습니다.")

    if not os.getenv("TOSS_PAYMENTS_SECRET_KEY", ""):
        raise RuntimeError("온라인 결제 설정이 완료되지 않았습니다.")

    client = confirm_client if confirm_client is not None else TossConfirmClient()
    toss_response = client.confirm(payment_key, toss_order_id, server_amount)

    toss_status = (toss_response or {}).get("status", "")
    if toss_status and toss_status != "DONE":
        raise ValueError("Toss 결제 상태가 완료가 아닙니다.")
    toss_total = (toss_response or {}).get("totalAmount")
    if toss_total is not None and int(toss_total) != server_amount:
        raise ValueError("Toss 응답 금액이 주문 금액과 일치하지 않습니다.")

    result = mark_paid(
        order_id,
        payment_provider="toss_payments",
        payment_ref=fingerprint,
        note=f"toss_confirm:{toss_order_id}",
    )
    return result


def mark_paid(order_id: str, *, payment_provider: str = "manual_bank_transfer", payment_ref: str | None = None, note: str | None = None) -> dict:
    order = get_order(order_id)
    if not order:
        raise ValueError("주문을 찾을 수 없습니다.")
    if order["status"] in {"canceled", "refunded"}:
        raise ValueError("취소/환불된 주문은 결제 확인할 수 없습니다.")
    timestamp = _iso(_now())
    next_status = "license_issued" if order.get("license_id") else "paid"
    conn = get_conn()
    try:
        conn.execute(
            """
            UPDATE orders
            SET status=?, payment_provider=?, payment_ref=COALESCE(?, payment_ref),
                note=COALESCE(?, note), paid_at=COALESCE(paid_at, ?), updated_at=?
            WHERE id=?
            """,
            (
                next_status,
                (payment_provider or "manual_bank_transfer").strip()[:80],
                (payment_ref or "").strip()[:120] or None,
                (note or "").strip()[:1000] or None,
                timestamp,
                timestamp,
                order_id,
            ),
        )
        conn.commit()
    finally:
        conn.close()
    return {"ok": True, "data": get_order(order_id)}


def cancel_order(order_id: str, *, note: str | None = None) -> dict:
    return _terminal_order_state(order_id, "canceled", "canceled_at", note)


def refund_order(order_id: str, *, note: str | None = None) -> dict:
    return _terminal_order_state(order_id, "refunded", "refunded_at", note)


def _terminal_order_state(order_id: str, status: str, timestamp_column: str, note: str | None) -> dict:
    order = get_order(order_id)
    if not order:
        raise ValueError("주문을 찾을 수 없습니다.")
    if order.get("license_id") and status == "canceled":
        raise ValueError("이미 라이선스가 발급된 주문은 취소 대신 환불 메모로 처리하세요.")
    timestamp = _iso(_now())
    conn = get_conn()
    try:
        conn.execute(
            f"UPDATE orders SET status=?, note=COALESCE(?, note), {timestamp_column}=?, updated_at=? WHERE id=?",
            (status, (note or "").strip()[:1000] or None, timestamp, timestamp, order_id),
        )
        conn.commit()
    finally:
        conn.close()
    return {"ok": True, "data": get_order(order_id)}


def issue_license(order_id: str) -> dict:
    order = get_order(order_id)
    if not order:
        raise ValueError("주문을 찾을 수 없습니다.")
    if order.get("license_id"):
        raise ValueError("이미 라이선스가 발급된 주문입니다.")
    if order["status"] != "paid":
        raise ValueError("결제 확인된 주문에서만 라이선스를 발급할 수 있습니다.")

    plan = _plan(order["plan_code"])
    expires_at = _iso(_now() + timedelta(days=plan["license_days"]))
    created = create_license(
        member_id=order.get("member_id"),
        plan_code=order["plan_code"],
        expires_at=expires_at,
        max_devices=1,
        note=f"order:{order_id} buyer:{order['buyer_name']}",
    )
    timestamp = _iso(_now())
    conn = get_conn()
    try:
        conn.execute(
            "UPDATE orders SET status='license_issued', license_id=?, updated_at=? WHERE id=? AND license_id IS NULL",
            (created["license"]["id"], timestamp, order_id),
        )
        conn.commit()
    finally:
        conn.close()
    return {
        "ok": True,
        "license_key": created["license_key"],
        "license": created["license"],
        "order": get_order(order_id),
        "delivery": {
            "mode": "manual_copy",
            "auto_send": False,
            "message": "자동 발송은 하지 않습니다. 운영자가 안내문을 복사해 직접 전달하세요.",
        },
        "customer_message": customer_license_message(created["license_key"], created["license"]),
    }


# Customer license guidance points only at the public homepage; the old
# launcher ZIP direct link must never appear in customer-facing copy.
YOONBOT_CUSTOMER_DOWNLOAD_PAGE = "https://arsen-ai.com/yoonbot"


def customer_license_message(license_key: str, license_item: dict) -> str:
    return "\n".join(
        [
            "[YOONBOT 라이선스 안내]",
            f"라이선스 키: {license_key}",
            f"만료일: {license_item.get('expires_at')}",
            "",
            "▶ 프로그램 다운로드",
            f"  {YOONBOT_CUSTOMER_DOWNLOAD_PAGE}",
            "  공식 홈페이지의 다운로드 버튼은 공개 릴리스가 준비된 경우에만 활성화됩니다.",
            "",
            "▶ 설치 방법",
            "  1. 위 공식 홈페이지에서 Windows 설치 파일을 내려받아 실행하세요.",
            "  2. 설치가 끝나면 YOONBOT을 실행하고 라이선스 인증 창에 위 라이선스 키를 입력하세요.",
            "  3. 처음 등록한 PC에 기기가 묶입니다. PC 변경이 필요하면 운영자에게 기기 초기화를 요청해주세요.",
            "",
            "▶ 안내",
            "  현재 초기 파일럿/베타 단계로 기능이 순차적으로 확장되고 있습니다.",
            "  사용 중 문의사항이나 피드백은 카카오톡 채널 또는 운영자에게 직접 연락해 주세요.",
        ]
    )


# ── Discount code management ──────────────────────────────────────────────────

def _discount_row_to_public(row: Any) -> dict:
    data = dict(row)
    return {
        "id": data["id"],
        "code": data["code"],
        "label": data.get("label") or "",
        "plan_code": data.get("plan_code") or None,
        "discount_type": data["discount_type"],
        "discount_value": int(data["discount_value"] or 0),
        "max_redemptions": data.get("max_redemptions"),
        "redeemed_count": int(data.get("redeemed_count") or 0),
        "starts_at": data.get("starts_at"),
        "expires_at": data.get("expires_at"),
        "enabled": bool(data.get("enabled", 1)),
        "note": data.get("note") or "",
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
    }


def list_discount_codes(enabled_only: bool = False) -> list[dict]:
    conn = get_conn()
    try:
        where = "WHERE enabled=1" if enabled_only else ""
        rows = conn.execute(
            f"SELECT * FROM yoonbot_discount_codes {where} ORDER BY created_at DESC"
        ).fetchall()
        return [_discount_row_to_public(row) for row in rows]
    finally:
        conn.close()


ALLOWED_DISCOUNT_TYPES = {"percent", "amount", "override_amount"}


def create_discount_code(
    *,
    code: str,
    label: str | None = None,
    plan_code: str | None = None,
    discount_type: str = "percent",
    discount_value: int,
    max_redemptions: int | None = 1,
    starts_at: str | None = None,
    expires_at: str | None = None,
    note: str | None = None,
) -> dict:
    normalized = _normalize_discount_code(code)
    if not normalized or not _DISCOUNT_CODE_RE.match(normalized):
        raise ValueError("할인 코드는 영문 대소문자, 숫자, 하이픈(-), 언더스코어(_)만 허용됩니다.")
    if discount_type not in ALLOWED_DISCOUNT_TYPES:
        raise ValueError(f"지원하지 않는 할인 유형입니다. 허용: {', '.join(ALLOWED_DISCOUNT_TYPES)}")
    if discount_type == "percent" and not (1 <= discount_value <= 100):
        raise ValueError("퍼센트 할인은 1~100 사이여야 합니다.")
    if discount_value < 0:
        raise ValueError("할인 값은 0 이상이어야 합니다.")

    created = _iso(_now())
    code_id = str(uuid.uuid4())
    conn = get_conn()
    try:
        existing = conn.execute(
            "SELECT id FROM yoonbot_discount_codes WHERE code=?", (normalized,)
        ).fetchone()
        if existing:
            raise ValueError("이미 존재하는 할인 코드입니다.")
        conn.execute(
            """
            INSERT INTO yoonbot_discount_codes (
                id, code, label, plan_code, discount_type, discount_value,
                max_redemptions, redeemed_count, starts_at, expires_at,
                enabled, note, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, ?, 1, ?, ?, ?)
            """,
            (
                code_id,
                normalized,
                (label or "").strip()[:120] or None,
                (plan_code or "").strip().lower() or None,
                discount_type,
                int(discount_value),
                max_redemptions,
                (starts_at or "").strip() or None,
                (expires_at or "").strip() or None,
                (note or "").strip()[:500] or None,
                created,
                created,
            ),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM yoonbot_discount_codes WHERE id=?", (code_id,)
        ).fetchone()
        return _discount_row_to_public(row)
    finally:
        conn.close()


def disable_discount_code(code: str) -> dict:
    normalized = _normalize_discount_code(code)
    if not normalized:
        raise ValueError("할인 코드를 입력하세요.")
    conn = get_conn()
    try:
        row = conn.execute(
            "SELECT * FROM yoonbot_discount_codes WHERE code=?", (normalized,)
        ).fetchone()
        if not row:
            raise ValueError("할인 코드를 찾을 수 없습니다.")
        updated = _iso(_now())
        conn.execute(
            "UPDATE yoonbot_discount_codes SET enabled=0, updated_at=? WHERE code=?",
            (updated, normalized),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM yoonbot_discount_codes WHERE code=?", (normalized,)
        ).fetchone()
        return _discount_row_to_public(row)
    finally:
        conn.close()
