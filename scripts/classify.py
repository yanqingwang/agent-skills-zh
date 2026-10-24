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
    ("分析与逆向", [r"reverse-engineer", r"understand"]),
    ("写作与表达", [r"humanizer", r"brag"]),
    ("调研与信息", [r"last30days"]),
    ("提示词工程", [r"prompt-master"]),
    ("知识转化", [r"book-to-skill", r"distilly"]),
    ("科学研究", [r"experimental-design"]),
    ("市场与增长", [r"product-marketing"]),
    ("省 token 与输出格式", [r"caveman", r"i-have-adhd"]),
    ("质量与审查", [r"code-review", r"reviewer", r"quality", r"security-review"]),
    ("上下文工程", [r"context", r"continuous-learning", r"autonomous-loops"]),
    ("设计品味", [r"taste", r"diagram-design", r"archify"]),
    ("头脑风暴与构思", [r"brainstorm", r"idea", r"refine"]),
    ("工程方法论", [r"tdd|test-driven|debug|plan|spec|verification|triage|search-first|ponytail"]),
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
        "reverse-engineer-anything": "逆向工程一切（REA）",
        "ponytail": "最小改动（ponytail）",
        "caveman": "省 token 电报体（caveman）",
        "archify": "交互图表生成（archify）",
        "understand": "代码库知识图谱（understand）",
        "last30days": "近 30 天调研（last30days）",
        "diagram-design": "图表设计（diagram-design）",
        "humanizer": "去 AI 腔（humanizer）",
        "i-have-adhd": "答案前置输出（i-have-adhd）",
        "product-marketing": "产品营销基础（product-marketing）",
        "experimental-design": "实验设计（experimental-design）",
        "search-first": "先检索后编码（search-first）",
        "security-review": "安全审查清单（security-review）",
        "continuous-learning-v2": "持续学习 v2（instinct）",
        "autonomous-loops": "自主循环（autonomous-loops）",
        "book-to-skill": "书籍转 Skill（book-to-skill）",
        "planning-with-files": "文件化计划（planning-with-files）",
        "distilly": "人物画像蒸馏（distilly）",
        "brag": "项目宣传文案（brag）",
        "prompt-master": "提示词大师（prompt-master）",
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
