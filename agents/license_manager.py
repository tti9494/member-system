import hashlib
import hmac
import os
import re
import secrets
import string
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from db import get_conn


LICENSE_DEFAULT_DAYS = int(os.getenv("LICENSE_DEFAULT_DAYS", "365"))
LICENSE_GRACE_SECONDS = int(os.getenv("LICENSE_GRACE_SECONDS", str(3 * 24 * 60 * 60)))
LICENSE_TOKEN_DAYS = int(os.getenv("LICENSE_TOKEN_DAYS", "90"))
LICENSE_KEY_PREFIX = os.getenv("LICENSE_KEY_PREFIX", "YB").strip().upper() or "YB"
LICENSE_KEY_ALPHABET = os.getenv(
    "LICENSE_KEY_ALPHABET",
    "ABCDEFGHJKLMNPQRSTUVWXYZ23456789",
)
# Trust-boundary bounds shared with cloudflare/src/worker.js (worker parity).
LICENSE_KEY_MAX_LEN = 64
LICENSE_HWID_MAX_LEN = 128
LICENSE_TOKEN_MAX_LEN = 128
LICENSE_APP_VERSION_MAX_LEN = 40
LICENSE_PLATFORM_MAX_LEN = 80
LICENSE_DEVICE_NAME_MAX_LEN = 120
# Server-side abuse limits keyed on license_events.ip_hash. Only blocked
# attempts count, so a healthy client verifying on schedule is never limited.
LICENSE_RATE_WINDOW_SECONDS = int(os.getenv("LICENSE_RATE_WINDOW_SECONDS", "600"))
LICENSE_ACTIVATE_RATE_MAX = int(os.getenv("LICENSE_ACTIVATE_RATE_MAX", "10"))
LICENSE_VERIFY_FAIL_RATE_MAX = int(os.getenv("LICENSE_VERIFY_FAIL_RATE_MAX", "20"))


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _secret() -> bytes:
    # Fail-closed: no predictable dev fallback secret.
    raw = os.getenv("LICENSE_SECRET_KEY") or os.getenv("CODE_SECRET_KEY") or ""
    if not raw:
        raise RuntimeError("LICENSE_SECRET_KEY 또는 CODE_SECRET_KEY가 설정되지 않았습니다.")
    return raw.encode("utf-8")


def _canonical(value: str) -> str:
    return "".join(ch for ch in (value or "").upper() if ch.isalnum())


def _hash_value(kind: str, value: str) -> str:
    canonical = _canonical(value)
    return hmac.new(_secret(), f"{kind}:{canonical}".encode("utf-8"), hashlib.sha256).hexdigest()


def _hash_loose(kind: str, value: str | None) -> str | None:
    if not value:
        return None
    return hmac.new(_secret(), f"{kind}:{value}".encode("utf-8"), hashlib.sha256).hexdigest()


def _license_hint(license_key: str) -> str:
    parts = license_key.split("-")
    tail = parts[-1] if parts else _canonical(license_key)[-4:]
    return f"{LICENSE_KEY_PREFIX}-****-****-****-{tail[-4:]}"


def generate_license_key() -> str:
    groups = [
        "".join(secrets.choice(LICENSE_KEY_ALPHABET) for _ in range(4))
        for _ in range(4)
    ]
    return "-".join([LICENSE_KEY_PREFIX, *groups])


def _new_token() -> str:
    return secrets.token_urlsafe(32)


def _version_tuple(version: str | None) -> tuple[int, ...]:
    if not version:
        return ()
    parts = re.findall(r"\d+", version)
    return tuple(int(part) for part in parts[:4])


def _is_version_blocked(app_version: str | None, min_version: str | None) -> bool:
    if not min_version or not app_version:
        return False
    app = _version_tuple(app_version)
    minimum = _version_tuple(min_version)
    return bool(app and minimum and app < minimum)


def _safe_user_agent(user_agent: str | None) -> str | None:
    if not user_agent:
        return None
    return user_agent[:200]


