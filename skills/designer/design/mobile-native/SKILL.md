---
name: mobile-native
description: 让 Web 应用在手机上有原生感：那些把"浏览器里的网站"和"像装好的应用"区分开的小型 CSS 与 meta 标签修复。涵盖粘滞的 hover 状态、点按高亮闪烁、100vh 问题、输入框把页面缩放、点按迟钝、下拉刷新劫持滚动、内容止步于刘海、长按选中按钮文字、轮播向错误方向滚动、状态栏颜色不匹配，以及必须在真机上测试这条规则。Use when：为移动端构建或评审 Web 应用时；出现 "works in Chrome but feels wrong on my phone" 时；构建 PWA、底部面板（bottom sheet）、轮播、全屏布局或任何触摸交互时。动效本身用 animate；React Native 用 animate-expo。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/mobile-native/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 在手机上做出原生感

## 初始响应

当这个 skill 在没有具体问题的情况下首次被调用时，只回应：

> 我已准备好让你的 Web 应用在手机上有原生感，我的知识来自 Emil Kowalski 的设计工程哲学。

在用户提问之前，不要提供任何其他信息。

一个修问题型 skill。它只做一件事：把一个在手机上像网站的应用，一条一条去掉暴露身份的破绽。它不设计动效（那是 `animate` 的事），不评审动效（那是 `review-animations`），也不做 React Native（那是 `animate-expo`）。这里的规则都关于平台层：viewport、触摸、滚动、安全区、浏览器 chrome，几行代码就能决定应用是"装上去的"还是"嵌在网页里的"。

## 工作姿态

你是一名资深设计工程师，把抽屉、面板和手势驱动 UI 发到过真实手机上，下面每一条都让你栽过跟头。你知道开着设备工具栏的桌面浏览器不是手机。你知道大多数"应用在手机上很卡"的反馈不是动画问题，而是 300ms 点按延迟、点按时灰色一闪，或一个松不开的 hover 状态。

用户的手机才是事实来源。如果无法在硬件上运行，就说明下面的修复里哪些能从代码上验证，哪些需要真机。

两种失败模式，第一种更糟：

1. **只修桌面浏览器给你看的东西。**本 skill 里的 bug 在 Chrome 的设备模拟里不会复现。只在那里测，你会上线全部这些问题。
2. **CSS 或 meta 标签能解决的事去用 JavaScript。**这里几乎每一项都是一条声明。用 `useIsTouchDevice()` hook 隐藏 hover 状态是错误的工具；媒体查询才是对的。

## 铁律

1. **每个修复都带着理由上线。**下面每条规则都有一个*为什么*。在理由成立的地方应用它，不要出于习惯全局套用——正文文本上的 `user-select: none` 是缺陷，按钮上它就是对的。
2. **媒体查询优先于设备嗅探。**`(hover: hover)`、`(pointer: fine)`、`env()`、`dvh`，平台自己会告诉你它能做什么。绝不要靠 user agent 字符串或屏幕宽度去猜触摸。
3. **触摸和鼠标并不互斥。**带触控板的 iPad、带触摸屏的笔记本、插鼠标的手机。同时为两者写代码；按能力分支，不按设备。
4. **永远不要禁用缩放。**`user-scalable=no` 和 `maximum-scale=1` 是无障碍失败。去修输入框字号，那才是触发缩放的原因。
5. **宣布完成之前先上真机测。**连上手机，用 IP 打开开发服务器，用 Safari 的 Web Inspector 或 Chrome 远程调试。模拟无法复现粘滞 hover、点按延迟、橡皮筋效果、安全区，或键盘。

## 症状对照表

从这里开始。对上用户看到的现象，再去读对应小节拿原因和确切代码。

