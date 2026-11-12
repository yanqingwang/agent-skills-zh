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
        "ui-ux-pro-max": "UI/UX 专业设计（ui-ux-pro-max）",
        "impeccable": "无可挑剔前端（impeccable）",
        "hallmark": "反 AI 味设计（hallmark）",
        "anatomy": "等距技术插画（anatomy）",
        "security-audit": "多阶段安全审计（security-audit）",
        "obsidian-cli": "Obsidian CLI（obsidian-cli）",
        "obsidian-markdown": "Obsidian Markdown 方言（obsidian-markdown）",
        "obsidian-bases": "Obsidian Bases（obsidian-bases）",
        "json-canvas": "JSON Canvas 格式（json-canvas）",
        "defuddle": "网页正文抽取（defuddle）",
        "knap": "仓库格式体检（knap）",
        "gcloud": "gcloud CLI 安全护栏（gcloud）",
        "context-degradation": "上下文退化诊治（context-degradation）",
        "long-horizon-prompting": "长程启动提示词（long-horizon-prompting）",
        "gsap-core": "GSAP 核心（gsap-core）",
        "gsap-scrolltrigger": "GSAP ScrollTrigger（gsap-scrolltrigger）",
        "gsap-react": "GSAP React 集成（gsap-react）",
        "frontend-slides": "网页幻灯片（frontend-slides）",
        "pixelfx": "像素艺术特效（pixelfx）",
        "banner-design": "Banner 设计（banner-design）",
        "brand": "品牌规范（brand）",
        "design-system": "设计系统（design-system）",
        "design": "UI 设计（design）",
        "slides": "幻灯片设计（slides）",
        "ui-styling": "UI 样式落地（ui-styling）",
        "gsap-frameworks": "GSAP 框架集成（gsap-frameworks）",
        "gsap-plugins": "GSAP 插件（gsap-plugins）",
        "gsap-performance": "GSAP 性能（gsap-performance）",
        "gsap-timeline": "GSAP 时间线（gsap-timeline）",
        "gsap-utils": "GSAP 工具函数（gsap-utils）",
        "memory-systems": "记忆系统设计（memory-systems）",
        "tool-design": "工具设计（tool-design）",
        "multi-agent-patterns": "多代理模式（multi-agent-patterns）",
        "bdi-mental-states": "BDI 心智状态建模（bdi-mental-states）",
        "literature-review": "文献综述（literature-review）",
        "peer-review": "同行评审（peer-review）",
        "scientific-writing": "科学论文写作（scientific-writing）",
        "statistical-power": "统计功效分析（statistical-power）",
        "copy-editing": "文案精修（copy-editing）",
        "pricing": "定价与包装（pricing）",
        "launch": "产品发布（launch）",
        "ab-testing": "A/B 测试（ab-testing）",
        "marketing-psychology": "营销心理学（marketing-psychology）",
        "python-project-structure": "Python 工程结构（python-project-structure）",
        "gitlab-ci-patterns": "GitLab CI 流水线（gitlab-ci-patterns）",
        "sast-configuration": "SAST 静态安全扫描配置（sast-configuration）",
        "review-agent-setup": "审查 Agent 治理（review-agent-setup）",
        "game-feel": "游戏手感（game-feel）",
        "godot-signals-groups": "Godot 信号与节点组（godot-signals-groups）",
        "godot-shaders": "Godot 着色器（godot-shaders）",
        "unity-animation": "Unity 角色动画（unity-animation）",
        "skill-development": "Skill 开发规范（skill-development）",
        "hook-development": "Hook 开发（hook-development）",
        "mcp-integration": "MCP 集成（mcp-integration）",
        "product-vision": "产品愿景（product-vision）",
        "stakeholder-map": "干系人地图（stakeholder-map）",
        "bgpt-paper-search": "BGPT 论文证据检索（bgpt-paper-search）",
        "n8n-code-tool": "n8n Code Tool 编程（n8n-code-tool）",
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