def _row_to_public(row: Any) -> dict:
    data = dict(row)
    return {
        "id": data["id"],
        "member_id": data.get("member_id"),
        "plan_code": data["plan_code"],
        "status": data["status"],
        "license_key_hint": data["license_key_hint"],
        "max_devices": data["max_devices"],
        "bound_device": bool(data.get("bound_hwid_hash")),
        "app_min_version": data.get("app_min_version"),
        "expires_at": data["expires_at"],
        "activated_at": data.get("activated_at"),
        "last_verified_at": data.get("last_verified_at"),
        "revoked_at": data.get("revoked_at"),
        "revoke_reason": data.get("revoke_reason"),
        "note": data.get("note"),
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
    }


def _event(
    conn,
    event_type: str,
    result: str,
    *,
    license_id: str | None = None,
    activation_id: str | None = None,
    reason_code: str | None = None,
    ip: str | None = None,
    user_agent: str | None = None,
    app_version: str | None = None,
    platform: str | None = None,
) -> None:
    conn.execute(
        """
        INSERT INTO license_events (
            id, license_id, activation_id, event_type, result, reason_code,
            ip_hash, user_agent, app_version, platform, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            str(uuid.uuid4()),
            license_id,
            activation_id,
            event_type,
            result,
            reason_code,
            _hash_loose("ip", ip),
            _safe_user_agent(user_agent),
            app_version,
            platform,
            _iso(_now()),
        ),
    )


def _failure(code: str, message: str, status: str = "invalid") -> dict:
    return {"ok": False, "status": status, "code": code, "message": message}


def _bounded(value: str | None, max_len: int) -> str | None:
    """Strip + bound an untrusted field. None = empty, overlong, or control chars."""
    text = (value or "").strip()
    if not text or len(text) > max_len:
        return None
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return None
    return text


def _rate_limit_failure() -> dict:
    # One generic error for every limited request, on both endpoints.
    return _failure("RATE_LIMITED", "요청이 제한되었습니다. 잠시 후 다시 시도해 주세요.")


def _is_rate_limited(conn, ip_hash: str | None, event_type: str, max_count: int) -> bool:
    if not ip_hash or max_count <= 0:
        return False
    window_start = _iso(_now() - timedelta(seconds=LICENSE_RATE_WINDOW_SECONDS))
    row = conn.execute(
        """
        SELECT COUNT(*) AS count FROM license_events
        WHERE ip_hash=? AND event_type=? AND result='blocked' AND created_at>=?
        """,
        (ip_hash, event_type, window_start),
    ).fetchone()
    return int(row["count"] if row else 0) >= max_count


def create_license(
    *,
    member_id: str | None = None,
    plan_code: str = "basic",
    expires_at: str | None = None,
    max_devices: int = 1,
    app_min_version: str | None = None,
    note: str | None = None,
) -> dict:
    now = _now()
    expires_dt = _parse_dt(expires_at) or now + timedelta(days=LICENSE_DEFAULT_DAYS)
    max_devices = max(1, int(max_devices or 1))

    conn = get_conn()
    try:
        if member_id:
            member = conn.execute("SELECT id FROM members WHERE id=?", (member_id,)).fetchone()
            if not member:
                raise ValueError("존재하지 않는 member_id입니다.")

        for _ in range(10):
            license_key = generate_license_key()
            license_hash = _hash_value("license", license_key)
            try:
                license_id = str(uuid.uuid4())
                conn.execute(
                    """
                    INSERT INTO licenses (
                        id, member_id, license_key_hash, license_key_hint, plan_code,
                        status, max_devices, app_min_version, expires_at, note,
                        created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, 'unused', ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        license_id,
                        member_id,
                        license_hash,
                        _license_hint(license_key),
                        plan_code.strip() or "basic",
                        max_devices,
                        app_min_version.strip() if app_min_version else None,
                        _iso(expires_dt),
                        note.strip() if note else None,
                        _iso(now),
                        _iso(now),
                    ),
                )
                _event(conn, "license_created", "ok", license_id=license_id)
                conn.commit()
                row = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
                return {
                    "ok": True,
                    "license_key": license_key,
                    "license": _row_to_public(row),
                }
            except Exception as exc:
                if "UNIQUE" not in str(exc).upper():
                    raise
                conn.rollback()
        raise RuntimeError("라이선스 키 생성 충돌이 반복되었습니다.")
    finally:
        conn.close()


