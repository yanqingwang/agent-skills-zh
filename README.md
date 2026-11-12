# Agent Skills 中文汉化库（agent-skills-zh）

> 将 GitHub 上最受欢迎的 Agent Skills 系统性汉化为中文，服务中文 AI 编程用户。
> **本仓库只做翻译，不做原创**——原创人物视角 Skills 另见独立仓库（原则 #7）。

**上游星标快照日期：2026-11-03** · 完整数据见 [data/upstream-inventory.md](data/upstream-inventory.md) · **工作状态**（收录规模/监控/待重译，CI 每日更新）见 [data/STATUS.md](data/STATUS.md)

## 按用户角色浏览

`skills/` 目录按**你是谁、你要做什么**组织，整个目录复制即可用：

| 你是… | 去这里 | 里面有什么 |
|---|---|---|
| 💻 **开发者** | `skills/developer/` | <ul><li><strong>engineering/</strong>：<a href="skills/developer/engineering/test-driven-development/SKILL.md">TDD</a>、<a href="skills/developer/engineering/systematic-debugging/SKILL.md">系统化调试</a>、<a href="skills/developer/engineering/writing-plans/SKILL.md">写计划</a>、<a href="skills/developer/engineering/ponytail/SKILL.md">ponytail 最小改动</a>、<a href="skills/developer/engineering/before-you-build/SKILL.md">before-you-build</a> 等</li><li><strong>quality/</strong>：<a href="skills/developer/quality/code-review/SKILL.md">代码审查</a>、<a href="skills/developer/quality/security-review/SKILL.md">安全审查</a>、<a href="skills/developer/quality/security-audit/SKILL.md">security-audit 多阶段安全审计（Cloudflare）</a>、<a href="skills/developer/quality/api-designer/SKILL.md">API 设计</a>、<a href="skills/developer/quality/agents/code-reviewer.md">代码审查者 Agent</a></li><li><strong>context/</strong>：<a href="skills/developer/context/context-engineering/SKILL.md">上下文工程</a>、<a href="skills/developer/context/context-degradation/SKILL.md">上下文退化诊治</a>、<a href="skills/developer/context/long-horizon-prompting/SKILL.md">长程启动提示词</a>、<a href="skills/developer/context/continuous-learning-v2/SKILL.md">持续学习</a>、<a href="skills/developer/context/autonomous-loops/SKILL.md">自主循环</a>、<a href="skills/developer/context/hivemind/SKILL.md">hivemind 编排</a>、<a href="skills/developer/context/claude-md-improver/SKILL.md">CLAUDE.md 优化</a></li><li><strong>framework/</strong>：<a href="skills/developer/framework/gsap-core/SKILL.md">GSAP 核心</a>、<a href="skills/developer/framework/gsap-scrolltrigger/SKILL.md">ScrollTrigger</a>、<a href="skills/developer/framework/gsap-react/SKILL.md">GSAP React（官方）</a></li><li><strong>efficiency/</strong>：<a href="skills/developer/efficiency/caveman/SKILL.md">caveman 省 token</a>、<a href="skills/developer/efficiency/i-have-adhd/SKILL.md">i-have-adhd 输出格式</a></li><li><strong>gstack/</strong>：<a href="skills/developer/gstack/SKILL.md">Garry Tan 整仓工具链，23+ 角色</a></li></ul> |
| ✍️ **写作者** | `skills/writer/` | <ul><li><strong>writing/</strong>：<a href="skills/writer/writing/humanizer/SKILL.md">humanizer 去 AI 腔</a>、<a href="skills/writer/writing/brag/SKILL.md">brag 项目文案</a></li><li><strong>prompting/</strong>：<a href="skills/writer/prompting/prompt-master/SKILL.md">prompt-master 提示词工程</a></li></ul> |
| 🎨 **设计师** | `skills/designer/design/` | <ul><li><a href="skills/designer/design/taste-skill/SKILL.md">taste 设计品味</a></li><li><a href="skills/designer/design/diagram-design/SKILL.md">diagram-design 编辑级图表</a></li><li><a href="skills/designer/design/archify/SKILL.md">archify 交互图表</a></li><li><a href="skills/designer/design/frontend-design/SKILL.md">frontend-design（官方）</a></li><li><a href="skills/designer/design/creative/SKILL.md">creative 风格设计</a></li><li><a href="skills/designer/design/ui-ux-pro-max/SKILL.md">ui-ux-pro-max 设计智能（144k★）</a></li><li><a href="skills/designer/design/impeccable/SKILL.md">impeccable 无可挑剔前端</a></li><li><a href="skills/designer/design/hallmark/SKILL.md">hallmark 反 AI 味设计</a></li><li><a href="skills/designer/design/anatomy/SKILL.md">anatomy 等距技术插画</a></li><li><strong>ui-ux-pro-max 系全家桶</strong>：<a href="skills/designer/design/design/SKILL.md">design</a>、<a href="skills/designer/design/design-system/SKILL.md">design-system</a>、<a href="skills/designer/design/ui-styling/SKILL.md">ui-styling</a>、<a href="skills/designer/design/brand/SKILL.md">brand</a>、<a href="skills/designer/design/banner-design/SKILL.md">banner-design</a>、<a href="skills/designer/design/slides/SKILL.md">slides</a></li></ul> |
| 🔬 **研究者** | `skills/researcher/` | <ul><li><strong>analysis/</strong>：<a href="skills/researcher/analysis/reverse-engineer-anything/SKILL.md">REA 逆向工程</a>、<a href="skills/researcher/analysis/understand/SKILL.md">understand 代码知识图谱</a></li><li><strong>science/</strong>：<a href="skills/researcher/science/experimental-design/SKILL.md">实验设计</a>、<a href="skills/researcher/science/autoresearch/SKILL.md">autoresearch</a>、<a href="skills/researcher/science/auto-paper-improvement-loop/SKILL.md">论文改进循环</a>、<a href="skills/researcher/science/arxiv/SKILL.md">arxiv</a></li><li><strong>info/</strong>：<a href="skills/researcher/info/last30days/SKILL.md">last30days 近 30 天调研</a></li><li><strong>knowledge/</strong>：<a href="skills/researcher/knowledge/book-to-skill/SKILL.md">book-to-skill</a>、<a href="skills/researcher/knowledge/distilly/SKILL.md">distilly 人物画像</a></li></ul> |
| 📈 **产品与增长** | `skills/growth/product/` | <ul><li><a href="skills/growth/product/product-marketing/SKILL.md">product-marketing</a></li><li><a href="skills/growth/product/product-discovery/SKILL.md">product-discovery</a></li><li><a href="skills/growth/product/create-prd/SKILL.md">create-prd</a></li><li><a href="skills/growth/product/intended-vs-implemented/SKILL.md">intended-vs-implemented</a></li><li><a href="skills/growth/product/seo-agentic/SKILL.md">seo-agentic</a> / <a href="skills/growth/product/seo-audit/SKILL.md">seo-audit</a></li><li><a href="skills/growth/product/backtest-expert/SKILL.md">回测</a>与<a href="skills/growth/product/data-quality-checker/SKILL.md">数据质量</a>（⚠️ 金融内容非投资建议）</li></ul> |
| 🎮 **游戏开发者** | `skills/gamedev/` | <ul><li><a href="skills/gamedev/godot-gdscript/SKILL.md">Godot GDScript</a> / <a href="skills/gamedev/unity-csharp-scripting/SKILL.md">Unity C#</a> / <a href="skills/gamedev/unreal-cpp-gameplay/SKILL.md">Unreal C++</a> 三大引擎核心</li><li><a href="skills/gamedev/agents/game-designer.md">游戏设计师</a> / <a href="skills/gamedev/agents/creative-director.md">创意总监</a> Agent</li><li><strong>art/</strong>：<a href="skills/gamedev/art/pixelfx/SKILL.md">pixelfx 像素艺术特效（244 个代码级特效）</a></li></ul> |
| 🎬 **创作者** | `skills/creator/` | <ul><li><strong>video/</strong>：<a href="skills/creator/video/video-shotcraft/SKILL.md">video-shotcraft 电影级产品视频</a></li><li><strong>slides/</strong>：<a href="skills/creator/slides/frontend-slides/SKILL.md">frontend-slides 网页幻灯片</a></li></ul> |
| 🏢 **Corporate Functions（企业职能岗）** | `skills/corporate/` | <ul><li><strong>finance/</strong>：<a href="skills/corporate/finance/buffett/SKILL.md">巴菲特式价值复利</a>、<a href="skills/corporate/finance/munger/SKILL.md">芒格心智模型</a>、<a href="skills/corporate/finance/dalio-principles-allweather/SKILL.md">达利欧全天候</a>、<a href="skills/corporate/finance/graham-net-net/SKILL.md">格雷厄姆净净资产</a>、<a href="skills/corporate/finance/alphaear-news/SKILL.md">财经热点</a>、<a href="skills/corporate/finance/alphaear-sentiment/SKILL.md">文本情绪分析</a></li><li><strong>supply-chain/</strong>：<a href="skills/corporate/supply-chain/serenity-skill/SKILL.md">供应链瓶颈研究</a></li><li><strong>sales/</strong>：<a href="skills/corporate/sales/sales-icp/SKILL.md">理想客户画像</a>、<a href="skills/corporate/sales/sales-qualify/SKILL.md">BANT+MEDDIC 资格评估</a>、<a href="skills/corporate/sales/sales-outreach/SKILL.md">冷触达序列</a>、<a href="skills/corporate/sales/sales-proposal/SKILL.md">销售方案</a>、<a href="skills/corporate/sales/sales-research/SKILL.md">公司调研</a></li><li><strong>ecommerce/</strong>：<a href="skills/corporate/ecommerce/dropshipping-product-research/SKILL.md">选品调研</a>、<a href="skills/corporate/ecommerce/competitor-price-analysis/SKILL.md">竞品价格分析</a>、<a href="skills/corporate/ecommerce/customer-feedback-analysis/SKILL.md">客户反馈分析</a></li></ul> |
| 🧰 **所有人在用的工具** | `skills/toolbox/` | <ul><li><strong>automation/</strong>：<a href="skills/toolbox/automation/n8n-code-javascript/SKILL.md">n8n 代码节点</a>、<a href="skills/toolbox/automation/n8n-error-handling/SKILL.md">n8n 错误处理</a>、<a href="skills/toolbox/automation/browser-act/SKILL.md">browser-act</a>、<a href="skills/toolbox/automation/notebooklm/SKILL.md">notebooklm</a></li><li><strong>meta/</strong>：<a href="skills/toolbox/meta/skill-seekers/SKILL.md">skill-seekers 文档转 skill</a>、<a href="skills/toolbox/meta/nvidia-skill-finder/SKILL.md">NVIDIA 技能发现器</a></li><li><strong>office/</strong>：<a href="skills/toolbox/office/officecli/SKILL.md">officecli</a></li><li><strong>compute/</strong>：<a href="skills/toolbox/compute/accelerated-computing-cudf/SKILL.md">GPU cuDF</a></li><li><strong>framework/</strong>：<a href="skills/toolbox/framework/vibe-skills/SKILL.md">vibe 运行时</a></li><li><strong>obsidian/</strong>：<a href="skills/toolbox/obsidian/obsidian-cli/SKILL.md">Obsidian CLI</a>、<a href="skills/toolbox/obsidian/obsidian-markdown/SKILL.md">Markdown 方言</a>、<a href="skills/toolbox/obsidian/obsidian-bases/SKILL.md">Bases</a>、<a href="skills/toolbox/obsidian/json-canvas/SKILL.md">JSON Canvas</a>、<a href="skills/toolbox/obsidian/defuddle/SKILL.md">defuddle 正文抽取</a>、<a href="skills/toolbox/obsidian/knap/SKILL.md">knap 格式体检（官方）</a></li><li><strong>cloud/</strong>：<a href="skills/toolbox/cloud/gcloud/SKILL.md">gcloud 命令护栏（Google 官方）</a></li></ul> |

