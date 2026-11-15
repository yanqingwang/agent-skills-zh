> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/cartesian/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Cartesian 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/cartesian/design.md`
- 预览卡：`bold-template-pack/templates/cartesian/preview.md`

## 选型元数据

- Slug：`cartesian`
- Tagline：安静的暖中性配色，古典 Playfair 衬线；有品位、不慌不忙。
- Mood：quiet、considered、elegant、warm-minimal
- Tone：classical、literary、restrained、confident-quiet
- Formality：high
- Density：low
- Scheme：light
- 适合：一切应当安静、深思、成熟的内容：投资论点、白皮书、咨询交付物、长篇研究、画廊/文化演示。对编辑特稿、创始人随笔，或任何以克制为信息的演示而言都是强选择，也包括科技与金融领域。
- 避免：需要视觉热度、多个点缀色或紧迫感的演示文稿，暖中性配色刻意保持低能量。

## 视觉速览

一套安静的博物馆图录编辑系统，建立在 Playfair Display 衬线标题、Inter 无衬线正文和五色调暖石配色之上。美学是"咨询演示遇上建筑专著"：极简几何线装饰（细圆、虚线弧、垂直与水平发丝线）漂浮在内容之后，暗示绘图纸与圆规作业。每条分隔线都是一条灰褐色的 1px 细线；没有任何粗体，没有任何喧闹。文化参照是 Massimo Vignelli 的编辑作品、Cooper Hewitt 图录，以及铅笔加描图纸的城市规划文档。

Cartesian 是一套安静的博物馆图录编辑系统。其定义性前提是通过 1px 线条实现克制。每个结构元素，列表分隔、议程横线、时间线连接线、卡片边框、表格分隔线，都是一条灰褐色 {colors.line} 的 1px 细线。没有粗边框，没有填充色，没有阴影，没有圆角表面。层级通过字体对比与负空间构建；传统意义上的深度并不存在。

## 预览要素

- Palette：bg-primary #EDE8E0; bg-secondary #E2DBD1; text-primary #1A1A1A; text-secondary #5A5A5A; accent #8A8178; line #B8B0A4
- Typography：Playfair Display; Inter
- Signature move：暖砂岩画布 {colors.bg-primary}，以单条 1px 灰褐色 {colors.line} 分隔线作为通用结构元素。
- Signature move：Playfair Display 衬线字重 400 用于每个标题/数字/引号；Inter 无衬线用于每个正文/标签/署名。
- Signature move：五色单色配色：两种石色、两种灰色、一种墨色。任何地方都没有鲜艳点缀色。
- Signature move：装饰性几何圆环（细实线 + 虚线圆，20-50% 不透明度）漂浮在内容之后，营造圆规绘制的氛围。
- Signature move：每个标签、署名与微文字都是大写 Inter，字距 2-3px。

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
