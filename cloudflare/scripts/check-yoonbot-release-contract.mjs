import { handleRequest } from "../src/worker.js";

const EXPECTED_ARTIFACT = "yoonbot-1.1.0-win-x64.exe";
const EXPECTED_ENDPOINT = `/api/yoonbot/artifacts/${EXPECTED_ARTIFACT}`;
const EXPECTED_CONTENT_TYPE = "application/vnd.microsoft.portable-executable";
const TEST_SHA256 = "a".repeat(64);
const EXTERNAL_URL = `https://downloads.example.test/${EXPECTED_ARTIFACT}`;
const LAUNCHER_ARTIFACT = "arsen-content-launcher-0.1.0-win-x64.zip";
const LAUNCHER_SHA256 = "3B0AB1E9A2295BC45757848C28EF96F6885CC7D5AFEA790DF8AAC8A25808FA75";

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function request(path, env = {}, init = {}) {
  const response = await handleRequest(new Request(`https://apply.arsen-ai.com${path}`, init), env);
  const body = await response.json().catch(() => null);
  return { response, body };
}

function assertClosedRelease(release, label) {
  assert(release?.download_ready === false, `${label}: download_ready must be false`);
  assert(release?.artifact_download_url === "", `${label}: artifact_download_url must be empty`);
  assert(release?.sha256 === "", `${label}: sha256 must be empty`);
  assert(Number(release?.size_bytes) === 0, `${label}: size_bytes must be 0`);
}

function assertReleaseShape(release, label) {
  assert(release?.latest_version === "1.1.0", `${label}: latest_version mismatch`);
  assert(release?.minimum_supported_version === "1.0.0", `${label}: minimum_supported_version mismatch`);
  assert(release?.artifact_name === EXPECTED_ARTIFACT, `${label}: artifact_name mismatch`);
  assert(!release.artifact_name.includes("/") && !release.artifact_name.includes("\\"), `${label}: artifact_name must be a basename`);
  assert(release.artifact_name.endsWith(".exe"), `${label}: artifact_name must be an exe`);
  assert(Array.isArray(release?.release_notes) && release.release_notes.length > 0, `${label}: release_notes missing`);
}

// 1) Public manifest without auth, no artifact configured: 200 + fail-closed.
const closedManifest = await request("/api/yoonbot/manifest", { ADMIN_API_KEY: "some-admin-key" });
assert(closedManifest.response.status === 200, "yoonbot manifest must be public (no auth)");
assert(typeof closedManifest.body?.server_time === "string" && closedManifest.body.server_time.length > 0, "yoonbot manifest must include server_time");
assert(Array.isArray(closedManifest.body?.notices), "yoonbot manifest must include notices array");
assertReleaseShape(closedManifest.body?.release, "closed manifest");
assertClosedRelease(closedManifest.body?.release, "closed manifest");

// 2) Public release without auth, no artifact: fail-closed.
const closedRelease = await request("/api/yoonbot/release", { ADMIN_API_KEY: "some-admin-key" });
assert(closedRelease.response.status === 200, "yoonbot release must be public (no auth)");
assertReleaseShape(closedRelease.body, "closed release");
assertClosedRelease(closedRelease.body, "closed release");

// 3) Explicit verified HTTPS URL + sha256 + size: download ready.
const externalEnv = {
  YOONBOT_ARTIFACT_DOWNLOAD_URL: EXTERNAL_URL,
  YOONBOT_ARTIFACT_SHA256: TEST_SHA256.toUpperCase(),
  YOONBOT_ARTIFACT_SIZE_BYTES: "12345",
};
const externalRelease = await request("/api/yoonbot/release", externalEnv);
assert(externalRelease.body?.download_ready === true, "external release must be ready");
assert(externalRelease.body?.artifact_download_url === EXTERNAL_URL, "external release URL mismatch");
assert(externalRelease.body?.sha256 === TEST_SHA256, "external release sha256 must be normalized 64-hex");
assert(Number(externalRelease.body?.size_bytes) === 12345, "external release size mismatch");

const externalArtifact = await handleRequest(new Request(`https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`), externalEnv);
assert(externalArtifact.status === 302, "external artifact must redirect");
assert(externalArtifact.headers.get("location") === EXTERNAL_URL, "external artifact redirect URL mismatch");

