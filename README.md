# Agent Skills 中文汉化库（agent-skills-zh）

> 将 GitHub 上最受欢迎的 Agent Skills 系统性汉化为中文，服务中文 AI 编程用户。
> **本仓库只做翻译，不做原创**——原创人物视角 Skills 另见独立仓库（原则 #7）。

**上游星标快照日期：2026-10-25** · 完整数据见 [data/upstream-inventory.md](data/upstream-inventory.md) · **工作状态**（收录规模/监控/待重译，CI 每日更新）见 [data/STATUS.md](data/STATUS.md)

## 按用户角色浏览

`skills/` 目录按**你是谁、你要做什么**组织，整个目录复制即可用：

| 你是… | 去这里 | 里面有什么 |
|---|---|---|
| 💻 **开发者** | `skills/developer/` | <ul><li><strong>engineering/</strong>：<a href="skills/developer/engineering/test-driven-development/SKILL.md">TDD</a>、<a href="skills/developer/engineering/systematic-debugging/SKILL.md">系统化调试</a>、<a href="skills/developer/engineering/writing-plans/SKILL.md">写计划</a>、<a href="skills/developer/engineering/ponytail/SKILL.md">ponytail 最小改动</a>、<a href="skills/developer/engineering/before-you-build/SKILL.md">before-you-build</a> 等</li><li><strong>quality/</strong>：<a href="skills/developer/quality/code-review/SKILL.md">代码审查</a>、<a href="skills/developer/quality/security-review/SKILL.md">安全审查</a>、<a href="skills/developer/quality/api-designer/SKILL.md">API 设计</a>、<a href="skills/developer/quality/agents/code-reviewer.md">代码审查者 Agent</a></li><li><strong>context/</strong>：<a href="skills/developer/context/context-engineering/SKILL.md">上下文工程</a>、<a href="skills/developer/context/continuous-learning-v2/SKILL.md">持续学习</a>、<a href="skills/developer/context/autonomous-loops/SKILL.md">自主循环</a>、<a href="skills/developer/context/hivemind/SKILL.md">hivemind 编排</a>、<a href="skills/developer/context/claude-md-improver/SKILL.md">CLAUDE.md 优化</a></li><li><strong>efficiency/</strong>：<a href="skills/developer/efficiency/caveman/SKILL.md">caveman 省 token</a>、<a href="skills/developer/efficiency/i-have-adhd/SKILL.md">i-have-adhd 输出格式</a></li><li><strong>gstack/</strong>：<a href="skills/developer/gstack/SKILL.md">Garry Tan 整仓工具链，23+ 角色</a></li></ul> |
| ✍️ **写作者** | `skills/writer/` | <ul><li><strong>writing/</strong>：<a href="skills/writer/writing/humanizer/SKILL.md">humanizer 去 AI 腔</a>、<a href="skills/writer/writing/brag/SKILL.md">brag 项目文案</a></li><li><strong>prompting/</strong>：<a href="skills/writer/prompting/prompt-master/SKILL.md">prompt-master 提示词工程</a></li></ul> |
| 🎨 **设计师** | `skills/designer/design/` | <ul><li><a href="skills/designer/design/taste-skill/SKILL.md">taste 设计品味</a></li><li><a href="skills/designer/design/diagram-design/SKILL.md">diagram-design 编辑级图表</a></li><li><a href="skills/designer/design/archify/SKILL.md">archify 交互图表</a></li><li><a href="skills/designer/design/frontend-design/SKILL.md">frontend-design（官方）</a></li><li><a href="skills/designer/design/creative/SKILL.md">creative 风格设计</a></li></ul> |
| 🔬 **研究者** | `skills/researcher/` | <ul><li><strong>analysis/</strong>：<a href="skills/researcher/analysis/reverse-engineer-anything/SKILL.md">REA 逆向工程</a>、<a href="skills/researcher/analysis/understand/SKILL.md">understand 代码知识图谱</a></li><li><strong>science/</strong>：<a href="skills/researcher/science/experimental-design/SKILL.md">实验设计</a>、<a href="skills/researcher/science/autoresearch/SKILL.md">autoresearch</a>、<a href="skills/researcher/science/auto-paper-improvement-loop/SKILL.md">论文改进循环</a>、<a href="skills/researcher/science/arxiv/SKILL.md">arxiv</a></li><li><strong>info/</strong>：<a href="skills/researcher/info/last30days/SKILL.md">last30days 近 30 天调研</a></li><li><strong>knowledge/</strong>：<a href="skills/researcher/knowledge/book-to-skill/SKILL.md">book-to-skill</a>、<a href="skills/researcher/knowledge/distilly/SKILL.md">distilly 人物画像</a></li></ul> |
| 📈 **产品与增长** | `skills/growth/product/` | <ul><li><a href="skills/growth/product/product-marketing/SKILL.md">product-marketing</a></li><li><a href="skills/growth/product/product-discovery/SKILL.md">product-discovery</a></li><li><a href="skills/growth/product/create-prd/SKILL.md">create-prd</a></li><li><a href="skills/growth/product/intended-vs-implemented/SKILL.md">intended-vs-implemented</a></li><li><a href="skills/growth/product/seo-agentic/SKILL.md">seo-agentic</a> / <a href="skills/growth/product/seo-audit/SKILL.md">seo-audit</a></li><li><a href="skills/growth/product/backtest-expert/SKILL.md">回测</a>与<a href="skills/growth/product/data-quality-checker/SKILL.md">数据质量</a>（⚠️ 金融内容非投资建议）</li></ul> |
| 🎮 **游戏开发者** | `skills/gamedev/` | <ul><li><a href="skills/gamedev/godot-gdscript/SKILL.md">Godot GDScript</a> / <a href="skills/gamedev/unity-csharp-scripting/SKILL.md">Unity C#</a> / <a href="skills/gamedev/unreal-cpp-gameplay/SKILL.md">Unreal C++</a> 三大引擎核心</li><li><a href="skills/gamedev/agents/game-designer.md">游戏设计师</a> / <a href="skills/gamedev/agents/creative-director.md">创意总监</a> Agent</li></ul> |
| 🎬 **创作者** | `skills/creator/video/` | <ul><li><a href="skills/creator/video/video-shotcraft/SKILL.md">video-shotcraft 电影级产品视频</a></li></ul> |
| 🏢 **Corporate Functions（企业职能岗）** | `skills/corporate/` | <ul><li><strong>finance/</strong>：<a href="skills/corporate/finance/buffett/SKILL.md">巴菲特式价值复利</a>、<a href="skills/corporate/finance/munger/SKILL.md">芒格心智模型</a>、<a href="skills/corporate/finance/dalio-principles-allweather/SKILL.md">达利欧全天候</a>、<a href="skills/corporate/finance/graham-net-net/SKILL.md">格雷厄姆净净资产</a>、<a href="skills/corporate/finance/alphaear-news/SKILL.md">财经热点</a>、<a href="skills/corporate/finance/alphaear-sentiment/SKILL.md">文本情绪分析</a></li><li><strong>supply-chain/</strong>：<a href="skills/corporate/supply-chain/serenity-skill/SKILL.md">供应链瓶颈研究</a></li><li><strong>sales/</strong>：<a href="skills/corporate/sales/sales-icp/SKILL.md">理想客户画像</a>、<a href="skills/corporate/sales/sales-qualify/SKILL.md">BANT+MEDDIC 资格评估</a>、<a href="skills/corporate/sales/sales-outreach/SKILL.md">冷触达序列</a>、<a href="skills/corporate/sales/sales-proposal/SKILL.md">销售方案</a>、<a href="skills/corporate/sales/sales-research/SKILL.md">公司调研</a></li><li><strong>ecommerce/</strong>：<a href="skills/corporate/ecommerce/dropshipping-product-research/SKILL.md">选品调研</a>、<a href="skills/corporate/ecommerce/competitor-price-analysis/SKILL.md">竞品价格分析</a>、<a href="skills/corporate/ecommerce/customer-feedback-analysis/SKILL.md">客户反馈分析</a></li></ul> |
| 🧰 **所有人在用的工具** | `skills/toolbox/` | <ul><li><strong>automation/</strong>：<a href="skills/toolbox/automation/n8n-code-javascript/SKILL.md">n8n 代码节点</a>、<a href="skills/toolbox/automation/n8n-error-handling/SKILL.md">n8n 错误处理</a>、<a href="skills/toolbox/automation/browser-act/SKILL.md">browser-act</a>、<a href="skills/toolbox/automation/notebooklm/SKILL.md">notebooklm</a></li><li><strong>meta/</strong>：<a href="skills/toolbox/meta/skill-seekers/SKILL.md">skill-seekers 文档转 skill</a>、<a href="skills/toolbox/meta/nvidia-skill-finder/SKILL.md">NVIDIA 技能发现器</a></li><li><strong>office/</strong>：<a href="skills/toolbox/office/officecli/SKILL.md">officecli</a></li><li><strong>compute/</strong>：<a href="skills/toolbox/compute/accelerated-computing-cudf/SKILL.md">GPU cuDF</a></li><li><strong>framework/</strong>：<a href="skills/toolbox/framework/vibe-skills/SKILL.md">vibe 运行时</a></li></ul> |

