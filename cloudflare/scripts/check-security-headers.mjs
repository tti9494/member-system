// 실행 검증: 보안 헤더가 API 응답뿐 아니라 env.ASSETS 정적 파일 조기 return에도
// 반드시 적용된다 (withCors 경유). admin 페이지의 no-store 헤더도 유지돼야 한다.
import { handleRequest } from "../src/worker.js";

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

const stubAssets = {
  fetch: async () =>
    new Response("<!doctype html><title>stub</title>", {
      status: 200,
      headers: { "content-type": "text/html; charset=utf-8" },
    }),
};

function expectSecurityHeaders(response, label, { https = true } = {}) {
  assert(response.headers.get("x-content-type-options") === "nosniff", `${label}: nosniff missing`);
  assert(response.headers.get("x-frame-options") === "DENY", `${label}: x-frame-options missing`);
  assert(
    response.headers.get("referrer-policy") === "strict-origin-when-cross-origin",
    `${label}: referrer-policy missing`
  );
  assert(
    response.headers.get("permissions-policy") === "camera=(), microphone=(), geolocation=()",
    `${label}: permissions-policy missing`
  );
  const hsts = response.headers.get("strict-transport-security") || "";
  if (https) {
    assert(hsts === "max-age=31536000", `${label}: HSTS must be max-age=31536000 (got "${hsts}")`);
    assert(!hsts.includes("includeSubDomains"), `${label}: HSTS must not include includeSubDomains`);
  } else {
    assert(hsts === "", `${label}: HSTS must be absent on http`);
  }
}

// 1) 일반 정적 asset 조기 return에도 보안 헤더가 붙는다.
const asset = await handleRequest(
  new Request("https://apply.arsen-ai.com/frontend/yoonbot.html"),
  { ASSETS: stubAssets }
);
assert(asset.status === 200, "asset: stub asset must return 200");
expectSecurityHeaders(asset, "asset early-return");

// 2) admin 페이지는 no-store 캐시 헤더를 유지한 채 보안 헤더도 받는다.
const admin = await handleRequest(
  new Request("https://apply.arsen-ai.com/frontend/admin.html"),
  { ASSETS: stubAssets }
);
assert(admin.status === 200, "admin asset: stub asset must return 200");
assert(admin.headers.get("cache-control") === "no-store, max-age=0", "admin asset: no-store must be kept");
assert(admin.headers.get("pragma") === "no-cache", "admin asset: pragma no-cache must be kept");
expectSecurityHeaders(admin, "admin asset early-return");

// 3) API 경로 응답에도 동일 헤더.
const api = await handleRequest(new Request("https://apply.arsen-ai.com/health"), {});
assert(api.status === 200, "api: /health must return 200");
expectSecurityHeaders(api, "api response");

// 4) HTTP(비TLS) 요청에는 HSTS가 붙지 않는다.
const httpAsset = await handleRequest(
  new Request("http://localhost:8788/frontend/yoonbot.html"),
  { ASSETS: stubAssets }
);
expectSecurityHeaders(httpAsset, "http asset", { https: false });

// 5) 최상위 오류도 고정 문구 + 보안 헤더 (ASSETS.fetch가 throw해도 500 고정 응답).
const broken = await handleRequest(
  new Request("https://apply.arsen-ai.com/frontend/yoonbot.html"),
  { ASSETS: { fetch: async () => { throw new Error("stub asset failure"); } } }
);
assert(broken.status === 500, "error path: must be 500");
const brokenBody = await broken.json();
assert(
  String(brokenBody?.detail || "").includes("서버 내부 오류가 발생했습니다"),
  "error path: fixed client message required"
);
assert(!JSON.stringify(brokenBody).includes("stub asset failure"), "error path: error.message must not leak");
expectSecurityHeaders(broken, "error response");

// 6) 관리자 인증 계약 (FastAPI parity): ADMIN_API_KEY 미설정 admin 요청은 503,
//    잘못된 키는 401.
const adminUnconfigured = await handleRequest(
  new Request("https://apply.arsen-ai.com/admin/licenses"),
  {}
);
assert(adminUnconfigured.status === 503, `admin auth: unconfigured ADMIN_API_KEY must be 503 (got ${adminUnconfigured.status})`);
expectSecurityHeaders(adminUnconfigured, "admin unconfigured response");

const adminWrongKey = await handleRequest(
  new Request("https://apply.arsen-ai.com/admin/licenses", {
    headers: { "x-admin-key": "wrong-key" },
  }),
  { ADMIN_API_KEY: "expected-admin-key" }
);
assert(adminWrongKey.status === 401, `admin auth: wrong key must be 401 (got ${adminWrongKey.status})`);
expectSecurityHeaders(adminWrongKey, "admin wrong-key response");

console.log("security headers contract ok");
