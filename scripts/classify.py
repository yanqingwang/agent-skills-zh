#!/usr/bin/env python3
"""按 manifest.json 自动生成分类索引 data/category-index.md。

分类规则：关键词匹配（文件路径 + 首行内容），规则集中在本脚本，可按需扩充。
用法：python3 scripts/classify.py
"""
from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "manifest.json"
OUT = ROOT / "data" / "category-index.md"

# 关键词 → 分类（顺序即优先级，先匹配先归类）
RULES: list[tuple[str, list[str]]] = [
    ("质量与审查", [r"code-review", r"reviewer", r"quality"]),
    ("上下文工程", [r"context"]),
    ("设计品味", [r"taste", r"design"]),
    ("头脑风暴与构思", [r"brainstorm", r"idea", r"refine"]),
    ("工程方法论", [r"tdd|test-driven|debug|plan|spec|verification|triage"]),
]


def classify(path: str) -> str:
    for category, patterns in RULES:
        if any(re.search(p, path, re.IGNORECASE) for p in patterns):
            return category
    return "其他"


def zh_title(path: str) -> str:
    """从 SKILL.md 的 frontmatter name/description 或路径推断中文标题。"""
    known = {
        "test-driven-development": "测试驱动开发（TDD）",
        "systematic-debugging": "系统化调试",
        "writing-plans": "写计划",
        "verification-before-completion": "完成前验证",
        "brainstorming": "头脑风暴",
        "code-review": "代码审查",
        "to-spec": "从想法到规格",
        "context-engineering": "上下文工程",
        "idea-refine": "想法精炼",
        "code-reviewer.md": "代码审查者 Agent",
        "taste-skill": "设计品味（taste）",
    }
    stem = pathlib.PurePosixPath(path).name
    parent = pathlib.PurePosixPath(path).parent.name
    return known.get(stem) or known.get(parent) or parent or stem


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows: list[tuple[str, str, str, str]] = []  # category, upstream, title, local path
    for up in manifest["upstreams"]:
        for entry in up["files"]:
            local = entry["local"]
            if not (ROOT / local).exists():
                continue  # 尚未翻译完成
            rows.append((classify(local), up["repo"], zh_title(local), local))

    groups: dict[str, list[tuple[str, str, str]]] = {}
    for cat, repo, title, path in rows:
        groups.setdefault(cat, []).append((repo, title, path))

    lines = [
        "<!-- 由 scripts/classify.py 自动生成，勿手改 -->",
        "# 分类索引",
        "",
    ]
    for cat in [c for c, _ in RULES] + ["其他"]:
        if cat not in groups:
            continue
        lines.append(f"## {cat}\n")
        for repo, title, path in sorted(groups[cat]):
            lines.append(f"- [{title}]({path}) — 上游 [{repo}](https://github.com/{repo})")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"written {OUT} ({sum(len(v) for v in groups.values())} files indexed)")


if __name__ == "__main__":
    main()
