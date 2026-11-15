> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/playful/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Playful 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/playful/design.md`
- 预览卡：`bold-template-pack/templates/playful/preview.md`

## 选型元数据

- Slug：`playful`
- Tagline：阳光暖桃色背景配 Syne 展示字体：亲切的独立产品发布演示。
- Mood：warm、approachable、indie、friendly
- Tone：upbeat、informal、welcoming
- Formality：low
- Density：medium
- Scheme：light
- 适合：一切应当显得温暖、独立而亲切的内容：创作者作品集、独立产品发布、生活方式品牌、小企业提案、通讯/社区演示。对任何想要亲切人性化而非企业感的演示文稿（包括科技或研究）同样欢迎。
- 避免：机构可信度比温暖更重要的场景：桃色配色刻意不正式。

## 视觉速览

一套温暖、手工打造的编辑系统，建立在蜜桃陶土画布上，炭黑油墨是唯一的"颜色"。展示字体用 Syne（字重 700–800，紧凑负字距）；正文字体用 Space Grotesk 字重 400–500。美学借鉴独立工作室演示、孔版印刷 zine 与速写本跨页：有机 blob 边框、涂鸦式 SVG 涂饰、略微旋转的卡片与双描边偏移边框，给每页幻灯片带上手触过、不修边幅的温暖。效果是创意工作室编辑风，不是企业提案：自信而人性化，有结构而松弛。

Playful 是一套手工打造编辑系统，锚定在单一暖画布上：蜜桃陶土色 {colors.bg}（#F0C8A0），炭黑 {colors.text}（#1A1A1A）是唯一有意义的"颜色"。一切读起来像陶土纸上的墨。没有次级品牌色、没有渐变、没有彩色点缀。系统完全押注于单色纪律，在形状、字重、旋转与手绘印记中寻找表现力，而不是在配色多样性中。

## 预览要素

- Palette：bg #F0C8A0; bg-alt #E8B88E; light #F7DEC6; text #1A1A1A
- Typography：Syne; Space Grotesk
- Signature move：蜜桃陶土画布（{colors.bg}），炭黑油墨（{colors.text}）是唯一颜色。没有次级品牌配色。
- Signature move：Syne 字重 700–800 配负字距用于每个展示与数字时刻；Space Grotesk 400–500 用于正文。
- Signature move：卡片上的双描边偏移边框：3px 描边外加 ::before 生成的 6–8px 偏移幽灵边框。
- Signature move：卡片、区块与统计数字带 ±0.5deg 至 ±3deg 的小旋转，营造手工摆放感。
- Signature move：带不对称圆角的有机 blob 形状充当装饰边框与填充。

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
