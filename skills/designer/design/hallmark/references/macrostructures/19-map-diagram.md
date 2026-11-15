> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/19-map-diagram.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 19 · Map / Diagram

一张大空间图组织整个页面：流程图、平面图、网络图、系统图。信息按空间排布，不是线性。

- **标题：** 小节字号下的定向标题，放在地图上方或旁边；地图承载页面。
- **正文：** 地图本身，节点与边，带一份图例。
- **分隔：** 内部不用；整张图是一个构图。
- **按钮：** 链接放进节点里；页面的那一个动作与定向语放在一起，在首屏内（44b），绝不在地图下方。
- **图像：** 地图就是图像：从真实地点或真实系统绘出的 SVG，带 hover 状态，加标签，或设 `aria-hidden` 并用一份承载每条事实的文字图例（33）。本来就是几何的东西是一等媒介（47c）。
- **Reveal：** 地图进入视口时逐节点落墨，至多五个节点，只做一次。

系统总览、生态图、流程图、组织架构图选它。

不要当作叙事的替代品。有些故事不该按空间读。

移动端：60rem 以下时，地图在容器内横向滚动，或收拢为节点的有序列表。

**样例开篇句**（点名路径或地界）：
> *"Browser, then API, then database. Tracejam sits between the last two."*（浏览器，然后 API，然后数据库。Tracejam 坐在后两者之间。）点名各层与位置。
> *"From stdin, through the pipe, into your dashboard."*（从 stdin，穿过管道，进你的仪表盘。）给下方画出的流贴上标签。
> *"Three tiers across two regions, one ledger."*（两个区域三层，一本账。）对系统计数，地理与结构兼有。
