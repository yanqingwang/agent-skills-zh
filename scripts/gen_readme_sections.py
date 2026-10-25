#!/usr/bin/env python3
"""生成 README 两个章节的 Markdown 片段：

1. 上游仓库登记表（含 star 数，完整数字不用 k）——由 data/manifest.json + data/sync-state.json 生成
2. 按职业/目的筛选推荐（按职业分类的 skill 组合，带汉化 SKILL.md 直达链接）

设计约束：
- 只读 manifest / sync-state / SKILL.md frontmatter，不写这两个文件之外的任何东西
- 推荐规则集中在 RECOMMENDATIONS，可按需扩充（新 skill 收录后在此登记）
用法：python3 scripts/gen_readme_sections.py           # 打印到 stdout
     python3 scripts/gen_readme_sections.py --write    # 覆写 data/readme-sections.md
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "manifest.json"
STATE = ROOT / "data" / "sync-state.json"
OUT = ROOT / "data" / "readme-sections.md"

STAR_SNAPSHOT_DATE = "2026-10-25"

# 职业 → 该职业下的「目的」→ 推荐的本地 skill 路径（相对仓库根）
# 路径必须存在于 manifest 的 files 列表内，否则生成时告警。
RECOMMENDATIONS: dict[str, list[tuple[str, list[str]]]] = {
    "💻 开发者": [
        ("动手前先把需求和风险想清楚", [
            "skills/developer/engineering/brainstorming/SKILL.md",
            "skills/developer/engineering/idea-refine/SKILL.md",
            "skills/developer/engineering/before-you-build/SKILL.md",
        ]),
        ("把想法落成规格与计划", [
            "skills/developer/engineering/writing-plans/SKILL.md",
            "skills/developer/engineering/to-spec/SKILL.md",
            "skills/developer/engineering/planning-with-files/SKILL.md",
        ]),
        ("写代码与修 bug", [
            "skills/developer/engineering/test-driven-development/SKILL.md",
            "skills/developer/engineering/systematic-debugging/SKILL.md",
            "skills/developer/engineering/ponytail/SKILL.md",
            "skills/developer/engineering/search-first/SKILL.md",
        ]),
        ("提交前自证完工", [
            "skills/developer/engineering/verification-before-completion/SKILL.md",
            "skills/developer/engineering/workflow-ship-change/SKILL.md",
        ]),
        ("代码与安全审查", [
            "skills/developer/quality/code-review/SKILL.md",
            "skills/developer/quality/code-reviewer/SKILL.md",
            "skills/developer/quality/agents/code-reviewer.md",
            "skills/developer/quality/security-review/SKILL.md",
        ]),
        ("API 与后端骨架", [
            "skills/developer/quality/api-designer/SKILL.md",
            "skills/developer/quality/fastapi-templates/SKILL.md",
            "skills/developer/engineering/build-mcp-server/SKILL.md",
        ]),
        ("上下文与长会话管理", [
            "skills/developer/context/context-engineering/SKILL.md",
            "skills/developer/context/strategic-compact/SKILL.md",
            "skills/developer/context/claude-md-improver/SKILL.md",
        ]),
        ("多 Agent 编排与自主学习", [
            "skills/developer/context/autonomous-loops/SKILL.md",
            "skills/developer/context/hivemind/SKILL.md",
            "skills/developer/context/continuous-learning-v2/SKILL.md",
        ]),
        ("省 token 与输出可读性", [
            "skills/developer/efficiency/caveman/SKILL.md",
            "skills/developer/efficiency/i-have-adhd/SKILL.md",
        ]),
        ("团队评审与 QA（gstack）", [
            "skills/developer/gstack/plan-ceo-review/SKILL.md",
            "skills/developer/gstack/qa/SKILL.md",
            "skills/developer/gstack/office-hours/SKILL.md",
        ]),
    ],
    "✍️ 写作者": [
        ("去掉 AI 腔、让文字像人写的", [
            "skills/writer/writing/humanizer/SKILL.md",
        ]),
        ("项目宣传与发布文案", [
            "skills/writer/writing/brag/SKILL.md",
        ]),
        ("为具体 AI 工具写提示词", [
            "skills/writer/prompting/prompt-master/SKILL.md",
        ]),
    ],
    "🎨 设计师": [
        ("确立 UI 美学方向", [
            "skills/designer/design/frontend-design/SKILL.md",
            "skills/designer/design/taste-skill/SKILL.md",
        ]),
        ("风格化视觉与创意落地页", [
            "skills/designer/design/creative/SKILL.md",
        ]),
        ("画架构图 / 流程图 / 编辑级图表", [
            "skills/designer/design/diagram-design/SKILL.md",
            "skills/designer/design/archify/SKILL.md",
        ]),
    ],
    "🔬 研究者": [
        ("摸清一个陌生代码库", [
            "skills/researcher/analysis/understand/SKILL.md",
            "skills/researcher/analysis/reverse-engineer-anything/SKILL.md",
        ]),
        ("追近 30 天真实讨论与舆情", [
            "skills/researcher/info/last30days/SKILL.md",
        ]),
        ("论文检索与改进", [
            "skills/researcher/science/arxiv/SKILL.md",
            "skills/researcher/science/auto-paper-improvement-loop/SKILL.md",
            "skills/researcher/science/autoresearch/SKILL.md",
        ]),
        ("实验与研究设计", [
            "skills/researcher/science/experimental-design/SKILL.md",
        ]),
        ("把书与文档变成 Skill / 摸清服务对象", [
            "skills/researcher/knowledge/book-to-skill/SKILL.md",
            "skills/researcher/knowledge/distilly/SKILL.md",
        ]),
    ],
    "📈 产品与增长": [
        ("验证机会与问题-方案契合", [
            "skills/growth/product/product-discovery/SKILL.md",
            "skills/growth/product/create-prd/SKILL.md",
        ]),
        ("定位与营销上下文", [
            "skills/growth/product/product-marketing/SKILL.md",
        ]),
        ("SEO 审计与优化", [
            "skills/growth/product/seo-audit/SKILL.md",
            "skills/growth/product/seo-agentic/SKILL.md",
        ]),
        ("对齐『说的』与『做的』", [
            "skills/growth/product/intended-vs-implemented/SKILL.md",
        ]),
        ("量化研究与数据把关", [
            "skills/growth/product/backtest-expert/SKILL.md",
            "skills/growth/product/data-quality-checker/SKILL.md",
        ]),
    ],
    "🎮 游戏开发者": [
        ("引擎内脚本与玩法", [
            "skills/gamedev/godot-gdscript/SKILL.md",
            "skills/gamedev/unity-csharp-scripting/SKILL.md",
            "skills/gamedev/unreal-cpp-gameplay/SKILL.md",
        ]),
        ("机制设计与创意方向", [
            "skills/gamedev/agents/game-designer.md",
            "skills/gamedev/agents/creative-director.md",
        ]),
    ],
    "🎬 创作者": [
        ("做电影级产品视频", [
            "skills/creator/video/video-shotcraft/SKILL.md",
        ]),
    ],
    "🧰 通用工具（所有职业）": [
        ("浏览器自动化", [
            "skills/toolbox/automation/browser-act/SKILL.md",
        ]),
        ("n8n 工作流", [
            "skills/toolbox/automation/n8n-error-handling/SKILL.md",
            "skills/toolbox/automation/n8n-code-javascript/SKILL.md",
        ]),
        ("Office 文档生成与校对", [
            "skills/toolbox/office/officecli/SKILL.md",
        ]),
        ("把文档/站点转成 Skill", [
            "skills/toolbox/meta/skill-seekers/SKILL.md",
            "skills/toolbox/meta/nvidia-skill-finder/SKILL.md",
        ]),
        ("GPU 数据处理（cuDF / pandas 加速）", [
            "skills/toolbox/compute/accelerated-computing-cudf/SKILL.md",
        ]),
        ("NotebookLM 知识库操作", [
            "skills/toolbox/automation/notebooklm/SKILL.md",
        ]),
        ("受治理的 vibe coding 运行时", [
            "skills/toolbox/framework/vibe-skills/SKILL.md",
        ]),
    ],
}

MODE_ZH = {
    "整仓": "整仓",
    "整仓收录": "整仓",
    "整目录": "整目录",
    "单文件": "单文件",
    "引用集": "引用集",
    "抽取": "抽取",
    "旗舰抽取": "抽取",
    "Agent 定义": "Agent 定义",
    "Agent 定义抽取": "Agent 定义",
    "规则型": "规则型",
    "规则型（新）": "规则型",
}


def load_json(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def upstream_table() -> str:
    manifest = load_json(MANIFEST)
    state = load_json(STATE)
    repos = state.get("repos", {})

    lines = [
        "| 上游 | Star | License | 批次 | 模式 | 翻译件 | 原样件 | 最近同步 |",
        "|---|--:|---|:-:|:-:|--:|--:|---|",
    ]
    for up in manifest["upstreams"]:
        repo = up["repo"]
        stars = up.get(f"stars_snapshot_{STAR_SNAPSHOT_DATE}")
        if stars is None:
            # 兼容旧键名（2026-10-24 快照），取不到再退回 '—'
            stars = up.get("stars_snapshot_2026-10-24")
        star_cell = f"{stars:,}" if isinstance(stars, int) else "—"
        head = repos.get(repo, "")
        head_cell = (
            f"[`{head[:7]}`](https://github.com/{repo}/commit/{head})" if head else "—"
        )
        n_t = len(up.get("files", []))
        n_v = len(up.get("verbatim", []))
        mode = MODE_ZH.get(up.get("mode", ""), up.get("mode", "") or "?")
        batch = up.get("batch", "?")
        lines.append(
            f"| [{repo}](https://github.com/{repo}) | {star_cell} | {up.get('license','?')} "
            f"| {batch} | {mode} | {n_t} | {n_v} | {head_cell} |"
        )
    return "\n".join(lines)


def recommendations() -> str:
    manifest = load_json(MANIFEST)
    valid = {
        f["local"]
        for up in manifest["upstreams"]
        for f in up.get("files", [])
    }

    def label(path: str) -> str:
        name = re.search(r"^name:\s*(.+)$",
                         pathlib.Path(ROOT / path).read_text(encoding="utf-8"),
                         re.M)
        base = (name.group(1).strip() if name else pathlib.Path(path).parent.name)
        # Agent 定义型文件（agents/*.md）与 Skill 同名时加后缀区分
        if pathlib.Path(path).parent.name == "agents":
            base += " Agent"
        return base

    out: list[str] = []
    missing: list[str] = []
    for persona, goals in RECOMMENDATIONS.items():
        out.append(f"### {persona}\n")
        for goal, paths in goals:
            items = []
            for p in paths:
                if p not in valid:
                    missing.append(p)
                    continue
                items.append(f"[{label(p)}]({p})")
            out.append(f"- **{goal}** → {' · '.join(items)}")
        out.append("")

    if missing:
        print("[warn] 以下推荐路径不在 manifest.files 中（未收录或路径写错）：",
              file=sys.stderr)
        for m in sorted(set(missing)):
            print("  -", m, file=sys.stderr)
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="覆写 data/readme-sections.md")
    args = ap.parse_args()

    body = (
        "<!-- 由 scripts/gen_readme_sections.py 生成，勿手改 -->\n\n"
        "## 上游仓库登记表\n\n" + upstream_table() + "\n\n"
        "## 按职业 / 目的筛选推荐\n\n" + recommendations()
    )
    if args.write:
        OUT.write_text(body, encoding="utf-8")
        print(f"已写入 {OUT.relative_to(ROOT)}")
    else:
        print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