// 4) Explicit URL without a valid sha256/size: fail-closed, no partial trust.
const badExternal = await request("/api/yoonbot/release", { YOONBOT_ARTIFACT_DOWNLOAD_URL: EXTERNAL_URL });
assertClosedRelease(badExternal.body, "external without sha256");
const httpExternal = await request("/api/yoonbot/release", {
  YOONBOT_ARTIFACT_DOWNLOAD_URL: `http://downloads.example.test/${EXPECTED_ARTIFACT}`,
  YOONBOT_ARTIFACT_SHA256: TEST_SHA256,
  YOONBOT_ARTIFACT_SIZE_BYTES: "12345",
});
assertClosedRelease(httpExternal.body, "non-https external URL");

// 5) No storage configured: artifact endpoint fails closed.
const noStorage = await request(EXPECTED_ENDPOINT);
assert(noStorage.response.status === 503, "yoonbot artifact without storage must return 503");

// 6) Unknown artifact names / traversal-shaped names: 404, never served.
const unknownName = await request("/api/yoonbot/artifacts/other-app-9.9.9.exe");
assert(unknownName.response.status === 404, "unknown yoonbot artifact name must return 404");
const traversal = await handleRequest(
  new Request(`https://apply.arsen-ai.com/api/yoonbot/artifacts/..%2f..%2fsecret.exe`),
  { YOONBOT_RELEASES: { async head() { throw new Error("must not touch R2"); }, async get() { throw new Error("must not touch R2"); } } },
);
assert([400, 404].includes(traversal.status), "traversal-shaped yoonbot artifact name must be rejected");

// 7) R2-backed artifact with sha256 custom metadata: ready + GET/HEAD served.
const r2Bytes = new Uint8Array([9, 8, 7]);
const fakeYoonbotR2 = {
  async head(key) {
    assert(key === EXPECTED_ARTIFACT, "yoonbot R2 head key mismatch");
    return { size: r2Bytes.length, customMetadata: { sha256: TEST_SHA256 } };
  },
  async get(key) {
    assert(key === EXPECTED_ARTIFACT, "yoonbot R2 get key mismatch");
    return {
      size: r2Bytes.length,
      httpEtag: '"yoonbot-etag"',
      body: r2Bytes,
      writeHttpMetadata() {},
    };
  },
};
const r2Release = await request("/api/yoonbot/release", { YOONBOT_RELEASES: fakeYoonbotR2 });
assert(r2Release.body?.download_ready === true, "R2 release must be ready");
assert(r2Release.body?.artifact_download_url === `https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`, "R2 release URL mismatch");
assert(r2Release.body?.sha256 === TEST_SHA256, "R2 release sha256 mismatch");
assert(Number(r2Release.body?.size_bytes) === r2Bytes.length, "R2 release size mismatch");

const r2Artifact = await handleRequest(new Request(`https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`), { YOONBOT_RELEASES: fakeYoonbotR2 });
assert(r2Artifact.status === 200, "R2 yoonbot artifact GET must return 200");
assert(r2Artifact.headers.get("content-type") === EXPECTED_CONTENT_TYPE, "R2 yoonbot artifact content-type mismatch");
assert((r2Artifact.headers.get("content-disposition") || "").includes(`attachment; filename="${EXPECTED_ARTIFACT}"`), "R2 yoonbot artifact must be an attachment");
assert(r2Artifact.headers.get("x-content-type-options") === "nosniff", "R2 yoonbot artifact must set nosniff");
assert(r2Artifact.headers.get("content-length") === String(r2Bytes.length), "R2 yoonbot artifact content-length mismatch");

const r2Head = await handleRequest(new Request(`https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`, { method: "HEAD" }), { YOONBOT_RELEASES: fakeYoonbotR2 });
assert(r2Head.status === 200, "R2 yoonbot artifact HEAD must return 200");
assert(r2Head.headers.get("content-length") === String(r2Bytes.length), "R2 yoonbot artifact HEAD content-length mismatch");

// 8) R2 object without verified sha256 metadata: manifest stays fail-closed.
const unverifiedR2 = {
  async head() {
    return { size: r2Bytes.length, customMetadata: {} };
  },
  async get() {
    return { size: r2Bytes.length, body: r2Bytes, writeHttpMetadata() {} };
  },
};
const unverifiedRelease = await request("/api/yoonbot/release", { YOONBOT_RELEASES: unverifiedR2 });
assertClosedRelease(unverifiedRelease.body, "R2 without sha256 metadata");

