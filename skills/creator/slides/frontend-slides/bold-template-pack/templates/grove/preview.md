> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/grove/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Grove 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/grove/design.md`
- 预览卡：`bold-template-pack/templates/grove/preview.md`

## 选型元数据

- Slug：`grove`
- Tagline：森林绿画布配米白文字、古典 Playfair 衬线与单一铁锈色点缀。
- Mood：organic、considered、warm、literary、natural
- Tone：classical、warm、considered、patient
- Formality：medium-high
- Density：medium
- Scheme：mixed
- 适合：一切应当显得自然、用心而成熟的内容：可持续与健康品牌、户外/自然产品、酒庄与餐厅、文学或艺术演示、咨询交付物、EN/CN 双语报告。对想要从容多于紧迫的科技、研究或商业演示而言，也是一个安静而独特的选择。
- 避免：需要霓虹能量或密集快节奏的演示文稿：森林绿画布与 Playfair 衬线押注于缓慢的古典语气。

## 视觉速览

一套安静的衬线编辑演示系统，语域接近装帧精良的专著或精品品牌手册。Playfair Display 字重 400（从不加粗）承担每个标题，以陶土珊瑚红斜体做强调是招牌动作。Jost 字重 300 以"好纸张"正文字体的身份承担每个段落。JetBrains Mono 字重 300 承担标签、眉题与纤细的界面装饰条。配色把深森林绿画布（#192b1b）与暖米白文字（#d4cfbf）配对，外加单一陶土珊瑚红点缀色（#c8524a）。慷慨的负空间、发丝级 1px 边框与近乎隐形的衬线水印数字，赋予它文学期刊式的沉静权威。

Grove 是一套安静的衬线编辑演示系统，语域接近文学专著或精品品牌手册。奠基性前提是克制：每页幻灯片承载一个聚焦的内容时刻，四周环绕深深的负空间，上下由纤细的 1px 界面装饰条锚定，并由一小组构图节拍支撑（珊瑚红眉题、36px 珊瑚红横线、斜体珊瑚红强调、破折号列表符、近乎隐形的水印数字）。

## 预览要素

- Palette：bg #192B1B; bg-alt #1E3221; bg-light #E8E4D6; bg-light-alt #DEDAD0; fg #D4CFBF; fg-light #192B1B; accent #C8524A
- Typography：完整设计文档在选定后阅读。
- Signature move：Playfair Display 字重 400 承担每个标题、每句引语、每个统计数字与每个水印数字。不允许粗体衬线：禁用粗体规则是本系统最重要的排印承诺。斜体 Playfair 以 {colors.accent} co...
- Signature move：Jost 字重 300 承担每段正文与列表。轻字重营造"好纸张"手感：它退居幕后，让衬线主导。
- Signature move：JetBrains Mono 字重 300 承担每个标签、眉题、页脚线、页码计数与统计图注。始终大写，字距至少 0.12em。
- Signature move：Noto Serif SC / Noto Sans SC 字重 300–500 作为所有角色的中文回退加载。整套演示文稿是双语感知的：内容中出现中文时，中文字符通过 Noto 字体渲染。
- Signature move：Playfair Display 字重 400（从不加粗）用于每个衬线时刻。{colors.accent} 中的斜体是标题强调色。

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