> 完整索引（含每件的上游链接）：[data/category-index.md](data/category-index.md)，由 [scripts/classify.py](scripts/classify.py) 按目录结构自动生成。

### 💻 开发者

- **动手前先把需求和风险想清楚** → [brainstorming](skills/developer/engineering/brainstorming/SKILL.md) · [idea-refine](skills/developer/engineering/idea-refine/SKILL.md) · [before-you-build](skills/developer/engineering/before-you-build/SKILL.md)
- **把想法落成规格与计划** → [writing-plans](skills/developer/engineering/writing-plans/SKILL.md) · [to-spec](skills/developer/engineering/to-spec/SKILL.md) · [planning-with-files](skills/developer/engineering/planning-with-files/SKILL.md)
- **写代码与修 bug** → [test-driven-development](skills/developer/engineering/test-driven-development/SKILL.md) · [systematic-debugging](skills/developer/engineering/systematic-debugging/SKILL.md) · [ponytail](skills/developer/engineering/ponytail/SKILL.md) · [search-first](skills/developer/engineering/search-first/SKILL.md)
- **提交前自证完工** → [verification-before-completion](skills/developer/engineering/verification-before-completion/SKILL.md) · [workflow-ship-change](skills/developer/engineering/workflow-ship-change/SKILL.md)
- **代码与安全审查** → [code-review](skills/developer/quality/code-review/SKILL.md) · [code-reviewer](skills/developer/quality/code-reviewer/SKILL.md) · [code-reviewer Agent](skills/developer/quality/agents/code-reviewer.md) · [security-review](skills/developer/quality/security-review/SKILL.md) · [security-audit](skills/developer/quality/security-audit/SKILL.md)
- **API 与后端骨架** → [api-designer](skills/developer/quality/api-designer/SKILL.md) · [fastapi-templates](skills/developer/quality/fastapi-templates/SKILL.md) · [build-mcp-server](skills/developer/engineering/build-mcp-server/SKILL.md)
- **上下文与长会话管理** → [context-engineering](skills/developer/context/context-engineering/SKILL.md) · [strategic-compact](skills/developer/context/strategic-compact/SKILL.md) · [claude-md-improver](skills/developer/context/claude-md-improver/SKILL.md) · [context-degradation](skills/developer/context/context-degradation/SKILL.md) · [long-horizon-prompting](skills/developer/context/long-horizon-prompting/SKILL.md) · [memory-systems](skills/developer/context/memory-systems/SKILL.md) · [tool-design](skills/developer/context/tool-design/SKILL.md) · [multi-agent-patterns](skills/developer/context/multi-agent-patterns/SKILL.md) · [bdi-mental-states](skills/developer/context/bdi-mental-states/SKILL.md)
- **多 Agent 编排与自主学习** → [autonomous-loops](skills/developer/context/autonomous-loops/SKILL.md) · [hivemind](skills/developer/context/hivemind/SKILL.md) · [continuous-learning-v2](skills/developer/context/continuous-learning-v2/SKILL.md)
- **网页动画（GSAP 官方）** → [gsap-core](skills/developer/framework/gsap-core/SKILL.md) · [gsap-scrolltrigger](skills/developer/framework/gsap-scrolltrigger/SKILL.md) · [gsap-react](skills/developer/framework/gsap-react/SKILL.md) · [gsap-timeline](skills/developer/framework/gsap-timeline/SKILL.md) · [gsap-plugins](skills/developer/framework/gsap-plugins/SKILL.md) · [gsap-frameworks](skills/developer/framework/gsap-frameworks/SKILL.md) · [gsap-performance](skills/developer/framework/gsap-performance/SKILL.md) · [gsap-utils](skills/developer/framework/gsap-utils/SKILL.md)
- **省 token 与输出可读性** → [caveman](skills/developer/efficiency/caveman/SKILL.md) · [i-have-adhd](skills/developer/efficiency/i-have-adhd/SKILL.md)
- **团队评审与 QA（gstack）** → [plan-ceo-review](skills/developer/gstack/plan-ceo-review/SKILL.md) · [qa](skills/developer/gstack/qa/SKILL.md) · [office-hours](skills/developer/gstack/office-hours/SKILL.md)
- **工程结构、CI 与安全扫描治理** → [python-project-structure](skills/developer/engineering/python-project-structure/SKILL.md) · [gitlab-ci-patterns](skills/developer/engineering/gitlab-ci-patterns/SKILL.md) · [sast-configuration](skills/developer/quality/sast-configuration/SKILL.md) · [review-agent-setup](skills/developer/quality/review-agent-setup/SKILL.md)
- **端到端修复与零幻觉编码** → ["focused-fix"](skills/developer/engineering/focused-fix/SKILL.md) · [zero-hallucination-coder](skills/developer/engineering/zero-hallucination-coder/SKILL.md)
- **Python 代码质量与规范** → [python-anti-patterns](skills/developer/engineering/python-anti-patterns/SKILL.md) · [python-code-style](skills/developer/engineering/python-code-style/SKILL.md)
- **评审、对抗审查与可观测性** → ["pr-review-expert"](skills/developer/quality/pr-review-expert/SKILL.md) · ["adversarial-reviewer"](skills/developer/quality/adversarial-reviewer/SKILL.md) · [grafana-dashboards](skills/developer/quality/grafana-dashboards/SKILL.md)
- **LLM 成本优化** → [llm-cost-optimizer](skills/developer/efficiency/llm-cost-optimizer/SKILL.md)