> 完整索引（含每件的上游链接）：[data/category-index.md](data/category-index.md)，由 [scripts/classify.py](scripts/classify.py) 按目录结构自动生成。

### 💻 开发者

- **动手前先把需求和风险想清楚** → [brainstorming](skills/developer/engineering/brainstorming/SKILL.md) · [idea-refine](skills/developer/engineering/idea-refine/SKILL.md) · [before-you-build](skills/developer/engineering/before-you-build/SKILL.md)
- **把想法落成规格与计划** → [writing-plans](skills/developer/engineering/writing-plans/SKILL.md) · [to-spec](skills/developer/engineering/to-spec/SKILL.md) · [planning-with-files](skills/developer/engineering/planning-with-files/SKILL.md)
- **写代码与修 bug** → [test-driven-development](skills/developer/engineering/test-driven-development/SKILL.md) · [systematic-debugging](skills/developer/engineering/systematic-debugging/SKILL.md) · [ponytail](skills/developer/engineering/ponytail/SKILL.md) · [search-first](skills/developer/engineering/search-first/SKILL.md)
- **提交前自证完工** → [verification-before-completion](skills/developer/engineering/verification-before-completion/SKILL.md) · [workflow-ship-change](skills/developer/engineering/workflow-ship-change/SKILL.md)
- **代码与安全审查** → [code-review](skills/developer/quality/code-review/SKILL.md) · [code-reviewer](skills/developer/quality/code-reviewer/SKILL.md) · [code-reviewer Agent](skills/developer/quality/agents/code-reviewer.md) · [security-review](skills/developer/quality/security-review/SKILL.md)
- **API 与后端骨架** → [api-designer](skills/developer/quality/api-designer/SKILL.md) · [fastapi-templates](skills/developer/quality/fastapi-templates/SKILL.md) · [build-mcp-server](skills/developer/engineering/build-mcp-server/SKILL.md)
- **上下文与长会话管理** → [context-engineering](skills/developer/context/context-engineering/SKILL.md) · [strategic-compact](skills/developer/context/strategic-compact/SKILL.md) · [claude-md-improver](skills/developer/context/claude-md-improver/SKILL.md)
- **多 Agent 编排与自主学习** → [autonomous-loops](skills/developer/context/autonomous-loops/SKILL.md) · [hivemind](skills/developer/context/hivemind/SKILL.md) · [continuous-learning-v2](skills/developer/context/continuous-learning-v2/SKILL.md)
- **省 token 与输出可读性** → [caveman](skills/developer/efficiency/caveman/SKILL.md) · [i-have-adhd](skills/developer/efficiency/i-have-adhd/SKILL.md)
- **团队评审与 QA（gstack）** → [plan-ceo-review](skills/developer/gstack/plan-ceo-review/SKILL.md) · [qa](skills/developer/gstack/qa/SKILL.md) · [office-hours](skills/developer/gstack/office-hours/SKILL.md)

