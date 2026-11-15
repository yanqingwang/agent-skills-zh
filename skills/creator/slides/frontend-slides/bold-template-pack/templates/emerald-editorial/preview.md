> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/emerald-editorial/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Emerald Editorial 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/emerald-editorial/design.md`
- 预览卡：`bold-template-pack/templates/emerald-editorial/preview.md`

## 选型元数据

- Slug：`emerald-editorial`
- Tagline：一套杂志封面式商业演示：翠绿 + 海军蓝 + 纸色，双线报头装饰，配大胆的 Bodoni 风展示衬线。
- Mood：editorial、considered、confident、magazine-cover
- Tone：literary、authoritative、warm、designed
- Formality：medium-high
- Density：medium
- Scheme：mixed
- 适合：一切应当像严肃杂志封面的内容，包括但不限于管理层汇报、计划办评审与战略简报。双线报头装饰赋予其编辑式的庄重而不显僵硬：用于产品发布或想要用心感而非企业感的研究回顾，也是出人意料的佳选。
- 避免：需要读起来安静、中性或机构式克制的场景：翠绿色场饱和度太高，无法隐入背景。

## 视觉速览

一套大胆的展示衬线编辑系统，语域接近时尚报头或复古杂志封面。Bodoni Moda 以字重 900 跑遍宽广的字号区间（44–460px），铺在高饱和的翠绿画布上，配深海军蓝油墨与燕麦纸点缀。招牌处理是一组堆叠双线装饰，像 19 世纪戏剧场刊那样框住居中的展示词。美学借鉴 Harper's Bazaar / Vogue / Wallpaper 封面：自信、戏剧化、忠于纸与墨，配色紧缩为三色，渐变与阴影为零。

Emerald Editorial 是一套大胆的展示衬线编辑系统，根植于时尚杂志与 19 世纪戏剧场刊的视觉语言。奠基性前提是单一字体：Bodoni Moda 字重 900，以毫不掩饰的字号使用：常规标题 92px，宣言与分节开场 130–200px，主视觉数字 460px。这种衬线响亮、戏剧化而自信。每页幻灯片以文字开场，而不是以图片。

## 预览要素

- Palette：bg #3CD896; bg-2 #2DC684; bg-3 #25B377; ink #0F1A5C; ink-2 #1B2774; ink-3 #3A4593; paper #F1E9D6
- Typography：完整设计文档在选定后阅读。
- Signature move：所有展示时刻用 Bodoni Moda 字重 900；所有正文与标签时刻用 Manrope 字重 500/700/800。
- Signature move：高饱和翠绿画布（{colors.bg}）配深海军蓝油墨（{colors.ink}）文字与反色面板。
- Signature move：双线装饰包住居中衬线词，是招牌装饰手法。
- Signature move：4px 墨色横线分隔每个堆叠分节、每个列表行、每个图表边框。4px 粗细是系统的默认横线。
- Signature move：任何地方都没有圆角。除 logo/字体字形本身为圆外，每个形状都是严格矩形。

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
