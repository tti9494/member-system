const DEFAULT_PRICE = 100000;
const DEFAULT_TITLE = "AI 결과물 제작 초급 4주반";
const DEFAULT_DESCRIPTION = "AI 도구를 실제 결과물로 연결하는 초급 4주 실습반입니다. 현재 시간과 장소를 수요 확인 중입니다.";
const DEFAULT_LOCATION = "추후 공지";
const DEFAULT_MATERIALS = "노트북, 충전기, 사용 중인 AI 계정, 만들고 싶은 결과물 또는 업무 예시";
const FREE_CLASS_TITLE = "무료 AI 강의";
const FREE_CLASS_DESCRIPTION = "AI 입문자를 위한 계정 세팅, 실습 방향, 업무 활용 예시를 무료로 안내합니다.";
const FREE_CLASS_MATERIALS = "노트북 또는 태블릿, 충전기, 사용 중인 AI 계정 정보, 궁금한 자동화 주제";
const FREE_CLASS_LOCATION = "장소 추후 안내";
const STUDY_PROGRAM_TYPE = "study";
const CLOUDFLARE_VERSION = "cloudflare-v1";
const PRODUCTION_ROUTE = "apply.arsen-ai.com/*";
const D1_DATABASE_NAME = "arsen_member_system";
const KAKAO_NOTICE_STATE_KEY = "kakao_notice_jobs_v1";
const KAKAO_NOTICE_JOB_LIMIT = 20;
const KAKAO_NOTICE_DEFAULT_MATERIALS = "노트북 또는 태블릿, 충전기, 사용 중인 AI 계정 정보, 궁금한 자동화 주제";
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
    description: "1개월 단위로 YOONBOT을 사용합니다.",
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
const CONSULTATION_STATUSES = new Set(["new", "contacted", "on_hold", "closed", "spam"]);
const DEFAULT_SITE_THEME_ID = "arsen-modern";
const KAKAO_AUTHORIZE_URL = "https://kauth.kakao.com/oauth/authorize";
const KAKAO_TOKEN_URL = "https://kauth.kakao.com/oauth/token";
const KAKAO_USER_ME_URL = "https://kapi.kakao.com/v2/user/me";
const KAKAO_STATE_COOKIE = "arsen_kakao_state";
const KAKAO_SESSION_COOKIE = "arsen_kakao_session";
const KAKAO_SESSION_MAX_AGE = 60 * 60 * 24 * 30;
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
const LAUNCHER_ARTIFACT_NAME = "arsen-content-launcher-0.1.0-win-x64.zip";
const LAUNCHER_ARTIFACT_KEY = LAUNCHER_ARTIFACT_NAME;
const LAUNCHER_ASSET_MANIFEST_PATH = `/launcher-artifacts/${LAUNCHER_ARTIFACT_NAME}.manifest.json`;
const LAUNCHER_RELEASE_URL = "https://apply.arsen-ai.com/api/launcher/release";
const LAUNCHER_DIRECT_DOWNLOAD_URL = `https://apply.arsen-ai.com/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`;
const LAUNCHER_RELEASE = Object.freeze({
  id: "arsen-content-launcher",
  name: "Arsen Content Launcher",
  version: "0.1.0",
  latest_version: "0.1.0",
  min_supported_version: "0.1.0",
  platform: "win32",
  arch: "x64",
  package_type: "zip",
  executable: "Arsen Content Launcher.exe",
  artifact_name: LAUNCHER_ARTIFACT_NAME,
  artifact_url: "",
  artifact_download_url: "",
  size_bytes: 147951169,
  sha256: "3B0AB1E9A2295BC45757848C28EF96F6885CC7D5AFEA790DF8AAC8A25808FA75",
  built_at: "2026-06-17T15:36:25+09:00",
  release_channel: "internal",
  update_policy: {
    auto_download: false,
    force_update: false,
    show_release_notes_on_start: true,
    show_notice_panel_on_start: true,
  },
  release_notes: [
    "Windows 런처 공지/업데이트 패널을 추가했습니다.",
    "고객용/내부용 프로그램 노출을 분리했습니다.",
    "피드백 접수와 민감정보 마스킹을 추가했습니다.",
    "HTTPS 다운로드와 SHA-256 검증 흐름을 준비했습니다.",
  ],
});
const LAUNCHER_PROGRAMS = Object.freeze([
  {
    id: "blog-lite",
    name: "Blog Studio Lite",
    version: "0.1.0",
    status: "public_preview",
    runtime: "web",
    description: "로그인 없이 키워드 발굴과 초안 맛보기를 제공하는 무료 체험 화면입니다.",
    entrypoint: "/blog-lite",
    expose_to_customer: true,
    internal_only: false,
    launcher_action: "open_url",
    features: [
      { id: "free_keyword_discovery", name: "키워드 발굴 10회/일", tier: "free", unlocked: true },
      { id: "free_draft_preview", name: "초안 3회/일", tier: "free", unlocked: true },
      { id: "save_draft", name: "초안 저장", tier: "basic", unlocked: false },
      { id: "agency_queue", name: "대량 작업 큐", tier: "agency", unlocked: false },
    ],
  },
  {
    id: "saas-studio",
    name: "Sales Trial Studio",
    version: "0.1.0",
    status: "public_preview",
    runtime: "web",
    description: "무료/유료 티어, 기능 잠금, 고객 체험 흐름을 확인하는 판매용 체험 화면입니다.",
    entrypoint: "/saas-studio",
    expose_to_customer: true,
    internal_only: false,
    launcher_action: "open_url",
    features: [
      { id: "tier_preview", name: "요금제 미리보기", tier: "free", unlocked: true },
      { id: "feature_lock_preview", name: "기능 잠금 미리보기", tier: "free", unlocked: true },
      { id: "billing_connection", name: "결제/라이선스 연결", tier: "pro", unlocked: false },
    ],
  },
  {
    id: "restaurant-studio",
    name: "Restaurant Studio",
    version: "0.1.0",
    status: "internal_beta",
    runtime: "web_and_local_cli",
    description: "맛집, 장소, 카페 콘텐츠를 후보 목록과 방문 전 체크 정보 중심으로 정리합니다.",
    entrypoint: "/restaurant-studio",
    expose_to_customer: true,
    internal_only: false,
    launcher_action: "open_url",
    features: [
      { id: "place_candidates", name: "장소 후보 정리", tier: "basic", unlocked: false },
      { id: "photo_context", name: "사진 기반 글쓰기", tier: "pro", unlocked: false },
      { id: "rights_notice", name: "이미지 권리 고지", tier: "pro", unlocked: false },
    ],
  },
  {
    id: "output-studio",
    name: "Output Studio",
    version: "0.1.0",
    status: "internal_beta",
    runtime: "web",
    description: "생성된 초안, 검증 점수, 채널별 문안, 승인 대기 목록을 확인합니다.",
    entrypoint: "/output-studio",
    expose_to_customer: true,
    internal_only: false,
    launcher_action: "open_url",
    features: [
      { id: "review_outputs", name: "결과물 검토", tier: "basic", unlocked: false },
      { id: "channel_copy", name: "채널별 문안 분리", tier: "pro", unlocked: false },
      { id: "approval_gate", name: "승인 게이트", tier: "agency", unlocked: false },
    ],
  },
]);
const LAUNCHER_NOTICES = Object.freeze([
  {
    id: "2026-06-17-launcher-contract",
    type: "update",
    level: "info",
    pinned: true,
    title: "ARSEN Launcher 파일럿 화면을 새롭게 정리했습니다.",
    body: "프로그램 안내, 서비스 연결 상태, 업데이트 정보와 중요 공지를 첫 화면에서 더 쉽게 확인할 수 있습니다.",
    date: "2026-07-26",
    published_at: "2026-07-26T18:00:00+09:00",
    show_in_launcher: true,
    show_in_website: true,
    dismissible: true,
  },
  {
    id: "2026-06-17-no-external-publish",
    type: "policy",
    level: "warning",
    pinned: true,
    title: "외부 발행은 승인 전까지 실행하지 않습니다.",
    body: "네이버, 워드프레스, 스레드 게시 기능은 별도 승인과 계정 보안 검토 후 연결합니다. 현재 화면은 초안 생성, 검토, 배포 준비까지를 기준으로 합니다.",
    date: "2026-06-17",
    published_at: "2026-06-17T14:35:00+09:00",
    show_in_launcher: true,
    show_in_website: true,
    dismissible: false,
  },
  {
    id: "2026-06-17-windows-handoff",
    type: "security",
    level: "info",
    pinned: false,
    title: "업데이트 파일은 기기와 보안 정보를 확인한 뒤 저장합니다.",
    body: "현재 제공 중인 Windows x64 파일은 HTTPS 공식 경로와 SHA-256 체크섬을 검증합니다. 자동 설치나 이전 버전 덮어쓰기는 실행하지 않습니다.",
    date: "2026-07-26",
    published_at: "2026-07-26T18:05:00+09:00",
    show_in_launcher: true,
    show_in_website: true,
    dismissible: true,
  },
]);
// YOONBOT Windows app public update contract. Fully separated from the
// Arsen Content Launcher artifact: different name, storage key/binding,
// asset path, and content type.
const YOONBOT_ARTIFACT_NAME = "YoonBot-Setup-1.1.0.exe";
const YOONBOT_ARTIFACT_KEY = YOONBOT_ARTIFACT_NAME;
const YOONBOT_ASSET_MANIFEST_PATH = `/yoonbot-artifacts/${YOONBOT_ARTIFACT_NAME}.manifest.json`;
const YOONBOT_EXE_CONTENT_TYPE = "application/vnd.microsoft.portable-executable";
const YOONBOT_RELEASE = Object.freeze({
  id: "yoonbot-windows",
  name: "YOONBOT",
  product_code: YOONBOT_PRODUCT_CODE,
  platform: "win32",
  arch: "x64",
  package_type: "exe",
  executable: YOONBOT_ARTIFACT_NAME,
  latest_version: "1.1.0",
  minimum_supported_version: "1.0.0",
  release_channel: "stable",
  artifact_name: YOONBOT_ARTIFACT_NAME,
  release_notes: [
    "YOONBOT 1.1.0 Windows 업데이트입니다.",
    "공식 HTTPS 다운로드와 SHA-256 검증 정보를 함께 제공합니다.",
  ],
});
const YOONBOT_NOTICES = Object.freeze([
  {
    id: "2026-08-28-yoonbot-1-1-0-update",
    type: "update",
    level: "info",
    pinned: true,
    title: "YOONBOT 1.1.0 업데이트 안내",
    body: "업데이트 파일은 공식 HTTPS 경로와 SHA-256 검증 정보가 준비된 경우에만 내려받기가 활성화됩니다.",
    published_at: "2026-08-28T09:00:00+09:00",
    dismissible: true,
  },
]);
const LAUNCHER_TIERS = Object.freeze([
  { id: "free", name: "무료 체험", audience: "가망 고객", internal_only: false, daily_limits: { keyword_discovery: 10, draft_generation: 3 }, enabled_features: ["키워드 발굴", "초안 일부 미리보기", "기본 품질 점수"], locked_features: ["초안 저장", "전체 본문 보기", "플랫폼별 발행 준비", "계정 연결"] },
  { id: "basic", name: "기본", audience: "개인 블로거", internal_only: false, daily_limits: { draft_generation: 10, connected_channels: 1 }, enabled_features: ["전체 초안", "초안 저장", "기본 재작성", "복사/내보내기"], locked_features: ["대량 작업 큐", "고급 검증 루프", "여러 채널 연결"] },
  { id: "pro", name: "전문가", audience: "파워블로거/소규모 사업자", internal_only: false, daily_limits: { draft_generation: 50, connected_channels: 5 }, enabled_features: ["고급 검증/재작성", "플랫폼별 문안", "키워드 저장", "사진 맥락 반영"], locked_features: ["고객별 작업 공간", "대행사 대량 큐"] },
  { id: "agency", name: "대행사", audience: "대행사/팀", internal_only: false, daily_limits: { draft_generation: "unlimited", connected_channels: 30 }, enabled_features: ["대량 작업 큐", "고객별 관리", "승인 워크플로우", "결과물 관리", "팀 운영"], locked_features: [] },
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

async function launcherAssetManifest(env, request) {
  if (!env.ASSETS || typeof env.ASSETS.fetch !== "function") return null;
  const manifestUrl = new URL(request.url);
  manifestUrl.pathname = LAUNCHER_ASSET_MANIFEST_PATH;
  manifestUrl.search = "";
  const response = await env.ASSETS.fetch(new Request(manifestUrl, { method: "GET" }));
  if (!response.ok) return null;
  const manifest = await response.json().catch(() => null);
  if (manifest?.artifact_name !== LAUNCHER_ARTIFACT_NAME) return null;
  if (Number(manifest.size_bytes) !== Number(LAUNCHER_RELEASE.size_bytes)) return null;
  if (String(manifest.sha256 || "").toUpperCase() !== LAUNCHER_RELEASE.sha256) return null;
  if (!Array.isArray(manifest.chunks) || !manifest.chunks.length) return null;
  return manifest;
}

async function launcherArtifactDownloadUrl(env, request) {
  const explicit = String(env.LAUNCHER_ARTIFACT_DOWNLOAD_URL || "").trim();
  if (explicit.startsWith("https://")) return explicit;
  const base = String(env.LAUNCHER_ARTIFACT_BASE_URL || "").trim().replace(/\/+$/, "");
  if (base.startsWith("https://")) {
    const requestOrigin = new URL(request.url).origin;
    if (base === requestOrigin) return "";
    return `${base}/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`;
  }
  if (env.LAUNCHER_RELEASES && typeof env.LAUNCHER_RELEASES.get === "function") {
    const url = new URL(request.url);
    if (url.protocol === "https:") return `${url.origin}/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`;
  }
  if (await launcherAssetManifest(env, request)) {
    const url = new URL(request.url);
    if (url.protocol === "https:") return `${url.origin}/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`;
  }
  return "";
}

function launcherArtifactHeaders(sizeBytes) {
  const headers = new Headers();
  headers.set("content-type", "application/zip");
  headers.set("content-disposition", `attachment; filename="${LAUNCHER_ARTIFACT_NAME}"`);
  headers.set("content-length", String(sizeBytes));
  headers.set("cache-control", "public, max-age=31536000, immutable");
  headers.set("x-content-type-options", "nosniff");
  return headers;
}

async function launcherAssetArtifactResponse(env, request) {
  const manifest = await launcherAssetManifest(env, request);
  if (!manifest) return null;
  const headers = launcherArtifactHeaders(manifest.size_bytes);
  if (request.method === "HEAD") return new Response(null, { headers });

  const body = new ReadableStream({
    async start(controller) {
      try {
        for (const chunk of manifest.chunks) {
          const chunkUrl = new URL(request.url);
          chunkUrl.pathname = chunk.path;
          chunkUrl.search = "";
          const response = await env.ASSETS.fetch(new Request(chunkUrl, { method: "GET" }));
          if (!response.ok || !response.body) throw new Error(`launcher_artifact_chunk_missing:${chunk.path}`);
          const reader = response.body.getReader();
          try {
            while (true) {
              const { done, value } = await reader.read();
              if (done) break;
              controller.enqueue(value);
            }
          } finally {
            reader.releaseLock();
          }
        }
        controller.close();
      } catch (error) {
        controller.error(error);
      }
    },
  });
  return new Response(body, { headers });
}

async function launcherArtifactResponse(env, request) {
  const explicitUrl = String(env.LAUNCHER_ARTIFACT_DOWNLOAD_URL || "").trim();
  if (explicitUrl.startsWith("https://")) return Response.redirect(explicitUrl, 302);

  const base = String(env.LAUNCHER_ARTIFACT_BASE_URL || "").trim().replace(/\/+$/, "");
  if (base.startsWith("https://") && base !== new URL(request.url).origin) {
    return Response.redirect(`${base}/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`, 302);
  }

  const assetResponse = await launcherAssetArtifactResponse(env, request);
  if (assetResponse) return assetResponse;

  if (!env.LAUNCHER_RELEASES || typeof env.LAUNCHER_RELEASES.get !== "function") {
    return fail(503, "launcher_artifact_storage_not_configured");
  }

  const object = await env.LAUNCHER_RELEASES.get(LAUNCHER_ARTIFACT_KEY);
  if (!object) return fail(404, "launcher_artifact_missing");

  const headers = new Headers();
  if (typeof object.writeHttpMetadata === "function") object.writeHttpMetadata(headers);
  headers.set("content-type", headers.get("content-type") || "application/zip");
  headers.set("content-disposition", `attachment; filename="${LAUNCHER_ARTIFACT_NAME}"`);
  headers.set("accept-ranges", "bytes");
  if (object.size) headers.set("content-length", String(object.size));
  if (object.httpEtag) headers.set("etag", object.httpEtag);
  return new Response(request.method === "HEAD" ? null : object.body, { headers });
}

async function launcherReleasePayload(env, request) {
  const artifactDownloadUrl = await launcherArtifactDownloadUrl(env, request);
  return {
    ...LAUNCHER_RELEASE,
    artifact_download_url: artifactDownloadUrl,
    artifact_url: artifactDownloadUrl,
    artifact_endpoint: `/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`,
    artifact_available: Boolean(artifactDownloadUrl),
  };
}

function launcherNoticesPayload(params = {}) {
  const audience = params.audience || "";
  const level = params.level || "";
  return LAUNCHER_NOTICES
    .filter((notice) => !level || notice.level === level)
    .filter((notice) => audience !== "launcher" || notice.show_in_launcher !== false)
    .filter((notice) => audience !== "website" || notice.show_in_website !== false)
    .sort((left, right) => {
      const pinned = Number(Boolean(right.pinned)) - Number(Boolean(left.pinned));
      if (pinned) return pinned;
      return String(right.published_at || "").localeCompare(String(left.published_at || ""));
    });
}

async function launcherManifestPayload(env, request) {
  return {
    schema_version: "arsen.launcher_manifest.v1",
    updated_at: "2026-06-17T14:30:00+09:00",
    cache_ttl_seconds: 300,
    channels: ["internal", "preview", "stable"],
    runtime: {
      service_id: "arsen-blog-automation",
      service_name: "Arsen Blog Automation",
      mode: "public_release",
      api_version: "2026-06-17",
      distribution_policy: {
        official_download_only: true,
        external_publish_enabled: false,
        payment_enabled: false,
        requires_user_approval_for_publish: true,
      },
    },
    product_strategy: {
      decision: "reuse_engine_separate_customer_product",
      summary: "내부 Blog Studio 엔진은 유지하되, 판매용 제품은 별도 고객 화면과 권한 계층으로 분리합니다.",
      tracks: [
        { id: "customer_saas", name: "판매용 웹 서비스", audience: "무료 체험/유료 고객", status: "preview", entrypoint: "/saas-studio", expose_to_customer: true, internal_only: false },
        { id: "vertical_generators", name: "전용 생성기", audience: "특화 유료 고객", status: "planned", entrypoint: "/restaurant-studio", expose_to_customer: true, internal_only: false },
      ],
    },
    tiers: LAUNCHER_TIERS,
    launcher: await launcherReleasePayload(env, request),
    programs: LAUNCHER_PROGRAMS,
    notices: launcherNoticesPayload({ audience: "launcher" }),
    served_at: now(),
    source: "member-system-cloudflare",
  };
}

async function adminLauncherStatusPayload(env, request) {
  const release = await launcherReleasePayload(env, request);
  const programs = LAUNCHER_PROGRAMS;
  const notices = launcherNoticesPayload({ audience: "launcher" });
  const visiblePrograms = programs.filter((program) => program.expose_to_customer && !program.internal_only);
  const pinnedNotices = notices.filter((notice) => notice.pinned);
  const warnings = [];
  if (!release.artifact_available) warnings.push("launcher_artifact_unavailable");
  if (!String(release.artifact_download_url || "").startsWith("https://")) warnings.push("launcher_artifact_url_not_https");
  if (!release.sha256) warnings.push("launcher_sha256_missing");
  if (!notices.length) warnings.push("launcher_notices_empty");
  return {
    service: "arsen-content-launcher",
    source: "member-system-cloudflare",
    managed_by: "cloudflare-worker-static-contract",
    editable: false,
    updated_at: "2026-06-17T14:30:00+09:00",
    served_at: now(),
    endpoints: {
      manifest: "/api/daf/manifest",
      programs: "/api/daf/programs",
      notices: "/api/daf/notices",
      release: "/api/launcher/release",
      artifact: release.artifact_endpoint || `/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}`,
    },
    release,
    metrics: {
      programs_total: programs.length,
      customer_programs: visiblePrograms.length,
      notices_total: notices.length,
      pinned_notices: pinnedNotices.length,
      release_notes: Array.isArray(release.release_notes) ? release.release_notes.length : 0,
    },
    checks: {
      artifact_available: Boolean(release.artifact_available),
      artifact_url_https: String(release.artifact_download_url || "").startsWith("https://"),
      sha256_present: Boolean(release.sha256),
      notice_panel_enabled: Boolean(release.update_policy?.show_notice_panel_on_start),
      release_notes_enabled: Boolean(release.update_policy?.show_release_notes_on_start),
      customer_programs_only: visiblePrograms.length === programs.length,
    },
    warnings,
    programs,
    notices,
  };
}

function isSha256Hex(value) {
  return /^[0-9a-f]{64}$/.test(String(value || "").trim().toLowerCase());
}

async function yoonbotAssetManifest(env, request) {
  if (!env.ASSETS || typeof env.ASSETS.fetch !== "function") return null;
  const manifestUrl = new URL(request.url);
  manifestUrl.pathname = YOONBOT_ASSET_MANIFEST_PATH;
  manifestUrl.search = "";
  const response = await env.ASSETS.fetch(new Request(manifestUrl, { method: "GET" }));
  if (!response.ok) return null;
  const manifest = await response.json().catch(() => null);
  if (manifest?.artifact_name !== YOONBOT_ARTIFACT_NAME) return null;
  if (!Number.isFinite(Number(manifest.size_bytes)) || Number(manifest.size_bytes) <= 0) return null;
  if (!isSha256Hex(manifest.sha256)) return null;
  if (!Array.isArray(manifest.chunks) || !manifest.chunks.length) return null;
  return manifest;
}

// Single validation rule for an R2 object: shared by the release contract
// (head) and the direct GET/HEAD artifact path so an object that fails the
// contract can never be served.
function yoonbotR2ObjectContract(object) {
  if (!object) return null;
  const sha256 = String(object.customMetadata?.sha256 || "").trim().toLowerCase();
  const sizeBytes = Number(object.size || 0);
  if (!isSha256Hex(sha256) || !(sizeBytes > 0)) return null;
  return { sha256, size_bytes: sizeBytes };
}

async function yoonbotR2Contract(env) {
  if (!env.YOONBOT_RELEASES || typeof env.YOONBOT_RELEASES.head !== "function") return null;
  return yoonbotR2ObjectContract(await env.YOONBOT_RELEASES.head(YOONBOT_ARTIFACT_KEY));
}

// Single validation rule for the explicit external URL: HTTPS + real 64-hex
// SHA-256 + positive size, or nothing. Shared by release and artifact paths.
function yoonbotExplicitUrlContract(env) {
  const explicitUrl = String(env.YOONBOT_ARTIFACT_DOWNLOAD_URL || "").trim();
  if (!explicitUrl) return null;
  const sha256 = String(env.YOONBOT_ARTIFACT_SHA256 || "").trim().toLowerCase();
  const sizeBytes = Number(env.YOONBOT_ARTIFACT_SIZE_BYTES || 0);
  if (!explicitUrl.startsWith("https://") || !isSha256Hex(sha256) || !(sizeBytes > 0)) return null;
  return { download_ready: true, artifact_download_url: explicitUrl, sha256, size_bytes: sizeBytes };
}

const YOONBOT_CODE_SIGNING_READY_STATUS = "signed";
const YOONBOT_BLOCKED_CODE_SIGNING = "blocked_code_signing";
const YOONBOT_BLOCKED_RELEASE_APPROVAL = "blocked_release_ready_approval";
const YOONBOT_BLOCKED_ARTIFACT_UNVERIFIED = "blocked_artifact_unverified";

function yoonbotCodeSigningStatus(env) {
  const status = String(env.YOONBOT_CODE_SIGNING_STATUS || "").trim().toLowerCase();
  return status || "not_signed";
}

function yoonbotReleaseReadyApproved(env) {
  return String(env.YOONBOT_RELEASE_READY_APPROVED || "").trim().toLowerCase() === "true";
}

// Operator gates for the public download. Fail-closed by default: an
// unsigned build or an unapproved release never goes public, even when a
// verified artifact exists and every storage check passes.
function yoonbotReleaseGateBlocks(env) {
  const blocked = [];
  if (yoonbotCodeSigningStatus(env) !== YOONBOT_CODE_SIGNING_READY_STATUS) blocked.push(YOONBOT_BLOCKED_CODE_SIGNING);
  if (!yoonbotReleaseReadyApproved(env)) blocked.push(YOONBOT_BLOCKED_RELEASE_APPROVAL);
  return blocked;
}

// Verified download source (HTTPS URL + 64-hex SHA-256 + size > 0) or null.
// Never invents checksum, size, or availability.
async function yoonbotVerifiedArtifactSource(env, request) {
  const explicitUrl = String(env.YOONBOT_ARTIFACT_DOWNLOAD_URL || "").trim();
  if (explicitUrl) {
    const explicitContract = yoonbotExplicitUrlContract(env);
    if (!explicitContract) return null;
    return {
      artifact_download_url: explicitContract.artifact_download_url,
      sha256: explicitContract.sha256,
      size_bytes: explicitContract.size_bytes,
      source: "external_url",
    };
  }
  const origin = new URL(request.url);
  if (origin.protocol !== "https:") return null;
  const selfDownloadUrl = `${origin.origin}/api/yoonbot/artifacts/${YOONBOT_ARTIFACT_NAME}`;
  const assetManifest = await yoonbotAssetManifest(env, request);
  if (assetManifest) {
    return {
      artifact_download_url: selfDownloadUrl,
      sha256: String(assetManifest.sha256).trim().toLowerCase(),
      size_bytes: Number(assetManifest.size_bytes),
      source: "pages_assets",
    };
  }
  const r2Contract = await yoonbotR2Contract(env);
  if (r2Contract) {
    return { artifact_download_url: selfDownloadUrl, ...r2Contract, source: "r2" };
  }
  return null;
}

// Fail-closed: download_ready only with a verified source AND the operator
// gates (code signing + release-ready approval) all passing.
async function yoonbotArtifactContract(env, request) {
  const closed = { download_ready: false, artifact_download_url: "", sha256: "", size_bytes: 0 };
  if (yoonbotReleaseGateBlocks(env).length) return closed;
  const verified = await yoonbotVerifiedArtifactSource(env, request);
  if (!verified) return closed;
  return {
    download_ready: true,
    artifact_download_url: verified.artifact_download_url,
    sha256: verified.sha256,
    size_bytes: verified.size_bytes,
  };
}

async function adminYoonbotReleaseStatusPayload(env, request) {
  const gateBlocks = yoonbotReleaseGateBlocks(env);
  const verified = await yoonbotVerifiedArtifactSource(env, request);
  const blockedReasons = verified ? gateBlocks : [...gateBlocks, YOONBOT_BLOCKED_ARTIFACT_UNVERIFIED];
  const codeSigningStatus = yoonbotCodeSigningStatus(env);
  const downloadReady = Boolean(verified) && gateBlocks.length === 0;
  return {
    service: "yoonbot-windows-release",
    source: "member-system-cloudflare",
    served_at: now(),
    latest_version: YOONBOT_RELEASE.latest_version,
    minimum_supported_version: YOONBOT_RELEASE.minimum_supported_version,
    artifact_name: YOONBOT_ARTIFACT_NAME,
    sha256: verified ? verified.sha256 : "",
    size_bytes: verified ? verified.size_bytes : 0,
    artifact_source: verified ? verified.source : "",
    artifact_verified: Boolean(verified),
    code_signing_status: codeSigningStatus,
    code_signing_ready: codeSigningStatus === YOONBOT_CODE_SIGNING_READY_STATUS,
    release_ready_approved: yoonbotReleaseReadyApproved(env),
    download_ready: downloadReady,
    public_status: downloadReady ? "available" : "preparing",
    blocked_reasons: blockedReasons,
    endpoints: {
      manifest: "/api/yoonbot/manifest",
      release: "/api/yoonbot/release",
      artifact: `/api/yoonbot/artifacts/${YOONBOT_ARTIFACT_NAME}`,
    },
  };
}

function yoonbotArtifactHeaders(sizeBytes) {
  const headers = new Headers();
  headers.set("content-type", YOONBOT_EXE_CONTENT_TYPE);
  headers.set("content-disposition", `attachment; filename="${YOONBOT_ARTIFACT_NAME}"`);
  headers.set("content-length", String(sizeBytes));
  headers.set("cache-control", "public, max-age=31536000, immutable");
  headers.set("x-content-type-options", "nosniff");
  return headers;
}

async function yoonbotAssetArtifactResponse(env, request) {
  const manifest = await yoonbotAssetManifest(env, request);
  if (!manifest) return null;
  const headers = yoonbotArtifactHeaders(manifest.size_bytes);
  if (request.method === "HEAD") return new Response(null, { headers });

  const body = new ReadableStream({
    async start(controller) {
      try {
        for (const chunk of manifest.chunks) {
          const chunkUrl = new URL(request.url);
          chunkUrl.pathname = chunk.path;
          chunkUrl.search = "";
          const response = await env.ASSETS.fetch(new Request(chunkUrl, { method: "GET" }));
          if (!response.ok || !response.body) throw new Error(`yoonbot_artifact_chunk_missing:${chunk.path}`);
          const reader = response.body.getReader();
          try {
            while (true) {
              const { done, value } = await reader.read();
              if (done) break;
              controller.enqueue(value);
            }
          } finally {
            reader.releaseLock();
          }
        }
        controller.close();
      } catch (error) {
        controller.error(error);
      }
    },
  });
  return new Response(body, { headers });
}

async function yoonbotArtifactResponse(env, request) {
  // Same operator gates as the release contract: an artifact closed in the
  // manifest can never be downloaded (or redirected to) directly either.
  if (yoonbotReleaseGateBlocks(env).length) return fail(404, "yoonbot_release_not_ready");
  const explicitUrl = String(env.YOONBOT_ARTIFACT_DOWNLOAD_URL || "").trim();
  if (explicitUrl) {
    const explicitContract = yoonbotExplicitUrlContract(env);
    if (!explicitContract) return fail(404, "yoonbot_artifact_not_verified");
    return Response.redirect(explicitContract.artifact_download_url, 302);
  }

  const assetResponse = await yoonbotAssetArtifactResponse(env, request);
  if (assetResponse) return assetResponse;

  if (!env.YOONBOT_RELEASES || typeof env.YOONBOT_RELEASES.get !== "function") {
    return fail(503, "yoonbot_artifact_storage_not_configured");
  }

  const object = await env.YOONBOT_RELEASES.get(YOONBOT_ARTIFACT_KEY);
  if (!object) return fail(404, "yoonbot_artifact_missing");
  const r2Contract = yoonbotR2ObjectContract(object);
  if (!r2Contract) return fail(404, "yoonbot_artifact_not_verified");

  const headers = new Headers();
  headers.set("content-type", YOONBOT_EXE_CONTENT_TYPE);
  headers.set("content-disposition", `attachment; filename="${YOONBOT_ARTIFACT_NAME}"`);
  headers.set("x-content-type-options", "nosniff");
  headers.set("accept-ranges", "bytes");
  headers.set("content-length", String(r2Contract.size_bytes));
  if (object.httpEtag) headers.set("etag", object.httpEtag);
  return new Response(request.method === "HEAD" ? null : object.body, { headers });
}

async function yoonbotReleasePayload(env, request) {
  const contract = await yoonbotArtifactContract(env, request);
  return {
    ...YOONBOT_RELEASE,
    artifact_endpoint: `/api/yoonbot/artifacts/${YOONBOT_ARTIFACT_NAME}`,
    ...contract,
    status: contract.download_ready ? "available" : "preparing",
  };
}

function yoonbotNoticesPayload() {
  return YOONBOT_NOTICES
    .map((notice) => ({ ...notice }))
    .sort((left, right) => {
      const pinned = Number(Boolean(right.pinned)) - Number(Boolean(left.pinned));
      if (pinned) return pinned;
      return String(right.published_at || "").localeCompare(String(left.published_at || ""));
    });
}

async function yoonbotManifestPayload(env, request) {
  return {
    schema_version: "arsen.yoonbot_manifest.v1",
    server_time: now(),
    notices: yoonbotNoticesPayload(),
    release: await yoonbotReleasePayload(env, request),
    source: "member-system-cloudflare",
  };
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

function looksLikeLegacyEncryptedCode(value) {
  const text = String(value || "").trim();
  if (!text || text.length < 32 || !/[+/=]/.test(text)) return false;
  try {
    return base64ToBytes(text).length >= 32;
  } catch (_) {
    return false;
  }
}

async function readableAccessCode(member, env) {
  const stored = String(member?.access_code || "").trim();
  if (!stored) return "";
  if (!looksLikeLegacyEncryptedCode(stored)) return stored;
  try {
    return await decryptValue(stored, env, "CODE_SECRET_KEY");
  } catch (_) {
    return "";
  }
}

async function accessCodeMatches(member, input, env) {
  const code = await readableAccessCode(member, env);
  return Boolean(code) && code === String(input || "").trim();
}

function base64UrlFromBytes(bytes) {
  return bytesToBase64(bytes).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64UrlFromString(value) {
  return base64UrlFromBytes(new TextEncoder().encode(String(value || "")));
}

function stringFromBase64Url(value) {
  const normalized = String(value || "").replace(/-/g, "+").replace(/_/g, "/");
  const padded = normalized + "=".repeat((4 - (normalized.length % 4)) % 4);
  return new TextDecoder().decode(base64ToBytes(padded));
}

function cookieValue(request, name) {
  const cookie = request.headers.get("cookie") || "";
  for (const part of cookie.split(";")) {
    const [key, ...valueParts] = part.trim().split("=");
    if (key === name) return valueParts.join("=");
  }
  return "";
}

async function kakaoCookieSignature(env, body) {
  const secret = String(env.KAKAO_SESSION_SECRET || env.ADMIN_KEY || env.TELEGRAM_WEBHOOK_SECRET || "arsen-local-kakao-session");
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const signature = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(body));
  return base64UrlFromBytes(new Uint8Array(signature));
}

async function signedCookie(payload, env) {
  const body = base64UrlFromString(JSON.stringify(payload || {}));
  return `${body}.${await kakaoCookieSignature(env, body)}`;
}

async function readSignedCookie(request, env, name) {
  const value = cookieValue(request, name);
  if (!value || !value.includes(".")) return null;
  const [body, signature] = value.split(".", 2);
  if (signature !== await kakaoCookieSignature(env, body)) return null;
  try {
    const payload = JSON.parse(stringFromBase64Url(body));
    return payload && typeof payload === "object" ? payload : null;
  } catch (_) {
    return null;
  }
}

function cookieHeader(name, value, maxAge, request) {
  const secure = new URL(request.url).protocol === "https:" ? "; Secure" : "";
  return `${name}=${value}; Max-Age=${maxAge}; Path=/; HttpOnly; SameSite=Lax${secure}`;
}

function deleteCookieHeader(name) {
  return `${name}=; Max-Age=0; Path=/; HttpOnly; SameSite=Lax`;
}

function redirectWithCookies(url, cookies = []) {
  const headers = new Headers({ location: url });
  for (const cookie of cookies) headers.append("set-cookie", cookie);
  return new Response(null, { status: 302, headers });
}

function safeNextPath(value) {
  const next = String(value || "/frontend/member.html").trim();
  if (!next.startsWith("/") || next.startsWith("//") || next.startsWith("/auth/")) return "/frontend/member.html";
  return next;
}

function withKakaoStatus(nextPath, status) {
  const separator = nextPath.includes("?") ? "&" : "?";
  return `${nextPath}${separator}kakao=${encodeURIComponent(status)}`;
}

function kakaoRedirectUri(env, request) {
  const explicit = String(env.KAKAO_REDIRECT_URI || "").trim();
  if (explicit) return explicit;
  const url = new URL(request.url);
  return `${url.origin}/auth/kakao/callback`;
}

function kakaoProfilePayload(user) {
  const account = user?.kakao_account && typeof user.kakao_account === "object" ? user.kakao_account : {};
  const properties = user?.properties && typeof user.properties === "object" ? user.properties : {};
  const profile = account.profile && typeof account.profile === "object" ? account.profile : {};
  return {
    id: String(user?.id || ""),
    nickname: properties.nickname || profile.nickname || "",
    email: account.email || "",
    phone_number: account.phone_number || "",
    connected_at: user?.connected_at || "",
  };
}

function kakaoPublicPayload(session, member) {
  const profile = session?.profile && typeof session.profile === "object" ? session.profile : {};
  return {
    connected: true,
    linked: Boolean(session?.member_id && member),
    nickname: profile.nickname || "",
  };
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

function consultationStatus(value) {
  const normalized = String(value || "").trim().toLowerCase();
  return CONSULTATION_STATUSES.has(normalized) ? normalized : "new";
}

function consultationPublic(row) {
  if (!row) return null;
  return {
    id: row.id,
    source: row.source || "public_site",
    topic: row.topic || "",
    name: row.name || "",
    email_masked: row.email_masked || "",
    phone_masked: row.phone_masked || "",
    product_interest: row.product_interest || "",
    message: row.message || "",
    status: row.status || "new",
    admin_note: row.admin_note || "",
    page_url: row.page_url || "",
    referrer: row.referrer || "",
    created_at: row.created_at,
    updated_at: row.updated_at,
  };
}

function consultationKind(row) {
  return row?.source === "home_newsletter" ? "newsletter" : "consultation";
}

function consultationKeyboard(env) {
  return {
    inline_keyboard: [[{ text: "상담 관리 열기", url: adminUrl(env) }]],
  };
}

function consultationMessage(row, contact) {
  const isNewsletter = consultationKind(row) === "newsletter";
  return [
    isNewsletter ? "<b>ARSEN 신규 소식받기 신청</b>" : "<b>ARSEN 신규 상담 신청</b>",
    `접수ID: <code>${htmlEscape(row.id || "-")}</code>`,
    row.member_id ? `신청자ID: <code>${htmlEscape(row.member_id)}</code>` : "",
    `출처: ${htmlEscape(row.source || "-")}`,
    `${isNewsletter ? "분류" : "상담 주제"}: ${htmlEscape(row.topic || "-")}`,
    `관심 상품: ${htmlEscape(row.product_interest || "-")}`,
    `이름: ${htmlEscape(row.name || "-")}`,
    `전화: ${htmlEscape(contact.phone || row.phone_masked || "-")}`,
    `이메일: ${htmlEscape(contact.email || row.email_masked || "-")}`,
    `내용: ${displayValue(row.message || "-", 500)}`,
    row.page_url ? `페이지: ${htmlEscape(row.page_url)}` : "",
    row.referrer ? `유입: ${htmlEscape(row.referrer)}` : "",
    `접수시각: ${htmlEscape(row.created_at || "-")}`,
  ].filter(Boolean).join("\n");
}

function consultationKindWhere(kind) {
  const normalized = String(kind || "").trim().toLowerCase();
  if (["newsletter", "news", "lead", "leads"].includes(normalized)) return "source='home_newsletter'";
  if (["consultation", "consult", "inquiry"].includes(normalized)) return "source!='home_newsletter'";
  return "";
}

async function consultationSummary(env, kind = "") {
  const kindWhere = consultationKindWhere(kind);
  const rows = await all(
    env,
    `SELECT status, COUNT(*) AS count FROM consultations ${kindWhere ? `WHERE ${kindWhere}` : ""} GROUP BY status`
  );
  const counts = Object.fromEntries(rows.map((row) => [row.status, Number(row.count || 0)]));
  return {
    total: Object.values(counts).reduce((sum, value) => sum + value, 0),
    new: counts.new || 0,
    contacted: counts.contacted || 0,
    on_hold: counts.on_hold || 0,
    closed: counts.closed || 0,
    spam: counts.spam || 0,
  };
}

async function listConsultations(env, params = {}) {
  const where = [];
  const values = [];
  const status = String(params.status || "").trim();
  if (status === "active") {
    where.push("status NOT IN ('closed', 'spam')");
  } else if (status) {
    where.push("status=?");
    values.push(consultationStatus(status));
  }
  const source = String(params.source || "").trim();
  if (source) {
    where.push("source=?");
    values.push(source.slice(0, 80));
  }
  const kindWhere = consultationKindWhere(params.kind || "");
  if (kindWhere) where.push(kindWhere);
  const clause = where.length ? `WHERE ${where.join(" AND ")}` : "";
  const rows = await all(env, `SELECT * FROM consultations ${clause} ORDER BY created_at DESC LIMIT 300`, ...values);
  return rows.map(consultationPublic);
}

async function getConsultationRow(env, consultationId) {
  return one(env, "SELECT * FROM consultations WHERE id=?", consultationId);
}

async function createConsultation(env, body, request) {
  const source = String(body.source || "public_site").trim().slice(0, 80) || "public_site";
  const rawContact = String(body.contact || body.lead_contact || "").trim();
  const contactLooksEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(rawContact);
  const contactDigits = normalizePhone(rawContact);
  const rawEmail = body.email || body.buyer_email || (contactLooksEmail ? rawContact : "");
  const rawPhone = String(body.phone || body.buyer_phone || (!contactLooksEmail && contactDigits.length >= 7 ? rawContact : "")).trim();
  const phoneForStorage = normalizePhoneForStorage(rawPhone);
  const phoneDigits = normalizePhone(phoneForStorage);
  const email = normalizeEmail(rawEmail || "");
  const isNewsletter = source === "home_newsletter";
  const contactKind = isNewsletter
    ? "phone"
    : String(body.contact_type || "").trim().toLowerCase() || (email ? "email" : phoneDigits ? "phone" : "");
  const newsletterLabel = contactKind === "phone" ? "번호" : "이메일";
  const topicBase = String(body.topic || body.consult_type || body.subject || body.product_interest || "상담").trim().slice(0, 120) || "상담";
  const topic = isNewsletter && !topicBase.includes("·") ? `${topicBase} · ${newsletterLabel}` : topicBase;
  const name = String(body.name || body.buyer_name || "").trim().slice(0, 80);
  const productInterest = String(body.product_interest || body.product || (isNewsletter ? `메인 소식 받기 · ${newsletterLabel}` : "")).trim().slice(0, 120) || null;
  const message = String(body.message || body.customer_message || body.memo || "").trim().slice(0, 2000) || null;
  if (isNewsletter && !name) return { response: fail(400, "소식받기 신청은 이름을 입력해야 합니다.") };
  if (isNewsletter && !phoneDigits) return { response: fail(400, "소식받기 신청은 전화번호를 입력해야 합니다.") };
  if (!phoneDigits && !email) return { response: fail(400, "연락 가능한 전화번호 또는 이메일이 필요합니다.") };
  if (body.consent_privacy === false || body.consent_privacy === "false" || body.consent_privacy === "0") {
    return { response: fail(400, "상담 연락을 위한 개인정보 수집 동의가 필요합니다.") };
  }

  const id = crypto.randomUUID();
  const created = now();
  const row = {
    id,
    source,
    topic,
    name: name || "상담 신청자",
    email_hash: email ? await hmacHex(`consultation-email:${email}`, env, "EMAIL_SECRET_KEY") : null,
    email_masked: maskEmail(email),
    email_encrypted: email ? await encryptLegacyValue(email, env, "EMAIL_SECRET_KEY") : "",
    phone_hash: phoneDigits ? await hmacHex(`consultation-phone:${phoneDigits}`, env, "PHONE_SECRET_KEY") : null,
    phone_masked: maskPhone(phoneForStorage),
    phone_encrypted: phoneDigits ? await encryptLegacyValue(phoneForStorage, env, "PHONE_SECRET_KEY") : "",
    product_interest: productInterest,
    message,
    status: "new",
    admin_note: null,
    page_url: String(body.page_url || "").trim().slice(0, 500) || null,
    referrer: String(body.referrer || "").trim().slice(0, 500) || null,
    user_agent: String(request.headers.get("user-agent") || "").slice(0, 500) || null,
    created_at: created,
    updated_at: created,
  };

  await env.DB.prepare(
    `INSERT INTO consultations (
      id, source, topic, name, email_hash, email_masked, email_encrypted,
      phone_hash, phone_masked, phone_encrypted, product_interest, message,
      status, admin_note, page_url, referrer, user_agent, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      row.id,
      row.source,
      row.topic,
      row.name,
      row.email_hash,
      row.email_masked,
      row.email_encrypted,
      row.phone_hash,
      row.phone_masked,
      row.phone_encrypted,
      row.product_interest,
      row.message,
      row.status,
      row.admin_note,
      row.page_url,
      row.referrer,
      row.user_agent,
      row.created_at,
      row.updated_at
    )
    .run();
  const memberPlanType = isNewsletter
    ? contactKind === "phone" ? "lead_phone" : "lead_email"
    : "consultation";
  const memberKindLabel = isNewsletter ? `소식 받기 · ${newsletterLabel}` : "상담";
  const memberId = await createEdgeMember(env, {
    name: name || "상담 신청자",
    phone: phoneForStorage,
    email,
    job: isNewsletter ? "소식 받기 신청" : "상담 신청",
    referral_source: source,
    reason: [
      `분류: ${memberKindLabel}`,
      topic,
      productInterest,
      message,
    ].filter(Boolean).join("\n"),
    ai_level: memberKindLabel,
    plan_type: memberPlanType,
    group_goals: productInterest || memberKindLabel,
    short_term_goal: message || topic,
    participation_type: memberKindLabel,
    preferred_schedule: "",
    available_time_slots: "",
    region: "",
    main_device: "",
    skills: "",
    contribution: message || productInterest || memberKindLabel,
    participation_grade: memberKindLabel,
    consent_marketing: false,
    consent_version: isNewsletter ? "public-newsletter-v1" : "public-consultation-v1",
    status: "pending",
  }, env);
  row.member_id = memberId;
  const hermesStatus = await sendTelegram(env, consultationMessage(row, { phone: phoneForStorage, email }), consultationKeyboard(env), "application");
  if (memberId) await logAction(env, memberId, "consultation_mirror", JSON.stringify({ consultation_id: id, source, topic }), request);
  await logAction(env, "system", "consultation_created", JSON.stringify({ id, member_id: memberId, source, topic, hermes_status: hermesStatus }), request);
  return {
    ok: true,
    message: isNewsletter ? "소식받기 신청이 접수되었습니다. 새 소식이 준비되면 안내드리겠습니다." : "상담 신청이 접수되었습니다. 운영자가 확인 후 연락드립니다.",
    data: { ...consultationPublic(row), member_id: memberId },
    member_id: memberId,
    notification: { telegram: hermesStatus },
  };
}

async function updateConsultationStatus(env, consultationId, body) {
  const status = consultationStatus(body.status);
  const note = String(body.admin_note || body.note || "").trim().slice(0, 1000) || null;
  const existing = await getConsultationRow(env, consultationId);
  if (!existing) return { ok: false, status: 404, message: "상담 접수를 찾을 수 없습니다." };
  const timestamp = now();
  await env.DB.prepare(
    "UPDATE consultations SET status=?, admin_note=COALESCE(?, admin_note), updated_at=? WHERE id=?"
  )
    .bind(status, note, timestamp, consultationId)
    .run();
  return { ok: true, data: consultationPublic(await getConsultationRow(env, consultationId)) };
}

async function consultationContact(env, consultationId) {
  const row = await getConsultationRow(env, consultationId);
  if (!row) return null;
  return {
    id: row.id,
    name: row.name || "상담 신청자",
    phone: await decryptValue(row.phone_encrypted, env, "PHONE_SECRET_KEY"),
    email: await decryptValue(row.email_encrypted, env, "EMAIL_SECRET_KEY"),
    phone_masked: row.phone_masked || "",
    email_masked: row.email_masked || "",
  };
}

function yoonbotPlan(planCode) {
  const normalized = String(planCode || "").trim().toLowerCase();
  return YOONBOT_PLANS.find((plan) => plan.code === normalized) || null;
}

function yoonbotProducts(env) {
  const provider = String((env && env.YOONBOT_PAYMENT_PROVIDER) || "");
  const clientKey = String((env && env.TOSS_PAYMENTS_CLIENT_KEY) || "");
  const secretKey = String((env && env.TOSS_PAYMENTS_SECRET_KEY) || "");
  const tossReady = provider === "toss_payments" && !!clientKey && !!secretKey;
  return {
    product: {
      code: YOONBOT_PRODUCT_CODE,
      name: "YOONBOT",
      payment_mode: tossReady ? "toss_payments" : "manual_bank_transfer",
      auto_charge: tossReady,
    },
    plans: YOONBOT_PLANS,
  };
}

function orderPaymentRef(orderId) {
  return `YB-${String(orderId || "").replace(/-/g, "").slice(0, 8).toUpperCase()}`;
}

function orderPublic(row) {
  if (!row) return null;
  const finalAmount = Number(row.amount_krw || 0);
  const originalAmount = row.original_amount_krw != null ? Number(row.original_amount_krw) : finalAmount;
  return {
    id: row.id,
    buyer_name: row.buyer_name,
    buyer_email_masked: row.buyer_email_masked || "",
    buyer_phone_masked: row.buyer_phone_masked || "",
    product_code: row.product_code || YOONBOT_PRODUCT_CODE,
    plan_code: row.plan_code,
    amount_krw: finalAmount,
    original_amount_krw: originalAmount,
    discount_code: row.discount_code || null,
    discount_label: row.discount_label || null,
    discount_amount_krw: Number(row.discount_amount_krw || 0),
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
    message: "관리자가 구매 내용을 확인한 뒤 입금 안내와 라이선스 발급을 수동으로 진행합니다.",
  };
}

function buildTossPaymentPayload(env, order, orderId) {
  const provider = String(env.YOONBOT_PAYMENT_PROVIDER || "");
  const clientKey = String(env.TOSS_PAYMENTS_CLIENT_KEY || "");
  const secretKey = String(env.TOSS_PAYMENTS_SECRET_KEY || "");
  if (provider !== "toss_payments" || !clientKey || !secretKey) {
    if (provider === "toss_payments") {
      return {
        ...manualPaymentPayload(orderId),
        message: "온라인 결제 설정 확인 중이라 수동 결제 안내로 진행합니다.",
      };
    }
    return manualPaymentPayload(orderId);
  }
  const baseUrl = String(env.YOONBOT_PUBLIC_BASE_URL || "https://apply.arsen-ai.com").replace(/\/$/, "");
  const tossOrderId = generateTossOrderId(orderId);
  const planCode = String(order.plan_code || "monthly");
  return {
    mode: "toss_payments",
    auto_charge: true,
    client_key: clientKey,
    toss_order_id: tossOrderId,
    order_name: `YOONBOT ${planCode.charAt(0).toUpperCase() + planCode.slice(1)} 라이선스`,
    amount: { value: Number(order.amount_krw || 0), currency: "KRW" },
    success_url: `${baseUrl}/frontend/yoonbot.html?payment=success`,
    fail_url: `${baseUrl}/frontend/yoonbot.html?payment=fail`,
    customer_name: order.buyer_name || "",
    customer_email: "",
  };
}

function generateTossOrderId(orderId) {
  const sanitized = String(orderId || "").replace(/[^A-Za-z0-9]/g, "").slice(0, 30);
  return `yb-${sanitized}`;
}

async function confirmTossPaymentWithToss(env, paymentKey, tossOrderId, amount) {
  const secretKey = String(env.TOSS_PAYMENTS_SECRET_KEY || "");
  if (!secretKey) throw new Error("TOSS_PAYMENTS_SECRET_KEY is not configured");
  const credentials = btoa(`${secretKey}:`);
  const response = await fetch("https://api.tosspayments.com/v1/payments/confirm", {
    method: "POST",
    headers: {
      Authorization: `Basic ${credentials}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ paymentKey, orderId: tossOrderId, amount }),
  });
  if (!response.ok) {
    const body = await response.text();
    throw new Error(`Toss confirm HTTP ${response.status}: ${body}`);
  }
  return response.json();
}

async function getYoonbotOrderByTossId(env, tossOrderId) {
  const row = await one(
    env,
    `SELECT o.*, l.license_key_hint, l.status AS license_status
     FROM orders o
     LEFT JOIN licenses l ON l.id=o.license_id
     WHERE o.toss_order_id=?`,
    tossOrderId
  );
  return orderPublic(row);
}

async function confirmTossPayment(env, internalOrderId, body, tossConfirmFn) {
  const order = await getYoonbotOrder(env, internalOrderId);
  if (!order) return { ok: false, message: "주문을 찾을 수 없습니다.", status: 404 };
  if ((order.product_code || YOONBOT_PRODUCT_CODE) !== YOONBOT_PRODUCT_CODE) {
    return { ok: false, message: "YOONBOT 주문이 아닙니다.", status: 400 };
  }
  if (YOONBOT_ORDER_TERMINAL_STATUSES.has(order.status)) {
    return { ok: false, message: "취소/환불된 주문은 결제 확인할 수 없습니다.", status: 400 };
  }
  if (order.status === "paid" || order.status === "license_issued") {
    if (order.payment_ref && body.payment_key && order.payment_ref === body.payment_key) {
      return { ok: true, data: order, idempotent: true };
    }
    return { ok: false, message: "이미 결제 처리된 주문입니다.", status: 400 };
  }
  const expectedTossOrderId = generateTossOrderId(internalOrderId);
  if (body.order_id !== expectedTossOrderId) {
    return { ok: false, message: "orderId가 서버 값과 일치하지 않습니다.", status: 400 };
  }
  const serverAmount = Number(order.amount_krw || 0);
  if (Number(body.amount) !== serverAmount) {
    return { ok: false, message: "결제 금액이 주문 금액과 일치하지 않습니다.", status: 400 };
  }
  if (!String(env.TOSS_PAYMENTS_SECRET_KEY || "")) {
    return { ok: false, message: "TOSS_PAYMENTS_SECRET_KEY가 설정되지 않았습니다.", status: 503 };
  }
  let tossResponse;
  try {
    const confirmFn = tossConfirmFn || confirmTossPaymentWithToss;
    tossResponse = await confirmFn(env, body.payment_key, body.order_id, serverAmount);
  } catch (err) {
    return { ok: false, message: String(err.message || "Toss 결제 확인에 실패했습니다."), status: 502 };
  }
  const tossStatus = String((tossResponse || {}).status || "");
  if (tossStatus && tossStatus !== "DONE") {
    return { ok: false, message: `Toss 결제 상태가 완료가 아닙니다: ${tossStatus}`, status: 400 };
  }
  const tossTotal = (tossResponse || {}).totalAmount;
  if (tossTotal != null && Number(tossTotal) !== serverAmount) {
    return { ok: false, message: "Toss 응답 금액이 주문 금액과 일치하지 않습니다.", status: 400 };
  }
  return markYoonbotOrderPaid(env, internalOrderId, {
    payment_provider: "toss_payments",
    payment_ref: body.payment_key,
    note: `toss_confirm:${body.order_id}`,
  });
}

async function confirmTossPaymentByTossId(env, tossOrderId, body, tossConfirmFn) {
  const order = await getYoonbotOrderByTossId(env, tossOrderId);
  if (!order) return { ok: false, message: "주문을 찾을 수 없습니다.", status: 404 };
  return confirmTossPayment(env, order.id, body, tossConfirmFn);
}

function educationPaymentRef(orderId) {
  return `ARSEN-${String(orderId || "").replace(/-/g, "").slice(0, 8).toUpperCase()}`;
}

function educationTossOrderId(orderId) {
  return `ae-${String(orderId || "").replace(/[^A-Za-z0-9]/g, "").slice(0, 30)}`;
}

function educationOrderPublic(row) {
  if (!row) return null;
  return {
    id: row.id,
    booking_id: row.booking_id,
    amount_krw: Number(row.amount_krw || 0),
    status: row.status || "payment_pending",
    payment_provider: row.payment_provider || "manual_bank_transfer",
    payment_reference: educationPaymentRef(row.id),
    toss_order_id: row.toss_order_id || educationTossOrderId(row.id),
    created_at: row.created_at || "",
    paid_at: row.paid_at || null,
  };
}

async function getEducationOrderRow(env, orderId) {
  return one(env, "SELECT * FROM education_payment_orders WHERE id=?", orderId);
}

async function createOrReuseEducationOrder(env, bookingId, memberId) {
  const booking = await one(
    env,
    `SELECT b.*, s.title AS session_title, s.price_krw AS session_price_krw
     FROM bookings b
     LEFT JOIN sessions s ON s.id=b.session_id
     WHERE b.id=? AND b.member_id=?`,
    bookingId,
    memberId
  );
  if (!booking) return { ok: false, status: 404, message: "본인 예약을 찾을 수 없습니다." };
  if (![...PENDING_BOOKING_STATUSES, "confirmed"].includes(booking.status)) {
    return { ok: false, status: 400, message: "취소되었거나 처리할 수 없는 예약입니다." };
  }
  if (booking.payment_status === "paid") {
    return { ok: false, status: 400, message: "이미 결제 확인된 예약입니다." };
  }
  const amount = Number(booking.payment_amount_krw || booking.session_price_krw || 0);
  if (amount <= 0 || booking.payment_status === "waived") {
    return { ok: false, status: 400, message: "이 예약은 온라인 결제 대상이 아닙니다." };
  }

  const existing = await one(
    env,
    "SELECT * FROM education_payment_orders WHERE booking_id=? ORDER BY created_at DESC LIMIT 1",
    bookingId
  );
  if (existing) {
    if (existing.status === "paid") return { ok: true, data: educationOrderPublic(existing), already_paid: true };
    if (!["canceled", "refunded"].includes(existing.status)) {
      return { ok: true, data: educationOrderPublic(existing), reused: true };
    }
    return { ok: false, status: 400, message: "취소 또는 환불된 결제 주문은 운영자 확인 후 다시 진행할 수 있습니다." };
  }

  const orderId = crypto.randomUUID();
  const timestamp = now();
  await env.DB.batch([
    env.DB.prepare(
      `INSERT OR IGNORE INTO education_payment_orders (
        id, booking_id, member_id, amount_krw, status, payment_provider,
        toss_order_id, created_at, updated_at
      ) VALUES (?, ?, ?, ?, 'payment_pending', 'manual_bank_transfer', ?, ?, ?)`
    ).bind(orderId, bookingId, memberId, amount, educationTossOrderId(orderId), timestamp, timestamp),
    env.DB.prepare(
      `UPDATE bookings
       SET status=CASE WHEN status='requested' THEN 'payment_pending' ELSE status END,
           payment_status=CASE WHEN payment_status IN ('not_sent','pending') THEN 'pending' ELSE payment_status END,
           updated_at=?
       WHERE id=?`
    ).bind(timestamp, bookingId),
  ]);
  const created = await one(env, "SELECT * FROM education_payment_orders WHERE booking_id=?", bookingId);
  return { ok: true, data: educationOrderPublic(created), reused: created?.id !== orderId };
}

async function educationPaymentPayload(env, order, orderName) {
  const provider = String(env.YOONBOT_PAYMENT_PROVIDER || "");
  const clientKey = String(env.TOSS_PAYMENTS_CLIENT_KEY || "");
  const secretKey = String(env.TOSS_PAYMENTS_SECRET_KEY || "");
  if (provider !== "toss_payments" || !clientKey || !secretKey) {
    const account = await selectedPaymentAccount(env);
    const payload = {
      mode: "manual_bank_transfer",
      auto_charge: false,
      payment_reference: order.payment_reference,
      amount_krw: order.amount_krw,
      message: "온라인 결제 설정 확인 중입니다. 아래 입금 안내 또는 운영자 안내에 따라 진행하세요.",
    };
    if (account) {
      payload.manual_account = {
        label: account.label || "입금 계좌",
        bank: account.bank || "",
        number: account.number || "",
        holder: account.holder || "",
      };
    }
    return payload;
  }
  const baseUrl = publicBaseUrl(env).replace(/\/$/, "");
  return {
    mode: "toss_payments",
    auto_charge: true,
    client_key: clientKey,
    toss_order_id: order.toss_order_id,
    order_name: String(orderName || "ARSEN 유료 강의").slice(0, 100),
    amount: { value: Number(order.amount_krw || 0), currency: "KRW" },
    success_url: `${baseUrl}/frontend/status.html?payment=success&education_order_id=${encodeURIComponent(order.id)}`,
    fail_url: `${baseUrl}/frontend/status.html?payment=fail&education_order_id=${encodeURIComponent(order.id)}`,
  };
}

async function educationPaymentKeyFingerprint(env, paymentKey) {
  if (!String(env.CODE_SECRET_KEY || "")) throw new Error("CODE_SECRET_KEY is not configured");
  const digest = await hmacHex(`education-payment:${paymentKey}`, env, "CODE_SECRET_KEY");
  return `toss:${digest.slice(0, 48)}`;
}

function constantTimeTextEqual(left, right) {
  const a = new TextEncoder().encode(String(left || ""));
  const b = new TextEncoder().encode(String(right || ""));
  let difference = a.length ^ b.length;
  for (let index = 0; index < Math.max(a.length, b.length); index += 1) {
    difference |= (a[index] || 0) ^ (b[index] || 0);
  }
  return difference === 0;
}

async function confirmEducationTossPayment(env, orderId, body, tossConfirmFn) {
  const order = await getEducationOrderRow(env, orderId);
  if (!order) return { ok: false, status: 404, message: "결제 주문을 찾을 수 없습니다." };
  if (["canceled", "refunded"].includes(order.status)) {
    return { ok: false, status: 400, message: "취소 또는 환불된 주문은 결제 확인할 수 없습니다." };
  }
  if (!body.payment_key || !String(env.CODE_SECRET_KEY || "")) {
    return { ok: false, status: 503, message: "온라인 결제 설정이 완료되지 않았습니다." };
  }
  const fingerprint = await educationPaymentKeyFingerprint(env, body.payment_key);
  if (order.status === "paid") {
    if (constantTimeTextEqual(order.payment_ref, fingerprint)) return { ok: true, data: educationOrderPublic(order), idempotent: true };
    return { ok: false, status: 400, message: "이미 결제 처리된 주문입니다." };
  }
  if (body.order_id !== order.toss_order_id) {
    return { ok: false, status: 400, message: "orderId가 서버 값과 일치하지 않습니다." };
  }
  const serverAmount = Number(order.amount_krw || 0);
  if (Number(body.amount) !== serverAmount) {
    return { ok: false, status: 400, message: "결제 금액이 주문 금액과 일치하지 않습니다." };
  }
  if (!String(env.TOSS_PAYMENTS_SECRET_KEY || "")) {
    return { ok: false, status: 503, message: "온라인 결제 설정이 완료되지 않았습니다." };
  }
  let tossResponse;
  try {
    tossResponse = await (tossConfirmFn || confirmTossPaymentWithToss)(env, body.payment_key, body.order_id, serverAmount);
  } catch (err) {
    return { ok: false, status: 502, message: String(err.message || "Toss 결제 확인에 실패했습니다.") };
  }
  const tossStatus = String((tossResponse || {}).status || "");
  if (tossStatus && tossStatus !== "DONE") {
    return { ok: false, status: 400, message: `Toss 결제 상태가 완료가 아닙니다: ${tossStatus}` };
  }
  if (tossResponse?.totalAmount != null && Number(tossResponse.totalAmount) !== serverAmount) {
    return { ok: false, status: 400, message: "Toss 응답 금액이 주문 금액과 일치하지 않습니다." };
  }

  const timestamp = now();
  await env.DB.batch([
    env.DB.prepare(
      `UPDATE education_payment_orders
       SET status='paid', payment_provider='toss_payments', payment_ref=?, paid_at=?, updated_at=?
       WHERE id=? AND status='payment_pending'`
    ).bind(fingerprint, timestamp, timestamp, orderId),
    env.DB.prepare(
      `UPDATE bookings
       SET status='confirmed', payment_status='paid', payment_note='온라인 결제 확인',
           confirmed_at=COALESCE(confirmed_at, ?), updated_at=?
       WHERE id=? AND EXISTS (
         SELECT 1 FROM education_payment_orders
         WHERE id=? AND status='paid' AND payment_ref=?
       )`
    ).bind(timestamp, timestamp, order.booking_id, orderId, fingerprint),
  ]);
  const refreshed = await getEducationOrderRow(env, orderId);
  if (refreshed?.status === "paid" && constantTimeTextEqual(refreshed.payment_ref, fingerprint)) {
    return { ok: true, data: educationOrderPublic(refreshed) };
  }
  return { ok: false, status: 409, message: "결제 주문 상태가 변경되어 다시 확인이 필요합니다." };
}

const DISCOUNT_CODE_RE = /^[A-Z0-9_\-]{1,64}$/;

function normalizeDiscountCode(code) {
  if (!code) return "";
  return String(code).trim().toUpperCase();
}

async function validateAndApplyDiscount(env, planCode, originalAmount, codeRaw, nowIso) {
  const code = normalizeDiscountCode(codeRaw);
  if (!code) return { finalAmount: originalAmount, discountAmount: 0, code: null, label: null };
  if (!DISCOUNT_CODE_RE.test(code)) {
    return { error: "할인 코드 형식이 올바르지 않습니다." };
  }
  const row = await one(env, "SELECT * FROM yoonbot_discount_codes WHERE code=?", code);
  if (!row) return { error: "유효하지 않은 할인 코드입니다." };
  if (!row.enabled) return { error: "사용 중지된 할인 코드입니다." };
  if (row.starts_at && nowIso < row.starts_at) return { error: "아직 사용 기간이 시작되지 않은 할인 코드입니다." };
  if (row.expires_at && nowIso > row.expires_at) return { error: "만료된 할인 코드입니다." };
  if (row.plan_code && row.plan_code !== planCode) return { error: "이 플랜에는 적용할 수 없는 할인 코드입니다." };
  const maxRed = row.max_redemptions;
  const redeemed = Number(row.redeemed_count || 0);
  if (maxRed != null && maxRed > 0 && redeemed >= maxRed) return { error: "이미 사용 횟수가 소진된 할인 코드입니다." };

  const dtype = String(row.discount_type || "").trim().toLowerCase();
  const dvalue = Number(row.discount_value || 0);
  const label = String(row.label || code).trim().slice(0, 120);
  let discountAmount = 0;
  if (dtype === "percent") {
    const pct = Math.max(1, Math.min(100, dvalue));
    discountAmount = Math.floor(originalAmount * pct / 100);
  } else if (dtype === "amount") {
    discountAmount = Math.min(dvalue, originalAmount);
  } else if (dtype === "override_amount") {
    discountAmount = Math.max(0, originalAmount - dvalue);
  } else {
    return { error: "지원하지 않는 할인 유형입니다." };
  }
  const finalAmount = Math.max(0, originalAmount - discountAmount);
  const updateResult = await env.DB.prepare(
    `UPDATE yoonbot_discount_codes
     SET redeemed_count=redeemed_count+1, updated_at=?
     WHERE code=?
       AND enabled=1
       AND (max_redemptions IS NULL OR max_redemptions <= 0 OR redeemed_count < max_redemptions)`
  ).bind(nowIso, code).run();
  const changed = Number(updateResult?.meta?.changes ?? updateResult?.changes ?? 0);
  if (changed !== 1) return { error: "이미 사용 횟수가 소진된 할인 코드입니다." };
  return { finalAmount, discountAmount, code, label };
}

async function createYoonbotOrder(env, body) {
  const productCode = String(body.product_code || YOONBOT_PRODUCT_CODE).trim().toLowerCase();
  if (productCode !== YOONBOT_PRODUCT_CODE) return { response: fail(400, "지원하지 않는 상품입니다.") };
  const plan = yoonbotPlan(body.plan_code || "monthly");
  if (!plan) return { response: fail(400, "지원하지 않는 YOONBOT 플랜입니다.") };
  const buyerName = String(body.buyer_name || "").trim().slice(0, 80);
  if (!buyerName) return { response: fail(400, "구매자 이름을 입력하세요.") };
  const email = normalizeEmail(body.buyer_email);
  const phone = normalizePhone(body.buyer_phone);
  if (!email && !phone) return { response: fail(400, "연락 가능한 이메일 또는 전화번호가 필요합니다.") };
  if (!body.consent_privacy || !body.consent_terms) {
    return { response: fail(400, "개인정보 수집과 결제 안내에 동의해야 합니다.") };
  }

  const orderId = crypto.randomUUID();
  const tossOrderId = generateTossOrderId(orderId);
  const created = licenseIso();
  const originalAmount = plan.amount_krw;

  const discountResult = await validateAndApplyDiscount(
    env, plan.code, originalAmount, body.discount_code || null, created
  );
  if (discountResult.error) return { response: fail(400, discountResult.error) };

  const { finalAmount, discountAmount, code: dCode, label: dLabel } = discountResult;

  await env.DB.prepare(
    `INSERT INTO orders (
      id, buyer_name, buyer_email_hash, buyer_email_masked,
      buyer_phone_hash, buyer_phone_masked, product_code, plan_code,
      amount_krw, original_amount_krw, discount_code, discount_label,
      discount_amount_krw, status, payment_provider, payment_ref,
      toss_order_id, customer_message, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'payment_pending', 'manual_bank_transfer', ?, ?, ?, ?, ?)`
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
      finalAmount,
      originalAmount,
      dCode,
      dLabel,
      discountAmount,
      orderPaymentRef(orderId),
      tossOrderId,
      String(body.customer_message || "").trim().slice(0, 1000) || null,
      created,
      created
    )
    .run();
  const order = await getYoonbotOrder(env, orderId);
  const paymentPayload = buildTossPaymentPayload(env, order, orderId);
  return { ok: true, data: order, payment: paymentPayload };
}

function discountRowPublic(row) {
  if (!row) return null;
  return {
    id: row.id,
    code: row.code,
    label: row.label || "",
    plan_code: row.plan_code || null,
    discount_type: row.discount_type,
    discount_value: Number(row.discount_value || 0),
    max_redemptions: row.max_redemptions != null ? Number(row.max_redemptions) : null,
    redeemed_count: Number(row.redeemed_count || 0),
    starts_at: row.starts_at || null,
    expires_at: row.expires_at || null,
    enabled: !!row.enabled,
    note: row.note || "",
    created_at: row.created_at,
    updated_at: row.updated_at,
  };
}

const ALLOWED_DISCOUNT_TYPES_WORKER = new Set(["percent", "amount", "override_amount"]);

async function createDiscountCode(env, body) {
  const normalized = normalizeDiscountCode(body.code);
  if (!normalized || !DISCOUNT_CODE_RE.test(normalized)) {
    return { error: "할인 코드는 영문 대소문자, 숫자, 하이픈(-), 언더스코어(_)만 허용됩니다." };
  }
  const dtype = String(body.discount_type || "percent").trim().toLowerCase();
  if (!ALLOWED_DISCOUNT_TYPES_WORKER.has(dtype)) {
    return { error: `지원하지 않는 할인 유형입니다. 허용: ${[...ALLOWED_DISCOUNT_TYPES_WORKER].join(", ")}` };
  }
  const dvalue = Number(body.discount_value);
  if (dtype === "percent" && !(dvalue >= 1 && dvalue <= 100)) {
    return { error: "퍼센트 할인은 1~100 사이여야 합니다." };
  }
  if (dvalue < 0) return { error: "할인 값은 0 이상이어야 합니다." };
  const existing = await one(env, "SELECT id FROM yoonbot_discount_codes WHERE code=?", normalized);
  if (existing) return { error: "이미 존재하는 할인 코드입니다." };
  const created = licenseIso();
  const id = crypto.randomUUID();
  const maxRed = body.max_redemptions != null ? Number(body.max_redemptions) : 1;
  await env.DB.prepare(
    `INSERT INTO yoonbot_discount_codes
     (id, code, label, plan_code, discount_type, discount_value,
      max_redemptions, redeemed_count, starts_at, expires_at, enabled, note, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, ?, 1, ?, ?, ?)`
  ).bind(
    id,
    normalized,
    String(body.label || "").trim().slice(0, 120) || null,
    String(body.plan_code || "").trim().toLowerCase() || null,
    dtype,
    dvalue,
    maxRed,
    String(body.starts_at || "").trim() || null,
    String(body.expires_at || "").trim() || null,
    String(body.note || "").trim().slice(0, 500) || null,
    created,
    created
  ).run();
  const row = await one(env, "SELECT * FROM yoonbot_discount_codes WHERE id=?", id);
  return { data: discountRowPublic(row) };
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
    "[YOONBOT 라이선스 안내]",
    `라이선스 키: ${licenseKey}`,
    `만료일: ${licenseItem.expires_at}`,
    "",
    "▶ Windows 런처 다운로드",
    LAUNCHER_DIRECT_DOWNLOAD_URL,
    `최신 버전 정보: ${LAUNCHER_RELEASE_URL}`,
    "",
    "▶ 설치 방법",
    "1. 다운로드한 zip 파일의 압축을 원하는 폴더에 해제하세요.",
    "2. 'Arsen Content Launcher.exe'를 실행하세요.",
    "3. 라이선스 인증 창에 위 라이선스 키를 입력하세요.",
    "4. 처음 등록한 PC에 기기가 묶입니다. PC 변경이 필요하면 운영자에게 기기 초기화를 요청해주세요.",
    "",
    "▶ 안내",
    "현재 초기 파일럿/베타 단계로 기능이 순차적으로 확장되고 있습니다.",
    "사용 중 문의사항이나 피드백은 카카오톡 채널 또는 운영자에게 직접 연락해 주세요.",
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
  if (!plan) return { ok: false, message: "지원하지 않는 YOONBOT 플랜입니다.", status: 400 };
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
    consultation: "상담",
    lead_email: "소식(이메일)",
    lead_phone: "소식(번호)",
  }[normalized] || planType || "-";
}

