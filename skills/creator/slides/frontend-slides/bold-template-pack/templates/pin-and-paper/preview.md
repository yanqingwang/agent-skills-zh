> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/pin-and-paper/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Pin & Paper 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/pin-and-paper/design.md`
- 预览卡：`bold-template-pack/templates/pin-and-paper/preview.md`

## 选型元数据

- Slug：`pin-and-paper`
- Tagline：黄色纸张配别针插画、墨蓝手写 Caveat 与纸张颗粒纹理。
- Mood：crafted、handmade、warm、thoughtful、literary
- Tone：literary、intimate、warm、grounded
- Formality：medium
- Density：medium
- Scheme：light
- 适合：一切应当显得手工打造、温暖且文学的内容：质性研究发现、创始人随笔、长篇品牌故事、工作坊复盘。招牌的别针插画与纸张颗粒纹理，特别适合任何想要个性与温暖多于光鲜的演示文稿，科技或商业亦不例外。
- 避免：需要数字原生光鲜或严格数据驱动的演示文稿：手写 Caveat 刻意不正式。

## 视觉速览

一套田野笔记本编辑系统，渲染成配深钴蓝油墨的黄色便笺纸。每页幻灯片带 fractalnoise 纸张颗粒叠加、把卡片"钉"在页面上的手绘安全别针 SVG 插画，以及用于个人批注的手写 Caveat 字体。Space Grotesk 以重字重承担印刷标题；DM Mono 处理档案标签。美学借鉴模拟时代的田野报告、复古公告板与科学笔记本的日记页：更像钉在软木板上的实验期刊，而非光鲜的演示。

Pin & Paper 是一套田野笔记本编辑系统，建立在单一材质前提上：每页幻灯片都是黄色便笺纸。纸张由基础色（{colors.paper}，高饱和镉黄）、两道柔和的径向渐变高光（左上受光、右下投影）以及 ::before 伪元素上不可省略的分形噪点颗粒叠加（正片叠底混合）共同渲染。这一组合造就了侧光下读起来像物理纸张的表面。没有颗粒，系统就会塌缩成扁平的卡通黄；纹理是根基，不是装饰。

## 预览要素

- Palette：paper #EFE56A; paper-2 #F5ECA0; paper-3 #E8D85A; paper-extra #FBE6A4; cream #F8F1D6; kraft #C9A66B; ink #1F3A8A; ink-soft #2D4FB8
- Typography：Space Grotesk; Caveat; DM Mono
- Signature move：黄色纸张背景（{components.paper-surface}），叠两道径向渐变，且每页幻灯片都带不可省略的分形噪点颗粒叠加（{components.paper-grain-overlay}）。
- Signature move：深钴蓝油墨（{colors.ink}）作为通用的文字、边框、分隔线与别针插画颜色。
- Signature move：米白卡面（{colors.cream}）配 1.5px 墨色边框、4px 微圆角，以及硬墨蓝偏移阴影（5px–6px，零模糊）。
- Signature move：手绘安全别针 SVG 插画（{components.pin-illustration}），有闭合与张开两种变体，以轻微旋转角度钉在卡片上。
- Signature move：三声部排印：Space Grotesk 负责印刷标题，Caveat 手写体负责个人声音，DM Mono 负责档案标签。

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
