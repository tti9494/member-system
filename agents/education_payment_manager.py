"""Server-locked payment orders for paid education bookings.

This intentionally stays separate from YOONBOT license orders. It stores no
extra customer contact data and never stores a raw Toss payment key.
"""

from __future__ import annotations

import hashlib
import hmac
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Any

from db import get_conn
from agents.booking_manager import get_booking, refresh_session_counts
from agents.order_manager import TossConfirmClient, get_toss_payment_config


ACTIVE_BOOKING_STATUSES = {"requested", "payment_guide_sent", "payment_pending", "payment_confirmed"}
TERMINAL_ORDER_STATUSES = {"canceled", "refunded"}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _payment_ref(order_id: str) -> str:
    return f"ARSEN-{order_id.replace('-', '')[:8].upper()}"


def _toss_order_id(order_id: str) -> str:
    return f"ae-{re.sub(r'[^A-Za-z0-9]', '', order_id)[:30]}"


def _payment_key_fingerprint(payment_key: str) -> str:
    secret = (os.getenv("CODE_SECRET_KEY") or "local-education-payment-secret").encode("utf-8")
    digest = hmac.new(secret, payment_key.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"toss:{digest[:48]}"


def _public_order(row: Any) -> dict | None:
    if not row:
        return None
    data = dict(row)
    return {
        "id": data["id"],
        "booking_id": data["booking_id"],
        "amount_krw": int(data.get("amount_krw") or 0),
        "status": data.get("status") or "payment_pending",
        "payment_provider": data.get("payment_provider") or "manual_bank_transfer",
        "payment_reference": _payment_ref(data["id"]),
        "toss_order_id": data.get("toss_order_id") or _toss_order_id(data["id"]),
        "created_at": data.get("created_at") or "",
        "paid_at": data.get("paid_at") or None,
    }


def _get_order_row(order_id: str) -> dict | None:
    conn = get_conn()
    try:
        row = conn.execute("SELECT * FROM education_payment_orders WHERE id=?", (order_id,)).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_order(order_id: str) -> dict | None:
    return _public_order(_get_order_row(order_id))


def _get_booking_payment_data(booking_id: str, member_id: str) -> dict:
    conn = get_conn()
    try:
        row = conn.execute(
            """
            SELECT b.id, b.member_id, b.status, b.payment_status, b.payment_amount_krw,
                   s.title AS session_title, s.price_krw AS session_price_krw
            FROM bookings b
            LEFT JOIN sessions s ON s.id=b.session_id
            WHERE b.id=? AND b.member_id=?
            """,
            (booking_id, member_id),
        ).fetchone()
        if not row:
            raise ValueError("본인 예약을 찾을 수 없습니다.")
        data = dict(row)
    finally:
        conn.close()
    if data.get("status") not in ACTIVE_BOOKING_STATUSES and data.get("status") != "confirmed":
        raise ValueError("취소되었거나 처리할 수 없는 예약입니다.")
    if data.get("payment_status") == "paid":
        raise ValueError("이미 결제 확인된 예약입니다.")
    amount = int(data.get("payment_amount_krw") or data.get("session_price_krw") or 0)
    if amount <= 0 or data.get("payment_status") == "waived":
        raise ValueError("이 예약은 온라인 결제 대상이 아닙니다.")
    return data | {"amount_krw": amount}


def create_or_reuse_order(*, booking_id: str, member_id: str) -> dict:
    booking = _get_booking_payment_data(booking_id, member_id)
    conn = get_conn()
    try:
        existing = conn.execute(
            "SELECT * FROM education_payment_orders WHERE booking_id=? ORDER BY created_at DESC LIMIT 1",
            (booking_id,),
        ).fetchone()
        if existing:
            order = dict(existing)
            if order.get("status") == "paid":
                return {"ok": True, "data": _public_order(order), "already_paid": True}
            if order.get("status") not in TERMINAL_ORDER_STATUSES:
                return {"ok": True, "data": _public_order(order), "reused": True}
            raise ValueError("취소 또는 환불된 결제 주문은 운영자 확인 후 다시 진행할 수 있습니다.")

        order_id = str(uuid.uuid4())
        now = _now()
        conn.execute(
            """
            INSERT INTO education_payment_orders (
                id, booking_id, member_id, amount_krw, status, payment_provider,
                toss_order_id, created_at, updated_at
            ) VALUES (?, ?, ?, ?, 'payment_pending', 'manual_bank_transfer', ?, ?, ?)
            """,
            (order_id, booking_id, member_id, booking["amount_krw"], _toss_order_id(order_id), now, now),
        )
        conn.execute(
            """
            UPDATE bookings
            SET status=CASE WHEN status='requested' THEN 'payment_pending' ELSE status END,
                payment_status=CASE WHEN payment_status IN ('not_sent', 'pending') THEN 'pending' ELSE payment_status END,
                updated_at=?
            WHERE id=?
            """,
            (now, booking_id),
        )
        conn.commit()
        row = conn.execute("SELECT * FROM education_payment_orders WHERE id=?", (order_id,)).fetchone()
        return {"ok": True, "data": _public_order(row)}
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def build_payment_payload(order: dict, *, order_name: str) -> dict:
    config = get_toss_payment_config()
    if not (
        config.get("provider") == "toss_payments"
        and config.get("client_key_set")
        and config.get("secret_key_set")
    ):
        return {
            "mode": "manual_bank_transfer",
            "auto_charge": False,
            "payment_reference": order["payment_reference"],
            "amount_krw": order["amount_krw"],
            "message": "온라인 결제 설정 확인 중입니다. 아래 입금 안내 또는 운영자 안내에 따라 진행하세요.",
        }
    base_url = str(config.get("base_url") or "").rstrip("/")
    success = f"{base_url}/frontend/status.html?payment=success&education_order_id={order['id']}"
    fail = f"{base_url}/frontend/status.html?payment=fail&education_order_id={order['id']}"
    return {
        "mode": "toss_payments",
        "auto_charge": True,
        "client_key": config["client_key"],
        "toss_order_id": order["toss_order_id"],
        "order_name": (order_name or "ARSEN 유료 강의")[:100],
        "amount": {"value": int(order["amount_krw"]), "currency": "KRW"},
        "success_url": success,
        "fail_url": fail,
    }


def confirm_toss_payment(
    *,
    order_id: str,
    payment_key: str,
    client_amount: int,
    toss_order_id: str,
    confirm_client: TossConfirmClient | None = None,
) -> dict:
    order = _get_order_row(order_id)
    if not order:
        raise ValueError("결제 주문을 찾을 수 없습니다.")
    if order.get("status") in TERMINAL_ORDER_STATUSES:
        raise ValueError("취소 또는 환불된 주문은 결제 확인할 수 없습니다.")
    fingerprint = _payment_key_fingerprint(payment_key)
    if order.get("status") == "paid":
        if hmac.compare_digest(str(order.get("payment_ref") or ""), fingerprint):
            return {"ok": True, "data": _public_order(order), "idempotent": True}
        raise ValueError("이미 결제 처리된 주문입니다.")
    if toss_order_id != order.get("toss_order_id"):
        raise ValueError("orderId가 서버 값과 일치하지 않습니다.")
    server_amount = int(order.get("amount_krw") or 0)
    if int(client_amount) != server_amount:
        raise ValueError("결제 금액이 주문 금액과 일치하지 않습니다.")
    if not os.getenv("TOSS_PAYMENTS_SECRET_KEY", ""):
        raise RuntimeError("온라인 결제 설정이 완료되지 않았습니다.")

    client = confirm_client if confirm_client is not None else TossConfirmClient()
    toss_response = client.confirm(payment_key, toss_order_id, server_amount)
    if (toss_response or {}).get("status") not in {"", "DONE"}:
        raise ValueError("결제 승인 상태를 확인하지 못했습니다.")
    total_amount = (toss_response or {}).get("totalAmount")
    if total_amount is not None and int(total_amount) != server_amount:
        raise ValueError("결제 승인 금액이 주문 금액과 일치하지 않습니다.")

    now = _now()
    conn = get_conn()
    try:
        changed = conn.execute(
            """
            UPDATE education_payment_orders
            SET status='paid', payment_provider='toss_payments', payment_ref=?, paid_at=?, updated_at=?
            WHERE id=? AND status='payment_pending'
            """,
            (fingerprint, now, now, order_id),
        ).rowcount
        if changed != 1:
            conn.rollback()
            refreshed = _get_order_row(order_id)
            if refreshed and refreshed.get("status") == "paid" and hmac.compare_digest(str(refreshed.get("payment_ref") or ""), fingerprint):
                return {"ok": True, "data": _public_order(refreshed), "idempotent": True}
            raise ValueError("결제 주문 상태가 변경되어 다시 확인이 필요합니다.")
        conn.execute(
            """
            UPDATE bookings
            SET status='confirmed', payment_status='paid', payment_note='온라인 결제 확인',
                confirmed_at=COALESCE(confirmed_at, ?), updated_at=?
            WHERE id=?
            """,
            (now, now, order["booking_id"]),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    refreshed_booking = get_booking(order["booking_id"])
    refresh_session_counts((refreshed_booking or {}).get("session_id"))
    return {"ok": True, "data": get_order(order_id)}
