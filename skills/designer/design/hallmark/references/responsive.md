> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/responsive.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 响应式

不寻常的布局时加载。不存在只有桌面才有的交互；每一页从 320 到 1920 CSS 像素都无瑕疵渲染。

## 脚本能查什么、查不了什么

sloplint 在 320、375、414、768、1024、1280、1440 与 1920 宽度覆盖机械的那一半：水平滚动与 `overflow-x: clip`（34）、换行的控件（49）、图片轨道与展示标题（50）、radio 式标签页（53）、堆叠的吸顶元素（56）。它看不到的在每个宽度用眼睛检查：每条桌面侧栏或过滤列都要能折叠成菜单或 disclosure，区块标题堆叠为单列，每个主题级覆盖都要带自己的移动端规则。

## 断点

两个，全页共用，用 `rem` 以跟随用户的字号。脚手架在这两处都把 token 调低：60rem 以下（约 960px，布局断点）gutter 降到 24px，三个 section gap 降到 80、96、120px；40rem 以下（约 640px，字体断点）gutter 降到 16px，section gap 降到 56、72、96px，列间距降到 16px。组件规则对准同样两个宽度，整页只朝一个方向写。只在内容本身断裂处加第三个断点。

- **60rem 以下：** 多列网格变单列，倾斜与裁切效果去掉，吸底/吸顶面板取消吸附，每种 hero 姿态都收缩到内容高度（Poster 可以保持 full-bleed）。
- **40rem 以下：** 展示字号下调，边距题注移入正文，注释合并。

## 流式与离散

连续变化的尺寸用 `clamp()`（刻度里的展示 token 已经如此）；离散变化的布局用媒体查询。能力检测用 `@media (hover: hover)` 与 `(pointer: coarse)`，绝不用宽度：

```css
@media (hover: hover) { .link:hover { text-decoration-thickness: 2px; } }
@media (pointer: coarse) { .btn { min-height: 48px; } }
```

贴近拇指的 UI（meta、导航链接、控件）在手机上放大，60rem 处收紧（`craft.md` § 9）。

## 可点击文字绝不换行

按钮、主导航链接与 CTA 在 320 到 1920 的每个宽度都是单行（49a）；页脚链接、标签页与面包屑同样如此，除非某个真实短语无法缩短（49b）。当出现换行时，按此顺序处理：

1. **缩短标签。** *Get started free* 改为 *Start free*；*Read the documentation* 改为 *Read the docs*。
2. **在控件上加 `white-space: nowrap`**，让它周围的行自行重排。
3. **折叠那一行**，而不是折叠标签：60rem 以下放不下的链接收进菜单，放得下的两三个短的留在栏内。

## 单位与安全区

- 高度会碰到移动端浏览器 chrome 时用 `dvh` 或 `svh`，hero 上绝不用 `vh`（6a）；宽度用 `width: 100%`，绝不用 `100vw`（34）。
- 使用 `viewport-fit=cover` 时，把安全区折进 gutter token：`--gutter: max(16px, env(safe-area-inset-left))`。

## 表格、图片、语言

- **表格**在手机上把命名行的列与操作行的列保持可见：每行重排为带标签的块，或固定第一列（`craft.md` § 9, F25）。手机上放十列是重设计，不是挤一挤。
- **图片：** `srcset` 配宽度描述符，不同裁切用 `<picture>`，每张图片都带 `width` 与 `height` 属性，首屏之下用 `loading="lazy"` 且 LCP 元素上绝不用。
- **语言：** 逻辑属性（`margin-inline-start`、`padding-block`），为字符串长 30%–40% 留出空间，不硬编码日期或数字格式。

绝不：用设备嗅探代替特性查询、只有 hover 的交互、以 `px` 写断点。
