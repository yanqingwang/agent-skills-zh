<!-- AUTO-GENERATED from capy-pr.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/capy-pr.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 19-C：Capy PR 正文（What changed、Why、Approvals）

仅在 Step 19 打印了 `CAPY_PR: on` 时读本节。Capy 下由人从 PR 与 READY
报告（经 Captain）决定合并，所以正文要用图展示改了什么、为什么、谁批
了什么。指南：Capy `gstack` Skill 的 SKILL.md 旁的 `captain.md`。

**顺序。** Step 19 写了 `gstack-ship-receipt` 块时它保持第一。然后是
`## What changed`、`## Why` 与 `## Approvals`，再是下方标准节。
`## Summary` 只写 commit 主题；不要重复图片说明。

1. **挑证据：** 一到三组前后对比，信号最强的放第一。第一张就是关键
   图。
   - UI 改动：用 browse 流程或宿主浏览器，在 base 与本分支以相同
     尺寸截取被改屏幕。
   - Skill 或提示词改动：`~/.claude/skills/gstack/bin/gstack-pr-shots --path <template or SKILL.md> --heading "<changed section>" --caption "<what changed and why>"`。
   - CLI 改动：把本次 ship 已经跑过的某命令在 base 与本分支的输出
     存进仓库文件（`.gstack/tmp/before.txt`、`.gstack/tmp/after.txt`），
     然后 `~/.claude/skills/gstack/bin/gstack-pr-shots --before <file> --after <file> --kind terminal --caption "<…>"`。
     绝不为做一张图去跑有副作用的命令。
   - 无可见表面：用最能体现改动的源码段或测试输出做图。
   `gstack-pr-shots` 拒绝命中密钥扫描器的输入
   （`PR_SHOTS_INPUT_REFUSED`）。从截取物中移除密钥；绝不绕过拒绝。
2. **读 `SHOT_PNG:`。** 是路径：用它。`unavailable (…)`：用你自己的
   浏览器以 880 px 宽截取打印的 `shot.html`，用那张 PNG。
   `failed (…)`：只用文字版。
3. **上传。** 仅限公开仓库（`gh repo view --json visibility -q .visibility`
   打印 `PUBLIC`）。私有仓库用文字版，除非那个人批准了图片（用
   `gstack-approvals add` 记录）。每张 PNG 用 Capy 的 PR 资产工具
   （`tools.pr.uploadAsset`）上传。精确内嵌它返回的 URL，图片说明作
   alt 文本：`![<caption>](<url>)`（返回的裸视频 URL 单独成行）。上传
   失败时仅为瞬时错误重试一次。否则用文字版并在说明下写
   `image upload failed: <reason>`。绝不为一张图阻塞发布。
4. **每张图下：** 一行说明改了什么、为什么，然后是打印的 `text.md`
   内容（折叠的文字前后对比，给看不到图的读者与搜索用）。
5. **`## Why`：** 两三句话，覆盖起因（issue、失败的运行，或那个人的
   请求，带引语）与用户将看到的效果。
6. **`## Approvals`：** 逐字呈现
   `~/.claude/skills/gstack/bin/gstack-approvals render` 的输出。它会
   转义单元格内容，回执绝不把它当作批准引用。
   `APPROVAL_RECORD_UNAVAILABLE` 时保留其文字并在 READY 报告中说明。
   绝不手打表格行。
7. **READY 报告：** 把关键图的 PNG 附到你发的报告上（Capy 的消息
   附件）并给出其上传 URL，让 Captain 能内联展示。
