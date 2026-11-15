> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/capsule/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Capsule 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/capsule/design.md`
- 预览卡：`bold-template-pack/templates/capsule/preview.md`

## 选型元数据

- Slug：`capsule`
- Tagline：暖骨色底上的模块化胶囊卡片，配完整的粉彩波普配色。
- Mood：playful、modern、warm、fresh、fun
- Tone：upbeat、graphic、approachable、cool
- Formality：medium-low
- Density：medium
- Scheme：light
- 适合：一切应当显得模块化、现代、略带 Y2K 感的内容：生活方式品牌、创作者作品集、DTC 新品发布、美妆/健康、代理商能力介绍。用于俏皮的科技演示，或想要波普艺术式清晰而非庄重感的研究演示，也很有趣。
- 避免：需要传统机构分量的场景，胶囊形状与粉彩波普会主动削弱权威感。

## 视觉速览

一套俏皮编辑系统，建立在胶囊形容器、日晒褪色的 cream 画布和九色糖果配色之上。Bodoni Moda 衬线标题与 Space Grotesk 正文搭配，像一本在 1970 年代冰淇淋店度假的文学杂志。每个承载文字的容器都是胶囊（border-radius 9999px），描以 2px 墨色描边，并投出 6-12px 的柔和偏移阴影。美学是"Memphis 遇上编辑风"：自信的排印、大量带边框的形状，以及作为氛围墙纸的漂浮装饰胶囊。

Capsule 是一套俏皮编辑系统，其定义性结构前提是胶囊：每个文字容器是胶囊，每个图标是胶囊，每根横条是胶囊，图表中的每个节点是胶囊。border-radius: 9999px 规则几乎适用于所有 UI 元素，较大的面板则柔化为 2rem 圆角。加上包裹每个形状的 2px 墨色描边，整个系统里的容器显得饱满、友好、图形辨识度强，既致敬 Memphis 设计与 70 年代末冰淇淋店招牌，又不放弃编辑纪律。

## 预览要素

- Palette：cream #F5F5F0; ink #1A1A1A; outline #1E1E1E; white #FFFFFF; coral #E85D4E; lime #C4D94E; lavender #C5B5E0; sky #8BB4F7
- Typography：Bodoni Moda; Space Grotesk
- Signature move：通用胶囊几何：小容器 border-radius: 9999px，较大的卡片/框架 2rem。
- Signature move：2px 实线 {colors.outline} 描边包裹每个胶囊、图标与卡片。
- Signature move：所有展示/标题/统计数字用 Bodoni Moda 衬线；所有正文/标签/胶囊文字用 Space Grotesk 无衬线。
- Signature move：日晒褪色的 cream 画布 {colors.cream}，叠加糖果点缀色 6-15% 不透明度的柔和径向光晕，营造背景氛围。
- Signature move：低不透明度墨色的硬偏移阴影（{colors.shadow}），偏移量 4/6/8/12px，始终为实色，始终在右下方向。

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
