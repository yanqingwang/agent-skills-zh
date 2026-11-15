> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/studio/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Studio 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/studio/design.md`
- 预览卡：`bold-template-pack/templates/studio/preview.md`

## 选型元数据

- Slug：`studio`
- Tagline：黑色画布配电光黄文字；高压电的设计工作室美学。
- Mood：electric、bold、graphic、design-led、high-contrast
- Tone：graphic、loud、modern、intentional
- Formality：medium
- Density：medium
- Scheme：dark
- 适合：一切应当显得电感十足且设计主导的内容：工作室资历介绍、创意代理商提案、品牌展示、艺术指导评审、时尚/球鞋品牌工作。当演讲者想让演示本身*就是*一份品牌宣言时，用于科技、研究或商业演示也是夺目的意外之选。
- 避免：应当显得安静或机构式的场景：黑与电光黄配色是本库中最响亮的一套。

## 视觉速览

一套"Boring Studios"代理机构演示系统：文字即图形体量，精神气质来自当代设计工作室演示（Pentagram、Anti、Order）。整个系统跑在 Barlow 字重 900 大写上，展示字号下的文字重到不再是文字，而开始成为形状。配色是二元加一：近黑色场（#1C1C1C）、酸性黄文字（#F5D200），以及同一黄色用作整页幻灯片背景。IBM Plex Mono 承担每个页脚元数据、页码计数与三栏字组。没有投影、没有圆角、没有点缀色：标题就是设计本身，每页幻灯片唯一的色彩决定是近黑底暗黄字，还是酸性黄底近黑字。

Studio 是一套文字即图形体量的演示系统：当代设计工作室演示（Pentagram、Anti、Order，"Boring Studios"代理机构美学）的视觉语域。前提化减到近乎严苛：单一字体（Barlow）、单一字重（900）、严格大写，字号大到文字不再像文字，而开始像图形形状。标题就是设计本身：没有装饰元素、没有点缀色、没有纹饰。把 Studio 幻灯片上其他一切拿掉只留标题，这页幻灯片仍读得出 Studio。

## 预览要素

- Palette：near-black #1C1C1C; near-black-alt #242422; acid-yellow #F5D200; acid-yellow-alt #F0CC00; border-dark #2E2E2C
- Typography：Barlow; IBM Plex Mono; {typography.body.fontFamily}
- Signature move：二元配色：{colors.near-black} 色场配 {colors.acid-yellow} 文字，或 {colors.acid-yellow} 色场配 {colors.near-black} 文字。没有第三种颜色。
- Signature move：所有标题在所有字号都用 Barlow 字重 900 大写；正文用 Barlow 400/500；IBM Plex Mono 只用于元数据装饰。
- Signature move：标题字号巨大：封面展示 12vw（1920px 视口下约 230px），宣言 7.5vw，分节标题 4.8vw。
- Signature move：所有展示文字配紧凑负字距（-0.01 至 -0.03em）；大写不可协商。
- Signature move：纯平：没有投影、没有圆角、没有渐变，黄/暗二元之外没有点缀色。

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
