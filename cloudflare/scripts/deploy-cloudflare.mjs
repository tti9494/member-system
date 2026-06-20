import { execFile } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import crypto from "node:crypto";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repo = resolve(root, "..");
const dbName = "arsen_member_system";
const workerName = "arsen-member-system";
const routePattern = "apply.arsen-ai.com/*";
const dataDir = resolve(root, ".data");
const secretsPath = resolve(root, ".secrets.local");
const wranglerToml = resolve(root, "wrangler.toml");
const envPath = resolve(repo, ".env");
const importLocalData = process.argv.includes("--import-local-data")
  || ["1", "true", "yes"].includes(String(process.env.MEMBER_SYSTEM_IMPORT_LOCAL_DATA || "").trim().toLowerCase());
const enableR2Binding = ["1", "true", "yes"].includes(String(process.env.MEMBER_SYSTEM_ENABLE_R2_BINDING || "").trim().toLowerCase());
const totalSteps = importLocalData ? 8 : 7;
let currentStep = 1;

function logStep(message) {
  console.log(`${currentStep++}/${totalSteps} ${message}`);
}

function run(command, args, options = {}) {
  return new Promise((resolvePromise, reject) => {
    const child = execFile(command, args, { cwd: root, env: process.env, maxBuffer: 20 * 1024 * 1024, ...options }, (error, stdout, stderr) => {
      if (error) {
        error.stdout = stdout;
        error.stderr = stderr;
        reject(error);
        return;
      }
      resolvePromise({ stdout, stderr });
    });
    if (options.input !== undefined) {
      child.stdin.end(options.input);
    }
  });
}

function parseEnvFile(path) {
  if (!existsSync(path)) return {};
  const text = readFileSync(path, "utf8");
  const result = {};
  for (const line of text.split(/\r?\n/)) {
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

function updateLocalSecrets(values) {
  const current = parseEnvFile(secretsPath);
  const next = { ...current, ...values };
  const lines = Object.entries(next).map(([key, value]) => `${key}=${value}`);
  writeFileSync(secretsPath, `${lines.join("\n")}\n`, { mode: 0o600 });
  return next;
}

function configured(value) {
  const text = String(value || "").trim();
  if (!text) return false;
  const lowered = text.toLowerCase();
  return !["your_", "placeholder", "token_here", "chat_id_here", "telegram_bot_token", "telegram_admin_chat_id"].some((marker) =>
    lowered.includes(marker)
  );
}

function firstConfigured(...values) {
  return values.find((value) => configured(value)) || "";
}

async function wrangler(args, options = {}) {
  return run("npx", ["--yes", "wrangler", ...args], options);
}

function parseWranglerJson(stdout) {
  const text = String(stdout || "");
  const starts = ["[", "{"]
    .map((char) => text.indexOf(char))
    .filter((index) => index >= 0);
  if (!starts.length) throw new Error("Wrangler JSON output was empty.");
  return JSON.parse(text.slice(Math.min(...starts)));
}

async function tryD1Migration(command, ignoredErrorText) {
  try {
    await wrangler(["d1", "execute", dbName, "--remote", "--yes", "--command", command]);
  } catch (error) {
    const detail = `${error.stderr || ""}\n${error.message || ""}`.toLowerCase();
    if (!detail.includes(String(ignoredErrorText).toLowerCase())) {
      throw error;
    }
  }
}

async function ensureD1() {
  let list;
  try {
    const { stdout } = await wrangler(["d1", "list", "--json"]);
    const payload = parseWranglerJson(stdout);
    list = Array.isArray(payload) ? payload : payload.result || [];
  } catch (error) {
    throw new Error(`Cloudflare D1 list failed. Set CLOUDFLARE_API_TOKEN first. ${error.stderr || error.message}`);
  }
  const existing = list.find((item) => item.name === dbName);
  if (existing) return existing.uuid || existing.id || existing.database_id;

  const { stdout } = await wrangler(["d1", "create", dbName]);
  const match = stdout.match(/"database_id"\s*:\s*"([^"]+)"/);
  if (!match) {
    throw new Error("D1 database was created, but database_id could not be parsed from wrangler output.");
  }
  return match[1];
}

function writeWranglerConfig(databaseId) {
  const config = `name = "${workerName}"
main = "src/worker.js"
compatibility_date = "2026-05-20"
workers_dev = true

[assets]
directory = "./dist"
binding = "ASSETS"

[[d1_databases]]
binding = "DB"
database_name = "${dbName}"
database_id = "${databaseId}"

${enableR2Binding ? `
[[r2_buckets]]
binding = "LAUNCHER_RELEASES"
bucket_name = "arsen-launcher-releases"
` : ""}

[vars]
ALLOWED_ORIGINS = "https://arsen-ai.com,https://www.arsen-ai.com,https://apply.arsen-ai.com"
PUBLIC_BASE_URL = "https://apply.arsen-ai.com"
KAKAO_REDIRECT_URI = "https://apply.arsen-ai.com/auth/kakao/callback"
TELEGRAM_NOTIFY_ENABLED = "true"
TELEGRAM_APPLICATION_NOTIFY_ENABLED = "true"
TELEGRAM_BOOKING_NOTIFY_ENABLED = "true"
`;
  writeFileSync(wranglerToml, config, { mode: 0o600 });
}

async function putSecret(name, value) {
  if (!value) throw new Error(`Missing required secret: ${name}`);
  await wrangler(["secret", "put", name], { input: `${value}\n` });
}

async function setTelegramWebhook(token, secret) {
  if (!configured(token) || !configured(secret)) return "not_configured";
  const response = await fetch(`https://api.telegram.org/bot${token}/setWebhook`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      url: "https://apply.arsen-ai.com/telegram/webhook",
      secret_token: secret,
      allowed_updates: ["callback_query"],
      drop_pending_updates: false,
    }),
  });
  if (!response.ok) return "failed";
  const body = await response.json().catch(() => null);
  return body?.ok ? "ok" : "failed";
}

