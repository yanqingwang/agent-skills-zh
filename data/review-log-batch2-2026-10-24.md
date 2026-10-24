# 第二批校验报告（review log · batch 2）

**校验日期：2026-10-24** · **范围**：第二批全生态 Top 20（20 个 SKILL.md 翻译件 + 1124 个原样配套件，17 个新上游）
**校验者**：父会话 bash 机械检查 + 2 个独立忠实度子代理（A 组 10 件 / B 组 10 件，沿用第一批"拆分校验"方法论）
**对照基准**：[review-checklist.md](review-checklist.md)
**结论：AGREE（20/20 PASS，可交付用户检查）**

## A. 合规红线（PASS）

- **A1 PASS**：17 个新上游 License 逐一经 gh api 核实（16 × MIT + caveman Apache-2.0 自 3.0.0 起全仓统一，LICENSING.md 原文核读）。收录清单见 [upstream-inventory.md](upstream-inventory.md) 第五节。
- **A2 PASS（红线）**：multica-ai/andrej-karpathy-skills 与 anthropics/skills（官方仓库，2026-10-24 查证 license: NONE）交付文件零出现。grep "karpathy" 在 skills/ 仅命中 1 处：last30days 上游 verbatim 代码 `scripts/lib/rerank.py:525`（人名别名模糊匹配算法自身逻辑），属上游原样件而非 karpathy-skills 内容。
- **A3 PASS**：THIRD-PARTY-NOTICES.md 追加 17 个上游（含 caveman Apache-2.0 条款摘要与版权行），明确排除区新增 anthropics/skills（无 License）与 gstack（整仓型延后）条目。
- **A4 PASS**：20/20 翻译件声明块完整（上游链接 / 原文件路径 / License / 翻译日期 2026-10-24 / AI 辅助翻译 / 非官方声明 / GLOSSARY 链接）。
- **A5 PASS**：无"官方中文版"声称。

## B. 忠实度（20/20 PASS，2 个独立子代理核对）

| 文件 | 标题序列 | 代码块 | 段落抽查 |
|---|---|---|---|
| rea/reverse-engineer-anything | 7/7 | 1/1 逐字 | PASS |
| ponytail/ponytail | 4/4 | N/A（无代码块） | PASS |
| caveman/caveman | 15/15 | N/A | PASS |
| archify/archify | 11/11 | 2/2 逐字 | PASS |
| understand-anything/understand | 23/23 | 27/27 逐字 | PASS |
| last30days-skill/last30days | 9/9 | 2/2 逐字 | PASS |
| diagram-design/diagram-design | 23/23 | N/A | PASS |
| humanizer/humanizer | 39/39 | N/A | PASS |
| i-have-adhd/i-have-adhd | 16/16 | 1/1 逐字 | PASS |
| marketingskills/product-marketing | 23/23 | 1/1 逐字 | PASS |
| scientific-agent-skills/experimental-design | 16/16 | 4/4 逐字 | PASS |
| ecc/search-first | 22/22 | 5/5 逐字 | PASS |
| ecc/security-review | 48/48 | 22/22 逐字 | PASS |
| ecc/continuous-learning-v2 | 23/23 | 9/9 逐字 | PASS |
| ecc/autonomous-loops | 46/46 | 23/23 逐字 | PASS |
| book-to-skill/book-to-skill | 29/29 | 全部逐字 | PASS |
| planning-with-files/planning-with-files | 45/45 | 12/12 逐字 | PASS |
| distilly/distilly | 4/4 | N/A | PASS |
| brag/brag | 13/13 | 3/3 逐字 | PASS |
| prompt-master/prompt-master | 13/13 | 1/1 逐字 | PASS |

## C/D. 机械检查（父会话 bash 取证，全部 PASS）

- 声明块 20/20；frontmatter `name` 与上游一致 20/20；代码围栏数量一致 20/20；行差全部落在 +3~+14（声明块开销）。
- manifest 全部 local 路径存在（含第二批 verbatim 1124 件），零缺失。
- classify.py 重跑：31 件全部归类，13 个分类（新增 8 类），experimental-design 不再误入"设计品味"。
- fetch_verbatim.py 打补丁支持 >1MB 大文件（raw 媒体类型）。`--check` 全量结果：ok=1176 fail=0 diff=3 → 3 件 DIFF 定位为 planning-with-files 上游于当日 18:50（CEST）发布 v3.25.2（晚于抓取快照）→ 重拉上游刷新 3 个脚本原样件（定向复检 31/31 一致），译文由代理按 diff 增量同步至 v3.25.2（新增"新计划创建契约"节等三处，517 行 vs 原文 513 行）。终态：**1210 件全部逐字节一致（fail=0 diff=0）**。

## 术语与功能性标记处理记录（抽样摘录）

- caveman：电报体英文示例保留原样（改中文会改变省 token 行为）；触发口令 `/caveman`、"caveman mode"、"stop caveman" 保留英文附中文注。
- humanizer：26 个英文 AI 腔 pattern 与禁用词清单保留英文（被指认对象本身），解释文字译中文。
- last30days：`LAW 1~11` 标签保留英文（被 references/ 交叉引用）；输出散文标签（`What I learned:` 等）保留英文。
- understand：`STOP`（9 处）、`$LANGUAGE_DIRECTIVE`、阶段名 SCAN/BATCH/… 保留英文；86 个代码块逐字节一致。
- planning-with-files：计划文件约定名、`===BEGIN PLAN DATA===` 定界符、Hook 英文报错串保留。

## 已知上游瑕疵（忠实保留，未修复）

- book-to-skill 原文步骤 10 存在未闭合 ```bash 围栏、Skill Locations 列表编号重复；译文逐行对应保留。
- continuous-learning-v2 原文 H1 因上游连字符换行拆成两行，译文按语义合并为一行（内容无增删）。

## 第二批执行教训

1. 并发 10 个翻译子代理触发"user concurrency limit"，改为**单代理串行**（用户点名）后稳定完成。
2. 一次用户中断导致 rea 翻译写到 134/504 行即中止 → 翻译完成度必须以**行数下限硬校验**（本轮已加入 ≥原文-10 行的自检项），rea 重做后 518 行。
3. gstack 类"整仓型"上游（skill 引用仓库根 bin/ 30+ 处）不适用单目录收录原则，需要独立的"整仓收录"模式——已记入第三批。
