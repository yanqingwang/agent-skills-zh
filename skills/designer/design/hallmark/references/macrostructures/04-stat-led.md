> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/04-stat-led.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 04 · Stat-Led

hero 是用户给的一个数字，配上说明它意义的那句话。之后的一切都在支撑或限定它。数据就是叙事。

- **标题：** 图形尺度的大数字展示（`craft.md` § 7，等宽数字），配一条有文字的标题。数字是最大的元素，但绝不是 hero 的全部文字：在它旁边或下方用一条真正的标题说出它的意义，不是一个小标签。两者合读：*"Four seconds. From the alert link to the slow span."*（四秒钟。从告警链接到慢 span。）
- **正文：** 各小节都以一个支撑数字或图表锚定。
- **分隔：** 数字块之间发丝线；`tabular-nums` 处处使用。
- **按钮：** 限定句之下的一枚描边 chip，标签是动词（"Read the report"，读这份报告）。
- **图像：** 图表与数据可视化按 [`../data-viz.md`](../data-viz.md)；产品照片只在用户要求的槽位里。
- **Reveal：** hero 数字上做数字跳动，用 `--dur-long` 从 0 数到目标值，正当性只在于数字是真的；标记里保留最终数字，所以脚本关闭与减少动效时照样可读（62）。

提示词说"我们有数字为证"时选它：企业与 B2B、融资、气候与影响力页面。

用户没给数字时避免使用。本页每个数字都是用户的，带上它的单位与来源（46a）；没有文字句的光秃数字过不了 46b。编造的大数字比没有数字更糟。

构图：支撑行用 Figures，限定句用 Rows（`layout.md` § 5）。

**样例开篇句**（数字是用户的；模仿文字如何补全它）：
> *"Four seconds. From the alert link to the slow span."*（四秒钟。从告警链接到慢 span。）先给数字，再说它换来了什么（Tracejam）。
> *"[the user's count] posts. New CSS you could use today."*（[the user's count] 篇帖子。今天就能用上的新 CSS。）一个计数把页面锚在真实体量上。
> *"[the user's rate] faster, so the team can decide late."*（快 [the user's rate]，团队因此可以晚点做决定。）一个倍率，然后是它带来的行为。
