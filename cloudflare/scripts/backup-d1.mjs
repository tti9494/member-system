import { execFile } from "node:child_process";
import { mkdirSync, statSync } from "node:fs";
import { resolve } from "node:path";

const root = new URL("..", import.meta.url).pathname;
const d1Name = process.env.MEMBER_SYSTEM_D1 || "arsen_member_system";
const backupDir = process.env.MEMBER_SYSTEM_D1_BACKUP_DIR || resolve(root, ".data", "backups");
const stamp = new Date().toISOString().replace(/[:.]/g, "-");
const output = resolve(backupDir, `${d1Name}-${stamp}.sql`);

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

mkdirSync(backupDir, { recursive: true, mode: 0o700 });
await run("npx", [
  "--yes",
  "wrangler",
  "d1",
  "export",
  d1Name,
  "--remote",
  "--skip-confirmation",
  "--output",
  output,
]);

const size = statSync(output).size;
console.log(JSON.stringify({
  ok: true,
  d1: d1Name,
  output,
  size_bytes: size,
  note: "Backup may contain operational member data. Keep this file private.",
}, null, 2));
