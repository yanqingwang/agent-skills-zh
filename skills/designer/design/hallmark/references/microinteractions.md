> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/microinteractions.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 微交互

当页面带有有状态的 UI 时加载。`craft.md` § 5 管时长、三款缓动与禁用项；`gates.md` 管破绽（tells）（10, 11, 12, 15, 16, 17, 18, 26, 27, 62）；主题的 Motion 章节决定多大程度上可以动。本文件管配方，且不复述上面任何一条。

## 原则

- **动效必须有职责，否则砍掉。** 每个动画都要澄清、引导或确认。问一句：如果它是瞬时的会损失什么；若答案是什么都不损失，就删掉它。
- **成功保持安静。** 用户看得见结果时，不弹 toast。toast 留给失败与页面无法展示的效果。
- **乐观更新，可回滚。** 立即更新界面，请求在背后发送，失败时回滚并提供重试入口。
- **Reduced motion 是一种状态，不是事后补丁。** 下文每个配方都写了它：空间性运动收缩为 150ms 的 opacity 交叉淡变，功能性状态照常变化。
- **键盘优先。** 每个 hover 交互都有 focus 等价物；不存在只有 hover 才能触达的东西。
- **每页至多三个原语**（一个展开、一个 hover 信号、一个功能循环如跑马灯或计数器，三者即满）。性格为 still 的主题一个都不用，功能性状态变化除外。

## 配方

时长为 `--dur-micro` 120ms、`--dur-short` 220ms、`--dur-long` 420ms；进入用 `--ease-out`，退出用 `--ease-in`（取进入时长的 60%–75%），开关切换用 `--ease-in-out`。弹簧只在俏皮主题声明了 spring posture 时出现，且只用于主控件和一处性格时刻（12）。

**按钮按压。** hover 是一个信号，颜色变化；按压下沉 1px，松开即回。焦点环永不动画。

```css
.btn { transition: background-color var(--dur-short) var(--ease-out), transform var(--dur-micro) var(--ease-out); }
.btn:hover { background: var(--color-paper-3); }
.btn:active { transform: translateY(1px); }
```

**输入框聚焦。** 轮廓立即出现，输入框内缩；边框可以加深一档，但宽度永不变化（39a）。label 静止时位于字段上方且永不移动：浮动 label 生来就是个 placeholder，这正是破绽。

**校验。** 字段被触碰后首次 blur 时校验一次，之后每次输入都校验；绝不在第一次按键时校验。辅助行在同一保留行（F14）中切换为错误信息：什么坏了、为什么、该怎么做。字段上加 `aria-invalid` 与 `aria-describedby`。

**Toast。** 只用于失败与不可见效果（16）。固定一个角落，新的把旧的同方向推，其余一律不重排。进入用 `--dur-long`，停留 4–6s，以 65% 时长退出；hover 和 focus 时自动消失暂停；错误 toast 带一个重试动作且不会自行消失。

**模态框。** 用 `showModal()` 打开的 `<dialog>`，页面其余部分加 `inert`。背景淡入，面板在 `--dur-long` `--ease-out` 下从 0.96 缩放到 1；关闭约取 65% 时长并用 `--ease-in`。初始焦点给第一个可交互元素，不给关闭按钮。Reduced motion：150ms 交叉淡变。

**菜单。** 用 Popover API（免费获得轻量关闭、Escape 与层叠），CSS 锚点定位在离边缘 16px 内自动翻转。打开用 `--dur-short` `--ease-out`，关闭取 65% 用 `--ease-in`；条目不超过八项时可以 30ms 交错。

**工具提示（Tooltip）。** hover 延迟 800–1000ms，focus 延迟 0（17）；opacity 用 `--dur-micro`。指针移到它上面时保持显示，Escape 时消失（WCAG 1.4.13）。

**标签页切换。** 指示条用 `transform` 移动（x 轴上的位移与缩放，绝不动 `width`），时长 `--dur-short`；离开的面板以 `--dur-micro` 淡出，进入的随后淡入。高度变化的面板用 `grid-template-rows: 0fr` 到 `1fr` 动画，绝不用 `height`。

**数字滚动。** 只用于真实数值（46a）。数据加载时，从上一个值（首次加载从零）开始，在 400–800ms 内数到新值，缓动 `--ease-out` 作用于数值本身，用 `Intl.NumberFormat` 格式化。只播报最终值（`aria-live="polite"`）。Reduced motion：直接给出最终值。

**复制到剪贴板。** label 切换为 *Copied* 持续 2.5s；不弹 toast，label 本身就是反馈。

```js
btn.addEventListener("click", async () => {
  await navigator.clipboard.writeText(value);
  btn.dataset.state = "copied";
  setTimeout(() => delete btn.dataset.state, 2500);
});
```

**拖拽排序。** 拖柄在 hover 和 focus 时出现；光标先 `grab` 后 `grabbing`；50% 透明度的幽灵跟随指针，1px 强调线标记落点。松手后以 `--dur-short` `--ease-out` 吸附归位，不用弹簧。方向键可对聚焦行重排；`aria-live` 播报移动。

**乐观更新。** 行立即变化，请求在背后运行。成功时一言不发。失败时该行以 `--dur-short` 回滚，并弹出带 *Try again* 的 toast，直到被处理才消失。

```js
const prev = item.done;
item.done = !prev; render();
try { await api.update(item); }
catch { item.done = prev; render(); toast({ tone: "error", message: "Could not save.", action: { label: "Try again", run: retry } }); }
```

**边输入边搜索。** 防抖 250ms；等待期间给字段一个安静的信号（边框加深一档）。命中项用 `<mark>`。防抖稳定后播报一次结果数，绝不逐键播报。

**命令面板。** ⌘K 或 `/` 立即打开；输入框全程保持焦点。方向键移动高亮，高亮以 `transform` 在 `--dur-micro` 内滑动；行本身永不移动。Enter 选择，Escape 关闭。首次打开时行可淡入，过滤时绝不淡入。

**页面加载展开。** 只编排一次入场，遵循 `craft.md` § 5：按 DOM 顺序交错，总计 0.4–0.8s，用 IntersectionObserver 而不是 scroll 监听，只播一次。静的主题跳过它，这是正确的做法。

## 动效性格

每个系统都要声明一种：目录主题写在自己的 Motion 章节，定制页面写在自己的样式表。同一个按压，在严厉的系统里比在平和的系统里更响。

| 性格 | 时长倍率 | 感觉像 |
| --- | --- | --- |
| **still** | 无 | 印刷品。一切不动；输入命令时光标可以闪烁，四五拍后转为实线，绝不自行闪烁。 |
| **severe** | 0.7–0.75 倍 | 快而果断；一步到位；处处不用弹簧。 |
| **brisk** | 0.85–0.9 倍 | 技术感与功能性：一块仪表盘。 |
| **calm** | 1.0–1.3 倍 | 从克制到宽裕，`--ease-out` 取其最柔和的一端。 |

多数页面的动效是太多，不是太少。静态答案通常就是正确答案。
