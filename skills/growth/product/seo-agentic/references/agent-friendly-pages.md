> **中文汉化版** · 上游：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) · 原文件：`skills/seo-agentic/references/agent-friendly-pages.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 友好页面：页面级审计参考

Agent 代替人行事：搜索、比较、填表、下单。它们通过三条通道读取页面，多数 agent 三条并用：

1. **截图 + 视觉模型**：视觉层级、按钮显著度、布局。慢且费 token。
2. **原始 HTML 与 DOM**：嵌套结构、ID、class、data 属性。
3. **无障碍树（accessibility tree）**：浏览器的语义摘要（role、name、状态）。三者中最干净的信号，也是厂商共识的一条。OpenAI 的发布者指南说其浏览器"使用 ARIA 标签……来理解页面结构和交互元素"；Lighthouse Agentic Browsing 文档把无障碍树称为 agent 的主要数据模型；WebKit 对 WebMCP 的反对意见也主张使用无障碍树，而不是另建一层并行工具层。

原生元素优先于 ARIA（W3C ARIA 第一原则）。ARIA 是修复自定义控件的，它不能替代真正的 `<button>`。

**一手来源：** Google 的 AI 优化指南（developers.google.com/search/docs/fundamentals/ai-optimization-guide）、其中链接的 web.dev agent-friendly 文章，以及 Chrome 的 Lighthouse Agentic Browsing 文档（developer.chrome.com/docs/lighthouse/agentic-browsing）。

## 审计清单

### 1. 使用真实的交互元素

| 通过 | 失败 |
|---|---|
| 用 `<button>` 做操作 | `<div onclick="...">` |
| 用 `<a href="...">` 做导航 | `<div onclick="window.location...">` |
| `<input>` / `<select>` / `<textarea>` | 自定义 `contenteditable` 控件 |

如果真实元素实在用不了，提供 `role`、`tabindex="0"`、可访问名称（accessible name），以及 Enter 和 Space 的按键处理器。自定义 div 控件进入无障碍树时常常没有 role，agent 会直接跳过它们。

### 2. 可访问名称与标签

每个输入框都需要 `<label for>`、`aria-label` 或 `aria-labelledby`。每个纯图标按钮都需要可访问名称。这些对应 Lighthouse `agent-accessibility-tree` 审计内的 axe 规则 `label`、`button-name`、`link-name`、`select-name` 和 `input-button-name`（完整列表见 `references/lighthouse-agentic-category.md`）。

### 3. 交互目标尺寸

视觉通道会丢弃未遮挡面积极小的交互元素。WCAG 2.2 AA 要求 24 x 24 CSS 像素（Apple HIG 为 44 x 44）；满足这两者也就过了 agent 的门槛。比这更小的，一律视为"对 agent 不可见"的候选。

### 4. 交互节点上不要有透明覆盖层

视觉模型会丢弃被遮挡的节点。常见肇事者：

- 盖在每个子链接之上的整卡点击处理器。
- 用户同意后仍残留的 cookie 同意层。
- 关闭后仍保留 `pointer-events: auto` 的 modal portal。
- 使用 `position: absolute; inset: 0` 的追踪层。

### 5. 布局稳定性

CLS 保持在 0.1 或以下（Lighthouse 把它计入 Agentic Browsing 分数），并且让功能相同的操作在各模板中待在同一个位置。一个在 `/shoes` 和 `/bags` 之间换位置的"加入购物车"按钮，会迫使截图类 agent 每页重新学习。

### 6. `cursor: pointer` 作为信号

视觉模型把 `cursor: pointer` 读作"可操作"。把它留在真实控件上，绝不加到非交互元素上。

### 7. 稳定且有含义的选择器

解析 DOM 的 agent 依赖 landmark（`<nav>`、`<main>`、`<article>`、`<aside>`）、布局容器上稳定的 `id`，以及描述用途的 `data-*` 属性。只有哈希过的 class 名对 agent 什么信息都给不了。

### 8. 需要标注的失败模式（从业者共识，非厂商实测）

- 仅悬停才出现的菜单，以及没有分页链接的无限滚动。
- 缺少对应 ARIA 模式的自定义下拉框和日期选择器。
- 封闭的 shadow DOM 和纯 canvas 界面。
- 陷阱焦点或遮挡控件的同意横幅或 modal。
- 内容页和信息页上的 CAPTCHA 或 bot 挑战。
- 主内容仅在客户端渲染（用 `agentic_check.py` 的 `server-rendered` 检查）。
- 一闪而过或只存在于 toast 里的确认状态。

目前没有受控的公开研究把无障碍树质量与 agent 任务成功率联系起来。把这些当作有推理依据的实践呈现，不要当作实测的提升。

## 工具

```bash
# Local 0-100 Agent-UX heuristic (HTML semantics + Chromium accessibility tree)
"${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo" run agent_ux_check.py <URL> --json

# Raw accessibility tree without scoring
"${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo" run render_page.py <URL> --mode auto --a11y-tree --json

# Google's own pass/fail view (the X/N fraction)
"${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo" run lighthouse_agentic.py <URL> --json
```

Agent-UX 分数是本地启发式。绝不要把它当作 Lighthouse Agentic Browsing 结果来呈现，后者是一个分数（X/N），不是 0-100 分。

## 快速人工检查

在 DevTools 里打开 Accessibility 面板或整页无障碍树，查看：

- 被暴露为 `generic` 的交互元素（语义坏了）。
- 没有可访问名称的输入框或按钮。
- 有点击处理器但没有 role 或 tabindex 的 `<div>`。

## 最后核验

2026-09-23，对照 Lighthouse 13.5.0 源码与 Chrome 的 Agentic Browsing 文档。当 web.dev 修改 agent-friendly 标准、或 Lighthouse 变更 `agent-accessibility-tree` 规则集时，需要重新核验。
