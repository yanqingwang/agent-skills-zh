> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/bold-poster/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Bold Poster 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/bold-poster/design.md`
- 预览卡：`bold-template-pack/templates/bold-poster/preview.md`

## 选型元数据

- Slug：`bold-poster`
- Tagline：编辑海报美学：超大 Shrikhand 展示字体，配单一的消防红点缀色。
- Mood：bold、editorial、loud、confident
- Tone：dramatic、graphic、sharp、intentional
- Formality：medium
- Density：low
- Scheme：light
- 适合：一切应当像杂志封面一样有冲击力的内容：品牌宣言、创始人愿景演示、编辑/文化类路演、创意评审。任何想让寥寥数语产生海报效果的场合都很出色，也包括意想不到的场景：科技主题演讲，或者想变得"值得引用"的金融宣言。
- 避免：需要在每页传达密集信息的演示文稿，这套布局围绕少量大字陈述构建，而非细节段落。

## 视觉速览

一套民粹主义编辑海报系统，将复古意大利体育杂志的展示字体与古典衬线正文、紧凑的等宽字体元数据混搭在一起。展示字体是 Shrikhand：一种厚重的粗衬线/手写体混合字体，带俏皮的意大利斜体个性，以海报级字号（常为 200-320px）呈现，且经常倾斜偏离轴线。正文使用 Libre Baskerville，营造文学性编辑语域；Space Grotesk 负责微型大写标签与边框装饰。配色毫不妥协：白色画布、深棕黑墨色（#1C1410）、单一饱和的番茄红（#D8000F），以及用于交替面板的暖调米白（#F5F2EF）。边框是 1.5-3px 的粗墨线；唯一的阴影是红色展示文字背后的一道堆叠偏移阴影。这种美学喧闹、自信、具有 unmistakable 的印刷海报感，更接近 1970 年代欧洲品牌年报或葡萄酒商目录，而非当代幻灯片。

Bold Poster 是一套民粹主义编辑海报系统，其视觉语汇取自复古意大利体育杂志、世纪中叶欧洲品牌年报和葡萄酒商目录。其前提是：每一页都应有"印刷品"之感，用厚重的展示字体排印，锁定一种强烈的红色点缀色，铺在白色或米白纸面上，网格用墨线划定，装饰严格保持最小化。

## 预览要素

- Palette：bg #FFFFFF; dark #1C1410; red #D8000F; light #F5F2EF
- Typography：完整设计文档在选定后阅读。
- Signature move：白色（{colors.bg}）画布与米白（{colors.light}）面板交替形成条纹，加上深色（{colors.dark}）与红色（{colors.red}）的全出血面板表面用于宣言时刻。
- Signature move：单一番茄红（{colors.red}）是唯一的点缀色——用于每一个数字、每一条分节线、每一个标签、每一条左侧栏标记。
- Signature move：三字体栈：Shrikhand（展示 + 数字）、Libre Baskerville（正文）、Space Grotesk（等宽标签 + 列表符号 + 边框装饰）。
- Signature move：展示字体 Shrikhand 经常倾斜（-6° 到 +2°），这种旋转是系统的招牌动作。
- Signature move：厚重墨色边框：表格网格容器 3px，单元格 1.5-2px，编辑左侧栏卡片 4px 红色，列表行之间 1px 发丝线。

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
