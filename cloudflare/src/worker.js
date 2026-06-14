const DEFAULT_PRICE = 50000;
const DEFAULT_TITLE = "AI 기초 셋팅 및 컨설팅 강의 1:4";
const DEFAULT_LOCATION = "영등포시장역 사무실";
const CLOUDFLARE_VERSION = "cloudflare-v1";
const PRODUCTION_ROUTE = "apply.arsen-ai.com/*";
const D1_DATABASE_NAME = "arsen_member_system";
const INACTIVE_BOOKING_STATUSES = new Set(["canceled", "rejected", "no_show"]);
const NON_MOVABLE_BOOKING_STATUSES = new Set(["canceled", "rejected", "no_show", "completed"]);
const PENDING_BOOKING_STATUSES = new Set(["requested", "payment_guide_sent", "payment_pending", "payment_confirmed"]);
const ALLOWED_BOOKING_STATUSES = new Set([
  "requested",
  "payment_guide_sent",
  "payment_pending",
  "payment_confirmed",
  "confirmed",
  "waitlisted",
  "canceled",
  "rejected",
  "completed",
  "no_show",
]);
const ALLOWED_PAYMENT_STATUSES = new Set(["not_sent", "guide_sent", "pending", "paid", "waived", "refunded", "failed"]);
const LICENSE_DEFAULT_DAYS = 365;
const LICENSE_GRACE_SECONDS = 3 * 24 * 60 * 60;
const LICENSE_TOKEN_DAYS = 90;
const LICENSE_KEY_PREFIX = "YB";
const LICENSE_KEY_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
const YOONBOT_PRODUCT_CODE = "yoonbot";
const YOONBOT_PLANS = Object.freeze([
  {
    code: "trial",
    name: "Trial",
    amount_krw: 0,
    license_days: 7,
    description: "운영자 승인 후 7일 테스트 라이선스를 발급합니다.",
  },
  {
    code: "monthly",
    name: "Monthly",
    amount_krw: 99000,
    license_days: 31,
    description: "1개월 단위로 YoonBot을 사용합니다.",
  },
  {
    code: "yearly",
    name: "Yearly",
    amount_krw: 990000,
    license_days: 365,
    description: "12개월 라이선스를 한 번에 발급합니다.",
  },
]);
const YOONBOT_ORDER_TERMINAL_STATUSES = new Set(["canceled", "refunded"]);
const DEFAULT_SITE_THEME_ID = "arsen-modern";
const SITE_THEME_PROFILES = Object.freeze([
  {
    id: "legacy",
    name: "구버전 기본",
    scope: "public-and-admin",
    css_path: "assets/themes/legacy.css",
    description: "각 페이지에 원래 들어 있던 기본 스타일을 우선 사용합니다.",
    enabled: true,
  },
  {
    id: "arsen-modern",
    name: "ARSEN 모던",
    scope: "public-and-admin",
    css_path: "assets/themes/arsen-modern.css",
    description: "현재 적용 중인 ARSEN 테마입니다. 공개 페이지는 라이트, 관리자 운영 화면은 다크 톤을 포함합니다.",
    enabled: true,
  },
]);

function now() {
  return new Date().toISOString();
}

function json(data, init = {}) {
  const headers = new Headers(init.headers || {});
  headers.set("content-type", "application/json; charset=utf-8");
  headers.set("cache-control", "no-store, max-age=0");
  headers.set("pragma", "no-cache");
  return new Response(JSON.stringify(data), { ...init, headers });
}

function fail(status, detail, extra = {}) {
  return json({ ok: false, detail, ...extra }, { status });
}

