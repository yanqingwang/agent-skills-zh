# 第八批校验报告（review log · 2026-11-03）

**校验日期：2026-11-03** · **范围**：2 个存量合集追加，8 个翻译件、80 个原样件（累计 61 登记 / 60 监控 / 176 翻译件 / 5194 原样件）
**校验者**：父会话机械检查（围栏代码块逐字节比对 / YAML / 声明块 / blob SHA）+ 5 组翻译代理自检回报
**结论：PASS（8/8 代码块与上游逐字节一致；lint 0 信号；无待重译工单）**

## 本批收录

| 上游 | 追加件 | 原样件 |
|---|---|---|
| muratcankoylan/Agent-Skills-for-Context-Engineering | memory-systems、tool-design、multi-agent-patterns、bdi-mental-states | 11（references/ + scripts/：memory_store.py、description_generator.py、coordination.py 等） |
| K-Dense-AI/scientific-agent-skills | literature-review、peer-review、scientific-writing、statistical-power | 69（assets/ 模板 + references/ + scripts/：generate_pdf.py、power.py、simulate_power.py 等） |

## 机械校验（全量）

- **翻译件**：8/8 frontmatter YAML 解析通过、`name` 保留英文、`description` 已译、声明块三行逐字、代码块逐字节一致（bdi-mental-states 的 Turtle/SPARQL/Prolog 块、scientific-writing 的 8 个块、statistical-power 的 4 个块等全部原样）
- **原样件**：80 件随 clone 同步拷贝，与上游 HEAD 同源；同步引擎复核 blob SHA 无差异（verbatim刷新=6 均为上游既有件刷新，非本批）
- **lint_zh_style**：0 信号（8 件初检即通过）
- **推荐区路径自检**：gen_readme_sections.py 报出 `citation-management` 路径错误（实为 `skills/researcher/info/` 非 `skills/researcher/science/`），已按 manifest 实际路径修正——脚本的 manifest 交叉校验机制有效拦截了一次错误推荐

## 文件级 License 核验

literature-review 与 statistical-power 源 frontmatter 为 `license: MIT license`（非 SPDX 写法，同一许可）；scientific-writing / peer-review 为 `license: MIT`；余 4 件无文件级字段，按仓库级 MIT 收录。无仓库级与文件级不一致情形。

## 收录定位说明

本批零新上游，是「缓收清单消化」而非扩张：两个大合集（muratcankoylan 18 件、K-Dense 177 件）中筛出跨领域、跨项目可复用的方法论级技能，其余单库/单领域指南（如 anndata、astropy、diffdock）继续缓收——它们绑定特定 Python 环境与研究流程，与本仓库「drop-in 即用」的定位不符。