### ✍️ 写作者

- **去掉 AI 腔、让文字像人写的** → [humanizer](skills/writer/writing/humanizer/SKILL.md)
- **项目宣传与发布文案** → [brag](skills/writer/writing/brag/SKILL.md)
- **为具体 AI 工具写提示词** → [prompt-master](skills/writer/prompting/prompt-master/SKILL.md)
- **文案精修与去 AI 腔** → [copy-editing](skills/writer/writing/copy-editing/SKILL.md)

### 🎨 设计师

- **确立 UI 美学方向** → [frontend-design](skills/designer/design/frontend-design/SKILL.md) · [design-taste-frontend](skills/designer/design/taste-skill/SKILL.md) · [ui-ux-pro-max](skills/designer/design/ui-ux-pro-max/SKILL.md) · [impeccable](skills/designer/design/impeccable/SKILL.md)
- **反 AI 味的设计与品牌判断** → [hallmark](skills/designer/design/hallmark/SKILL.md)
- **等距技术插画** → [anatomy](skills/designer/design/anatomy/SKILL.md)
- **游戏像素艺术特效** → [pixelfx](skills/gamedev/art/pixelfx/SKILL.md)
- **UI 设计全家桶（ui-ux-pro-max 系）** → [ui-ux-pro-max](skills/designer/design/ui-ux-pro-max/SKILL.md) · [design](skills/designer/design/design/SKILL.md) · [design-system](skills/designer/design/design-system/SKILL.md) · [ui-styling](skills/designer/design/ui-styling/SKILL.md) · [brand](skills/designer/design/brand/SKILL.md) · [banner-design](skills/designer/design/banner-design/SKILL.md) · [slides](skills/designer/design/slides/SKILL.md)
- **风格化视觉与创意落地页** → [creative](skills/designer/design/creative/SKILL.md)
- **画架构图 / 流程图 / 编辑级图表** → [diagram-design](skills/designer/design/diagram-design/SKILL.md) · [archify](skills/designer/design/archify/SKILL.md)
- **极简与新粗野主义风格** → [minimal](skills/designer/design/minimal/SKILL.md) · [neobrutalism](skills/designer/design/neobrutalism/SKILL.md)

