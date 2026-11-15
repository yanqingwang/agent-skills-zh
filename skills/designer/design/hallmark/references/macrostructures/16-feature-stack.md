> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/16-feature-stack.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 16 · Feature Stack

吸顶的左侧面板持有标题，右侧面板与滚动同步，轮播相关截图。节奏像电影。

- **标题：** 收在吸顶面板内；内容在旁边轮换时持续在场。
- **正文：** 两栏，左吸顶，右滚动；右侧面板在每个小节播放 3 到 6 张细节截图。
- **分隔：** 小节条带；吸顶面板每小节重新锚定，在吸顶导航之下位于 `top: var(--banner-height)`（56）。
- **按钮：** 在吸顶面板里，到达该小节最后一张截图后出现；脚本关闭时它就在那里（62）。
- **图像：** 滚动栏是真实截图，或截图到位之前槽位里建出来的产品（`imagery.md` § 4）；绝不是一排空框（68）。
- **Reveal：** 不用淡入类；吸顶滚动本身就是动效。用 [`../scroll-choreography.md`](../scroll-choreography.md) § 4 Sticky diptych 编排，面板保持在左侧；或 § 1 Pinned chapter：每页一种模式。

高端产品、复杂的功能故事、任何需要在访客滚动时控制节奏的地方选它。

移动优先的受众没有强回退时避免使用。吸顶滚动同步在小屏幕上很粗糙。

构图：钉住的 Split（`layout.md` § 5），钉法按 `scroll-choreography.md` § 4。

移动端：60rem 以下时，吸顶面板变成其截图之上的标题，按文档流堆叠。

**样例开篇句**（钉住一句陈述，然后带访客走一遍）：
> *"Plan, build, ship."*（计划、构建、上线。）三个动词，三块吸顶面板。
> *"Read anything that emits lines."*（读任何会吐出行的东西。）先点名什么可以做，然后带着走一遍（Streampipe）。
> *"From stdin, through the pipe, into your dashboard."*（从 stdin，穿过管道，进你的仪表盘。）点出数据路径，然后逐步解释。
