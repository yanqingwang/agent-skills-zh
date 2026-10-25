# Agent Skills 中文汉化库（agent-skills-zh）

> 将 GitHub 上最受欢迎的 Agent Skills 系统性汉化为中文，服务中文 AI 编程用户。
> **本仓库只做翻译，不做原创**——原创人物视角 Skills 另见独立仓库（原则 #7）。

**上游星标快照日期：2026-10-24** · 完整数据见 [data/upstream-inventory.md](data/upstream-inventory.md)

## 按用户角色浏览

`skills/` 目录按**你是谁、你要做什么**组织，整个目录复制即可用：

| 你是… | 去这里 | 里面有什么 |
|---|---|---|
| 💻 **开发者** | `skills/developer/` | `engineering/`（TDD、系统化调试、写计划、ponytail 最小改动、before-you-build…）、`quality/`（代码审查、安全审查、API 设计、代码审查者 Agent）、`context/`（上下文工程、持续学习、自主循环、hivemind 编排、CLAUDE.md 优化）、`efficiency/`（caveman 省 token、i-have-adhd 输出格式）、`gstack/`（Garry Tan 整仓工具链，23+ 角色） |
| ✍️ **写作者** | `skills/writer/` | `writing/`（humanizer 去 AI 腔、brag 项目文案）、`prompting/`（prompt-master 提示词工程） |
| 🎨 **设计师** | `skills/designer/design/` | taste 设计品味、diagram-design 编辑级图表、archify 交互图表、frontend-design（官方）、creative 风格设计 |
| 🔬 **研究者** | `skills/researcher/` | `analysis/`（REA 逆向工程、understand 代码知识图谱）、`science/`（实验设计、autoresearch、论文改进循环、arxiv）、`info/`（last30days 近 30 天调研）、`knowledge/`（book-to-skill、distilly 人物画像） |
| 📈 **产品与增长** | `skills/growth/product/` | product-marketing、product-discovery、create-prd、intended-vs-implemented、seo-agentic / seo-audit、回测与数据质量（⚠️ 金融内容非投资建议） |
| 🎮 **游戏开发者** | `skills/gamedev/` | Godot GDScript / Unity C# / Unreal C++ 三大引擎核心 + 游戏设计师 / 创意总监 Agent |
| 🎬 **创作者** | `skills/creator/video/` | video-shotcraft 电影级产品视频 |
| 🧰 **所有人在用的工具** | `skills/toolbox/` | `automation/`（n8n 工作流 ×2、browser-act、notebooklm）、`meta/`（skill-seekers 文档转 skill、NVIDIA 技能发现器）、`office/`（officecli）、`compute/`（GPU cuDF）、`framework/`（vibe 运行时） |

> 完整索引（含每件的上游链接）：[data/category-index.md](data/category-index.md)，由 [scripts/classify.py](scripts/classify.py) 按目录结构自动生成。

### 上游仓库登记（同步监控清单）

每日 CI（[sync-check.yml](.github/workflows/sync-check.yml)，UTC 02:00）逐仓比对 HEAD → HEAD 变化即拉取上游 tree 逐件比对：**原样件自动刷新**（逐字节）、**翻译件变更转[重译工单](../../issues?q=label%3Atranslation)**、全部变化记入 [data/sync-log/](data/sync-log/)。变更检测用 git blob SHA（内容哈希，等价逐字节）。网络操作失败重试 5 次。

