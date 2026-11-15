> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/bold-template-pack/templates/blue-professional/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Blue Professional 预览卡

本文件仅用于标题页预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/blue-professional/design.md`
- 预览卡：`bold-template-pack/templates/blue-professional/preview.md`

## 选型元数据

- Slug: `blue-professional`
- Tagline: 奶油纸底配电光钴蓝点缀，干净现代的专业感。
- Mood: 专业、现代、平静、可信
- Tone: 干净、审慎、精致、中性
- Formality: 中偏高
- Density: 中
- Scheme: 浅色
- Best for: 一切该有现代审慎、略带权威感的内容：B2B SaaS 提案、咨询交付物、顾问动态、投资人报告。任何时候想显得专业又不僵硬，都是干净得体的选择：研究综述、内部评审、服务型企业的品牌工作。
- Avoid for: 需要热烈、俏皮或刻意随意的演示。冷调电光蓝的克制会显得过于打磨。

## 视觉速览

一套克制的咨询级演示系统，铺在暖奶油画布（#fdfae7）上，只用单一饱和钴蓝（#1e2bfa）作强调色。展示字体用 Space Grotesk 承担标题与数字标注，Inter 负责正文与边框装饰。卡片是 4% 不透明度的淡钴蓝，配 1.5px 半透明边框与 10-14px 圆角，安静，绝不用实色描边。美学借鉴投资研究报告、麦肯锡级季度简报与当代金融仪表盘：有分寸，数据密集却不拥挤，专业感一眼可辨。这套系统为高管远距离阅读而建，字体层级强，所有强调时刻都交给单一强调色。

Blue Professional 是一套咨询级演示系统，为高管简报、研究交付物与季度评审设计。其底层视觉前提是克制，只守住一个强承诺：暖奶油画布（{colors.bg} — #fdfae7）与单一饱和钴蓝（{colors.primary} — #1e2bfa），由它承担每一处强调、每一个指标、每一个 CTA、每一个眉标、每一块图表填充。没有次级品牌色、没有浅彩配色、没有冷暖对撞，只有奶油、钴蓝，以及一组紧凑的低饱和灰供正文使用。

## 预览要素

- Palette: bg #FDFAE7; primary #1E2BFA; text #111111; text-muted #6B6B6B; text-light #9A9A9A; positive #059669; negative #DC2626
- Typography: 选定后阅读完整设计文档。
- Signature move: 每一处表面都用暖奶油底（{colors.bg}），绝不用纯白，绝不用灰。
- Signature move: 单一饱和钴蓝（{colors.primary}）是唯一强调色，用于每一个眉标、指标、CTA、图表填充与进度指示。
- Signature move: Space Grotesk（展示 + 边框装饰）+ Inter（正文），两者都不得替换。
- Signature move: 卡片用 4% 钴蓝淡色，配 20% 钴蓝的 1.5px 边框与 10-14px 圆角。
- Signature move: 柔和胶囊状边框装饰（{components.tag-pill}、{components.cta-button}），圆角一律 100px。

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
- 永远不要在页面上放置用户需求备注（如期望气质、受众、内部使用标签），除非用户明确要求这些字面词出现在演示中。
- 可见边框装饰只使用真实演示内容：演示标题、真实的分节标题、日期、作者、公司、页码，或来自用户材料的真实内容短语。
- 生成预览时不要读取 `template.html`。
- 不要读取其他模板的 `design.md` 文件。
- 在用户为完整演示选定本模板后，先阅读完整设计文档再生成最终幻灯片。