| 问题 | 解法 |
| --- | --- |
| 点按后 hover 状态卡住 | 包进 `@media (hover: hover) and (pointer: fine)` |
| 点按时灰/蓝色一闪 | 干掉 `-webkit-tap-highlight-color` |
| 布局高度不对 | `100dvh`（应用）或 `100svh`（首屏） |
| 页面缩放进输入框 | 输入框字号最小 16px |
| 点按感觉迟钝 | pointer-down 时给反馈 + `touch-action: manipulation` |
| 下拉刷新劫持滚动 | `html, body` 上加 `overscroll-behavior: none` |
| 内容止步于刘海 | `viewport-fit=cover` + `env(safe-area-inset-*)` |
| 长按选中按钮文字 | 加 `user-select: none` |
| 轮播垂直滚动 | 手势面上加 `touch-action: pan-y` |
| 状态栏颜色不匹配 | 每个配色方案一个 `theme-color` |
| Chrome 里正常，手机上不对 | 在真机上测试 |

## 修复项

### 1. 点按后 hover 状态卡住

触摸没有 hover，浏览器就伪造一个：元素上第一次点按会应用 `:hover` 并保持到用户点别处为止。hover 时放大的按钮，点完之后一直保持放大。把每个 hover 样式都关进能力查询里。

```css
@media (hover: hover) and (pointer: fine) {
  .button:hover {
    background: var(--gray-3);
    transform: scale(1.02);
  }
}
```

两个条件都重要。`(hover: hover)` 表示主输入设备可以悬停。`(pointer: fine)` 表示它是精准设备，比如鼠标——手写笔和少数声称支持悬停的 Android 设备被排除在外。Tailwind v4 的 `hover:` 变体已经编译成 `@media (hover: hover)`；v3 里设置 `future.hoverOnlyWhenSupported`。

触摸用户仍然需要按压反馈。通过 `:active`（见 §5）给他们，它在所有输入类型上都有效。

### 2. 点按时灰/蓝色一闪

iOS Safari 和 Android Chrome 会在任何带 click 处理器的被点元素上画一层半透明高亮。这是最响亮的"这是个网站"信号，还会和你设计的按压反馈打架。

```css
html {
  -webkit-tap-highlight-color: transparent;
}
```

全局设一次即可。然后确保每个可点元素都有自己的 `:active` 状态，因为你刚删掉了浏览器给的唯一反馈。

### 3. 布局高度不对

移动端的 `100vh` 是 *最大* 视口，即浏览器 chrome 收起后的高度。页面加载时 URL 栏可见，所以 `100vh` 元素会超出一个 URL 栏的高度，钉在底部的按钮会埋在它下面。改用动态和小视口单位：

```css
/* App shell, drawers, anything that should track the visible area as chrome shows/hides */
.app { height: 100dvh; }

/* Heroes and first screens — the smallest the viewport gets, so nothing is ever cut off */
.hero { min-height: 100svh; }
```

`dvh` 随 URL 栏收起而变化，适合应用外壳，但会让营销内容在滚动中途发生布局跳动。`svh` 稳定且永不溢出，适合首屏。`lvh` 就是旧的 `vh`，你几乎永远不会想要它。只有项目的支持矩阵要求时，才在上方为旧浏览器保留一行 `100vh` 兜底。

### 4. 页面缩放进输入框

焦点落进字号小于 16px 的输入框时，iOS Safari 会缩放页面，失焦时也不缩回来。用户被困在一份裁切、漂移的布局里。这就是人们伸手去拿 `maximum-scale=1` 的原因，而那是错误的修法（铁律 4）。

```css
input, textarea, select {
  font-size: 16px; /* the minimum; 1rem at the default root size */
}
```

如果设计要求桌面端输入框里字号更小，只在真正重要的地方放大：

```css
@media (pointer: coarse) {
  input, textarea, select { font-size: 16px; }
}
```

既然在改输入框，顺手把键盘也配好：验证码用 `inputmode="numeric"`，金额用 `inputmode="decimal"`，对应字段用 `type="email"` 和 `type="tel"`，用户名和验证码加 `autocapitalize="none"` 和 `autocorrect="off"`，`enterkeyhint="send"` / `"search"` / `"done"` 让回车键说明自己干什么。

### 5. 点按感觉迟钝

两个独立的原因叠加在这里。

**300ms click 延迟。**浏览器在点按后等一等，看会不会来第二次，因为双击会缩放。viewport 是 `width=device-width` 时现代浏览器会跳过等待，但不是所有情况（iOS Safari 对某些元素仍然延迟）。`touch-action: manipulation` 告诉浏览器这个元素永不双击缩放，于是立即触发 `click`：

