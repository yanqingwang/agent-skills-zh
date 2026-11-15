> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/soft-editorial/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Soft Editorial 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/soft-editorial/design.md`
- 预览卡：`bold-template-pack/templates/soft-editorial/preview.md`

## 选型元数据

- Slug：`soft-editorial`
- Tagline：暖纸张上的 Cormorant Garamond 衬线，配鼠尾草绿、腮红粉与柠檬黄点缀。
- Mood：literary、elegant、quiet、warm-classical
- Tone：literary、considered、warm、magazine
- Formality：high
- Density：low
- Scheme：light
- 适合：一切应当显得文学、优雅而从容的内容：编辑特稿、长篇品牌故事、画廊/博物馆演示、咨询交付物、婚礼/生活方式媒体、创始人随笔。对想要周日副刊式温暖而非企业光鲜的科技、研究或商业演示同样出色。
- 避免：需要视觉热度或冲击力的演示文稿：暖纸张配色与 Cormorant 衬线刻意保持安静。

## 视觉速览

一套温暖杂志跨页美学：那种带田野笔记抱负的小型印刷季刊会委托设计的版式。Cormorant Garamond 以正体斜体混排承担每个标题与装饰时刻；Work Sans 退居支撑性正文。配色是米白纸张外加一组粉彩糖果点缀（灰粉、柠檬绿、柔蜜桃、鼠尾草绿、丁香紫），用作彩色卡片背景。慷慨的圆角卡片（24–36px 圆角）以半透明白浮在米白色场上。情绪是编辑式沉静，撒一点孔版印刷色彩：更像文学研究笔记本，而非企业演示。

Soft Editorial 是一套温暖杂志跨页演示系统，视觉线索来自小出版社文学季刊与设计研究笔记本。前提是单一字体（Cormorant Garamond）几乎讲完所有的话，只有在衬线会疲惫处由庄重的人文无衬线（Work Sans）支撑。米白纸张色场是常量：每页幻灯片都坐在 {colors.paper}（#F2EEDF）上，一种暖调做旧米白，读起来是物理纸张，不是屏幕白。色场之上，圆角卡片以两种语域浮动：默认内容用半透明白的柔和，点缀时刻用高饱和粉彩糖果。

## 预览要素

- Palette：paper #F2EEDF; paper-2 #ECE6D2; ink #2A241B; ink-soft #5C5345; pink #E1A4C2; lemon #D6DD63; blush #E8C9B6; sage #B7C7A8
- Typography：Cormorant Garamond; Work Sans
- Signature move：单一暖米白表面（{colors.paper}）贯穿每页幻灯片；粉彩只作卡片填充，绝不作幻灯片背景（以 {colors.pink} 满版填充的收尾页除外）。
- Signature move：Cormorant Garamond 承担每个展示、标题、眉题与装饰时刻；Work Sans 只留给正文与眉线。
- Signature move：标题内正体 + 斜体混排是系统的排印信号：斜体短语从标题的字重 500 降到字重 400。
- Signature move：高饱和粉彩（{colors.pink}、{colors.lemon}、{colors.blush}、{colors.sage}、{colors.lilac}）是可互换的卡片填充，没有固定语义。
- Signature move：圆角卡片（24–36px 圆角）是默认容器；胶囊完全圆润（999px）；半透明白（{colors.card-fill}）是默认卡片填充。

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
