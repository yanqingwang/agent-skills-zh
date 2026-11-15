> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/peoples-platform/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# People's Platform (Block & Bold) 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/peoples-platform/design.md`
- 预览卡：`bold-template-pack/templates/peoples-platform/preview.md`

## 选型元数据

- Slug：`peoples-platform`
- Tagline：行动主义海报能量：米白底上的蓝、橙、红，配 Alfa Slab + Caveat Brush。
- Mood：activist、loud、graphic、honest
- Tone：punchy、direct、expressive、warm-bold
- Formality：medium-low
- Density：medium-high
- Scheme：light
- 适合：一切应当显得诚实、响亮且图形化的内容：文化评论、宣言、公民与社区演示、设计讲座、活动提案。特别适合创始人愿景时刻、使命宣言，或任何想要抗议海报能量而非企业光鲜感的演示文稿，各行各业皆可。
- 避免：机构式克制本身就是目标的场景：高饱和的政治海报配色全力押注于外放能量。

## 视觉速览

一套 WPA 海报遇上政治竞选的演示系统，建立在三种字体与五色配色（可归并为三个功能角色）之上。Alfa Slab One 是一种压缩粗衬线，以极端字号、纯大写承担全部重活。Caveat Brush 作为手写的人类插话空降进来：小写、略微旋转、情感温暖。DM Mono 以紧凑大写字距承担所有元数据。配色是电光钴蓝、琥珀橙与火热红：红色专门充当阴影/纵深色，绝不用作表面填充。每页幻灯片叠加纸张颗粒，让整套演示有丝网印刷的质感。美学响亮、自信、民粹：属于抗议标语牌、工会通讯或竞选大巴的那种视觉语言。

People's Platform 是一套 WPA 海报遇上政治竞选的幻灯片系统：信念的视觉语言，公共演讲的图形语域。画布是暖纸（{colors.paper}，#F5F2EA），比白纸暖一丝，每页幻灯片通过 CSS 伪元素叠加颗粒纹理，让整套演示像是丝网印出来而不是渲染出来的。

## 预览要素

- Palette：blue #2C2CDC; blue-deep #1B1BB0; orange #F2A03A; orange-deep #E89321; red #E83A2A; red-deep #B7281C; cream #F4E9D6; paper #F5F2EA
- Typography：Alfa Slab One; Caveat Brush; Archivo Narrow; DM Mono
- Signature move：纸张画布（{colors.paper}，#F5F2EA），每页幻灯片通过 CSS 伪元素叠加颗粒。
- Signature move：堆叠双重文字阴影：Npx Npx 0 {colors.red}，2Npx 2Npx 0 {colors.red-deep}。阴影尺寸随字号缩放。
- Signature move：所有展示与结构文字用 Alfa Slab One：大写、行高 0.82–1.04、字距 0.005em。
- Signature move：红色（{colors.red}）专门用作阴影色：绝不用作表面背景。
- Signature move：所有主要结构分隔用厚重的 6px 墨色边框（顶栏、分节标题、列分隔、内嵌边框）。

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
