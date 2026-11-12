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

STAR_SNAPSHOT_DATE = "2026-11-03"

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
            "skills/developer/quality/security-audit/SKILL.md",
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
            "skills/developer/context/context-degradation/SKILL.md",
            "skills/developer/context/long-horizon-prompting/SKILL.md",
            "skills/developer/context/memory-systems/SKILL.md",
            "skills/developer/context/tool-design/SKILL.md",
            "skills/developer/context/multi-agent-patterns/SKILL.md",
            "skills/developer/context/bdi-mental-states/SKILL.md",
        ]),
        ("多 Agent 编排与自主学习", [
            "skills/developer/context/autonomous-loops/SKILL.md",
            "skills/developer/context/hivemind/SKILL.md",
            "skills/developer/context/continuous-learning-v2/SKILL.md",
        ]),
        ("网页动画（GSAP 官方）", [
            "skills/developer/framework/gsap-core/SKILL.md",
            "skills/developer/framework/gsap-scrolltrigger/SKILL.md",
            "skills/developer/framework/gsap-react/SKILL.md",
            "skills/developer/framework/gsap-timeline/SKILL.md",
            "skills/developer/framework/gsap-plugins/SKILL.md",
            "skills/developer/framework/gsap-frameworks/SKILL.md",
            "skills/developer/framework/gsap-performance/SKILL.md",
            "skills/developer/framework/gsap-utils/SKILL.md",
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
        ("工程结构、CI 与安全扫描治理", [
            "skills/developer/engineering/python-project-structure/SKILL.md",
            "skills/developer/engineering/gitlab-ci-patterns/SKILL.md",
            "skills/developer/quality/sast-configuration/SKILL.md",
            "skills/developer/quality/review-agent-setup/SKILL.md",
        ]),
        ("端到端修复与零幻觉编码", [
            "skills/developer/engineering/focused-fix/SKILL.md",
            "skills/developer/engineering/zero-hallucination-coder/SKILL.md",
        ]),
        ("Python 代码质量与规范", [
            "skills/developer/engineering/python-anti-patterns/SKILL.md",
            "skills/developer/engineering/python-code-style/SKILL.md",
        ]),
        ("评审、对抗审查与可观测性", [
            "skills/developer/quality/pr-review-expert/SKILL.md",
            "skills/developer/quality/adversarial-reviewer/SKILL.md",
            "skills/developer/quality/grafana-dashboards/SKILL.md",
        ]),
        ("LLM 成本优化", [
            "skills/developer/efficiency/llm-cost-optimizer/SKILL.md",
        ]),
        ("EGM 方法论与前端模式", [
            "skills/developer/engineering/egm-brainstorm/SKILL.md",
            "skills/developer/engineering/egm-draft/SKILL.md",
            "skills/developer/quality/egm-review/SKILL.md",
            "skills/developer/engineering/frontend-patterns/SKILL.md",
        ]),
        ("CI、并行开发与代码审查", [
            "skills/developer/engineering/github-actions-templates/SKILL.md",
            "skills/developer/engineering/parallel-feature-development/SKILL.md",
            "skills/developer/quality/open-code-review/SKILL.md",
            "skills/developer/quality/chaos-engineer/SKILL.md",
        ]),
        ("工程基建与第三方集成", [
            "skills/developer/engineering/turborepo-caching/SKILL.md",
            "skills/developer/engineering/recsys-pipeline-architect/SKILL.md",
            "skills/developer/engineering/linkerd-patterns/SKILL.md",
            "skills/developer/engineering/dependency-upgrade/SKILL.md",
            "skills/developer/engineering/stripe-integration-expert/SKILL.md",
        ]),
        ("服务网格流量治理", [
            "skills/developer/engineering/istio-traffic-management/SKILL.md",
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
        ("文案精修与去 AI 腔", [
            "skills/writer/writing/copy-editing/SKILL.md",
        ]),
        ("邮件与模板文案", [
            "skills/writer/writing/cold-email/SKILL.md",
            "skills/writer/writing/email-template-builder/SKILL.md",
        ]),
    ],
    "🎨 设计师": [
        ("确立 UI 美学方向", [
            "skills/designer/design/frontend-design/SKILL.md",
            "skills/designer/design/taste-skill/SKILL.md",
            "skills/designer/design/ui-ux-pro-max/SKILL.md",
            "skills/designer/design/impeccable/SKILL.md",
        ]),
        ("反 AI 味的设计与品牌判断", [
            "skills/designer/design/hallmark/SKILL.md",
        ]),
        ("等距技术插画", [
            "skills/designer/design/anatomy/SKILL.md",
        ]),
        ("游戏像素艺术特效", [
            "skills/gamedev/art/pixelfx/SKILL.md",
        ]),
        ("UI 设计全家桶（ui-ux-pro-max 系）", [
            "skills/designer/design/ui-ux-pro-max/SKILL.md",
            "skills/designer/design/design/SKILL.md",
            "skills/designer/design/design-system/SKILL.md",
            "skills/designer/design/ui-styling/SKILL.md",
            "skills/designer/design/brand/SKILL.md",
            "skills/designer/design/banner-design/SKILL.md",
            "skills/designer/design/slides/SKILL.md",
        ]),
        ("风格化视觉与创意落地页", [
            "skills/designer/design/creative/SKILL.md",
        ]),
        ("画架构图 / 流程图 / 编辑级图表", [
            "skills/designer/design/diagram-design/SKILL.md",
            "skills/designer/design/archify/SKILL.md",
        ]),
        ("极简与新粗野主义风格", [
            "skills/designer/design/minimal/SKILL.md",
            "skills/designer/design/neobrutalism/SKILL.md",
        ]),
        ("布局与设计模板", [
            "skills/designer/design/bento/SKILL.md",
            "skills/designer/design/od-blog-post/SKILL.md",
            "skills/designer/design/od-critique/SKILL.md",
        ]),
        ("玻璃拟态与编辑排版风格", [
            "skills/designer/design/glassmorphism/SKILL.md",
            "skills/designer/design/editorial/SKILL.md",
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
            "skills/researcher/science/statistical-power/SKILL.md",
        ]),
        ("文献调研与学术评审", [
            "skills/researcher/science/literature-review/SKILL.md",
            "skills/researcher/science/peer-review/SKILL.md",
            "skills/researcher/info/citation-management/SKILL.md",
        ]),
        ("科学论文写作", [
            "skills/researcher/science/scientific-writing/SKILL.md",
        ]),
        ("把书与文档变成 Skill / 摸清服务对象", [
            "skills/researcher/knowledge/book-to-skill/SKILL.md",
            "skills/researcher/knowledge/distilly/SKILL.md",
        ]),
        ("论文证据检索（BGPT）", [
            "skills/researcher/science/bgpt-paper-search/SKILL.md",
        ]),
        ("研究流水线与运营", [
            "skills/researcher/science/ml-pipeline-workflow/SKILL.md",
            "skills/researcher/knowledge/research-ops-skills/SKILL.md",
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
        ("定价、发布与增长实验", [
            "skills/growth/product/pricing/SKILL.md",
            "skills/growth/product/launch/SKILL.md",
            "skills/growth/product/ab-testing/SKILL.md",
            "skills/growth/product/marketing-psychology/SKILL.md",
        ]),
        ("产品愿景与干系人对齐", [
            "skills/growth/product/product-vision/SKILL.md",
            "skills/growth/product/stakeholder-map/SKILL.md",
        ]),
        ("内容策略、留存与客户研究", [
            "skills/growth/product/content-strategy/SKILL.md",
            "skills/growth/product/churn-prevention/SKILL.md",
            "skills/growth/product/customer-research/SKILL.md",
        ]),
        ("SEO、内容与数据", [
            "skills/growth/product/content-brief/SKILL.md",
            "skills/growth/product/keyword-research/SKILL.md",
            "skills/growth/product/sql-queries/SKILL.md",
            "skills/growth/product/schema/SKILL.md",
            "skills/growth/product/programmatic-seo/SKILL.md",
        ]),
        ("转化与引流", [
            "skills/growth/product/popups/SKILL.md",
            "skills/growth/product/signup/SKILL.md",
            "skills/growth/product/free-tools/SKILL.md",
        ]),
        ("联合营销", [
            "skills/growth/product/co-marketing/SKILL.md",
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
        ("引擎进阶：信号、着色器与动画", [
            "skills/gamedev/godot-signals-groups/SKILL.md",
            "skills/gamedev/godot-shaders/SKILL.md",
            "skills/gamedev/unity-animation/SKILL.md",
        ]),
        ("手感与反馈（game feel）", [
            "skills/gamedev/game-feel/SKILL.md",
        ]),
        ("NavMesh、Game Jam 与快速原型", [
            "skills/gamedev/unity-navmesh/SKILL.md",
            "skills/gamedev/game-jam/SKILL.md",
            "skills/gamedev/prototype-fast/SKILL.md",
        ]),
        ("系统与关卡设计", [
            "skills/gamedev/input-systems/SKILL.md",
            "skills/gamedev/performance-optimization/SKILL.md",
            "skills/gamedev/level-design/SKILL.md",
            "skills/gamedev/save-systems/SKILL.md",
            "skills/gamedev/threejs-scene-setup/SKILL.md",
        ]),
        ("引擎进阶：Tilemap / Niagara / 镜头", [
            "skills/gamedev/unity-tilemap-2d/SKILL.md",
            "skills/gamedev/unreal-niagara/SKILL.md",
            "skills/gamedev/camera-systems/SKILL.md",
        ]),
    ],
    "🎬 创作者": [
        ("做电影级产品视频", [
            "skills/creator/video/video-shotcraft/SKILL.md",
        ]),
        ("做网页幻灯片", [
            "skills/creator/slides/frontend-slides/SKILL.md",
        ]),
        ("视频内容策略", [
            "skills/creator/video/video-content-strategist/SKILL.md",
        ]),
    ],
    "🏢 Corporate Functions（企业职能岗）": [
        ("财务/投资分析（投资人方法论）", [
            "skills/corporate/finance/buffett/SKILL.md",
            "skills/corporate/finance/munger/SKILL.md",
            "skills/corporate/finance/dalio-principles-allweather/SKILL.md",
            "skills/corporate/finance/graham-net-net/SKILL.md",
        ]),
        ("财经舆情监控与情绪分析", [
            "skills/corporate/finance/alphaear-news/SKILL.md",
            "skills/corporate/finance/alphaear-sentiment/SKILL.md",
        ]),
        ("供应链瓶颈研究（A 股科技/先进制造）", [
            "skills/corporate/supply-chain/serenity-skill/SKILL.md",
        ]),
        ("销售：客户画像与线索资格", [
            "skills/corporate/sales/sales-icp/SKILL.md",
            "skills/corporate/sales/sales-qualify/SKILL.md",
            "skills/corporate/sales/sales-research/SKILL.md",
        ]),
        ("销售：冷触达与方案赢单", [
            "skills/corporate/sales/sales-outreach/SKILL.md",
            "skills/corporate/sales/sales-proposal/SKILL.md",
        ]),
        ("电商：选品、定价与客户反馈", [
            "skills/corporate/ecommerce/dropshipping-product-research/SKILL.md",
            "skills/corporate/ecommerce/competitor-price-analysis/SKILL.md",
            "skills/corporate/ecommerce/customer-feedback-analysis/SKILL.md",
        ]),
        ("合同与提案撰写", [
            "skills/corporate/sales/contract-and-proposal-writer/SKILL.md",
        ]),
        ("会议分析", [
            "skills/corporate/sales/meeting-analyzer/SKILL.md",
        ]),
    ],
    "🧰 通用工具（所有职业）": [
        ("浏览器自动化", [
            "skills/toolbox/automation/browser-act/SKILL.md",
        ]),
        ("n8n 工作流", [
            "skills/toolbox/automation/n8n-error-handling/SKILL.md",
            "skills/toolbox/automation/n8n-code-javascript/SKILL.md",
            "skills/toolbox/automation/n8n-code-tool/SKILL.md",
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
        ("Obsidian 知识库操作（官方）", [
            "skills/toolbox/obsidian/obsidian-cli/SKILL.md",
            "skills/toolbox/obsidian/obsidian-markdown/SKILL.md",
            "skills/toolbox/obsidian/obsidian-bases/SKILL.md",
            "skills/toolbox/obsidian/json-canvas/SKILL.md",
            "skills/toolbox/obsidian/defuddle/SKILL.md",
            "skills/toolbox/obsidian/knap/SKILL.md",
        ]),
        ("GCP gcloud 命令护栏（官方）", [
            "skills/toolbox/cloud/gcloud/SKILL.md",
        ]),
        ("Claude Code 插件开发（官方）", [
            "skills/toolbox/meta/skill-development/SKILL.md",
            "skills/toolbox/meta/hook-development/SKILL.md",
            "skills/toolbox/meta/mcp-integration/SKILL.md",
        ]),
        ("文件格式转换与 n8n 进阶", [
            "skills/toolbox/automation/file-conversion/SKILL.md",
            "skills/toolbox/automation/using-n8n-mcp-skills/SKILL.md",
            "skills/toolbox/automation/n8n-multi-instance/SKILL.md",
        ]),
        ("PPT 生成与 n8n 进阶", [
            "skills/toolbox/office/2slides-ppt-generator/SKILL.md",
            "skills/toolbox/automation/n8n-agents/SKILL.md",
            "skills/toolbox/automation/n8n-expression-syntax/SKILL.md",
        ]),
        ("Hook 与提示词治理", [
            "skills/toolbox/meta/block-no-verify-hook/SKILL.md",
            "skills/toolbox/meta/prompt-governance/SKILL.md",
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

    def star_of(up: dict) -> int:
        """取最新快照 star 数；取不到按 -1 排到末尾。"""
        v = up.get(f"stars_snapshot_{STAR_SNAPSHOT_DATE}")
        if not isinstance(v, int):
            v = up.get("stars_snapshot_2026-10-25")
        if not isinstance(v, int):
            v = up.get("stars_snapshot_2026-10-24")
        if not isinstance(v, int):
            snaps = [val for k, val in up.items()
                     if k.startswith("stars_snapshot_") and isinstance(val, int)]
            v = snaps[-1] if snaps else -1
        return v

    lines = [
        "| 上游 | Star | License | 模式 | 翻译件 | 原样件 | 最近同步 |",
        "|---|--:|---|:-:|--:|--:|---|",
    ]
    # 批次仍存于 manifest（batch 字段），此处不再展示，只按 star 降序排
    for up in sorted(manifest["upstreams"], key=star_of, reverse=True):
        repo = up["repo"]
        stars = star_of(up)
        star_cell = f"{stars:,}" if stars >= 0 else "—"
        head = repos.get(repo, "")
        head_cell = (
            f"[`{head[:7]}`](https://github.com/{repo}/commit/{head})" if head else "—"
        )
        # 翻译件 = SKILL.md/Agent 定义 + 已译散文（references/*.md 等）
        n_t = len(up.get("files", [])) + len(up.get("translated_prose", []))
        n_v = len(up.get("verbatim", []))
        mode = MODE_ZH.get(up.get("mode", ""), up.get("mode", "") or "?")
        lines.append(
            f"| [{repo}](https://github.com/{repo}) | {star_cell} | {up.get('license','?')} "
            f"| {mode} | {n_t} | {n_v} | {head_cell} |"
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
        "## 按职业 / 目的筛选推荐\n\n" + recommendations() + "\n"
        "## 上游仓库登记表\n\n" + upstream_table() + "\n"
    )
    if args.write:
        OUT.write_text(body, encoding="utf-8")
        print(f"已写入 {OUT.relative_to(ROOT)}")
    else:
        print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