async function main() {
  mkdirSync(dataDir, { recursive: true });
  const localEnv = parseEnvFile(envPath);
  const existingLocalSecrets = parseEnvFile(secretsPath);
  const localSecrets = updateLocalSecrets({
    CONTACT_ENCRYPTION_KEY:
      existingLocalSecrets.CONTACT_ENCRYPTION_KEY || crypto.randomBytes(32).toString("base64url"),
    TELEGRAM_WEBHOOK_SECRET:
      existingLocalSecrets.TELEGRAM_WEBHOOK_SECRET || crypto.randomBytes(32).toString("base64url"),
    KAKAO_SESSION_SECRET:
      existingLocalSecrets.KAKAO_SESSION_SECRET || crypto.randomBytes(32).toString("base64url"),
  });
  const adminKey = localEnv.ADMIN_API_KEY || existingLocalSecrets.ADMIN_API_KEY;
  if (!adminKey) {
    throw new Error("ADMIN_API_KEY was not found in /Users/yoon/member-system/.env or cloudflare/.secrets.local");
  }
  const phoneSecret = localEnv.PHONE_SECRET_KEY || existingLocalSecrets.PHONE_SECRET_KEY;
  const emailSecret = localEnv.EMAIL_SECRET_KEY || existingLocalSecrets.EMAIL_SECRET_KEY;
  const codeSecret = localEnv.CODE_SECRET_KEY || existingLocalSecrets.CODE_SECRET_KEY;
  if (!phoneSecret || !emailSecret) {
    throw new Error("PHONE_SECRET_KEY and EMAIL_SECRET_KEY are required to preserve existing encrypted contact records.");
  }

  const telegramToken = firstConfigured(localEnv.TELEGRAM_BOT_TOKEN, existingLocalSecrets.TELEGRAM_BOT_TOKEN);
  const telegramChatId = firstConfigured(
    localEnv.TELEGRAM_ADMIN_CHAT_ID,
    localEnv.TELEGRAM_CHAT_ID,
    existingLocalSecrets.TELEGRAM_ADMIN_CHAT_ID,
    existingLocalSecrets.TELEGRAM_CHAT_ID,
  );

  logStep("build static assets");
  await run("npm", ["run", "build"], { cwd: root });

  logStep("ensure D1 database");
  const databaseId = await ensureD1();
  writeWranglerConfig(databaseId);

  logStep("apply schema");
  await wrangler(["d1", "execute", dbName, "--remote", "--yes", "--file", "schema.sql"]);
  await tryD1Migration("ALTER TABLE members ADD COLUMN available_time_slots TEXT", "duplicate column name");
  await tryD1Migration("ALTER TABLE members ADD COLUMN kakao_id TEXT", "duplicate column name");
  await tryD1Migration("ALTER TABLE members ADD COLUMN kakao_profile TEXT", "duplicate column name");
  await tryD1Migration("ALTER TABLE members ADD COLUMN kakao_connected_at TEXT", "duplicate column name");
  await wrangler(["d1", "execute", dbName, "--remote", "--yes", "--command", "CREATE INDEX IF NOT EXISTS idx_members_kakao_id ON members(kakao_id)"]);
  await tryD1Migration("ALTER TABLE orders ADD COLUMN toss_order_id TEXT", "duplicate column name");
  await tryD1Migration("ALTER TABLE orders ADD COLUMN original_amount_krw INTEGER", "duplicate column name");
  await tryD1Migration("ALTER TABLE orders ADD COLUMN discount_code TEXT", "duplicate column name");
  await tryD1Migration("ALTER TABLE orders ADD COLUMN discount_label TEXT", "duplicate column name");
  await tryD1Migration("ALTER TABLE orders ADD COLUMN discount_amount_krw INTEGER NOT NULL DEFAULT 0", "duplicate column name");

  if (importLocalData) {
    logStep("export local sqlite seed (explicit opt-in)");
    const seedPath = resolve(dataDir, "current-data.sql");
    await run("python3", ["scripts/export-d1-data.py", resolve(repo, "members.db"), seedPath], { cwd: root });

    logStep("import local data into D1 without replacing existing rows");
    await wrangler(["d1", "execute", dbName, "--remote", "--yes", "--file", seedPath]);
  } else {
    logStep("skip local sqlite import; preserving live D1 operational data");
  }

  logStep("deploy worker + assets + production route");
  await wrangler(["deploy", "--route", routePattern]);

  logStep("set Cloudflare secrets");
  await putSecret("ADMIN_API_KEY", adminKey);
  await putSecret("PHONE_SECRET_KEY", phoneSecret);
  await putSecret("EMAIL_SECRET_KEY", emailSecret);
  if (configured(codeSecret)) await putSecret("CODE_SECRET_KEY", codeSecret);
  await putSecret("CONTACT_ENCRYPTION_KEY", localSecrets.CONTACT_ENCRYPTION_KEY);
  await putSecret("TELEGRAM_WEBHOOK_SECRET", localSecrets.TELEGRAM_WEBHOOK_SECRET);
  await putSecret("KAKAO_SESSION_SECRET", localSecrets.KAKAO_SESSION_SECRET);
  if (configured(telegramToken)) await putSecret("TELEGRAM_BOT_TOKEN", telegramToken);
  if (configured(telegramChatId)) await putSecret("TELEGRAM_ADMIN_CHAT_ID", telegramChatId);
  if (configured(localEnv.KAKAO_REST_API_KEY || existingLocalSecrets.KAKAO_REST_API_KEY)) {
    await putSecret("KAKAO_REST_API_KEY", localEnv.KAKAO_REST_API_KEY || existingLocalSecrets.KAKAO_REST_API_KEY);
  }
  if (configured(localEnv.KAKAO_CLIENT_SECRET || existingLocalSecrets.KAKAO_CLIENT_SECRET)) {
    await putSecret("KAKAO_CLIENT_SECRET", localEnv.KAKAO_CLIENT_SECRET || existingLocalSecrets.KAKAO_CLIENT_SECRET);
  }

  logStep("set Telegram webhook");
  const webhookStatus = await setTelegramWebhook(telegramToken, localSecrets.TELEGRAM_WEBHOOK_SECRET);
  console.log(`Telegram webhook: ${webhookStatus}`);

  console.log("Cloudflare deploy complete. Test https://apply.arsen-ai.com/health and public/admin pages.");
}

main().catch((error) => {
  console.error(error.message || error);
  process.exit(1);
});
