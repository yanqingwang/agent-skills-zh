# 散文引用件汉化首批（review log · 2026-11-03）

**校验日期：2026-11-03** · **范围**：新工作线首批——69 件 `references/*.md` 等人读行为规范汉化（累计 175 翻译件 + 66 已译散文 / 5128 原样件）
**校验者**：父会话机械检查（声明块完整性 / 通道互斥 / lint）+ 10 组翻译代理自检回报（代码块逐字节比对）
**结论：PASS（66 件已译散文声明块齐全；translated_prose 与 verbatim 无交集；lint 0 信号）**

## 机制改造（本次核心）

**问题**：原则 #11 原先把散文引用件一律归入 `verbatim`（原样复制），`fetch_verbatim.py` 与 `sync_daily.py` 会在每次同步时用上游英文**覆盖**已汉化内容——直接翻译散文，下次 CI 就冲回英文。

**改造**：
1. `data/manifest.json` 新增 `translated_prose` 清单，与 `verbatim` 严格互斥
2. `scripts/sync_daily.py`：翻译件集合 = `files` + `translated_prose`，上游 blob 变更 → 重译工单（销单条件：声明块同步日期 ≥ 首次发现日期）
3. `scripts/fetch_verbatim.py`：只处理 `verbatim`，不触碰已译散文
4. `scripts/lint_zh_style.py` / `scripts/gen_readme_sections.py`：翻译件计数与体检范围纳入 `translated_prose`
5. 新增 [PROSE_TRANSLATION.md](../PROSE_TRANSLATION.md)：判定标准（该译/不该译）、声明块格式、翻译规则
6. `PRINCIPLES.md` #11 由三类改为四类，新增「已译散文」

## 汉化范围（69 件 / 449KB）

| 上游 | 件数 | 内容 |
|---|--:|---|
| K-Dense-AI/scientific-agent-skills | 44 | experimental-design（设计类型/析因与 DOE/随机化与区组化/序贯与自适应）、exploratory-data-analysis（各科学数据格式）、literature-review（检索与引用策略/引用格式/核心流程/数据库策略）、peer-review（工具参考/伦理审查/统计可复现/安全校验）、scientific-writing（IMRaD/图表规范/写作原则/引用格式/报告排版/研究诚信/署名与 AI 保密/源账本等 20 件）、statistical-power（效应量/闭式配方/模拟功效） |
| mvanhorn/last30days-skill | 13 | agent-mode、discovery、competitors、category-peers、hiring-signals、followups、library-queue、recommendations、runtime、grok-bot-x |
| morluto/rea | 3 | android-applications、evidence-workflows、runtime-observation |
| Orchestra-Research/AI-Research-SKILLs | 2 | skill-routing、progress-reporting |
| latent-spaces/brag | 3 | step-1-inspect、step-4-deliver、tones |
| alirezarezvani/claude-skills | 2 | **deepread 的 knowledge-map.md 与 feynman.md**（用户点名的示例） |
| nidhinjs/prompt-master | 1 | patterns |

## 判定：译 / 不译

- **译**：`references/` `assets/` 下人读的行为规范（流程、检查清单、写作指南、模板说明）
- **不译**（仍在 verbatim）：`understand/languages/*.md`（语法解析表）、`locales/*.md`（本地化词条）、`assets/music/cues/*.md`（素材）、CSV/JSON 模板骨架的字段名

## 质量

- 声明块 66/66 齐全（`translated_prose` 中全部含「中文汉化版」+ 2026-11-03 同步日期）
- 代码块逐字节一致（各组自检；含嵌套围栏、bash 注释、FreeMind XML 等）
- **AI 腔门禁**：散文统一用单破折号 `—` 对齐上游 em dash，不使用中文双破折号 `——`；连带修复了 statistical-power 与 multi-agent-patterns 两个 SKILL.md 的破折号超标
- 模板骨架中依赖英文字面量的占位符（`{{TODO: ...}}`、`# DRAFT — NOT FOR SUBMISSION`、CRediT 角色名、`[$ref-one]`）一律保留——上游脚本按英文串匹配，翻译会破坏其功能

## 过程事件

- **并发代理越界**：首三组代理自行修改了 `data/manifest.json`、`scripts/lint_zh_style.py`、`README.md` 等共享文件。处置：核查改动内容均正确且必要（翻译件计数与体检范围本就该纳入已译散文），保留；后续 7 组在提示词中明确禁止触碰共享文件，由父会话统一登记 manifest。
- **锚点失效**：REA 的 SKILL.md 用英文章节名锚点指向 references（`#native-runtime-questions`）。译后标题变中文会导致链接失效，译文在对应标题处补了 `<a id="...">` 显式锚点，保持 SKILL.md 侧无需改动。
- **manifest 既有重复**：`Orchestra-Research/AI-Research-SKILLs` 的 `autoresearch/SKILL.md` 在 HEAD 即重复登记一条，本次顺手去重。
