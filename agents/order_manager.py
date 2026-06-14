import hashlib
import hmac
import os
import re
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from db import get_conn
from agents.license_manager import create_license


PRODUCT_CODE = "yoonbot"
ORDER_STATUSES = {"payment_pending", "paid", "license_issued", "canceled", "refunded"}
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
        "description": "1개월 단위로 YoonBot을 사용합니다.",
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
    raw = os.getenv(name) or os.getenv("CODE_SECRET_KEY") or "local-order-dev-secret"
    return raw.encode("utf-8")


def _hmac(name: str, value: str) -> str:
    return hmac.new(_secret(name), value.encode("utf-8"), hashlib.sha256).hexdigest()


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
        raise ValueError("지원하지 않는 YoonBot 플랜입니다.")
    return plan


def products() -> dict:
    return {
        "product": {
            "code": PRODUCT_CODE,
            "name": "YoonBot",
            "payment_mode": "manual_bank_transfer",
            "auto_charge": False,
        },
        "plans": list(PLANS.values()),
    }


def _payment_ref(order_id: str) -> str:
    return f"YB-{order_id.replace('-', '')[:8].upper()}"


def _row_to_public(row: Any) -> dict | None:
    if not row:
        return None
    data = dict(row)
    return {
        "id": data["id"],
        "buyer_name": data["buyer_name"],
        "buyer_email_masked": data.get("buyer_email_masked") or "",
        "buyer_phone_masked": data.get("buyer_phone_masked") or "",
        "product_code": data.get("product_code") or PRODUCT_CODE,
        "plan_code": data["plan_code"],
        "amount_krw": int(data["amount_krw"] or 0),
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
    conn = get_conn()
    try:
        conn.execute(
            """
            INSERT INTO orders (
                id, buyer_name, buyer_email_hash, buyer_email_masked,
                buyer_phone_hash, buyer_phone_masked, product_code, plan_code,
                amount_krw, status, payment_provider, payment_ref,
                customer_message, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'payment_pending', 'manual_bank_transfer', ?, ?, ?, ?)
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
                plan["amount_krw"],
                _payment_ref(order_id),
                (customer_message or "").strip()[:1000] or None,
                created,
                created,
            ),
        )
        conn.commit()
    finally:
        conn.close()
    return {"ok": True, "data": get_order(order_id), "payment": manual_payment_payload(order_id)}


def manual_payment_payload(order_id: str | None = None) -> dict:
    return {
        "mode": "manual_bank_transfer",
        "auto_charge": False,
        "payment_ref": _payment_ref(order_id) if order_id else "",
        "message": "관리자가 신청 내용을 확인한 뒤 입금 안내와 라이선스 발급을 수동으로 진행합니다.",
    }


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


def customer_license_message(license_key: str, license_item: dict) -> str:
    return "\n".join(
        [
            "[YoonBot 라이선스 안내]",
            f"라이선스 키: {license_key}",
            f"만료일: {license_item.get('expires_at')}",
            "Windows YoonBot 실행 후 라이선스 인증 창에 위 키를 입력하세요.",
            "처음 등록한 PC에 기기가 묶입니다. PC 변경이 필요하면 운영자에게 기기 초기화를 요청해주세요.",
        ]
    )
