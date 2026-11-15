> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/coral/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Coral 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/coral/design.md`
- 预览卡：`bold-template-pack/templates/coral/preview.md`

## 选型元数据

- Slug：`coral`
- Tagline：近黑底面上的米白与珊瑚红，用超大号 Bebas Neue 排出。
- Mood：bold、warm、modern、confident
- Tone：graphic、punchy、magazine
- Formality：medium
- Density：medium
- Scheme：mixed
- 适合：一切应当显得暖色图形化且编辑感十足的内容：时尚、美妆、健身、餐饮、生活方式品牌、代理商资历介绍。同样适合创作者作品集、宣言式陈述，或想要温暖感与单一大胆点缀色、而非企业冷酷感的科技/研究演示。
- 避免：需要安静或机构感的场景：珊瑚红点缀色与超大 Bebas Neue 全力押注于自信的杂志语气。

## 视觉速览

一套大胆的杂志海报系统，运行于三种表面语域：珊瑚红火、墨黑与暖米白，由 Bebas Neue 展示大写字母与恒定的 45° 斜线纹理驱动。Inter 负责正文；Bebas Neue 以宽字距处理每个标题、统计数字、名称与元数据图形。文化参照是世纪中叶旅行海报、Saul Bass 电影片头与现代编辑风体育杂志：实色平面以硬边相接，超大压缩大写字母充当建筑元素，单一珊瑚红色相既是点缀色也是整页环境色。

Coral 是一套大胆的杂志海报系统，建立在珊瑚红火、墨黑与暖米白三种表面语域之上，各语域以硬边相接。定义性的结构前提是实色平面：一页幻灯片会切分为珊瑚红半区 + 米白半区 + 墨黑顶部区，每个区域是一片平涂实色，承载各自独立的构图。区域之间没有渐变过渡；两种颜色的交汇点就是版式本身。它是更精致编辑系统的民粹主义对应物：更像体育杂志封面，而非文学图录。

## 预览要素

- Palette：coral #E85D5D; coral-dark #D44A4A; cream #F5F0E8; cream-dark #E8E0D4; black #1A1A1A; gray #6B6B6B; light-gray #B0B0B0; white #FFFFFF
- Typography：Bebas Neue; Inter
- Signature move：实色区域切分：珊瑚红/墨黑/米白区域以硬边相接。
- Signature move：点缀色边框：4px 珊瑚红左框、5px 珊瑚红顶框、3px 墨黑顶框、4px 墨黑横线。
- Signature move：45° 斜线纹理：一层 6% 不透明度的黑色斜向重复图案叠加在珊瑚红区域上，提供质感。
- Signature move：超大装饰排印：12% 不透明度的背景数字、35% 不透明度的巨型引号，置于主内容之后或旁边。
- Signature move：三表面系统：{colors.coral}（火）、{colors.black}（墨）、{colors.cream}（纸），用作以硬边相接的实色区域。

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