function allowedOrigin(request, env) {
  const origin = request.headers.get("origin") || "";
  const configured = String(env.ALLOWED_ORIGINS || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
  if (configured.includes(origin)) return origin;
  if (!origin) return "";
  return "";
}

function withCors(response, request, env) {
  const headers = new Headers(response.headers);
  const origin = allowedOrigin(request, env);
  if (origin) {
    headers.set("access-control-allow-origin", origin);
    headers.set("vary", "origin");
    headers.set("access-control-allow-headers", "authorization,content-type,x-admin-key");
    headers.set("access-control-allow-methods", "GET,POST,PUT,DELETE,OPTIONS");
  }
  return new Response(response.body, { status: response.status, statusText: response.statusText, headers });
}

function requireAdmin(request, env) {
  const expected = String(env.ADMIN_API_KEY || "");
  if (!expected) return { ok: false, response: fail(500, "ADMIN_API_KEY is not configured") };
  const actual = request.headers.get("x-admin-key") || "";
  if (actual !== expected) return { ok: false, response: fail(401, "관리자 비밀번호가 필요합니다.") };
  return { ok: true };
}

async function readJson(request) {
  if (request.method === "GET" || request.method === "HEAD") return {};
  const text = await request.text();
  if (!text.trim()) return {};
  try {
    return JSON.parse(text);
  } catch (_) {
    throw new Error("JSON 본문을 해석하지 못했습니다.");
  }
}

function normalizePhone(value) {
  return String(value || "").replace(/[^\d]/g, "");
}

function normalizePhoneForStorage(value) {
  const digits = normalizePhone(value);
  if (digits.length === 11) return `${digits.slice(0, 3)}-${digits.slice(3, 7)}-${digits.slice(7)}`;
  return String(value || "").trim();
}

function phoneCandidates(value) {
  const raw = String(value || "").trim();
  const digits = normalizePhone(value);
  const formatted = normalizePhoneForStorage(value);
  return [raw, formatted, digits].filter((item, index, arr) => item && arr.indexOf(item) === index);
}

function maskPhone(value) {
  const digits = normalizePhone(value);
  if (digits.length < 7) return digits ? `${digits.slice(0, 3)}****` : "";
  return `${digits.slice(0, 3)}-${"*".repeat(Math.max(3, digits.length - 7))}-${digits.slice(-4)}`;
}

async function sha256Hex(value) {
  const bytes = new TextEncoder().encode(String(value || ""));
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function hmacHex(value, env, secretName) {
  const key = await legacySecretKey(env, secretName, "sign");
  const signature = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(String(value || "")));
  return [...new Uint8Array(signature)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

function bytesToBase64(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary);
}

function base64ToBytes(text) {
  return Uint8Array.from(atob(text), (char) => char.charCodeAt(0));
}

function legacyRawKey(env, secretName) {
  const raw = new TextEncoder().encode(String(env[secretName] || ""));
  const key = new Uint8Array(32);
  key.set(raw.slice(0, 32));
  return key;
}

async function legacySecretKey(env, secretName, usage) {
  const raw = legacyRawKey(env, secretName);
  if (usage === "sign") {
    return crypto.subtle.importKey("raw", raw, { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  }
  return crypto.subtle.importKey("raw", raw, "AES-CBC", false, usage === "decrypt" ? ["decrypt"] : ["encrypt"]);
}

async function aesKey(env) {
  const secret = String(env.CONTACT_ENCRYPTION_KEY || "");
  if (!secret) return null;
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(secret));
  return crypto.subtle.importKey("raw", digest, "AES-GCM", false, ["encrypt", "decrypt"]);
}

function pkcs7Pad(bytes) {
  const remainder = bytes.length % 16;
  const padLength = remainder === 0 ? 16 : 16 - remainder;
  const output = new Uint8Array(bytes.length + padLength);
  output.set(bytes);
  output.fill(padLength, bytes.length);
  return output;
}

function pkcs7Unpad(bytes) {
  if (!bytes.length) return bytes;
  const padLength = bytes[bytes.length - 1];
  if (padLength <= 0 || padLength > 16) return bytes;
  return bytes.slice(0, bytes.length - padLength);
}

async function encryptLegacyValue(value, env, secretName) {
  const text = String(value || "");
  if (!text) return "";
  const key = await legacySecretKey(env, secretName, "encrypt");
  const cbcIv = crypto.getRandomValues(new Uint8Array(16));
  const cipher = await crypto.subtle.encrypt({ name: "AES-CBC", iv: cbcIv }, key, pkcs7Pad(new TextEncoder().encode(text)));
  const combined = new Uint8Array(cbcIv.length + cipher.byteLength);
  combined.set(cbcIv);
  combined.set(new Uint8Array(cipher), cbcIv.length);
  return bytesToBase64(combined);
}

async function decryptValue(value, env, secretName) {
  const text = String(value || "");
  if (!text) return "";
  if (text.startsWith("aesgcm:")) {
    const key = await aesKey(env);
    if (!key) return "";
    const [ivText, cipherText] = text.slice("aesgcm:".length).split(".");
    const plain = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: base64ToBytes(ivText) },
      key,
      base64ToBytes(cipherText)
    );
    return new TextDecoder().decode(plain);
  }
  const raw = base64ToBytes(text);
  if (raw.length < 32) return "";
  const iv = raw.slice(0, 16);
  const cipher = raw.slice(16);
  const key = await legacySecretKey(env, secretName, "decrypt");
  const plain = await crypto.subtle.decrypt({ name: "AES-CBC", iv }, key, cipher);
  return new TextDecoder().decode(pkcs7Unpad(new Uint8Array(plain)));
}

function gradeCount(data) {
  let score = 0;
  if (data.ai_subscription) score += 1;
  if (data.can_code) score += 1;
  if (data.can_present) score += 1;
  if (Array.isArray(data.available_time_slots) ? data.available_time_slots.length : data.available_time_slots) score += 1;
  if (data.short_term_goal || data.desired_outcome) score += 1;
  if (score >= 3) return "power";
  if (score >= 1) return "starter";
  return "new";
}

function accessCode() {
  const alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const bytes = crypto.getRandomValues(new Uint8Array(6));
  return [...bytes].map((byte) => alphabet[byte % alphabet.length]).join("");
}

function licenseCanonical(value) {
  return String(value || "").toUpperCase().replace(/[^A-Z0-9]/g, "");
}

function requireLicenseSecret(env) {
  if (!String(env.LICENSE_SECRET_KEY || "")) {
    throw new Error("LICENSE_SECRET_KEY is not configured");
  }
}

async function licenseHmacHex(env, value) {
  requireLicenseSecret(env);
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(String(env.LICENSE_SECRET_KEY || "")),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const signature = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(String(value || "")));
  return [...new Uint8Array(signature)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function licenseHash(env, kind, value) {
  return licenseHmacHex(env, `${kind}:${licenseCanonical(value)}`);
}

async function licenseHashLoose(env, kind, value) {
  if (!value) return null;
  return licenseHmacHex(env, `${kind}:${String(value || "")}`);
}

function licenseIso(date = new Date()) {
  return date.toISOString().replace(/\.\d{3}Z$/, "Z");
}

function parseLicenseDate(value) {
  const text = String(value || "").trim();
  if (!text) return null;
  const normalized = /(?:Z|[+-]\d{2}:?\d{2})$/.test(text) ? text : `${text}+00:00`;
  const date = new Date(normalized);
  return Number.isNaN(date.getTime()) ? null : date;
}

function addDays(date, days) {
  return new Date(date.getTime() + Number(days || 0) * 24 * 60 * 60 * 1000);
}

function randomLicenseKey() {
  const bytes = crypto.getRandomValues(new Uint8Array(16));
  const groups = [];
  for (let groupIndex = 0; groupIndex < 4; groupIndex += 1) {
    let group = "";
    for (let offset = 0; offset < 4; offset += 1) {
      group += LICENSE_KEY_ALPHABET[bytes[groupIndex * 4 + offset] % LICENSE_KEY_ALPHABET.length];
    }
    groups.push(group);
  }
  return [LICENSE_KEY_PREFIX, ...groups].join("-");
}

function randomActivationToken() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return [...bytes].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

function licenseKeyHint(licenseKey) {
  const canonical = licenseCanonical(licenseKey);
  return `${LICENSE_KEY_PREFIX}-****-****-****-${canonical.slice(-4) || "****"}`;
}

function licenseVersionTuple(version) {
  return (String(version || "").match(/\d+/g) || []).slice(0, 4).map((part) => Number(part));
}

function isLicenseVersionBlocked(appVersion, minVersion) {
  if (!appVersion || !minVersion) return false;
  const app = licenseVersionTuple(appVersion);
  const minimum = licenseVersionTuple(minVersion);
  if (!app.length || !minimum.length) return false;
  const length = Math.max(app.length, minimum.length);
  for (let index = 0; index < length; index += 1) {
    const left = app[index] || 0;
    const right = minimum[index] || 0;
    if (left < right) return true;
    if (left > right) return false;
  }
  return false;
}

function licenseRequestIp(request) {
  return request.headers.get("cf-connecting-ip") || request.headers.get("x-forwarded-for") || "";
}

function safeUserAgent(request) {
  return String(request.headers.get("user-agent") || "").slice(0, 200);
}

function bearerToken(request) {
  const value = request.headers.get("authorization") || "";
  const match = value.match(/^Bearer\s+(.+)$/i);
  return match ? match[1].trim() : "";
}

function licensePublic(row) {
  if (!row) return null;
  return {
    id: row.id,
    member_id: row.member_id || null,
    plan_code: row.plan_code || "basic",
    status: row.status || "unused",
    license_key_hint: row.license_key_hint,
    max_devices: Number(row.max_devices || 1),
    bound_device: Boolean(row.bound_hwid_hash),
    app_min_version: row.app_min_version || null,
    expires_at: row.expires_at,
    activated_at: row.activated_at || null,
    last_verified_at: row.last_verified_at || null,
    revoked_at: row.revoked_at || null,
    revoke_reason: row.revoke_reason || null,
    note: row.note || null,
    created_at: row.created_at,
    updated_at: row.updated_at,
  };
}

function licenseAdminPublic(row) {
  const item = licensePublic(row);
  if (!item) return null;
  return {
    ...item,
    dev_license_key: row.dev_license_key || null,
  };
}

function licenseFailure(code, message, status = "invalid") {
  return { ok: false, status, code, message };
}

async function licenseEvent(env, eventType, result, options = {}) {
  await env.DB.prepare(
    `INSERT INTO license_events (
      id, license_id, activation_id, event_type, result, reason_code,
      ip_hash, user_agent, app_version, platform, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      crypto.randomUUID(),
      options.license_id || null,
      options.activation_id || null,
      eventType,
      result,
      options.reason_code || null,
      await licenseHashLoose(env, "ip", options.ip || null),
      String(options.user_agent || "").slice(0, 200) || null,
      options.app_version || null,
      options.platform || null,
      licenseIso()
    )
    .run();
}

async function licenseSummary(env) {
  const rows = await all(env, "SELECT status, COUNT(*) AS count FROM licenses GROUP BY status");
  const counts = Object.fromEntries(rows.map((row) => [row.status, Number(row.count || 0)]));
  return {
    total: Object.values(counts).reduce((sum, value) => sum + value, 0),
    unused: counts.unused || 0,
    active: counts.active || 0,
    expired: counts.expired || 0,
    revoked: counts.revoked || 0,
  };
}

async function listLicenses(env, params = {}) {
  const where = [];
  const values = [];
  if (params.status) {
    where.push("status=?");
    values.push(params.status);
  }
  if (params.member_id) {
    where.push("member_id=?");
    values.push(params.member_id);
  }
  const clause = where.length ? `WHERE ${where.join(" AND ")}` : "";
  const rows = await all(env, `SELECT * FROM licenses ${clause} ORDER BY created_at DESC`, ...values);
  return rows.map(licenseAdminPublic);
}

async function getLicense(env, licenseId) {
  const row = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
  return row ? licenseAdminPublic(row) : null;
}

async function createLicense(env, body, request) {
  requireLicenseSecret(env);
  const created = licenseIso();
  const memberId = String(body.member_id || "").trim() || null;
  if (memberId) {
    const member = await one(env, "SELECT id FROM members WHERE id=?", memberId);
    if (!member) return { response: fail(400, "존재하지 않는 member_id입니다.") };
  }
  const expiresAt = licenseIso(parseLicenseDate(body.expires_at) || addDays(new Date(), LICENSE_DEFAULT_DAYS));
  const maxDevices = Math.max(1, Math.floor(Number(body.max_devices || 1)));
  const planCode = String(body.plan_code || "basic").trim().slice(0, 80) || "basic";
  const appMinVersion = String(body.app_min_version || "").trim().slice(0, 80) || null;
  const note = String(body.note || "").trim().slice(0, 1000) || null;

  for (let attempt = 0; attempt < 10; attempt += 1) {
    const licenseKey = randomLicenseKey();
    const licenseId = crypto.randomUUID();
    try {
      await env.DB.prepare(
        `INSERT INTO licenses (
          id, member_id, license_key_hash, license_key_hint, dev_license_key, plan_code,
          status, max_devices, app_min_version, expires_at, note, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, 'unused', ?, ?, ?, ?, ?, ?)`
      )
        .bind(
          licenseId,
          memberId,
          await licenseHash(env, "license", licenseKey),
          licenseKeyHint(licenseKey),
          licenseKey,
          planCode,
          maxDevices,
          appMinVersion,
          expiresAt,
          note,
          created,
          created
        )
        .run();
      await licenseEvent(env, "license_created", "ok", {
        license_id: licenseId,
        ip: licenseRequestIp(request),
        user_agent: safeUserAgent(request),
      });
      const row = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
      return { ok: true, license_key: licenseKey, license: licensePublic(row) };
    } catch (error) {
      if (!String(error?.message || error).toUpperCase().includes("UNIQUE")) throw error;
    }
  }
  throw new Error("라이선스 키 생성 충돌이 반복되었습니다.");
}

async function revokeLicense(env, licenseId, reason, request) {
  const row = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
  if (!row) return licenseFailure("LICENSE_NOT_FOUND", "라이선스를 찾을 수 없습니다.");
  const updated = licenseIso();
  const reasonText = String(reason || "manual").slice(0, 200);
  await env.DB.prepare("UPDATE licenses SET status='revoked', revoked_at=?, revoke_reason=?, updated_at=? WHERE id=?")
    .bind(updated, reasonText, updated, licenseId)
    .run();
  await env.DB.prepare("UPDATE license_activations SET status='revoked', revoked_at=?, updated_at=? WHERE license_id=? AND status='active'")
    .bind(updated, updated, licenseId)
    .run();
  await licenseEvent(env, "license_revoked", "ok", {
    license_id: licenseId,
    reason_code: reasonText.slice(0, 80),
    ip: licenseRequestIp(request),
    user_agent: safeUserAgent(request),
  });
  return { ok: true, license: licensePublic(await one(env, "SELECT * FROM licenses WHERE id=?", licenseId)) };
}

async function resetLicenseDevice(env, licenseId, reason, request) {
  const row = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
  if (!row) return licenseFailure("LICENSE_NOT_FOUND", "라이선스를 찾을 수 없습니다.");
  if (row.status === "revoked") return licenseFailure("LICENSE_REVOKED", "회수된 라이선스는 기기 초기화할 수 없습니다.", "revoked");
  const updated = licenseIso();
  const expiresAt = parseLicenseDate(row.expires_at);
  const newStatus = expiresAt && expiresAt <= new Date() ? "expired" : "unused";
  await env.DB.prepare(
    "UPDATE licenses SET status=?, bound_hwid_hash=NULL, activated_at=NULL, last_verified_at=NULL, updated_at=? WHERE id=?"
  )
    .bind(newStatus, updated, licenseId)
    .run();
  await env.DB.prepare("UPDATE license_activations SET status='revoked', revoked_at=?, updated_at=? WHERE license_id=? AND status='active'")
    .bind(updated, updated, licenseId)
    .run();
  await licenseEvent(env, "license_device_reset", "ok", {
    license_id: licenseId,
    reason_code: String(reason || "manual").slice(0, 80),
    ip: licenseRequestIp(request),
    user_agent: safeUserAgent(request),
  });
  return { ok: true, license: licensePublic(await one(env, "SELECT * FROM licenses WHERE id=?", licenseId)) };
}

async function extendLicense(env, licenseId, expiresAtValue, request) {
  const expiresAt = parseLicenseDate(expiresAtValue);
  if (!expiresAt) return licenseFailure("INVALID_EXPIRES_AT", "만료일을 확인할 수 없습니다.");
  const row = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
  if (!row) return licenseFailure("LICENSE_NOT_FOUND", "라이선스를 찾을 수 없습니다.");
  let status = row.status;
  if (status === "expired" && expiresAt > new Date()) status = row.bound_hwid_hash ? "active" : "unused";
  const updated = licenseIso();
  await env.DB.prepare("UPDATE licenses SET status=?, expires_at=?, updated_at=? WHERE id=?")
    .bind(status, licenseIso(expiresAt), updated, licenseId)
    .run();
  await licenseEvent(env, "license_extended", "ok", {
    license_id: licenseId,
    ip: licenseRequestIp(request),
    user_agent: safeUserAgent(request),
  });
  return { ok: true, license: licensePublic(await one(env, "SELECT * FROM licenses WHERE id=?", licenseId)) };
}

async function activateLicense(env, body, request) {
  const licenseKey = String(body.license_key || "").trim();
  const hwid = String(body.hwid || "").trim();
  if (!licenseKey || !hwid) return licenseFailure("INVALID_REQUEST", "라이선스 키와 HWID가 필요합니다.");
  const appVersion = String(body.app_version || "").trim() || null;
  const platform = String(body.platform || "windows").trim().slice(0, 80) || "windows";
  const deviceName = String(body.device_name || "").trim().slice(0, 120) || null;
  const ip = licenseRequestIp(request);
  const userAgent = safeUserAgent(request);
  const current = new Date();
  const licenseKeyHash = await licenseHash(env, "license", licenseKey);
  const hwidHash = await licenseHash(env, "hwid", hwid);
  const row = await one(env, "SELECT * FROM licenses WHERE license_key_hash=?", licenseKeyHash);

  if (!row) {
    await licenseEvent(env, "license_activate", "blocked", { reason_code: "LICENSE_NOT_FOUND", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("LICENSE_NOT_FOUND", "라이선스 키를 확인할 수 없습니다.");
  }

  const licenseId = row.id;
  const expiresAt = parseLicenseDate(row.expires_at);
  if (expiresAt && expiresAt <= current) {
    await env.DB.prepare("UPDATE licenses SET status='expired', updated_at=? WHERE id=? AND status!='revoked'").bind(licenseIso(current), licenseId).run();
    await licenseEvent(env, "license_activate", "blocked", { license_id: licenseId, reason_code: "LICENSE_EXPIRED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("LICENSE_EXPIRED", "만료된 라이선스입니다.", "expired");
  }
  if (row.status === "revoked") {
    await licenseEvent(env, "license_activate", "blocked", { license_id: licenseId, reason_code: "LICENSE_REVOKED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("LICENSE_REVOKED", "회수된 라이선스입니다.", "revoked");
  }
  if (isLicenseVersionBlocked(appVersion, row.app_min_version)) {
    await licenseEvent(env, "license_activate", "blocked", { license_id: licenseId, reason_code: "APP_VERSION_BLOCKED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("APP_VERSION_BLOCKED", "프로그램 업데이트가 필요합니다.", row.status);
  }
  if (row.bound_hwid_hash && row.bound_hwid_hash !== hwidHash) {
    await licenseEvent(env, "license_activate", "blocked", { license_id: licenseId, reason_code: "HWID_MISMATCH", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("HWID_MISMATCH", "이미 다른 기기에 등록된 라이선스입니다.", row.status);
  }

  const token = randomActivationToken();
  const tokenHash = await licenseHash(env, "token", token);
  let tokenExpiresAt = addDays(current, LICENSE_TOKEN_DAYS);
  if (expiresAt && tokenExpiresAt > expiresAt) tokenExpiresAt = expiresAt;
  const activationId = crypto.randomUUID();
  const timestamp = licenseIso(current);
  await env.DB.prepare("UPDATE license_activations SET status='revoked', revoked_at=?, updated_at=? WHERE license_id=? AND status='active'")
    .bind(timestamp, timestamp, licenseId)
    .run();
  await env.DB.prepare(
    `INSERT INTO license_activations (
      id, license_id, token_hash, hwid_hash, platform, device_name,
      app_version, status, first_seen_at, last_seen_at, expires_at, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, 'active', ?, ?, ?, ?, ?)`
  )
    .bind(activationId, licenseId, tokenHash, hwidHash, platform, deviceName, appVersion, timestamp, timestamp, licenseIso(tokenExpiresAt), timestamp, timestamp)
    .run();
  await env.DB.prepare(
    `UPDATE licenses
     SET status='active', bound_hwid_hash=?, activated_at=COALESCE(activated_at, ?), last_verified_at=?, updated_at=?
     WHERE id=?`
  )
    .bind(hwidHash, timestamp, timestamp, timestamp, licenseId)
    .run();
  await licenseEvent(env, "license_activate", "ok", { license_id: licenseId, activation_id: activationId, ip, user_agent: userAgent, app_version: appVersion, platform });
  const updated = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
  return {
    ok: true,
    status: "active",
    activation_token: token,
    license: licensePublic(updated),
    server_time: timestamp,
    grace_seconds: LICENSE_GRACE_SECONDS,
  };
}

async function verifyLicense(env, body, request, activationToken) {
  const hwid = String(body.hwid || "").trim();
  if (!hwid) return licenseFailure("INVALID_REQUEST", "HWID가 필요합니다.");
  const appVersion = String(body.app_version || "").trim() || null;
  const platform = String(body.platform || "windows").trim().slice(0, 80) || "windows";
  const ip = licenseRequestIp(request);
  const userAgent = safeUserAgent(request);
  const current = new Date();
  const tokenHash = await licenseHash(env, "token", activationToken);
  const hwidHash = await licenseHash(env, "hwid", hwid);
  const row = await one(
    env,
    `SELECT
      a.id AS activation_id,
      a.hwid_hash AS activation_hwid_hash,
      a.status AS activation_status,
      a.expires_at AS activation_expires_at,
      l.*
     FROM license_activations a
     JOIN licenses l ON l.id = a.license_id
     WHERE a.token_hash=?`,
    tokenHash
  );
  if (!row) {
    await licenseEvent(env, "license_verify", "blocked", { reason_code: "TOKEN_NOT_FOUND", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("TOKEN_NOT_FOUND", "인증 토큰을 확인할 수 없습니다.");
  }

  const licenseId = row.id;
  const activationId = row.activation_id;
  if (row.activation_status !== "active") {
    await licenseEvent(env, "license_verify", "blocked", { license_id: licenseId, activation_id: activationId, reason_code: "TOKEN_REVOKED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("TOKEN_REVOKED", "인증 토큰이 회수되었습니다.");
  }
  const activationExpires = parseLicenseDate(row.activation_expires_at);
  const licenseExpires = parseLicenseDate(row.expires_at);
  if (activationExpires && activationExpires <= current) {
    await env.DB.prepare("UPDATE license_activations SET status='expired', updated_at=? WHERE id=?").bind(licenseIso(current), activationId).run();
    await licenseEvent(env, "license_verify", "blocked", { license_id: licenseId, activation_id: activationId, reason_code: "TOKEN_EXPIRED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("TOKEN_EXPIRED", "인증 토큰이 만료되었습니다.", "expired");
  }
  if (licenseExpires && licenseExpires <= current) {
    await env.DB.prepare("UPDATE licenses SET status='expired', updated_at=? WHERE id=? AND status!='revoked'").bind(licenseIso(current), licenseId).run();
    await licenseEvent(env, "license_verify", "blocked", { license_id: licenseId, activation_id: activationId, reason_code: "LICENSE_EXPIRED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("LICENSE_EXPIRED", "만료된 라이선스입니다.", "expired");
  }
  if (row.status === "revoked") {
    await licenseEvent(env, "license_verify", "blocked", { license_id: licenseId, activation_id: activationId, reason_code: "LICENSE_REVOKED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("LICENSE_REVOKED", "회수된 라이선스입니다.", "revoked");
  }
  if (row.activation_hwid_hash !== hwidHash || row.bound_hwid_hash !== hwidHash) {
    await licenseEvent(env, "license_verify", "blocked", { license_id: licenseId, activation_id: activationId, reason_code: "HWID_MISMATCH", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("HWID_MISMATCH", "등록된 기기와 다릅니다.", row.status);
  }
  if (isLicenseVersionBlocked(appVersion, row.app_min_version)) {
    await licenseEvent(env, "license_verify", "blocked", { license_id: licenseId, activation_id: activationId, reason_code: "APP_VERSION_BLOCKED", ip, user_agent: userAgent, app_version: appVersion, platform });
    return licenseFailure("APP_VERSION_BLOCKED", "프로그램 업데이트가 필요합니다.", row.status);
  }

  const timestamp = licenseIso(current);
  await env.DB.prepare("UPDATE license_activations SET last_seen_at=?, app_version=?, platform=?, updated_at=? WHERE id=?")
    .bind(timestamp, appVersion, platform, timestamp, activationId)
    .run();
  await env.DB.prepare("UPDATE licenses SET last_verified_at=?, updated_at=? WHERE id=?").bind(timestamp, timestamp, licenseId).run();
  await licenseEvent(env, "license_verify", "ok", { license_id: licenseId, activation_id: activationId, ip, user_agent: userAgent, app_version: appVersion, platform });
  const updated = await one(env, "SELECT * FROM licenses WHERE id=?", licenseId);
  return {
    ok: true,
    status: "active",
    license: licensePublic(updated),
    server_time: timestamp,
    grace_seconds: LICENSE_GRACE_SECONDS,
  };
}

function normalizeEmail(value) {
  return String(value || "").trim().toLowerCase();
}

function maskEmail(value) {
  const email = normalizeEmail(value);
  if (!email.includes("@")) return "";
  const [local, domain] = email.split("@");
  const visible = local.length >= 2 ? local.slice(0, 2) : local.slice(0, 1);
  return `${visible}${"*".repeat(Math.max(3, local.length - visible.length))}@${domain}`;
}

function yoonbotPlan(planCode) {
  const normalized = String(planCode || "").trim().toLowerCase();
  return YOONBOT_PLANS.find((plan) => plan.code === normalized) || null;
}

function yoonbotProducts() {
  return {
    product: {
      code: YOONBOT_PRODUCT_CODE,
      name: "YoonBot",
      payment_mode: "manual_bank_transfer",
      auto_charge: false,
    },
    plans: YOONBOT_PLANS,
  };
}

function orderPaymentRef(orderId) {
  return `YB-${String(orderId || "").replace(/-/g, "").slice(0, 8).toUpperCase()}`;
}

function orderPublic(row) {
  if (!row) return null;
  return {
    id: row.id,
    buyer_name: row.buyer_name,
    buyer_email_masked: row.buyer_email_masked || "",
    buyer_phone_masked: row.buyer_phone_masked || "",
    product_code: row.product_code || YOONBOT_PRODUCT_CODE,
    plan_code: row.plan_code,
    amount_krw: Number(row.amount_krw || 0),
    status: row.status,
    payment_provider: row.payment_provider || "manual_bank_transfer",
    payment_ref: row.payment_ref || "",
    member_id: row.member_id || null,
    license_id: row.license_id || null,
    license_key_hint: row.license_key_hint || null,
    license_status: row.license_status || null,
    note: row.note || null,
    customer_message: row.customer_message || null,
    paid_at: row.paid_at || null,
    canceled_at: row.canceled_at || null,
    refunded_at: row.refunded_at || null,
    created_at: row.created_at,
    updated_at: row.updated_at,
  };
}

function manualPaymentPayload(orderId = "") {
  return {
    mode: "manual_bank_transfer",
    auto_charge: false,
    payment_ref: orderId ? orderPaymentRef(orderId) : "",
    message: "관리자가 신청 내용을 확인한 뒤 입금 안내와 라이선스 발급을 수동으로 진행합니다.",
  };
}

async function createYoonbotOrder(env, body) {
  const productCode = String(body.product_code || YOONBOT_PRODUCT_CODE).trim().toLowerCase();
  if (productCode !== YOONBOT_PRODUCT_CODE) return { response: fail(400, "지원하지 않는 상품입니다.") };
  const plan = yoonbotPlan(body.plan_code || "monthly");
  if (!plan) return { response: fail(400, "지원하지 않는 YoonBot 플랜입니다.") };
  const buyerName = String(body.buyer_name || "").trim().slice(0, 80);
  if (!buyerName) return { response: fail(400, "구매자 이름을 입력하세요.") };
  const email = normalizeEmail(body.buyer_email);
  const phone = normalizePhone(body.buyer_phone);
  if (!email && !phone) return { response: fail(400, "연락 가능한 이메일 또는 전화번호가 필요합니다.") };
  if (!body.consent_privacy || !body.consent_terms) {
    return { response: fail(400, "개인정보 수집과 결제 안내에 동의해야 합니다.") };
  }

  const orderId = crypto.randomUUID();
  const created = licenseIso();
  await env.DB.prepare(
    `INSERT INTO orders (
      id, buyer_name, buyer_email_hash, buyer_email_masked,
      buyer_phone_hash, buyer_phone_masked, product_code, plan_code,
      amount_krw, status, payment_provider, payment_ref,
      customer_message, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'payment_pending', 'manual_bank_transfer', ?, ?, ?, ?)`
  )
    .bind(
      orderId,
      buyerName,
      email ? await hmacHex(`order-email:${email}`, env, "EMAIL_SECRET_KEY") : null,
      maskEmail(email),
      phone ? await hmacHex(`order-phone:${phone}`, env, "PHONE_SECRET_KEY") : null,
      maskPhone(phone),
      YOONBOT_PRODUCT_CODE,
      plan.code,
      plan.amount_krw,
      orderPaymentRef(orderId),
      String(body.customer_message || "").trim().slice(0, 1000) || null,
      created,
      created
    )
    .run();
  const order = await getYoonbotOrder(env, orderId);
  return { ok: true, data: order, payment: manualPaymentPayload(orderId) };
}

async function orderSummary(env) {
  const rows = await all(env, "SELECT status, COUNT(*) AS count FROM orders GROUP BY status");
  const counts = Object.fromEntries(rows.map((row) => [row.status, Number(row.count || 0)]));
  return {
    total: Object.values(counts).reduce((sum, value) => sum + value, 0),
    payment_pending: counts.payment_pending || 0,
    paid: counts.paid || 0,
    license_issued: counts.license_issued || 0,
    canceled: counts.canceled || 0,
    refunded: counts.refunded || 0,
  };
}

async function listYoonbotOrders(env, params = {}) {
  const where = [];
  const values = [];
  if (params.status) {
    where.push("o.status=?");
    values.push(params.status);
  }
  if (params.plan_code) {
    where.push("o.plan_code=?");
    values.push(params.plan_code);
  }
  const clause = where.length ? `WHERE ${where.join(" AND ")}` : "";
  const rows = await all(
    env,
    `SELECT o.*, l.license_key_hint, l.status AS license_status
     FROM orders o
     LEFT JOIN licenses l ON l.id=o.license_id
     ${clause}
     ORDER BY o.created_at DESC`,
    ...values
  );
  return rows.map(orderPublic);
}

async function getYoonbotOrder(env, orderId) {
  const row = await one(
    env,
    `SELECT o.*, l.license_key_hint, l.status AS license_status
     FROM orders o
     LEFT JOIN licenses l ON l.id=o.license_id
     WHERE o.id=?`,
    orderId
  );
  return orderPublic(row);
}

async function markYoonbotOrderPaid(env, orderId, body) {
  const order = await getYoonbotOrder(env, orderId);
  if (!order) return { ok: false, message: "주문을 찾을 수 없습니다.", status: 404 };
  if (YOONBOT_ORDER_TERMINAL_STATUSES.has(order.status)) {
    return { ok: false, message: "취소/환불된 주문은 결제 확인할 수 없습니다.", status: 400 };
  }
  const timestamp = licenseIso();
  const nextStatus = order.license_id ? "license_issued" : "paid";
  await env.DB.prepare(
    `UPDATE orders
     SET status=?, payment_provider=?, payment_ref=COALESCE(?, payment_ref),
       note=COALESCE(?, note), paid_at=COALESCE(paid_at, ?), updated_at=?
     WHERE id=?`
  )
    .bind(
      nextStatus,
      String(body.payment_provider || "manual_bank_transfer").trim().slice(0, 80),
      String(body.payment_ref || "").trim().slice(0, 120) || null,
      String(body.note || "").trim().slice(0, 1000) || null,
      timestamp,
      timestamp,
      orderId
    )
    .run();
  return { ok: true, data: await getYoonbotOrder(env, orderId) };
}

async function setYoonbotOrderTerminalStatus(env, orderId, status, timestampColumn, note) {
  const order = await getYoonbotOrder(env, orderId);
  if (!order) return { ok: false, message: "주문을 찾을 수 없습니다.", status: 404 };
  if (status === "canceled" && order.license_id) {
    return { ok: false, message: "이미 라이선스가 발급된 주문은 취소 대신 환불 메모로 처리하세요.", status: 400 };
  }
  const timestamp = licenseIso();
  await env.DB.prepare(
    `UPDATE orders SET status=?, note=COALESCE(?, note), ${timestampColumn}=?, updated_at=? WHERE id=?`
  )
    .bind(status, String(note || "").trim().slice(0, 1000) || null, timestamp, timestamp, orderId)
    .run();
  return { ok: true, data: await getYoonbotOrder(env, orderId) };
}

function yoonbotCustomerLicenseMessage(licenseKey, licenseItem) {
  return [
    "[YoonBot 라이선스 안내]",
    `라이선스 키: ${licenseKey}`,
    `만료일: ${licenseItem.expires_at}`,
    "Windows YoonBot 실행 후 라이선스 인증 창에 위 키를 입력하세요.",
    "처음 등록한 PC에 기기가 묶입니다. PC 변경이 필요하면 운영자에게 기기 초기화를 요청해주세요.",
  ].join("\n");
}

async function issueYoonbotOrderLicense(env, orderId, request) {
  const order = await getYoonbotOrder(env, orderId);
  if (!order) return { ok: false, message: "주문을 찾을 수 없습니다.", status: 404 };
  if (order.license_id) return { ok: false, message: "이미 라이선스가 발급된 주문입니다.", status: 400 };
  if (order.status !== "paid") {
    return { ok: false, message: "결제 확인된 주문에서만 라이선스를 발급할 수 있습니다.", status: 400 };
  }
  const plan = yoonbotPlan(order.plan_code);
  if (!plan) return { ok: false, message: "지원하지 않는 YoonBot 플랜입니다.", status: 400 };
  const expiresAt = licenseIso(addDays(new Date(), plan.license_days));
  const created = await createLicense(env, {
    member_id: order.member_id || null,
    plan_code: order.plan_code,
    expires_at: expiresAt,
    max_devices: 1,
    note: `order:${orderId} buyer:${order.buyer_name}`,
  }, request);
  if (created.response) return { ok: false, message: "라이선스 발급에 실패했습니다.", status: 400 };
  await env.DB.prepare(
    "UPDATE orders SET status='license_issued', license_id=?, updated_at=? WHERE id=? AND license_id IS NULL"
  )
    .bind(created.license.id, licenseIso(), orderId)
    .run();
  const updatedOrder = await getYoonbotOrder(env, orderId);
  return {
    ok: true,
    license_key: created.license_key,
    license: created.license,
    order: updatedOrder,
    delivery: noSendDelivery("manual_license_delivery").delivery,
    customer_message: yoonbotCustomerLicenseMessage(created.license_key, created.license),
  };
}

function noSendDelivery(mode = "manual_copy") {
  return {
    delivery: {
      mode,
      auto_send: false,
      message: "자동 발송은 하지 않습니다. 운영자가 문구를 복사해 직접 전달하세요.",
    },
  };
}

function configuredValue(value) {
  const text = String(value || "").trim();
  if (!text) return false;
  const lowered = text.toLowerCase();
  return !["your_", "placeholder", "token_here", "chat_id_here", "telegram_bot_token", "telegram_admin_chat_id"].some((marker) =>
    lowered.includes(marker)
  );
}

function envFlag(env, name, fallback = "") {
  const value = String(env[name] ?? fallback ?? "").trim().toLowerCase();
  return ["1", "true", "yes", "on"].includes(value);
}

function telegramEnabled(env, kind = "application") {
  if (kind === "button") return true;
  const global = String(env.TELEGRAM_NOTIFY_ENABLED || "");
  if (kind === "booking") return envFlag(env, "TELEGRAM_BOOKING_NOTIFY_ENABLED", global);
  return envFlag(env, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", env.TELEGRAM_BOOKING_NOTIFY_ENABLED || global);
}

function telegramConfigured(env, requireChat = true) {
  return configuredValue(env.TELEGRAM_BOT_TOKEN) && (!requireChat || configuredValue(env.TELEGRAM_ADMIN_CHAT_ID));
}

function htmlEscape(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function compactText(value, limit = 160) {
  const text = String(value || "")
    .replace(/\r/g, "\n")
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .join("\n");
  if (!text) return "-";
  return text.length > limit ? `${text.slice(0, limit).trimEnd()}...` : text;
}

function displayValue(value, limit = 220) {
  const text = Array.isArray(value) ? value.filter(Boolean).join(", ") : compactText(value, limit);
  if (!text || text === "-") return "-";
  const normalized = String(text);
  return htmlEscape(normalized.length > limit ? `${normalized.slice(0, limit).trimEnd()}...` : normalized);
}

function yesNo(value) {
  if (value === true || value === 1 || value === "1" || value === "true") return "예";
  if (value === false || value === 0 || value === "0" || value === "false") return "아니오";
  return "-";
}

function planTypeLabel(planType) {
  const normalized = String(planType || "").toLowerCase();
  return {
    free: "무료강의",
    full: "유료강의",
    basic: "기본강의",
  }[normalized] || planType || "-";
}

function contactPlanLabel(planType) {
  const normalized = String(planType || "").toLowerCase();
  return {
    free: "무료",
    full: "유료",
    basic: "기본",
  }[normalized] || "기본";
}

function contactDisplayName(name, planType) {
  const displayName = String(name || "신청자").trim() || "신청자";
  if (displayName.startsWith("[ARSEN ")) return displayName;
  return `[ARSEN ${contactPlanLabel(planType)}] ${displayName}`;
}

function contactNote(row) {
  return [
    `plan=${row.plan_type || "basic"}`,
    `status=${row.status || "unknown"}`,
    `member_id=${row.id || ""}`,
    `booking=${row.booking_status_summary || "none"}`,
    `created_at=${row.created_at || ""}`,
  ].join("; ");
}

function contactExportDetail(formatName, rows) {
  return JSON.stringify({
    format: formatName,
    count: rows.length,
    pii: "decrypted_for_admin_export",
  });
}

function noticePhone(value) {
  const text = String(value || "");
  return text.includes("*") ? text : maskPhone(text);
}

function publicBaseUrl(env) {
  return String(env.PUBLIC_BASE_URL || "https://apply.arsen-ai.com").replace(/\/+$/, "");
}

function adminUrl(env) {
  return `${publicBaseUrl(env)}/frontend/admin.html`;
}

function memberKeyboard(env, memberId) {
  if (!memberId) return null;
  return {
    inline_keyboard: [
      [
        { text: "승인 + 코드 발급", callback_data: `arsen:approve:${memberId}` },
        { text: "관리자 열기", url: adminUrl(env) },
      ],
    ],
  };
}

function bookingKeyboard(env, bookingId) {
  if (!bookingId) return null;
  return {
    inline_keyboard: [
      [
        { text: "입금 안내", callback_data: `arsen:payguide:${bookingId}` },
        { text: "입금 확인", callback_data: `arsen:confirm:${bookingId}` },
      ],
      [
        { text: "장소 안내", callback_data: `arsen:location:${bookingId}` },
        { text: "관리자 열기", url: adminUrl(env) },
      ],
    ],
  };
}

function statsLines(data) {
  if (!data) return [];
  return [
    "현황:",
    `- 대기 인원: ${Number(data.pending || 0)}명`,
    `- 승인 인원: ${Number(data.approved || 0)}명`,
    `- 전체 신청: ${Number(data.total || 0)}명`,
    `- 예약 신청: ${Number(data.requested_bookings || 0)}명`,
    `- 활성 예약: ${Number(data.active_bookings || 0)}명`,
  ];
}

function applicationMessage(member, counts, duplicate = false, attempted = null) {
  const planLabel = planTypeLabel(attempted?.plan_type || member?.plan_type);
  const base = [
    duplicate
      ? `<b>ARSEN 중복 신청 감지 - ${htmlEscape(planLabel)}</b>`
      : `<b>ARSEN 신규 ${htmlEscape(planLabel)} 신청</b>`,
    `이름: ${displayValue(attempted?.name || member?.name)}`,
    `이메일: ${displayValue(attempted?.email)}`,
    `연락처: ${displayValue(attempted?.phone || member?.phone_masked || attempted?.phone_masked)}`,
    `신청ID: <code>${htmlEscape(member?.id || "-")}</code>`,
    `상태: ${htmlEscape(member?.status || "pending")}`,
    `신청 구분: ${displayValue(planLabel)}`,
    `등급: ${htmlEscape(member?.participation_grade || "-")}`,
    `성별/나이: ${displayValue(attempted?.gender || member?.gender)} / ${displayValue(attempted?.age || member?.age)}`,
    `직업/소속: ${displayValue(attempted?.job || member?.job)}`,
    `유입 경로: ${displayValue(attempted?.referral_source || member?.referral_source)}`,
    `AI 레벨: ${displayValue(attempted?.ai_level || member?.ai_level)}`,
    `사용 AI 도구: ${displayValue(attempted?.ai_tools || member?.ai_tools)}`,
    `AI 구독: ${displayValue(attempted?.ai_subscription || member?.ai_subscription)}`,
    `주당 AI 사용 시간: ${displayValue(attempted?.ai_weekly_hours || member?.ai_weekly_hours)}`,
    `AI 활용 분야: ${displayValue(attempted?.ai_use_cases || member?.ai_use_cases)}`,
    `모임 목적: ${displayValue(attempted?.group_goals || member?.group_goals)}`,
    `참여 방식: ${displayValue(attempted?.participation_type || member?.participation_type)}`,
    `참여 가능 지역: ${displayValue(attempted?.region || member?.region)}`,
    `참여 가능 시간: ${displayValue(attempted?.available_time_slots || member?.available_time_slots)}`,
    `선호 일정: ${displayValue(attempted?.preferred_schedule || member?.preferred_schedule)}`,
    `주 사용 기기: ${displayValue(attempted?.main_device || member?.main_device)}`,
    `코딩 가능: ${yesNo(attempted?.can_code ?? member?.can_code)}`,
    `발표/강의 가능: ${yesNo(attempted?.can_present ?? member?.can_present)}`,
    `보유 스킬: ${displayValue(attempted?.skills || member?.skills)}`,
    `기여 방식: ${displayValue(attempted?.contribution || member?.contribution)}`,
    `신청 이유: ${displayValue(attempted?.reason || member?.reason)}`,
    `단기 목표: ${displayValue(attempted?.short_term_goal || member?.short_term_goal)}`,
    `강의에서 해보고 싶은 내용: ${displayValue(attempted?.desired_outcome || member?.desired_outcome)}`,
    `준비 상태: ${displayValue(attempted?.preparedness || member?.preparedness)}`,
    `마케팅 동의: ${yesNo(attempted?.consent_marketing ?? member?.consent_marketing)}`,
  ];
  if (duplicate) {
    base.push(`중복 기준: ${htmlEscape(member?.duplicate_source || "-")}`);
    base.push(`이번 입력 이름: ${htmlEscape(attempted?.name || "-")}`);
  }
  return [...base, ...statsLines(counts)].join("\n");
}

function bookingSummaryLines(booking) {
  const amount = Number(booking?.payment_amount_krw || booking?.session_price_krw || DEFAULT_PRICE);
  const [dateText, timeText] = formatKoreanDateTimeRange(booking?.session_starts_at, booking?.session_ends_at);
  return [
    `예약ID: <code>${htmlEscape(booking?.id || "-")}</code>`,
    `신청자: ${htmlEscape(booking?.applicant_name || booking?.member_name || "-")} (${htmlEscape(noticePhone(booking?.phone_masked || ""))})`,
    `회원ID: <code>${htmlEscape(booking?.member_id || "-")}</code>`,
    `일정: ${htmlEscape(booking?.session_title || DEFAULT_TITLE)}`,
    `시간: ${htmlEscape(`${dateText} ${timeText}`.trim())}`,
    `예약상태: ${htmlEscape(booking?.status || "-")}`,
    `입금상태: ${htmlEscape(booking?.payment_status || "-")}`,
    `금액: ${amount.toLocaleString("ko-KR")}원`,
    `순서: 신청 ${booking?.request_rank || "-"} / 입금확정 ${booking?.paid_rank || "-"}`,
    `목표/내용: ${htmlEscape(compactText(booking?.desired_outcome))}`,
    `준비상태: ${htmlEscape(compactText(booking?.preparedness))}`,
  ];
}

function bookingMessage(booking, counts, duplicate = false) {
  return [
    duplicate ? "<b>ARSEN 중복 수강/예약 신청</b>" : "<b>ARSEN 신규 수강/예약 신청</b>",
    ...bookingSummaryLines(booking),
    ...statsLines(counts),
  ].join("\n");
}

async function sendTelegram(env, text, replyMarkup = null, kind = "application") {
  if (!telegramEnabled(env, kind)) return "disabled";
  if (!telegramConfigured(env, true)) return "not_configured";
  try {
    const response = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        chat_id: env.TELEGRAM_ADMIN_CHAT_ID,
        text,
        parse_mode: "HTML",
        disable_web_page_preview: true,
        ...(replyMarkup ? { reply_markup: replyMarkup } : {}),
      }),
    });
    return response.ok ? "ok" : "failed";
  } catch (_) {
    return "failed";
  }
}

async function answerTelegramCallback(env, callbackQueryId, text) {
  if (!callbackQueryId) return "missing_callback_id";
  if (!telegramConfigured(env, false)) return "not_configured";
  try {
    const response = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/answerCallbackQuery`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ callback_query_id: callbackQueryId, text, show_alert: false }),
    });
    return response.ok ? "ok" : "failed";
  } catch (_) {
    return "failed";
  }
}