### ✍️ 写作者

- **去掉 AI 腔、让文字像人写的** → [humanizer](skills/writer/writing/humanizer/SKILL.md)
- **项目宣传与发布文案** → [brag](skills/writer/writing/brag/SKILL.md)
- **为具体 AI 工具写提示词** → [prompt-master](skills/writer/prompting/prompt-master/SKILL.md)

### 🎨 设计师

- **确立 UI 美学方向** → [frontend-design](skills/designer/design/frontend-design/SKILL.md) · [design-taste-frontend](skills/designer/design/taste-skill/SKILL.md)
- **风格化视觉与创意落地页** → [creative](skills/designer/design/creative/SKILL.md)
- **画架构图 / 流程图 / 编辑级图表** → [diagram-design](skills/designer/design/diagram-design/SKILL.md) · [archify](skills/designer/design/archify/SKILL.md)

### 🔬 研究者

- **摸清一个陌生代码库** → [understand](skills/researcher/analysis/understand/SKILL.md) · [reverse-engineer-anything](skills/researcher/analysis/reverse-engineer-anything/SKILL.md)
- **追近 30 天真实讨论与舆情** → [last30days](skills/researcher/info/last30days/SKILL.md)
- **论文检索与改进** → [arxiv](skills/researcher/science/arxiv/SKILL.md) · [auto-paper-improvement-loop](skills/researcher/science/auto-paper-improvement-loop/SKILL.md) · [autoresearch](skills/researcher/science/autoresearch/SKILL.md)
- **实验与研究设计** → [experimental-design](skills/researcher/science/experimental-design/SKILL.md)
- **把书与文档变成 Skill / 摸清服务对象** → [book-to-skill](skills/researcher/knowledge/book-to-skill/SKILL.md) · [distilly](skills/researcher/knowledge/distilly/SKILL.md)