### 🔬 研究者

- **摸清一个陌生代码库** → [understand](skills/researcher/analysis/understand/SKILL.md) · [reverse-engineer-anything](skills/researcher/analysis/reverse-engineer-anything/SKILL.md)
- **追近 30 天真实讨论与舆情** → [last30days](skills/researcher/info/last30days/SKILL.md)
- **论文检索与改进** → [arxiv](skills/researcher/science/arxiv/SKILL.md) · [auto-paper-improvement-loop](skills/researcher/science/auto-paper-improvement-loop/SKILL.md) · [autoresearch](skills/researcher/science/autoresearch/SKILL.md)
- **实验与研究设计** → [experimental-design](skills/researcher/science/experimental-design/SKILL.md) · [statistical-power](skills/researcher/science/statistical-power/SKILL.md)
- **文献调研与学术评审** → [literature-review](skills/researcher/science/literature-review/SKILL.md) · [peer-review](skills/researcher/science/peer-review/SKILL.md) · [citation-management](skills/researcher/info/citation-management/SKILL.md)
- **科学论文写作** → [scientific-writing](skills/researcher/science/scientific-writing/SKILL.md)
- **把书与文档变成 Skill / 摸清服务对象** → [book-to-skill](skills/researcher/knowledge/book-to-skill/SKILL.md) · [distilly](skills/researcher/knowledge/distilly/SKILL.md)
- **论文证据检索（BGPT）** → [bgpt-paper-search](skills/researcher/science/bgpt-paper-search/SKILL.md)

### 📈 产品与增长

- **验证机会与问题-方案契合** → [product-discovery](skills/growth/product/product-discovery/SKILL.md) · [create-prd](skills/growth/product/create-prd/SKILL.md)
- **定位与营销上下文** → [product-marketing](skills/growth/product/product-marketing/SKILL.md)
- **SEO 审计与优化** → [seo-audit](skills/growth/product/seo-audit/SKILL.md) · [seo-agentic](skills/growth/product/seo-agentic/SKILL.md)
- **对齐『说的』与『做的』** → [intended-vs-implemented](skills/growth/product/intended-vs-implemented/SKILL.md)
- **量化研究与数据把关** → [backtest-expert](skills/growth/product/backtest-expert/SKILL.md) · [data-quality-checker](skills/growth/product/data-quality-checker/SKILL.md)
- **定价、发布与增长实验** → [pricing](skills/growth/product/pricing/SKILL.md) · [launch](skills/growth/product/launch/SKILL.md) · [ab-testing](skills/growth/product/ab-testing/SKILL.md) · [marketing-psychology](skills/growth/product/marketing-psychology/SKILL.md)
- **产品愿景与干系人对齐** → [product-vision](skills/growth/product/product-vision/SKILL.md) · [stakeholder-map](skills/growth/product/stakeholder-map/SKILL.md)
- **内容策略、留存与客户研究** → [content-strategy](skills/growth/product/content-strategy/SKILL.md) · [churn-prevention](skills/growth/product/churn-prevention/SKILL.md) · [customer-research](skills/growth/product/customer-research/SKILL.md)

### 🎮 游戏开发者

- **引擎内脚本与玩法** → [godot-gdscript](skills/gamedev/godot-gdscript/SKILL.md) · [unity-csharp-scripting](skills/gamedev/unity-csharp-scripting/SKILL.md) · [unreal-cpp-gameplay](skills/gamedev/unreal-cpp-gameplay/SKILL.md)
- **机制设计与创意方向** → [game-designer Agent](skills/gamedev/agents/game-designer.md) · [creative-director Agent](skills/gamedev/agents/creative-director.md)
- **引擎进阶：信号、着色器与动画** → [godot-signals-groups](skills/gamedev/godot-signals-groups/SKILL.md) · [godot-shaders](skills/gamedev/godot-shaders/SKILL.md) · [unity-animation](skills/gamedev/unity-animation/SKILL.md)
- **手感与反馈（game feel）** → [game-feel](skills/gamedev/game-feel/SKILL.md)
- **NavMesh、Game Jam 与快速原型** → [unity-navmesh](skills/gamedev/unity-navmesh/SKILL.md) · [game-jam](skills/gamedev/game-jam/SKILL.md) · [prototype-fast](skills/gamedev/prototype-fast/SKILL.md)

