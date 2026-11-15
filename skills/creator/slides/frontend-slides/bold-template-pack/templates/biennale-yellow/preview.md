> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/bold-template-pack/templates/biennale-yellow/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Biennale Yellow 预览卡

本文件仅用于标题页预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/biennale-yellow/design.md`
- 预览卡：`bold-template-pack/templates/biennale-yellow/preview.md`

## 选型元数据

- Slug: `biennale-yellow`
- Tagline: 暖羊皮纸上的日光黄，配深靛蓝衬线与氛围感日晕渐变。
- Mood: 编辑感、有氛围、温暖、文化机构感、海报感
- Tone: 文学、审慎、沉静、温润现代、荷兰编辑风
- Formality: 高
- Density: 中
- Scheme: 浅色
- Best for: 一切该有艺术双年展海报或博物馆年度项目册质感的内容：展览演示、艺术机构公告、设计会议手册、策展提案、文学出版物、工作室回顾。同样适合任何想要荷兰编辑氛围、又要有醒目单色印记的演示。
- Avoid for: 需要视觉冲击或饱和多色能量的演示。暖纸底与单一黄色配色刻意安静、重氛围。

## 视觉速览

一套文学编辑风演示系统，视觉语域取自艺术双年展图录或安静的展览海报。美学建立在暖羊皮纸底（#E9E5DB）之上，铺开柔和日光黄（#F1EE2E）的径向光晕，衬以单一的深靛蓝墨色。展示字体是 Instrument Serif：一款当代高对比衬线，升部修长、斜体优雅，配 Archivo 作无衬线边框装饰，JetBrains Mono 负责数字与元数据标注。没有投影、没有圆角、没有带边框的卡片：唯一的结构线是墨色的 1px 发丝线。气质介于折起的博物馆手册、慢读的文学季刊与地中海展览海报之间：自信、有氛围、克制到底。

Biennale Yellow 是一套文学编辑风演示系统，取法欧洲艺术双年展图录、慢节奏展览海报与文学季刊的视觉语言。没有卡片、没有按钮、没有阴影、没有圆角。结构语汇只有三样：纸、墨、黄。

## 预览要素

- Palette: paper #E9E5DB; paper-deep #DCD6C4; sun #F1EE2E; sun-soft #F8F39B; haze #F0DA7C; ink #1B2566; ember #E26B4A
- Typography: 选定后阅读完整设计文档。
- Signature move: 每一处表面都用暖羊皮纸底（{colors.paper}）；绝不用白，绝不用灰。
- Signature move: 所有文字与所有分隔线只用单一墨色（{colors.ink}），不设次级文字色。
- Signature move: 日光黄（{colors.sun}）以三种方式使用：铺满的面板、柔和的径向光晕、半透明几何色块衬底。
- Signature move: 所有展示场合都由 Instrument Serif 承担，字号从 40px 到 720px+。
- Signature move: Archivo Bold 全大写配 0.16–0.32em 字距，是通用的标签声部。

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
