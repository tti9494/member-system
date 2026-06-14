import { existsSync, readFileSync } from "node:fs";

const root = new URL("..", import.meta.url);
const repo = new URL("../..", import.meta.url);
const base = process.env.ARSEN_MEMBER_BASE_URL || "https://apply.arsen-ai.com";

function parseEnv(path) {
  if (!existsSync(path)) return {};
  const result = {};
  for (const line of readFileSync(path, "utf8").split(/\r?\n/)) {
    const match = line.match(/^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/);
    if (!match) continue;
    let value = match[2].trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    result[match[1]] = value;
  }
  return result;
}

async function getJson(path, headers = {}) {
  const response = await fetch(`${base}${path}`, { headers });
  const body = await response.json().catch(() => null);
  return { status: response.status, body };
}

async function postJson(path, payload = {}, headers = {}) {
  const response = await fetch(`${base}${path}`, {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: JSON.stringify(payload),
  });
  const body = await response.json().catch(() => null);
  return { status: response.status, body };
}

async function getPage(path) {
  const response = await fetch(`${base}${path}`);
  const text = await response.text();
  return {
    status: response.status,
    final_path: response.url.replace(base, ""),
    html: (response.headers.get("content-type") || "").includes("text/html"),
    has_expected_ui: /강의|신청|관리자|예약자/.test(text),
    has_delete_excluded_filter: text.includes("삭제 제외"),
  };
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

const env = {
  ...parseEnv(new URL(".secrets.local", root).pathname),
  ...parseEnv(new URL(".env", repo).pathname),
};
const adminKey = env.ADMIN_API_KEY || "";

const health = await getJson("/health");
const sessions = await getJson("/sessions");
const blockedStats = await getJson("/stats");
const rootPage = await getPage("/");
const join = await getPage("/frontend/join-full.html");
const statusPage = await getPage("/frontend/status.html");
const adminPage = await getPage("/frontend/admin.html");

assert(health.status === 200 && health.body?.ok, "health check failed");
assert(rootPage.status === 200 && rootPage.html, "root page failed");
assert(join.status === 200 && join.html && join.has_expected_ui, "join page failed");
assert(statusPage.status === 200 && statusPage.html && statusPage.has_expected_ui, "status page failed");
assert(adminPage.status === 200 && adminPage.html && adminPage.has_expected_ui, "admin page failed");
assert(adminPage.has_delete_excluded_filter, "admin member default filter is missing");
assert(sessions.status === 200 && Array.isArray(sessions.body?.data), "sessions API failed");
assert(blockedStats.status === 401, "admin API should reject missing key");

const output = {
  base,
  health: health.status,
  pages: { root: rootPage.status, join: join.status, status: statusPage.status, admin: adminPage.status },
  public_sessions: sessions.body.data.length,
  admin_without_key: blockedStats.status,
};

if (adminKey) {
  const headers = { "X-Admin-Key": adminKey };
  const stats = await getJson("/stats", headers);
  const members = await getJson("/members", headers);
  const bookings = await getJson("/admin/bookings", headers);
  assert(stats.status === 200 && stats.body?.ok, "admin stats failed");
  assert(members.status === 200 && members.body?.ok, "admin members failed");
  assert(bookings.status === 200 && bookings.body?.ok && Array.isArray(bookings.body.data), "admin bookings failed");
  const activeTestMembers = (members.body.data || []).filter(
    (member) => member.status !== "erased" && String(member.name || "").includes("테스트"),
  );
  assert(activeTestMembers.length === 0, "active test members still visible");
  const confirmedBooking = bookings.body.data.find((booking) => booking.status === "confirmed");
  if (confirmedBooking) {
    const locationGuide = await postJson(
      `/admin/bookings/${encodeURIComponent(confirmedBooking.id)}/location-guide`,
      {},
      headers,
    );
    const guide = String(locationGuide.body?.location_guide || "");
    assert(locationGuide.status === 200 && locationGuide.body?.ok, "location guide endpoint failed");
    assert(guide.split("\n").length >= 8, "location guide must be multiline");
    assert(!guide.includes("\\n"), "location guide contains literal backslash-n");
    assert(guide.includes("[장소 안내]") && guide.includes("준비물:"), "location guide copy contract failed");
  }
  output.admin_with_key = {
    stats: stats.status,
    members: members.status,
    bookings: bookings.status,
    member_total: members.body.total,
    active_test_members: activeTestMembers.length,
    location_guide_checked: Boolean(confirmedBooking),
  };
}

console.log(JSON.stringify(output, null, 2));
