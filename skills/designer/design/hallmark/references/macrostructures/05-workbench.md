> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/05-workbench.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 05 · Workbench

真实产品截图是主要内容。页面是对使用中应用的一次导览，短说明字幕代替营销文案。

- **标题：** 小节字号下朴素而功能化；截图自己说话。
- **正文：** 一串截图块，每块一个 `<figure>`，其 `<figcaption>` 陈述一个事实外加一条行内注释。
- **分隔：** 截图就是分隔；小节靠间距与截图分开。
- **按钮：** hero 的那一个动作（44b）；主题允许吸顶元素时，第三张截图之后用一条底栏承载它，标签是动词（"Start a project"，开始一个项目）。
- **图像：** 真实截图，不加框，放在 `<figure>` 里；用户未提供时，用 `data-slot` 里建出来的产品（`imagery.md` § 4）。不要浏览器或设备镶边（47a、47b）。
- **Reveal：** 一次文字揭幕，用在第一条字幕上；截图即刻加载，其余的就那么摆着。

SaaS、开发者工具、编辑器扩展，任何"看到产品被使用"就是卖点的地方选它。

产品是概念型或服务主导时避免使用。Workbench 需要一个 UI 可展示。

构图：截图用 Showcase 与 Split，收尾用 Band（`layout.md` § 5）；可选的那条栏是 `--z-sticky` 层级上带一个动作的吸顶底栏。

**样例开篇句**（模仿其具体性；页面带访客走一遍）：
> *"$ streampipe parse access.log --filter status=5xx | jq"* 以一条真实命令开场，不是一句声明。
> *"Read anything that emits lines: files, pipes, sockets, kubectl logs."*（读任何会吐出行的东西：文件、管道、socket、kubectl 日志。）点名输入，拒绝抽象。
> *"Open the trace, find the span, fix the regression."*（打开追踪，找到 span，修掉回归。）三个具体动词。
