# 第九批校验报告（review log · 2026-11-12）

**校验日期：2026-11-12** · **范围**：7 个存量合集追加，20 个翻译件、40 个原样件（累计 61 登记 / 60 监控 / 195 翻译件 / 5168 原样件；全库 189 个 SKILL.md 汉化）
**校验者**：父会话机械检查（声明块 / 围栏代码块含 ```lang 围栏行逐字节还原 / YAML name / blob SHA / 残留英文散文 / lint）+ 8 组翻译代理与 2 组聚焦代理自检回报
**结论：PASS**

## 本批收录

| 上游 | 追加件 | 原样件 |
|---|---|---|
| coreyhaines31/marketingskills | copy-editing、pricing、launch、ab-testing、marketing-psychology | 16 |
| wshobson/agents | python-project-structure、gitlab-ci-patterns、sast-configuration、review-agent-setup | 0 |
| gamedev-skills/awesome-gamedev-agent-skills | game-feel、godot-signals-groups、godot-shaders、unity-animation | 4 |
| anthropics/claude-plugins-official | skill-development、hook-development、mcp-integration | 17 |
| phuryn/pm-skills | product-vision、stakeholder-map | 0 |
| K-Dense-AI/scientific-agent-skills | bgpt-paper-search | 0 |
| czlonkowski/n8n-skills | n8n-code-tool | 3 |

## 机械校验（全量）

- **翻译件**：20/20 frontmatter `name` 保留英文、`description` 已译、声明块三行逐字（含按目录深度计算的 GLOSSARY 相对路径）、``` 围栏数与原文件一致、全部代码块（含 ```lang 围栏行与内容）逐字节还原为上游原文；frontmatter 其余字段保持原样
- **残留英文散文**：19 件 0 处；`ab-testing` 的 2 处为上游原样保留的品牌名链接标签（Evan Miller's / Optimizely's），与原文逐字一致，非漏译
- **原样件**：40 件由 `gh api` 按当前上游 HEAD 的 blob 原样下载；复取 7 仓 tree 后以 `git hash-object` 复核，ok=40 / diff=0 / missing=0
- **file-shas 基线**：20 件写入当前 HEAD blob SHA，避免下轮 CI 因缺基线静默漏检；复取 tree 复核 0 条过期
- **lint_zh_style**：全库 0 信号；`git diff --check` 干净；新目录无未登记文件、无临时产物
- **索引与推荐区**：`gen_readme_sections.py` 的 manifest 交叉校验无告警；20 条路径全部见于 README.md、data/readme-sections.md、data/category-index.md；STATUS.md / 上游登记表计数已重生成

## 收录定位说明

本批零新上游，是「存量合集补全」：只取跨项目可复用、自包含或配套件极少的件；所有正文取 GitHub 现时 HEAD 的 blob，不沿用 2026-10-25 的本地克隆快照（已确认多数落后），避免译文与上游脱节。配套 `references/` 散文按原则 #11「先原样复制保证可用」留待后续批次汉化。聚合型大合集（sickn33、affaan-m/ECC 桩件）、单库绑定指南与超大单件（iOfficeAI/OfficeCLI 25–66KB）继续按「宁缺毋滥」缓收。

## 同步状态说明

本批未改动 `data/sync-state.json`（HEAD 快照）：其中 7 仓的快照为 2026-11-11，而部分上游（coreyhaines31、anthropics、gamedev-skills）在此期间已前进，下轮 CI 会自行比对、刷新既有原样件并推进 HEAD；本批新增件已按当前 HEAD 建基线，不会被误报漏检。
