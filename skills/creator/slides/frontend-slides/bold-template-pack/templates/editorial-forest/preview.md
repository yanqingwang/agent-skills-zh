> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/editorial-forest/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Editorial Forest 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/editorial-forest/design.md`
- 预览卡：`bold-template-pack/templates/editorial-forest/preview.md`

## 选型元数据

- Slug：`editorial-forest`
- Tagline：森林绿、灰粉与暖米白，配上 Source Serif 4，构成一套安静而用心的季报式演示文稿。
- Mood：editorial、quiet、considered、warm、intentional
- Tone：literary、thoughtful、warm、low-pressure
- Formality：medium
- Density：medium
- Scheme：mixed
- 适合：一切应当像一篇用心编辑的文章的内容：季度评审、内部汇报、工作室动态、创意代理商演示。同样适合任何想要温暖从容、而非企业感的演示文稿，包括研究回顾、图书或项目发布、团队复盘。
- 避免：需要紧迫感、冲击力或销售驱动感的场景：配色与节奏刻意保持安静。

## 视觉速览

一套以衬线为主导的编辑演示系统，语域接近文学季刊或艺术书专著。展示字体用 Source Serif 4，字重 500，开启光学尺寸轴，封面与统计时刻放大到 220px。配色把深森林绿（#2e4a2a）与灰玫瑰粉（#e89cb1）铺在燕麦米白的纸面底色（#efe7d4）上，JetBrains Mono 担任编辑界面装饰（标签、图注、坐标轴刻度）。美学更接近企鹅经典书封、Apartamento 杂志跨页或安静的年报，而非技术主题演讲：自信、纸感、坚守一套很小的色彩词表。

Editorial Forest 是一套以衬线为主导的编辑演示系统，声调语域接近企鹅经典、安静年报或艺术书跨页。系统的奠基性前提是单一而自信的排印声音：Source Serif 4，以极端字号（最高 220px）承担标题与统计数字，JetBrains Mono 扮演编辑界面装饰的配角（标签、图注、坐标轴刻度、页脚线）。

## 预览要素

- Palette：green #2E4A2A; green-deep #243A21; green-lite #3A5A36; pink #E89CB1; pink-deep #D27E96; cream #EFE7D4; cream-2 #E6DCC4; ink #1A1A17
- Typography：JetBrains Mono
- Signature move：三色编辑配色：深森林绿、灰玫瑰粉、燕麦米白纸张。每页两种表面色调是常态；三种就是喧闹。
- Signature move：所有标题、正文与展示时刻用 Source Serif 4 字重 500。开启光学尺寸轴以获得随字号变化的字形。
- Signature move：所有标签、图注、坐标轴刻度与页脚线用 JetBrains Mono 字重 500 大写，配宽字距（0.14em–0.18em）。
- Signature move：展示字号在封面与统计数字时刻放大到 220px；主标题 96px；卡片标题 56–84px。
- Signature move：2px 发丝线分隔堆叠的分节，永不加粗，颜色也从不脱离区域语境。

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