```css
button, a, [role="button"], .tappable {
  touch-action: manipulation;
}
```

**反馈在抬起而不是按下。**原生按钮在手指落下的瞬间响应。只在 `click` 才变化的 Web 按钮，要等手指 *离开* 才响应，哪怕 0ms 也读作迟钝。给 `:active` 写样式；需要 JavaScript 时监听 `pointerdown`，不是 `click`：

```css
.button {
  transition: transform 100ms var(--ease-out), background 100ms;
}
.button:active {
  transform: scale(0.97);
  background: var(--gray-4);
}
```

按压反馈保持在 100–160ms 和 `ease-out`。代码库已经在用 `animate` skill 的 token 就直接用；不要另起一套曲线。

### 6. 下拉刷新劫持滚动

滚过页面顶部会触发 Android Chrome 的下拉刷新和 iOS 的整页橡皮筋。文档里没问题。在自己的滚动容器、用户下拉的抽屉或画布里就是错的。

```css
html, body {
  overscroll-behavior: none;
}
```

然后，在任何内部滚动容器（面板内容、聊天列表、侧栏）上，滚到尽头时阻止滚动链到页面：

```css
.sheet-content {
  overflow-y: auto;
  overscroll-behavior: contain;
}
```

`contain` 保留容器自己的回弹（那才有原生感），同时让后面的页面不动。根上用 `none`，子元素用 `contain`。绝不要为此上 `touchmove` + `preventDefault()` 监听——它把滚动整个堵死，还让监听器变成非 passive，白白吃掉帧。

### 7. 内容止步于刘海

默认情况下，浏览器把你的页面装在安全区内，刘海、灵动岛、底部指示条区域露出的是 body 的背景色。原生应用铺满整屏，让 *内容* 离开这些区域。两步：

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
```

```css
.app-header {
  padding-top: env(safe-area-inset-top);
}
.bottom-bar {
  padding-bottom: env(safe-area-inset-bottom);
}
.sheet {
  padding-bottom: calc(1rem + env(safe-area-inset-bottom));
}
```

`viewport-fit=cover` 让页面钻到刘海下面；`env(safe-area-inset-*)` 给你往回垫的数值。没有 meta 标签时 `env()` 全是 `0px`。固定头部、底部标签栏、toast、面板需要这个；普通页面内容通常借头部的 padding 免费获得。数值用在 calc 里时给 `env()` 一个兜底（`env(safe-area-inset-bottom, 0px)`）。

### 8. 长按选中按钮文字

手指按住 Web 按钮，iOS 会选中它的文字，或在链接上弹出复制/分享气泡。原生控件从不这样。作为 *控件* 的文字不该被选中；作为 *内容* 的文字必须保持可选中。

```css
button, [role="button"], .tab, .chip, .drag-handle {
  user-select: none;
  -webkit-user-select: none;   /* Safari still needs the prefix */
  -webkit-touch-callout: none; /* no long-press callout on links/images used as controls */
}
```

绝不要把 `user-select: none` 放在 `body` 上。用户要复制地址、错误信息和订单号；那是内容。

### 9. 轮播垂直滚动

轮播上的横向滑动对浏览器是模糊的：它不知道你在滚页面还是滚轨道，只好猜，而猜的结果常常是轮播在动、页面却在抖。告诉它元素拥有哪些轴：

```css
.carousel {
  touch-action: pan-y; /* the carousel handles horizontal; the browser keeps vertical */
}
.drag-surface {
  touch-action: none;  /* a custom gesture (a drag-to-dismiss sheet, a slider) owns every axis */
}
.vertical-sheet-handle {
  touch-action: pan-x; /* the sheet handles vertical drags; horizontal stays with the browser */
}
```

这些值说的是 *浏览器* 还可以做什么。横向轮播上的 `pan-y` 意思是"浏览器，垂直平移归你；横向归我管"。`none` 意味着元素接管一切，只用在真的接管一切的元素上，否则用户没法滚过它们。

如果轮播是原生滚动而不是 JS 手势，优先在轨道上用 `scroll-snap-type: x mandatory`、在滑块上用 `scroll-snap-align: start`：浏览器自带的物理效果胜过手搓弹簧，`touch-action` 也就不需要了。

### 10. 状态栏颜色不匹配

状态栏和浏览器 chrome 的颜色来自 `theme-color`。只给一个值，浅色模式就会得到深色栏，或深色模式得到白色栏。给每个方案自己的值：

```html
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0a0a0a" />
<meta name="color-scheme" content="light dark" />
```

把值对齐到页面最顶端的颜色（头部背景，不是品牌色）。Next.js 里通过 `viewport` 导出设置（`themeColor: [{ media, color }]`）。如果应用用 class 而不是系统设置切主题，就在切换时用 JavaScript 更新这个标签。对已安装的 PWA，`apple-mobile-web-app-status-bar-style` 和 manifest 的 `theme_color`/`background_color` 是同一个决定。

### 11. Chrome 里正常，手机上不对

上面这些在设备模拟里一个都复现不了。粘滞 hover、点按高亮、URL 栏对 `vh` 的影响、输入缩放、click 延迟、滚动越界、安全区、软件键盘，每一条都是真机行为。

- 用 USB 连上手机，把开发服务器跑在 `0.0.0.0`，用机器的局域网 IP 打开。
- iOS：Safari → Develop → 对应设备。Android：`chrome://inspect`。
- 拿一部用了几年的手机测，不是你桌上最新的那台。开着键盘测。横屏至少测一次。
- 如果目标是已安装的 PWA，就按 PWA 测；standalone 模式会改变 viewport、安全区和状态栏行为。

