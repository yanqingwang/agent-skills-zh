> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/cobalt-grid/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Cobalt Grid 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/cobalt-grid/design.md`
- 预览卡：`bold-template-pack/templates/cobalt-grid/preview.md`

## 选型元数据

- Slug：`cobalt-grid`
- Tagline：图纸画布上的电光钴蓝衬线，以阶梯式像素故障装饰与纤细发丝线锚定。
- Mood：editorial、design-research、studious、modernist、tech-print、monochrome
- Tone：considered、literary、studious、quietly-modern、editorial
- Formality：high
- Density：medium
- Scheme：light
- 适合：一切应当像一份安静严肃的设计/研究简报、艺术出版物或精选趋势报告的内容。特别适合工作室年报、代理商能力介绍、设计研究出版物、建筑/艺术/学术演示，以及任何想要单一严格点缀色与印刷账本式沉静、而非企业光鲜感的演示文稿。
- 避免：需要温暖感、多彩能量或随性/俏皮语气的演示文稿：严格的钴蓝 + 米白 + 网格配色刻意保持清冷克制。

## 视觉速览

一套日系杂志趋势报告系统，建立在暖米白纸张、电光钴蓝油墨与永久存在于每页幻灯片背后的图纸网格之上。Newsreader 衬线标题以 18vh 的高度耸立，DM Mono 负责界面装饰与跑马灯文字。招牌装饰是一条像素故障列：竖直扫描线沿陈述式幻灯片的右缘阶梯式下行，并与二维码风格的 8×8 网格贴片搭配。文化参照是 WIRED Japan、Shift 杂志，以及用双色孔版印刷（米白 + 一种钴蓝）印制的建筑趋势报告。

Cobalt Grid 是一套双色趋势报告编辑系统，建立在三块不可动摇的基石上：暖米白纸张画布（{colors.paper}）、电光钴蓝油墨（{colors.ink}），以及永久位于每页幻灯片背后的图纸网格。网格不是可选装饰：它通过每个 .stage 上的 ::before 伪元素渲染，无法关闭。美学是"双色孔版印刷专著"：只有米白 + 钴蓝，网格让整套演示文稿带上建筑描图纸或日系趋势报告的质感。

## 预览要素

- Palette：paper #F0EBDE; paper-2 #E6E0CE; ink #1F2BE0; ink-soft #5560E5
- Typography：Newsreader; Hanken Grotesk; DM Mono
- Signature move：1.5px 钴蓝发丝线边框（每页幻灯片的顶部与底部）。
- Signature move：分节标题下方 1.5px 钴蓝顶栏横线。
- Signature move：表格或索引条目之间 1px 淡钴蓝行分隔线。
- Signature move：置于一切内容背后的 10% 不透明度图纸网格。
- Signature move：像素故障与二维码块装饰 SVG 贴片，作为构图点缀。

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