### 📈 产品与增长

- **验证机会与问题-方案契合** → [product-discovery](skills/growth/product/product-discovery/SKILL.md) · [create-prd](skills/growth/product/create-prd/SKILL.md)
- **定位与营销上下文** → [product-marketing](skills/growth/product/product-marketing/SKILL.md)
- **SEO 审计与优化** → [seo-audit](skills/growth/product/seo-audit/SKILL.md) · [seo-agentic](skills/growth/product/seo-agentic/SKILL.md)
- **对齐『说的』与『做的』** → [intended-vs-implemented](skills/growth/product/intended-vs-implemented/SKILL.md)
- **量化研究与数据把关** → [backtest-expert](skills/growth/product/backtest-expert/SKILL.md) · [data-quality-checker](skills/growth/product/data-quality-checker/SKILL.md)

### 🎮 游戏开发者

- **引擎内脚本与玩法** → [godot-gdscript](skills/gamedev/godot-gdscript/SKILL.md) · [unity-csharp-scripting](skills/gamedev/unity-csharp-scripting/SKILL.md) · [unreal-cpp-gameplay](skills/gamedev/unreal-cpp-gameplay/SKILL.md)
- **机制设计与创意方向** → [game-designer Agent](skills/gamedev/agents/game-designer.md) · [creative-director Agent](skills/gamedev/agents/creative-director.md)

### 🎬 创作者

