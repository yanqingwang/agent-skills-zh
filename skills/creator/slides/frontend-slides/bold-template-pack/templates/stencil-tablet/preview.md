> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/stencil-tablet/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Stencil & Tablet 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/stencil-tablet/design.md`
- 预览卡：`bold-template-pack/templates/stencil-tablet/preview.md`

## 选型元数据

- Slug：`stencil-tablet`
- Tagline：骨白纸张配镂空刻板标题与六色大地色配色：考古遇上品牌。
- Mood：archival、earthy、tactile、considered、graphic
- Tone：weighty、considered、tactile、literary
- Formality：medium-high
- Density：medium
- Scheme：light
- 适合：一切应当显得档案感、有触感且厚重图形化的内容：博物馆与文化机构演示、艺术/建筑品牌、长篇研究、遗产与手作品牌、宣言。任何时候都是佳选（科技与商业领域亦然）：只要你想让演示读起来像一本野外手册，而不是幻灯片。
- 避免：要求数字原生光鲜或俏皮波普的场景：镂空刻板展示字体与大地色配色押注于刻意的模拟质感。

## 视觉速览

一套西海岸滑板海报遇上市政刻板告示的系统。Stardos Stencil 以其特有的断墨缺口承担每个标题、每个数字与每个厚重的展示时刻；Barlow Condensed 以特重字重跑遍所有元数据与大写界面装饰；Inter 处理正文。配色是骨白（#E2DCC9）与黑，由一组高饱和复古印刷点缀色激活：赭石、洋红、橙、青绿、蓝、芥末、橄榄。柔和圆角的"石板"卡片（22–26px 圆角）以彩色块在幻灯片间平铺。文字巨大且大写，数字以 160–540px 主宰画面，色块充当版式。情绪同时是工业海报、复古工坊招牌与音乐节阵容表。

Stencil & Tablet 是一套海报音量、文字主导的演示系统。前提是单一展示字体：Stardos Stencil，处理每个标题、每个数字、每个特写时刻，其特有的刻板断墨给每个字形带上轻微磨损的工业语域。配角阵容是 Barlow Condensed（特重 600–900、大写、宽字距），跑遍所有元数据、界面装饰、胶囊与图例：Inter 则处理少数几段正文，它们存在的意义多半是为上方响亮的文字加注。

## 预览要素

- Palette：bone #E2DCC9; black #000000; ink #0A0A0A; paper #F4EFE0; sienna #A06A3C; magenta #C73B7A; orange #EE7A2E; teal #2D7E73
- Typography：Stardos Stencil; Bowlby One; Barlow Condensed; Inter
- Signature move：多数幻灯片用骨白（{colors.bone}）色场；议程式与加粗分隔幻灯片用黑色场配骨白文字。
- Signature move：Stardos Stencil 用于每个标题、每个数字、每个特写刻板时刻：断墨刻板字形就是系统的身份标识。
- Signature move：Barlow Condensed 特重大写用于所有界面装饰、元数据、胶囊、图例与标签。字距慷慨（0.06–0.14em）。
- Signature move：Inter 用于正文：戏份很小，支撑上方响亮的文字。
- Signature move：七色点缀配色（{colors.sienna}、{colors.magenta}、{colors.orange}、{colors.teal}、{colors.blue}、{colors.mustard}、{colors.olive}）外加纸张色（{colors.paper}）：用作整卡填充。

## 国际化 / CJK 预览注意

- 若预览使用中文或其他 CJK 文本，请保持 CJK 字距为 0、放宽行高，并避免对 CJK 文本应用大写变换。
- 选定后请使用完整 `design.md` 的 CJK 章节，获取确切的字体搭配与各文字系统专属调整。

## 预览规则

- 在固定舞台模型内精确构建一页 1920x1080 的标题页。
- 保留上述的配色、字体角色、表面节奏与装饰语汇。
- 使用用户的真实标题/副标题/语境信息；不要复制演示示例内容。
- 渲染出的预览必须看起来像真实的第一页，而不是模板选型卡。
- 永远不要在页面上放置内部工作流文字：不得出现 `preview`、`generated from`、`preview.md`、`template`、`preset`、`style option`、`Option A/B/C`、文件名、路径或来源文档标签。
- 永远不要把模板名称或 slug 放到页面本身；只在聊天消息中提及。
- 永远不要在页面上放置用户需求备注（如期望的气质、受众、内部使用标签），除非用户明确要求这些字面词出现在演示中。
- 可见边框装饰只使用真实演示内容：演示标题、真实的分节标题、日期、作者、公司、页码，或来自用户材料的真实内容短语。
- 生成预览时不要读取 `template.html`。
- 不要读取其他模板的 `design.md` 文件。
- 在用户为完整演示选定本模板后，先阅读完整设计文档再生成最终幻灯片。