| 上游 | License | 批次 | 模式 | 翻译件 | 原样件 | 最近同步 |
|---|---|:-:|:-:|--:|--:|---|
| [obra/superpowers](https://github.com/obra/superpowers) | MIT | ? | ? | 5 | 13 | [`2ce8aa1`](https://github.com/obra/superpowers/commit/2ce8aa1) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | MIT | ? | ? | 2 | 2 | [`5beb35b`](https://github.com/mattpocock/skills/commit/5beb35b) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT | ? | ? | 3 | 4 | [`aeac41d`](https://github.com/addyosmani/agent-skills/commit/aeac41d) |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT | ? | ? | 1 | 36 | [`12af471`](https://github.com/Leonxlnx/taste-skill/commit/12af471) |
| [morluto/rea](https://github.com/morluto/rea) | MIT | 2 | ? | 1 | 7 | [`26e1559`](https://github.com/morluto/rea/commit/26e1559) |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT | 2 | ? | 1 | 0 | [`09c434a`](https://github.com/DietrichGebert/ponytail/commit/09c434a) |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 | 2 | ? | 1 | 1 | [`1f951fb`](https://github.com/JuliusBrussee/caveman/commit/1f951fb) |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | MIT | 2 | ? | 1 | 202 | [`25cf370`](https://github.com/tt-a1i/archify/commit/25cf370) |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | MIT | 2 | ? | 1 | 54 | [`e24fcf6`](https://github.com/Egonex-AI/Understand-Anything/commit/e24fcf6) |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | MIT | 2 | ? | 1 | 152 | [`f3cd06a`](https://github.com/mvanhorn/last30days-skill/commit/f3cd06a) |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | MIT | 2 | ? | 1 | 286 | [`0b9b10c`](https://github.com/cathrynlavery/diagram-design/commit/0b9b10c) |
| [blader/humanizer](https://github.com/blader/humanizer) | MIT | 2 | ? | 1 | 0 | [`8c307f3`](https://github.com/blader/humanizer/commit/8c307f3) |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | MIT | 2 | ? | 1 | 0 | [`1ecea19`](https://github.com/ayghri/i-have-adhd/commit/1ecea19) |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | 2 | ? | 1 | 1 | [`e85f3cb`](https://github.com/coreyhaines31/marketingskills/commit/e85f3cb) |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | MIT | 2 | ? | 1 | 6 | [`593377b`](https://github.com/K-Dense-AI/scientific-agent-skills/commit/593377b) |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT | 2 | ? | 5 | 11 | [`90606c8`](https://github.com/affaan-m/ECC/commit/90606c8) |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | MIT | 2 | ? | 1 | 25 | [`a24e62f`](https://github.com/virgiliojr94/book-to-skill/commit/a24e62f) |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | MIT | 2 | ? | 1 | 31 | [`dcdfb27`](https://github.com/OthmanAdi/planning-with-files/commit/dcdfb27) |
| [titanwings/distilly](https://github.com/titanwings/distilly) | MIT | 2 | ? | 1 | 58 | [`0afc45c`](https://github.com/titanwings/distilly/commit/0afc45c) |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | MIT | 2 | ? | 1 | 288 | [`669ab92`](https://github.com/latent-spaces/brag/commit/669ab92) |
| [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | MIT | 2 | ? | 1 | 2 | [`49b3a72`](https://github.com/nidhinjs/prompt-master/commit/49b3a72) |
| [garrytan/gstack](https://github.com/garrytan/gstack) | MIT | 3 | 整仓 | 3 | 1285 | [`e66c43c`](https://github.com/garrytan/gstack/commit/e66c43c) |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | Apache-2.0 | 3 | 整目录 | 1 | 1354 | [`43bd349`](https://github.com/Vincentwei1021/video-shotcraft/commit/43bd349) |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | MIT | 3 | 单文件 | 1 | 0 | [`00b2bd5`](https://github.com/teng-lin/notebooklm-py/commit/00b2bd5) |
| [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) | Apache-2.0 | 3 | 引用集 | 1 | 36 | [`0407cb2`](https://github.com/foryourhealth111-pixel/Vibe-Skills/commit/0407cb2) |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | MIT | 3 | 单文件 | 1 | 0 | [`5b5d8df`](https://github.com/yusufkaraaslan/Skill_Seekers/commit/5b5d8df) |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | MIT | 3 | 整目录 | 1 | 8 | [`773a529`](https://github.com/Orchestra-Research/AI-Research-SKILLs/commit/773a529) |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | MIT | 3 | 抽取 | 2 | 23 | [`6d2f02e`](https://github.com/alirezarezvani/claude-skills/commit/6d2f02e) |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | MIT | 3 | 抽取 | 2 | 0 | [`07b34f6`](https://github.com/phuryn/pm-skills/commit/07b34f6) |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | MIT | 3 | 抽取 | 2 | 8 | [`6be93f4`](https://github.com/AgriciDaniel/claude-seo/commit/6be93f4) |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | MIT | 3 | 抽取 | 2 | 0 | [`18bceb3`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/18bceb3) |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | MIT | 3 | 抽取 | 2 | 11 | [`9e7dbd6`](https://github.com/Jeffallan/claude-skills/commit/9e7dbd6) |
| [MengTo/Skills](https://github.com/MengTo/Skills) | MIT | 3 | 抽取 | 1 | 4 | [`398cd41`](https://github.com/MengTo/Skills/commit/398cd41) |
| [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | MIT | 3 | 抽取 | 2 | 10 | [`e037563`](https://github.com/czlonkowski/n8n-skills/commit/e037563) |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Apache-2.0 | 4 | 抽取 | 3 | 12 | [`5826794`](https://github.com/anthropics/claude-plugins-official/commit/5826794) |
| [wshobson/agents](https://github.com/wshobson/agents) | MIT | 4 | 抽取 | 2 | 2 | [`0874a27`](https://github.com/wshobson/agents/commit/0874a27) |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | MIT | 4 | Agent 定义 | 2 | 0 | [`05ad7c8`](https://github.com/Donchitos/Claude-Code-Game-Studios/commit/05ad7c8) |
| [tw93/Waza](https://github.com/tw93/Waza) | MIT | 4 | 规则型 | 2 | 0 | [`4afc0f0`](https://github.com/tw93/Waza/commit/4afc0f0) |
| [NVIDIA/skills](https://github.com/NVIDIA/skills) | Apache-2.0 AND CC-BY-4.0 | 4 | 抽取 | 2 | 39 | [`b713368`](https://github.com/NVIDIA/skills/commit/b713368) |
| [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | Apache-2.0 | 4 | 抽取 | 3 | 4 | [`184b72b`](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/commit/184b72b) |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | MIT | 4 | 抽取 | 1 | 1 | [`f631a09`](https://github.com/bergside/awesome-design-skills/commit/f631a09) |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | MIT | 4 | 抽取 | 2 | 8 | [`52c9323`](https://github.com/tradermonty/claude-trading-skills/commit/52c9323) |
| [browser-act/skills](https://github.com/browser-act/skills) | MIT | 4 | 抽取 | 1 | 0 | [`11c057b`](https://github.com/browser-act/skills/commit/11c057b) |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | Apache-2.0 | 4 | 抽取 | 1 | 0 | [`5e3e262`](https://github.com/iOfficeAI/OfficeCLI/commit/5e3e262) |

*登记由 `data/manifest.json` 生成；快照与监测状态在 `data/sync-state.json`，翻译件 blob 基线在 `data/file-shas.json`。*

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
