> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/14-narrative-workflow.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 14 · Narrative Workflow

编号的阶段讲出用户随时间使用产品的故事。每一节是一个阶段；页面是一条流程时间线。

- **标题：** 阶段编号骑在标题内部（`<h2>1.0 Intake</h2>`），或由 `<ol>` 配 `counter()` 生成。绝不另立标签放在标题旁：那是阶段字号下的 eyebrow（54）。
- **正文：** 每个阶段有一段短解释和一个全尺寸对象：用户给了屏幕截图时放一张 360px 高以上的产品截图，否则放提示词里的数字或行（一个计时器、一个计数、该阶段造出的东西）。三个阶段拿同类对象读起来就是三个功能（8）：对象要逐阶段变化。
- **分隔：** 阶段之间一道线，用主题的线宽；编号留在标题里，绝不上线。
- **按钮：** hero 的那一个动作（44b），在页脚回访一次（"Start at stage one"，从第一阶段开始）；阶段内部放链接。
- **图像：** 每阶段一张真实截图，常带注释，放在 `<figure>` 或槽位里；只有一张或没有屏幕图时，绝不每阶段一个槽位（68）。
- **Reveal：** 主题允许 reveal 时，在第一个阶段上做一次横向扫入；后面的阶段就那么摆着。与滑杆联动的阶段序列可改用 [`../scroll-choreography.md`](../scroll-choreography.md) § 1 Pinned chapter：每页一种模式。

有明确工作流的产品选它：项目管理、设计到开发的流水线、写作工具。

在单一时刻完成工作的工具避免使用。Narrative Workflow 需要真实的序列。

构图：Steps，每阶段配其截图（`layout.md` § 5）。

**样例开篇句**（阶段标题：编号、宣告式、流程语言、每行一个阶段）：
> *"1. Sourdough overnight. 2. Score at dawn. 3. Pull at seven."*（1. 酸面团过夜。2. 黎明割包。3. 七点出炉。）三个编号阶段，没有营销（Maple Street Bread）。
> *"1.0 Parse. 2.0 Filter. 3.0 Route."*（1.0 解析。2.0 过滤。3.0 路由。）版本式编号，三个具体动词（Streampipe）。
> *"I. We design products that last twelve years. II. A material is sustainable when someone can repair it."*（I. 我们设计能用十二年的产品。II. 一种材料能被修复，才算可持续。）罗马数字与宣告句（Meridian）。