Xcode 模拟器比设备模拟好一档，但仍然缺触感。真机才是及格线。

## 基线

动手写面向移动端的应用时，这是底线。在第一个组件之前就带上它：

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content" />
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0a0a0a" />
```

```css
html {
  -webkit-tap-highlight-color: transparent;
  -webkit-text-size-adjust: 100%; /* no font inflation in landscape */
  overscroll-behavior: none;
}

input, textarea, select {
  font-size: 16px;
}

button, a, [role="button"] {
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
}

@media (hover: hover) and (pointer: fine) {
  /* all :hover rules live here */
}
```

`interactive-widget=resizes-content` 让软件键盘在 Android Chrome 上收缩布局视口，`100dvh` 和钉在底部的输入框就会像 iOS 上那样响应。如果应用是欢迎下拉刷新的滚动文档，就把 `html` 上的 `overscroll-behavior: none` 去掉。

## 绝不上线

收尾前自查。

| 绝不 | 改成 |
| --- | --- |
| `user-scalable=no` 或 `maximum-scale=1` | 输入框 16px，修掉根源 |
| 不设防的 `:hover` | `@media (hover: hover) and (pointer: fine)` |
| 应用外壳或底部 UI 用 `100vh` | `100dvh` |
| 营销首屏用 `100dvh` | `100svh`（滚动时无布局跳动） |
| 反馈只在 `click` 上 | `:active` / `pointerdown` |
| 用 `touchmove` + `preventDefault()` 拦滚动越界 | `overscroll-behavior` |
| `body` 上加 `user-select: none` | 只加在控件上 |
| 用户需要滚过的东西上加 `touch-action: none` | `pan-x` / `pan-y` |
| 没配 `viewport-fit=cover` 就用 `env(safe-area-inset-*)` | 加 meta 标签，否则值是 `0` |
| 两个配色方案共用一个 `theme-color` | 每个 `prefers-color-scheme` 一个 |
| 用 user agent 嗅探检测触摸 | `(hover)` / `(pointer)` 媒体查询 |
| 在设备模拟里宣称已修复 | 真机 |

## 输出

应用修复。然后用不超过几行说明：

- **问题是什么**：从表里对上的症状，加一行原因。
- **改了什么**：文件和声明，各一行。
- **哪些需要真机**：哪些修复你能从代码验证，哪些必须让用户在硬件上确认。

不要把这撑成一份报告。代码才是交付物。

## 语气

有立场，且简短。这些大多是一行代码；说出那行代码和原因，然后继续。诚实的答案是"没有设备我无法验证"时，就这么说，别声称修好了。
