# Google Contacts Export Runbook (2026-05-11)

## Current Mode

- Default mode is safe export only.
- Google People API automatic registration is disabled.
- No OAuth browser flow, external upload, or Google API call is part of this runbook.

## Admin Export

- CSV: `GET /admin/contacts-export.csv`
- vCard: `GET /admin/contacts-export.vcf`
- Both endpoints require admin authentication or approved local admin preview.
- Export decrypts contact fields only inside the endpoint response.
- General `/members` and `/members/{member_id}` responses must not include decrypted or encrypted contact fields.

## Export Fields

- Applicant name
- Phone number
- Email
- Member status
- Application type (`plan_type`)
- Participation grade
- Created time
- Booking status summary

## Audit Log

Every export appends a `member_logs` row:

- `member_id`: `system`
- `action`: `contacts_export`
- `detail`: export format and row count only

The log detail must not include phone numbers, email addresses, tokens, or secret values.

## Disabled Google Contacts Stub

Stub file: `agents/google_contacts.py`

Environment variable names needed before any future automatic sync can be considered:

- `GOOGLE_CONTACTS_ENABLED`
- `GOOGLE_CONTACTS_CLIENT_ID`
- `GOOGLE_CONTACTS_CLIENT_SECRET`
- `GOOGLE_CONTACTS_REFRESH_TOKEN`
- `GOOGLE_CONTACTS_REDIRECT_URI`

Do not print or commit actual values.

## Approval Gate Before Enabling Automatic Registration

Before enabling People API registration, get explicit user approval for:

- Turning on automatic Google Contacts registration.
- Google Cloud project and People API scope selection.
- OAuth client setup and token storage location.
- Exact contacts to sync and duplicate handling policy.
- Audit log format for sync attempts and failures.
- Rollback plan to disable sync immediately.
