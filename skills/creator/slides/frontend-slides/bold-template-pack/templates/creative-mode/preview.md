> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/creative-mode/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Creative Mode 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/creative-mode/design.md`
- 预览卡：`bold-template-pack/templates/creative-mode/preview.md`

## 选型元数据

- Slug：`creative-mode`
- Tagline：米白纸张画布，配自信的多色（绿、粉、橙、黄）点缀色与 Archivo Black 展示字体。
- Mood：creative、confident、playful、design-led
- Tone：graphic、expressive、modern
- Formality：medium
- Density：medium-high
- Scheme：light
- 适合：一切应当显得设计主导且自信的内容：创意代理商提案、设计工作室演示、广告公司资历介绍、品牌创意评审、艺术指导评审。当演讲者想以品味而非惯例开场时，用于技术分享、研究发现或财务评审也是出人意料的佳选。
- 避免：要求机构式克制与安静权威的场景：高饱和的多点缀色配色会显得外放而非正式。

## 视觉速览

一套为 1920x1080 幻灯片打造的新粗野主义编辑演示系统。整套演示锚定在暖米白画布上，配以厚重的 4px 墨色边框、硬偏移投影和大胆的四色点缀配色（森林绿、亮粉、焦橙、阳光黄）。展示标题以 Archivo Black 纯大写呈现：激进、响亮、字距毫无柔化。JetBrains Mono 等宽标签呼应排印规则单。正文使用 Space Grotesk。每页幻灯片都是平涂色块：无渐变、无圆角卡片、不玩含蓄。美学是三分包豪斯网格、三分朋克 zine、三分瑞士编辑风。

Creative Mode 是一套面向 1920x1080 演示的新粗野主义编辑幻灯片系统。奠基性的美学选择是技法克制配表达激进：无圆角卡片、无渐变、无暗示光源的阴影，只有平涂色块与硬偏移投影（"孔版印刷"或"丝网印刷"式，阴影是一块同色实心偏移）。

## 预览要素

- Palette：cream #EFE9D9; cream-2 #E4DCC4; ink #0F0F0F; ink-2 #2A2A2A; green #1F8A4C; green-dark #136636; pink #F06CA8; pink-dark #D14E8B
- Typography：Archivo Black; Space Grotesk; JetBrains Mono
- Signature move：米白画布（{colors.cream}，#EFE9D9）作为通用背景；绿色（{colors.green}，#1F8A4C）仅用于收尾页。
- Signature move：每个结构元素上都有 4px 实线墨色边框：卡片、面板、表格单元格、图表坐标轴。
- Signature move：以硬偏移盒阴影取代模糊投影：featured 区块用 24px 24px 0 color，24px 24px 0 4px ink。
- Signature move：Archivo Black 展示字体，大写配 0.92 行高，紧凑到极致。
- Signature move：四种点缀色均作平涂填充；每页只用四色中的两三种，绝不同时全用。

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
