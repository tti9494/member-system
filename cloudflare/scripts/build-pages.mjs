import { cp, mkdir, rm, stat, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const sourceFrontend = resolve(root, "..", "frontend");
const dist = resolve(root, "dist");
const checkOnly = process.argv.includes("--check");
const frontendHtmlFiles = [
  "admin.html",
  "class-stories.html",
  "education.html",
  "join-basic.html",
  "join-free.html",
  "join-full.html",
  "license-admin.html",
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
<a href="/frontend/privacy.html">개인정보처리방침</a>
</div>
</main>
</body>
</html>
`
  );
}

console.log(checkOnly ? "cloudflare pages build inputs ok" : `cloudflare pages dist ready: ${dist}`);