- **做电影级产品视频** → [video-shotcraft](skills/creator/video/video-shotcraft/SKILL.md)

### 🏢 Corporate Functions（企业职能岗）

- **财务/投资分析（投资人方法论）** → [buffett](skills/corporate/finance/buffett/SKILL.md) · [munger](skills/corporate/finance/munger/SKILL.md) · [dalio-principles-allweather](skills/corporate/finance/dalio-principles-allweather/SKILL.md) · [graham-net-net](skills/corporate/finance/graham-net-net/SKILL.md)
- **财经舆情监控与情绪分析** → [alphaear-news](skills/corporate/finance/alphaear-news/SKILL.md) · [alphaear-sentiment](skills/corporate/finance/alphaear-sentiment/SKILL.md)
- **供应链瓶颈研究（A 股科技/先进制造）** → [serenity-skill](skills/corporate/supply-chain/serenity-skill/SKILL.md)
- **销售：客户画像与线索资格** → [sales-icp](skills/corporate/sales/sales-icp/SKILL.md) · [sales-qualify](skills/corporate/sales/sales-qualify/SKILL.md) · [sales-research](skills/corporate/sales/sales-research/SKILL.md)
- **销售：冷触达与方案赢单** → [sales-outreach](skills/corporate/sales/sales-outreach/SKILL.md) · [sales-proposal](skills/corporate/sales/sales-proposal/SKILL.md)
- **电商：选品、定价与客户反馈** → [dropshipping-product-research](skills/corporate/ecommerce/dropshipping-product-research/SKILL.md) · [competitor-price-analysis](skills/corporate/ecommerce/competitor-price-analysis/SKILL.md) · [customer-feedback-analysis](skills/corporate/ecommerce/customer-feedback-analysis/SKILL.md)

### 🧰 通用工具（所有职业）

- **浏览器自动化** → [browser-act](skills/toolbox/automation/browser-act/SKILL.md)
- **n8n 工作流** → [n8n-error-handling](skills/toolbox/automation/n8n-error-handling/SKILL.md) · [n8n-code-javascript](skills/toolbox/automation/n8n-code-javascript/SKILL.md)
- **Office 文档生成与校对** → [officecli](skills/toolbox/office/officecli/SKILL.md)
- **把文档/站点转成 Skill** → [skill-builder](skills/toolbox/meta/skill-seekers/SKILL.md) · [nvidia-skill-finder](skills/toolbox/meta/nvidia-skill-finder/SKILL.md)
- **GPU 数据处理（cuDF / pandas 加速）** → [accelerated-computing-cudf](skills/toolbox/compute/accelerated-computing-cudf/SKILL.md)
- **NotebookLM 知识库操作** → [notebooklm](skills/toolbox/automation/notebooklm/SKILL.md)
- **受治理的 vibe coding 运行时** → [vibe](skills/toolbox/framework/vibe-skills/SKILL.md)

### 上游仓库登记（同步监控清单）

每日 CI（[sync-check.yml](.github/workflows/sync-check.yml)，UTC 02:00）逐仓比对 HEAD → HEAD 变化即拉取上游 tree 逐件比对：**原样件自动刷新**（逐字节）、**翻译件变更转[重译工单](../../issues?q=label%3Atranslation)**、全部变化记入 [data/sync-log/](data/sync-log/)。变更检测用 git blob SHA（内容哈希，等价逐字节）。网络操作失败重试 5 次。