const APPLICATION_PLAN_TYPES = new Set(["free", "basic", "full"]);
const LEAD_PLAN_TYPES = new Set(["consultation", "lead_email", "lead_phone"]);

function leadSourceLabel(planType) {
  const normalized = String(planType || "").toLowerCase();
  if (normalized.startsWith("lead_")) return "소식받기";
  if (normalized === "consultation") return "상담";
  return planTypeLabel(normalized);
}

function canUpgradeLeadToApplication(existing, attempted) {
  const existingPlan = String(existing?.plan_type || "").toLowerCase();
  const attemptedPlan = String(attempted?.plan_type || "").toLowerCase();
  return LEAD_PLAN_TYPES.has(existingPlan) && APPLICATION_PLAN_TYPES.has(attemptedPlan);
}

function canRefreshDuplicateApplication(existing, attempted) {
  const existingPlan = String(existing?.plan_type || "").toLowerCase();
  const attemptedPlan = String(attempted?.plan_type || "").toLowerCase();
  return APPLICATION_PLAN_TYPES.has(existingPlan) && APPLICATION_PLAN_TYPES.has(attemptedPlan);
}

function contactPlanLabel(planType) {
  const normalized = String(planType || "").toLowerCase();
  return {
    free: "무료",
    full: "유료",
    basic: "기본",
    consultation: "상담",
    lead_email: "소식 이메일",
    lead_phone: "소식 번호",
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

function kakaoNoticeKeyboard(env, jobId) {
  if (!jobId) return null;
  return {
    inline_keyboard: [
      [
        { text: "카톡 발송 승인", callback_data: `arsen:noticeok:${jobId}` },
        { text: "취소", callback_data: `arsen:noticeno:${jobId}` },
      ],
      [
        { text: "긴급정지", callback_data: `arsen:noticestop:${jobId}` },
        { text: "관리자 열기", url: adminUrl(env) },
      ],
    ],
  };
}

function kakaoNoticeReadyCount(job) {
  return (job.recipients || []).filter((item) => item.status === "ready" || item.status === "sent").length;
}

function kakaoNoticeSentCount(job) {
  return (job.recipients || []).filter((item) => item.status === "sent").length;
}

const KAKAO_NOTICE_FAILURE_STATUSES = ["failed", "blocked", "prepare_failed", "skipped"];

function kakaoNoticeFailureCount(job) {
  return (job.recipients || []).filter((item) => KAKAO_NOTICE_FAILURE_STATUSES.includes(item.status)).length;
}

function kakaoNoticePendingRetryRecipients(job, includeSent = false) {
  return (job.recipients || []).filter((item) => includeSent || item.status !== "sent");
}

function kakaoNoticeReasonLabel(recipient) {
  const reason = String(recipient?.error || recipient?.status || "").trim();
  const labels = {
    blocked: "차단됨",
    failed: "실패",
    prepare_failed: "준비 실패",
    pending: "미처리",
    ready: "준비됨/미발송",
    skipped: "제외됨",
    stopped: "중단됨",
    not_prepared: "준비 안 됨",
    stop_requested: "중단 요청",
    chat_window_not_opened: "채팅창 열기 실패",
    osascript_timeout: "카카오톡 자동화 응답 없음",
    target_not_found: "검색 대상 없음",
    friend_found_no_chat: "친구 확인/채팅창 열기 실패",
    kakao_paste_failed: "붙여넣기 실패",
    kakao_send_failed: "전송 확인 실패",
  };
  return labels[reason] || reason || "-";
}

function latestRetryableKakaoNoticeJob(state, jobId = "") {
  const jobs = (state.jobs || []).filter((job) => job.target !== "local_group_admin");
  if (jobId) return jobs.find((job) => job.id === jobId) || null;
  return jobs[0] || null;
}

function kakaoNoticeFailureListText(job, recipients) {
  const total = Number(job.recipients?.length || 0);
  const sent = kakaoNoticeSentCount(job);
  const failed = Number(recipients.length || 0);
  const lines = recipients.slice(0, 45).map((recipient, index) => {
    const name = recipient.name || "-";
    const searchName = recipient.kakao_display_name || name;
    return `${index + 1}. ${htmlEscape(name)} → <code>${htmlEscape(searchName)}</code> / ${htmlEscape(kakaoNoticeReasonLabel(recipient))}`;
  });
  if (!lines.length) lines.push("미발송/실패 대상이 없습니다.");
  if (recipients.length > 45) lines.push(`... 외 ${recipients.length - 45}명`);
  return [
    "<b>ARSEN 카톡 미발송/실패 목록</b>",
    `작업ID: <code>${htmlEscape(job.id)}</code>`,
    `상태: ${htmlEscape(job.status || "-")}`,
    `전체: ${total}명 / 성공 기록: ${sent}명 / 미발송·실패: ${failed}명`,
    "",
    ...lines,
    "",
    `재시도: <code>카톡공지 재시도 ${htmlEscape(job.id)}</code>`,
  ].filter(Boolean).join("\n");
}

function kakaoNoticeStopKeyboard(jobId = "") {
  return {
    inline_keyboard: [[{ text: "긴급정지", callback_data: `arsen:noticestop:${jobId || "active"}` }]],
  };
}

function kakaoNoticeSearchName(memberName) {
  return `아르센_${String(memberName || "신청자").replace(/\s+/g, "")}`;
}

function kakaoNoticeJobId() {
  const suffix = crypto.getRandomValues(new Uint8Array(3));
  return `kn_${Date.now().toString(36)}_${[...suffix].map((byte) => byte.toString(16).padStart(2, "0")).join("")}`;
}

function safeJobForTelegram(job) {
  const ready = kakaoNoticeReadyCount(job);
  const total = Number(job.recipients?.length || 0);
  const first = (job.recipients || []).find((item) => item.status === "ready") || job.recipients?.[0] || null;
  return [
    "<b>ARSEN 카톡 대상 준비 결과</b>",
    `작업ID: <code>${htmlEscape(job.id)}</code>`,
    `대상: ${htmlEscape(job.target_label || "-")}`,
    `상태: ${htmlEscape(job.status || "-")}`,
    `준비 완료: ${ready}명`,
    `준비 실패/제외: ${Math.max(0, total - ready)}명`,
    ...(ready > 0
      ? [
          first ? `첫 대상: ${htmlEscape(first.name)} → <code>${htmlEscape(first.kakao_display_name)}</code>` : "",
          ...kakaoNoticeSampleLines(job),
          "승인 버튼을 누르면 위 문구 그대로(개인 코드만 대상별 실제 값) 준비 완료 대상에게 전송합니다. 중간에 멈추려면 /arsen_stop 또는 긴급정지를 누르세요.",
        ]
      : ["발송 가능한 대상이 없어 발송 승인을 막았습니다."]),
  ].filter(Boolean).join("\n");
}

function safePrepareJobForTelegram(job) {
  const first = job.recipients?.[0] || null;
  const total = Number(job.recipients?.length || 0);
  const targetCount = job.target === "local_group" && total === 0 ? "맥에어에서 로컬 그룹 로딩" : `${total}명`;
  return [
    "<b>ARSEN 카톡 대상 준비 작업 생성</b>",
    `작업ID: <code>${htmlEscape(job.id)}</code>`,
    `대상: ${htmlEscape(job.target_label || "-")}`,
    `검사 후보: ${targetCount}`,
    `제외: ${Number(job.skipped?.length || 0)}명`,
    first ? `첫 대상: ${htmlEscape(first.name)} → <code>${htmlEscape(first.kakao_display_name)}</code>` : "",
    ...kakaoNoticeSampleLines(job),
    "먼저 맥에어가 카카오톡 대상 채팅방을 열 수 있는지 검사합니다. 준비 완료 후 발송 승인 버튼을 다시 보내드립니다.",
  ].filter(Boolean).join("\n");
}

function maskKakaoNoticeMessage(message) {
  return String(message || "")
    .replace(/(코드|신청 확인 코드)\s*:\s*[A-Z0-9-]+/gi, "$1: ******")
    .slice(0, 900);
}

const KAKAO_NOTICE_PLACEHOLDER_TOKENS = ["[[호칭]]", "[[이름]]"];
const KAKAO_NOTICE_CUSTOM_MESSAGE_MAX = 2000;

function kakaoPolishTokenCount(text, token) {
  return String(text || "").split(token).length - 1;
}

function kakaoPolishPlaceholdersPreserved(original, polished) {
  return KAKAO_NOTICE_PLACEHOLDER_TOKENS.every(
    (token) => kakaoPolishTokenCount(original, token) === kakaoPolishTokenCount(polished, token)
  );
}

function kakaoPolishProvider(env) {
  const preferred = String(env.KAKAO_POLISH_PROVIDER || "").trim().toLowerCase();
  const candidates = [
    { name: "anthropic", key: String(env.ANTHROPIC_API_KEY || "").trim() },
    { name: "gemini", key: String(env.GEMINI_API_KEY || "").trim() },
  ].filter((item) => item.key);
  if (!candidates.length) return null;
  return candidates.find((item) => item.name === preferred) || candidates[0];
}

function kakaoPolishInstructions(context) {
  const kind = context?.kind === "local_group" ? "local_group" : "member_notice";
  return [
    "당신은 카카오톡 공지 문구 교정기입니다.",
    "운영자가 쓴 원문을 자연스럽고 정중한 한국어 안내 문구로 다듬으세요.",
    "규칙:",
    "- 날짜/시간/장소/링크/숫자 등 사실 정보를 추가하거나 바꾸지 마세요.",
    "- 원문에 없는 약속이나 내용을 만들지 마세요.",
    "- [[호칭]], [[이름]] 같은 이중 대괄호 자리표시자는 철자 그대로, 같은 횟수로 유지하세요.",
    kind === "member_notice"
      ? "- 이 문구는 확인 코드/일정 안내 아래에 붙는 운영자 멘트입니다. 인사말 중복을 피하고 간결하게 유지하세요."
      : "- 이 문구는 그룹 단체 안내 메시지 전체입니다.",
    "- 다듬어진 문구만 출력하세요. 설명, 머리말, 따옴표, 코드블록을 붙이지 마세요.",
  ].join("\n");
}

function kakaoPolishTimeoutSignal() {
  try {
    return typeof AbortSignal !== "undefined" && AbortSignal.timeout ? AbortSignal.timeout(15000) : undefined;
  } catch {
    return undefined;
  }
}

async function callKakaoPolishModel(env, provider, rawMessage, context) {
  const instructions = kakaoPolishInstructions(context);
  if (provider.name === "anthropic") {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": provider.key,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: String(env.KAKAO_POLISH_MODEL || "claude-opus-4-8"),
        max_tokens: 1024,
        system: instructions,
        messages: [{ role: "user", content: rawMessage }],
      }),
      signal: kakaoPolishTimeoutSignal(),
    });
    if (!response.ok) throw new Error(`anthropic_http_${response.status}`);
    const data = await response.json();
    if (data?.stop_reason === "refusal") throw new Error("anthropic_refusal");
    return (data?.content || [])
      .filter((part) => part?.type === "text")
      .map((part) => String(part.text || ""))
      .join("")
      .trim();
  }
  if (provider.name === "gemini") {
    const model = String(env.KAKAO_POLISH_MODEL || "gemini-2.5-flash");
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
      method: "POST",
      headers: { "content-type": "application/json", "x-goog-api-key": provider.key },
      body: JSON.stringify({
        systemInstruction: { parts: [{ text: instructions }] },
        contents: [{ role: "user", parts: [{ text: rawMessage }] }],
      }),
      signal: kakaoPolishTimeoutSignal(),
    });
    if (!response.ok) throw new Error(`gemini_http_${response.status}`);
    const data = await response.json();
    return (data?.candidates?.[0]?.content?.parts || [])
      .map((part) => String(part?.text || ""))
      .join("")
      .trim();
  }
  throw new Error("unknown_polish_provider");
}

