> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/vellum/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Vellum 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/vellum/design.md`
- 预览卡：`bold-template-pack/templates/vellum/preview.md`

## 选型元数据

- Slug：`vellum`
- Tagline：深海军蓝画布配暖黄 Cormorant 衬线与单一灰青点缀色。安静的书卷气美学。
- Mood：scholarly、literary、considered、quiet、intellectual
- Tone：literary、considered、patient、intelligent
- Formality：high
- Density：low
- Scheme：dark
- 适合：一切应当显得学术、文学且安静睿智的内容：研究综合、白皮书、学术与政策简报、咨询交付物、长篇编辑文章、创始人随笔。对任何想要沉静用心氛围而非高能视觉的演示文稿（包括科技、商业或创作者作品）同样是强选择。
- 避免：需要视觉热度或波普感的场景：海军蓝 + 暖黄 Cormorant 美学刻意低速运转。

## 视觉速览

一套"随笔钉在墙上"的演示系统：单一单色色场，深长春花蓝（#2A3870），暖黄绿文字（#E8D85C）居中浮在其上，每页如此。斜体 Cormorant Garamond 以所有字号承担每个标题：斜体衬线就是个性，衬在大胆的色场之上。DM Sans 以安静的配角身份处理正文。Courier Prime 等宽提供打字批注的声音：作为"图钉便签"署名坐在每页幻灯片的左下角。情绪是画廊展墙遇上档案夹：安静、单色、深度静置。一种颜色、两款温暖字体、零动效。

Vellum 是一套单色的"墙上随笔"演示系统。视觉前提既严苛又温柔：每页幻灯片都是同一片深长春花蓝海军蓝色场（{colors.navy}，#2A3870），暖黄绿文字（{colors.yellow}，#E8D85C）居中浮在其上。没有备选表面。没有明/暗主题。没有第二种背景色。色场是常量；文字与左下角的一枚小批注是其余的一切。

## 预览要素

- Palette：navy #2A3870; navy-alt #343F80; navy-deep #1F2858; navy-mid #34407A; yellow #E8D85C; emphasis-yellow #F5E168; teal #3A7878
- Typography：Cormorant Garamond; DM Sans; Courier Prime; {typography.label.fontFamily}
- Signature move：单一单色色场：{colors.navy}（深长春花蓝），每页如此。没有亮色主题，没有反色。
- Signature move：斜体 Cormorant Garamond 字重 400 用于每个标题、每个数字、每个特写衬线时刻。
- Signature move：正文与导语段落用 DM Sans；装饰标签与图钉便签署名用 Courier Prime 等宽。
- Signature move：黄色文字（{colors.yellow}）是主色；更亮的 {colors.emphasis-yellow} 是标题内唯一的 <em> 颜色。
- Signature move：灰青（{colors.teal}）是第二点缀色：只用于大引号字形、图钉便签文字、眉题、28px 横线与列表计数标记。

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