// 9) Bundled asset chunks: ready + streamed GET and HEAD.
const chunkA = new Uint8Array([1, 2]);
const chunkB = new Uint8Array([3]);
const fakeAssets = {
  async fetch(assetRequest) {
    const path = new URL(assetRequest.url).pathname;
    if (path === `/yoonbot-artifacts/${EXPECTED_ARTIFACT}.manifest.json`) {
      return new Response(JSON.stringify({
        artifact_name: EXPECTED_ARTIFACT,
        size_bytes: 3,
        sha256: TEST_SHA256,
        chunks: [
          { path: `/yoonbot-artifacts/${EXPECTED_ARTIFACT}.part-000`, size_bytes: 2 },
          { path: `/yoonbot-artifacts/${EXPECTED_ARTIFACT}.part-001`, size_bytes: 1 },
        ],
      }), { headers: { "content-type": "application/json" } });
    }
    if (path === `/yoonbot-artifacts/${EXPECTED_ARTIFACT}.part-000`) return new Response(chunkA);
    if (path === `/yoonbot-artifacts/${EXPECTED_ARTIFACT}.part-001`) return new Response(chunkB);
    return new Response("not found", { status: 404 });
  },
};
const assetRelease = await request("/api/yoonbot/release", { ASSETS: fakeAssets });
assert(assetRelease.body?.download_ready === true, "asset release must be ready");
assert(assetRelease.body?.artifact_download_url === `https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`, "asset release URL mismatch");
assert(assetRelease.body?.sha256 === TEST_SHA256, "asset release sha256 mismatch");

const assetArtifact = await handleRequest(new Request(`https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`), { ASSETS: fakeAssets });
assert(assetArtifact.status === 200, "asset yoonbot artifact GET must return 200");
assert(assetArtifact.headers.get("content-type") === EXPECTED_CONTENT_TYPE, "asset yoonbot artifact content-type mismatch");
assert(assetArtifact.headers.get("x-content-type-options") === "nosniff", "asset yoonbot artifact must set nosniff");
const assetBytes = new Uint8Array(await assetArtifact.arrayBuffer());
assert(assetBytes.length === 3 && assetBytes[0] === 1 && assetBytes[2] === 3, "asset yoonbot artifact bytes mismatch");

const assetHead = await handleRequest(new Request(`https://apply.arsen-ai.com${EXPECTED_ENDPOINT}`, { method: "HEAD" }), { ASSETS: fakeAssets });
assert(assetHead.status === 200, "asset yoonbot artifact HEAD must return 200");
assert(assetHead.headers.get("content-length") === "3", "asset yoonbot artifact HEAD content-length mismatch");

// 10) Non-https origin never advertises a self download URL.
const httpOrigin = await handleRequest(new Request(`http://localhost:8787/api/yoonbot/release`), { YOONBOT_RELEASES: fakeYoonbotR2 });
const httpOriginBody = await httpOrigin.json();
assertClosedRelease(httpOriginBody, "http origin release");

// 11) Launcher contract regression: yoonbot config must not leak into launcher,
//     and launcher config must not open the yoonbot contract.
const launcherRelease = await request("/api/launcher/release", externalEnv);
assert(launcherRelease.response.status === 200, "launcher release must still return 200");
assert(launcherRelease.body?.artifact_name === LAUNCHER_ARTIFACT, "launcher artifact name must stay the ZIP");
assert(launcherRelease.body?.sha256 === LAUNCHER_SHA256, "launcher sha256 must be unchanged");
assert(launcherRelease.body?.artifact_available === false, "yoonbot env must not make launcher artifact available");
assert(launcherRelease.body?.artifact_download_url === "", "yoonbot env must not set launcher download URL");

const yoonbotWithLauncherEnv = await request("/api/yoonbot/release", {
  LAUNCHER_ARTIFACT_DOWNLOAD_URL: `https://downloads.example.test/${LAUNCHER_ARTIFACT}`,
});
assertClosedRelease(yoonbotWithLauncherEnv.body, "launcher env must not open yoonbot release");

console.log("yoonbot release contract ok");
