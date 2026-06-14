"""Disabled Google Contacts integration stub.

This module intentionally does not call Google APIs or start OAuth flows.
Use the CSV/vCard export endpoints for the current safe operating mode.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


GOOGLE_CONTACTS_ENABLED = os.getenv("GOOGLE_CONTACTS_ENABLED", "").lower() in {
    "1",
    "true",
    "yes",
    "on",
}

REQUIRED_ENV_VARS = (
    "GOOGLE_CONTACTS_ENABLED",
    "GOOGLE_CONTACTS_CLIENT_ID",
    "GOOGLE_CONTACTS_CLIENT_SECRET",
    "GOOGLE_CONTACTS_REFRESH_TOKEN",
    "GOOGLE_CONTACTS_REDIRECT_URI",
)


@dataclass(frozen=True)
class GoogleContactsPlan:
    enabled: bool
    mode: str
    required_env_vars: tuple[str, ...]
    user_approval_required: bool
    oauth_required: bool


def integration_plan() -> GoogleContactsPlan:
    """Return operator-safe setup metadata without exposing secret values."""
    return GoogleContactsPlan(
        enabled=GOOGLE_CONTACTS_ENABLED,
        mode="disabled_stub" if not GOOGLE_CONTACTS_ENABLED else "requires_explicit_approval",
        required_env_vars=REQUIRED_ENV_VARS,
        user_approval_required=True,
        oauth_required=True,
    )


def sync_contacts(*_args, **_kwargs) -> dict:
    """Placeholder for a future People API sync.

    The current implementation must never perform network calls. A future
    implementation needs explicit operator approval, OAuth setup, and tests
    that keep disabled mode as the default.
    """
    plan = integration_plan()
    return {
        "ok": False,
        "enabled": plan.enabled,
        "status": "disabled",
        "message": "Google Contacts automatic registration is disabled. Use CSV/vCard export.",
        "required_env_vars": list(plan.required_env_vars),
        "user_approval_required": plan.user_approval_required,
        "oauth_required": plan.oauth_required,
    }
