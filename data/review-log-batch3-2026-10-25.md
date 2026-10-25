# 第三批校验报告（review log · batch 3）

**校验日期：2026-10-25** · **范围**：13 个新上游（12 MIT + video-shotcraft/Vibe-Skills Apache-2.0）、21 个 SKILL.md 收录（20 实译 + video-shotcraft 中文原生收录）、2739 个原样配套件（累计 3918）
**校验者**：父会话 bash 机械检查 + 2 个独立忠实度子代理（A 组 11 件 / B 组 10 件）
**结论：AGREE（21/21 PASS，3918 件字节一致 diff=0）**

## A. 合规（PASS）

- 13 个上游 License 逐一核实：11 MIT + 2 Apache-2.0（video-shotcraft / Vibe-Skills）， THIRD-PARTY-NOTICES 已补 13 节
- 无 License 仓库（karpathy-skills / anthropics/skills）零出现
- 声明块 21/21（翻译日期 2026-10-25，gstack 三件按整仓模式注明）；无"官方中文版"声称

## B. 忠实度（21/21 PASS，双代理抽查）

- A 组（gstack×3 + 单件 8）：标题序列全对齐（office-hours 48/48、plan-ceo-review 56/56、qa 49/49 等）；代码块全量逐字节比对 90/90 一致
- B 组（其余 10）：标题全对齐；52 个代码块逐字节一致；标识符零漂移（retryOnFail×10、sourceIndex×9 等精确核对）
- 发现并修复 1 处轻微问题：notebooklm 代码块内一行注释被译 → 已回退英文原文
- video-shotcraft：去声明块后正文与上游逐字节一致（中文原生收录验证）

## C/D. 机械与管线（PASS）

- 机械检查：声明块 21/21、frontmatter name 一致 21/21、代码围栏一致 21/21、行差 +0~+14
- manifest 路径全量存在性 0 缺失；classify 52 件全归类
- **fetch_verbatim.py 新增 `--trees` 模式**：一仓一次 trees API + 本地 `git hash-object` blob SHA 比对（内容哈希等价逐字节），替代逐文件 API（3918 件每日校验的请求量从 ~4000 降至 ~35）
- 全量字节校验终态：**ok=3918 fail=0 diff=0**

## 校验过程中发现并修复的问题（过程记录）

1. **manifest 前缀笔误连锁**：登记脚本 planned 集漏写 `skills/` 前缀 → 21 件全部被误移 verbatim → 反向修复；ai-research-skills 的 cp -r 因目标目录已存在产生嵌套 `0-autoresearch-skill/0-autoresearch-skill/`，磁盘扁平化 + manifest upstream/local 双键修正
2. **上游漂移 17 件**：taste-skill(6)、gstack(8)、rea(3) 在快照后更新 → raw 逐件刷新 + sync-state HEAD 更新；rea 上游 SKILL.md 仍为 v49（仅 references 更新），译文无需跟进
3. 教训：`cp -r src dest` 前必须确保 dest 不存在（用 `rsync -a src/ dest/` 或先删目标）；manifest 批量改键后必须重跑全量校验闭环
