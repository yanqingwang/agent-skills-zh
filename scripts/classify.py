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
# 类别由目录结构承载：skills/<用户角色>/<类别>/<skill>/
# 角色与类别即分类，不再做关键词推断。

RULES: list[tuple[str, list[str]]] = []

PERSONA_ZH = {
    "developer": "开发者",
    "writer": "写作者",
    "designer": "设计师",
    "researcher": "研究者",
    "growth": "产品与增长",
    "gamedev": "游戏开发者",
    "creator": "创作者",
    "toolbox": "通用工具箱",
    "gstack": "开发者 · gstack 整仓",
}


def classify(path: str) -> str:
    parts = pathlib.PurePosixPath(path).parts
    persona = PERSONA_ZH.get(parts[1], parts[1]) if len(parts) > 2 else "其他"
    if parts[1] == "gstack":
        return PERSONA_ZH["gstack"]
    if len(parts) > 3:
        return f"{persona} · {parts[2]}"
    return persona


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
                continue
            rows.append((classify(local), up["repo"], zh_title(local), local))

    groups: dict[str, list[tuple[str, str, str]]] = {}
    for cat, repo, title, path in rows:
        groups.setdefault(cat, []).append((repo, title, path))

    lines = [
        "<!-- 由 scripts/classify.py 自动生成，勿手改；分类 = skills/ 目录结构 -->",
        "# 分类索引（按用户角色）",
        "",
    ]
    for cat in sorted(groups):
        lines.append(f"## {cat}\n")
        for repo, title, path in sorted(groups[cat], key=lambda x: x[2]):
            lines.append(f"- [{title}]({path}) — 上游 [{repo}](https://github.com/{repo})")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"written {OUT} ({sum(len(v) for v in groups.values())} files indexed)")


if __name__ == "__main__":
    main()
