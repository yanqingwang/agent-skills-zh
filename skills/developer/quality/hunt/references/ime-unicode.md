> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/hunt/references/ime-unicode.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# IME / Unicode 调试参考

webview 宿主应用与 macOS 原生应用中反复出现的模式。在形成假设之前先检查这些。

## IME 状态失步

**症状**：拉丁字符显示正常，但 CJK（中日韩）输入丢失、重复或在错误的时机上屏。

**疑似原因**：
- 组合中途切换输入法：IME 把 preedit 用过时的目标上屏，随后新模式又处理一遍同样的按键。
- 组合进行中 `keydown` 处理器吞掉事件：抑制确认事件绑定的提交/导航动作，同时保留 IME 正常的文字上屏。不要把该动作排到 `compositionend` 再执行；`isComposing` 已经为 false 的情况见"事件顺序"一节。
- Webview 与原生窗框分离焦点：在 Tauri 中，webview 与原生窗口标题栏可以同时持有焦点。IME 组合期间点击原生控件会触发 focus-out，把不完整的 preedit 文本上屏。

**观测手段**：
- 记录 `compositionstart`、`compositionupdate`、`compositionend` 的顺序；确认它们按序触发、无缺漏。
- 记录每个 `compositionupdate` 的 `data` 字段；突然出现的空字符串意味着被强制上屏。

## IME 上屏后光标位置漂移

**症状**：确认一个 CJK 词之后，光标跳到错误位置或选区塌缩。

**疑似原因**：
- 组合期间 DOM 被改动：`isComposing` 为 true 时 React/Svelte/Vue 重新渲染会重置选区。批量合并状态更新，只在 `compositionend` 时统一刷出。
- 混用偏移单位：JavaScript 字符串长度与文本节点 DOM 偏移使用 UTF-16 code unit；字符串迭代数的是 code point，而可见字符操作可能需要字素簇（grapheme cluster）。转换位置之前先确认接收方 API 使用的单位；把 `str.length` 换成 `[...str].length` 本身也可能造成漂移。

## Emoji ZWJ 序列被拆开

**症状**：多人或职业 emoji（例如 `👩‍🚒`）被渲染成两三个独立 emoji，或 ZWJ（`U+200D`）以可见字符出现。

**疑似原因**：
- 在 UTF-16 code unit 偏移处切片：若 `n` 落在序列内部，`str.slice(0, n)` 会把 ZWJ 序列切开。可见字符截断应使用 `Intl.Segmenter` 配合 `granularity: 'grapheme'`。
- 字体不支持该序列：字体逐个渲染每个 code point。用 `canvas.measureText` 验证，或通过 `document.fonts` 查看实际使用的字体。
- 序列化时 ZWJ 被剥掉：某些 JSON 编码器会规范化或转义 `U+200D`。核对存储字符串的原始字节。

**测试**：`[...'👩‍🚒'].length` 是 3 个 code point；`[...new Intl.Segmenter(undefined, {granularity: 'grapheme'}).segment('👩‍🚒')].length` 是 1 个字素簇。针对消费方 API 单独测试偏移。

## `compositionend` / `keydown` 事件顺序

**症状**：绑定在 Enter 或 Tab 上的动作在 IME 确认期间触发，提交了不完整的输入。

**疑似原因**：`compositionend` 可能先于确认 `keydown`（此时 `isComposing` 已为 false），也可能在其之后。以受影响的 IME 与宿主的实际顺序为准，不要从操作系统推断。

**验证目标**：IME 确认只上屏文本不提交；随后的有意 Enter 只提交一次。在 `compositionend` 时清除的标志与 `isComposing` 有同样的顺序缺口。记录按键事件与组合边界，从观察到的宿主行为推导确认键守卫，并在回归测试中重放两种顺序加上一次正常 Enter。不要用任意超时替代这些证据。

## macOS 文本系统与 Webview 冲突

**症状**：撤销（`Cmd+Z`）回退的是单个 IME preedit 字符而不是已上屏的词；或系统文本快捷键（Cmd+Shift+Left 选词）在 webview 内外的表现不一致。

**原因**：WKWebView 有自己的文本系统，与 NSTextView 的约定部分重叠。webview 宿主的按键处理配置可能抑制系统快捷键（Tauri 的 `tauri.conf.json` 或 `app.json` 中的 `preventDefaultFor`，或其他宿主的等价物）；检查其中是否存在过宽的 `preventDefault` 规则。
