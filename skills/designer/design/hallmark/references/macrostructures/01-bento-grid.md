> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/01-bento-grid.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 01 · Bento Grid

大小不一的模块块铺成不规则网格。每块是一个功能、一个用户给的数字、一张图或一条用户提供的引言。节奏来自尺寸变化，不是卡片均质。

- **标题：** 网格第一行之上的展示标题；hero 就一屏，网格在 hero 内部或其正下方开始（44c），绝不出一整条高高的空带。
- **正文：** 不对称网格，六到九个混合跨度的块（1×1、2×1、1×2、2×2）；带图像的轨道用 `minmax(0, 1fr)`（50）。
- **分隔：** 一条缝隙 `--gap-columns`；不用线；网格就是节奏。
- **按钮：** hero 里一枚描边 chip；块内是带动词的字排链接。
- **图像：** 紧裁在各块内部；绝不满幅出血。
- **Reveal：** 不用，或网格进入时一次性的淡入。

提示词是"许多小东西要展示"时选它：功能页、SaaS 落地页，访客有几个同等有效入口的任何地方。放数字或引言的块只在用户提供了它们时才存在（46a）。

信息是一个 hero 想法时避免使用。Bento 分散注意力；单一想法的页面要 Marquee 或 Stat-Led。

构图：Bento 与 Grid（`layout.md` § 5）。

**样例开篇句**（模仿其具体性，不照搬措辞）：
> *"Distributed tracing that explains itself."*（自己会解释自己的分布式追踪。）五个词说出品类与承诺（Tracejam）。
> *"An API for sending mail from code."*（一个从代码里发邮件的 API。）点出产品类别与读者。
> *"Everything a small kitchen needs to sell online."*（一家小厨房在网上卖货需要的一切。）点出规模与任务。
