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
    out = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{upstream_path}", "--jq", ".content"],
        capture_output=True, text=True, check=True,
    ).stdout
    return base64.b64decode(out)


def main() -> int:
    check_only = "--check" in sys.argv
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
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


if __name__ == "__main__":
    raise SystemExit(main())