async function polishKakaoNoticeMessage(env, rawMessage, context = {}) {
  const raw = String(rawMessage || "").trim();
  if (!raw) return { text: "", status: "skipped", provider: "" };
  if (String(env.KAKAO_POLISH_ENABLED || "") === "0") return { text: raw, status: "skipped", provider: "" };
  const provider = kakaoPolishProvider(env);
  if (!provider) return { text: raw, status: "unavailable", provider: "" };
  try {
    const polished = (await callKakaoPolishModel(env, provider, raw, context))
      .slice(0, KAKAO_NOTICE_CUSTOM_MESSAGE_MAX)
      .trim();
    if (!polished) return { text: raw, status: "failed", provider: provider.name };
    if (!kakaoPolishPlaceholdersPreserved(raw, polished)) return { text: raw, status: "failed", provider: provider.name };
    return { text: polished, status: "polished", provider: provider.name };
  } catch {
    return { text: raw, status: "failed", provider: provider.name };
  }
}

function kakaoNoticePolishLine(job) {
  const status = String(job.polish_status || "");
  if (!status || status === "skipped") return "";
  if (job.source_job_id) return "문구 다듬기: 원본 작업에서 승인된 문구 유지";
  const provider = String(job.polish_provider || "");
  const labels = {
    polished: `문구 다듬기: AI 적용${provider ? ` (${provider})` : ""}`,
    unavailable: "문구 다듬기: AI 미설정 — 원문 그대로 사용",
    failed: "문구 다듬기: AI 실패 — 원문 그대로 사용",
  };
  return labels[status] || "";
}