### 🎬 创作者

- **做电影级产品视频** → [video-shotcraft](skills/creator/video/video-shotcraft/SKILL.md)
- **做网页幻灯片** → [frontend-slides](skills/creator/slides/frontend-slides/SKILL.md)

### 🏢 Corporate Functions（企业职能岗）

- **财务/投资分析（投资人方法论）** → [buffett](skills/corporate/finance/buffett/SKILL.md) · [munger](skills/corporate/finance/munger/SKILL.md) · [dalio-principles-allweather](skills/corporate/finance/dalio-principles-allweather/SKILL.md) · [graham-net-net](skills/corporate/finance/graham-net-net/SKILL.md)
- **财经舆情监控与情绪分析** → [alphaear-news](skills/corporate/finance/alphaear-news/SKILL.md) · [alphaear-sentiment](skills/corporate/finance/alphaear-sentiment/SKILL.md)
- **供应链瓶颈研究（A 股科技/先进制造）** → [serenity-skill](skills/corporate/supply-chain/serenity-skill/SKILL.md)
- **销售：客户画像与线索资格** → [sales-icp](skills/corporate/sales/sales-icp/SKILL.md) · [sales-qualify](skills/corporate/sales/sales-qualify/SKILL.md) · [sales-research](skills/corporate/sales/sales-research/SKILL.md)
- **销售：冷触达与方案赢单** → [sales-outreach](skills/corporate/sales/sales-outreach/SKILL.md) · [sales-proposal](skills/corporate/sales/sales-proposal/SKILL.md)
- **电商：选品、定价与客户反馈** → [dropshipping-product-research](skills/corporate/ecommerce/dropshipping-product-research/SKILL.md) · [competitor-price-analysis](skills/corporate/ecommerce/competitor-price-analysis/SKILL.md) · [customer-feedback-analysis](skills/corporate/ecommerce/customer-feedback-analysis/SKILL.md)
- **合同与提案撰写** → ["contract-and-proposal-writer"](skills/corporate/sales/contract-and-proposal-writer/SKILL.md)

### 🧰 通用工具（所有职业）

- **浏览器自动化** → [browser-act](skills/toolbox/automation/browser-act/SKILL.md)
- **n8n 工作流** → [n8n-error-handling](skills/toolbox/automation/n8n-error-handling/SKILL.md) · [n8n-code-javascript](skills/toolbox/automation/n8n-code-javascript/SKILL.md) · [n8n-code-tool](skills/toolbox/automation/n8n-code-tool/SKILL.md)
- **Office 文档生成与校对** → [officecli](skills/toolbox/office/officecli/SKILL.md)
- **把文档/站点转成 Skill** → [skill-builder](skills/toolbox/meta/skill-seekers/SKILL.md) · [nvidia-skill-finder](skills/toolbox/meta/nvidia-skill-finder/SKILL.md)
- **GPU 数据处理（cuDF / pandas 加速）** → [accelerated-computing-cudf](skills/toolbox/compute/accelerated-computing-cudf/SKILL.md)
- **NotebookLM 知识库操作** → [notebooklm](skills/toolbox/automation/notebooklm/SKILL.md)
- **受治理的 vibe coding 运行时** → [vibe](skills/toolbox/framework/vibe-skills/SKILL.md)
- **Obsidian 知识库操作（官方）** → [obsidian-cli](skills/toolbox/obsidian/obsidian-cli/SKILL.md) · [obsidian-markdown](skills/toolbox/obsidian/obsidian-markdown/SKILL.md) · [obsidian-bases](skills/toolbox/obsidian/obsidian-bases/SKILL.md) · [json-canvas](skills/toolbox/obsidian/json-canvas/SKILL.md) · [defuddle](skills/toolbox/obsidian/defuddle/SKILL.md) · [knap](skills/toolbox/obsidian/knap/SKILL.md)
- **GCP gcloud 命令护栏（官方）** → [gcloud](skills/toolbox/cloud/gcloud/SKILL.md)
- **Claude Code 插件开发（官方）** → [skill-development](skills/toolbox/meta/skill-development/SKILL.md) · [hook-development](skills/toolbox/meta/hook-development/SKILL.md) · [mcp-integration](skills/toolbox/meta/mcp-integration/SKILL.md)
- **文件格式转换与 n8n 进阶** → [file-conversion](skills/toolbox/automation/file-conversion/SKILL.md) · [using-n8n-mcp-skills](skills/toolbox/automation/using-n8n-mcp-skills/SKILL.md) · [n8n-multi-instance](skills/toolbox/automation/n8n-multi-instance/SKILL.md)

### 上游仓库登记（同步监控清单）

每日 CI（[sync-check.yml](.github/workflows/sync-check.yml)，UTC 02:00）逐仓比对 HEAD → HEAD 变化即拉取上游 tree 逐件比对：**原样件自动刷新**（逐字节）、**翻译件变更转[重译工单](../../issues?q=label%3Atranslation)**、全部变化记入 [data/sync-log/](data/sync-log/)。变更检测用 git blob SHA（内容哈希，等价逐字节）。网络操作失败重试 5 次。