function codeDeliveryMessage(member, code, env) {
  const name = member?.name || "신청자";
  return [
    `[ARSEN AI] ${name}님 강의 신청 확인 코드입니다.`,
    `코드: ${code}`,
    `예약자 확인: ${publicBaseUrl(env)}/frontend/status.html`,
    "정보 공유방: https://open.kakao.com/o/gm9tRoJh",
    "문의: https://open.kakao.com/o/s88zv6pf",
  ].join("\n");
}

function parseKstDate(value) {
  if (!value) return null;
  const text = String(value).trim();
  const normalized = /(?:Z|[+-]\d{2}:?\d{2})$/.test(text) ? text : `${text}+09:00`;
  const date = new Date(normalized);
  return Number.isNaN(date.getTime()) ? null : date;
}

function koreanTime(date) {
  const parts = new Intl.DateTimeFormat("ko-KR", {
    timeZone: "Asia/Seoul",
    hour: "numeric",
    minute: "2-digit",
    hour12: true,
  }).formatToParts(date);
  const dayPeriod = parts.find((part) => part.type === "dayPeriod")?.value || "";
  const hour = parts.find((part) => part.type === "hour")?.value || "";
  const minute = parts.find((part) => part.type === "minute")?.value || "00";
  return minute === "00" ? `${dayPeriod} ${hour}시` : `${dayPeriod} ${hour}시 ${minute}분`;
}

function formatKoreanDateTimeRange(startsAt, endsAt) {
  const start = parseKstDate(startsAt);
  const end = parseKstDate(endsAt);
  if (!start) return [startsAt || "-", ""];
  const month = new Intl.DateTimeFormat("en-US", { timeZone: "Asia/Seoul", month: "numeric" }).format(start);
  const day = new Intl.DateTimeFormat("en-US", { timeZone: "Asia/Seoul", day: "numeric" }).format(start);
  const year = new Intl.DateTimeFormat("en-US", { timeZone: "Asia/Seoul", year: "numeric" }).format(start);
  const weekday = new Intl.DateTimeFormat("ko-KR", { timeZone: "Asia/Seoul", weekday: "short" }).format(start);
  const dateText = `${year}년 ${month}월 ${day}일 (${weekday})`;
  let timeText = koreanTime(start);
  if (end) {
    timeText = `${timeText} - ${koreanTime(end)}`;
  }
  return [dateText, timeText];
}

function paymentAccountLines(paymentAccount) {
  if (!paymentAccount) return [];
  const bank = String(paymentAccount.bank || "").trim();
  const number = String(paymentAccount.number || "").trim();
  const holder = String(paymentAccount.holder || "").trim();
  const memo = String(paymentAccount.memo || "").trim();
  const account = [bank, number].filter(Boolean).join(" ");
  const lines = [];
  if (account) lines.push(`입금 계좌: ${account}`);
  if (holder) lines.push(`예금주: ${holder}`);
  if (memo) lines.push(`계좌 메모: ${memo}`);
  return lines;
}

async function selectedPaymentAccount(env, accountId) {
  const payload = await setting(env, "payment_accounts", { accounts: [], active_id: "" });
  const accounts = Array.isArray(payload.accounts) ? payload.accounts : [];
  const selectedId = accountId || payload.active_id || accounts[0]?.id || "";
  return accounts.find((account) => account.id === selectedId) || null;
}

function defaultPaymentGuide(booking, paymentAccount = null) {
  const [dateText, timeText] = formatKoreanDateTimeRange(booking?.session_starts_at, booking?.session_ends_at);
  const amount = Number(booking?.payment_amount_krw || booking?.session_price_krw || DEFAULT_PRICE);
  const custom = String(booking?.session_payment_guide || "").trim();
  const lines = [
    "[입금 안내]",
    `과정: ${booking?.session_title || DEFAULT_TITLE}`,
    `일정: ${dateText}`,
    `시간: ${timeText || "-"}`,
    `장소: ${booking?.session_location || booking?.location || DEFAULT_LOCATION}`,
    `금액: ${amount.toLocaleString("ko-KR")}원`,
  ];
  const accountLines = paymentAccountLines(paymentAccount);
  if (accountLines.length) {
    lines.push("", ...accountLines);
  } else if (!custom) {
    lines.push("", "계좌 정보는 운영자가 확인 후 개별 안내합니다.");
  }
  lines.push("", "입금 후 입금자명과 신청자명이 다르면 운영자에게 알려주세요.");
  if (custom) lines.push("", custom);
  return lines.join("\n").trim();
}

