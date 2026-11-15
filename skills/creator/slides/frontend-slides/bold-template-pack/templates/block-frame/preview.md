> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/bold-template-pack/templates/block-frame/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# BlockFrame 预览卡

本文件仅用于标题页预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/block-frame/design.md`
- 预览卡：`bold-template-pack/templates/block-frame/preview.md`

## 选型元数据

- Slug: `block-frame`
- Tagline: 新粗野主义演示，柔和霓虹色块配粗黑边框。
- Mood: 大胆、俏皮、图形感、清新
- Tone: 自信、图形感、波普、设计主导
- Formality: 中偏低
- Density: 高
- Scheme: 浅色
- Best for: 一切该有波普图形与设计主导感的内容：独立 SaaS 发布、代理商资质展示、创意评审、品牌改版。科技、金融或研究主题若想显得自信而当代、而非一本正经，也是出人意料的好选择。
- Avoid for: 需要安静机构克制或传统分量的场合（受监管的披露、正式法律文书）。

## 视觉速览

一套极繁的新粗野主义演示系统，建立在 4px 实心黑边框、8px 硬边偏移阴影，以及五种饱和柔和浅彩加奶油与米白的高明度糖果配色之上。展示字体用 Inter 800-900 字重的紧凑全大写，次级边框装饰用 Space Grotesk 充当准等宽标签字面。倾斜的装饰形状（旋转的星形、矩形、徽章）刺穿边框，刻意打破网格。浅彩大胆配对：粉 + 蓝 + 绿 + 黄 + 奶油在各区域循环，并置经过安排。美学借鉴 zine 排版、1990 年代复兴贴纸书与当代玩具包装：大胆、欢快、略带混乱，从不怯场。

BlockFrame 是一套极繁的新粗野主义演示系统，建立在五条结构法则之上：每个区域都有 4px 黑边框，每个浮起元素都有 8px 硬边偏移阴影，每个角都是直角，每个强调色都是饱和浅彩，每个布局都允许稍微歪一点。这套系统的乐趣来自这些法则的刻意碰撞：带边框的卡片与带边框的卡片相遇，阴影叠着阴影，倾斜的装饰有意刺穿网格。

## 预览要素

- Palette: black #000000; white #FFFFFF; offwhite #FFFDF5; pink #FE90E8; blue #C0F7FE; green #99E885; yellow #F7CB46; cream #FFDC8B
- Typography: 选定后阅读完整设计文档。
- Signature move: 主卡片 4px 实心黑边框，次级边框装饰 3px，绝不更细。
- Signature move: 主卡片 8px 硬边偏移阴影，次级边框装饰 4px，纯黑、零模糊。
- Signature move: 五色浅彩（粉、蓝、绿、黄、奶油）加黑、白、米白，在各表面间循环。
- Signature move: Inter 800-900 字重全大配负字距是展示声部；Space Grotesk 600 字重全大配 0.08em 字距是标签声部。
- Signature move: 处处直角，唯一的例外是数字卡片上一个圆形强调点。

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
