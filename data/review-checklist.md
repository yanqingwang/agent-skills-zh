# Deepseeker 校验清单（review-checklist）

> 校验执行者按此清单逐项核查并输出结论。全部 PASS 才算"双方一致"。
> 校验结论写入 `data/review-log-2026-10-24.md`（含逐文件 PASS/ISSUE 与修复记录）。

## A. 合规红线（任一 FAIL 即整体 FAIL）

- [ ] A1. 收录文件仅来自 License 为 MIT/Apache-2.0 的仓库（第一批 4 个 MIT + 第二批 16 个 MIT + caveman Apache-2.0）
- [ ] A2. **无任何内容来自无 License 仓库**（multica-ai/andrej-karpathy-skills、anthropics/skills 必须零出现；上游 verbatim 代码中对人名 "karpathy" 的算法性引用除外）
- [ ] A3. THIRD-PARTY-NOTICES.md 含全部上游（第一批 4 + 第二批 17）的 License 声明与版权归属
- [ ] A4. 每个翻译文件头部有声明块：上游链接、原文件路径、License、翻译日期、"AI 辅助翻译"、"非官方中文版"
- [ ] A5. 未声称"官方中文版"

## B. 忠实度抽查（逐文件）

- [ ] B1. 从上游重新拉取原文，对比章节标题序列：数量与顺序一致
- [ ] B2. 抽查每个文件 2-3 个关键段落：语义一致，无漏译、无添加原文没有的建议
- [ ] B3. 代码块/命令/路径与原文逐字一致（翻译不得改动代码）
- [ ] B4. frontmatter 的 name 保留英文原值；description 为中文

## C. 术语一致性

- [ ] C1. GLOSSARY.md 统一译法全库一致（grep：提示词/代码审查/根因/上下文工程/规格 等无变体混用）
- [ ] C2. 不译词未被翻译（grep：Skill/Agent/Harness/Hook/worktree/token 不应以"技能/代理员/挽具/挂钩/代币"等出现）

## D. 结构与管线

- [ ] D1. 全部翻译件与 verbatim 件存在于 data/manifest.json 声明的 local 路径
- [ ] D2. scripts/classify.py 可运行且生成的 data/category-index.md 覆盖全部翻译件、分类正确
- [ ] D3. .github/workflows/sync-check.yml 语法有效（yaml 解析通过）
- [ ] D4. scripts/fetch_verbatim.py --check 全量 1210 件逐字节一致（第二批起含 >1MB 大文件，raw 媒体类型抓取）
- [ ] D4. data/upstream-inventory.md 星标数与 gh api 实时值一致（±0.5%内）且 License 标注正确
- [ ] D5. **目录完整性**：各 SKILL.md 正文引用的目录内文件在本地全部存在（无悬空引用）；manifest `verbatim` 清单 51 个文件全部落盘；`python3 scripts/fetch_verbatim.py --check` 返回 diff=0（原样件逐字节一致）；`verbatim_excluded` 之外无遗漏的运行所需文件

## 输出格式

每个文件一行：`PASS | 文件路径 | 备注`；整体结论：`AGREE`（双方一致，可交付用户检查）或 `DISAGREE`（附问题清单与建议修复）。
