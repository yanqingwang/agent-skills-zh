> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/primitive-terminal.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 终端窗口（CLI 外壳变体）

可选的整页皮肤，把任何图表包进一个假终端窗口：带三个圆点的标题栏、一行 `$` 提示符、通篇等宽字体。用于开发者工具发布、CLI 产品帖，以及需要把截图读成"终端"而非"编辑文档"的技术社交卡片。

这是一个**第二种、固定的皮肤**，token 表见 [style-guide.md § Terminal skin](style-guide.md#terminal-skin-opt-in-alternate)。它不继承 `onboarding.md` 的品牌 token，也不参与浅色/深色反色规则；每个终端示例都用同一组九个 token，与宿主站点的品牌无关。

## 语法

```html
<div class="terminal">
  <div class="titlebar">
    <div class="dot accent"></div>
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="titlebar-name">loop.sh — self-improving-loop</div>
  </div>
  <main class="frame">
    <p class="prompt">
      <span class="sign">$</span> diagram-design render --type loop
    </p>
    <h1># The self-improving loop</h1>
    <svg>...</svg>
  </main>
</div>
```

```css
body {
  background: var(--terminal-page);
}
.terminal {
  background: var(--terminal-paper);
  border: 1px solid var(--terminal-border);
  border-radius: 12px;
}
.titlebar {
  background: var(--terminal-bar);
  border-bottom: 1px solid var(--terminal-border);
}
.dot {
  background: var(--terminal-soft);
}
.dot.accent {
  background: var(--terminal-accent);
}
```

在 SVG 内部，把默认的浅色/深色 token 按 1:1 换成对应的 `terminal-*` 版本：`paper` → `terminal-paper`，`ink` → `terminal-ink`，`muted`/`soft` → `terminal-muted`/`terminal-soft`，`accent`/`accent-tint` → `terminal-accent`/`terminal-accent-tint`。枢纽/焦点节点模式（被高亮的那一个元素反色填充）依然适用。

## 字体排印

**通篇等宽**：这是唯一一个"全等宽"正确的变体。完全去掉 Instrument Serif 和 Geist 无衬线；页面标题用等宽、粗体，前缀 `# `（读起来像注释行）。eyebrow 变成 shell 提示符：`$ ` 用 `terminal-accent`，命令用 `terminal-muted`。

所有文字角色都在 `style-guide.md` 的默认字号阶梯之上调高约 1–2px（如 `node-name` 12px → 14px，`sublabel`/`arrow-label` 8–9px → 9–10px，枢纽标签 16px → 18px）。等宽字体在默认字号下，比它所替代的衬线/无衬线混排看起来偏小，而这些卡片通常是在社交信息流的缩放下观看，不是全幅展示。

## 标题栏圆点

三个 10px 圆点，macOS 风格。**单 accent 规则在这里同样约束颜色**：一个圆点是 `terminal-accent`，另外两个是 `terminal-soft`。不要用红/黄/绿红绿灯三色：那是第二、第三种色相，调色板禁止。

## 关键规则

- 不用纯黑（`#000000`）：用 `terminal-page`（`#0a0a0a`）/ `terminal-paper`（`#141414`）。与默认皮肤同一条规则、同一个理由：真黑在 OLED 和印刷上会截断。
- 只允许一个 accent。图需要第二个焦点元素时，用 `terminal-ink`（白）以字重/字号做强调，不用第二种颜色。
- 背景点阵图案（如使用）保持 `rgba(255,255,255,0.06–0.08)`：隐约可见的纹理，不与标题栏外壳争抢视觉。

## 何时使用

- 开发者工具 / CLI 产品发布帖（npm 包、CLI 标志、终端工作流）。
- "这是给工程师的工具"本身就是信息一部分的技术社交卡片。
- 想在深色为主的信息流（X、Discord、开发者博客）里跳出来的截图。

## 何时不用

- 编辑类 / 长文帖：改配默认浅色或完整编辑排版变体。
- 来自 `onboarding.md` 的品牌匹配输出：终端是固定皮肤，不做品牌 token 化。别想着把两者调和。
- 任何读者群体不会把 `$`/`#`/标题栏圆点读成外壳而非内容的图。
