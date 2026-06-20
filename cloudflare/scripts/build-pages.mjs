import { createReadStream } from "node:fs";
import { cp, mkdir, open, rm, stat, writeFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const sourceFrontend = resolve(root, "..", "frontend");
const dist = resolve(root, "dist");
const checkOnly = process.argv.includes("--check");
const skipLauncherArtifact = ["1", "true", "yes"].includes(String(process.env.MEMBER_SYSTEM_SKIP_LAUNCHER_ARTIFACT || "").trim().toLowerCase());
const launcherArtifactName = "arsen-content-launcher-0.1.0-win-x64.zip";
const launcherArtifactSource = `/Users/yoon/.arsen-work-bus/artifacts/launcher/${launcherArtifactName}`;
const launcherArtifactExpectedSize = 147951169;
const launcherArtifactExpectedSha256 = "3B0AB1E9A2295BC45757848C28EF96F6885CC7D5AFEA790DF8AAC8A25808FA75";
const launcherArtifactChunkSize = 20 * 1024 * 1024;
const frontendHtmlFiles = [
  "admin.html",
  "class-dashboard.html",
  "class-stories.html",
  "education.html",
  "join-basic.html",
  "join-free.html",
  "join-full.html",
  "license-admin.html",
  "member.html",
  "payment-admin.html",
  "privacy.html",
  "review-submit.html",
  "status.html",
  "yoonbot.html",
];
const frontendAssetFiles = [
  "arsen-theme.css",
  "theme-loader.js",
  "yoonbot-hero.png",
  "themes/arsen-modern.css",
  "themes/legacy.css",
];

async function exists(path) {
  try {
    await stat(path);
    return true;
  } catch (_) {
    return false;
  }
}

async function sha256File(path) {
  return new Promise((resolveHash, reject) => {
    const hash = createHash("sha256");
    createReadStream(path)
      .on("data", (chunk) => hash.update(chunk))
      .on("error", reject)
      .on("end", () => resolveHash(hash.digest("hex").toUpperCase()));
  });
}

async function verifyLauncherArtifactSource() {
  if (skipLauncherArtifact) return null;
  if (!(await exists(launcherArtifactSource))) {
    throw new Error(`Missing launcher artifact: ${launcherArtifactSource}`);
  }
  const info = await stat(launcherArtifactSource);
  if (info.size !== launcherArtifactExpectedSize) {
    throw new Error(`Launcher artifact size mismatch: expected ${launcherArtifactExpectedSize}, got ${info.size}`);
  }
  const sha256 = await sha256File(launcherArtifactSource);
  if (sha256 !== launcherArtifactExpectedSha256) {
    throw new Error(`Launcher artifact sha256 mismatch: expected ${launcherArtifactExpectedSha256}, got ${sha256}`);
  }
  return { size: info.size, sha256 };
}

async function writeLauncherArtifactChunks(sourceInfo) {
  if (skipLauncherArtifact || !sourceInfo) return;
  const artifactDir = resolve(dist, "launcher-artifacts");
  await mkdir(artifactDir, { recursive: true });
  const handle = await open(launcherArtifactSource, "r");
  const chunks = [];
  let offset = 0;
  let index = 0;
  try {
    while (offset < sourceInfo.size) {
      const length = Math.min(launcherArtifactChunkSize, sourceInfo.size - offset);
      const buffer = Buffer.allocUnsafe(length);
      const { bytesRead } = await handle.read(buffer, 0, length, offset);
      if (bytesRead !== length) {
        throw new Error(`Launcher artifact chunk read failed at byte ${offset}: expected ${length}, got ${bytesRead}`);
      }
      const chunk = buffer.subarray(0, bytesRead);
      const chunkName = `${launcherArtifactName}.part-${String(index).padStart(3, "0")}`;
      const chunkPath = `/launcher-artifacts/${chunkName}`;
      await writeFile(resolve(artifactDir, chunkName), chunk);
      chunks.push({
        path: chunkPath,
        size_bytes: bytesRead,
        sha256: createHash("sha256").update(chunk).digest("hex").toUpperCase(),
      });
      offset += bytesRead;
      index += 1;
    }
  } finally {
    await handle.close();
  }

  await writeFile(
    resolve(artifactDir, `${launcherArtifactName}.manifest.json`),
    `${JSON.stringify({
      artifact_name: launcherArtifactName,
      size_bytes: sourceInfo.size,
      sha256: sourceInfo.sha256,
      chunk_size_bytes: launcherArtifactChunkSize,
      chunks,
    }, null, 2)}\n`
  );
}

if (!(await exists(sourceFrontend))) {
  throw new Error(`Missing frontend source: ${sourceFrontend}`);
}
for (const file of frontendHtmlFiles) {
  const source = resolve(sourceFrontend, file);
  if (!(await exists(source))) throw new Error(`Missing frontend file: ${source}`);
}
for (const file of frontendAssetFiles) {
  const source = resolve(sourceFrontend, "assets", file);
  if (!(await exists(source))) throw new Error(`Missing frontend asset: ${source}`);
}
const launcherArtifactSourceInfo = await verifyLauncherArtifactSource();

if (!checkOnly) {
  await rm(dist, { recursive: true, force: true });
}

await mkdir(resolve(dist, "frontend"), { recursive: true });

if (!checkOnly) {
  for (const file of frontendHtmlFiles) {
    const source = resolve(sourceFrontend, file);
    await cp(source, resolve(dist, "frontend", file));
  }
  for (const file of frontendAssetFiles) {
    const source = resolve(sourceFrontend, "assets", file);
    await mkdir(dirname(resolve(dist, "frontend", "assets", file)), { recursive: true });
    await cp(source, resolve(dist, "frontend", "assets", file));
  }
  await writeFile(
    resolve(dist, "index.html"),
    `<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ARSEN 신청 페이지</title>
<style>
*{box-sizing:border-box}
body{margin:0;min-height:100vh;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Noto Sans KR",sans-serif;background:#0b111c;color:#eef4ff;display:grid;place-items:center;padding:28px 16px}
main{width:min(720px,100%);border:1px solid #334258;border-radius:16px;background:#121a28;padding:30px;box-shadow:0 18px 50px rgba(0,0,0,.28)}
h1{margin:0 0 10px;font-size:clamp(1.8rem,5vw,2.4rem);letter-spacing:0}
p{margin:0 0 22px;color:#b8c6d9;line-height:1.7}
.actions{display:grid;gap:12px}
a{display:block;border:1px solid #40526d;border-radius:12px;color:#eef4ff;text-decoration:none;padding:16px 18px;font-weight:800;background:#182234}
a.primary{background:#18438f;border-color:#6ea8ff}
a span{display:block;margin-top:4px;color:#b8c6d9;font-weight:600;font-size:.95rem}
</style>
</head>
<body>
<main>
<h1>ARSEN 신청 페이지</h1>
<p>원하는 신청 유형을 선택해주세요. 무료 강의는 일정 회차 없이 연락과 편성 참고 정보를 받습니다.</p>
<div class="actions">
<a class="primary" href="/frontend/join-free.html">무료 강의 신청<span>참여 가능 지역과 시간대를 남겨주세요.</span></a>
<a href="/frontend/class-stories.html">공개 후기 보기<span>관리자가 승인한 후기와 결과물만 표시됩니다.</span></a>
<a href="/frontend/join-basic.html">체험 신청 (Basic)<span>간단한 체험 신청과 운영자 확인용입니다.</span></a>
<a href="/frontend/join-full.html">정식 신청 (Full)<span>승인 코드 발급 후 유료 강의 참여까지 연결됩니다.</span></a>
<a href="/frontend/member.html">회원 페이지<span>승인 코드로 예약과 수강 이력을 확인합니다.</span></a>
<a href="/frontend/privacy.html">개인정보처리방침</a>
</div>
</main>
</body>
</html>
`
  );
  await writeLauncherArtifactChunks(launcherArtifactSourceInfo);
}

console.log(checkOnly ? "cloudflare pages build inputs ok" : `cloudflare pages dist ready: ${dist}`);
