# 汉化原则（PRINCIPLES）

> 本文件固化 2026-10-24 与仓库所有者商定的汉化原则。所有后续贡献者在动手前必读。

## 1. 独立建仓，不向上游提交正文
汉化正文只存在于本仓库。上游仅通过"先开 issue 询问 → 获同意 → README 引流链接"的方式建立联系。理由：正文 PR 会被上游拒绝或搁置，且投入攒的是上游的 star 而非本仓库的资产。

## 2. 无 License = 不翻译
只翻译有明确宽松 License（MIT 等）的上游。无 License 仓库默认保留所有权利，翻译分发即侵权。
当前排除：`multica-ai/andrej-karpathy-skills`（223k 星，无 License）。如需 Karpathy 中文内容，必须走独立调研蒸馏（原创路径），不得翻译其文件。

## 3. 合规三件套
每个上游必须：① 在 `THIRD-PARTY-NOTICES.md` 保留其 LICENSE 原文与版权声明；② README 来源表注明"基于上游 X 翻译修改"；③ 标注星标快照日期。

## 4. 翻译文件头部声明
每个翻译文件在 frontmatter 之后附声明块：上游链接、原文件路径、License、翻译日期、同步状态、"AI 辅助翻译"标注。

## 5. 术语统一
以 `GLOSSARY.md` 为准。代码块、shell 命令、frontmatter 字段名、专有概念（Skill/Agent/Harness/Hook/token/worktree）不译。

## 6. 自动同步
GitHub Actions 每日比对上游 HEAD，变更即开待翻译 issue；翻译文件头标注同步日期，杜绝"过期翻译误导用户"。

## 7. 翻译仓与原创仓分离
本仓库只收翻译。原创内容（如女娲造人产出的中文人物视角 Skills）另建仓库，不混 License、不混定位。

## 8. 定位：流量入口而非现金流主体
本仓库的变现路径是 Sponsors → 引流到定制服务与原创仓库 → 咨询。不为星标绝对值优化，为"汉化质量信任"优化——同步状态与人工校对是核心信任资产。

## 9. 不伪装背书
未获上游明确授权前，不得声称"官方中文版"。

## 10. 质量纪律
宁缺毋滥：第一批只收 11 个高价值文件，人工校对后发布；机器直翻不直接入库。

## 11. 目录完整性（drop-in replacement）原则
收录一个 Skill = 其 `SKILL.md`（翻译）+ **其运行所引用的目录内全部文件（原样复制，逐字节一致）**。用户把本地目录放进技能库后必须开箱即用，不得出现"指向不存在文件"的悬空引用。文件分三类：
- **翻译件**：SKILL.md（含 frontmatter description）
- **原样复制件**：脚本（.sh/.py/.mjs/.cjs/.ts）、样式（.css）、数据（.json/.yaml）、HTML 模板、上游散文引用文件（*.md）——前四类永不翻译；*.md 散文引用件先原样复制保证可用，翻译排入第二批 issue
- **排除件**：上游仓库级工具（install.sh、各 Harness 的 plugin manifest、CI）与上游自身 QA 产物（test-*.md、CREATION-LOG.md）不收录；排除清单记录在 data/manifest.json 的 verbatim_excluded
同步时重跑 `scripts/fetch_verbatim.py` 刷新原样件，`--check` 模式供校验逐字节一致性。
