> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/editorial-tri-tone/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Editorial Tri-Tone 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/editorial-tri-tone/design.md`
- 预览卡：`bold-template-pack/templates/editorial-tri-tone/preview.md`

## 选型元数据

- Slug：`editorial-tri-tone`
- Tagline：三色编辑系统：灰粉、芥末米白与深勃艮第酒红，用 Bricolage + Instrument Serif 排出。
- Mood：editorial、warm、intentional、moody
- Tone：literary、warm、considered、stylish
- Formality：medium-high
- Density：medium
- Scheme：mixed
- 适合：一切应当像时尚杂志跨页的内容：编辑提案、时尚品牌演示、生活方式媒体、艺术指导评审。同样适合任何想要三色纪律与衬线/无衬线对比、而非惯常中性色的演示文稿，科技、研究或商业皆可。
- 避免：需要读起来柔软或抚慰的演示文稿：勃艮第/粉/米白三色刻意追求高对比与造型感。

## 视觉速览

一套文学杂志遇上年报的演示系统，建立在严格的三色配色上：腮红粉、金黄奶油与深勃艮第酒红。尽管有十一个 CSS 变量名，整个系统只存在三个 hex 值；每个别名只是三者之一的语义化重命名。标题用 Bricolage Grotesque（带光学尺寸轴的可变怪诞体）以极端字重与负字距呈现。Instrument Serif（仅斜体切）作为富于表现力的点缀字体，用于章节数字、拉引语、年份与署名。JetBrains Mono 以紧凑大写字距承担所有元数据、标签与分节标记。美学是"独立艺术出版物"：带版权页、手工编号版本和编辑桌的那种。

Editorial Tri-Tone 是一套文学杂志式演示系统，建立在尽可能严格的三色配色上：三个 hex 值，十一个 CSS 变量名。命名系统透露了编辑意图：--pink 与 --sky 指向同一抹腮红；--cream、--butter、--lime 与 --terracotta 都解析为同一种金黄；--burgundy、--navy、--forest 与 --ink 全部坍缩为同一种深酒红。这些别名的存在是为了传达颜色在语境中的角色，而不是引入变化。

## 预览要素

- Palette：pink #F2B6C6; butter #F2D86A; burgundy #7A1F35
- Typography：Bricolage Grotesque; Instrument Serif; JetBrains Mono
- Signature move：带语义别名的三色配色：腮红粉（#F2B6C6）、金黄奶油（#F2D86A）、深勃艮第（#7A1F35）。
- Signature move：混搭排印：Bricolage Grotesque 怪诞体负责展示与正文；Instrument Serif 负责富表现力的点缀数字、引语与年份；JetBrains Mono 负责所有标签。
- Signature move：Bricolage Grotesque 标题内的 em 标签总会切换为 Instrument Serif 斜体：这是系统的首要排印混搭。
- Signature move：胶囊形（border-radius 999px）是通用标签组件，在封面、图表图例与收尾页使用三种不同尺寸。
- Signature move：数值卡片有 28px 的慷慨圆角：柔和圆润，不走粗野主义。

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