| 上游 | Star | License | 模式 | 翻译件 | 原样件 | 最近同步 |
|---|--:|---|:-:|--:|--:|---|
| [morluto/rea](https://github.com/morluto/rea) | 422,686 | MIT | ? | 4 | 4 | [`b912ec1`](https://github.com/morluto/rea/commit/b912ec184ca2ecbd5b59d046187be5b4a59ca3c1) |
| [obra/superpowers](https://github.com/obra/superpowers) | 311,201 | MIT | ? | 5 | 13 | [`2ce8aa1`](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 310,169 | MIT | ? | 2 | 2 | [`4ae2317`](https://github.com/mattpocock/skills/commit/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 295,608 | MIT | ? | 10 | 11 | [`b38be6a`](https://github.com/affaan-m/ECC/commit/b38be6a7f6350964d59328b52f0624e1d1d552d1) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 228,516 | NONE (excluded) | ? | 0 | 0 | — |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 182,852 | MIT | ? | 1 | 0 | [`96608e0`](https://github.com/DietrichGebert/ponytail/commit/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 144,260 | MIT | 整目录（旗舰 + 6 姊妹件） | 7 | 256 | [`713eef5`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/commit/713eef51b04efc98d6fa565323b495f7c9c89fd4) |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 138,676 | MIT | 整仓 | 13 | 1275 | [`b42ad1e`](https://github.com/garrytan/gstack/commit/b42ad1e300fad1641ef1bc65c876701d235d921d) |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 116,925 | Apache-2.0 | ? | 1 | 1 | [`2e068f7`](https://github.com/JuliusBrussee/caveman/commit/2e068f735253cce28256744804785f01887d9646) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 112,815 | MIT | ? | 3 | 4 | [`301b02b`](https://github.com/addyosmani/agent-skills/commit/301b02b12bff98e4688e6984af6556802322bbde) |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 108,664 | MIT | ? | 1 | 36 | [`12af471`](https://github.com/Leonxlnx/taste-skill/commit/12af471f627f866411b4bd785b19646d3672784c) |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 100,404 | Apache-2.0 | 整目录 | 1 | 57 | [`9fadc41`](https://github.com/pbakaus/impeccable/commit/9fadc41729c38fd47d7ae622b501558653f9d2e9) |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 92,717 | Apache-2.0 | ? | 1 | 202 | [`a406594`](https://github.com/tt-a1i/archify/commit/a4065941f12be7967436261d9934784e381d423c) |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 89,877 | MIT | ? | 1 | 54 | [`4e6d329`](https://github.com/Egonex-AI/Understand-Anything/commit/4e6d3299017a7432da15957874992837a315c5b4) |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 66,360 | MIT | ? | 11 | 142 | [`6894d44`](https://github.com/mvanhorn/last30days-skill/commit/6894d44e088c449ecdd7246a18763fddba1ff805) |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 64,335 | MIT | ? | 1 | 286 | [`3eb03b8`](https://github.com/cathrynlavery/diagram-design/commit/3eb03b8d2984e47ddd9b083db9abdcdaa3c69635) |
| [blader/humanizer](https://github.com/blader/humanizer) | 63,995 | MIT | ? | 1 | 0 | [`0ef9fe5`](https://github.com/blader/humanizer/commit/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0) |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 59,825 | MIT | ? | 1 | 0 | [`1ecea19`](https://github.com/ayghri/i-have-adhd/commit/1ecea1993b7fce257ffbd686c070948b5e07eda6) |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 58,091 | MIT | ? | 11 | 31 | [`88c79f6`](https://github.com/coreyhaines31/marketingskills/commit/88c79f6528a9347420e57ceb1fff9a60de651768) |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 57,337 | MIT | 整目录 | 1 | 19 | [`c1c8a8c`](https://github.com/cloudflare/security-audit-skill/commit/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8) |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 55,827 | MIT | 旗舰抽取（7 件） | 52 | 72 | [`a25cf9e`](https://github.com/K-Dense-AI/scientific-agent-skills/commit/a25cf9ec00e2745d03f8704acf6f6919694ccd9a) |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 50,642 | MIT | 整仓 | 6 | 5 | [`3ccff53`](https://github.com/kepano/obsidian-skills/commit/3ccff5338ea700537839b21900aa5358a0402c98) |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 45,939 | MIT | 整目录 | 1 | 182 | [`4f6a46c`](https://github.com/Nutlope/hallmark/commit/4f6a46c6dc325d40ab268c93e25c7b96676ebccd) |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 45,841 | Apache-2.0 | 抽取 | 9 | 41 | [`a7ba5b9`](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) |
| [wshobson/agents](https://github.com/wshobson/agents) | 42,114 | MIT | 抽取 | 16 | 9 | [`7e2fb55`](https://github.com/wshobson/agents/commit/7e2fb559cf4b824b27f1fec49fe88f7511066d26) |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 36,785 | MIT | ? | 1 | 25 | [`7540eef`](https://github.com/virgiliojr94/book-to-skill/commit/7540eefbe74933f5fc84c86becac52486b347778) |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 33,478 | MIT | Agent 定义 | 2 | 0 | [`05ad7c8`](https://github.com/Donchitos/Claude-Code-Game-Studios/commit/05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418) |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 32,952 | Apache-2.0 | 抽取 | 3 | 110 | [`c56512c`](https://github.com/iOfficeAI/OfficeCLI/commit/c56512c8c7b76fe284f09940e4cd492470099d3e) |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 31,756 | MIT | 整目录 | 1 | 78 | [`9906a34`](https://github.com/zarazhangrui/frontend-slides/commit/9906a34d640d2111f724544cbc50f7f130569ae1) |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 29,179 | MIT | 抽取 | 13 | 31 | [`9ef0c3c`](https://github.com/alirezarezvani/claude-skills/commit/9ef0c3c213932e645cc5cbeeb3c35c3a762a2437) |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 27,837 | MIT | ? | 1 | 31 | [`0fa6c79`](https://github.com/OthmanAdi/planning-with-files/commit/0fa6c79885e14534074cb7df8535e1efa3dc7149) |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 27,633 | MIT | 抽取 | 6 | 0 | [`2a12295`](https://github.com/phuryn/pm-skills/commit/2a12295a7717569baa7be181b4cfebe3ca38a6bb) |
| [titanwings/distilly](https://github.com/titanwings/distilly) | 26,310 | MIT | ? | 1 | 58 | [`0afc45c`](https://github.com/titanwings/distilly/commit/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa) |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | 25,971 | MIT | 抽取 | 2 | 8 | [`6be93f4`](https://github.com/AgriciDaniel/claude-seo/commit/6be93f45064ffbadced572b5d5c95f55fd263af0) |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 24,097 | MIT | 整目录 | 1 | 89 | [`1482e84`](https://github.com/wheresryan22/anatomy/commit/1482e8469b0a9e0d8cc18ea2740a01423d29ae80) |
| [google/skills](https://github.com/google/skills) | 21,799 | Apache-2.0 | 抽取 | 1 | 3 | [`0c369ce`](https://github.com/google/skills/commit/0c369ce1c8ab5f93b1d28752b8bea622b2eedcdc) |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 20,073 | MIT | 单文件 | 1 | 0 | [`7db1000`](https://github.com/teng-lin/notebooklm-py/commit/7db1000b516c3f3a7d3afe7c4c572924ee7a5264) |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | 20,061 | MIT | ? | 4 | 285 | [`669ab92`](https://github.com/latent-spaces/brag/commit/669ab9286aa28b6c3ee30e75f181ee74319d012a) |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18,504 | MIT | 抽取 | 2 | 0 | [`2927b40`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/2927b40b2ea37774de53763338c5e8f91a7601e6) |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 18,288 | MIT | 旗舰抽取（6 件） | 6 | 18 | [`9ff0c99`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/commit/9ff0c99108b36d3b886defd825d8ac1f47dba374) |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | 17,747 | MIT | 整仓（8 单文件 skill 全量） | 8 | 0 | [`aed9cfd`](https://github.com/greensock/gsap-skills/commit/aed9cfd3277740755f6bfc1155c7aa645403b760) |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 16,160 | Apache-2.0 | 整目录 | 1 | 1204 | [`1266a3e`](https://github.com/Vincentwei1021/video-shotcraft/commit/1266a3ec4831289c4d893d42dd5102723658039a) |
| [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | 15,428 | MIT | ? | 2 | 1 | [`49b3a72`](https://github.com/nidhinjs/prompt-master/commit/49b3a72469b1e7287d66387004ccfcca90e5968a) |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 15,266 | MIT | 单文件 | 1 | 0 | [`5b5d8df`](https://github.com/yusufkaraaslan/Skill_Seekers/commit/5b5d8dfca263fa76e6daae9f292890b311ef36aa) |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 14,204 | MIT | 整目录 | 4 | 4 | [`773a529`](https://github.com/Orchestra-Research/AI-Research-SKILLs/commit/773a52944ba4747a18bd4ae9ade53fff041adcbc) |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 12,183 | MIT | 抽取 | 4 | 21 | [`078a25c`](https://github.com/Jeffallan/claude-skills/commit/078a25cc5bfd8011459be7b91d004e900c1d02d3) |
| [tw93/Waza](https://github.com/tw93/Waza) | 7,496 | MIT | 规则型 | 7 | 45 | [`5821754`](https://github.com/tw93/Waza/commit/58217546cd94fcf5ddcde4265c00a9377ed3192c) |
| [MengTo/Skills](https://github.com/MengTo/Skills) | 7,200 | MIT | 抽取 | 2 | 10 | [`aa0a995`](https://github.com/MengTo/Skills/commit/aa0a995a0ea33a2600b19ea7c9ff85f17e7ca0da) |
| [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 6,582 | Apache-2.0 | 抽取 | 12 | 10 | [`19d93f9`](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/commit/19d93f97c9c1ea0f8b306e77aa81e0d3e352d3e9) |
| [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | 6,573 | MIT | 抽取 | 6 | 17 | [`e037563`](https://github.com/czlonkowski/n8n-skills/commit/e037563e101749e630e6688d121d04529fe6ee7b) |
| [browser-act/skills](https://github.com/browser-act/skills) | 6,311 | MIT | 抽取 | 1 | 0 | [`11c057b`](https://github.com/browser-act/skills/commit/11c057b03f92101642cadc9f840564574120d184) |
| [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | 4,154 | MIT | 整仓 | 1 | 16 | [`193e409`](https://github.com/muxuuu/serenity-skill/commit/193e409c6ec6acad8e52c29c0570470ed83e3eae) |
| [NVIDIA/skills](https://github.com/NVIDIA/skills) | 3,830 | Apache-2.0 AND CC-BY-4.0 | 抽取 | 2 | 39 | [`40af08d`](https://github.com/NVIDIA/skills/commit/40af08da3d4f52325cfa030775e26705d5f0ba78) |
| [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) | 3,788 | Apache-2.0 | 引用集 | 1 | 36 | [`d881d9c`](https://github.com/foryourhealth111-pixel/Vibe-Skills/commit/d881d9cd6b4a37186c447f7758e802d70c2b27ef) |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | 3,558 | MIT | 抽取 | 4 | 21 | [`d8e71ce`](https://github.com/tradermonty/claude-trading-skills/commit/d8e71ce2f0b069eb5b6fca352857c168c35e6c46) |
| [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) | 3,492 | MIT | 整目录 | 1 | 299 | [`a841596`](https://github.com/patch-gg/pixelfx/commit/a84159688af3ca37a4be05a0d422b94451b2e24e) |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | 3,450 | MIT | 抽取 | 5 | 5 | [`f631a09`](https://github.com/bergside/awesome-design-skills/commit/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8) |
| [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | 3,096 | Apache-2.0 | 抽取 | 2 | 11 | [`853f09b`](https://github.com/RKiding/Awesome-finance-skills/commit/853f09b4d0baae747759ed31e21ed5c5b2316a5f) |
| [questflowai/investorskills](https://github.com/questflowai/investorskills) | 1,907 | MIT | 抽取 | 4 | 4 | [`2844d78`](https://github.com/questflowai/investorskills/commit/2844d7809a73c01e769c8c1c7ae8189788db4d9e) |
| [zubair-trabzada/ai-sales-team-claude](https://github.com/zubair-trabzada/ai-sales-team-claude) | 1,500 | MIT | 抽取 | 5 | 0 | [`efef8b8`](https://github.com/zubair-trabzada/ai-sales-team-claude/commit/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce) |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | 1,316 | MIT | 抽取 | 3 | 0 | [`ee0fb29`](https://github.com/nexscope-ai/eCommerce-Skills/commit/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e) |


*登记表与推荐区由 [scripts/gen_readme_sections.py](scripts/gen_readme_sections.py) 从 `data/manifest.json` + `data/sync-state.json` 生成（片段备份见 [data/readme-sections.md](data/readme-sections.md)），勿手改；**按 Star 降序排列**，Star 为 2026-11-03 快照（完整数字，不用 k）。批次信息仍存于 `data/manifest.json` 的 `batch` 字段，此处不再展示。快照与监测状态在 `data/sync-state.json`，翻译件 blob 基线在 `data/file-shas.json`。*

## 使用方法

将 `skills/<角色>/<类别>/<skill-name>/` **整个目录**复制到你所用 Harness 的技能目录（如 Claude Code 的 `~/.claude/skills/`、DSH 的技能目录），或按各上游原版安装方式替换为中文版目录。

目录内文件分四类（原则 #11，详见 [PRINCIPLES.md](PRINCIPLES.md)）：

| 类型 | 文件 | 处理 |
|---|---|---|
| 翻译件 | `SKILL.md`（含 description） | 已译中文，头部带来源与同步声明 |
| 已译散文 | `references/*.md` 等人读行为规范（流程说明、检查清单、写作指南） | 已译中文，头部带来源与同步声明；登记在 manifest `translated_prose`，上游变更走重译工单，不被自动覆盖 |
| 原样复制件 | 脚本/样式/数据（.sh .py .mjs .cjs .ts .css .json .yaml .html）与机器解析的词表/格式定义（.md） | 逐字节与上游一致 |
| 排除件 | 上游 install.sh、plugin manifest、QA 产物 | 不收录，清单见 data/manifest.json `verbatim_excluded` |

## 合规与致谢

- 所有上游均为 MIT License：版权声明与许可原文保留于 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)
- 本仓库为翻译作品，注明"基于上游 X 翻译修改"，不代表上游官方中文版，除非上游 README 明确链接本仓库
- 术语统一见 [GLOSSARY.md](GLOSSARY.md)；翻译原则见 [PRINCIPLES.md](PRINCIPLES.md)

## 口号与命令本地化说明（试验批次：addyosmani-agent-skills）

> 2026-10-24 起在 **addyosmani-agent-skills 的 3 个文件**上试点口号本地化。你正在测试的正是这个批次——其他上游暂保持纯翻译版，测试结论出来后再决定是否推广。

### 判定口径：三类处理

| 类型 | 判定 | 处理 |
|---|---|---|
| 修辞性口号/图注 | 展示性文字，不影响功能 | **全译中文** |
| 输出模板标题 | 产出文档的结构标题 | **双语标题**：`中文（English）`，两种语言都可检索 |
| 功能性标记 | 被识别/解析/复制的标识 | **保留英文**，必要处附中文等价句 |

### 本批次逐项改动

**context-engineering/SKILL.md**
- ✅ 上下文层级 ASCII 图的 5 条英文注释 → 中文（如 `← Always loaded, project-wide` → `← 始终加载，全项目生效`）
- ✅ 行内计划示例块：列表内容译中文；结尾 `→ Executing unless you redirect.` 改为英中并列（`（除非你纠正方向，否则照此执行）`）
- 🔒 **保留**：`PLAN:` 标记（会话内约定信号）、`CLAUDE.md` 模板块（作为被复制生成的文件内容，保持英文惯例）

**idea-refine/SKILL.md**
- ✅ 触发语句补充中文等价句：`"帮我把这个想法打磨一下"、"围绕 [概念] 发散一下"、"压力测试我的计划"`（英文触发词原样保留，两者都可用）
- ✅ 一页纸输出模板：7 个章节标题改双语（如 `## 问题陈述（Problem Statement）`），占位说明译中文
- 🔒 **保留**：`bash skills/idea-refine/scripts/idea-refine.sh` 命令、frontmatter 触发词 `ideate/refine this idea/stress-test my plan`（与上游识别逻辑兼容）

**agents/code-reviewer.md**
- ✅ 审查输出模板：7 个章节标题改双语（如 `### 严重问题（Critical Issues）`），占位说明译中文
- ✅ 四级分类定义行加中文注：`**Critical（严重）**` / `**Required（必改）**` / `**Optional（可选）**` / `**Nit（轻微）**`
- 🔒 **保留**：`Critical/Required/Optional/Nit` 分类标签本身（与 `code-review-and-quality` Skill 共用的分类学，改了会破坏交叉引用）、判定值 `APPROVE | REQUEST CHANGES`（输出解析锚点）

### 测试建议（决定是否推广）

1. **中文触发测试**：对 idea-refine 说"帮我把这个想法打磨一下"，确认能触发
2. **输出检查**：确认一页纸文档/审查报告的双语标题渲染正常、无格式破坏
3. **PLAN 标记测试**：多步任务中确认 `PLAN:` 行内计划仍被正确识别与执行
4. 若以上都正常，可推广到其余上游（superpowers 的铁律/闸门块、mattpocock 模板等）；若发现 Agent 识别异常，回退方式见各文件声明块"口号本地化"行的对照说明

## 工作日志（按批次）

收录批次不再作为目录组织方式，仅作为工作日志留存：检索与决策记录见 [data/upstream-inventory.md](data/upstream-inventory.md)，各批校验报告见 [data/review-log-*.md](data/)，每日上游变化见 [data/sync-log/](data/sync-log/)。

## 同步策略

`.github/workflows/sync-check.yml` 每日比对各上游 HEAD commit 与 `data/sync-state.json`：
上游有变更 → 自动开 issue 列出待重译文件 → 人工翻译后更新快照。每个翻译文件头部标注同步日期。

## 与上游的关系（引流策略）

向上游申请的方式：先开 issue 询问维护者，获同意后在其 README 提"中文版"一行链接指向本仓库。
