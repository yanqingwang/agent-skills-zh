> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/signal/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Signal 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/signal/design.md`
- 预览卡：`bold-template-pack/templates/signal/preview.md`

## 选型元数据

- Slug：`signal`
- Tagline：深海军蓝画布配骨白纸张与单一哑金点缀色；机构气质，分量沉静。
- Mood：institutional、trustworthy、considered、weighty
- Tone：sober、polished、established、literary
- Formality：high
- Density：high
- Scheme：mixed
- 适合：一切应当显得有分量、用心且机构可信的内容：投资人演示、董事会汇报、咨询交付物、法律/政策简报、咨询提案。对想要安静权威而非喧哗的科技、研究或品牌工作同样是强选择。
- 避免：应当显得火热、快速或刻意俏皮的场景：海军蓝 + 金色的克制押注于沉稳语气。

## 视觉速览

一套文学编辑演示系统，气质来自长篇杂志：《经济学人》式的克制混合私人情报简报。Source Serif 4 承担每个标题，句中混排正体与古金色斜体；DM Sans 退居正文；IBM Plex Mono 跑遍所有时间戳、眉题与界面装饰。双表面系统是暖米白纸张（#F0ECE3）与深编辑海军蓝（#1C2644），由单一火热点缀色古金（#C8A870）串联，古金只用于横线、斜体强调与数字。一层近乎隐形的 80px 网格纹理盖在每页暗色幻灯片上，如指纹般存在。效果沉稳、用心，还有一点点贵族气。

Signal 是一套文学编辑演示系统：一篇长篇情报简报或严肃杂志的季度评审若以演示文稿运行，就会是这个样子。视觉前提是两种字体的联姻：一款深烘焙色的编辑衬线（Source Serif 4）承载声音，一款精密怪诞体（DM Sans）承载实体，一款压缩等宽字体（IBM Plex Mono）负责每个时间戳、眉题与界面装饰元数据。成品读起来像一种安静的权威：演示不需要喊叫，排印已经预告了严肃。

## 预览要素

- Palette：navy #1C2644; navy-alt #232F55; cream #F0ECE3; cream-alt #E6E0D4; text-warm #E2DCD0; text-muted-dark #8A96A8; text-hint-dark #4E5A6E; ink #1A2030
- Typography：Source Serif 4; DM Sans; IBM Plex Mono; {typography.label.fontFamily}
- Signature move：Source Serif 4 承担每个标题，句中混排正体/斜体；标题中的斜体永远是金色。
- Signature move：正文用 DM Sans；每个时间戳、眉题、标签与界面装饰元素用 IBM Plex Mono。
- Signature move：双表面：{colors.navy}（暗）与 {colors.cream}（亮）互换使用，同一页幻灯片内绝不混融，特殊分屏版式除外。
- Signature move：古金（{colors.gold}）是唯一点缀色。它标记横线、斜体强调与数字，别无他处。
- Signature move：{colors.border-dark} / {colors.border-light} 的发丝级 1px 边框分隔每个区域。没有卡片装饰，没有圆角面板。

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
