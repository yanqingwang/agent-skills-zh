> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/neo-grid-bold/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Neo-Grid Bold 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/neo-grid-bold/design.md`
- 预览卡：`bold-template-pack/templates/neo-grid-bold/preview.md`

## 选型元数据

- Slug：`neo-grid-bold`
- Tagline：米白纸面上的编辑风新粗野主义，配单一霓虹黄点缀色。
- Mood：confident、punchy、editorial、modern
- Tone：bold、minimal、design-led、graphic
- Formality：medium
- Density：high
- Scheme：light
- 适合：一切应当显得自信且编辑图形化的内容：设计主导的提案、品牌工作、创始人演讲、大会主题演讲。特别适合统计密集的幻灯片、对比与流程图。当演讲者想显得设计主导而非企业化时，用于科技、研究或金融同样出色。
- 避免：需要显得安静、传统或温暖的场景：霓虹黄点缀色与大写展示字体押注于自信的编辑语气。

## 视觉速览

一套厚重的编辑海报系统，建立在严格的 12 列 × 8 行块网格上，以霓虹黄点缀色铺在油灰米白上。Space Grotesk 字重 700 严格大写承担每个展示时刻；JetBrains Mono 承担每个标签与元数据标牌。每页幻灯片读起来像一期被切成彩色面板的杂志跨页：纸米白、墨黑与电光柠檬黄在各单元格间互换角色。美学借鉴当代编辑印刷、粗野主义年报，以及设计周展示中最民粹海报的一端。

Neo-Grid Bold 是一套厚重的编辑海报系统，建立在单一的结构前提上：每页幻灯片是一个 12 列 × 8 行的 CSS 网格，自幻灯片边缘内缩 40px，单元格之间留 12px 间隙。构图通过给网格跨度指派彩色面板完成：grid-column: 4 / span 5 与 grid-row: 1 / span 5 就是版式的描述方式。网格是刚性的；视觉变化来自 {colors.paper}、{colors.ink} 与 {colors.accent-lemon} 面板在单元格间的排布。

## 预览要素

- Palette：paper #F5F4EF; bg #ECECE8; ink #0A0A0A; accent-lemon #E6FF3D; muted #8A8A85; stage-bg #1A1A1A
- Typography：Space Grotesk; JetBrains Mono
- Signature move：通用 12 列 × 8 行 CSS 网格（{components.frame}），自每页幻灯片边缘内缩 40px，单元格间 12px 间隙。
- Signature move：三色面板系统：纸米白（{colors.paper}）为默认，墨黑（{colors.ink}）用于反色区块，点缀柠檬黄（{colors.accent-lemon}）用于信号区块。
- Signature move：Space Grotesk 字重 700 大写配负字距，用于每个展示元素。
- Signature move：JetBrains Mono 大写配 0.08–0.12em 字距，用于每个标签、页码与坐标轴标牌。
- Signature move：招牌角标与块标：小的 2×2 块状印记，充当装饰性身份标签。

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
