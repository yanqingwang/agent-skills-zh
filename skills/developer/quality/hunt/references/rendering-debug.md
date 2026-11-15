> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/hunt/references/rendering-debug.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 渲染 bug 调试参考

## 渲染 bug 模式

激活场景："PDF 看起来不对"、"分页问题"、"字体不渲染"、PDF 输出损坏、打印布局错误。

先静态分析（审查 CSS），需要时再复现。

### WeasyPrint

- `rgba()` 会触发双重矩形 bug：改用实心十六进制颜色
- `page-break-inside: avoid` 常被忽略：使用显式分页
- 基于 float 的布局在分页边界处常出问题：优先用 flexbox 或 block
- 渲染时外部字体 URL 被拦截：以 base64 内嵌字体或本地托管

### 字体加载

- 检查 `@font-face` 的 src 路径（相对还是绝对）
- 外部字体的 CORS 头必须允许渲染来源
- 格式支持：WeasyPrint 偏好 WOFF/TTF；WOFF2 支持取决于版本
- 缺少字体回退 = 文字不可见或使用系统回退字形

### 页面溢出

- 逐行调试之前，先算内容高度与页面高度的差
- 缩小 `line-height`、`padding` 或 `margin` 来腾出空间
- 孤行/寡行控制：在 `@page` body 规则中写 `orphans: 3; widows: 3`

### 浏览器打印 CSS

- 确认 `@media print` 规则存在且未被覆盖
- `@page` 边距要计入打印机不可打印区域（至少约 6mm）
- 在章节分隔处使用 `break-before: page` / `break-after: page`
- 在浏览器 DevTools 中用 `window.print()` 测试，不要只看视觉预览
