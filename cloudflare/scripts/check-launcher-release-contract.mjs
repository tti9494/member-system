import { handleRequest } from "../src/worker.js";

const EXPECTED_SHA256 = "3B0AB1E9A2295BC45757848C28EF96F6885CC7D5AFEA790DF8AAC8A25808FA75";
const EXPECTED_ARTIFACT = "arsen-content-launcher-0.1.0-win-x64.zip";
const ARTIFACT_URL = `https://downloads.example.test/${EXPECTED_ARTIFACT}`;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function request(path, env = {}) {
  const response = await handleRequest(new Request(`https://apply.arsen-ai.com${path}`), env);
  const body = await response.json().catch(() => null);
  return { response, body };
}

async function adminRequest(path, env = {}) {
  const response = await handleRequest(
    new Request(`https://apply.arsen-ai.com${path}`, { headers: { "x-admin-key": "test-admin-key" } }),
    { ADMIN_API_KEY: "test-admin-key", ...env },
  );
  const body = await response.json().catch(() => null);
  return { response, body };
}

const manifest = await request("/api/daf/manifest", {
  LAUNCHER_ARTIFACT_DOWNLOAD_URL: ARTIFACT_URL,
});
assert(manifest.response.status === 200, "launcher manifest must return 200");
assert(manifest.body?.schema_version === "arsen.launcher_manifest.v1", "launcher manifest schema mismatch");
assert(Array.isArray(manifest.body?.programs) && manifest.body.programs.length === 4, "launcher manifest must expose 4 customer programs");
assert(Array.isArray(manifest.body?.notices) && manifest.body.notices.length === 3, "launcher manifest must expose 3 launcher notices");
assert(!manifest.body.programs.some((program) => program.internal_only), "launcher manifest must not expose internal programs");
assert(!manifest.body.programs.some((program) => program.id === "launcher-studio"), "launcher manifest must hide launcher-studio");
assert(!manifest.body.tiers.some((tier) => tier.id === "owner" || tier.internal_only), "launcher manifest must hide owner tier");

const release = await request("/api/launcher/release", {
  LAUNCHER_ARTIFACT_DOWNLOAD_URL: ARTIFACT_URL,
});
assert(release.response.status === 200, "launcher release must return 200");
assert(release.body?.version === "0.1.0", "launcher release version mismatch");
assert(release.body?.artifact_name === EXPECTED_ARTIFACT, "launcher artifact name mismatch");
assert(release.body?.artifact_download_url === ARTIFACT_URL, "launcher artifact download URL mismatch");
assert(release.body?.artifact_available === true, "launcher artifact should be available when URL is configured");
assert(release.body?.sha256 === EXPECTED_SHA256, "launcher SHA-256 mismatch");
assert(Number(release.body?.size_bytes) === 147951169, "launcher artifact size mismatch");

const noArtifactRelease = await request("/api/launcher/release");
assert(noArtifactRelease.response.status === 200, "launcher release without artifact URL must still return 200");
assert(noArtifactRelease.body?.artifact_download_url === "", "launcher release must not invent artifact URL without config");
assert(noArtifactRelease.body?.artifact_available === false, "launcher artifact must be unavailable without config");

const artifactRedirect = await handleRequest(
  new Request(`https://apply.arsen-ai.com/api/daf/launcher/artifacts/${EXPECTED_ARTIFACT}`),
  { LAUNCHER_ARTIFACT_DOWNLOAD_URL: ARTIFACT_URL },
);
assert(artifactRedirect.status === 302, "launcher artifact endpoint should redirect to configured storage URL");
assert(artifactRedirect.headers.get("location") === ARTIFACT_URL, "launcher artifact redirect URL mismatch");

const artifactUnavailable = await request(`/api/daf/launcher/artifacts/${EXPECTED_ARTIFACT}`);
assert(artifactUnavailable.response.status === 503, "launcher artifact endpoint must fail closed without storage URL");