def list_licenses(status: str | None = None, member_id: str | None = None) -> list[dict]:
    where = []
    params: list[Any] = []
    if status:
        where.append("status=?")
        params.append(status)
    if member_id:
        where.append("member_id=?")
        params.append(member_id)
    clause = f"WHERE {' AND '.join(where)}" if where else ""
    conn = get_conn()
    try:
        rows = conn.execute(
            f"SELECT * FROM licenses {clause} ORDER BY created_at DESC",
            params,
        ).fetchall()
        return [_row_to_public(row) for row in rows]
    finally:
        conn.close()


def get_license(license_id: str) -> dict | None:
    conn = get_conn()
    try:
        row = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        return _row_to_public(row) if row else None
    finally:
        conn.close()


def license_summary() -> dict:
    conn = get_conn()
    try:
        rows = conn.execute("SELECT status, COUNT(*) AS count FROM licenses GROUP BY status").fetchall()
        counts = {row["status"]: row["count"] for row in rows}
        return {
            "total": sum(counts.values()),
            "unused": counts.get("unused", 0),
            "active": counts.get("active", 0),
            "expired": counts.get("expired", 0),
            "revoked": counts.get("revoked", 0),
        }
    finally:
        conn.close()


def activate_license(
    *,
    license_key: str,
    hwid: str,
    app_version: str | None = None,
    platform: str = "windows",
    device_name: str | None = None,
    client_ip: str | None = None,
    user_agent: str | None = None,
) -> dict:
    # Worker parity: reject empty/blank/overlong inputs before any hashing or DB access.
    license_key = _bounded(license_key, LICENSE_KEY_MAX_LEN)
    hwid = _bounded(hwid, LICENSE_HWID_MAX_LEN)
    if not license_key or not hwid:
        return _failure("INVALID_REQUEST", "라이선스 키와 HWID가 필요합니다.")
    raw_app_version = (app_version or "").strip()
    app_version = _bounded(raw_app_version, LICENSE_APP_VERSION_MAX_LEN) if raw_app_version else None
    raw_platform = (platform or "").strip()
    platform = _bounded(raw_platform, LICENSE_PLATFORM_MAX_LEN) if raw_platform else "windows"
    raw_device_name = (device_name or "").strip()
    device_name = _bounded(raw_device_name, LICENSE_DEVICE_NAME_MAX_LEN) if raw_device_name else None
    if (raw_app_version and app_version is None) or platform is None or (raw_device_name and device_name is None):
        return _failure("INVALID_REQUEST", "요청 값을 확인해 주세요.")
    now = _now()
    license_hash = _hash_value("license", license_key)
    hwid_hash = _hash_value("hwid", hwid)
    ip_hash = _hash_loose("ip", client_ip)
    conn = get_conn()
    try:
        conn.execute("BEGIN IMMEDIATE")
        if _is_rate_limited(conn, ip_hash, "license_activate", LICENSE_ACTIVATE_RATE_MAX):
            _event(
                conn,
                "license_activate",
                "blocked",
                reason_code="RATE_LIMITED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _rate_limit_failure()
        row = conn.execute("SELECT * FROM licenses WHERE license_key_hash=?", (license_hash,)).fetchone()
        if not row:
            _event(
                conn,
                "license_activate",
                "blocked",
                reason_code="LICENSE_NOT_FOUND",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("LICENSE_NOT_FOUND", "라이선스 키를 확인할 수 없습니다.")

        license_id = row["id"]
        expires_dt = _parse_dt(row["expires_at"])
        if expires_dt and expires_dt <= now:
            conn.execute(
                "UPDATE licenses SET status='expired', updated_at=? WHERE id=? AND status!='revoked'",
                (_iso(now), license_id),
            )
            _event(
                conn,
                "license_activate",
                "blocked",
                license_id=license_id,
                reason_code="LICENSE_EXPIRED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("LICENSE_EXPIRED", "만료된 라이선스입니다.", "expired")

        if row["status"] == "revoked":
            _event(
                conn,
                "license_activate",
                "blocked",
                license_id=license_id,
                reason_code="LICENSE_REVOKED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("LICENSE_REVOKED", "회수된 라이선스입니다.", "revoked")

        if _is_version_blocked(app_version, row["app_min_version"]):
            _event(
                conn,
                "license_activate",
                "blocked",
                license_id=license_id,
                reason_code="APP_VERSION_BLOCKED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("APP_VERSION_BLOCKED", "프로그램 업데이트가 필요합니다.", row["status"])

        bound_hwid = row["bound_hwid_hash"]
        if bound_hwid and bound_hwid != hwid_hash:
            _event(
                conn,
                "license_activate",
                "blocked",
                license_id=license_id,
                reason_code="HWID_MISMATCH",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("HWID_MISMATCH", "이미 다른 기기에 등록된 라이선스입니다.", row["status"])

        token = _new_token()
        token_hash = _hash_value("token", token)
        token_expires = now + timedelta(days=LICENSE_TOKEN_DAYS)
        if expires_dt and token_expires > expires_dt:
            token_expires = expires_dt

        conn.execute(
            """
            UPDATE license_activations
            SET status='revoked', revoked_at=?, updated_at=?
            WHERE license_id=? AND status='active'
            """,
            (_iso(now), _iso(now), license_id),
        )
        activation_id = str(uuid.uuid4())
        conn.execute(
            """
            INSERT INTO license_activations (
                id, license_id, token_hash, hwid_hash, platform, device_name,
                app_version, status, first_seen_at, last_seen_at, expires_at,
                created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, 'active', ?, ?, ?, ?, ?)
            """,
            (
                activation_id,
                license_id,
                token_hash,
                hwid_hash,
                platform or "windows",
                device_name[:120] if device_name else None,
                app_version,
                _iso(now),
                _iso(now),
                _iso(token_expires),
                _iso(now),
                _iso(now),
            ),
        )
        conn.execute(
            """
            UPDATE licenses
            SET status='active', bound_hwid_hash=?, activated_at=COALESCE(activated_at, ?),
                last_verified_at=?, updated_at=?
            WHERE id=?
            """,
            (hwid_hash, _iso(now), _iso(now), _iso(now), license_id),
        )
        _event(
            conn,
            "license_activate",
            "ok",
            license_id=license_id,
            activation_id=activation_id,
            ip=client_ip,
            user_agent=user_agent,
            app_version=app_version,
            platform=platform,
        )
        conn.commit()
        updated = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        return {
            "ok": True,
            "status": "active",
            "activation_token": token,
            "license": _row_to_public(updated),
            "server_time": _iso(now),
            "grace_seconds": LICENSE_GRACE_SECONDS,
        }
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def verify_license(
    *,
    activation_token: str,
    hwid: str,
    app_version: str | None = None,
    platform: str = "windows",
    client_ip: str | None = None,
    user_agent: str | None = None,
) -> dict:
    # Worker parity: reject empty/blank/overlong inputs before any hashing or DB access.
    activation_token = _bounded(activation_token, LICENSE_TOKEN_MAX_LEN)
    hwid = _bounded(hwid, LICENSE_HWID_MAX_LEN)
    if not activation_token:
        return _failure("INVALID_REQUEST", "인증 토큰이 필요합니다.")
    if not hwid:
        return _failure("INVALID_REQUEST", "HWID가 필요합니다.")
    raw_app_version = (app_version or "").strip()
    app_version = _bounded(raw_app_version, LICENSE_APP_VERSION_MAX_LEN) if raw_app_version else None
    raw_platform = (platform or "").strip()
    platform = _bounded(raw_platform, LICENSE_PLATFORM_MAX_LEN) if raw_platform else "windows"
    if (raw_app_version and app_version is None) or platform is None:
        return _failure("INVALID_REQUEST", "요청 값을 확인해 주세요.")
    now = _now()
    token_hash = _hash_value("token", activation_token)
    hwid_hash = _hash_value("hwid", hwid)
    ip_hash = _hash_loose("ip", client_ip)
    conn = get_conn()
    try:
        conn.execute("BEGIN IMMEDIATE")
        if _is_rate_limited(conn, ip_hash, "license_verify", LICENSE_VERIFY_FAIL_RATE_MAX):
            _event(
                conn,
                "license_verify",
                "blocked",
                reason_code="RATE_LIMITED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _rate_limit_failure()
        row = conn.execute(
            """
            SELECT
                a.id AS activation_id, a.hwid_hash AS activation_hwid_hash,
                a.status AS activation_status, a.expires_at AS activation_expires_at,
                l.*
            FROM license_activations a
            JOIN licenses l ON l.id = a.license_id
            WHERE a.token_hash=?
            """,
            (token_hash,),
        ).fetchone()
        if not row:
            _event(
                conn,
                "license_verify",
                "blocked",
                reason_code="TOKEN_NOT_FOUND",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("TOKEN_NOT_FOUND", "인증 토큰을 확인할 수 없습니다.")

        license_id = row["id"]
        activation_id = row["activation_id"]
        if row["activation_status"] != "active":
            _event(
                conn,
                "license_verify",
                "blocked",
                license_id=license_id,
                activation_id=activation_id,
                reason_code="TOKEN_REVOKED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("TOKEN_REVOKED", "인증 토큰이 회수되었습니다.")

        activation_expires = _parse_dt(row["activation_expires_at"])
        license_expires = _parse_dt(row["expires_at"])
        if activation_expires and activation_expires <= now:
            conn.execute(
                """
                UPDATE license_activations
                SET status='expired', updated_at=?
                WHERE id=?
                """,
                (_iso(now), activation_id),
            )
            _event(
                conn,
                "license_verify",
                "blocked",
                license_id=license_id,
                activation_id=activation_id,
                reason_code="TOKEN_EXPIRED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("TOKEN_EXPIRED", "인증 토큰이 만료되었습니다.", "expired")

        if license_expires and license_expires <= now:
            conn.execute(
                "UPDATE licenses SET status='expired', updated_at=? WHERE id=? AND status!='revoked'",
                (_iso(now), license_id),
            )
            _event(
                conn,
                "license_verify",
                "blocked",
                license_id=license_id,
                activation_id=activation_id,
                reason_code="LICENSE_EXPIRED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("LICENSE_EXPIRED", "만료된 라이선스입니다.", "expired")

        if row["status"] == "revoked":
            _event(
                conn,
                "license_verify",
                "blocked",
                license_id=license_id,
                activation_id=activation_id,
                reason_code="LICENSE_REVOKED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("LICENSE_REVOKED", "회수된 라이선스입니다.", "revoked")

        if row["activation_hwid_hash"] != hwid_hash or row["bound_hwid_hash"] != hwid_hash:
            _event(
                conn,
                "license_verify",
                "blocked",
                license_id=license_id,
                activation_id=activation_id,
                reason_code="HWID_MISMATCH",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("HWID_MISMATCH", "등록된 기기와 다릅니다.", row["status"])

        if _is_version_blocked(app_version, row["app_min_version"]):
            _event(
                conn,
                "license_verify",
                "blocked",
                license_id=license_id,
                activation_id=activation_id,
                reason_code="APP_VERSION_BLOCKED",
                ip=client_ip,
                user_agent=user_agent,
                app_version=app_version,
                platform=platform,
            )
            conn.commit()
            return _failure("APP_VERSION_BLOCKED", "프로그램 업데이트가 필요합니다.", row["status"])

        conn.execute(
            """
            UPDATE license_activations
            SET last_seen_at=?, app_version=?, platform=?, updated_at=?
            WHERE id=?
            """,
            (_iso(now), app_version, platform or "windows", _iso(now), activation_id),
        )
        conn.execute(
            "UPDATE licenses SET last_verified_at=?, updated_at=? WHERE id=?",
            (_iso(now), _iso(now), license_id),
        )
        _event(
            conn,
            "license_verify",
            "ok",
            license_id=license_id,
            activation_id=activation_id,
            ip=client_ip,
            user_agent=user_agent,
            app_version=app_version,
            platform=platform,
        )
        conn.commit()
        updated = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        return {
            "ok": True,
            "status": "active",
            "license": _row_to_public(updated),
            "server_time": _iso(now),
            "grace_seconds": LICENSE_GRACE_SECONDS,
        }
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def revoke_license(license_id: str, reason: str = "manual") -> dict:
    now = _now()
    conn = get_conn()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        if not row:
            return _failure("LICENSE_NOT_FOUND", "라이선스를 찾을 수 없습니다.")
        conn.execute(
            """
            UPDATE licenses
            SET status='revoked', revoked_at=?, revoke_reason=?, updated_at=?
            WHERE id=?
            """,
            (_iso(now), reason[:200], _iso(now), license_id),
        )
        conn.execute(
            """
            UPDATE license_activations
            SET status='revoked', revoked_at=?, updated_at=?
            WHERE license_id=? AND status='active'
            """,
            (_iso(now), _iso(now), license_id),
        )
        _event(conn, "license_revoked", "ok", license_id=license_id, reason_code=reason[:80])
        conn.commit()
        updated = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        return {"ok": True, "license": _row_to_public(updated)}
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def reset_license_device(license_id: str, reason: str = "manual") -> dict:
    now = _now()
    conn = get_conn()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        if not row:
            return _failure("LICENSE_NOT_FOUND", "라이선스를 찾을 수 없습니다.")
        if row["status"] == "revoked":
            return _failure("LICENSE_REVOKED", "회수된 라이선스는 기기 초기화할 수 없습니다.", "revoked")
        expires = _parse_dt(row["expires_at"])
        new_status = "expired" if expires and expires <= now else "unused"
        conn.execute(
            """
            UPDATE licenses
            SET status=?, bound_hwid_hash=NULL, activated_at=NULL,
                last_verified_at=NULL, updated_at=?
            WHERE id=?
            """,
            (new_status, _iso(now), license_id),
        )
        conn.execute(
            """
            UPDATE license_activations
            SET status='revoked', revoked_at=?, updated_at=?
            WHERE license_id=? AND status='active'
            """,
            (_iso(now), _iso(now), license_id),
        )
        _event(conn, "license_device_reset", "ok", license_id=license_id, reason_code=reason[:80])
        conn.commit()
        updated = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        return {"ok": True, "license": _row_to_public(updated)}
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def extend_license(license_id: str, expires_at: str) -> dict:
    now = _now()
    expires_dt = _parse_dt(expires_at)
    if not expires_dt:
        return _failure("INVALID_EXPIRES_AT", "만료일을 확인할 수 없습니다.")
    conn = get_conn()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        if not row:
            return _failure("LICENSE_NOT_FOUND", "라이선스를 찾을 수 없습니다.")
        status = row["status"]
        if status == "expired" and expires_dt > now:
            status = "active" if row["bound_hwid_hash"] else "unused"
        conn.execute(
            "UPDATE licenses SET status=?, expires_at=?, updated_at=? WHERE id=?",
            (status, _iso(expires_dt), _iso(now), license_id),
        )
        _event(conn, "license_extended", "ok", license_id=license_id)
        conn.commit()
        updated = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        return {"ok": True, "license": _row_to_public(updated)}
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