function defaultLocationGuide(booking) {
  const [dateText, timeText] = formatKoreanDateTimeRange(booking?.session_starts_at, booking?.session_ends_at);
  const name = booking?.applicant_name || booking?.member_name || "신청자";
  return [
    "[장소 안내]",
    `${name}님, 입금 확인되어 예약이 확정되었습니다.`,
    `과정: ${booking?.session_title || DEFAULT_TITLE}`,
    `일정: ${dateText}`,
    `시간: ${timeText || "-"}`,
    `장소: ${booking?.session_location || booking?.location || DEFAULT_LOCATION}`,
    "준비물: 노트북, 충전기, 사용 중인 AI 계정 정보, 자동화하고 싶은 업무 예시",
    "도착 전 문의가 있으면 1:1 문의방으로 편하게 남겨주세요.",
  ].join("\n").trim();
}

function defaultRefundGuide(booking) {
  const amount = Number(booking?.payment_amount_krw || DEFAULT_PRICE);
  return [
    "[환불 확인 안내]",
    `${booking?.applicant_name || booking?.member_name || "신청자"}님 예약 취소가 접수되었습니다.`,
    `확인 필요 금액: ${amount.toLocaleString("ko-KR")}원`,
    "입금이 완료된 예약이어서 운영자가 환불 계좌를 확인한 뒤 환불을 진행해야 합니다.",
    "환불받으실 은행/계좌번호/예금주를 보내주시면 확인 후 처리하겠습니다.",
  ].join("\n").trim();
}

function isApiPath(path) {
  return (
    path === "/health" ||
    path === "/sessions" ||
    path === "/apply" ||
    path === "/stats" ||
    path === "/api/site-theme" ||
    path === "/api/education" ||
    path === "/api/license/activate" ||
    path === "/api/license/verify" ||
    path.startsWith("/api/yoonbot/") ||
    path === "/api/review-board" ||
    path.startsWith("/api/review-board/submit/") ||
    path === "/telegram/webhook" ||
    path.startsWith("/admin/") ||
    path.startsWith("/member/") ||
    path.startsWith("/members") ||
    path.startsWith("/approve/") ||
    path.startsWith("/reject/") ||
    path.startsWith("/regen-code/") ||
    path.startsWith("/blacklist/") ||
    path.startsWith("/unblacklist/") ||
    path.startsWith("/scheduler/")
  );
}

async function logAction(env, memberId, action, detail, request) {
  await env.DB.prepare(
    "INSERT INTO member_logs (id, member_id, action, detail, ip, created_at) VALUES (?, ?, ?, ?, ?, ?)"
  )
    .bind(crypto.randomUUID(), memberId || "system", action, detail || "", request.headers.get("cf-connecting-ip") || "", now())
    .run();
}

async function setting(env, key, fallback) {
  const row = await env.DB.prepare("SELECT value FROM operator_settings WHERE key=?").bind(key).first();
  if (!row) return fallback;
  try {
    return JSON.parse(row.value);
  } catch (_) {
    return fallback;
  }
}

async function saveSetting(env, key, value) {
  await env.DB.prepare(
    "INSERT INTO operator_settings (key, value, updated_at) VALUES (?, ?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at"
  )
    .bind(key, JSON.stringify(value), now())
    .run();
}

function themeProfile(themeId) {
  return SITE_THEME_PROFILES.find((theme) => theme.id === themeId && theme.enabled !== false) || null;
}

async function siteThemePayload(env) {
  const saved = await setting(env, "site_theme", {});
  const activeId = themeProfile(saved.active_theme_id) ? saved.active_theme_id : DEFAULT_SITE_THEME_ID;
  const active = themeProfile(activeId) || themeProfile(DEFAULT_SITE_THEME_ID);
  const themes = SITE_THEME_PROFILES.map((theme) => ({ ...theme, available: true }));
  return {
    active_theme_id: active?.id || DEFAULT_SITE_THEME_ID,
    active_theme: { ...active, available: true },
    themes,
    updated_at: saved.updated_at || "",
  };
}

async function saveSiteTheme(env, activeThemeId) {
  const active = themeProfile(activeThemeId);
  if (!active) return null;
  const payload = { active_theme_id: active.id, updated_at: now() };
  await saveSetting(env, "site_theme", payload);
  return siteThemePayload(env);
}

async function one(env, sql, ...params) {
  return env.DB.prepare(sql).bind(...params).first();
}

async function all(env, sql, ...params) {
  const result = await env.DB.prepare(sql).bind(...params).all();
  return result.results || [];
}

function safeMember(row) {
  if (!row) return null;
  const copy = { ...row };
  delete copy.email_encrypted;
  delete copy.phone_encrypted;
  return copy;
}

function withCapacityFields(row) {
  if (!row) return row;
  const copy = { ...row };
  const capacity = Number(copy.capacity_max || 0);
  const active = Number(copy.active_booking_count || 0);
  const requested = Number(copy.requested_count || 0);
  const confirmed = Number(copy.confirmed_booking_count ?? copy.confirmed_count ?? 0);
  copy.active_booking_count = active;
  copy.requested_count = requested;
  copy.confirmed_booking_count = confirmed;
  copy.remaining_capacity = capacity > 0 ? Math.max(capacity - active, 0) : 0;
  copy.is_request_full = capacity > 0 && active >= capacity;
  return copy;
}

function responseText(text, type = "text/plain; charset=utf-8", init = {}) {
  const headers = new Headers(init.headers || {});
  headers.set("content-type", type);
  return new Response(text, { ...init, headers });
}