const fakeR2 = {
  async get(key) {
    assert(key === EXPECTED_ARTIFACT, "launcher R2 key mismatch");
    return {
      size: 3,
      httpEtag: '"fake-etag"',
      body: new Uint8Array([1, 2, 3]),
      writeHttpMetadata(headers) {
        headers.set("content-type", "application/zip");
      },
    };
  },
};

const r2Release = await request("/api/launcher/release", { LAUNCHER_RELEASES: fakeR2 });
assert(r2Release.body?.artifact_available === true, "launcher release should be available when R2 binding exists");
assert(
  r2Release.body?.artifact_download_url === `https://apply.arsen-ai.com/api/daf/launcher/artifacts/${EXPECTED_ARTIFACT}`,
  "launcher R2 artifact URL mismatch",
);

const r2Artifact = await handleRequest(
  new Request(`https://apply.arsen-ai.com/api/daf/launcher/artifacts/${EXPECTED_ARTIFACT}`),
  { LAUNCHER_RELEASES: fakeR2 },
);
assert(r2Artifact.status === 200, "launcher R2 artifact endpoint should return 200");
assert(r2Artifact.headers.get("content-type") === "application/zip", "launcher R2 artifact content type mismatch");
assert(r2Artifact.headers.get("content-length") === "3", "launcher R2 artifact content length mismatch");

const fakeAssets = {
  async fetch(request) {
    const path = new URL(request.url).pathname;
    if (path === `/launcher-artifacts/${EXPECTED_ARTIFACT}.manifest.json`) {
      return new Response(JSON.stringify({
        artifact_name: EXPECTED_ARTIFACT,
        size_bytes: 147951169,
        sha256: EXPECTED_SHA256,
        chunks: [{ path: `/launcher-artifacts/${EXPECTED_ARTIFACT}.part-000`, size_bytes: 3 }],
      }), { headers: { "content-type": "application/json" } });
    }
    if (path === `/launcher-artifacts/${EXPECTED_ARTIFACT}.part-000`) {
      return new Response(new Uint8Array([1, 2, 3]));
    }
    return new Response("not found", { status: 404 });
  },
};

const assetRelease = await request("/api/launcher/release", { ASSETS: fakeAssets });
assert(assetRelease.body?.artifact_available === true, "launcher release should be available when bundled asset chunks exist");
assert(
  assetRelease.body?.artifact_download_url === `https://apply.arsen-ai.com/api/daf/launcher/artifacts/${EXPECTED_ARTIFACT}`,
  "launcher bundled asset URL mismatch",
);
const assetHead = await handleRequest(
  new Request(`https://apply.arsen-ai.com/api/daf/launcher/artifacts/${EXPECTED_ARTIFACT}`, { method: "HEAD" }),
  { ASSETS: fakeAssets },
);
assert(assetHead.status === 200, "launcher bundled asset HEAD should return 200");
assert(assetHead.headers.get("content-type") === "application/zip", "launcher bundled asset content type mismatch");
assert(assetHead.headers.get("content-length") === "147951169", "launcher bundled asset content length mismatch");

const adminStatus = await adminRequest("/admin/launcher-status", { ASSETS: fakeAssets });
assert(adminStatus.response.status === 200, "launcher admin status must return 200");
assert(adminStatus.body?.ok === true, "launcher admin status must be wrapped in ok=true");
assert(adminStatus.body?.data?.release?.version === "0.1.0", "launcher admin status release version mismatch");
assert(adminStatus.body?.data?.metrics?.customer_programs === 4, "launcher admin status customer program count mismatch");
assert(adminStatus.body?.data?.metrics?.notices_total === 3, "launcher admin status notice count mismatch");
assert(adminStatus.body?.data?.checks?.artifact_available === true, "launcher admin status artifact check mismatch");
assert(adminStatus.body?.data?.endpoints?.manifest === "/api/daf/manifest", "launcher admin status manifest endpoint mismatch");

console.log("launcher release contract ok");
