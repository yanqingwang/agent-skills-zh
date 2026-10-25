#!/usr/bin/env python3
"""按 manifest.json 的 verbatim 清单，从上游原样抓取非翻译文件（代码/样式/数据/未译散文）。

原则（PRINCIPLES #11）：收录一个 Skill = SKILL.md（翻译）+ 目录内被引用文件（原样复制，逐字节一致）。
代码、样式、数据文件永不翻译。同步时重跑本脚本即可刷新所有 verbatim 文件。

用法：python3 scripts/fetch_verbatim.py [--check]
  --check  仅比对本地文件与上游是否逐字节一致，不写入（供 CI/校验用）
"""
from __future__ import annotations

import base64
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "manifest.json"


def fetch(upstream_path: str, repo: str) -> bytes:
    # raw 媒体类型：>1MB 的文件（音频/大 JSON 等）contents API 默认 base64 路径会报
    # "too large"，raw 直返原始字节，上限 100MB；<1MB 文件行为不变。
    out = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{upstream_path}",
         "-H", "Accept: application/vnd.github.raw"],
        capture_output=True, check=True,
    ).stdout
    return out


def main() -> int:
    check_only = "--check" in sys.argv
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--trees" in sys.argv:
        raise SystemExit(tree_check(manifest))
    ok = fail = changed = 0
    for up in manifest["upstreams"]:
        for entry in up.get("verbatim", []):
            local = ROOT / entry["local"]
            try:
                blob = fetch(entry["upstream"], up["repo"])
            except subprocess.CalledProcessError as e:
                print(f"FAIL fetch {up['repo']}/{entry['upstream']}: {e.stderr.strip()[:80]}")
                fail += 1
                continue
            if check_only:
                if local.exists() and local.read_bytes() == blob:
                    ok += 1
                else:
                    print(f"DIFF {entry['local']}")
                    changed += 1
            else:
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_bytes(blob)
                ok += 1
    mode = "check" if check_only else "write"
    print(f"[{mode}] ok={ok} fail={fail} diff={changed}")
    return 1 if fail or (check_only and changed) else 0


def tree_check(manifest) -> int:
    """按 git blob SHA 全量校验（整仓收录后 verbatim 件数 3000+，逐文件 API 太重）。

    每个上游仅 1 次 trees API 拿全仓 blob sha 映射，本地用 git hash-object 计算
    blob sha1 比对——与逐字节比对等价（blob sha 即内容哈希），但无内容下载。
    """
    ok = fail = diff = 0
    for up in manifest["upstreams"]:
        out = subprocess.run(
            ["gh", "api", f"repos/{up['repo']}/git/trees/HEAD?recursive=1",
             "--jq", '.tree[] | select(.type=="blob") | .path + "\t" + .sha'],
            capture_output=True, text=True, check=False,
        )
        if out.returncode != 0:
            print(f"FAIL tree {up['repo']}: {out.stderr.strip()[:100]}")
            fail += 1
            continue
        shas = {}
        for line in out.stdout.splitlines():
            path, _, sha = line.partition("\t")
            if path and sha:
                shas[path] = sha
        for entry in up.get("verbatim", []):
            local = ROOT / entry["local"]
            want = shas.get(entry["upstream"])
            if want is None or not local.exists():
                print(f"DIFF {entry['local']} (上游不存在或本地缺失)")
                diff += 1
                continue
            h = subprocess.run(["git", "hash-object", str(local)],
                               capture_output=True, text=True, check=True).stdout.strip()
            if h == want:
                ok += 1
            else:
                print(f"DIFF {entry['local']}")
                diff += 1
    print(f"[tree-check] ok={ok} fail={fail} diff={diff}")
    return 1 if fail or diff else 0


if __name__ == "__main__":
    raise SystemExit(main())