function csvCell(value) {
  const text = String(value ?? "");
  if (/[",\n\r]/.test(text)) return `"${text.replace(/"/g, '""')}"`;
  return text;
}

function csvRows(rows) {
  return rows.map((row) => row.map(csvCell).join(",")).join("\n") + "\n";
}

function listFromValue(value) {
  if (Array.isArray(value)) return value.map((item) => String(item).trim()).filter(Boolean);
  const text = String(value || "").trim();
  if (!text) return [];
  if (text.startsWith("[") && text.endsWith("]")) {
    try {
      const parsed = JSON.parse(text);
      if (Array.isArray(parsed)) return parsed.map((item) => String(item).trim()).filter(Boolean);
    } catch (_) {
      // Fall through to line parsing.
    }
  }
  return text
    .replace(/\r/g, "\n")
    .replace(/,/g, "\n")
    .split("\n")
    .map((item) => item.trim())
    .filter(Boolean);
}

function listText(value) {
  return JSON.stringify(listFromValue(value));
}

function reviewInviteStatus(value) {
  const status = String(value || "active").trim().toLowerCase();
  return ["active", "revoked"].includes(status) ? status : "active";
}

async function reviewTokenHash(token) {
  const encoded = new TextEncoder().encode(String(token || ""));
  const digest = await crypto.subtle.digest("SHA-256", encoded);
  return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

function reviewInviteRow(row) {
  if (!row) return null;
  const copy = { ...row };
  copy.max_submissions = Number(copy.max_submissions || 0);
  copy.submitted_count = Number(copy.submitted_count || 0);
  copy.is_open =
    copy.status === "active" &&
    (!copy.expires_at || String(copy.expires_at) >= now()) &&
    (!copy.max_submissions || copy.submitted_count < copy.max_submissions);
  delete copy.token_hash;
  return copy;
}

function reviewInstructorStatus(value) {
  const status = String(value || "active").trim().toLowerCase();
  return ["active", "inactive"].includes(status) ? status : "active";
}

function reviewEntryStatus(value) {
  const status = String(value || "draft").trim().toLowerCase();
  return ["draft", "public", "hidden"].includes(status) ? status : "draft";
}

function reviewInstructorRow(row) {
  if (!row) return null;
  return {
    ...row,
    specialties: listFromValue(row.specialties),
    sort_order: Number(row.sort_order || 0),
  };
}

function reviewEntryRow(row) {
  if (!row) return null;
  return {
    ...row,
    tags: listFromValue(row.tags),
    image_urls: listFromValue(row.image_urls),
    privacy_checked: Boolean(row.privacy_checked),
    featured: Boolean(row.featured),
  };
}

async function reviewBoardRows(env, publicOnly = false) {
  const instructors = publicOnly
    ? await all(env, "SELECT * FROM review_instructors WHERE status='active' ORDER BY sort_order ASC, created_at DESC")
    : await all(env, "SELECT * FROM review_instructors ORDER BY sort_order ASC, created_at DESC");
  const entries = publicOnly
    ? await all(
        env,
        `SELECT e.*, i.name AS instructor_name, i.role AS instructor_role
         FROM review_entries e
         LEFT JOIN review_instructors i ON i.id=e.instructor_id
         WHERE e.status='public'
           AND e.privacy_checked=1
           AND (i.status='active' OR i.id IS NULL)
         ORDER BY e.featured DESC, COALESCE(e.class_date, e.created_at) DESC, e.created_at DESC`
      )
    : await all(
        env,
        `SELECT e.*, i.name AS instructor_name, i.role AS instructor_role
         FROM review_entries e
         LEFT JOIN review_instructors i ON i.id=e.instructor_id
         ORDER BY e.created_at DESC`
      );
  const mappedEntries = entries.map(reviewEntryRow);
  const inviteRows = publicOnly
    ? []
    : await all(
        env,
        `SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
         FROM review_invites ri
         LEFT JOIN review_instructors i ON i.id=ri.instructor_id
         ORDER BY ri.created_at DESC`
      );
  return {
    instructors: instructors.map(reviewInstructorRow),
    entries: mappedEntries,
    invites: inviteRows.map(reviewInviteRow),
    stats: {
      instructors: instructors.length,
      entries: mappedEntries.length,
      public_entries: mappedEntries.filter((item) => item.status === "public").length,
      featured_entries: mappedEntries.filter((item) => item.featured).length,
    },
  };
}

async function getReviewInstructor(env, id) {
  return reviewInstructorRow(await one(env, "SELECT * FROM review_instructors WHERE id=?", id));
}

async function getReviewEntry(env, id) {
  return reviewEntryRow(
    await one(
      env,
      `SELECT e.*, i.name AS instructor_name, i.role AS instructor_role
       FROM review_entries e
       LEFT JOIN review_instructors i ON i.id=e.instructor_id
       WHERE e.id=?`,
      id
    )
  );
}

async function getReviewInvite(env, id) {
  return reviewInviteRow(
    await one(
      env,
      `SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
       FROM review_invites ri
       LEFT JOIN review_instructors i ON i.id=ri.instructor_id
       WHERE ri.id=?`,
      id
    )
  );
}

async function getReviewInviteByToken(env, token) {
  const tokenHash = await reviewTokenHash(token);
  return reviewInviteRow(
    await one(
      env,
      `SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
       FROM review_invites ri
       LEFT JOIN review_instructors i ON i.id=ri.instructor_id
       WHERE ri.token_hash=?`,
      tokenHash
    )
  );
}

function safePublicBooking(row) {
  if (!row) return null;
  return {
    id: row.id,
    session_id: row.session_id,
    session_title: row.session_title,
    session_starts_at: row.session_starts_at,
    session_ends_at: row.session_ends_at,
    location: row.location,
    status: row.status,
    payment_status: row.payment_status,
    payment_amount_krw: row.payment_amount_krw,
    created_at: row.created_at,
    updated_at: row.updated_at,
  };
}

async function sessionRows(env, includeClosed = false) {
  const where = includeClosed ? "1=1" : "status IN ('open','full') AND starts_at >= datetime('now', '-1 day')";
  const rows = await all(
    env,
    `SELECT s.*,
      (SELECT COUNT(*) FROM bookings b WHERE b.session_id=s.id AND b.status NOT IN ('canceled','rejected','no_show')) AS active_booking_count,
      (SELECT COUNT(*) FROM bookings b WHERE b.session_id=s.id AND b.status IN ('requested','payment_guide_sent','payment_pending','payment_confirmed')) AS requested_count,
      (SELECT COUNT(*) FROM bookings b WHERE b.session_id=s.id AND b.status='confirmed') AS confirmed_booking_count
     FROM sessions s
     WHERE ${where}
     ORDER BY starts_at ASC`
  );
  return rows.map(withCapacityFields);
}

async function getSession(env, sessionId) {
  const row = await one(
    env,
    `SELECT s.*,
      (SELECT COUNT(*) FROM bookings b WHERE b.session_id=s.id AND b.status NOT IN ('canceled','rejected','no_show')) AS active_booking_count,
      (SELECT COUNT(*) FROM bookings b WHERE b.session_id=s.id AND b.status IN ('requested','payment_guide_sent','payment_pending','payment_confirmed')) AS requested_count,
      (SELECT COUNT(*) FROM bookings b WHERE b.session_id=s.id AND b.status='confirmed') AS confirmed_booking_count
     FROM sessions s WHERE s.id=?`,
    sessionId
  );
  return withCapacityFields(row);
}

function sessionAcceptance(session) {
  if (!session) return [false, "일정을 찾을 수 없습니다."];
  if (!["open", "full"].includes(session.status)) return [false, "공개된 일정만 예약할 수 있습니다."];
  if (session.status === "full") return [false, "이미 마감된 일정입니다."];
  const capacity = Number(session.capacity_max || 0);
  const active = Number(session.active_booking_count || 0);
  if (capacity > 0 && active >= capacity) return [false, "정원이 마감되었습니다."];
  return [true, ""];
}

async function refreshSessionCount(env, sessionId) {
  if (!sessionId) return;
  const confirmedRow = await one(
    env,
    "SELECT COUNT(*) AS count FROM bookings WHERE session_id=? AND status='confirmed'",
    sessionId
  );
  const activeRow = await one(
    env,
    "SELECT COUNT(*) AS count FROM bookings WHERE session_id=? AND status NOT IN ('canceled','rejected','no_show')",
    sessionId
  );
  const session = await one(env, "SELECT capacity_max, status FROM sessions WHERE id=?", sessionId);
  const confirmed = Number(confirmedRow?.count || 0);
  const active = Number(activeRow?.count || 0);
  const capacity = Number(session?.capacity_max || 0);
  const nextStatus = session && ["open", "full"].includes(session.status)
    ? (capacity > 0 && active >= capacity ? "full" : "open")
    : session?.status || null;
  await env.DB.prepare("UPDATE sessions SET confirmed_count=?, status=COALESCE(?, status), updated_at=? WHERE id=?")
    .bind(confirmed, nextStatus, now(), sessionId)
    .run();
}

async function bookingRows(env, { status = "", sessionId = "" } = {}) {
  const clauses = [];
  const params = [];
  if (status) {
    clauses.push("b.status=?");
    params.push(status);
  }
  if (sessionId) {
    clauses.push("b.session_id=?");
    params.push(sessionId);
  }
  const where = clauses.length ? `WHERE ${clauses.join(" AND ")}` : "";
  return all(
    env,
    `WITH booking_order AS (
       SELECT
         id,
         ROW_NUMBER() OVER (
           PARTITION BY session_id
           ORDER BY created_at ASC, id ASC
         ) AS request_rank,
         ROW_NUMBER() OVER (
           PARTITION BY session_id
           ORDER BY
             CASE WHEN confirmed_at IS NULL THEN 1 ELSE 0 END,
             confirmed_at ASC,
             created_at ASC,
             id ASC
         ) AS paid_rank_raw
       FROM bookings
       WHERE status NOT IN ('canceled','rejected','no_show')
     ),
     waitlist_order AS (
       SELECT
         id,
         ROW_NUMBER() OVER (
           PARTITION BY session_id
           ORDER BY created_at ASC, id ASC
         ) AS waitlist_rank
       FROM bookings
       WHERE status='waitlisted'
     )
     SELECT b.*, s.title AS session_title, s.starts_at AS session_starts_at, s.ends_at AS session_ends_at,
      s.location AS session_location, s.location AS location, s.capacity_max AS session_capacity_max,
      s.price_krw AS session_price_krw, s.payment_guide AS session_payment_guide,
      bo.request_rank,
      CASE WHEN b.status='confirmed' AND b.payment_status='paid' THEN bo.paid_rank_raw END AS paid_rank,
      CASE WHEN b.status='waitlisted' THEN wo.waitlist_rank END AS waitlist_rank,
      m.name AS member_name, m.status AS member_status, m.ai_level AS member_ai_level, m.plan_type AS member_plan_type
     FROM bookings b
     LEFT JOIN sessions s ON s.id=b.session_id
     LEFT JOIN booking_order bo ON bo.id=b.id
     LEFT JOIN waitlist_order wo ON wo.id=b.id
     LEFT JOIN members m ON m.id=b.member_id
     ${where}
     ORDER BY b.created_at DESC`,
    ...params
  );
}

async function getBooking(env, bookingId) {
  const rows = await bookingRows(env);
  return rows.find((row) => row.id === bookingId) || null;
}

async function createBooking(env, data) {
  const id = crypto.randomUUID();
  const created = now();
  await env.DB.prepare(
    `INSERT INTO bookings (
      id, session_id, member_id, applicant_name, phone_masked, desired_outcome, preparedness,
      status, payment_status, payment_amount_krw, payment_note, confirmed_at, canceled_at, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      id,
      data.session_id || null,
      data.member_id || null,
      data.applicant_name || "신청자",
      data.phone_masked || "",
      data.desired_outcome || "",
      data.preparedness || "",
      data.status || "requested",
      data.payment_status || "not_sent",
      Number(data.payment_amount_krw || DEFAULT_PRICE),
      data.payment_note || "",
      data.confirmed_at || null,
      data.canceled_at || null,
      created,
      created
    )
    .run();
  await refreshSessionCount(env, data.session_id);
  return id;
}

async function createEdgeMember(env, data, envSource = env) {
  const id = crypto.randomUUID();
  const created = now();
  const phone = normalizePhoneForStorage(data.phone || "");
  const email = String(data.email || "").trim().toLowerCase();
  await env.DB.prepare(
    `INSERT INTO members (
      id, name, email_encrypted, email_hash, phone_hash, phone_masked, phone_encrypted,
      gender, age, job, referral_source, reason, ai_level, plan_type,
      ai_tools, ai_subscription, ai_weekly_hours, ai_use_cases, group_goals, short_term_goal,
      participation_type, preferred_schedule, available_time_slots, region, main_device, can_code, can_present,
      skills, contribution, participation_grade, consent_personal, consent_marketing,
      consent_at, consent_version, status, access_code, code_issued_at, approved_at, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      id,
      data.name || "신청자",
      await encryptLegacyValue(email, envSource, "EMAIL_SECRET_KEY"),
      email ? await hmacHex(email, envSource, "EMAIL_SECRET_KEY") : "",
      phone ? await hmacHex(phone, envSource, "PHONE_SECRET_KEY") : "",
      maskPhone(phone),
      await encryptLegacyValue(phone, envSource, "PHONE_SECRET_KEY"),
      data.gender || "",
      Number(data.age || 0),
      data.job || "운영자 수동 등록",
      data.referral_source || "manual",
      data.reason || data.short_term_goal || "",
      data.ai_level || "",
      data.plan_type || "full",
      data.ai_tools || "",
      data.ai_subscription || "",
      data.ai_weekly_hours || "",
      data.ai_use_cases || "",
      data.group_goals || "",
      data.short_term_goal || "",
      data.participation_type || "",
      data.preferred_schedule || "",
      Array.isArray(data.available_time_slots) ? JSON.stringify(data.available_time_slots) : data.available_time_slots || "",
      data.region || "",
      data.main_device || "",
      data.can_code ? 1 : 0,
      data.can_present ? 1 : 0,
      data.skills || "",
      data.contribution || "",
      data.participation_grade || gradeCount(data),
      1,
      data.consent_marketing ? 1 : 0,
      created,
      data.consent_version || "manual-admin-cloudflare-v1",
      data.status || "approved",
      data.access_code || null,
      data.access_code ? created : null,
      data.status === "approved" ? created : null,
      created
    )
    .run();
  return id;
}

async function findMemberByPhone(env, phone) {
  for (const candidate of phoneCandidates(phone)) {
    const phoneHash = await hmacHex(candidate, env, "PHONE_SECRET_KEY");
    const member = await one(env, "SELECT * FROM members WHERE phone_hash=? ORDER BY created_at DESC LIMIT 1", phoneHash);
    if (member) return member;
  }
  return null;
}

async function findDuplicateMember(env, { phone = "", email = "" } = {}) {
  for (const candidate of phoneCandidates(phone)) {
    const phoneHash = await hmacHex(candidate, env, "PHONE_SECRET_KEY");
    const member = await one(
      env,
      "SELECT * FROM members WHERE phone_hash=? AND status!='erased' ORDER BY created_at DESC LIMIT 1",
      phoneHash
    );
    if (member) return { ...member, duplicate_source: "phone" };
  }
  const cleanEmail = String(email || "").trim().toLowerCase();
  if (cleanEmail) {
    const emailHash = await hmacHex(cleanEmail, env, "EMAIL_SECRET_KEY");
    const member = await one(
      env,
      "SELECT * FROM members WHERE email_hash=? AND status!='erased' ORDER BY created_at DESC LIMIT 1",
      emailHash
    );
    if (member) return { ...member, duplicate_source: "email" };
  }
  return null;
}

async function handleApply(request, env) {
  const data = await readJson(request);
  const name = String(data.name || "").trim();
  const phone = normalizePhoneForStorage(data.phone || "");
  if (!name || !phone) return fail(400, "이름과 연락처를 입력하세요.");
  if (!data.consent_personal) return fail(400, "개인정보 동의가 필요합니다.");

  const email = String(data.email || "").trim().toLowerCase();
  const duplicate = await findDuplicateMember(env, { phone: data.phone || phone, email });
  if (duplicate) {
    if (duplicate.status === "blacklist") return fail(409, "현재 신청할 수 없는 연락처입니다.");
    await logAction(env, duplicate.id, "duplicate_apply", `source=${duplicate.duplicate_source}`, request);
    const counts = await stats(env);
    const hermesStatus = await sendTelegram(
      env,
      applicationMessage(duplicate, counts, true, { ...data, phone_masked: maskPhone(phone) }),
      memberKeyboard(env, duplicate.id),
      "application"
    );
    await logAction(env, duplicate.id, "duplicate_apply_notify", hermesStatus, request);
    return json({
      ok: true,
      duplicate: true,
      message: "이미 신청이 접수되어 있습니다. 기존 신청 상태를 기준으로 안내드릴게요.",
      member_id: duplicate.id,
      status: duplicate.status,
      next_steps: [
        "기존 신청이 대기 중이면 운영자가 순서대로 확인합니다.",
        "이미 승인된 경우 예약자 확인 페이지에서 기존 연락처와 코드를 사용해 수강 신청을 진행하세요.",
        "코드를 잊었다면 운영자에게 재발급을 요청해주세요.",
      ],
      reservation: null,
      payment: null,
    });
  }

  const phoneHash = await hmacHex(phone, env, "PHONE_SECRET_KEY");
  const emailHash = email ? await hmacHex(email, env, "EMAIL_SECRET_KEY") : "";

  const id = crypto.randomUUID();
  const created = now();
  const selectedSession = data.session_id ? await getSession(env, data.session_id) : null;
  const member = {
    ...data,
    preferred_schedule:
      data.preferred_schedule || (selectedSession ? `${selectedSession.starts_at} / ${selectedSession.location}` : ""),
  };
  await env.DB.prepare(
    `INSERT INTO members (
      id, name, email_encrypted, email_hash, phone_hash, phone_masked, phone_encrypted,
      gender, age, job, referral_source, reason, ai_level, plan_type,
      ai_tools, ai_subscription, ai_weekly_hours, ai_use_cases, group_goals, short_term_goal,
      participation_type, preferred_schedule, available_time_slots, region, main_device, can_code, can_present,
      skills, contribution, participation_grade, consent_personal, consent_marketing,
      consent_at, consent_version, status, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      id,
      name,
      await encryptLegacyValue(email, env, "EMAIL_SECRET_KEY"),
      emailHash,
      phoneHash,
      maskPhone(phone),
      await encryptLegacyValue(phone, env, "PHONE_SECRET_KEY"),
      member.gender || "",
      Number(member.age || 0),
      member.job || "",
      member.referral_source || "",
      member.reason || member.desired_outcome || "",
      member.ai_level || "",
      member.plan_type || "full",
      Array.isArray(member.ai_tools) ? JSON.stringify(member.ai_tools) : member.ai_tools || "",
      member.ai_subscription || "",
      member.ai_weekly_hours || "",
      Array.isArray(member.ai_use_cases) ? JSON.stringify(member.ai_use_cases) : member.ai_use_cases || "",
      Array.isArray(member.group_goals) ? JSON.stringify(member.group_goals) : member.group_goals || "",
      member.short_term_goal || member.desired_outcome || "",
      member.participation_type || "",
      member.preferred_schedule || "",
      Array.isArray(member.available_time_slots) ? JSON.stringify(member.available_time_slots) : member.available_time_slots || "",
      member.region || "",
      member.main_device || "",
      member.can_code ? 1 : 0,
      member.can_present ? 1 : 0,
      member.skills || member.preparedness || "",
      member.contribution || "",
      gradeCount(member),
      member.consent_personal ? 1 : 0,
      member.consent_marketing ? 1 : 0,
      created,
      member.consent_version || "cloudflare-v1",
      "pending",
      created
    )
    .run();
  await logAction(env, id, "apply", `plan=${member.plan_type || "full"}`, request);
  const createdMember = await one(env, "SELECT * FROM members WHERE id=?", id);
  const hermesStatus = await sendTelegram(
    env,
    applicationMessage(createdMember, await stats(env), false, member),
    memberKeyboard(env, id),
    "application"
  );
  await logAction(env, id, "hermes_notify", hermesStatus, request);
  return json({
    ok: true,
    message: "신청이 접수되었습니다.",
    member_id: id,
    booking_id: null,
    next_steps: [
      "운영자가 신청 내용을 확인한 뒤 승인 코드를 발급합니다.",
      "승인 코드를 받은 뒤 예약자 확인 페이지에서 원하는 일정을 예약합니다.",
      "입금 확인 후 자리가 확정됩니다.",
    ],
    reservation: null,
    payment: null,
  });
}

async function handlePublicVerify(request, env) {
  const body = await readJson(request);
  const member = await findMemberByPhone(env, body.phone || "");
  if (!member) return fail(404, "신청 정보를 찾을 수 없습니다. 신청한 전화번호를 확인해주세요.");
  if (member.access_code !== String(body.code || "").trim()) return fail(400, "코드 확인에 실패했습니다.");
  if (member.status !== "approved") return fail(400, `현재 신청 상태는 ${member.status}입니다.`);
  const bookings = await bookingRows(env);
  return json({
    ok: true,
    data: {
      member: safeMember(member),
      bookings: bookings.filter((row) => row.member_id === member.id).map(safePublicBooking),
    },
  });
}

async function handlePublicBooking(request, env) {
  const body = await readJson(request);
  const member = await one(env, "SELECT * FROM members WHERE id=?", body.member_id || "");
  if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
  if (member.status !== "approved") return fail(400, "승인된 신청자만 예약할 수 있습니다.");
  if (member.access_code !== String(body.code || "").trim()) return fail(400, "코드 확인에 실패했습니다.");
  const existing = await one(
    env,
    "SELECT * FROM bookings WHERE member_id=? AND session_id=? AND status NOT IN ('canceled','rejected','no_show') LIMIT 1",
    member.id,
    body.session_id
  );
  if (existing) {
    const existingBooking = await getBooking(env, existing.id);
    return json({ ok: true, duplicate: true, message: "이미 접수된 예약 신청이 있습니다.", data: safePublicBooking(existingBooking) });
  }
  const session = await getSession(env, body.session_id || "");
  const [ok, reason] = sessionAcceptance(session);
  if (!ok) return fail(400, reason);
  const bookingId = await createBooking(env, {
    session_id: body.session_id,
    member_id: member.id,
    applicant_name: member.name,
    phone_masked: member.phone_masked,
    desired_outcome: body.desired_outcome || member.short_term_goal || member.reason || "",
    preparedness: body.preparedness || "",
    payment_amount_krw: Number(session.price_krw || DEFAULT_PRICE),
  });
  await logAction(env, member.id, "booking_requested_public", `booking_id=${bookingId}`, request);
  const booking = await getBooking(env, bookingId);
  await sendTelegram(env, bookingMessage(booking, await stats(env), false), bookingKeyboard(env, bookingId), "booking");
  return json({ ok: true, message: "예약 신청이 접수되었습니다.", data: safePublicBooking(booking) });
}

async function telegramCallbackResult(env, data, request) {
  const parts = String(data || "").split(":");
  if (parts.length !== 3 || parts[0] !== "arsen") return "지원하지 않는 버튼입니다.";
  const [_, action, targetId] = parts;

  if (action === "approve") {
    const member = await one(env, "SELECT * FROM members WHERE id=?", targetId);
    if (!member) return "신청자를 찾을 수 없습니다.";
    if (["blacklist", "erased", "rejected"].includes(member.status)) {
      return `현재 상태가 ${member.status}라 코드 발급을 중단했습니다.`;
    }
    const code = member.access_code || accessCode();
    const issuedAt = now();
    await env.DB.prepare("UPDATE members SET status='approved', access_code=?, code_issued_at=?, approved_at=COALESCE(approved_at, ?) WHERE id=?")
      .bind(code, issuedAt, issuedAt, targetId)
      .run();
    await logAction(env, targetId, "telegram_approve_code_issued", "button=approve", request);
    const updated = await one(env, "SELECT * FROM members WHERE id=?", targetId);
    const delivery = codeDeliveryMessage(updated, code, env);
    await sendTelegram(
      env,
      [
        "<b>ARSEN 코드 발급 완료</b>",
        `이름: ${htmlEscape(updated?.name || "-")}`,
        `회원ID: <code>${htmlEscape(targetId)}</code>`,
        `코드: <code>${htmlEscape(code)}</code>`,
        "",
        "안내문자/카톡 복사용:",
        htmlEscape(delivery),
      ].join("\n"),
      memberKeyboard(env, targetId),
      "button"
    );
    return "승인 및 코드 발급 완료";
  }

  if (action === "payguide") {
    const booking = await getBooking(env, targetId);
    if (!booking) return "예약 신청을 찾을 수 없습니다.";
    const paymentAccount = await selectedPaymentAccount(env);
    const guide = defaultPaymentGuide(booking, paymentAccount);
    await env.DB.prepare("UPDATE bookings SET status='payment_guide_sent', payment_status='guide_sent', payment_note=?, updated_at=? WHERE id=?")
      .bind(guide, now(), targetId)
      .run();
    await logAction(env, targetId, "telegram_payment_guide_sent", "manual_copy", request);
    await sendTelegram(
      env,
      [
        "<b>ARSEN 입금 안내 문구</b>",
        `예약ID: <code>${htmlEscape(targetId)}</code>`,
        "신청자에게 자동 문자/카톡 전송은 하지 않았습니다. 아래 문구를 복사해 전달하세요.",
        "",
        htmlEscape(guide),
      ].join("\n"),
      bookingKeyboard(env, targetId),
      "button"
    );
    return "입금 안내 문구 생성 완료";
  }

  if (action === "confirm") {
    const booking = await getBooking(env, targetId);
    if (!booking) return "예약 신청을 찾을 수 없습니다.";
    if (booking.status !== "confirmed" && booking.session_id) {
      await refreshSessionCount(env, booking.session_id);
      const session = await getSession(env, booking.session_id);
      const confirmed = Number(session?.confirmed_booking_count || 0);
      const capacity = Number(session?.capacity_max || 0);
      if (capacity > 0 && confirmed >= capacity) return "정원이 이미 마감되어 확정할 수 없습니다.";
    }
    await env.DB.prepare("UPDATE bookings SET status='confirmed', payment_status='paid', payment_note=?, confirmed_at=COALESCE(confirmed_at, ?), updated_at=? WHERE id=?")
      .bind(booking.payment_note || "텔레그램 버튼 입금 확인", now(), now(), targetId)
      .run();
    await refreshSessionCount(env, booking.session_id);
    await logAction(env, targetId, "telegram_payment_confirmed", "manual_confirm", request);
    const updated = await getBooking(env, targetId);
    const guide = defaultLocationGuide(updated);
    await sendTelegram(
      env,
      [
        "<b>ARSEN 입금 확인 + 장소 안내</b>",
        `예약ID: <code>${htmlEscape(targetId)}</code>`,
        "신청자에게 자동 문자/카톡 전송은 하지 않았습니다. 아래 장소 안내를 복사해 전달하세요.",
        "",
        htmlEscape(guide),
      ].join("\n"),
      bookingKeyboard(env, targetId),
      "button"
    );
    return "입금 확인 및 예약 확정 완료";
  }

  if (action === "location") {
    const booking = await getBooking(env, targetId);
    if (!booking) return "예약 신청을 찾을 수 없습니다.";
    const guide = defaultLocationGuide(booking);
    await logAction(env, targetId, "telegram_location_guide_viewed", "manual_copy", request);
    await sendTelegram(
      env,
      [
        "<b>ARSEN 장소 안내 문구</b>",
        `예약ID: <code>${htmlEscape(targetId)}</code>`,
        "신청자에게 자동 문자/카톡 전송은 하지 않았습니다. 아래 문구를 복사해 전달하세요.",
        "",
        htmlEscape(guide),
      ].join("\n"),
      bookingKeyboard(env, targetId),
      "button"
    );
    return "장소 안내 문구 생성 완료";
  }

  return "지원하지 않는 버튼입니다.";
}

async function handleTelegramWebhook(request, env) {
  const expected = String(env.TELEGRAM_WEBHOOK_SECRET || "");
  if (!expected) return fail(503, "Telegram webhook secret is not configured.");
  if (request.headers.get("X-Telegram-Bot-Api-Secret-Token") !== expected) {
    return fail(401, "Invalid Telegram webhook secret.");
  }
  const payload = await readJson(request);
  const callback = payload.callback_query || {};
  const message = await telegramCallbackResult(env, callback.data || "", request);
  await answerTelegramCallback(env, callback.id || "", message);
  return json({ ok: true, message });
}

async function stats(env) {
  const members = await one(env, "SELECT COUNT(*) AS count FROM members WHERE status!='erased'");
  const pending = await one(env, "SELECT COUNT(*) AS count FROM members WHERE status='pending'");
  const approved = await one(env, "SELECT COUNT(*) AS count FROM members WHERE status='approved'");
  const rejected = await one(env, "SELECT COUNT(*) AS count FROM members WHERE status='rejected'");
  const blacklist = await one(env, "SELECT COUNT(*) AS count FROM members WHERE status='blacklist'");
  const erased = await one(env, "SELECT COUNT(*) AS count FROM members WHERE status='erased'");
  const bookings = await one(env, "SELECT COUNT(*) AS count FROM bookings");
  const requested = await one(env, "SELECT COUNT(*) AS count FROM bookings WHERE status='requested'");
  const active = await one(env, "SELECT COUNT(*) AS count FROM bookings WHERE status NOT IN ('canceled','rejected','no_show')");
  return {
    total: Number(members?.count || 0),
    pending: Number(pending?.count || 0),
    approved: Number(approved?.count || 0),
    rejected: Number(rejected?.count || 0),
    blacklist: Number(blacklist?.count || 0),
    erased: Number(erased?.count || 0),
    bookings: Number(bookings?.count || 0),
    requested_bookings: Number(requested?.count || 0),
    active_bookings: Number(active?.count || 0),
  };
}

async function databaseCounts(env) {
  const [members, sessions, bookings, licenses, orders, logs, settings] = await Promise.all([
    one(env, "SELECT COUNT(*) AS count FROM members"),
    one(env, "SELECT COUNT(*) AS count FROM sessions"),
    one(env, "SELECT COUNT(*) AS count FROM bookings"),
    one(env, "SELECT COUNT(*) AS count FROM licenses"),
    one(env, "SELECT COUNT(*) AS count FROM orders"),
    one(env, "SELECT COUNT(*) AS count FROM member_logs"),
    one(env, "SELECT COUNT(*) AS count FROM operator_settings"),
  ]);
  return {
    members: Number(members?.count || 0),
    sessions: Number(sessions?.count || 0),
    bookings: Number(bookings?.count || 0),
    licenses: Number(licenses?.count || 0),
    orders: Number(orders?.count || 0),
    member_logs: Number(logs?.count || 0),
    operator_settings: Number(settings?.count || 0),
  };
}

async function recentMaskedMembers(env, limit = 8) {
  return all(
    env,
    `SELECT id, name, phone_masked, status, created_at,
      '' AS sheets_status,
      'cloudflare-no-send' AS hermes_status,
      'cloudflare-d1' AS backup_status,
      (
        SELECT status
        FROM bookings b
        WHERE b.member_id=members.id
        ORDER BY b.created_at DESC
        LIMIT 1
      ) AS booking_status
     FROM members
     ORDER BY created_at DESC
     LIMIT ?`,
    limit
  );
}

async function storageStatus(env) {
  const counts = await databaseCounts(env);
  const latestLog = await one(env, "SELECT action, created_at FROM member_logs ORDER BY created_at DESC LIMIT 1");
  const recent = await recentMaskedMembers(env, 8);
  return {
    service: "Cloudflare Worker + D1",
    primary: "cloudflare-d1",
    route: PRODUCTION_ROUTE,
    version: CLOUDFLARE_VERSION,
    db: {
      exists: true,
      path: `Cloudflare D1:${D1_DATABASE_NAME}`,
      size_bytes: 0,
    },
    counts,
    sheets: { configured: false, status: "not_used_on_cloudflare" },
    hermes: {
      active: telegramConfigured(env, true) && (telegramEnabled(env, "application") || telegramEnabled(env, "booking")),
      configured: telegramConfigured(env, true),
      status: telegramConfigured(env, true) && (telegramEnabled(env, "application") || telegramEnabled(env, "booking")) ? "ON" : "OFF",
      global_enabled: envFlag(env, "TELEGRAM_NOTIFY_ENABLED"),
      active_application: telegramConfigured(env, true) && telegramEnabled(env, "application"),
      application_enabled: telegramEnabled(env, "application"),
      application_mode: telegramConfigured(env, true) && telegramEnabled(env, "application") ? "telegram_sendMessage" : "not_configured",
      active_booking: telegramConfigured(env, true) && telegramEnabled(env, "booking"),
      booking_enabled: telegramEnabled(env, "booking"),
      booking_mode: telegramConfigured(env, true) && telegramEnabled(env, "booking") ? "telegram_sendMessage" : "not_configured",
    },
    backup: {
      last_run: {
        created_at: latestLog?.created_at || now(),
        detail: { ok_count: 1, failed_count: 0, source: "cloudflare-d1" },
      },
      targets: [
        {
          name: "cloudflare-d1",
          label: "Cloudflare D1 운영 DB",
          path: D1_DATABASE_NAME,
          available: true,
          mode: "wrangler_d1_export",
          latest: latestLog ? { path: "member_logs latest action", modified_at: latestLog.created_at, size_bytes: 0 } : null,
        },
      ],
    },
    recent,
  };
}

function implementationStatus() {
  return {
    service: "member-system-cloudflare",
    current_phase: "Cloudflare 운영 전환 완료",
    route: PRODUCTION_ROUTE,
    version: CLOUDFLARE_VERSION,
    next_gates: [
      "운영 중 예약/신청 스모크 테스트 정기 실행",
      "D1 export 백업 파일 보관",
      "Mac Air 터널 의존 제거 확인",
    ],
    stages: [
      {
        version: "V1",
        title: "Cloudflare Worker + D1 운영 주소 전환",
        status: "done",
        summary: "apply.arsen-ai.com/* 라우트가 Worker로 연결되어 Mac Air 전원과 분리되었습니다.",
      },
      {
        version: "V2",
        title: "관리자 이동/취소/입금 후 데이터 재조회",
        status: "done",
        summary: "일정 변경 후 전체 대시보드를 다시 읽고 선택 날짜와 예약 목록을 갱신합니다.",
      },
      {
        version: "V3",
        title: "운영 스모크/데이터 비교/백업 스크립트",
        status: "done",
        summary: "민감값 출력 없이 운영 주소와 D1 count, 백업 명령을 확인하는 스크립트를 제공합니다.",
      },
      {
        version: "V4",
        title: "남은 운영 게이트",
        status: "check",
        summary: "실제 관리자 계정으로 이동/취소/입금확정 실사용 점검을 한 번 더 하면 됩니다.",
      },
    ],
  };
}

async function maskedSnapshot(env, limit = 200) {
  const members = await all(
    env,
    "SELECT id, name, phone_masked, status, participation_grade, plan_type, created_at FROM members ORDER BY created_at DESC LIMIT ?",
    limit
  );
  const sessions = await all(
    env,
    "SELECT id, title, starts_at, ends_at, location, status, capacity_max, confirmed_count, created_at, updated_at FROM sessions ORDER BY starts_at ASC LIMIT ?",
    limit
  );
  const bookings = await all(
    env,
    "SELECT id, session_id, member_id, applicant_name, phone_masked, status, payment_status, payment_amount_krw, confirmed_at, canceled_at, created_at, updated_at FROM bookings ORDER BY created_at DESC LIMIT ?",
    limit
  );
  const memberLogs = await all(
    env,
    "SELECT member_id, action, detail, created_at FROM member_logs ORDER BY created_at DESC LIMIT ?",
    limit
  );
  return {
    ok: true,
    data: {
      members,
      sessions,
      bookings,
      member_logs: memberLogs.map((log) => ({
        ...log,
        member_id_tail: String(log.member_id || "").slice(-8),
        member_id: undefined,
      })),
      counts: await databaseCounts(env),
      generated_at: now(),
    },
  };
}

function contactStatusFilter(value) {
  const normalized = String(value || "").trim().toLowerCase();
  if (!normalized || ["active", "non_erased", "not_erased", "all_active"].includes(normalized)) return "";
  return normalized;
}

function contactPlanFilter(value) {
  const normalized = String(value || "").trim().toLowerCase();
  return ["free", "full", "basic"].includes(normalized) ? normalized : "";
}

async function contactsRows(env, filters = {}) {
  const conditions = ["m.status!='erased'"];
  const params = [];
  const status = contactStatusFilter(filters.status);
  const planType = contactPlanFilter(filters.plan_type || filters.plan);
  const grade = String(filters.grade || "").trim();
  if (status) {
    conditions.push("m.status=?");
    params.push(status);
  }
  if (planType) {
    conditions.push("m.plan_type=?");
    params.push(planType);
  }
  if (grade) {
    conditions.push("m.participation_grade=?");
    params.push(grade);
  }
  const rows = await all(
    env,
    `SELECT
       m.id,
       m.name,
       m.phone_encrypted,
       m.email_encrypted,
       m.phone_masked,
       m.status,
       m.plan_type,
       m.participation_grade,
       m.created_at,
       COALESCE((
         SELECT GROUP_CONCAT(
           COALESCE(b.status, 'unknown') || ' / payment=' || COALESCE(b.payment_status, 'unknown') ||
           CASE WHEN s.title IS NOT NULL AND s.title != '' THEN ' / ' || s.title ELSE '' END ||
           CASE WHEN s.starts_at IS NOT NULL AND s.starts_at != '' THEN ' / ' || s.starts_at ELSE '' END,
           ' | '
         )
         FROM bookings b
         LEFT JOIN sessions s ON s.id=b.session_id
         WHERE b.member_id=m.id
       ), 'none') AS booking_status_summary
     FROM members m
     WHERE ${conditions.join(" AND ")}
     ORDER BY m.created_at DESC`,
    ...params
  );
  const contacts = [];
  for (const row of rows) {
    let phone = "";
    let email = "";
    try {
      phone = await decryptValue(row.phone_encrypted, env, "PHONE_SECRET_KEY");
    } catch (_) {
      phone = "";
    }
    try {
      email = await decryptValue(row.email_encrypted, env, "EMAIL_SECRET_KEY");
    } catch (_) {
      email = "";
    }
    contacts.push({
      id: row.id,
      name: row.name,
      phone,
      email,
      phone_masked: row.phone_masked,
      status: row.status,
      plan_type: row.plan_type,
      participation_grade: row.participation_grade,
      created_at: row.created_at,
      booking_status_summary: row.booking_status_summary || "none",
      contact_name: contactDisplayName(row.name, row.plan_type),
      contact_note: contactNote(row),
    });
  }
  return contacts;
}

function vcardEscape(value) {
  return String(value || "").replace(/\\/g, "\\\\").replace(/\n/g, "\\n").replace(/,/g, "\\,").replace(/;/g, "\\;");
}

async function handleAdmin(request, env, path) {
  const auth = requireAdmin(request, env);
  if (!auth.ok) return auth.response;
  const method = request.method;
  const parts = path.split("/").filter(Boolean);

  if (path === "/stats" && method === "GET") return json({ ok: true, data: await stats(env) });
  if (path === "/scheduler/status" && method === "GET") return json({ ok: true, data: null, jobs: [] });
  if (path === "/admin/implementation-status" && method === "GET") {
    return json({ ok: true, data: implementationStatus() });
  }
  if (path === "/admin/storage-status" && method === "GET") {
    return json({ ok: true, data: await storageStatus(env) });
  }
  if (path === "/admin/security-status" && method === "GET") {
    return json({
      ok: true,
      data: {
        admin_password: {
          configured: Boolean(env.ADMIN_API_KEY),
          length_ok: String(env.ADMIN_API_KEY || "").length >= 8,
          min_length: 8,
          env_private: true,
          env_mode: "cloudflare-secret",
          storage: "cloudflare-secret",
        },
        password_tool: {
          sources: [{ name: "wrangler secret put ADMIN_API_KEY", exists: true, path: "Cloudflare Worker Secret" }],
          backup_targets: [{ name: "cloudflare-secrets", label: "Cloudflare Secret", available: true, path: "Workers Secret Store" }],
        },
      },
    });
  }
  if (path === "/admin/site-theme" && method === "GET") {
    return json({ ok: true, data: await siteThemePayload(env) });
  }
  if (path === "/admin/site-theme" && method === "PUT") {
    const body = await readJson(request);
    const payload = await saveSiteTheme(env, body.active_theme_id);
    if (!payload) return fail(400, "알 수 없는 테마입니다.");
    await logAction(env, "system", "site_theme_update", body.active_theme_id, request);
    return json({ ok: true, data: payload });
  }
  if (path === "/admin/backup-now" && method === "POST") {
    await logAction(env, "system", "cloudflare_backup_checkpoint", "Use wrangler d1 export for SQL backup.", request);
    return json({ ok: true, data: { ok_count: 1, failed_count: 0, targets: [{ name: "cloudflare-d1", status: "export-ready" }] } });
  }
  if (path === "/admin/admin-tools/backup" && method === "POST") {
    return json({ ok: true, data: { ok_count: 1, failed_count: 0, targets: [{ name: "cloudflare-secret-config", status: "managed" }] } });
  }
  if (path === "/admin/password" && method === "POST") {
    return fail(501, "Cloudflare 배포판에서는 관리자 비밀번호를 Workers Secret으로 변경해야 합니다.");
  }
  if (path === "/admin/storage-snapshot" && method === "GET") {
    const url = new URL(request.url);
    const limit = Math.max(1, Math.min(500, Number(url.searchParams.get("limit") || 200)));
    return json(await maskedSnapshot(env, limit));
  }
  if (path === "/admin/storage-snapshot.csv" && method === "GET") {
    const url = new URL(request.url);
    const limit = Math.max(1, Math.min(500, Number(url.searchParams.get("limit") || 200)));
    const snapshot = await maskedSnapshot(env, limit);
    const rows = [
      ["kind", "id", "name_or_title", "status", "payment_status", "phone_masked", "created_at", "updated_at"],
      ...snapshot.data.members.map((item) => ["member", item.id, item.name, item.status, "", item.phone_masked, item.created_at, ""]),
      ...snapshot.data.sessions.map((item) => ["session", item.id, item.title, item.status, "", "", item.created_at, item.updated_at]),
      ...snapshot.data.bookings.map((item) => ["booking", item.id, item.applicant_name, item.status, item.payment_status, item.phone_masked, item.created_at, item.updated_at]),
    ];
    return responseText(csvRows(rows), "text/csv; charset=utf-8");
  }
  if (path === "/admin/licenses" && method === "GET") {
    const url = new URL(request.url);
    return json({
      ok: true,
      summary: await licenseSummary(env),
      data: await listLicenses(env, {
        status: String(url.searchParams.get("status") || "").trim(),
        member_id: String(url.searchParams.get("member_id") || "").trim(),
      }),
    });
  }
  if (path === "/admin/licenses" && method === "POST") {
    const body = await readJson(request);
    const result = await createLicense(env, body, request);
    if (result.response) return result.response;
    await logAction(env, "system", "yoonbot_license_created", result.license.license_key_hint, request);
    return json(result);
  }
  if (path === "/admin/licenses/summary" && method === "GET") {
    return json({ ok: true, data: await licenseSummary(env) });
  }
  if (parts[0] === "admin" && parts[1] === "licenses" && parts[2]) {
    const licenseId = parts[2];
    if (!parts[3] && method === "GET") {
      const item = await getLicense(env, licenseId);
      if (!item) return fail(404, "라이선스를 찾을 수 없습니다.");
      return json({ ok: true, data: item });
    }
    if (parts[3] === "revoke" && method === "POST") {
      const body = await readJson(request);
      const result = await revokeLicense(env, licenseId, body.reason || "manual", request);
      if (!result.ok) return fail(404, result.message || "라이선스를 찾을 수 없습니다.", result);
      await logAction(env, "system", "yoonbot_license_revoked", licenseId, request);
      return json(result);
    }
    if (parts[3] === "reset-device" && method === "POST") {
      const body = await readJson(request);
      const result = await resetLicenseDevice(env, licenseId, body.reason || "manual", request);
      if (!result.ok) return fail(400, result.message || "기기 초기화에 실패했습니다.", result);
      await logAction(env, "system", "yoonbot_license_device_reset", licenseId, request);
      return json(result);
    }
    if (parts[3] === "extend" && method === "POST") {
      const body = await readJson(request);
      const result = await extendLicense(env, licenseId, body.expires_at, request);
      if (!result.ok) return fail(400, result.message || "만료일 변경에 실패했습니다.", result);
      await logAction(env, "system", "yoonbot_license_extended", licenseId, request);
      return json(result);
    }
  }
  if (path === "/admin/yoonbot/orders" && method === "GET") {
    const url = new URL(request.url);
    return json({
      ok: true,
      summary: await orderSummary(env),
      data: await listYoonbotOrders(env, {
        status: String(url.searchParams.get("status") || "").trim(),
        plan_code: String(url.searchParams.get("plan_code") || "").trim(),
      }),
    });
  }
  if (parts[0] === "admin" && parts[1] === "yoonbot" && parts[2] === "orders" && parts[3]) {
    const orderId = parts[3];
    if (!parts[4] && method === "GET") {
      const order = await getYoonbotOrder(env, orderId);
      if (!order) return fail(404, "주문을 찾을 수 없습니다.");
      return json({ ok: true, data: order });
    }
    if (parts[4] === "mark-paid" && method === "POST") {
      const result = await markYoonbotOrderPaid(env, orderId, await readJson(request));
      if (!result.ok) return fail(result.status || 400, result.message || "결제 확인에 실패했습니다.");
      await logAction(env, "system", "yoonbot_order_mark_paid", orderId, request);
      return json(result);
    }
    if (parts[4] === "issue-license" && method === "POST") {
      const result = await issueYoonbotOrderLicense(env, orderId, request);
      if (!result.ok) return fail(result.status || 400, result.message || "라이선스 발급에 실패했습니다.");
      await logAction(env, "system", "yoonbot_order_license_issued", orderId, request);
      return json(result);
    }
    if (parts[4] === "cancel" && method === "POST") {
      const body = await readJson(request);
      const result = await setYoonbotOrderTerminalStatus(env, orderId, "canceled", "canceled_at", body.note || body.reason || "manual");
      if (!result.ok) return fail(result.status || 400, result.message || "주문 취소에 실패했습니다.");
      await logAction(env, "system", "yoonbot_order_canceled", orderId, request);
      return json(result);
    }
    if (parts[4] === "refund-note" && method === "POST") {
      const body = await readJson(request);
      const result = await setYoonbotOrderTerminalStatus(env, orderId, "refunded", "refunded_at", body.note || body.reason || "manual");
      if (!result.ok) return fail(result.status || 400, result.message || "환불 메모 처리에 실패했습니다.");
      await logAction(env, "system", "yoonbot_order_refunded", orderId, request);
      return json(result);
    }
  }
  if (path === "/admin/contacts-export.csv" && method === "GET") {
    const url = new URL(request.url);
    const contacts = await contactsRows(env, {
      status: url.searchParams.get("status"),
      grade: url.searchParams.get("grade"),
      plan_type: url.searchParams.get("plan_type"),
    });
    const rows = [
      [
        "Name",
        "Given Name",
        "Family Name",
        "Phone 1 - Type",
        "Phone 1 - Value",
        "E-mail 1 - Type",
        "E-mail 1 - Value",
        "Notes",
        "Group Membership",
        "member_id",
        "name",
        "phone",
        "email",
        "status",
        "plan_type",
        "participation_grade",
        "created_at",
        "booking_status_summary",
      ],
      ...contacts.map((item) => [
        item.contact_name,
        "",
        "",
        item.phone ? "Mobile" : "",
        item.phone,
        item.email ? "Home" : "",
        item.email,
        item.contact_note,
        "* myContacts",
        item.id,
        item.name,
        item.phone,
        item.email,
        item.status,
        item.plan_type,
        item.participation_grade,
        item.created_at,
        item.booking_status_summary,
      ]),
    ];
    await logAction(env, "system", "contacts_export", contactExportDetail("csv", contacts), request);
    return responseText(csvRows(rows), "text/csv; charset=utf-8", {
      headers: { "content-disposition": "attachment; filename=contacts-export.csv" },
    });
  }
  if (path === "/admin/contacts-export.vcf" && method === "GET") {
    const url = new URL(request.url);
    const contacts = await contactsRows(env, {
      status: url.searchParams.get("status"),
      grade: url.searchParams.get("grade"),
      plan_type: url.searchParams.get("plan_type"),
    });
    const cards = contacts.map((item) => [
      "BEGIN:VCARD",
      "VERSION:3.0",
      `FN:${vcardEscape(item.contact_name)}`,
      `N:;${vcardEscape(item.contact_name)};;;`,
      item.phone ? `TEL;TYPE=CELL:${vcardEscape(item.phone)}` : "",
      item.email ? `EMAIL:${vcardEscape(item.email)}` : "",
      `NOTE:${vcardEscape(item.contact_note)}`,
      "END:VCARD",
    ].filter(Boolean).join("\n"));
    await logAction(env, "system", "contacts_export", contactExportDetail("vcf", contacts), request);
    return responseText(cards.join("\n") + (cards.length ? "\n" : ""), "text/vcard; charset=utf-8", {
      headers: { "content-disposition": "attachment; filename=contacts-export.vcf" },
    });
  }

  if (path === "/members" && method === "GET") {
    const rows = await all(env, "SELECT * FROM members ORDER BY created_at DESC");
    return json({ ok: true, data: rows.map(safeMember), total: rows.length });
  }
  if (parts[0] === "admin" && parts[1] === "members" && parts[2] && parts[3] === "code-delivery-log" && method === "POST") {
    const body = await readJson(request);
    await logAction(env, parts[2], "code_delivered", JSON.stringify({
      channel: body.channel || "direct",
      note: body.note || "",
      no_send: true,
    }), request);
    return json({ ok: true, data: { member_id: parts[2], logged: true }, ...noSendDelivery("manual_code_delivery") });
  }
  if (parts[0] === "members" && parts[1] && parts[2] === "erase" && method === "POST") {
    const body = await readJson(request);
    const member = await one(env, "SELECT id FROM members WHERE id=?", parts[1]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    let canceled = 0;
    if (body.cancel_bookings !== false) {
      const active = await all(env, "SELECT id, session_id FROM bookings WHERE member_id=? AND status NOT IN ('canceled','rejected','no_show')", parts[1]);
      for (const booking of active) {
        await env.DB.prepare("UPDATE bookings SET status='canceled', canceled_at=?, payment_note=COALESCE(payment_note, ''), updated_at=? WHERE id=?")
          .bind(now(), now(), booking.id)
          .run();
        await refreshSessionCount(env, booking.session_id);
        canceled += 1;
      }
    }
    await env.DB.prepare(
      "UPDATE members SET name='삭제된 신청자', email_encrypted='', email_hash='', phone_hash='', phone_masked='', phone_encrypted='', status='erased', rejection_reason='operator erased personal data' WHERE id=?"
    )
      .bind(parts[1])
      .run();
    await logAction(env, parts[1], "member_erased", `bookings_canceled=${canceled}`, request);
    return json({ ok: true, data: { member_id: parts[1], bookings_canceled: canceled } });
  }
  if (parts[0] === "members" && parts[1] && method === "GET") {
    if (parts[2] === "contact") {
      const member = await one(env, "SELECT * FROM members WHERE id=?", parts[1]);
      if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
      await logAction(env, parts[1], "contact_view", "admin_contact_reveal", request);
      return json({
        ok: true,
        data: {
          id: member.id,
          name: member.name,
          phone: await decryptValue(member.phone_encrypted, env, "PHONE_SECRET_KEY"),
          email: await decryptValue(member.email_encrypted, env, "EMAIL_SECRET_KEY"),
          phone_masked: member.phone_masked,
        },
      });
    }
    if (parts[2] === "access-code") {
      const member = await one(env, "SELECT id, name, access_code, code_issued_at FROM members WHERE id=?", parts[1]);
      if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
      return json({
        ok: true,
        data: {
          code: member.access_code,
          expires_at: null,
          issued_at: member.code_issued_at,
          expiry_label: "기한 없음",
          delivery_message: member.access_code ? codeDeliveryMessage(member, member.access_code, env) : "",
        },
      });
    }
    const member = await one(env, "SELECT * FROM members WHERE id=?", parts[1]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    return json({ ok: true, data: safeMember(member) });
  }

  if (["approve", "regen-code"].includes(parts[0]) && parts[1] && method === "POST") {
    const member = await one(env, "SELECT * FROM members WHERE id=?", parts[1]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    const code = accessCode();
    await env.DB.prepare("UPDATE members SET status='approved', access_code=?, code_issued_at=?, approved_at=? WHERE id=?")
      .bind(code, now(), now(), parts[1])
      .run();
    await logAction(env, parts[1], parts[0] === "approve" ? "approve" : "code_regen", "code_issued", request);
    const updated = await one(env, "SELECT * FROM members WHERE id=?", parts[1]);
    const deliveryMessage = codeDeliveryMessage(updated, code, env);
    await sendTelegram(
      env,
      [
        "<b>ARSEN 코드 발급 완료</b>",
        `이름: ${htmlEscape(updated?.name || "-")}`,
        `회원ID: <code>${htmlEscape(parts[1])}</code>`,
        `코드: <code>${htmlEscape(code)}</code>`,
        "",
        "안내문자/카톡 복사용:",
        htmlEscape(deliveryMessage),
      ].join("\n"),
      memberKeyboard(env, parts[1]),
      "application"
    );
    return json({ ok: true, message: "승인 및 코드 발급 완료", code, expires_at: null, delivery_message: deliveryMessage });
  }
  if (parts[0] === "reject" && parts[1] && method === "POST") {
    const body = await readJson(request);
    await env.DB.prepare("UPDATE members SET status='rejected', rejection_reason=? WHERE id=?").bind(body.reason || "", parts[1]).run();
    await logAction(env, parts[1], "reject", body.reason || "", request);
    return json({ ok: true, message: "거절 처리 완료" });
  }
  if (["blacklist", "unblacklist"].includes(parts[0]) && parts[1] && method === "POST") {
    const status = parts[0] === "blacklist" ? "blacklist" : "pending";
    await env.DB.prepare("UPDATE members SET status=? WHERE id=?").bind(status, parts[1]).run();
    await logAction(env, parts[1], parts[0], `status=${status}`, request);
    return json({ ok: true, message: status === "blacklist" ? "차단 처리 완료" : "차단 해제 완료" });
  }

  if (path === "/admin/payment-accounts" && method === "GET") {
    return json({ ok: true, data: await setting(env, "payment_accounts", { accounts: [], active_id: "" }) });
  }
  if (path === "/admin/payment-accounts" && method === "PUT") {
    const body = await readJson(request);
    await saveSetting(env, "payment_accounts", { accounts: body.accounts || [], active_id: body.active_id || "" });
    return json({ ok: true, data: { accounts: body.accounts || [], active_id: body.active_id || "" } });
  }
  if (path === "/admin/preparation-guide" && method === "GET") {
    return json({ ok: true, data: await setting(env, "preparation_guide", { message: "", default_message: "" }), ...noSendDelivery() });
  }
  if (path === "/admin/preparation-guide" && method === "PUT") {
    const body = await readJson(request);
    const payload = { message: body.message || "", default_message: body.default_message || "", updated_at: now() };
    await saveSetting(env, "preparation_guide", payload);
    return json({ ok: true, data: payload, ...noSendDelivery() });
  }

  if (path === "/admin/review-board" && method === "GET") {
    return json({ ok: true, data: await reviewBoardRows(env, false) });
  }
  if (path === "/admin/review-board/invites" && method === "GET") {
    const rows = await all(
      env,
      `SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
       FROM review_invites ri
       LEFT JOIN review_instructors i ON i.id=ri.instructor_id
       ORDER BY ri.created_at DESC`
    );
    return json({ ok: true, data: rows.map(reviewInviteRow) });
  }
  if (path === "/admin/review-board/invites" && method === "POST") {
    const body = await readJson(request);
    if (body.instructor_id && !(await getReviewInstructor(env, body.instructor_id))) return fail(400, "선택한 강사를 찾을 수 없습니다.");
    const id = crypto.randomUUID();
    const token = `${crypto.randomUUID()}-${crypto.randomUUID()}`;
    const tokenHash = await reviewTokenHash(token);
    const created = now();
    await env.DB.prepare(
      `INSERT INTO review_invites (
        id, token_hash, label, instructor_id, class_title, class_date, status,
        max_submissions, submitted_count, expires_at, created_at, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?)`
    )
      .bind(
        id,
        tokenHash,
        String(body.label || "").trim(),
        body.instructor_id || null,
        String(body.class_title || "").trim(),
        String(body.class_date || "").trim(),
        reviewInviteStatus(body.status),
        Math.max(0, Number(body.max_submissions || 0)),
        String(body.expires_at || "").trim(),
        created,
        created
      )
      .run();
    const invite = await getReviewInvite(env, id);
    invite.token = token;
    await logAction(env, "review_board", "review_invite_create", JSON.stringify({ id, status: invite.status }), request);
    return json({ ok: true, id, data: invite });
  }
  if (parts[0] === "admin" && parts[1] === "review-board" && parts[2] === "invites" && parts[3] && parts[4] === "revoke" && method === "POST") {
    const inviteId = parts[3];
    const current = await getReviewInvite(env, inviteId);
    if (!current) return fail(404, "후기 작성 링크를 찾을 수 없습니다.");
    await env.DB.prepare("UPDATE review_invites SET status='revoked', updated_at=? WHERE id=?").bind(now(), inviteId).run();
    await logAction(env, "review_board", "review_invite_revoke", JSON.stringify({ id: inviteId }), request);
    return json({ ok: true, data: await getReviewInvite(env, inviteId) });
  }
  if (path === "/admin/review-board/instructors" && method === "POST") {
    const body = await readJson(request);
    const name = String(body.name || "").trim();
    if (!name) return fail(400, "강사 이름이 필요합니다.");
    const id = crypto.randomUUID();
    const created = now();
    await env.DB.prepare(
      `INSERT INTO review_instructors (
        id, name, role, bio, specialties, status, sort_order, created_at, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`
    )
      .bind(
        id,
        name,
        String(body.role || "").trim(),
        String(body.bio || "").trim(),
        listText(body.specialties),
        reviewInstructorStatus(body.status),
        Number(body.sort_order || 0),
        created,
        created
      )
      .run();
    await logAction(env, "review_board", "review_instructor_create", JSON.stringify({ id, status: reviewInstructorStatus(body.status) }), request);
    return json({ ok: true, id, data: await getReviewInstructor(env, id) });
  }
  if (parts[0] === "admin" && parts[1] === "review-board" && parts[2] === "instructors" && parts[3]) {
    const instructorId = parts[3];
    if (method === "PUT") {
      const current = await getReviewInstructor(env, instructorId);
      if (!current) return fail(404, "강사를 찾을 수 없습니다.");
      const body = await readJson(request);
      const allowed = {
        name: (value) => String(value || "").trim(),
        role: (value) => String(value || "").trim(),
        bio: (value) => String(value || "").trim(),
        specialties: listText,
        status: reviewInstructorStatus,
        sort_order: (value) => Number(value || 0),
      };
      const keys = Object.keys(allowed).filter((key) => body[key] !== undefined && body[key] !== null);
      if (!keys.length) return fail(400, "변경할 값이 없습니다.");
      await env.DB.prepare(`UPDATE review_instructors SET ${keys.map((key) => `${key}=?`).join(", ")}, updated_at=? WHERE id=?`)
        .bind(...keys.map((key) => allowed[key](body[key])), now(), instructorId)
        .run();
      await logAction(env, "review_board", "review_instructor_update", JSON.stringify({ id: instructorId, fields: keys }), request);
      return json({ ok: true, data: await getReviewInstructor(env, instructorId) });
    }
    if (method === "DELETE") {
      const current = await getReviewInstructor(env, instructorId);
      if (!current) return fail(404, "강사를 찾을 수 없습니다.");
      await env.DB.prepare("DELETE FROM review_instructors WHERE id=?").bind(instructorId).run();
      await logAction(env, "review_board", "review_instructor_delete", JSON.stringify({ id: instructorId }), request);
      return json({ ok: true, data: { id: instructorId } });
    }
  }
  if (path === "/admin/review-board/entries" && method === "POST") {
    const body = await readJson(request);
    const classTitle = String(body.class_title || body.title || "").trim();
    const title = String(body.title || classTitle).trim();
    if (!classTitle || !title) return fail(400, "수업명과 후기 제목이 필요합니다.");
    if (body.instructor_id && !(await getReviewInstructor(env, body.instructor_id))) return fail(400, "선택한 강사를 찾을 수 없습니다.");
    const id = crypto.randomUUID();
    const created = now();
    await env.DB.prepare(
      `INSERT INTO review_entries (
        id, instructor_id, class_title, class_date, title, summary, body, tags, image_urls,
        status, source, privacy_checked, featured, created_at, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
    )
      .bind(
        id,
        body.instructor_id || null,
        classTitle,
        String(body.class_date || "").trim(),
        title,
        String(body.summary || "").trim(),
        String(body.body || "").trim(),
        listText(body.tags),
        listText(body.image_urls),
        reviewEntryStatus(body.status),
        String(body.source || "manual").trim() || "manual",
        body.privacy_checked ? 1 : 0,
        body.featured ? 1 : 0,
        created,
        created
      )
      .run();
    await logAction(env, "review_board", "review_entry_create", JSON.stringify({ id, status: reviewEntryStatus(body.status), privacy_checked: Boolean(body.privacy_checked) }), request);
    return json({ ok: true, id, data: await getReviewEntry(env, id) });
  }
  if (parts[0] === "admin" && parts[1] === "review-board" && parts[2] === "entries" && parts[3]) {
    const entryId = parts[3];
    if (method === "PUT") {
      const current = await getReviewEntry(env, entryId);
      if (!current) return fail(404, "후기를 찾을 수 없습니다.");
      const body = await readJson(request);
      if (body.instructor_id && !(await getReviewInstructor(env, body.instructor_id))) return fail(400, "선택한 강사를 찾을 수 없습니다.");
      const allowed = {
        instructor_id: (value) => value || null,
        class_title: (value) => String(value || "").trim(),
        class_date: (value) => String(value || "").trim(),
        title: (value) => String(value || "").trim(),
        summary: (value) => String(value || "").trim(),
        body: (value) => String(value || "").trim(),
        tags: listText,
        image_urls: listText,
        status: reviewEntryStatus,
        source: (value) => String(value || "manual").trim() || "manual",
        privacy_checked: (value) => (value ? 1 : 0),
        featured: (value) => (value ? 1 : 0),
      };
      const keys = Object.keys(allowed).filter((key) => body[key] !== undefined && body[key] !== null);
      if (!keys.length) return fail(400, "변경할 값이 없습니다.");
      await env.DB.prepare(`UPDATE review_entries SET ${keys.map((key) => `${key}=?`).join(", ")}, updated_at=? WHERE id=?`)
        .bind(...keys.map((key) => allowed[key](body[key])), now(), entryId)
        .run();
      await logAction(env, "review_board", "review_entry_update", JSON.stringify({ id: entryId, fields: keys }), request);
      return json({ ok: true, data: await getReviewEntry(env, entryId) });
    }
    if (method === "DELETE") {
      const current = await getReviewEntry(env, entryId);
      if (!current) return fail(404, "후기를 찾을 수 없습니다.");
      await env.DB.prepare("DELETE FROM review_entries WHERE id=?").bind(entryId).run();
      await logAction(env, "review_board", "review_entry_delete", JSON.stringify({ id: entryId }), request);
      return json({ ok: true, data: { id: entryId } });
    }
  }

  if (path === "/admin/sessions" && method === "GET") {
    const rows = await sessionRows(env, true);
    return json({ ok: true, data: rows, total: rows.length });
  }
  if (path === "/admin/sessions" && method === "POST") {
    const body = await readJson(request);
    const id = crypto.randomUUID();
    const created = now();
    await env.DB.prepare(
      `INSERT INTO sessions (
        id, title, description, program_type, audience_level, starts_at, ends_at, timezone,
        capacity_min, capacity_max, confirmed_count, price_krw, location, materials, status,
        payment_guide, created_at, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?, ?, ?)`
    )
      .bind(
        id,
        body.title || DEFAULT_TITLE,
        body.description || "",
        body.program_type || "ai_basic_setup",
        body.audience_level || "all",
        body.starts_at,
        body.ends_at,
        body.timezone || "Asia/Seoul",
        Number(body.capacity_min || 4),
        Number(body.capacity_max || 5),
        Number(body.price_krw || DEFAULT_PRICE),
        body.location || DEFAULT_LOCATION,
        body.materials || "",
        body.status || "open",
        body.payment_guide || "",
        created,
        created
      )
      .run();
    await logAction(env, id, "session_create", body.title || DEFAULT_TITLE, request);
    return json({ ok: true, id, data: await getSession(env, id) });
  }
  if (parts[0] === "admin" && parts[1] === "sessions" && parts[2] && method === "POST") {
    if (parts[2] === "seed-default-sunday") {
      const body = await readJson(request);
      const weeks = Math.max(1, Math.min(12, Number(body.weeks || 4)));
      const createdIds = [];
      const updatedIds = [];
      const kstNow = new Date(Date.now() + 9 * 60 * 60 * 1000);
      const daysUntilSunday = (7 - kstNow.getUTCDay()) % 7;
      const base = new Date(Date.UTC(kstNow.getUTCFullYear(), kstNow.getUTCMonth(), kstNow.getUTCDate() + daysUntilSunday));
      for (let week = 0; week < weeks; week += 1) {
        for (const hour of [10, 13, 16]) {
          const startKst = new Date(base.getTime() + week * 7 * 24 * 60 * 60 * 1000 + hour * 60 * 60 * 1000);
          const endKst = new Date(startKst.getTime() + 2 * 60 * 60 * 1000);
          const startsAt = new Date(startKst.getTime() - 9 * 60 * 60 * 1000).toISOString();
          const endsAt = new Date(endKst.getTime() - 9 * 60 * 60 * 1000).toISOString();
          const existing = await one(env, "SELECT id FROM sessions WHERE starts_at=?", startsAt);
          if (existing) {
            await env.DB.prepare("UPDATE sessions SET title=?, ends_at=?, location=?, status='open', updated_at=? WHERE id=?")
              .bind(DEFAULT_TITLE, endsAt, DEFAULT_LOCATION, now(), existing.id)
              .run();
            updatedIds.push(existing.id);
          } else {
            const id = crypto.randomUUID();
            const created = now();
            await env.DB.prepare(
              `INSERT INTO sessions (
                id, title, description, program_type, audience_level, starts_at, ends_at, timezone,
                capacity_min, capacity_max, confirmed_count, price_krw, location, materials, status,
                payment_guide, created_at, updated_at
              ) VALUES (?, ?, ?, 'ai_basic_setup', 'all', ?, ?, 'Asia/Seoul', 4, 5, 0, ?, ?, '', 'open', '', ?, ?)`
            )
              .bind(id, DEFAULT_TITLE, "", startsAt, endsAt, DEFAULT_PRICE, DEFAULT_LOCATION, created, created)
              .run();
            createdIds.push(id);
          }
        }
      }
      await logAction(env, "booking", "session_seed_default_sunday", `created=${createdIds.length},updated=${updatedIds.length}`, request);
      return json({ ok: true, created: createdIds.length, updated: updatedIds.length, total: createdIds.length + updatedIds.length, ids: [...createdIds, ...updatedIds] });
    }
    if (parts[3] === "manual-booking") {
      const session = await getSession(env, parts[2]);
      if (!session) return fail(404, "일정을 찾을 수 없습니다.");
      const body = await readJson(request);
      let member = body.member_id ? await one(env, "SELECT * FROM members WHERE id=?", body.member_id) : null;
      if (body.member_id && !member) return fail(404, "선택한 신청자를 찾을 수 없습니다.");
      if (!member) {
        if (!body.applicant_name || !body.phone) return fail(400, "신청자 이름과 연락처를 입력하세요.");
        const memberId = await createEdgeMember(env, {
          name: body.applicant_name,
          phone: body.phone,
          email: body.email || "",
          short_term_goal: body.desired_outcome || body.payment_note || "",
          status: "approved",
        });
        member = await one(env, "SELECT * FROM members WHERE id=?", memberId);
      } else if (member.status !== "approved") {
        await env.DB.prepare("UPDATE members SET status='approved', approved_at=? WHERE id=?").bind(now(), member.id).run();
        member.status = "approved";
      }
      const existing = await one(
        env,
        "SELECT id FROM bookings WHERE member_id=? AND session_id=? AND status NOT IN ('canceled','rejected','no_show') LIMIT 1",
        member.id,
        parts[2]
      );
      if (existing) {
        await env.DB.prepare("UPDATE bookings SET status='confirmed', payment_status='paid', payment_note=?, confirmed_at=?, updated_at=? WHERE id=?")
          .bind(body.payment_note || "운영자 수동 추가: 입금 확인 완료", now(), now(), existing.id)
          .run();
        await refreshSessionCount(env, parts[2]);
        return json({ ok: true, message: "이미 연결된 예약을 입금확정으로 변경했습니다. 자동 알림은 보내지 않았습니다.", data: await getBooking(env, existing.id), member_id: member.id, reused_member: true, ...noSendDelivery("manual_booking") });
      }
      const [ok, reason] = sessionAcceptance(session);
      if (!ok) return fail(409, reason);
      const bookingId = await createBooking(env, {
        session_id: parts[2],
        member_id: member.id,
        applicant_name: body.applicant_name || member.name,
        phone_masked: member.phone_masked || maskPhone(body.phone || ""),
        desired_outcome: body.desired_outcome || "",
        preparedness: "운영자 수동 추가",
        status: "confirmed",
        payment_status: "paid",
        payment_amount_krw: Number(body.payment_amount_krw || session.price_krw || DEFAULT_PRICE),
        payment_note: body.payment_note || "운영자 수동 추가: 입금 확인 완료",
        confirmed_at: now(),
      });
      await logAction(env, member.id, "manual_booking_confirmed", `booking_id=${bookingId}`, request);
      return json({ ok: true, message: "입금확정 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다.", data: await getBooking(env, bookingId), member_id: member.id, reused_member: Boolean(body.member_id), ...noSendDelivery("manual_booking") });
    }
    const body = await readJson(request);
    const allowed = ["title", "description", "program_type", "audience_level", "starts_at", "ends_at", "timezone", "capacity_min", "capacity_max", "price_krw", "location", "materials", "status", "payment_guide"];
    const fields = allowed.filter((key) => body[key] !== undefined);
    if (!fields.length) return fail(400, "변경할 값이 없습니다.");
    const sql = fields.map((key) => `${key}=?`).join(", ");
    await env.DB.prepare(`UPDATE sessions SET ${sql}, updated_at=? WHERE id=?`)
      .bind(...fields.map((key) => body[key]), now(), parts[2])
      .run();
    await refreshSessionCount(env, parts[2]);
    return json({ ok: true, data: await getSession(env, parts[2]) });
  }
  if (parts[0] === "admin" && parts[1] === "sessions" && parts[2] && method === "DELETE") {
    const active = await one(env, "SELECT COUNT(*) AS count FROM bookings WHERE session_id=? AND status NOT IN ('canceled','rejected','no_show')", parts[2]);
    if (Number(active?.count || 0) > 0) return fail(409, "신청 또는 확정 예약이 남은 일정은 삭제할 수 없습니다. 먼저 예약을 취소하세요.");
    await env.DB.prepare("UPDATE bookings SET session_id=NULL, updated_at=? WHERE session_id=?").bind(now(), parts[2]).run();
    await env.DB.prepare("DELETE FROM sessions WHERE id=?").bind(parts[2]).run();
    return json({ ok: true, message: "일정을 삭제했습니다." });
  }

  if (path === "/admin/bookings" && method === "GET") {
    const url = new URL(request.url);
    const rows = await bookingRows(env, { status: url.searchParams.get("status") || "", sessionId: url.searchParams.get("session_id") || "" });
    return json({ ok: true, data: rows, total: rows.length });
  }
  if (parts[0] === "admin" && parts[1] === "bookings" && parts[2]) {
    const bookingId = parts[2];
    if (method === "GET") {
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      return json({ ok: true, data: booking });
    }
    if (parts[3] === "state" && method === "POST") {
      const body = await readJson(request);
      if (body.status && !ALLOWED_BOOKING_STATUSES.has(body.status)) return fail(400, "허용되지 않은 예약 상태입니다.");
      if (body.payment_status && !ALLOWED_PAYMENT_STATUSES.has(body.payment_status)) return fail(400, "허용되지 않은 입금 상태입니다.");
      const current = await getBooking(env, bookingId);
      if (!current) return fail(404, "예약 신청을 찾을 수 없습니다.");
      if (body.status === "confirmed" && current.status !== "confirmed" && current.session_id) {
        await refreshSessionCount(env, current.session_id);
        const session = await getSession(env, current.session_id);
        const confirmed = Number(session?.confirmed_booking_count || 0);
        const capacity = Number(session?.capacity_max || 0);
        if (capacity > 0 && confirmed >= capacity) return fail(409, "정원이 이미 마감되어 확정할 수 없습니다.");
      }
      await env.DB.prepare(
        "UPDATE bookings SET status=COALESCE(?, status), payment_status=COALESCE(?, payment_status), payment_note=COALESCE(?, payment_note), confirmed_at=CASE WHEN ?='confirmed' THEN ? ELSE confirmed_at END, canceled_at=CASE WHEN ?='canceled' THEN ? ELSE canceled_at END, updated_at=? WHERE id=?"
      )
        .bind(body.status || null, body.payment_status || null, body.payment_note || null, body.status || "", now(), body.status || "", now(), now(), bookingId)
        .run();
      await refreshSessionCount(env, current.session_id);
      return json({ ok: true, data: await getBooking(env, bookingId) });
    }
    if (parts[3] === "move-session" && method === "POST") {
      const body = await readJson(request);
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      if (!body.session_id) return fail(400, "이동할 일정을 선택하세요.");
      if (booking.session_id === body.session_id) return json({ ok: true, message: "이미 선택한 일정에 연결되어 있습니다.", data: booking, old_session_id: booking.session_id, new_session_id: body.session_id });
      if (NON_MOVABLE_BOOKING_STATUSES.has(booking.status)) return fail(409, "취소/거절/노쇼/완료 예약은 이동할 수 없습니다.");
      await refreshSessionCount(env, body.session_id);
      const target = await getSession(env, body.session_id || "");
      const [ok, reason] = sessionAcceptance(target);
      if (!ok) return fail(409, reason);
      const moveNote = String(body.note || "").trim();
      const existingNote = String(booking.payment_note || "").trim();
      const nextNote = moveNote
        ? [existingNote, `[일정 이동] ${moveNote}`].filter(Boolean).join("\n")
        : existingNote;
      await env.DB.prepare("UPDATE bookings SET session_id=?, payment_note=?, updated_at=? WHERE id=?")
        .bind(body.session_id, nextNote, now(), bookingId)
        .run();
      await refreshSessionCount(env, booking.session_id);
      await refreshSessionCount(env, body.session_id);
      return json({ ok: true, message: "예약 일정을 이동했습니다. 자동 알림은 보내지 않았습니다.", data: await getBooking(env, bookingId), old_session_id: booking.session_id, new_session_id: body.session_id, ...noSendDelivery("session_move") });
    }
    if (parts[3] === "send-payment-guide" && method === "POST") {
      const body = await readJson(request);
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      const paymentAccount = await selectedPaymentAccount(env, body.payment_account_id);
      const guide = String(body.payment_note || "").trim() || defaultPaymentGuide(booking, paymentAccount);
      await env.DB.prepare("UPDATE bookings SET status='payment_guide_sent', payment_status='guide_sent', payment_note=?, updated_at=? WHERE id=?")
        .bind(guide, now(), bookingId)
        .run();
      return json({
        ok: true,
        message: "입금 안내 상태로 변경했습니다. 신청자에게 자동 전송하지 않았습니다. 아래 문구를 복사해 카카오톡/문자로 직접 전달하세요.",
        payment_guide: guide,
        data: await getBooking(env, bookingId),
        ...noSendDelivery("manual_copy"),
      });
    }
    if (parts[3] === "confirm-payment" && method === "POST") {
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      if (booking.status === "confirmed") {
        return json({ ok: true, message: "이미 확정된 예약입니다.", data: booking, ...noSendDelivery("manual_confirm") });
      }
      if (booking.session_id) {
        await refreshSessionCount(env, booking.session_id);
        const session = await getSession(env, booking.session_id);
        const confirmed = Number(session?.confirmed_booking_count || 0);
        const capacity = Number(session?.capacity_max || 0);
        if (capacity > 0 && confirmed >= capacity) {
          return fail(409, "정원이 이미 마감되어 확정할 수 없습니다.");
        }
      }
      await env.DB.prepare("UPDATE bookings SET status='confirmed', payment_status='paid', payment_note=?, confirmed_at=?, updated_at=? WHERE id=?")
        .bind(String((await readJson(request)).payment_note || booking.payment_note || "운영자 수동 입금 확인"), now(), now(), bookingId)
        .run();
      await refreshSessionCount(env, booking.session_id);
      return json({ ok: true, message: "입금 확인 및 예약 확정 완료. 자동 알림은 보내지 않았습니다.", data: await getBooking(env, bookingId), ...noSendDelivery("manual_confirm") });
    }
    if (parts[3] === "location-guide" && method === "POST") {
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      return json({
        ok: true,
        message: "장소 안내 문구를 만들었습니다. 신청자에게 자동 전송하지 않았습니다.",
        location_guide: defaultLocationGuide(booking),
        data: booking,
        ...noSendDelivery("manual_copy"),
      });
    }
    if (parts[3] === "refund-guide" && method === "POST") {
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      return json({
        ok: true,
        message: "환불 안내 문구를 만들었습니다. 실제 환불 처리 여부는 운영자가 별도로 확인해야 합니다.",
        refund_guide: defaultRefundGuide(booking),
        data: booking,
        ...noSendDelivery("manual_copy"),
      });
    }
    if (method === "DELETE") {
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      if (!INACTIVE_BOOKING_STATUSES.has(booking.status)) return fail(409, "활성 예약은 먼저 취소한 뒤 삭제하세요.");
      await env.DB.prepare("DELETE FROM bookings WHERE id=?").bind(bookingId).run();
      await refreshSessionCount(env, booking.session_id);
      return json({ ok: true, message: "예약 신청 기록을 삭제했습니다.", data: { booking_id: bookingId } });
    }
  }

  return fail(404, "Cloudflare member-system endpoint not found");
}

export async function handleRequest(request, env) {
  if (request.method === "OPTIONS") return withCors(new Response(null, { status: 204 }), request, env);
  try {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, "") || "/";
    if ((request.method === "GET" || request.method === "HEAD") && !isApiPath(path) && env.ASSETS) {
      if (path === "/") {
        const indexUrl = new URL(request.url);
        indexUrl.pathname = "/index.html";
        return env.ASSETS.fetch(new Request(indexUrl, request));
      }
      return env.ASSETS.fetch(request);
    }
    let response;
    if (path === "/health") {
      response = json({ ok: true, service: "member-system-cloudflare", time: now() });
    } else if (path === "/sessions" && request.method === "GET") {
      const rows = await sessionRows(env, false);
      response = json({ ok: true, data: rows.map((row) => ({ ...row, payment_guide: undefined })), total: rows.length });
    } else if (path === "/apply" && request.method === "POST") {
      response = await handleApply(request, env);
    } else if (path === "/member/verify-code" && request.method === "POST") {
      response = await handlePublicVerify(request, env);
    } else if (path === "/member/bookings" && request.method === "POST") {
      response = await handlePublicBooking(request, env);
    } else if (path === "/telegram/webhook" && request.method === "POST") {
      response = await handleTelegramWebhook(request, env);
    } else if (path === "/api/site-theme" && request.method === "GET") {
      response = json({ ok: true, data: await siteThemePayload(env) });
    } else if (path === "/api/education" && request.method === "GET") {
      const data = await setting(env, "education", { resources: [], updated_at: "" });
      const includeHidden = url.searchParams.get("include_hidden") === "true";
      if (includeHidden) {
        const auth = requireAdmin(request, env);
        if (!auth.ok) response = auth.response;
        else response = json({ ok: true, ...data });
      } else {
        const resources = Array.isArray(data.resources) ? data.resources.filter((item) => item.visible !== false) : [];
        response = json({ ok: true, resources, updated_at: data.updated_at || "" });
      }
    } else if (path === "/api/education" && request.method === "PUT") {
      const auth = requireAdmin(request, env);
      if (!auth.ok) response = auth.response;
      else {
        const body = await readJson(request);
        const payload = { resources: Array.isArray(body.resources) ? body.resources : body, updated_at: now() };
        await saveSetting(env, "education", payload);
        response = json({ ok: true, ...payload });
      }
    } else if (path === "/api/license/activate" && request.method === "POST") {
      response = json(await activateLicense(env, await readJson(request), request));
    } else if (path === "/api/license/verify" && request.method === "POST") {
      const token = bearerToken(request);
      response = token
        ? json(await verifyLicense(env, await readJson(request), request, token))
        : fail(401, "라이선스 인증 토큰이 필요합니다.");
    } else if (path === "/api/yoonbot/products" && request.method === "GET") {
      response = json({ ok: true, ...yoonbotProducts() });
    } else if (path === "/api/yoonbot/orders" && request.method === "POST") {
      const result = await createYoonbotOrder(env, await readJson(request));
      if (result.response) response = result.response;
      else {
        await logAction(env, "system", "yoonbot_order_created", result.data.id, request);
        response = json(result);
      }
    } else if (path.startsWith("/api/review-board/submit/")) {
      const token = path.split("/").pop() || "";
      const invite = await getReviewInviteByToken(env, token);
      if (!invite) response = fail(404, "유효하지 않은 후기 작성 링크입니다.");
      else if (!invite.is_open) response = fail(400, "현재 사용할 수 없는 후기 작성 링크입니다.");
      else if (request.method === "GET") {
        response = json({ ok: true, data: { invite, instructors: (await reviewBoardRows(env, true)).instructors } });
      } else if (request.method === "POST") {
        const body = await readJson(request);
        const classTitle = String(body.class_title || invite.class_title || "").trim();
        const displayName = String(body.display_name || "수강생").trim().slice(0, 80) || "수강생";
        const summary = String(body.summary || "").trim().slice(0, 500);
        const bodyText = String(body.body || "").trim().slice(0, 4000);
        if (!classTitle) response = fail(400, "수업명을 입력하세요.");
        else if (!summary && !bodyText) response = fail(400, "후기 내용을 입력하세요.");
        else if (!body.consent_public_review) response = fail(400, "후기 검수와 공개 후보 등록에 동의해야 합니다.");
        else if (body.instructor_id && !(await getReviewInstructor(env, body.instructor_id))) response = fail(400, "선택한 강사를 찾을 수 없습니다.");
        else {
          const id = crypto.randomUUID();
          const created = now();
          const rawRating = Number(body.rating || 5);
          const rating = Number.isFinite(rawRating) ? Math.max(1, Math.min(5, rawRating)) : 5;
          const tags = listText(["수강생 제출", `평점 ${rating}점`, ...listFromValue(body.tags)]);
          const storedBody = [`작성자 공개명: ${displayName}`, `평점: ${rating}점`, bodyText ? `\n${bodyText}` : ""].join("\n").trim();
          await env.DB.prepare(
            `INSERT INTO review_entries (
              id, instructor_id, class_title, class_date, title, summary, body, tags, image_urls,
              status, source, privacy_checked, featured, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft', ?, 0, 0, ?, ?)`
          )
            .bind(
              id,
              body.instructor_id || invite.instructor_id || null,
              classTitle,
              String(body.class_date || invite.class_date || "").trim(),
              String(body.title || `${displayName}님의 수업 후기`).trim(),
              summary,
              storedBody,
              tags,
              listText(body.image_urls),
              `student_link:${invite.id}`,
              created,
              created
            )
            .run();
          await env.DB.prepare("UPDATE review_invites SET submitted_count=submitted_count+1, updated_at=? WHERE id=?").bind(created, invite.id).run();
          await logAction(env, "review_board", "review_submission_received", JSON.stringify({ entry_id: id, status: "draft", source: "student_link" }), request);
          response = json({
            ok: true,
            message: "후기가 접수되었습니다. 관리자가 개인정보를 확인하고 승인하면 후기보드에 공개됩니다.",
            data: { id, status: "draft" },
          });
        }
      } else {
        response = fail(405, "지원하지 않는 요청입니다.");
      }
    } else if (path === "/api/review-board" && request.method === "GET") {
      response = json({ ok: true, data: await reviewBoardRows(env, true) });
    } else {
      response = await handleAdmin(request, env, path);
    }
    return withCors(response, request, env);
  } catch (error) {
    return withCors(fail(500, error.message || "server error"), request, env);
  }
}

export default {
  fetch: handleRequest,
};

export const testables = {
  normalizePhone,
  maskPhone,
  sessionAcceptance,
  safeMember,
  accessCode,
  licenseCanonical,
  isLicenseVersionBlocked,
  licensePublic,
  defaultPaymentGuide,
  defaultLocationGuide,
  defaultRefundGuide,
};