function kakaoNoticeSampleLines(job) {
  const first = (job.recipients || []).find((item) => item.status === "ready") || job.recipients?.[0] || null;
  const source = first?.message || (job.target === "local_group" ? job.custom_message : "");
  const sample = maskKakaoNoticeMessage(source || "");
  const lines = [];
  const polishLine = kakaoNoticePolishLine(job);
  if (polishLine) lines.push(polishLine);
  if (sample) {
    lines.push("<b>발송 문구 미리보기(개인 코드는 마스킹)</b>");
    lines.push(htmlEscape(sample));
  }
  return lines;
}

function kakaoNoticeMessage(row, code, env, customMessage = "") {
  const [dateText, timeText] = formatKoreanDateTimeRange(row.session_starts_at, row.session_ends_at);
  const title = row.session_title || DEFAULT_TITLE;
  const location = row.session_location || row.location || DEFAULT_LOCATION;
  const materials = row.session_materials || KAKAO_NOTICE_DEFAULT_MATERIALS;
  const custom = String(customMessage || "").trim();
  const hasSession = Boolean(row.session_id || row.booking_id || row.session_title || row.session_starts_at);
  if (!hasSession && !custom) return codeDeliveryMessage(row, code, env);
  return [
    `[ARSEN AI] ${row.name || "신청자"}님 안내드립니다.`,
    "",
    `신청 확인 코드: ${code}`,
    hasSession ? `과정: ${title}` : "",
    hasSession ? `일정: ${dateText}` : "",
    hasSession ? `시간: ${timeText || "-"}` : "",
    hasSession ? `장소: ${location}` : "",
    hasSession ? `준비물: ${materials}` : "",
    custom ? "" : "",
    custom,
    "",
    `예약자 확인: ${publicBaseUrl(env)}/frontend/status.html`,
    "변경이 필요하면 1:1 문의방으로 알려주세요.",
  ].filter((line) => line !== "").join("\n").trim();
}

async function kakaoNoticeState(env) {
  const saved = await setting(env, KAKAO_NOTICE_STATE_KEY, { jobs: [] });
  return { jobs: Array.isArray(saved.jobs) ? saved.jobs : [] };
}

async function saveKakaoNoticeState(env, state) {
  const jobs = Array.isArray(state.jobs) ? state.jobs : [];
  await saveSetting(env, KAKAO_NOTICE_STATE_KEY, { jobs: jobs.slice(0, KAKAO_NOTICE_JOB_LIMIT), updated_at: now() });
}

function updateKakaoNoticeJob(state, jobId, updater) {
  const jobs = Array.isArray(state.jobs) ? state.jobs : [];
  const index = jobs.findIndex((job) => job.id === jobId);
  if (index < 0) return null;
  const next = { ...jobs[index] };
  updater(next);
  next.updated_at = now();
  jobs[index] = next;
  state.jobs = jobs;
  return next;
}

async function latestNoticeSession(env) {
  const upcoming = await one(
    env,
    "SELECT * FROM sessions WHERE status NOT IN ('draft','canceled','deleted') AND starts_at>=? ORDER BY starts_at ASC LIMIT 1",
    now()
  );
  if (upcoming) return upcoming;
  return one(env, "SELECT * FROM sessions WHERE status NOT IN ('draft','canceled','deleted') ORDER BY starts_at DESC LIMIT 1");
}

async function kakaoNoticeRowsForSession(env, sessionId) {
  return all(
    env,
    `SELECT
       m.*,
       b.id AS booking_id,
       b.session_id,
       b.status AS booking_status,
       s.title AS session_title,
       s.starts_at AS session_starts_at,
       s.ends_at AS session_ends_at,
       s.location AS session_location,
       s.location AS location,
       s.materials AS session_materials
     FROM bookings b
     JOIN members m ON m.id=b.member_id
     LEFT JOIN sessions s ON s.id=b.session_id
     WHERE b.session_id=?
       AND b.status NOT IN ('canceled','rejected','no_show')
       AND m.status='approved'
     ORDER BY b.created_at ASC, m.name ASC`,
    sessionId
  );
}

async function kakaoNoticeRowsForApproved(env) {
  return all(
    env,
    `SELECT
       m.*,
       NULL AS booking_id,
       NULL AS session_id,
       NULL AS booking_status,
       NULL AS session_title,
       NULL AS session_starts_at,
       NULL AS session_ends_at,
       NULL AS session_location,
       NULL AS location,
       NULL AS session_materials
     FROM members m
     WHERE m.status='approved'
     ORDER BY m.approved_at DESC, m.created_at DESC`
  );
}

function trimCommandPrefix(line, patterns) {
  let value = String(line || "").trim();
  for (const pattern of patterns) value = value.replace(pattern, "").trim();
  return value;
}

function splitGroupFriend(rest) {
  const parts = String(rest || "").split(/\s*\/\s*/);
  return {
    groupName: String(parts[0] || "").trim(),
    friendName: String(parts.slice(1).join("/")).trim(),
  };
}

