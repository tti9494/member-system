import { execFile } from "node:child_process";
import { existsSync } from "node:fs";
import { resolve } from "node:path";

const root = new URL("..", import.meta.url).pathname;
const repo = resolve(root, "..");
const dbPath = process.env.MEMBER_SYSTEM_SQLITE || resolve(repo, "members.db");
const d1Name = process.env.MEMBER_SYSTEM_D1 || "arsen_member_system";
const tables = ["members", "sessions", "bookings", "member_logs", "operator_settings"];

function run(command, args, options = {}) {
  return new Promise((resolvePromise, reject) => {
    execFile(command, args, { cwd: root, maxBuffer: 20 * 1024 * 1024, ...options }, (error, stdout, stderr) => {
      if (error) {
        error.stdout = stdout;
        error.stderr = stderr;
        reject(error);
        return;
      }
      resolvePromise({ stdout, stderr });
    });
  });
}

async function localCounts() {
  if (!existsSync(dbPath)) return null;
  const code = `
import json, sqlite3, sys
path = sys.argv[1]
tables = ${JSON.stringify(tables)}
conn = sqlite3.connect(path)
existing = {row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
out = {}
for table in tables:
    if table in existing:
        out[table] = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
conn.close()
print(json.dumps(out, ensure_ascii=False))
`;
  const { stdout } = await run("python3", ["-c", code, dbPath], { cwd: repo });
  return JSON.parse(stdout);
}

function parseWranglerRows(payload) {
  const text = String(payload || "");
  const starts = ["[", "{"]
    .map((char) => text.indexOf(char))
    .filter((index) => index >= 0);
  if (!starts.length) throw new Error("Wrangler JSON output was empty.");
  const parsed = JSON.parse(text.slice(Math.min(...starts)));
  const items = Array.isArray(parsed) ? parsed : [parsed];
  const rows = [];
  for (const item of items) {
    const results = item?.results || item?.result?.[0]?.results || item?.result?.results || [];
    rows.push(...results);
  }
  return rows;
}

async function remoteCounts() {
  const sql = tables.map((table) => `SELECT '${table}' AS table_name, COUNT(*) AS count FROM ${table}`).join(" UNION ALL ");
  const { stdout } = await run("npx", ["--yes", "wrangler", "d1", "execute", d1Name, "--remote", "--json", "--command", sql]);
  const rows = parseWranglerRows(stdout);
  return Object.fromEntries(rows.map((row) => [row.table_name, Number(row.count || 0)]));
}

const [local, remote] = await Promise.all([localCounts(), remoteCounts()]);
const comparison = {};
for (const table of tables) {
  comparison[table] = {
    local: local ? local[table] ?? 0 : null,
    d1: remote[table] ?? 0,
    match: local ? (local[table] ?? 0) === (remote[table] ?? 0) : null,
  };
}

console.log(JSON.stringify({
  sqlite_present: Boolean(local),
  d1: d1Name,
  comparison,
}, null, 2));
