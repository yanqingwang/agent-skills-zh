> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/monochrome/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Monochrome 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/monochrome/design.md`
- 预览卡：`bold-template-pack/templates/monochrome/preview.md`

## 选型元数据

- Slug：`monochrome`
- Tagline：象牙白账本纸配全黑文字；Lora 衬线标题、Jost 正文，完全没有颜色。
- Mood：restrained、literary、archival、ledger
- Tone：literary、considered、neutral、honest
- Formality：high
- Density：high
- Scheme：light
- 适合：一切应当像手工排字账本的内容：用户研究综合、白皮书、长篇报告、学术与政策简报、咨询交付物、EN/CN 双语报告。同样适合科技、设计或品牌演示中想让文字成为页面上唯一主角的那一类。
- 避免：需要视觉个性或以色彩主导叙事的演示文稿：全油墨配色刻意保持清苦。

## 视觉速览

一套以黑油墨印在米白纸上的文学编辑系统。超轻几何无衬线（Jost 字重 200–300）承担每个标题；Lora 斜体衬线处理引语文字与洞察卡标题；JetBrains Mono 提供结构化界面装饰。没有任何彩色点缀：配色中的每种颜色都是石墨或米白色调，"点缀"只是"更深的油墨"的意思。美学借鉴独立研究报告、学术专著与当代编辑设计中最安静的一端：更像一本印刷期刊，而非技术演示。

Monochrome（Ivory Ledger）是一套文学编辑系统，建立在单一材质约束上：黑油墨配米白纸，别无其他。配色有八个 token，但其中七个是米白或石墨的色调变体。没有彩色点缀："点缀"色只是更深的油墨。最终得到的是一套读起来像精心排字的研报或安静的当代专著的系统，而不像一场演示。

## 预览要素

- Palette：cream-paper #FAFADF; cream-paper-2 #F2F2D2; cream-paper-3 #F0F0D4; cream-warm #F5F0E4; ink-black #1A1A16; ink-graphite #5E5E54; ink-graphite-light #8A8A80
- Typography：Jost; JetBrains Mono; Lora; {typography.label.fontFamily}
- Signature move：每页幻灯片都用米白纸张背景（{colors.cream-paper}）：从不用白，默认也不暗。米白就是表面，不是风格选择。
- Signature move：超轻 Jost（展示字重 200，正文字重 300）是主导的排印声音。
- Signature move：Lora 斜体衬线只出现在两个特定时刻：拉引语正文与洞察卡标题。别无他处。
- Signature move：JetBrains Mono 大写配 0.12em 以上字距，处理每个结构标签、界面装饰标签、坐标轴与列表符。
- Signature move：系统没有任何彩色点缀。点缀色就是 {colors.ink-black}：稍微更深的油墨。

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