| 上游 | Star | License | 模式 | 翻译件 | 原样件 | 最近同步 |
|---|--:|---|:-:|--:|--:|---|
| [morluto/rea](https://github.com/morluto/rea) | 379,407 | MIT | ? | 1 | 7 | [`8e6a957`](https://github.com/morluto/rea/commit/8e6a95788688439baeeec8e54c9b3e845226f79d) |
| [obra/superpowers](https://github.com/obra/superpowers) | 304,679 | MIT | ? | 5 | 13 | [`2ce8aa1`](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 302,600 | MIT | ? | 2 | 2 | [`5beb35b`](https://github.com/mattpocock/skills/commit/5beb35b040e3de97e54fa9e386d7e42d15c295c2) |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 288,185 | MIT | ? | 8 | 11 | [`90606c8`](https://github.com/affaan-m/ECC/commit/90606c8315ee09cafc303515c5f33024db6b9882) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 223,425 | NONE (excluded) | ? | 0 | 0 | — |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 175,600 | MIT | ? | 1 | 0 | [`09c434a`](https://github.com/DietrichGebert/ponytail/commit/09c434ab73ca43761c5d8b0c5d341926c2fba710) |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 137,553 | MIT | 整仓 | 3 | 1285 | [`f344103`](https://github.com/garrytan/gstack/commit/f344103a3d5f10071f63b836447be874c0e112e8) |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 114,844 | Apache-2.0 | ? | 1 | 1 | [`9444131`](https://github.com/JuliusBrussee/caveman/commit/944413127101fc816451571c169dc1eeb3194bed) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 110,246 | MIT | ? | 3 | 4 | [`aeac41d`](https://github.com/addyosmani/agent-skills/commit/aeac41d4d005999432bb7312f7ff06383a91d59d) |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 102,071 | MIT | ? | 1 | 36 | [`12af471`](https://github.com/Leonxlnx/taste-skill/commit/12af471f627f866411b4bd785b19646d3672784c) |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 88,808 | MIT | ? | 1 | 202 | [`25cf370`](https://github.com/tt-a1i/archify/commit/25cf37080fc8b1dbe758a4efc3935b55f3327083) |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 88,097 | MIT | ? | 1 | 54 | [`e24fcf6`](https://github.com/Egonex-AI/Understand-Anything/commit/e24fcf6d371bcfa529bc110bacb1bb43de1b8d33) |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 65,344 | MIT | ? | 1 | 152 | [`f3cd06a`](https://github.com/mvanhorn/last30days-skill/commit/f3cd06a620e385ce15109ed6d3b70fc20c89eccc) |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 60,774 | MIT | ? | 1 | 286 | [`0b9b10c`](https://github.com/cathrynlavery/diagram-design/commit/0b9b10cab3dbf695642fa1a6c4b4f60df9083689) |
| [blader/humanizer](https://github.com/blader/humanizer) | 60,306 | MIT | ? | 1 | 0 | [`8c307f3`](https://github.com/blader/humanizer/commit/8c307f367c91bd974002f10f2be2965d642c13df) |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 58,621 | MIT | ? | 1 | 0 | [`1ecea19`](https://github.com/ayghri/i-have-adhd/commit/1ecea1993b7fce257ffbd686c070948b5e07eda6) |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 56,393 | MIT | ? | 2 | 4 | [`e85f3cb`](https://github.com/coreyhaines31/marketingskills/commit/e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b) |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 54,456 | MIT | ? | 2 | 26 | [`593377b`](https://github.com/K-Dense-AI/scientific-agent-skills/commit/593377bb048752abb0152deab9fbb1083a6087df) |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 44,380 | Apache-2.0 | 抽取 | 5 | 18 | [`5826794`](https://github.com/anthropics/claude-plugins-official/commit/58267944f92187b7d6a1c822165c96c81c864806) |
| [wshobson/agents](https://github.com/wshobson/agents) | 41,653 | MIT | 抽取 | 5 | 6 | [`0874a27`](https://github.com/wshobson/agents/commit/0874a27b17a22e2b7c2e2bcd725768e0803cad06) |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 35,996 | MIT | ? | 1 | 25 | [`a24e62f`](https://github.com/virgiliojr94/book-to-skill/commit/a24e62f4d8caf2ee433f6e48d9073800f56f906e) |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 32,406 | Apache-2.0 | 抽取 | 2 | 0 | [`5e3e262`](https://github.com/iOfficeAI/OfficeCLI/commit/5e3e26278753be846b4b0b2fb0387f42d911553a) |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 28,664 | MIT | 抽取 | 3 | 25 | [`6d2f02e`](https://github.com/alirezarezvani/claude-skills/commit/6d2f02ea077eead1bee5411a31bcc6db5a11a70c) |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 27,629 | MIT | ? | 1 | 31 | [`dcdfb27`](https://github.com/OthmanAdi/planning-with-files/commit/dcdfb278de53fdb69b2067ea173dbb1de45345a3) |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 27,447 | MIT | Agent 定义 | 2 | 0 | [`05ad7c8`](https://github.com/Donchitos/Claude-Code-Game-Studios/commit/05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418) |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 27,356 | MIT | 抽取 | 3 | 0 | [`07b34f6`](https://github.com/phuryn/pm-skills/commit/07b34f64ee828df08953f505b7f747aef85ae7c6) |
| [titanwings/distilly](https://github.com/titanwings/distilly) | 25,986 | MIT | ? | 1 | 58 | [`0afc45c`](https://github.com/titanwings/distilly/commit/0afc45c29c360ba7bc8260f1bb0bf34e9155f4fa) |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | 20,110 | MIT | 抽取 | 2 | 8 | [`6be93f4`](https://github.com/AgriciDaniel/claude-seo/commit/6be93f45064ffbadced572b5d5c95f55fd263af0) |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 19,890 | MIT | 单文件 | 1 | 0 | [`00b2bd5`](https://github.com/teng-lin/notebooklm-py/commit/00b2bd5077b11fc85efb814250b81ded2bd7da8f) |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | 18,400 | MIT | ? | 1 | 288 | [`669ab92`](https://github.com/latent-spaces/brag/commit/669ab9286aa28b6c3ee30e75f181ee74319d012a) |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18,014 | MIT | 抽取 | 2 | 0 | [`18bceb3`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/18bceb3c71c638bef58096274e1c9a6d323dbc0a) |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 15,217 | MIT | 单文件 | 1 | 0 | [`5b5d8df`](https://github.com/yusufkaraaslan/Skill_Seekers/commit/5b5d8dfca263fa76e6daae9f292890b311ef36aa) |
| [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | 15,005 | MIT | ? | 1 | 2 | [`49b3a72`](https://github.com/nidhinjs/prompt-master/commit/49b3a72469b1e7287d66387004ccfcca90e5968a) |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 13,912 | MIT | 整目录 | 1 | 8 | [`773a529`](https://github.com/Orchestra-Research/AI-Research-SKILLs/commit/773a52944ba4747a18bd4ae9ade53fff041adcbc) |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 13,457 | Apache-2.0 | 整目录 | 1 | 1354 | [`43bd349`](https://github.com/Vincentwei1021/video-shotcraft/commit/43bd349a136651865ecfa6ea1cf012f6e957d304) |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 12,043 | MIT | 抽取 | 3 | 16 | [`9e7dbd6`](https://github.com/Jeffallan/claude-skills/commit/9e7dbd688015cbd1f440374f8671028bb67c608f) |
| [tw93/Waza](https://github.com/tw93/Waza) | 7,356 | MIT | 规则型 | 5 | 25 | [`b3664a5`](https://github.com/tw93/Waza/commit/b3664a561877f872d7ec14f2a8ec34023d00a484) |
| [MengTo/Skills](https://github.com/MengTo/Skills) | 6,999 | MIT | 抽取 | 2 | 10 | [`6b16085`](https://github.com/MengTo/Skills/commit/6b16085676e1fbe30056721cd245fd7836ec6396) |
| [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | 6,518 | MIT | 抽取 | 2 | 10 | [`e037563`](https://github.com/czlonkowski/n8n-skills/commit/e037563e101749e630e6688d121d04529fe6ee7b) |
| [browser-act/skills](https://github.com/browser-act/skills) | 6,272 | MIT | 抽取 | 1 | 0 | [`11c057b`](https://github.com/browser-act/skills/commit/11c057b03f92101642cadc9f840564574120d184) |
| [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | 4,119 | MIT | 整仓 | 1 | 16 | [`193e409`](https://github.com/muxuuu/serenity-skill/commit/193e409c6ec6acad8e52c29c0570470ed83e3eae) |
| [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 4,027 | Apache-2.0 | 抽取 | 3 | 4 | [`184b72b`](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/commit/184b72be02884f782a0058f2eeae2ce4277453e4) |
| [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) | 3,765 | Apache-2.0 | 引用集 | 1 | 36 | [`0407cb2`](https://github.com/foryourhealth111-pixel/Vibe-Skills/commit/0407cb2e8db9aae4fccfe7b456a67419a9aee0f2) |
| [NVIDIA/skills](https://github.com/NVIDIA/skills) | 3,721 | Apache-2.0 AND CC-BY-4.0 | 抽取 | 2 | 39 | [`b713368`](https://github.com/NVIDIA/skills/commit/b71336851ae0416f6eaf4cd623d04749981e7cbf) |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | 3,336 | MIT | 抽取 | 2 | 2 | [`f631a09`](https://github.com/bergside/awesome-design-skills/commit/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8) |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | 3,262 | MIT | 抽取 | 3 | 14 | [`52c9323`](https://github.com/tradermonty/claude-trading-skills/commit/52c932329e25a614eea9e55f7aa8e7677e8c0b84) |
| [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | 3,084 | Apache-2.0 | 抽取 | 2 | 11 | [`853f09b`](https://github.com/RKiding/Awesome-finance-skills/commit/853f09b4d0baae747759ed31e21ed5c5b2316a5f) |
| [questflowai/investorskills](https://github.com/questflowai/investorskills) | 1,882 | MIT | 抽取 | 4 | 4 | [`2844d78`](https://github.com/questflowai/investorskills/commit/2844d7809a73c01e769c8c1c7ae8189788db4d9e) |
| [zubair-trabzada/ai-sales-team-claude](https://github.com/zubair-trabzada/ai-sales-team-claude) | 1,468 | MIT | 抽取 | 5 | 0 | [`efef8b8`](https://github.com/zubair-trabzada/ai-sales-team-claude/commit/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce) |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | 1,251 | MIT | 抽取 | 3 | 0 | [`ee0fb29`](https://github.com/nexscope-ai/eCommerce-Skills/commit/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e) |

*登记表与推荐区由 [scripts/gen_readme_sections.py](scripts/gen_readme_sections.py) 从 `data/manifest.json` + `data/sync-state.json` 生成（片段备份见 [data/readme-sections.md](data/readme-sections.md)），勿手改；**按 Star 降序排列**，Star 为 2026-10-25 快照（完整数字，不用 k）。批次信息仍存于 `data/manifest.json` 的 `batch` 字段，此处不再展示。快照与监测状态在 `data/sync-state.json`，翻译件 blob 基线在 `data/file-shas.json`。*

## 使用方法

将 `skills/<角色>/<类别>/<skill-name>/` **整个目录**复制到你所用 Harness 的技能目录（如 Claude Code 的 `~/.claude/skills/`、DSH 的技能目录），或按各上游原版安装方式替换为中文版目录。

目录内文件分三类（原则 #11，详见 [PRINCIPLES.md](PRINCIPLES.md)）：

| 类型 | 文件 | 处理 |
|---|---|---|
| 翻译件 | `SKILL.md`（含 description） | 已译中文，头部带来源与同步声明 |
| 原样复制件 | 脚本/样式/数据（.sh .py .mjs .cjs .ts .css .json .yaml .html）与上游散文引用（.md） | 逐字节与上游一致；散文件翻译排后续 issue |
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
