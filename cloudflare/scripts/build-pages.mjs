import { createReadStream } from "node:fs";
import { cp, mkdir, open, rm, stat, writeFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { homedir } from "node:os";
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
// YOONBOT Windows artifact is optional: skipped when the file is absent so the
// public release contract stays fail-closed (download_ready=false) until the
// real 1.1.0 exe is staged. Separate name/dir from the launcher ZIP.
const yoonbotArtifactName = "YoonBot-Setup-1.1.0.exe";
const yoonbotArtifactSource = resolve(
  process.env.YOONBOT_ARTIFACT_SOURCE_DIR || resolve(homedir(), ".arsen-work-bus", "artifacts", "yoonbot"),
  yoonbotArtifactName
);
const yoonbotArtifactChunkSize = 20 * 1024 * 1024;
const frontendHtmlFiles = [
  "admin.html",
  "class-dashboard.html",
  "class-stories.html",
  "education.html",
  "join-basic.html",
  "join-free.html",
  "join-full.html",
  "kakao-members.html",
  "license-admin.html",
  "member.html",
  "payment-admin.html",
  "privacy.html",
  "review-submit.html",
  "session-admin.html",
  "status.html",
  "study.html",
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

async function writeYoonbotArtifactChunks() {
  if (!(await exists(yoonbotArtifactSource))) return;
  const info = await stat(yoonbotArtifactSource);
  if (!info.size) return;
  const sha256 = (await sha256File(yoonbotArtifactSource)).toLowerCase();
  const artifactDir = resolve(dist, "yoonbot-artifacts");
  await mkdir(artifactDir, { recursive: true });
  const handle = await open(yoonbotArtifactSource, "r");
  const chunks = [];
  let offset = 0;
  let index = 0;
  try {
    while (offset < info.size) {
      const length = Math.min(yoonbotArtifactChunkSize, info.size - offset);
      const buffer = Buffer.allocUnsafe(length);
      const { bytesRead } = await handle.read(buffer, 0, length, offset);
      if (bytesRead !== length) {
        throw new Error(`Yoonbot artifact chunk read failed at byte ${offset}: expected ${length}, got ${bytesRead}`);
      }
      const chunk = buffer.subarray(0, bytesRead);
      const chunkName = `${yoonbotArtifactName}.part-${String(index).padStart(3, "0")}`;
      await writeFile(resolve(artifactDir, chunkName), chunk);
      chunks.push({
        path: `/yoonbot-artifacts/${chunkName}`,
        size_bytes: bytesRead,
        sha256: createHash("sha256").update(chunk).digest("hex").toLowerCase(),
      });
      offset += bytesRead;
      index += 1;
    }
  } finally {
    await handle.close();
  }

  await writeFile(
    resolve(artifactDir, `${yoonbotArtifactName}.manifest.json`),
    `${JSON.stringify({
      artifact_name: yoonbotArtifactName,
      size_bytes: info.size,
      sha256,
      chunk_size_bytes: yoonbotArtifactChunkSize,
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
<title>ARSEN 고객 페이지</title>
<style>
*{box-sizing:border-box}
body{margin:0;min-height:100vh;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Noto Sans KR",sans-serif;background:#0b111c;color:#eef4ff;display:grid;place-items:center;padding:28px 16px}
main{width:min(820px,100%);border:1px solid #334258;border-radius:16px;background:#121a28;padding:30px;box-shadow:0 18px 50px rgba(0,0,0,.28)}
h1{margin:0 0 10px;font-size:clamp(1.8rem,5vw,2.4rem);letter-spacing:0}
p{margin:0 0 22px;color:#b8c6d9;line-height:1.7}
.actions{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
a{display:block;border:1px solid #40526d;border-radius:12px;color:#eef4ff;text-decoration:none;padding:16px 18px;font-weight:800;background:#182234}
a.primary{background:#18438f;border-color:#6ea8ff}
a.product{background:#0f3d35;border-color:#36d399}
a span{display:block;margin-top:4px;color:#b8c6d9;font-weight:600;font-size:.95rem}
@media(max-width:720px){.actions{grid-template-columns:1fr}}
</style>
</head>
<body>
<main>
<h1>ARSEN 고객 페이지</h1>
<p>유료 강의 신청, 예약 확인, 스터디와 회원 기능을 한곳에서 확인합니다.</p>
<div class="actions">
<a class="primary" href="/frontend/join-full.html">AI 결과물 제작 초급 4주반 신청<span>1기 · 정원 8명 · 100,000원 · 시간과 장소 수요 확인 중</span></a>
<a class="product" href="/frontend/yoonbot.html#download">YOONBOT 다운로드<span>Windows 런처를 내려받고 파일럿 구매 정보를 확인합니다.</span></a>
<a href="/frontend/status.html">예약 확인<span>신청/예약 상태와 안내 문구를 확인합니다.</span></a>
<a href="/frontend/study.html">스터디 참가<span>승인 멤버 전용 스터디 일정을 확인하고 신청합니다.</span></a>
<a href="/frontend/class-dashboard.html">수업용 대시보드<span>강의 자료와 공개 학습 아카이브를 봅니다.</span></a>
<a href="/frontend/class-stories.html">공개 후기 보기<span>관리자가 승인한 후기와 결과물만 표시됩니다.</span></a>
<a href="/frontend/member.html">회원 페이지<span>승인 코드로 예약과 수강 이력을 확인합니다.</span></a>
<a href="/frontend/privacy.html">개인정보처리방침</a>
</div>
</main>
</body>
</html>
`
  );
  await writeLauncherArtifactChunks(launcherArtifactSourceInfo);
  await writeYoonbotArtifactChunks();
}

console.log(checkOnly ? "cloudflare pages build inputs ok" : `cloudflare pages dist ready: ${dist}`);
