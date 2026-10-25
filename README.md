# Agent Skills 中文汉化库（agent-skills-zh）

> 将 GitHub 上最受欢迎的 Agent Skills 系统性汉化为中文，服务中文 AI 编程用户。
> **本仓库只做翻译，不做原创**——原创人物视角 Skills 另见独立仓库（原则 #7）。

**上游星标快照日期：2026-10-24** · 完整数据见 [data/upstream-inventory.md](data/upstream-inventory.md)

## 来源仓库

星标快照 2026-10-24。完整检索与决策记录见 [data/upstream-inventory.md](data/upstream-inventory.md)。

### 第一批（20 个翻译件）

| 上游仓库 | 星标 | License | 本仓库收录 |
|---|---:|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 304k | MIT | 5 个 Skill |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 302k | MIT | 2 个 Skill |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 110k | MIT | 2 个 Skill + 1 个 Agent |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 102k | MIT | 1 个 Skill |
| [morluto/rea](https://github.com/morluto/rea) | 377k | MIT | reverse-engineer-anything |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 175k | MIT | ponytail |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 115k | Apache-2.0 | caveman |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 89k | MIT | archify |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 88k | MIT | understand |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 65k | MIT | last30days |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 61k | MIT | diagram-design |
| [blader/humanizer](https://github.com/blader/humanizer) | 60k | MIT | humanizer |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 59k | MIT | i-have-adhd |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 56k | MIT | product-marketing |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 54k | MIT | experimental-design |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 288k | MIT | search-first / security-review / continuous-learning-v2 / autonomous-loops |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 36k | MIT | book-to-skill |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 28k | MIT | planning-with-files |
| [titanwings/distilly](https://github.com/titanwings/distilly) | 26k | MIT | distilly |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | 18k | MIT | brag |
| [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | 15k | MIT | prompt-master |

**重要合规发现**：`挑选的skills，均为上游允许翻译的skills。如 anthropics/skills`（183k 星，官方仓库）经查证**无 License**，则排除，不翻译不分发。`garrytan/gstack`（137k，MIT）为整仓型工具链（skill 强依赖根 `bin/`），推迟至第三批以整仓模式收录。`multica-ai/andrej-karpathy-skills`（223k）无 License，继续排除。

## 分类索引

由 [scripts/classify.py](scripts/classify.py) 按 [data/manifest.json](data/manifest.json) 自动生成 → [data/category-index.md](data/category-index.md)

- **工程方法论**：TDD、系统化调试、写计划、完成前验证、规格拆解、ponytail 最小改动、search-first、planning-with-files
- **质量与审查**：代码审查、审查者 Agent、security-review 安全检查清单
- **头脑风暴与构思**：brainstorming、idea-refine
- **上下文工程**：context-engineering、continuous-learning-v2、autonomous-loops
- **设计品味**：taste-skill、diagram-design、archify
- **写作与表达**：humanizer、brag
- **分析与逆向**：reverse-engineer-anything、understand
- **调研与信息**：last30days
- **提示词工程**：prompt-master
- **知识转化**：book-to-skill、distilly
- **科学研究**：experimental-design
- **市场与增长**：product-marketing
- **省 token 与输出格式**：caveman、i-have-adhd

## 使用方法

将 `skills/<上游名>/<skill-name>/` **整个目录**复制到你所用 Harness 的技能目录（如 Claude Code 的 `~/.claude/skills/`、DSH 的技能目录），或按各上游原版安装方式替换为中文版目录。

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

## 同步策略

`.github/workflows/sync-check.yml` 每日比对各上游 HEAD commit 与 `data/sync-state.json`：
上游有变更 → 自动开 issue 列出待重译文件 → 人工翻译后更新快照。每个翻译文件头部标注同步日期。

## 与上游的关系（引流策略）

向上游申请的方式：先开 issue 询问维护者，获同意后在其 README 提"中文版"一行链接指向本仓库。