function parseKakaoGroupAdminCommand(clean, firstLine, firstToken) {
  if (firstToken === "/kakao_groups" || /^카톡\s*그룹\s*목록$/.test(firstLine) || /^그룹\s*목록$/.test(firstLine)) {
    return { kind: "group_admin", groupAction: "list" };
  }
  if (firstToken === "/kakao_group_view" || /^카톡\s*그룹\s*보기\b/.test(firstLine) || /^그룹\s*보기\b/.test(firstLine)) {
    const groupName = trimCommandPrefix(firstLine, [/^\/kakao_group_view(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*그룹\s*보기/, /^그룹\s*보기/]);
    return { kind: "group_admin", groupAction: "view", groupName };
  }
  if (firstToken === "/kakao_group_create" || /^카톡\s*그룹\s*생성\b/.test(firstLine) || /^그룹\s*생성\b/.test(firstLine)) {
    const groupName = trimCommandPrefix(firstLine, [/^\/kakao_group_create(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*그룹\s*생성/, /^그룹\s*생성/]);
    return { kind: "group_admin", groupAction: "create", groupName };
  }
  if (firstToken === "/kakao_group_delete" || /^카톡\s*그룹\s*삭제\b/.test(firstLine) || /^그룹\s*삭제\b/.test(firstLine)) {
    const rest = trimCommandPrefix(firstLine, [/^\/kakao_group_delete(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*그룹\s*삭제/, /^그룹\s*삭제/]);
    const confirmed = /\s확인$/.test(rest);
    return { kind: "group_admin", groupAction: "delete", groupName: rest.replace(/\s확인$/, "").trim(), confirmed };
  }
  if (firstToken === "/kakao_group_rename" || /^카톡\s*그룹\s*이름변경\b/.test(firstLine) || /^그룹\s*이름변경\b/.test(firstLine)) {
    const rest = trimCommandPrefix(firstLine, [/^\/kakao_group_rename(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*그룹\s*이름변경/, /^그룹\s*이름변경/]);
    const confirmed = /\s확인$/.test(rest);
    const body = rest.replace(/\s확인$/, "").trim();
    const [groupName, ...nextParts] = body.split(/\s*->\s*/);
    return { kind: "group_admin", groupAction: "rename", groupName: String(groupName || "").trim(), newGroupName: nextParts.join(" -> ").trim(), confirmed };
  }
  if (firstToken === "/kakao_group_add" || /^카톡\s*그룹\s*추가\b/.test(firstLine) || /^그룹\s*추가\b/.test(firstLine)) {
    const rest = trimCommandPrefix(firstLine, [/^\/kakao_group_add(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*그룹\s*추가/, /^그룹\s*추가/]);
    const parsed = splitGroupFriend(rest);
    return { kind: "group_admin", groupAction: "add_member", groupName: parsed.groupName, friendName: parsed.friendName };
  }
  if (firstToken === "/kakao_group_remove" || /^카톡\s*그룹\s*제거\b/.test(firstLine) || /^그룹\s*제거\b/.test(firstLine)) {
    const rest = trimCommandPrefix(firstLine, [/^\/kakao_group_remove(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*그룹\s*제거/, /^그룹\s*제거/]);
    const confirmed = /\s확인$/.test(rest);
    const parsed = splitGroupFriend(rest.replace(/\s확인$/, "").trim());
    return { kind: "group_admin", groupAction: "remove_member", groupName: parsed.groupName, friendName: parsed.friendName, confirmed };
  }
  return null;
}

function parseKakaoNoticeCommand(text) {
  const clean = String(text || "").trim();
  if (!clean) return null;
  const firstLine = clean.split(/\n+/)[0].trim();
  const firstToken = firstLine.split(/\s+/)[0].replace(/@[A-Za-z0-9_]+$/, "");
  if (firstToken === "/arsen_ping" || clean === "아르센핑") return { kind: "ping" };
  if (firstToken === "/arsen_stop" || clean === "긴급정지" || clean === "멈춰") {
    return { kind: "stop", jobId: firstLine.split(/\s+/)[1] || "active" };
  }
  const groupAdmin = parseKakaoGroupAdminCommand(clean, firstLine, firstToken);
  if (groupAdmin) return groupAdmin;
  if (firstToken === "/kakao_notice_failed" || /^카톡\s*공지\s*(실패목록|미발송목록|안된사람|안된사람들)\b/.test(firstLine)) {
    const rest = trimCommandPrefix(firstLine, [
      /^\/kakao_notice_failed(?:@[A-Za-z0-9_]+)?/i,
      /^카톡\s*공지\s*(실패목록|미발송목록|안된사람|안된사람들)/,
    ]);
    return { kind: "notice_failed_list", jobId: rest.trim() };
  }
  if (firstToken === "/kakao_notice_retry" || /^카톡\s*공지\s*재시도\b/.test(firstLine)) {
    const rest = trimCommandPrefix(firstLine, [/^\/kakao_notice_retry(?:@[A-Za-z0-9_]+)?/i, /^카톡\s*공지\s*재시도/]);
    const tokens = rest.split(/\s+/).filter(Boolean);
    const includeSent = tokens.some((token) => ["전체", "all", "전체재시도"].includes(token.toLowerCase()));
    const jobId = tokens.find((token) => !["전체", "all", "전체재시도"].includes(token.toLowerCase())) || "";
    return { kind: "notice_retry", jobId, includeSent };
  }
  const noticePrefix = firstToken === "/arsen_notice"
    || /^카톡\s*공지/.test(firstLine)
    || /^공지\s*카톡/.test(firstLine);
  const groupPrefix = firstToken === "/arsen_group_notice"
    || firstToken === "/kakao_group_notice"
    || /^카톡\s*그룹/.test(firstLine)
    || /^그룹\s*카톡/.test(firstLine);
  if (!noticePrefix && !groupPrefix) return null;
  const markerIndex = clean.indexOf("멘트:");
  const commandPart = markerIndex >= 0 ? clean.slice(0, markerIndex).trim() : clean.split(/\n+/)[0].trim();
  const customMessage = markerIndex >= 0 ? clean.slice(markerIndex + "멘트:".length).trim() : clean.split(/\n+/).slice(1).join("\n").trim();
  if (groupPrefix) {
    const groupName = commandPart
      .replace(/^\/(?:arsen_group_notice|kakao_group_notice)(?:@[A-Za-z0-9_]+)?/i, "")
      .replace(/^카톡\s*그룹|^그룹\s*카톡/, "")
      .trim();
    return { kind: "notice", target: "local_group", localGroupName: groupName, customMessage };
  }
  const tokens = commandPart.replace(/^카톡\s*공지|^공지\s*카톡/, "카톡공지").split(/\s+/).slice(1);
  let target = "approved";
  let sessionId = "";
  let localGroupName = "";
  for (let i = 0; i < tokens.length; i += 1) {
    const token = tokens[i];
    const lowered = token.toLowerCase();
    if (["approved", "all", "전체", "승인"].includes(lowered)) target = "approved";
    if (["latest", "next", "다음", "최근"].includes(lowered)) target = "latest";
    if (["group", "그룹"].includes(lowered)) {
      target = "local_group";
      localGroupName = tokens.slice(i + 1).join(" ").trim();
      break;
    }
    if (lowered.startsWith("session:")) {
      target = "session";
      sessionId = token.slice("session:".length);
    } else if (lowered === "session" && tokens[i + 1]) {
      target = "session";
      sessionId = tokens[i + 1];
      i += 1;
    }
  }
  return { kind: "notice", target, sessionId, localGroupName, customMessage };
}

async function stopKakaoNoticeJobs(env, jobId, request) {
  const state = await kakaoNoticeState(env);
  let stopped = 0;
  state.jobs = (state.jobs || []).map((job) => {
    const targetMatch = !jobId || jobId === "active" || job.id === jobId;
    if (!targetMatch) return job;
    if (!["prepare_requested", "preparing", "prepared", "pending_approval", "approved", "claimed", "stop_requested", "group_manage_requested", "group_managing"].includes(job.status)) return job;
    stopped += 1;
    return {
      ...job,
      status: job.status === "claimed" ? "stop_requested" : "stopped",
      stop_requested_at: now(),
      updated_at: now(),
    };
  });
  await saveKakaoNoticeState(env, state);
  await logAction(env, "system", "kakao_notice_stop_requested", `${jobId || "active"}:${stopped}`, request);
  return stopped;
}

async function createKakaoNoticeJob(env, command, request) {
  let targetLabel = "다음 강의";
  let rows = [];
  let sessionId = command.sessionId || "";
  if (command.target === "local_group") {
    const groupName = String(command.localGroupName || "").trim();
    if (!groupName) return { ok: false, message: "로컬 그룹명을 입력해야 합니다. 예: 카톡그룹 그룹명 멘트: 보낼 내용" };
    if (!String(command.customMessage || "").trim()) return { ok: false, message: "그룹 발송은 멘트가 필요합니다. 예: 카톡그룹 그룹명 멘트: 보낼 내용" };
    targetLabel = `로컬 그룹: ${groupName}`;
  } else if (command.target === "approved") {
    targetLabel = "승인 회원 전체";
    rows = await kakaoNoticeRowsForApproved(env);
  } else {
    if (!sessionId) {
      const session = await latestNoticeSession(env);
      sessionId = session?.id || "";
      targetLabel = session?.title ? `다음 강의: ${session.title}` : "다음 강의";
    } else {
      targetLabel = `강의 세션: ${sessionId}`;
    }
    if (!sessionId) return { ok: false, message: "공지 대상 강의 세션을 찾지 못했습니다." };
    rows = await kakaoNoticeRowsForSession(env, sessionId);
  }

  // 운영자 멘트만 AI 다듬기 대상. 이름/코드 등 개인 데이터는 이후 Worker가 결정적으로 삽입한다.
  const rawCustomMessage = String(command.customMessage || "").trim().slice(0, KAKAO_NOTICE_CUSTOM_MESSAGE_MAX);
  const polish = await polishKakaoNoticeMessage(env, rawCustomMessage, {
    kind: command.target === "local_group" ? "local_group" : "member_notice",
  });
  const customMessage = polish.text;

  const recipients = [];
  const skipped = [];
  for (const row of rows) {
    const code = await readableAccessCode(row, env);
    if (!code) {
      skipped.push({ member_id: row.id, name: row.name || "", reason: "missing_access_code" });
      continue;
    }
    recipients.push({
      id: crypto.randomUUID(),
      member_id: row.id,
      booking_id: row.booking_id || "",
      name: row.name || "",
      kakao_display_name: kakaoNoticeSearchName(row.name),
      message: kakaoNoticeMessage(row, code, env, customMessage),
      status: "pending",
      error: "",
    });
  }

  if (command.target !== "local_group" && !recipients.length) return { ok: false, message: `발송 가능한 대상이 없습니다. 제외 ${skipped.length}명` };

  const job = {
    id: kakaoNoticeJobId(),
    status: "prepare_requested",
    phase: "prepare",
    target: command.target,
    target_label: targetLabel,
    local_group_name: String(command.localGroupName || "").trim().slice(0, 120),
    session_id: sessionId || "",
    custom_message: customMessage.slice(0, KAKAO_NOTICE_CUSTOM_MESSAGE_MAX),
    original_custom_message: rawCustomMessage,
    polish_status: polish.status,
    polish_provider: polish.provider,
    recipients,
    skipped,
    created_at: now(),
    updated_at: now(),
    approved_at: "",
    claimed_at: "",
    finished_at: "",
  };
  const state = await kakaoNoticeState(env);
  state.jobs = [job, ...(state.jobs || [])];
  await saveKakaoNoticeState(env, state);
  await logAction(env, "system", "kakao_notice_job_created", `${job.id}:recipients=${recipients.length}:skipped=${skipped.length}`, request);
  return { ok: true, job };
}

async function kakaoNoticeFailedList(env, command) {
  const state = await kakaoNoticeState(env);
  const job = latestRetryableKakaoNoticeJob(state, String(command.jobId || "").trim());
  if (!job) return { ok: false, message: "카톡 공지 작업을 찾지 못했습니다." };
  const recipients = kakaoNoticePendingRetryRecipients(job, false);
  return { ok: true, job, recipients, text: kakaoNoticeFailureListText(job, recipients) };
}

async function createKakaoNoticeRetryJob(env, command, request) {
  const state = await kakaoNoticeState(env);
  const sourceJob = latestRetryableKakaoNoticeJob(state, String(command.jobId || "").trim());
  if (!sourceJob) return { ok: false, message: "재시도할 카톡 공지 작업을 찾지 못했습니다." };
  const retryRecipients = kakaoNoticePendingRetryRecipients(sourceJob, command.includeSent === true);
  if (!retryRecipients.length) return { ok: false, message: "재시도할 미발송/실패 대상이 없습니다." };
  const recipients = retryRecipients.map((recipient) => ({
    id: crypto.randomUUID(),
    member_id: String(recipient.member_id || ""),
    booking_id: String(recipient.booking_id || ""),
    name: String(recipient.name || "").slice(0, 120),
    kakao_display_name: String(recipient.kakao_display_name || recipient.name || "").slice(0, 160),
    message: String(recipient.message || "").slice(0, 4000),
    status: "pending",
    error: "",
    sent_at: "",
    retry_from_recipient_id: String(recipient.id || ""),
  }));
  const job = {
    id: kakaoNoticeJobId(),
    status: "prepare_requested",
    phase: "prepare",
    target: sourceJob.target || "retry",
    target_label: `재시도: ${sourceJob.target_label || sourceJob.id}`,
    source_job_id: sourceJob.id,
    local_group_name: String(sourceJob.local_group_name || "").slice(0, 120),
    session_id: String(sourceJob.session_id || ""),
    custom_message: String(sourceJob.custom_message || "").slice(0, KAKAO_NOTICE_CUSTOM_MESSAGE_MAX),
    original_custom_message: String(sourceJob.original_custom_message || "").slice(0, KAKAO_NOTICE_CUSTOM_MESSAGE_MAX),
    polish_status: String(sourceJob.polish_status || ""),
    polish_provider: String(sourceJob.polish_provider || ""),
    recipients,
    skipped: [],
    created_at: now(),
    updated_at: now(),
    approved_at: "",
    claimed_at: "",
    finished_at: "",
  };
  state.jobs = [job, ...(state.jobs || [])];
  await saveKakaoNoticeState(env, state);
  await logAction(env, "system", "kakao_notice_retry_job_created", `${job.id}:source=${sourceJob.id}:recipients=${recipients.length}`, request);
  return { ok: true, job, sourceJob, retryRecipients };
}

async function createKakaoGroupAdminJob(env, command, request) {
  const action = String(command.groupAction || "").trim();
  const groupName = String(command.groupName || "").trim();
  const newGroupName = String(command.newGroupName || "").trim();
  const friendName = String(command.friendName || "").trim();
  const destructive = ["delete", "rename", "remove_member"].includes(action);
  if (!action) return { ok: false, message: "그룹 관리 동작을 찾지 못했습니다." };
  if (["view", "create", "delete", "rename", "add_member", "remove_member"].includes(action) && !groupName) {
    return { ok: false, message: "그룹명을 입력해야 합니다." };
  }
  if (action === "rename" && !newGroupName) return { ok: false, message: "새 그룹명을 입력해야 합니다. 예: 카톡그룹이름변경 기존 -> 새이름 확인" };
  if (["add_member", "remove_member"].includes(action) && !friendName) {
    return { ok: false, message: "친구 이름을 입력해야 합니다. 예: 카톡그룹추가 그룹명 / 친구이름" };
  }
  if (destructive && command.confirmed !== true) {
    return { ok: false, message: "삭제/이름변경/제거는 명령 끝에 '확인'을 붙여야 합니다." };
  }
  const labelMap = {
    list: "그룹 목록",
    view: "그룹 보기",
    create: "그룹 생성",
    delete: "그룹 삭제",
    rename: "그룹 이름변경",
    add_member: "그룹 멤버 추가",
    remove_member: "그룹 멤버 제거",
  };
  const job = {
    id: kakaoNoticeJobId(),
    status: "group_manage_requested",
    phase: "group_manage",
    target: "local_group_admin",
    target_label: labelMap[action] || "그룹 관리",
    group_action: action,
    local_group_name: groupName.slice(0, 120),
    new_group_name: newGroupName.slice(0, 120),
    friend_name: friendName.slice(0, 120),
    summary: "",
    recipients: [],
    skipped: [],
    created_at: now(),
    updated_at: now(),
    claimed_at: "",
    finished_at: "",
  };
  const state = await kakaoNoticeState(env);
  state.jobs = [job, ...(state.jobs || [])];
  await saveKakaoNoticeState(env, state);
  await logAction(env, "system", "kakao_group_admin_job_created", `${job.id}:${action}`, request);
  return { ok: true, job };
}

async function handleTelegramMessage(env, message, request) {
  const chatId = String(message?.chat?.id || "");
  const text = String(message?.text || "").trim();
  const command = parseKakaoNoticeCommand(text);
  if (!command) return "ignored";
  const threadId = String(message?.message_thread_id || "");
  const isAdminChat = !String(env.TELEGRAM_ADMIN_CHAT_ID || "") || chatId === String(env.TELEGRAM_ADMIN_CHAT_ID);
  if (!isAdminChat) {
    await sendTelegramToChat(
      env,
      chatId,
      [
        "ARSEN 봇은 이 메시지를 받았지만, 이 방은 관리자 방으로 등록되어 있지 않습니다.",
        "관리자 방에서 다시 보내거나 TELEGRAM_ADMIN_CHAT_ID 설정을 확인하세요.",
      ].join("\n"),
      null,
      "button",
      threadId
    );
    return "ignored_non_admin_chat_notified";
  }
  if (command.kind === "ping") {
    await sendTelegramToChat(env, chatId, "ARSEN Cloudflare 텔레그램 수신 정상입니다.", null, "button", threadId);
    return "ping_ok";
  }
  if (command.kind === "stop") {
    const stopped = await stopKakaoNoticeJobs(env, command.jobId, request);
    await sendTelegramToChat(env, chatId, `ARSEN 카톡 공지 긴급정지 요청 처리: ${stopped}개 작업`, null, "button", threadId);
    return "stop_requested";
  }
  if (command.kind === "notice_failed_list") {
    const result = await kakaoNoticeFailedList(env, command);
    await sendTelegramToChat(
      env,
      chatId,
      result.ok ? result.text : `ARSEN 카톡 실패목록 조회 실패: ${htmlEscape(result.message || "unknown")}`,
      null,
      "button",
      threadId
    );
    return result.ok ? "notice_failed_list" : result.message || "failed";
  }
  if (command.kind === "notice_retry") {
    const result = await createKakaoNoticeRetryJob(env, command, request);
    if (!result.ok) {
      await sendTelegramToChat(env, chatId, `ARSEN 카톡 재시도 작업 생성 실패: ${htmlEscape(result.message || "unknown")}`, null, "button", threadId);
      return result.message || "failed";
    }
    await sendTelegramToChat(env, chatId, kakaoNoticeFailureListText(result.sourceJob, result.retryRecipients), null, "button", threadId);
    await sendTelegramToChat(env, chatId, safePrepareJobForTelegram(result.job), kakaoNoticeStopKeyboard(result.job.id), "button", threadId);
    return "notice_retry_job_created";
  }
  if (command.kind === "group_admin") {
    const result = await createKakaoGroupAdminJob(env, command, request);
    if (!result.ok) {
      await sendTelegramToChat(env, chatId, `카톡 그룹 관리 요청 실패: ${htmlEscape(result.message || "unknown")}`, null, "button", threadId);
      return result.message || "failed";
    }
    await sendTelegramToChat(
      env,
      chatId,
      [
        "<b>카톡 그룹 관리 요청 생성</b>",
        `작업ID: <code>${htmlEscape(result.job.id)}</code>`,
        `작업: ${htmlEscape(result.job.target_label || "-")}`,
        result.job.local_group_name ? `그룹: ${htmlEscape(result.job.local_group_name)}` : "",
        result.job.friend_name ? `대상: ${htmlEscape(result.job.friend_name)}` : "",
        "맥에어가 로컬 그룹 DB를 수정/조회한 뒤 결과를 알려드립니다.",
      ].filter(Boolean).join("\n"),
      null,
      "button",
      threadId
    );
    return "group_admin_job_created";
  }
  const result = await createKakaoNoticeJob(env, command, request);
  if (!result.ok) {
    await sendTelegramToChat(
      env,
      chatId,
      `ARSEN 카톡 공지 작업 생성 실패: ${htmlEscape(result.message || "unknown")}`,
      null,
      "button",
      threadId
    );
    return result.message || "failed";
  }
  await sendTelegramToChat(env, chatId, safePrepareJobForTelegram(result.job), kakaoNoticeStopKeyboard(result.job.id), "button", threadId);
  return "notice_job_created";
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
  const upgradeFrom = attempted?.lead_upgrade_from || attempted?.upgrade_from_plan_type || "";
  const sourceLabel = leadSourceLabel(upgradeFrom);
  const title = upgradeFrom
    ? `<b>ARSEN ${htmlEscape(sourceLabel)}에서 ${htmlEscape(planLabel)} 신청으로 변경</b>`
    : duplicate
      ? `<b>ARSEN 재신청 - ${htmlEscape(planLabel)}</b>`
      : `<b>ARSEN 신규 ${htmlEscape(planLabel)} 신청</b>`;
  const base = [
    title,
    upgradeFrom
      ? `전환 안내: 기존 ${htmlEscape(sourceLabel)} 리드를 신청자/멤버 목록의 ${htmlEscape(planLabel)} 신청으로 승격했습니다.`
      : "",
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
  ].filter(Boolean);
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
  return sendTelegramToChat(env, env.TELEGRAM_ADMIN_CHAT_ID, text, replyMarkup, kind);
}

async function sendTelegramToChat(env, chatId, text, replyMarkup = null, kind = "application", messageThreadId = "") {
  if (!telegramEnabled(env, kind)) return "disabled";
  if (!telegramConfigured(env, false)) return "not_configured";
  if (!chatId) return "missing_chat_id";
  try {
    const body = {
      chat_id: chatId,
      text,
      parse_mode: "HTML",
      disable_web_page_preview: true,
      ...(replyMarkup ? { reply_markup: replyMarkup } : {}),
    };
    if (messageThreadId) body.message_thread_id = messageThreadId;
    const response = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(body),
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

function defaultFreeClassGuide(booking) {
  const [dateText, timeText] = formatKoreanDateTimeRange(booking?.session_starts_at, booking?.session_ends_at);
  const name = booking?.applicant_name || booking?.member_name || "신청자";
  return [
    "[무료강의 안내]",
    "",
    `${name}님, 무료강의 신청이 확인되었습니다.`,
    "",
    "강의 정보",
    `과정: ${booking?.session_title || DEFAULT_TITLE}`,
    `일정: ${dateText}`,
    `시간: ${timeText || "-"}`,
    `장소: ${booking?.session_location || booking?.location || DEFAULT_LOCATION}`,
    "",
    "참여 전 확인",
    "참석 가능 여부를 답장으로 알려주세요.",
    "준비물: 노트북 또는 태블릿, 사용 중인 AI 계정, 궁금한 자동화 주제",
    "변경이 필요하면 1:1 문의방으로 편하게 남겨주세요.",
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
	    path === "/study/sessions" ||
	    path === "/apply" ||
    path === "/stats" ||
    path === "/api/site-theme" ||
    path === "/api/daf/manifest" ||
    path === "/api/daf/programs" ||
    path === "/api/daf/notices" ||
    path === "/api/daf/launcher/release" ||
    path === "/api/launcher/release" ||
    path.startsWith("/api/daf/launcher/artifacts/") ||
    path === "/api/education" ||
    path === "/api/consultations" ||
    path === "/api/license/activate" ||
    path === "/api/license/verify" ||
    path.startsWith("/api/yoonbot/") ||
    path === "/api/review-board" ||
    path.startsWith("/api/review-board/submit/") ||
    path === "/telegram/webhook" ||
    path.startsWith("/auth/kakao") ||
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

async function kakaoNoticeJobsPayload(env, status = "") {
  const state = await kakaoNoticeState(env);
  const jobs = (state.jobs || []).filter((job) => !status || status === "all" || job.status === status);
  return {
    ok: true,
    data: jobs.map((job) => ({
      ...job,
      total: Number(job.recipients?.length || 0),
      sent: kakaoNoticeSentCount(job),
      failed: (job.recipients || []).filter((item) => item.status === "failed").length,
    })),
  };
}

async function kakaoNoticeJobPayload(env, jobId) {
  const state = await kakaoNoticeState(env);
  const job = (state.jobs || []).find((item) => item.id === jobId);
  if (!job) return fail(404, "카톡 공지 작업을 찾지 못했습니다.");
  return json({ ok: true, data: job });
}

async function claimKakaoNoticeJob(env, jobId, request) {
  const state = await kakaoNoticeState(env);
  const job = updateKakaoNoticeJob(state, jobId, (item) => {
    if (item.status === "prepare_requested") {
      item.status = "preparing";
      item.claim_phase = "prepare";
    } else if (item.status === "approved") {
      item.status = "claimed";
      item.claim_phase = "send";
    } else if (item.status === "group_manage_requested") {
      item.status = "group_managing";
      item.claim_phase = "group_manage";
    } else {
      return;
    }
    item.claimed_at = now();
  });
  if (!job) return fail(404, "카톡 공지 작업을 찾지 못했습니다.");
  if (!["preparing", "claimed", "group_managing"].includes(job.status)) return fail(409, `현재 작업 상태는 ${job.status}입니다.`);
  await saveKakaoNoticeState(env, state);
  await logAction(env, "system", "kakao_notice_job_claimed", jobId, request);
  return json({ ok: true, data: job });
}

async function finishKakaoNoticeJob(env, jobId, body, request) {
  const state = await kakaoNoticeState(env);
  const incoming = Array.isArray(body.recipients) ? body.recipients : [];
  const resultMap = new Map(incoming.map((item) => [String(item.id || item.recipient_id || ""), item]));
  const isProgress = body.progress === true;
  const job = updateKakaoNoticeJob(state, jobId, (item) => {
    const seenRecipientIds = new Set();
    item.recipients = (item.recipients || []).map((recipient) => {
      seenRecipientIds.add(String(recipient.id || ""));
      const result = resultMap.get(String(recipient.id || ""));
      if (!result) return recipient;
      return {
        ...recipient,
        name: result.name ? String(result.name).slice(0, 120) : recipient.name,
        kakao_display_name: result.kakao_display_name ? String(result.kakao_display_name).slice(0, 160) : recipient.kakao_display_name,
        message: result.message ? String(result.message).slice(0, 4000) : recipient.message,
        status: String(result.status || recipient.status || ""),
        error: String(result.error || "").slice(0, 240),
        sent_at: result.sent_at || recipient.sent_at || "",
      };
    });
    const appended = incoming
      .filter((result) => String(result.id || result.recipient_id || "") && !seenRecipientIds.has(String(result.id || result.recipient_id || "")))
      .map((result) => ({
        id: String(result.id || result.recipient_id || crypto.randomUUID()),
        member_id: String(result.member_id || ""),
        booking_id: String(result.booking_id || ""),
        name: String(result.name || "").slice(0, 120),
        kakao_display_name: String(result.kakao_display_name || result.name || "").slice(0, 160),
        message: String(result.message || "").slice(0, 4000),
        status: String(result.status || "pending"),
        error: String(result.error || "").slice(0, 240),
        sent_at: result.sent_at || "",
      }));
    if (appended.length) item.recipients = [...item.recipients, ...appended].slice(0, 500);
    const failed = kakaoNoticeFailureCount(item);
    const ready = kakaoNoticeReadyCount(item);
    const sent = kakaoNoticeSentCount(item);
    const dryRun = item.recipients.filter((recipient) => recipient.status === "dry_run").length;
    item.ready_count = ready;
    item.status = isProgress ? (body.status || item.status) : body.status || (failed ? "failed" : dryRun ? "dry_run_done" : "done");
    item.sent_count = sent;
    item.failed_count = failed;
    if (body.summary !== undefined) item.summary = String(body.summary || "").slice(0, 3500);
    if (!isProgress) item.finished_at = now();
  });
  if (!job) return fail(404, "카톡 공지 작업을 찾지 못했습니다.");
  await saveKakaoNoticeState(env, state);
  if (isProgress) {
    const done = (job.recipients || []).filter((recipient) => recipient.status && recipient.status !== "pending").length;
    const ready = kakaoNoticeReadyCount(job);
    const total = Number(job.recipients?.length || 0);
    await logAction(env, "system", "kakao_notice_job_progress", `${jobId}:${done}/${total}`, request);
    await sendTelegram(
      env,
      [
        "<b>ARSEN 카톡 대상 준비 진행</b>",
        `작업ID: <code>${htmlEscape(jobId)}</code>`,
        `진행: ${done}/${total}명`,
        `준비 완료: ${ready}명`,
        `준비 실패: ${Math.max(0, done - ready)}명`,
      ].join("\n"),
      kakaoNoticeStopKeyboard(jobId),
      "button"
    );
    return json({ ok: true, data: job });
  }
  await logAction(env, "system", "kakao_notice_job_finished", `${jobId}:${job.status}`, request);
  if (job.target === "local_group_admin") {
    await sendTelegram(
      env,
      [
        "<b>카톡 그룹 관리 결과</b>",
        `작업ID: <code>${htmlEscape(jobId)}</code>`,
        `작업: ${htmlEscape(job.target_label || "-")}`,
        `상태: ${htmlEscape(job.status)}`,
        job.summary ? "" : "",
        job.summary ? htmlEscape(job.summary) : "",
      ].filter(Boolean).join("\n"),
      null,
      "button"
    );
    return json({ ok: true, data: job });
  }
  if (["prepared", "prepare_failed", "prepare_blocked"].includes(job.status)) {
    const ready = kakaoNoticeReadyCount(job);
    await sendTelegram(
      env,
      safeJobForTelegram(job),
      ready > 0 ? kakaoNoticeKeyboard(env, jobId) : kakaoNoticeStopKeyboard(jobId),
      "button"
    );
    return json({ ok: true, data: job });
  }
  await sendTelegram(
    env,
    [
      "<b>ARSEN 카톡 공지 결과</b>",
      `작업ID: <code>${htmlEscape(jobId)}</code>`,
      `상태: ${htmlEscape(job.status)}`,
      `성공: ${Number(job.sent_count || 0)}명`,
      `실패: ${Number(job.failed_count || 0)}명`,
    ].join("\n"),
    null,
    "button"
  );
  return json({ ok: true, data: job });
}

function safeMember(row) {
  if (!row) return null;
  const copy = { ...row };
  delete copy.email_encrypted;
  delete copy.phone_encrypted;
  delete copy.kakao_profile;
  return copy;
}

function safePublicMember(row) {
  if (!row) return null;
  return {
    id: row.id,
    name: row.name,
    phone_masked: row.phone_masked,
    openchat_nickname: row.openchat_nickname || "",
    status: row.status,
    plan_type: row.plan_type,
    participation_grade: row.participation_grade,
    paid_class_count: Number(row.paid_class_count || 0),
    approved_at: row.approved_at,
    code_expires_at: null,
    code_expiry_label: "기한 없음",
  };
}

function classSummaryText(summary) {
  const free = Number(summary?.free_completed || 0);
  const paid = Number(summary?.paid_completed || 0);
  const scheduled = Number(summary?.total_scheduled || 0);
  return `무료 ${free}회 · 유료 ${paid}회${scheduled ? ` · 예정 ${scheduled}건` : ""}`;
}

const MEMBER_LOOKUP_CHUNK_SIZE = 80;

function chunkValues(values, size = MEMBER_LOOKUP_CHUNK_SIZE) {
  const chunks = [];
  for (let index = 0; index < values.length; index += size) {
    chunks.push(values.slice(index, index + size));
  }
  return chunks;
}

async function memberClassSummaries(env, memberIds) {
  if (!memberIds.length) return new Map();
  const attendedExpr = `(
    b.status='completed'
    OR (
      b.status='confirmed'
      AND COALESCE(s.starts_at, b.confirmed_at, b.updated_at, b.created_at) <= ?
    )
  )`;
  const rows = [];
  for (const chunk of chunkValues(memberIds)) {
    const placeholders = chunk.map(() => "?").join(",");
    const chunkRows = await all(
      env,
      `SELECT
         b.member_id,
         SUM(CASE WHEN ${attendedExpr} AND (
           COALESCE(s.program_type, '') LIKE '%free%' OR COALESCE(s.price_krw, b.payment_amount_krw, 0)=0 OR b.payment_status='waived'
         ) THEN 1 ELSE 0 END) AS free_completed,
         SUM(CASE WHEN ${attendedExpr} AND NOT (
           COALESCE(s.program_type, '') LIKE '%free%' OR COALESCE(s.price_krw, b.payment_amount_krw, 0)=0 OR b.payment_status='waived'
         ) THEN 1 ELSE 0 END) AS paid_completed,
         SUM(CASE WHEN b.status IN ('requested','payment_guide_sent','payment_pending','payment_confirmed','confirmed','waitlisted') AND NOT ${attendedExpr} AND (
           COALESCE(s.program_type, '') LIKE '%free%' OR COALESCE(s.price_krw, b.payment_amount_krw, 0)=0 OR b.payment_status='waived'
         ) THEN 1 ELSE 0 END) AS free_scheduled,
         SUM(CASE WHEN b.status IN ('requested','payment_guide_sent','payment_pending','payment_confirmed','confirmed','waitlisted') AND NOT ${attendedExpr} AND NOT (
           COALESCE(s.program_type, '') LIKE '%free%' OR COALESCE(s.price_krw, b.payment_amount_krw, 0)=0 OR b.payment_status='waived'
         ) THEN 1 ELSE 0 END) AS paid_scheduled
       FROM bookings b
       LEFT JOIN sessions s ON s.id=b.session_id
       WHERE b.member_id IN (${placeholders})
       GROUP BY b.member_id`,
      now(),
      now(),
      now(),
      now(),
      ...chunk
    );
    rows.push(...chunkRows);
  }
  const result = new Map();
  for (const row of rows) {
    const freeCompleted = Number(row.free_completed || 0);
    const paidCompleted = Number(row.paid_completed || 0);
    const freeScheduled = Number(row.free_scheduled || 0);
    const paidScheduled = Number(row.paid_scheduled || 0);
    result.set(row.member_id, {
      free_completed: freeCompleted,
      paid_completed: paidCompleted,
      free_scheduled: freeScheduled,
      paid_scheduled: paidScheduled,
      total_completed: freeCompleted + paidCompleted,
      total_scheduled: freeScheduled + paidScheduled,
    });
  }
  return result;
}

async function memberPaidClassCount(env, memberId) {
  const row = await one(
    env,
    `SELECT COUNT(*) AS count
     FROM bookings b
     LEFT JOIN sessions s ON s.id=b.session_id
     WHERE b.member_id=?
       AND (
         b.status='completed'
         OR (
           b.status='confirmed'
           AND COALESCE(s.starts_at, b.confirmed_at, b.updated_at, b.created_at) <= ?
         )
       )
       AND COALESCE(s.program_type, '') != ?
       AND COALESCE(s.program_type, '') NOT LIKE '%free%'
       AND COALESCE(s.price_krw, b.payment_amount_krw, 0) > 0
       AND COALESCE(b.payment_status, '') != 'waived'`,
    memberId,
    now(),
    STUDY_PROGRAM_TYPE
  );
  return Number(row?.count || 0);
}

async function withPublicMemberStats(env, member) {
  if (!member) return null;
  return { ...member, paid_class_count: await memberPaidClassCount(env, member.id) };
}

function completedBooking(row) {
  if (!row) return false;
  if (row.status === "completed") return true;
  if (row.status !== "confirmed") return false;
  const value = row.session_starts_at || row.confirmed_at || row.updated_at || row.created_at || "";
  const date = parseKstDate(value);
  return Boolean(date && date.getTime() <= Date.now());
}

function bookingKind(row) {
  const program = String(row?.session_program_type || "").toLowerCase();
  const amount = Number(row?.session_price_krw ?? row?.payment_amount_krw ?? 0);
  if (program === STUDY_PROGRAM_TYPE) return "study";
  if (program.includes("free") || amount === 0 || row?.payment_status === "waived") return "free";
  return "paid";
}

function memberLevelProfile(bookings = [], reviews = []) {
  const counts = { free: 0, paid: 0, study: 0, reviews: reviews.length };
  for (const booking of bookings) {
    if (!completedBooking(booking)) continue;
    counts[bookingKind(booking)] += 1;
  }
  const points = counts.free * 10 + counts.paid * 30 + counts.study * 15 + counts.reviews * 5;
  const levels = [
    { level: 4, name: "Partner", min: 150, next: null, access: "파트너 후보" },
    { level: 3, name: "Builder", min: 80, next: 150, access: "심화 게시판" },
    { level: 2, name: "Member", min: 30, next: 80, access: "스터디 게시판" },
    { level: 1, name: "Starter", min: 0, next: 30, access: "기본 게시판" },
  ];
  const current = levels.find((item) => points >= item.min) || levels[levels.length - 1];
  return {
    points,
    level: current.level,
    level_name: current.name,
    next_points: current.next,
    points_to_next: current.next ? Math.max(0, current.next - points) : 0,
    counts,
    access_label: current.access,
    board_access: {
      basic: true,
      study: current.level >= 2,
      advanced: current.level >= 3,
      partner: current.level >= 4,
    },
  };
}

function memberReviewPublicRow(row) {
  if (!row) return null;
  return {
    id: row.id,
    booking_id: row.booking_id || "",
    class_title: row.class_title,
    class_date: row.class_date,
    title: row.title,
    summary: row.summary,
    status: row.status,
    source: row.source,
    privacy_checked: Boolean(row.privacy_checked),
    created_at: row.created_at,
    updated_at: row.updated_at,
  };
}

async function memberReviewRows(env, memberId) {
  if (!memberId) return [];
  try {
    const rows = await all(
      env,
      `SELECT id, booking_id, class_title, class_date, title, summary, status, source, privacy_checked, created_at, updated_at
       FROM review_entries
       WHERE member_id=?
       ORDER BY created_at DESC`,
      memberId
    );
    return rows.map(memberReviewPublicRow);
  } catch (error) {
    if (String(error?.message || error).includes("no such column")) return [];
    throw error;
  }
}

async function publicMemberDashboardPayload(env, member, kakao = null) {
  const safe = safePublicMember(await withPublicMemberStats(env, member));
  const bookings = (await bookingRows(env)).filter((row) => row.member_id === member.id).map(safePublicBooking);
  const reviews = await memberReviewRows(env, member.id);
  return {
    member: safe,
    bookings,
    reviews,
    progress: memberLevelProfile(bookings, reviews),
    ...(kakao ? { kakao } : {}),
  };
}

async function memberContactRegistrations(env, memberIds) {
  if (!memberIds.length) return new Map();
  const rows = [];
  for (const chunk of chunkValues(memberIds)) {
    const placeholders = chunk.map(() => "?").join(",");
    const chunkRows = await all(
      env,
      `SELECT member_id, detail, created_at
       FROM member_logs
       WHERE action='contact_registered'
         AND member_id IN (${placeholders})
       ORDER BY created_at ASC`,
      ...chunk
    );
    rows.push(...chunkRows);
  }
  const result = new Map();
  for (const row of rows) {
    let detail = {};
    try {
      detail = JSON.parse(row.detail || "{}");
    } catch (_) {
      detail = {};
    }
    result.set(row.member_id, {
      registered: Boolean(detail.registered ?? true),
      note: String(detail.note || ""),
      created_at: row.created_at,
    });
  }
  return result;
}

function parseDuplicateDetail(detailText) {
  const text = String(detailText || "").trim();
  if (!text) return {};
  try {
    const parsed = JSON.parse(text);
    return parsed && typeof parsed === "object" ? parsed : { note: text };
  } catch (_) {
    const result = { note: text };
    for (const part of text.split(",")) {
      if (!part.includes("=")) continue;
      const [key, ...rest] = part.split("=");
      result[key.trim()] = rest.join("=").trim();
    }
    return result;
  }
}

async function memberDuplicateActivity(env, memberIds) {
  if (!memberIds.length) return new Map();
  const rows = [];
  for (const chunk of chunkValues(memberIds)) {
    const placeholders = chunk.map(() => "?").join(",");
    const chunkRows = await all(
      env,
      `SELECT member_id, detail, created_at
       FROM member_logs
       WHERE action='duplicate_apply'
         AND member_id IN (${placeholders})
       ORDER BY created_at DESC`,
      ...chunk
    );
    rows.push(...chunkRows);
  }
  const result = new Map();
  for (const row of rows) {
    const detail = parseDuplicateDetail(row.detail);
    const bucket = result.get(row.member_id) || { count: 0, logs: [] };
    bucket.count += 1;
    if (bucket.logs.length < 5) {
      bucket.logs.push({
        created_at: row.created_at,
        source: detail.source || detail.duplicate_source || "",
        attempt_name: detail.attempt_name || detail.name || "",
        attempt_phone_masked: detail.attempt_phone_masked || "",
        attempt_plan_type: detail.attempt_plan_type || "",
        attempt_session_id: detail.attempt_session_id || "",
        note: detail.note || "",
      });
    }
    result.set(row.member_id, bucket);
  }
  for (const activity of result.values()) {
    const latest = activity.logs[0] || {};
    const sourceLabel = { phone: "전화번호", email: "이메일" }[latest.source] || latest.source || "확인 기준";
    const attemptName = latest.attempt_name || "이름 미기록";
    activity.last_at = latest.created_at || null;
    activity.last_source = latest.source || "";
    activity.last_attempt_name = latest.attempt_name || "";
    activity.last_attempt_plan_type = latest.attempt_plan_type || "";
    activity.summary_text = `재신청 ${activity.count}회 · 최근 ${sourceLabel} · ${attemptName}`;
  }
  return result;
}

async function membersWithAdminFields(env, rows) {
  const members = rows.map(safeMember).filter(Boolean);
  const ids = members.map((member) => member.id).filter(Boolean);
  const summaries = await memberClassSummaries(env, ids);
  const registrations = await memberContactRegistrations(env, ids);
  const duplicateActivity = await memberDuplicateActivity(env, ids);
  for (const member of members) {
    const summary = summaries.get(member.id) || {
      free_completed: 0,
      paid_completed: 0,
      free_scheduled: 0,
      paid_scheduled: 0,
      total_completed: 0,
      total_scheduled: 0,
    };
    const registration = registrations.get(member.id) || {};
    member.class_summary = summary;
    member.class_summary_text = classSummaryText(summary);
    member.contact_registered = Boolean(registration.registered);
    member.contact_registered_at = registration.created_at || null;
    member.contact_registered_note = registration.note || "";
    const duplicate = duplicateActivity.get(member.id) || { count: 0, logs: [], summary_text: "" };
    member.duplicate_apply_count = Number(duplicate.count || 0);
    member.duplicate_apply_last_at = duplicate.last_at || null;
    member.duplicate_apply_last_source = duplicate.last_source || "";
    member.duplicate_apply_last_attempt_name = duplicate.last_attempt_name || "";
    member.duplicate_apply_last_attempt_plan_type = duplicate.last_attempt_plan_type || "";
    member.duplicate_apply_summary_text = duplicate.summary_text || "";
    member.duplicate_apply_logs = duplicate.logs || [];
    member.latest_activity_at = [member.created_at, duplicate.last_at].filter(Boolean).sort().pop() || member.created_at || null;
  }
  return members;
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
    session_program_type: row.session_program_type,
    session_audience_level: row.session_audience_level,
    session_starts_at: row.session_starts_at,
    session_ends_at: row.session_ends_at,
    session_location: row.session_location || row.location,
    session_price_krw: row.session_price_krw,
    location: row.location,
    status: row.status,
    payment_status: row.payment_status,
    payment_amount_krw: row.payment_amount_krw,
    confirmed_at: row.confirmed_at,
    request_rank: row.request_rank,
    paid_rank: row.paid_rank,
    waitlist_rank: row.waitlist_rank,
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
      s.price_krw AS session_price_krw, s.payment_guide AS session_payment_guide, s.materials AS session_materials,
      s.program_type AS session_program_type, s.audience_level AS session_audience_level,
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
      Number(data.payment_amount_krw == null || data.payment_amount_krw === "" ? DEFAULT_PRICE : data.payment_amount_krw),
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

function isFreeSession(session) {
  if (!session) return false;
  if (isStudySession(session)) return false;
  return String(session.program_type || "").toLowerCase().includes("free") || Number(session.price_krw || 0) === 0;
}

function isStudySession(session) {
  return String(session?.program_type || "").toLowerCase() === STUDY_PROGRAM_TYPE;
}

async function studyMemberAcceptance(env, session, memberId) {
  const paidCompleted = await memberPaidClassCount(env, memberId);
  if (!isStudySession(session)) return [true, "", { paid_completed: paidCompleted }];
  const audienceLevel = String(session?.audience_level || "approved").toLowerCase();
  if (audienceLevel === "paid_only" && paidCompleted < 1) {
    return [false, "이 스터디는 유료강의 수강 이력이 있는 승인 멤버만 신청할 수 있습니다.", { paid_completed: paidCompleted, audience_level: audienceLevel }];
  }
  return [true, "", { paid_completed: paidCompleted, audience_level: audienceLevel }];
}

async function maybeCreateFreeSessionBooking(env, member, sessionId, request) {
  if (!sessionId) return null;
  const session = await getSession(env, sessionId);
  if (!isFreeSession(session)) return { error: "무료강의 일정만 무료 신청에서 바로 예약할 수 있습니다.", status: 400 };
  const existing = await one(
    env,
    "SELECT id FROM bookings WHERE member_id=? AND session_id=? AND status NOT IN ('canceled','rejected','no_show') LIMIT 1",
    member.id,
    sessionId
  );
  if (existing) {
    return {
      booking: await getBooking(env, existing.id),
      booking_id: existing.id,
      duplicate_booking: true,
      message: "이미 선택한 무료강의 일정에 신청되어 있습니다.",
    };
  }
  const [ok, reason] = sessionAcceptance(session);
  if (!ok) return { error: reason, status: 400 };
  const bookingId = await createBooking(env, {
    session_id: sessionId,
    member_id: member.id,
    applicant_name: member.name || "신청자",
    phone_masked: member.phone_masked || "",
    desired_outcome: member.short_term_goal || member.reason || "",
    preparedness: member.skills || "",
    status: "confirmed",
    payment_status: "waived",
    payment_amount_krw: 0,
    payment_note: "무료강의 신청: 입금 없음",
    confirmed_at: now(),
  });
  await logAction(env, member.id, "free_booking_created", `booking_id=${bookingId}`, request);
  return {
    booking: await getBooking(env, bookingId),
    booking_id: bookingId,
    duplicate_booking: false,
    message: "무료강의 일정 신청이 함께 접수되었습니다.",
  };
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

async function upgradeLeadToApplication(env, memberId, data, envSource = env) {
  const timestamp = now();
  const phone = normalizePhoneForStorage(data.phone || "");
  const email = String(data.email || "").trim().toLowerCase();
  const result = await env.DB.prepare(
    `UPDATE members
     SET name=?,
         email_encrypted=?,
         email_hash=?,
         phone_hash=?,
         phone_masked=?,
         phone_encrypted=?,
         gender=?,
         age=?,
         job=?,
         referral_source=?,
         reason=?,
         ai_level=?,
         plan_type=?,
         ai_tools=?,
         ai_subscription=?,
         ai_weekly_hours=?,
         ai_use_cases=?,
         group_goals=?,
         short_term_goal=?,
         participation_type=?,
         preferred_schedule=?,
         available_time_slots=?,
         region=?,
         main_device=?,
         can_code=?,
         can_present=?,
         skills=?,
         contribution=?,
         participation_grade=?,
         consent_personal=?,
         consent_marketing=?,
         consent_at=?,
         consent_version=?,
         status='pending',
         rejection_reason=NULL,
         access_code=NULL,
         code_expires_at=NULL,
         code_issued_at=NULL,
         code_fail_count=0,
         code_locked_until=NULL,
         approved_at=NULL
     WHERE id=?`
  )
    .bind(
      data.name || "신청자",
      await encryptLegacyValue(email, envSource, "EMAIL_SECRET_KEY"),
      email ? await hmacHex(email, envSource, "EMAIL_SECRET_KEY") : "",
      phone ? await hmacHex(phone, envSource, "PHONE_SECRET_KEY") : "",
      maskPhone(phone),
      await encryptLegacyValue(phone, envSource, "PHONE_SECRET_KEY"),
      data.gender || "",
      Number(data.age || 0),
      data.job || "",
      data.referral_source || "",
      data.reason || data.desired_outcome || "",
      data.ai_level || "",
      data.plan_type || "full",
      Array.isArray(data.ai_tools) ? JSON.stringify(data.ai_tools) : data.ai_tools || "",
      data.ai_subscription || "",
      data.ai_weekly_hours || "",
      Array.isArray(data.ai_use_cases) ? JSON.stringify(data.ai_use_cases) : data.ai_use_cases || "",
      Array.isArray(data.group_goals) ? JSON.stringify(data.group_goals) : data.group_goals || "",
      data.short_term_goal || data.desired_outcome || "",
      data.participation_type || "",
      data.preferred_schedule || "",
      Array.isArray(data.available_time_slots) ? JSON.stringify(data.available_time_slots) : data.available_time_slots || "",
      data.region || "",
      data.main_device || "",
      data.can_code ? 1 : 0,
      data.can_present ? 1 : 0,
      data.skills || data.preparedness || "",
      data.contribution || "",
      data.participation_grade || gradeCount(data),
      data.consent_personal ? 1 : 0,
      data.consent_marketing ? 1 : 0,
      timestamp,
      data.consent_version || "lead-upgrade-cloudflare-v1",
      memberId
    )
    .run();
  await env.DB.prepare(
    `UPDATE consultations
     SET status='closed',
         admin_note=COALESCE(admin_note, '강의 신청으로 전환됨'),
         updated_at=?
     WHERE member_id=? AND status NOT IN ('closed', 'spam')`
  )
    .bind(timestamp, memberId)
    .run();
  return Number(result?.meta?.changes || result?.changes || 0) > 0;
}

async function refreshDuplicateApplication(env, memberId, data, envSource = env) {
  const timestamp = now();
  const phone = normalizePhoneForStorage(data.phone || "");
  const email = String(data.email || "").trim().toLowerCase();
  const result = await env.DB.prepare(
    `UPDATE members
     SET name=?,
         email_encrypted=?,
         email_hash=?,
         phone_hash=?,
         phone_masked=?,
         phone_encrypted=?,
         gender=?,
         age=?,
         job=?,
         referral_source=?,
         reason=?,
         ai_level=?,
         plan_type=?,
         ai_tools=?,
         ai_subscription=?,
         ai_weekly_hours=?,
         ai_use_cases=?,
         group_goals=?,
         short_term_goal=?,
         participation_type=?,
         preferred_schedule=?,
         available_time_slots=?,
         region=?,
         main_device=?,
         can_code=?,
         can_present=?,
         skills=?,
         contribution=?,
         participation_grade=?,
         consent_personal=?,
         consent_marketing=?,
         consent_at=?,
         consent_version=?,
         status=CASE WHEN status='rejected' THEN 'pending' ELSE status END,
         rejection_reason=CASE WHEN status='rejected' THEN NULL ELSE rejection_reason END
     WHERE id=?`
  )
    .bind(
      data.name || "신청자",
      await encryptLegacyValue(email, envSource, "EMAIL_SECRET_KEY"),
      email ? await hmacHex(email, envSource, "EMAIL_SECRET_KEY") : "",
      phone ? await hmacHex(phone, envSource, "PHONE_SECRET_KEY") : "",
      maskPhone(phone),
      await encryptLegacyValue(phone, envSource, "PHONE_SECRET_KEY"),
      data.gender || "",
      Number(data.age || 0),
      data.job || "",
      data.referral_source || "",
      data.reason || data.desired_outcome || "",
      data.ai_level || "",
      data.plan_type || "full",
      Array.isArray(data.ai_tools) ? JSON.stringify(data.ai_tools) : data.ai_tools || "",
      data.ai_subscription || "",
      data.ai_weekly_hours || "",
      Array.isArray(data.ai_use_cases) ? JSON.stringify(data.ai_use_cases) : data.ai_use_cases || "",
      Array.isArray(data.group_goals) ? JSON.stringify(data.group_goals) : data.group_goals || "",
      data.short_term_goal || data.desired_outcome || "",
      data.participation_type || "",
      data.preferred_schedule || "",
      Array.isArray(data.available_time_slots) ? JSON.stringify(data.available_time_slots) : data.available_time_slots || "",
      data.region || "",
      data.main_device || "",
      data.can_code ? 1 : 0,
      data.can_present ? 1 : 0,
      data.skills || data.preparedness || "",
      data.contribution || "",
      data.participation_grade || gradeCount(data),
      data.consent_personal ? 1 : 0,
      data.consent_marketing ? 1 : 0,
      timestamp,
      data.consent_version || "duplicate-refresh-cloudflare-v1",
      memberId
    )
    .run();
  return Number(result?.meta?.changes || result?.changes || 0) > 0;
}

async function findMemberByPhone(env, phone) {
  for (const candidate of phoneCandidates(phone)) {
    const phoneHash = await hmacHex(candidate, env, "PHONE_SECRET_KEY");
    const member = await one(env, "SELECT * FROM members WHERE phone_hash=? ORDER BY created_at DESC LIMIT 1", phoneHash);
    if (member) return member;
  }
  return null;
}

async function findMemberByKakaoId(env, kakaoId) {
  const id = String(kakaoId || "").trim();
  if (!id) return null;
  return one(env, "SELECT * FROM members WHERE kakao_id=? AND status!='erased' ORDER BY kakao_connected_at DESC LIMIT 1", id);
}

async function linkMemberKakao(env, memberId, kakaoId, profile = {}) {
  const result = await env.DB.prepare(
    "UPDATE members SET kakao_id=?, kakao_profile=?, kakao_connected_at=? WHERE id=?"
  )
    .bind(String(kakaoId || ""), JSON.stringify(profile || {}), now(), memberId)
    .run();
  return Number(result?.meta?.changes || result?.changes || 0) > 0;
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
  if (String(data.plan_type || "") === "free") {
    // join-free.html 프론트 필수 검증과 동일 기준 — API 직접 호출 우회 방지
    const freeRegion = String(data.region || "").trim();
    if (!freeRegion) return fail(400, "무료강의 신청은 참여 가능 지역을 입력해야 합니다.");
    const freeSlots = (Array.isArray(data.available_time_slots) ? data.available_time_slots : [data.available_time_slots])
      .filter((slot) => String(slot || "").trim());
    if (!freeSlots.length) return fail(400, "무료강의 신청은 참여 가능 시간대를 최소 1개 선택해야 합니다.");
  }

  const email = String(data.email || "").trim().toLowerCase();
  const selectedSession = data.session_id ? await getSession(env, data.session_id) : null;
  if (selectedSession && !data.preferred_schedule) {
    data.preferred_schedule = [selectedSession.starts_at, selectedSession.location].filter(Boolean).join(" / ");
  }
  if (data.desired_outcome && !data.short_term_goal) data.short_term_goal = data.desired_outcome;
  if (data.preparedness && !data.skills) data.skills = data.preparedness;
  const duplicate = await findDuplicateMember(env, { phone: data.phone || phone, email });
  if (duplicate) {
    if (duplicate.status === "blacklist") return fail(409, "현재 신청할 수 없는 연락처입니다.");
    if (canUpgradeLeadToApplication(duplicate, data)) {
      data.participation_grade = gradeCount(data);
      data.consent_version = data.consent_version || "lead-upgrade-cloudflare-v1";
      const previousPlan = duplicate.plan_type || "";
      const upgraded = await upgradeLeadToApplication(env, duplicate.id, data);
      if (!upgraded) return fail(500, "기존 리드를 강의 신청으로 전환하지 못했습니다.");
      const upgradedMember = await one(env, "SELECT * FROM members WHERE id=?", duplicate.id);
      await logAction(env, duplicate.id, "duplicate_apply", JSON.stringify({
        source: duplicate.duplicate_source,
        converted: true,
        from_plan_type: previousPlan,
        to_plan_type: data.plan_type || "",
        attempt_name: data.name || "",
        attempt_phone_masked: maskPhone(phone),
        attempt_plan_type: data.plan_type || "",
        attempt_session_id: data.session_id || "",
      }), request);
      await logAction(env, duplicate.id, "lead_upgraded_to_apply", JSON.stringify({
        from_plan_type: previousPlan,
        to_plan_type: data.plan_type || "",
        from_label: leadSourceLabel(previousPlan),
        to_label: planTypeLabel(data.plan_type),
      }), request);
      let freeBooking = null;
      if (data.plan_type === "free" && data.session_id) {
        freeBooking = await maybeCreateFreeSessionBooking(env, upgradedMember, data.session_id, request);
        if (freeBooking?.error) return fail(freeBooking.status || 400, freeBooking.error);
      }
      const counts = await stats(env);
      const hermesStatus = await sendTelegram(
        env,
        applicationMessage(upgradedMember, counts, false, {
          ...data,
          phone_masked: maskPhone(phone),
          lead_upgrade_from: previousPlan,
        }),
        memberKeyboard(env, duplicate.id),
        "application"
      );
      await logAction(env, duplicate.id, "hermes_notify", hermesStatus, request);
      return json({
        ok: true,
        duplicate: false,
        upgraded_from_lead: true,
        previous_plan_type: previousPlan,
        message: `${leadSourceLabel(previousPlan)} 내역을 ${planTypeLabel(data.plan_type)} 신청으로 변경해 접수했습니다.`,
        member_id: duplicate.id,
        status: upgradedMember?.status || "pending",
        next_steps: [
          "운영자가 신청 내용을 확인한 뒤 승인 코드를 발급합니다.",
          "관리자 신청자/멤버 목록에서는 강의 신청자로 표시됩니다.",
          "무료강의 일정을 선택했다면 해당 일정 신청도 함께 연결됩니다.",
        ],
        booking_id: freeBooking?.booking_id || null,
        reservation: freeBooking?.booking ? safePublicBooking(freeBooking.booking) : null,
        payment: null,
      });
    }
    const previousPlan = duplicate.plan_type || "";
    let activeMember = duplicate;
    let refreshedApplication = false;
    if (canRefreshDuplicateApplication(duplicate, data)) {
      data.participation_grade = gradeCount(data);
      data.consent_version = data.consent_version || "duplicate-refresh-cloudflare-v1";
      refreshedApplication = await refreshDuplicateApplication(env, duplicate.id, data);
      if (!refreshedApplication) return fail(500, "기존 신청 정보를 최신 신청으로 갱신하지 못했습니다.");
      activeMember = await one(env, "SELECT * FROM members WHERE id=?", duplicate.id);
    }
    let freeBooking = null;
    if (data.plan_type === "free" && data.session_id) {
      freeBooking = await maybeCreateFreeSessionBooking(env, activeMember, data.session_id, request);
      if (freeBooking?.error) return fail(freeBooking.status || 400, freeBooking.error);
    }
    await logAction(env, duplicate.id, "duplicate_apply", JSON.stringify({
      source: duplicate.duplicate_source,
      refreshed: refreshedApplication,
      from_plan_type: previousPlan,
      to_plan_type: data.plan_type || "",
      attempt_name: data.name || "",
      attempt_phone_masked: maskPhone(phone),
      attempt_plan_type: data.plan_type || "",
      attempt_session_id: data.session_id || "",
    }), request);
    const counts = await stats(env);
    const hermesStatus = await sendTelegram(
      env,
      applicationMessage(activeMember, counts, true, { ...data, phone_masked: maskPhone(phone) }),
      memberKeyboard(env, duplicate.id),
      "application"
    );
    await logAction(env, duplicate.id, "duplicate_apply_notify", hermesStatus, request);
    return json({
      ok: true,
      duplicate: true,
      latest_application_refreshed: refreshedApplication,
      previous_plan_type: previousPlan,
      message: refreshedApplication
        ? `기존 신청 정보를 ${planTypeLabel(data.plan_type)} 기준으로 갱신했습니다.`
        : "이미 신청이 접수되어 있습니다. 기존 신청 상태를 기준으로 안내드릴게요.",
      member_id: duplicate.id,
      status: activeMember?.status || duplicate.status,
      next_steps: [
        "관리자 신청자 목록에서 최근 재신청 시간 기준으로 확인할 수 있습니다.",
        "무료강의 일정을 선택했다면 같은 일정에 중복 예약 없이 연결합니다.",
        "유료강의는 승인 코드 받은 뒤 예약자 확인 페이지에서 진행하세요.",
      ],
      booking_id: freeBooking?.booking_id || null,
      reservation: freeBooking?.booking ? safePublicBooking(freeBooking.booking) : null,
      payment: null,
    });
  }

  const phoneHash = await hmacHex(phone, env, "PHONE_SECRET_KEY");
  const emailHash = email ? await hmacHex(email, env, "EMAIL_SECRET_KEY") : "";

  const id = crypto.randomUUID();
  const created = now();
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
  let freeBooking = null;
  if (member.plan_type === "free" && member.session_id) {
    freeBooking = await maybeCreateFreeSessionBooking(env, createdMember, member.session_id, request);
    if (freeBooking?.error) return fail(freeBooking.status || 400, freeBooking.error);
  }
  const hermesStatus = await sendTelegram(
    env,
    applicationMessage(createdMember, await stats(env), false, member),
    memberKeyboard(env, id),
    "application"
  );
  await logAction(env, id, "hermes_notify", hermesStatus, request);
  return json({
    ok: true,
    message: freeBooking?.message || "신청이 접수되었습니다.",
    member_id: id,
    booking_id: freeBooking?.booking_id || null,
    next_steps: freeBooking ? [
      "선택한 무료강의 일정에 신청이 접수되었습니다.",
      "운영자가 무료강의 안내 멘트를 복사해 개별 안내할 수 있습니다.",
      "수업 후 운영자가 참여 완료/불참을 표시해 수강 이력에 반영합니다.",
    ] : [
      "운영자가 신청 내용을 확인한 뒤 승인 코드를 발급합니다.",
      "승인 코드를 받은 뒤 예약자 확인 페이지에서 원하는 일정을 예약합니다.",
      "입금 확인 후 자리가 확정됩니다.",
    ],
    reservation: freeBooking?.booking ? safePublicBooking(freeBooking.booking) : null,
    payment: null,
  });
}

async function handlePublicVerify(request, env) {
  const body = await readJson(request);
  const member = await findMemberByPhone(env, body.phone || "");
  if (!member) return fail(404, "신청 정보를 찾을 수 없습니다. 신청한 전화번호를 확인해주세요.");
  if (!(await accessCodeMatches(member, body.code, env))) return fail(400, "코드 확인에 실패했습니다.");
  if (member.status !== "approved") return fail(400, `현재 신청 상태는 ${member.status}입니다.`);
  return json({
    ok: true,
    data: await publicMemberDashboardPayload(env, member),
  });
}

async function handlePublicBooking(request, env) {
  const body = await readJson(request);
  const member = await one(env, "SELECT * FROM members WHERE id=?", body.member_id || "");
  if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
  if (member.status !== "approved") return fail(400, "승인된 신청자만 예약할 수 있습니다.");
  const kakaoSession = await readSignedCookie(request, env, KAKAO_SESSION_COOKIE);
  const kakaoMemberOk = Boolean(kakaoSession?.member_id && kakaoSession.member_id === member.id);
  if (body.code) {
    if (!(await accessCodeMatches(member, body.code, env))) return fail(400, "코드 확인에 실패했습니다.");
  } else if (kakaoMemberOk) {
    await logAction(env, member.id, "booking_kakao_verified", "", request);
  } else {
    return fail(400, "승인 코드 확인 또는 카카오 회원 로그인이 필요합니다.");
  }
  const session = await getSession(env, body.session_id || "");
  const [ok, reason] = sessionAcceptance(session);
  if (!ok) return fail(400, reason);
  const [eligible, eligibilityReason] = await studyMemberAcceptance(env, session, member.id);
  if (!eligible) return fail(403, eligibilityReason);
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
  const studySession = isStudySession(session);
  const amount = studySession ? Number(session.price_krw || 0) : Number(session.price_krw || DEFAULT_PRICE);
  const bookingId = await createBooking(env, {
    session_id: body.session_id,
    member_id: member.id,
    applicant_name: member.name,
    phone_masked: member.phone_masked,
    desired_outcome: body.desired_outcome || member.short_term_goal || member.reason || "",
    preparedness: body.preparedness || "",
    payment_status: studySession && amount === 0 ? "waived" : "not_sent",
    payment_amount_krw: amount,
  });
  await logAction(env, member.id, "booking_requested_public", `booking_id=${bookingId}`, request);
  const booking = await getBooking(env, bookingId);
  await sendTelegram(env, bookingMessage(booking, await stats(env), false), bookingKeyboard(env, bookingId), "booking");
  return json({ ok: true, message: studySession ? "스터디 참가 신청이 접수되었습니다." : "예약 신청이 접수되었습니다.", data: safePublicBooking(booking) });
}

async function handleKakaoStart(request, env) {
  const url = new URL(request.url);
  const nextPath = safeNextPath(url.searchParams.get("next"));
  if (!String(env.KAKAO_REST_API_KEY || "").trim()) {
    return redirectWithCookies(withKakaoStatus(nextPath, "not_configured"));
  }
  const state = crypto.randomUUID().replace(/-/g, "");
  const params = new URLSearchParams({
    response_type: "code",
    client_id: String(env.KAKAO_REST_API_KEY || "").trim(),
    redirect_uri: kakaoRedirectUri(env, request),
    state,
  });
  const stateCookie = await signedCookie({ state, next: nextPath, iat: now() }, env);
  return redirectWithCookies(`${KAKAO_AUTHORIZE_URL}?${params.toString()}`, [
    cookieHeader(KAKAO_STATE_COOKIE, stateCookie, 600, request),
  ]);
}

async function handleKakaoCallback(request, env) {
  const url = new URL(request.url);
  const statePayload = await readSignedCookie(request, env, KAKAO_STATE_COOKIE);
  const nextPath = safeNextPath(statePayload?.next);
  const cleanup = [deleteCookieHeader(KAKAO_STATE_COOKIE)];
  if (url.searchParams.get("error")) {
    return redirectWithCookies(withKakaoStatus(nextPath, "error"), cleanup);
  }
  if (!statePayload || statePayload.state !== url.searchParams.get("state") || !url.searchParams.get("code")) {
    return redirectWithCookies(withKakaoStatus(nextPath, "state_error"), cleanup);
  }
  if (!String(env.KAKAO_REST_API_KEY || "").trim()) {
    return redirectWithCookies(withKakaoStatus(nextPath, "not_configured"), cleanup);
  }

  const tokenBody = new URLSearchParams({
    grant_type: "authorization_code",
    client_id: String(env.KAKAO_REST_API_KEY || "").trim(),
    redirect_uri: kakaoRedirectUri(env, request),
    code: url.searchParams.get("code"),
  });
  if (String(env.KAKAO_CLIENT_SECRET || "").trim()) {
    tokenBody.set("client_secret", String(env.KAKAO_CLIENT_SECRET || "").trim());
  }

  let user;
  try {
    const tokenResponse = await fetch(KAKAO_TOKEN_URL, {
      method: "POST",
      headers: { "content-type": "application/x-www-form-urlencoded;charset=utf-8" },
      body: tokenBody.toString(),
    });
    if (!tokenResponse.ok) throw new Error(`token_${tokenResponse.status}`);
    const token = await tokenResponse.json();
    if (!token.access_token) throw new Error("missing_access_token");
    const userResponse = await fetch(KAKAO_USER_ME_URL, {
      headers: { authorization: `Bearer ${token.access_token}` },
    });
    if (!userResponse.ok) throw new Error(`user_${userResponse.status}`);
    user = await userResponse.json();
  } catch (error) {
    await logAction(env, "kakao", "kakao_login_failed", String(error?.message || error), request);
    return redirectWithCookies(withKakaoStatus(nextPath, "token_error"), cleanup);
  }

  const profile = kakaoProfilePayload(user);
  const kakaoId = profile.id || String(user?.id || "");
  const member = await findMemberByKakaoId(env, kakaoId);
  const sessionCookie = await signedCookie({
    kakao_id: kakaoId,
    member_id: member?.id || "",
    profile,
    iat: now(),
  }, env);
  await logAction(env, member?.id || "kakao", "kakao_login", member ? "linked=1" : "linked=0", request);
  return redirectWithCookies(withKakaoStatus(nextPath, member ? "linked" : "unmatched"), [
    ...cleanup,
    cookieHeader(KAKAO_SESSION_COOKIE, sessionCookie, KAKAO_SESSION_MAX_AGE, request),
  ]);
}

async function handleKakaoMe(request, env) {
  const session = await readSignedCookie(request, env, KAKAO_SESSION_COOKIE);
  if (!session?.kakao_id) return fail(401, "카카오 로그인이 필요합니다.");
  const member = session.member_id ? await one(env, "SELECT * FROM members WHERE id=?", session.member_id) : null;
  const kakao = kakaoPublicPayload(session, member);
  return json({
    ok: true,
    data: member ? await publicMemberDashboardPayload(env, member, kakao) : { kakao, member: null, bookings: [], reviews: [], progress: memberLevelProfile([], []) },
  });
}

async function handleKakaoLink(request, env) {
  const session = await readSignedCookie(request, env, KAKAO_SESSION_COOKIE);
  if (!session?.kakao_id) return fail(401, "카카오 로그인이 필요합니다.");
  const body = await readJson(request);
  const member = await findMemberByPhone(env, body.phone || "");
  if (!member) return fail(404, "신청 정보를 찾을 수 없습니다. 신청한 전화번호를 확인해주세요.");
  if (!(await accessCodeMatches(member, body.code, env))) return fail(400, "코드 확인에 실패했습니다.");
  if (member.status !== "approved") return fail(400, `현재 신청 상태는 ${member.status}입니다.`);
  const existing = await findMemberByKakaoId(env, session.kakao_id);
  if (existing && existing.id !== member.id) return fail(409, "이미 다른 회원 정보에 연결된 카카오 계정입니다.");
  const profile = session.profile && typeof session.profile === "object" ? session.profile : {};
  await linkMemberKakao(env, member.id, session.kakao_id, profile);
  const linked = await one(env, "SELECT * FROM members WHERE id=?", member.id);
  const sessionCookie = await signedCookie({ ...session, member_id: member.id, iat: now() }, env);
  const response = json({
    ok: true,
    message: "카카오 계정이 회원 정보와 연결되었습니다.",
    data: await publicMemberDashboardPayload(env, linked, { connected: true, linked: true, nickname: profile.nickname || "" }),
  });
  response.headers.append("set-cookie", cookieHeader(KAKAO_SESSION_COOKIE, sessionCookie, KAKAO_SESSION_MAX_AGE, request));
  await logAction(env, member.id, "kakao_linked", "", request);
  return response;
}

async function verifyPublicMemberAccess(request, env, body) {
  const member = await one(env, "SELECT * FROM members WHERE id=?", body.member_id || "");
  if (!member) return { response: fail(404, "회원 정보를 찾을 수 없습니다.") };
  if (member.status !== "approved") return { response: fail(400, "승인된 회원만 사용할 수 있습니다.") };
  const kakaoSession = await readSignedCookie(request, env, KAKAO_SESSION_COOKIE);
  const kakaoMemberOk = Boolean(kakaoSession?.member_id && kakaoSession.member_id === member.id);
  if (body.code) {
    if (!(await accessCodeMatches(member, body.code, env))) return { response: fail(400, "코드 확인에 실패했습니다.") };
  } else if (!kakaoMemberOk) {
    return { response: fail(400, "승인 코드 확인 또는 카카오 회원 로그인이 필요합니다.") };
  }
  return { member, kakaoMemberOk };
}

function cleanOpenchatNickname(value) {
  return String(value || "").replace(/\s+/g, " ").trim().slice(0, 40);
}

async function handleMemberProfileUpdate(request, env) {
  const body = await readJson(request);
  const access = await verifyPublicMemberAccess(request, env, body);
  if (access.response) return access.response;
  const nickname = cleanOpenchatNickname(body.openchat_nickname);
  await env.DB.prepare("UPDATE members SET openchat_nickname=? WHERE id=?")
    .bind(nickname, access.member.id)
    .run();
  await logAction(env, access.member.id, "member_profile_update", JSON.stringify({ fields: ["openchat_nickname"] }), request);
  const updated = await one(env, "SELECT * FROM members WHERE id=?", access.member.id);
  return json({ ok: true, message: "오픈톡 닉네임을 저장했습니다.", data: await publicMemberDashboardPayload(env, updated) });
}

async function handleMemberReviewCreate(request, env) {
  const body = await readJson(request);
  const access = await verifyPublicMemberAccess(request, env, body);
  if (access.response) return access.response;
  const booking = await getBooking(env, String(body.booking_id || ""));
  if (!booking || booking.member_id !== access.member.id) return fail(404, "수강 이력을 찾을 수 없습니다.");
  if (!completedBooking(booking)) return fail(400, "수강 완료된 강의만 후기를 작성할 수 있습니다.");
  const title = String(body.title || "").trim();
  const text = String(body.body || body.summary || "").trim();
  if (!title || !text) return fail(400, "후기 제목과 내용을 입력하세요.");
  const existing = await one(
    env,
    "SELECT id FROM review_entries WHERE member_id=? AND booking_id=? LIMIT 1",
    access.member.id,
    booking.id
  ).catch((error) => {
    if (String(error?.message || error).includes("no such column")) return null;
    throw error;
  });
  if (existing) return fail(409, "이미 이 수업에 작성한 후기가 있습니다. 운영자 검수 상태를 확인해 주세요.");
  const id = crypto.randomUUID();
  const created = now();
  await env.DB.prepare(
    `INSERT INTO review_entries (
      id, member_id, booking_id, instructor_id, class_title, class_date, title, summary, body, tags, image_urls,
      status, source, privacy_checked, featured, created_at, updated_at
    ) VALUES (?, ?, ?, NULL, ?, ?, ?, ?, ?, ?, ?, 'draft', 'member', 0, 0, ?, ?)`
  )
    .bind(
      id,
      access.member.id,
      booking.id,
      booking.session_title || "ARSEN 강의",
      String(booking.session_starts_at || booking.created_at || "").slice(0, 10),
      title,
      text.slice(0, 160),
      text,
      listText(["마이페이지", bookingKind(booking)]),
      "[]",
      created,
      created
    )
    .run();
  await logAction(env, access.member.id, "member_review_create", JSON.stringify({ review_id: id, booking_id: booking.id }), request);
  const updated = await one(env, "SELECT * FROM members WHERE id=?", access.member.id);
  return json({
    ok: true,
    message: "후기가 초안으로 저장되었습니다. 운영자 검수 후 공개할 수 있습니다.",
    data: await publicMemberDashboardPayload(env, updated),
  });
}

function handleKakaoLogout() {
  const response = json({ ok: true, message: "카카오 회원 세션을 종료했습니다." });
  response.headers.append("set-cookie", deleteCookieHeader(KAKAO_SESSION_COOKIE));
  return response;
}

async function telegramCallbackResult(env, data, request, callback = {}) {
  const parts = String(data || "").split(":");
  if (parts.length !== 3 || parts[0] !== "arsen") return "지원하지 않는 버튼입니다.";
  const [_, action, targetId] = parts;
  const callbackChatId = String(callback?.message?.chat?.id || env.TELEGRAM_ADMIN_CHAT_ID || "");
  const callbackThreadId = String(callback?.message?.message_thread_id || "");

  if (action === "noticestop") {
    const stopped = await stopKakaoNoticeJobs(env, targetId, request);
    await sendTelegramToChat(env, callbackChatId, `ARSEN 카톡 공지 긴급정지 요청 처리: ${stopped}개 작업`, null, "button", callbackThreadId);
    return "카톡 공지 긴급정지 요청 완료";
  }

  if (action === "noticeok" || action === "noticeno") {
    const state = await kakaoNoticeState(env);
    const current = (state.jobs || []).find((item) => item.id === targetId);
    if (current && !["pending_approval", "prepared"].includes(current.status)) return `현재 작업 상태는 ${current.status}입니다.`;
    if (action === "noticeok" && current && current.status === "prepared" && kakaoNoticeReadyCount(current) < 1) {
      return "발송 준비 완료 대상이 없어 승인할 수 없습니다.";
    }
    const job = updateKakaoNoticeJob(state, targetId, (item) => {
      if (!["pending_approval", "prepared"].includes(item.status)) return;
      item.status = action === "noticeok" ? "approved" : "rejected";
      item.approved_at = action === "noticeok" ? now() : "";
      item.rejected_at = action === "noticeno" ? now() : "";
      item.phase = action === "noticeok" ? "send" : item.phase;
    });
    if (!job) return "카톡 공지 작업을 찾지 못했습니다.";
    await saveKakaoNoticeState(env, state);
    await logAction(env, "system", action === "noticeok" ? "kakao_notice_job_approved" : "kakao_notice_job_rejected", targetId, request);
    if (action === "noticeok") {
      await sendTelegramToChat(
        env,
        callbackChatId,
        [
          "<b>ARSEN 카톡 공지 승인 완료</b>",
          `작업ID: <code>${htmlEscape(targetId)}</code>`,
          `대상: ${kakaoNoticeReadyCount(job) || Number(job.recipients?.length || 0)}명`,
          "맥에어 카톡 발송기가 준비 완료 대상만 가져가 전송을 시작합니다.",
          "중간에 멈추려면 /arsen_stop 또는 아래 긴급정지를 누르세요.",
        ].join("\n"),
        kakaoNoticeStopKeyboard(targetId),
        "button",
        callbackThreadId
      );
      return "카톡 공지 발송 승인 완료";
    }
    return "카톡 공지 작업 취소 완료";
  }

  if (action === "approve") {
    const member = await one(env, "SELECT * FROM members WHERE id=?", targetId);
    if (!member) return "신청자를 찾을 수 없습니다.";
    if (["blacklist", "erased", "rejected"].includes(member.status)) {
      return `현재 상태가 ${member.status}라 코드 발급을 중단했습니다.`;
    }
    const code = (await readableAccessCode(member, env)) || accessCode();
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
  if (payload.message) {
    const result = await handleTelegramMessage(env, payload.message, request);
    return json({ ok: true, message: result });
  }
  const callback = payload.callback_query || {};
  const message = await telegramCallbackResult(env, callback.data || "", request, callback);
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
  const free = await one(env, "SELECT COUNT(*) AS count FROM members WHERE plan_type='free' AND status!='erased'");
  const full = await one(env, "SELECT COUNT(*) AS count FROM members WHERE plan_type='full' AND status!='erased'");
  const basic = await one(env, "SELECT COUNT(*) AS count FROM members WHERE plan_type='basic' AND status!='erased'");
  const consultation = await one(env, "SELECT COUNT(*) AS count FROM members WHERE plan_type='consultation' AND status!='erased'");
  const leadEmail = await one(env, "SELECT COUNT(*) AS count FROM members WHERE plan_type='lead_email' AND status!='erased'");
  const leadPhone = await one(env, "SELECT COUNT(*) AS count FROM members WHERE plan_type='lead_phone' AND status!='erased'");
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
    free: Number(free?.count || 0),
    full: Number(full?.count || 0),
    basic: Number(basic?.count || 0),
    consultation: Number(consultation?.count || 0),
    lead_email: Number(leadEmail?.count || 0),
    lead_phone: Number(leadPhone?.count || 0),
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
  return ["free", "full", "basic", "consultation", "lead_email", "lead_phone"].includes(normalized) ? normalized : "";
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
  if (path === "/admin/launcher-status" && method === "GET") {
    return json({ ok: true, data: await adminLauncherStatusPayload(env, request) });
  }
  if (path === "/admin/yoonbot/release-status" && method === "GET") {
    return json({ ok: true, data: await adminYoonbotReleaseStatusPayload(env, request) });
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
  if (path === "/admin/kakao-notice/jobs" && method === "GET") {
    const url = new URL(request.url);
    return json(await kakaoNoticeJobsPayload(env, String(url.searchParams.get("status") || "").trim()));
  }
  if (parts[0] === "admin" && parts[1] === "kakao-notice" && parts[2] === "jobs" && parts[3]) {
    const jobId = parts[3];
    if (!parts[4] && method === "GET") return kakaoNoticeJobPayload(env, jobId);
    if (parts[4] === "claim" && method === "POST") return claimKakaoNoticeJob(env, jobId, request);
    if (parts[4] === "stop" && method === "POST") {
      const stopped = await stopKakaoNoticeJobs(env, jobId, request);
      return json({ ok: true, stopped });
    }
    if (parts[4] === "result" && method === "POST") return finishKakaoNoticeJob(env, jobId, await readJson(request), request);
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
  if (path === "/admin/consultations" && method === "GET") {
    const url = new URL(request.url);
    return json({
      ok: true,
      summary: await consultationSummary(env, String(url.searchParams.get("kind") || "").trim()),
      data: await listConsultations(env, {
        status: String(url.searchParams.get("status") || "").trim(),
        source: String(url.searchParams.get("source") || "").trim(),
        kind: String(url.searchParams.get("kind") || "").trim(),
      }),
    });
  }
  if (parts[0] === "admin" && parts[1] === "consultations" && parts[2]) {
    const consultationId = parts[2];
    if (!parts[3] && method === "GET") {
      const item = await getConsultationRow(env, consultationId);
      if (!item) return fail(404, "상담 접수를 찾을 수 없습니다.");
      return json({ ok: true, data: consultationPublic(item) });
    }
    if (parts[3] === "contact" && method === "GET") {
      const contact = await consultationContact(env, consultationId);
      if (!contact) return fail(404, "상담 접수를 찾을 수 없습니다.");
      await logAction(env, "system", "consultation_contact_view", consultationId, request);
      return json({ ok: true, data: contact });
    }
    if (parts[3] === "status" && method === "POST") {
      const result = await updateConsultationStatus(env, consultationId, await readJson(request));
      if (!result.ok) return fail(result.status || 400, result.message || "상담 상태 변경에 실패했습니다.");
      await logAction(env, "system", "consultation_status_update", `${consultationId}:${result.data.status}`, request);
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

  // ── Admin discount code routes ──────────────────────────────────────────────
  if (path === "/admin/yoonbot/discounts" && method === "GET") {
    const rows = await all(env, "SELECT * FROM yoonbot_discount_codes ORDER BY created_at DESC");
    const data = rows.map(discountRowPublic);
    return json({ ok: true, data, total: data.length });
  }
  if (path === "/admin/yoonbot/discounts" && method === "POST") {
    const body = await readJson(request);
    const result = await createDiscountCode(env, body);
    if (result.error) return fail(400, result.error);
    await logAction(env, "system", "yoonbot_discount_created", result.data.code, request);
    return json({ ok: true, data: result.data });
  }
  if (parts[0] === "admin" && parts[1] === "yoonbot" && parts[2] === "discounts" && parts[3] && parts[4] === "disable" && method === "POST") {
    const codeParam = normalizeDiscountCode(parts[3]);
    if (!codeParam) return fail(400, "할인 코드를 입력하세요.");
    const row = await one(env, "SELECT * FROM yoonbot_discount_codes WHERE code=?", codeParam);
    if (!row) return fail(400, "할인 코드를 찾을 수 없습니다.");
    const updated = licenseIso();
    await env.DB.prepare(
      "UPDATE yoonbot_discount_codes SET enabled=0, updated_at=? WHERE code=?"
    ).bind(updated, codeParam).run();
    const updatedRow = await one(env, "SELECT * FROM yoonbot_discount_codes WHERE code=?", codeParam);
    await logAction(env, "system", "yoonbot_discount_disabled", codeParam, request);
    return json({ ok: true, data: discountRowPublic(updatedRow) });
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
    const data = await membersWithAdminFields(env, rows);
    data.sort((a, b) => String(b.latest_activity_at || b.created_at || "").localeCompare(String(a.latest_activity_at || a.created_at || "")));
    return json({ ok: true, data, total: data.length });
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
  if (parts[0] === "admin" && parts[1] === "members" && parts[2] && !parts[3] && method === "PUT") {
    const body = await readJson(request);
    const member = await one(env, "SELECT id FROM members WHERE id=?", parts[2]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    const allowed = [
      "name", "gender", "age", "job", "referral_source", "reason", "ai_level", "plan_type",
      "ai_tools", "ai_subscription", "ai_weekly_hours", "ai_use_cases", "group_goals", "short_term_goal",
      "participation_type", "preferred_schedule", "available_time_slots", "region", "main_device",
      "can_code", "can_present", "skills", "contribution", "participation_grade", "openchat_nickname", "consent_marketing",
      "status", "rejection_reason",
    ];
    if (body.status && !["pending", "approved", "rejected", "blacklist", "erased"].includes(body.status)) return fail(400, "상태 값이 올바르지 않습니다.");
    if (body.plan_type && !["free", "full", "basic", "consultation", "lead_email", "lead_phone"].includes(body.plan_type)) return fail(400, "신청 유형 값이 올바르지 않습니다.");
    const fields = allowed.filter((key) => body[key] !== undefined);
    if (!fields.length) return fail(400, "변경할 값이 없습니다.");
    const values = fields.map((key) => {
      const value = body[key];
      if (["ai_tools", "ai_use_cases", "group_goals", "available_time_slots"].includes(key) && Array.isArray(value)) return JSON.stringify(value);
      if (["can_code", "can_present", "consent_marketing"].includes(key)) return value ? 1 : 0;
      return value == null ? "" : value;
    });
    await env.DB.prepare(`UPDATE members SET ${fields.map((key) => `${key}=?`).join(", ")} WHERE id=?`)
      .bind(...values, parts[2])
      .run();
    await logAction(env, parts[2], "member_update", JSON.stringify({ fields }), request);
    const updated = await one(env, "SELECT * FROM members WHERE id=?", parts[2]);
    const data = (await membersWithAdminFields(env, [updated]))[0] || safeMember(updated);
    return json({ ok: true, data });
  }
  if (parts[0] === "admin" && parts[1] === "members" && parts[2] && parts[3] === "contact-registered" && method === "POST") {
    const body = await readJson(request);
    const member = await one(env, "SELECT id FROM members WHERE id=?", parts[2]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    await logAction(env, parts[2], "contact_registered", JSON.stringify({
      registered: body.registered !== false,
      note: String(body.note || ""),
    }), request);
    const updated = await one(env, "SELECT * FROM members WHERE id=?", parts[2]);
    const data = (await membersWithAdminFields(env, [updated]))[0] || safeMember(updated);
    return json({ ok: true, data });
  }
  if (parts[0] === "admin" && parts[1] === "members" && parts[2] && parts[3] === "kakao-unlink" && method === "POST") {
    const member = await one(env, "SELECT id, kakao_id FROM members WHERE id=?", parts[2]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    if (!member.kakao_id) return fail(400, "연결된 카카오 계정이 없습니다.");
    await env.DB.prepare("UPDATE members SET kakao_id=NULL, kakao_profile=NULL, kakao_connected_at=NULL WHERE id=?")
      .bind(parts[2])
      .run();
    await logAction(env, parts[2], "kakao_unlinked_by_admin", "admin_manual_unlink", request);
    const updated = await one(env, "SELECT * FROM members WHERE id=?", parts[2]);
    const data = (await membersWithAdminFields(env, [updated]))[0] || safeMember(updated);
    return json({ ok: true, message: "카카오 계정 연결을 해제했습니다.", data });
  }
  if (parts[0] === "admin" && parts[1] === "members" && parts[2] && parts[3] === "kick" && method === "POST") {
    const body = await readJson(request);
    const member = await one(env, "SELECT id FROM members WHERE id=?", parts[2]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    const reason = String(body.reason || "운영자 강의 추방 처리").trim();
    const active = await all(
      env,
      "SELECT id, session_id, payment_note FROM bookings WHERE member_id=? AND status NOT IN ('canceled','rejected','no_show','completed')",
      parts[2]
    );
    for (const booking of active) {
      const note = [booking.payment_note, `[강의 추방] ${reason}`].filter(Boolean).join("\n");
      await env.DB.prepare("UPDATE bookings SET status='canceled', canceled_at=?, payment_note=?, updated_at=? WHERE id=?")
        .bind(now(), note, now(), booking.id)
        .run();
      await refreshSessionCount(env, booking.session_id);
    }
    await logAction(env, parts[2], "member_kicked_from_classes", JSON.stringify({ count: active.length, reason }), request);
    return json({ ok: true, message: `활성 강의 예약 ${active.length}건을 취소 처리했습니다.`, data: { member_id: parts[2], canceled: active.length } });
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
      const code = await readableAccessCode(member, env);
      return json({
        ok: true,
        data: {
          code,
          code_exists: Boolean(code),
          expires_at: null,
          issued_at: member.code_issued_at,
          expiry_label: "기한 없음",
          delivery_message: code ? codeDeliveryMessage(member, code, env) : "",
        },
      });
    }
    const member = await one(env, "SELECT * FROM members WHERE id=?", parts[1]);
    if (!member) return fail(404, "신청자를 찾을 수 없습니다.");
    const data = (await membersWithAdminFields(env, [member]))[0] || safeMember(member);
    return json({ ok: true, data });
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
        body.description || DEFAULT_DESCRIPTION,
        body.program_type || "ai_basic_setup",
        body.audience_level || "all",
        body.starts_at,
        body.ends_at,
        body.timezone || "Asia/Seoul",
        Number(body.capacity_min || 4),
        Number(body.capacity_max || 8),
        Number(body.price_krw == null || body.price_krw === "" ? DEFAULT_PRICE : body.price_krw),
        body.location || DEFAULT_LOCATION,
        body.materials || DEFAULT_MATERIALS,
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
            await env.DB.prepare("UPDATE sessions SET title=?, description=?, ends_at=?, location=?, materials=?, price_krw=?, capacity_min=4, capacity_max=8, status='open', updated_at=? WHERE id=?")
              .bind(DEFAULT_TITLE, DEFAULT_DESCRIPTION, endsAt, DEFAULT_LOCATION, DEFAULT_MATERIALS, DEFAULT_PRICE, now(), existing.id)
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
              ) VALUES (?, ?, ?, 'ai_basic_setup', 'all', ?, ?, 'Asia/Seoul', 4, 8, 0, ?, ?, ?, 'open', '', ?, ?)`
            )
              .bind(id, DEFAULT_TITLE, DEFAULT_DESCRIPTION, startsAt, endsAt, DEFAULT_PRICE, DEFAULT_LOCATION, DEFAULT_MATERIALS, created, created)
              .run();
            createdIds.push(id);
          }
        }
      }
      await logAction(env, "booking", "session_seed_default_sunday", `created=${createdIds.length},updated=${updatedIds.length}`, request);
      return json({ ok: true, created: createdIds.length, updated: updatedIds.length, total: createdIds.length + updatedIds.length, ids: [...createdIds, ...updatedIds] });
    }
    if (parts[2] === "seed-free-class") {
      const body = await readJson(request);
      const weeks = Math.max(1, Math.min(12, Number(body.weeks || 4)));
      const createdIds = [];
      const updatedIds = [];
      const kstNow = new Date(Date.now() + 9 * 60 * 60 * 1000);
      let daysUntilSaturday = (6 - kstNow.getUTCDay() + 7) % 7;
      if (daysUntilSaturday === 0) daysUntilSaturday = 7;
      const base = new Date(Date.UTC(kstNow.getUTCFullYear(), kstNow.getUTCMonth(), kstNow.getUTCDate() + daysUntilSaturday));
      for (let week = 0; week < weeks; week += 1) {
        const startKst = new Date(base.getTime() + week * 7 * 24 * 60 * 60 * 1000 + 10 * 60 * 60 * 1000);
        const endKst = new Date(startKst.getTime() + 2 * 60 * 60 * 1000);
        const startsAt = new Date(startKst.getTime() - 9 * 60 * 60 * 1000).toISOString();
        const endsAt = new Date(endKst.getTime() - 9 * 60 * 60 * 1000).toISOString();
        const existing = await one(env, "SELECT id FROM sessions WHERE starts_at=? AND program_type='free_class'", startsAt);
        if (existing) {
          await env.DB.prepare(
            `UPDATE sessions
             SET title=?, description=?, audience_level='beginner', ends_at=?, location=?, materials=?,
                 price_krw=0, capacity_min=1, capacity_max=20, status='open', updated_at=?
             WHERE id=?`
          )
            .bind(FREE_CLASS_TITLE, FREE_CLASS_DESCRIPTION, endsAt, FREE_CLASS_LOCATION, FREE_CLASS_MATERIALS, now(), existing.id)
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
            ) VALUES (?, ?, ?, 'free_class', 'beginner', ?, ?, 'Asia/Seoul', 1, 20, 0, 0, ?, ?, 'open', '', ?, ?)`
          )
            .bind(id, FREE_CLASS_TITLE, FREE_CLASS_DESCRIPTION, startsAt, endsAt, FREE_CLASS_LOCATION, FREE_CLASS_MATERIALS, created, created)
            .run();
          createdIds.push(id);
        }
      }
      await logAction(env, "booking", "session_seed_free_class", `created=${createdIds.length},updated=${updatedIds.length}`, request);
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
      const studySession = isStudySession(session);
      const freeSession = isFreeSession(session);
      const participationSession = studySession || freeSession;
      const manualNote = body.payment_note || (studySession ? "운영자 수동 추가: 스터디 참여 확정" : freeSession ? "운영자 수동 추가: 무료강의 확정" : "운영자 수동 추가: 입금 확인 완료");
      if (existing) {
        await env.DB.prepare("UPDATE bookings SET status='confirmed', payment_status=?, payment_note=?, confirmed_at=?, updated_at=? WHERE id=?")
          .bind(participationSession ? "waived" : "paid", manualNote, now(), now(), existing.id)
          .run();
        await refreshSessionCount(env, parts[2]);
        return json({ ok: true, message: studySession ? "이미 연결된 스터디 예약을 참여확정으로 변경했습니다. 자동 알림은 보내지 않았습니다." : freeSession ? "이미 연결된 무료강의 예약을 확정으로 변경했습니다. 자동 알림은 보내지 않았습니다." : "이미 연결된 예약을 입금확정으로 변경했습니다. 자동 알림은 보내지 않았습니다.", data: await getBooking(env, existing.id), member_id: member.id, reused_member: true, ...noSendDelivery("manual_booking") });
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
        payment_status: participationSession ? "waived" : "paid",
        payment_amount_krw: Number(body.payment_amount_krw == null || body.payment_amount_krw === "" ? (participationSession ? 0 : session.price_krw || DEFAULT_PRICE) : body.payment_amount_krw),
        payment_note: manualNote,
        confirmed_at: now(),
      });
      await logAction(env, member.id, "manual_booking_confirmed", `booking_id=${bookingId}`, request);
      return json({ ok: true, message: studySession ? "스터디 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다." : freeSession ? "무료강의 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다." : "입금확정 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다.", data: await getBooking(env, bookingId), member_id: member.id, reused_member: Boolean(body.member_id), ...noSendDelivery("manual_booking") });
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
    if (parts[3] === "free-guide" && method === "POST") {
      const booking = await getBooking(env, bookingId);
      if (!booking) return fail(404, "예약 신청을 찾을 수 없습니다.");
      return json({
        ok: true,
        message: "무료강의 안내 문구를 만들었습니다. 신청자에게 자동 전송하지 않았습니다.",
        free_guide: defaultFreeClassGuide(booking),
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
    const parts = path.split("/").filter(Boolean);
    if ((request.method === "GET" || request.method === "HEAD") && !isApiPath(path) && env.ASSETS) {
      let assetResponse;
      if (path === "/") {
        const indexUrl = new URL(request.url);
        indexUrl.pathname = "/index.html";
        assetResponse = await env.ASSETS.fetch(new Request(indexUrl, request));
      } else {
        assetResponse = await env.ASSETS.fetch(request);
      }
      if (path === "/frontend/admin" || path === "/frontend/admin.html") {
        const headers = new Headers(assetResponse.headers);
        headers.set("cache-control", "no-store, max-age=0");
        headers.set("pragma", "no-cache");
        return new Response(assetResponse.body, { status: assetResponse.status, statusText: assetResponse.statusText, headers });
      }
      return assetResponse;
    }
    let response;
    if (path === "/health") {
      response = json({ ok: true, service: "member-system-cloudflare", time: now() });
    } else if (path === "/api/daf/manifest" && request.method === "GET") {
      response = json(await launcherManifestPayload(env, request));
    } else if (path === "/api/daf/programs" && request.method === "GET") {
      response = json({
        schema_version: "arsen.launcher_manifest.v1",
        updated_at: "2026-06-17T14:30:00+09:00",
        served_at: now(),
        programs: LAUNCHER_PROGRAMS,
      });
    } else if (path === "/api/daf/notices" && request.method === "GET") {
      const audience = url.searchParams.get("audience") || "";
      const level = url.searchParams.get("level") || "";
      if (audience && !["launcher", "website"].includes(audience)) response = fail(422, "invalid_audience");
      else if (level && !["info", "warning", "critical"].includes(level)) response = fail(422, "invalid_level");
      else response = json({
        schema_version: "arsen.launcher_manifest.v1",
        updated_at: "2026-06-17T14:30:00+09:00",
        served_at: now(),
        notices: launcherNoticesPayload({ audience, level }),
      });
    } else if ((path === "/api/daf/launcher/release" || path === "/api/launcher/release") && request.method === "GET") {
      response = json(await launcherReleasePayload(env, request));
    } else if (path === `/api/daf/launcher/artifacts/${LAUNCHER_ARTIFACT_NAME}` && (request.method === "GET" || request.method === "HEAD")) {
      response = await launcherArtifactResponse(env, request);
    } else if (path === "/sessions" && request.method === "GET") {
      const url = new URL(request.url);
      const programType = String(url.searchParams.get("program_type") || "").toLowerCase();
      const rows = (await sessionRows(env, false)).filter((row) => !programType || String(row.program_type || "").toLowerCase() === programType);
      response = json({ ok: true, data: rows.map((row) => ({ ...row, payment_guide: undefined })), total: rows.length });
    } else if (path === "/study/sessions" && request.method === "GET") {
      const rows = (await sessionRows(env, false)).filter((row) => isStudySession(row));
      response = json({ ok: true, data: rows.map((row) => ({ ...row, payment_guide: undefined })), total: rows.length, workflow: "회원 확인 → 스터디 선택 → 참가 신청 → 운영자 확인" });
    } else if (path === "/apply" && request.method === "POST") {
      response = await handleApply(request, env);
    } else if (path === "/member/verify-code" && request.method === "POST") {
      response = await handlePublicVerify(request, env);
    } else if (path === "/member/profile" && request.method === "POST") {
      response = await handleMemberProfileUpdate(request, env);
    } else if (path === "/member/reviews" && request.method === "POST") {
      response = await handleMemberReviewCreate(request, env);
    } else if (path === "/member/bookings" && request.method === "POST") {
      response = await handlePublicBooking(request, env);
    } else if (
      parts[0] === "member" &&
      parts[1] === "bookings" &&
      parts[2] &&
      parts[3] === "payment-intent" &&
      request.method === "POST"
    ) {
      const bookingId = parts[2];
      const body = await readJson(request);
      const member = await one(env, "SELECT * FROM members WHERE id=?", body.member_id || "");
      if (!member || member.status !== "approved") response = fail(400, "승인된 신청자만 결제를 진행할 수 있습니다.");
      else if (!(await accessCodeMatches(member, body.code, env))) response = fail(400, "승인 코드 확인에 실패했습니다.");
      else {
        const result = await createOrReuseEducationOrder(env, bookingId, member.id);
        if (!result.ok) response = fail(result.status || 400, result.message || "결제 주문을 준비하지 못했습니다.");
        else {
          const booking = await getBooking(env, bookingId);
          if (result.already_paid) response = json({ ok: true, message: "이미 결제가 확인된 예약입니다.", data: result.data, booking: safePublicBooking(booking) });
          else {
            const payment = await educationPaymentPayload(env, result.data, booking?.session_title || "ARSEN 유료 강의");
            await logAction(env, member.id, "education_payment_intent_created", `booking_id=${bookingId}`, request);
            response = json({ ok: true, message: "결제 정보를 준비했습니다.", data: result.data, payment, booking: safePublicBooking(booking) });
          }
        }
      }
    } else if (
      parts[0] === "member" &&
      parts[1] === "education-orders" &&
      parts[2] &&
      parts[3] === "payments" &&
      parts[4] === "toss" &&
      parts[5] === "confirm" &&
      request.method === "POST"
    ) {
      const orderId = parts[2];
      const result = await confirmEducationTossPayment(env, orderId, await readJson(request));
      if (!result.ok) response = fail(result.status || 400, result.message || "결제 확인에 실패했습니다.");
      else {
        const order = await getEducationOrderRow(env, orderId);
        const booking = order ? await getBooking(env, order.booking_id) : null;
        await logAction(env, "system", "education_toss_payment_confirmed", orderId, request);
        response = json({ ...result, booking: safePublicBooking(booking) });
      }
    } else if (path === "/auth/kakao/start" && request.method === "GET") {
      response = await handleKakaoStart(request, env);
    } else if (path === "/auth/kakao/callback" && request.method === "GET") {
      response = await handleKakaoCallback(request, env);
    } else if (path === "/auth/kakao/me" && request.method === "GET") {
      response = await handleKakaoMe(request, env);
    } else if (path === "/auth/kakao/link" && request.method === "POST") {
      response = await handleKakaoLink(request, env);
    } else if (path === "/auth/kakao/logout" && request.method === "POST") {
      response = handleKakaoLogout();
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
    } else if (path === "/api/consultations" && request.method === "POST") {
      const result = await createConsultation(env, await readJson(request), request);
      response = result.response || json(result);
    } else if (path === "/api/license/activate" && request.method === "POST") {
      response = json(await activateLicense(env, await readJson(request), request));
    } else if (path === "/api/license/verify" && request.method === "POST") {
      const token = bearerToken(request);
      response = token
        ? json(await verifyLicense(env, await readJson(request), request, token))
        : fail(401, "라이선스 인증 토큰이 필요합니다.");
    } else if (path === "/api/yoonbot/manifest" && request.method === "GET") {
      response = json(await yoonbotManifestPayload(env, request));
    } else if (path === "/api/yoonbot/release" && request.method === "GET") {
      response = json(await yoonbotReleasePayload(env, request));
    } else if (path === `/api/yoonbot/artifacts/${YOONBOT_ARTIFACT_NAME}` && (request.method === "GET" || request.method === "HEAD")) {
      response = await yoonbotArtifactResponse(env, request);
    } else if (path.startsWith("/api/yoonbot/artifacts/") && (request.method === "GET" || request.method === "HEAD")) {
      response = fail(404, "yoonbot_artifact_missing");
    } else if (path === "/api/yoonbot/products" && request.method === "GET") {
      response = json({ ok: true, ...yoonbotProducts(env) });
    } else if (path === "/api/yoonbot/orders" && request.method === "POST") {
      const result = await createYoonbotOrder(env, await readJson(request));
      if (result.response) response = result.response;
      else {
        await logAction(env, "system", "yoonbot_order_created", result.data.id, request);
        response = json(result);
      }
    } else if (
      parts[0] === "api" &&
      parts[1] === "yoonbot" &&
      parts[2] === "orders" &&
      parts[3] === "by-toss-id" &&
      parts[4] &&
      parts[5] === "payments" &&
      parts[6] === "toss" &&
      parts[7] === "confirm" &&
      request.method === "POST"
    ) {
      const tossOrderId = parts[4];
      const body = await readJson(request);
      const result = await confirmTossPaymentByTossId(env, tossOrderId, body);
      if (!result.ok) response = fail(result.status || 400, result.message || "결제 확인에 실패했습니다.");
      else {
        await logAction(env, "system", "yoonbot_toss_payment_confirmed", tossOrderId, request);
        response = json(result);
      }
    } else if (
      parts[0] === "api" &&
      parts[1] === "yoonbot" &&
      parts[2] === "orders" &&
      parts[3] &&
      parts[4] === "payments" &&
      parts[5] === "toss" &&
      parts[6] === "confirm" &&
      request.method === "POST"
    ) {
      const internalOrderId = parts[3];
      const body = await readJson(request);
      const result = await confirmTossPayment(env, internalOrderId, body);
      if (!result.ok) response = fail(result.status || 400, result.message || "결제 확인에 실패했습니다.");
      else {
        await logAction(env, "system", "yoonbot_toss_payment_confirmed", internalOrderId, request);
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
