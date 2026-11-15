> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/interaction-and-states.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 交互与状态

为表单与有状态控件加载。`craft.md` § 9 与 gate 39a 管输入规则，§ 2 管对比度；本文件管八状态表、字段配方与覆盖层模式。

## 八个状态

| 状态 | 时机 | 处理 |
| --- | --- | --- |
| 默认 | 静止时 | 基础样式 |
| 悬停 | 指针悬于其上，在 `@media (hover: hover)` 内 | 一个信号：色阶、1px 抬升或边框变化（11） |
| 聚焦 | 键盘或程序化聚焦 | 焦点环，立即出现（15, 26a） |
| 按下 | 按压期间 | 下沉 1px 或加深一档 |
| 禁用 | 不可交互 | 三通道齐用：`opacity: 0.55`、`cursor: not-allowed` 与原生 `disabled` 属性；控件必须保持可聚焦时用 `aria-disabled="true"`（39a） |
| 加载 | 处理中 | 行内进度；标签保持可读，宽度不跳动 |
| 错误 | 失败 | 边框与报错信息用 `--color-error`，加 `aria-invalid`；绝不只用颜色 |
| 成功 | 完成 | 成功就是结果本身，来自服务端的应答；至多加一个页面图标集内的图标；不用 toast（16）；没有发起请求就没有成功态（70） |

缺任何一个状态，元素就不算完成。

## 焦点环

脚手架的环就是页面的环：`outline: 2px solid var(--color-focus); outline-offset: 2px`，输入框上用内缩（负 offset），绝不与相邻字段相撞。对元素与页面都保持 3:1。用 `:focus-visible`，只对键盘出现；绝不在无替代的情况下 `outline: none`。

## 点击区域

手指能碰到的东西一律 44 x 44 CSS px。不改外观地扩大小控件：

```css
.icon-btn { position: relative; }
.icon-btn::before { content: ""; position: absolute; inset: -12px; }
```

## 表单

- 每个字段上方有可见标签；绝不用占位符当标签。
- 占位符展示格式（`01 Jan 2026`），绝不写指令。
- 字段被碰过之后失焦时校验一次，之后每次输入都校验。
- 错误信息说清坏了什么、为什么、怎么办，能一句说完就一句；用 `aria-describedby` 绑定到字段并设置 `aria-invalid="true"`。
- 必填字段带 `aria-required` 与一个可见标记，绝不只用颜色。
- 只在请求进行中禁用提交，静止时绝不禁用。

## 字段

一切文本输入框、textarea、select 与 combobox。

**边框宽度绝不变。**状态变化落到 `background-color`、`border-color`、`outline` 或 `box-shadow`，绝不动 `border-width`；静止时预留一个透明 outline，环出现时不位移。

```css
.input { border: 1px solid var(--color-muted); outline: 2px solid transparent; outline-offset: -3px; }
.input:focus-visible { outline-color: var(--color-focus); }
```

| 状态 | 处理 |
| --- | --- |
| 默认 | 1px `--color-muted` 边框（字段边缘需要 3:1，发丝线永远达不到），纸色背景，占位符用 `--color-muted` |
| 悬停 | 背景变 `--color-paper-2`，边框不变 |
| 聚焦 | 焦点环；边框可在同宽度下加深到 `--color-ink-2` |
| 已填写 | 同默认；状态由值本身承载 |
| 禁用 | 三通道；占位符再暗一档 |
| 错误 | `--color-error` 边框，错误文本进辅助行，右缘槽放页面图标集内的错误图标 |
| 成功 | 只在真实校验返回后出现；页面图标集内的对勾图标；用户编辑即清除 |
| 加载 | 右缘槽放一个小 spinner；字段保持可编辑，提交等待 |

- **高度：**输入框与旁边按钮等高（营销页 44 到 52px，39）；竖向 padding 为 `(height - line-height) / 2`。
- **右缘槽：**预留约 24px 给清除按钮、错误字形或 spinner，出现时不引起重排。
- **标签**在上方 4 到 8px；**辅助说明**在下方约 4px，用标签字号、更安静，所在行预留 `min-height: 1lh`（F14）；错误替换该行内的辅助说明，绝不另起第二行。
- 绝不对 `border-width`、`padding` 或 `height` 做过渡；绝不让焦点环做动画。

**控件。**Textarea：`resize: vertical`、`min-height: 6rem`。Select：用原生，包装器上放自定义箭头；只在保持原生键盘与屏幕阅读器行为时才做完全自定义的 select。Checkbox 与 radio：用原生，廉价而正确的版本用 `accent-color`，在 CSS 中按状态设置样式，绝不用脚本切换。开关（switch）就是遵守同一契约的 checkbox。Range：滑块可聚焦并有 44px 点击区域。File input：样式化 `<label>` 作为表面。Combobox：listbox 悬在下方不推挤内容，`aria-expanded` 如实反映，方向键循环，Enter 选中，Escape 关闭。

## 模态与覆盖层

- 用 `showModal()` 打开原生 `<dialog>`：焦点陷阱、Escape 与 `::backdrop` 白送。
- 加了自定义定位就要钉住它，否则可能缩到角落：`position: fixed; inset: 0; margin: auto; height: fit-content; max-height: min(80dvh, 40rem)`。非 dialog 覆盖层在 fixed 容器上用 `display: grid; place-items: center` 居中。
- 背后的页面加 `inert`；Escape、点击遮罩与可见的关闭控件都能关闭；首个焦点给第一个可交互元素。

## 弹层、菜单与工具提示

轻关闭、堆叠与 Escape 用 Popover API；可用处用 CSS anchor positioning，否则用 `position: fixed` 配 `getBoundingClientRect()`；靠近视口边缘时翻转；绝不放进会裁切它的 `overflow: hidden` 祖先里。

## 撤销优先于确认

可逆动作立即执行，并提供 5 到 10 秒的撤销。不可逆动作（删除账号、drop 表）保留确认，并让用户输入被销毁对象的名字。

## 加载与空态

- 内容形状已知处（列表、卡片、表格）用骨架屏；spinner 只出现在按钮里，替换标签。
- 空态是一行说明什么为空、一行说明为什么重要、一个动作（`craft.md` § 6）。绝不是一句光秃秃的 *No results*。
- 用户视线附近的禁用控件要说明为何禁用。
