#!/usr/bin/env python3
"""每日上游同步引擎：比对 HEAD → 刷新原样件 → 记录变化 → 生成重译清单。

流程（对 data/manifest.json 的每个上游，跳过无收录文件的占位条目）：
  1. 取上游 HEAD sha，与 data/sync-state.json 比对；未变化则跳过。
  2. HEAD 变化：拉取上游 git tree（blob sha 全表），与本地逐一比对——
     - verbatim 件 blob sha 不一致 → 自动从上游刷新（下游同步，逐字节覆盖）；
     - 翻译件（SKILL.md / Agent 定义 / 规则）上游 blob sha 与上次快照不一致
       → 本地是中文译文无法字节比对，记入重译清单（对照 data/file-shas.json 的
       上次快照；首跑只建基线不报变更）。
  3. 变化写入 data/sync-log/YYYY-MM-DD.md；重译清单写 data/sync-pending-retranslation.md。
  4. 更新 sync-state 与 file-shas。

用法：
  python3 scripts/sync_daily.py             # 执行同步（本地或 CI）
  python3 scripts/sync_daily.py --dry-run   # 只比对与报告，不写任何文件

网络操作失败重试 5 次（仓库纪律）；全部失败该上游记 FAIL 不中断整体。
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "manifest.json"
STATE = ROOT / "data" / "sync-state.json"
FILE_SHAS = ROOT / "data" / "file-shas.json"
LOG_DIR = ROOT / "data" / "sync-log"
PENDING = ROOT / "data" / "sync-pending-retranslation.md"
RETRIES = 5


def gh(*args: str, binary: bool = False) -> bytes | None:
    """gh api 调用，失败重试 RETRIES 次；最终失败返回 None。"""
    for attempt in range(1, RETRIES + 1):
        r = subprocess.run(["gh", "api", *args], capture_output=True)
        if r.returncode == 0:
            return r.stdout
        sys.stderr.write(f"gh api 重试 {attempt}/{RETRIES}: {args[0]} {r.stderr.decode()[:120]}\n")
    return None


def head_sha(repo: str) -> str | None:
    out = gh(f"repos/{repo}/commits/HEAD", "--jq", ".sha")
    return out.decode().strip() if out else None


def tree_shas(repo: str) -> dict[str, str] | None:
    out = gh(f"repos/{repo}/git/trees/HEAD?recursive=1", "--jq",
             '.tree[] | select(.type=="blob") | .path + "\t" + .sha')
    if out is None:
        return None
    shas = {}
    for line in out.decode().splitlines():
        path, _, sha = line.partition("\t")
        if path and sha:
            shas[path] = sha
    return shas


def local_blob_sha(path: pathlib.Path) -> str | None:
    if not path.exists():
        return None
    r = subprocess.run(["git", "hash-object", str(path)], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def fetch_raw(repo: str, upstream_path: str) -> bytes | None:
    """按 raw 媒体类型取上游文件原始字节（支持 >1MB 大文件）。"""
    return gh(f"repos/{repo}/contents/{upstream_path}",
              "-H", "Accept: application/vnd.github.raw")


def main() -> int:
    dry = "--dry-run" in sys.argv
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    state = json.loads(STATE.read_text(encoding="utf-8"))
    shas_store = json.loads(FILE_SHAS.read_text(encoding="utf-8")) if FILE_SHAS.exists() else {}
    baseline_first_run = not FILE_SHAS.exists()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_lines: list[str] = [f"# 上游同步日志 {today}\n"]
    pending: list[str] = []
    refreshed = skipped = unchanged = failed = 0

    for up in manifest["upstreams"]:
        repo = up["repo"]
        verbatim = up.get("verbatim", [])
        translated = up.get("files", [])
        if not verbatim and not translated:
            log_lines.append(f"- ⏭️ `{repo}` — 无收录文件（排除占位），跳过")
            skipped += 1
            continue

        new_head = head_sha(repo)
        if new_head is None:
            log_lines.append(f"- ❌ `{repo}` — HEAD 获取失败（重试 {RETRIES} 次后放弃）")
            failed += 1
            continue
        old_head = state["repos"].get(repo, "")
        short = new_head[:12]
        if old_head == new_head and repo in shas_store:
            # HEAD 未变化且翻译件基线已建：完全跳过
            unchanged += 1
            continue
        if not old_head:
            state["repos"][repo] = new_head
            log_lines.append(f"- 🆕 `{repo}` — 首次登记 HEAD `{short}`")

        shas = tree_shas(repo)
        if shas is None:
            log_lines.append(f"- ❌ `{repo}` — tree 获取失败（`{old_head[:12]}` → `{short}`），本次跳过，待下轮重试")
            failed += 1
            continue

        if old_head == new_head:
            # 仅补建翻译件基线（首跑或历史缺口），文件无变化
            prev = shas_store.setdefault(repo, {})
            for e in translated:
                want = shas.get(e["upstream"])
                if want is not None:
                    prev[e["upstream"]] = want
            unchanged += 1
            continue

        repo_changes: list[str] = []
        # verbatim：blob sha 不一致即刷新
        for e in verbatim:
            want = shas.get(e["upstream"])
            if want is None:
                repo_changes.append(f"  - ⚠️ verbatim `{e['upstream']}` 上游已不存在（本地保留，需人工评估）")
                continue
            local = ROOT / e["local"]
            if local_blob_sha(local) != want:
                blob = fetch_raw(repo, e["upstream"])
                if blob is None:
                    repo_changes.append(f"  - ❌ verbatim `{e['upstream']}` 刷新失败（网络）")
                    failed += 1
                    continue
                if not dry:
                    local.parent.mkdir(parents=True, exist_ok=True)
                    local.write_bytes(blob)
                repo_changes.append(f"  - 🔄 verbatim `{e['upstream']}` 已自动刷新")
                refreshed += 1
        # 翻译件：上游 blob sha 与快照比对 → 重译清单
        prev = shas_store.get(repo, {})
        for e in translated:
            want = shas.get(e["upstream"])
            if want is None:
                repo_changes.append(f"  - ⚠️ 翻译件 `{e['upstream']}` 上游已不存在（本地译文保留，需人工评估）")
                continue
            if prev.get(e["upstream"]) not in (None, want):
                repo_changes.append(f"  - ✏️ 翻译件 `{e['upstream']}` 上游有变更 → 需重译（本地：`{e['local']}`）")
                pending.append(f"- `{repo}` · `{e['upstream']}` → 本地 `{e['local']}`")
            prev[e["upstream"]] = want
        shas_store[repo] = prev

        if repo_changes:
            log_lines.append(f"- 📦 `{repo}`（`{old_head[:12]}` → `{short}`）")
            log_lines.extend(repo_changes)
        else:
            log_lines.append(f"- 🔎 `{repo}`（`{old_head[:12]}` → `{short}`）HEAD 变化但收录文件无变更")
        state["repos"][repo] = new_head

    # 写盘
    if not dry:
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        FILE_SHAS.write_text(json.dumps(shas_store, ensure_ascii=False, indent=2) + "\n")
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        log_file = LOG_DIR / f"{today}.md"
        with log_file.open("a", encoding="utf-8") as f:
            if not log_file.exists():
                f.write(f"# 上游同步日志 {today}\n\n")
            f.write("\n".join(log_lines[1:]) + "\n")
        if pending:
            PENDING.write_text(
                f"# 待重译清单（{today} 自动生成）\n\n上游翻译件有变更，需按 GLOSSARY/PRINCIPLES 增量重译并更新文件头同步日期：\n\n"
                + "\n".join(pending) + "\n", encoding="utf-8")
        elif PENDING.exists():
            PENDING.unlink()

    mode = "DRY-RUN" if dry else "SYNC"
    print(f"[{mode}] 未变化={unchanged} 首登/跳过={skipped} verbatim刷新={refreshed} 待重译={len(pending)} 失败={failed}")
    print("\n".join(log_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
