> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/pink-script/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Pink Script — After Hours 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/pink-script/design.md`
- 预览卡：`bold-template-pack/templates/pink-script/preview.md`

## 选型元数据

- Slug：`pink-script`
- Tagline：黑色画布、亮粉点缀色、珠光米白纸张、Instrument Serif 标题：深夜编辑式的奢华。
- Mood：nocturnal、moody、intentional、luxe、expressive
- Tone：literary、sultry、considered、magazine
- Formality：medium-high
- Density：low
- Scheme：dark
- 适合：一切应当显得夜色、用心而略带奢华的内容：时尚品牌演示、创作者个人品牌、夜间/夜生活/烈酒发布、奢侈产品揭晓、编辑特稿。对想要以磁性自信落地的技术主题演讲、研究综合或商业提案而言，也是夺人眼球的意外之选。
- 避免：白天的企业职业化与传统 B2B 场景：暗画布配亮粉点缀在那里会显得过于造型化、过于外放。

## 视觉速览

一套夜色高级定制的编辑系统：暗暖黑纸张上以火热紫红油墨渲染，配柔和的胶片颗粒叠加与发丝级内框。DM Serif Display 以最高 600px 的字号承担每个花体与编辑时刻；Inter 字重 300 承担正文声音；JetBrains Mono 承担精品目录元数据。美学借鉴亮面时尚杂志跨页、深夜香水广告与高端 zine 的编辑页：更像时装屋的季节型录，而非初创公司演示。

Pink Script 是一套夜色高级定制编辑系统，建立在单一的氛围前提上：深暖黑表面，左上被一片略暖的 #1A1218 椭圆照亮，向右下渐隐至近黑。偏离中心的光源读起来像摄影棚柔光箱扫过杂志跨页的一角。其上叠加 8% 不透明度、滤色混合的细微胶片颗粒，添上深夜编辑摄影的照相颗粒感。表面之内是一道 1px 发丝级内框（纸粉色 14% 不透明度，自每边内缩 36px），是每页的编辑边框。拿掉受光渐变、胶片颗粒与内框，系统就会塌缩...

## 预览要素

- Palette：ink-deep #060507; ink-violet #0F0D11; paper-blush #F5EDF1; pink #ED3D8C; pink-light #FF66A8; pink-deep #B81D67
- Typography：DM Serif Display; Inter; JetBrains Mono
- Signature move：深暖黑表面（{components.slide-surface}），左上被径向渐变椭圆照亮。
- Signature move：每页幻灯片叠加细微胶片颗粒（{components.film-grain}）：不透明度 0.08，滤色混合。
- Signature move：1px 纸粉内框（{components.hairline-frame}），自每边内缩 36px，每页都有。
- Signature move：火热紫红粉（{colors.pink}）是唯一的彩色点缀：用作花体颜色、眉题颜色、线条颜色、胶囊描边、行内强调，以及主视觉花体背后的柔光晕。
- Signature move：DM Serif Display 承担每个编辑时刻，字号从 32px 缩放到 600px。没有第二种展示字体。

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
