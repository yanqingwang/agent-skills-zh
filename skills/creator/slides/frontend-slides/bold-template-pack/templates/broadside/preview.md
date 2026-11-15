> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/broadside/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Broadside 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/broadside/design.md`
- 预览卡：`bold-template-pack/templates/broadside/preview.md`

## 选型元数据

- Slug：`broadside`
- Tagline：深色编辑画布，单一火橙点缀色，双语拉丁/中文字体栈。
- Mood：editorial、dramatic、loud、newspaper
- Tone：graphic、punchy、literary、considered
- Formality：medium-high
- Density：medium
- Scheme：dark
- 适合：一切应当像大字报（broadside）报纸头条一样落地的内容：品牌宣言、杂志与文化类路演、设计演讲、双语 EN/CN 演示、创始人愿景陈述。对想要戏剧化单点缀编辑感的科技、研究或商业演示而言，也是一个醒目的选择。
- 避免：需要安静、温暖或机构传统感的演示文稿，深色画布加火橙点缀色全力拥抱戏剧性。

## 视觉速览

一套抗议海报编辑系统，建立在超大 Barlow 字体与单一火橙环境色之上。美学是"火上的墨"：深色页面用于记录，橙色页面用于宣告。展示字体极其巨大（13vw，1440 宽度下约 187px），字重 900 小写，把词当作图形元素而非阅读文案。文化参照是大字报印刷、SPACE10 报告，以及用一种响亮色彩与零装饰重新诠释的 Wim Crouwel 网格。

Broadside 是一套抗议海报编辑系统。其定义性前提：字号大到让文字不再表现为文本，而开始表现为图形基元。13vw（{typography.display}）的展示字号在 1440 宽的屏幕上把一个单词放到约 187px，宽到让眼睛在阅读之前先扫过字形。这是该系统首要的表达手段。

## 预览要素

- Palette：ink-black #111111; ink-black-alt #1A1A18; fire-orange #E85D26; cream #F0ECE5; cream-muted #888880; cream-hint #505048; border-dark #282826
- Typography：Barlow; IBM Plex Mono; {typography.label.fontFamily}
- Signature move：字重 900 的小写超大 Barlow 展示字体，展示元素上永远不用大写。
- Signature move：双色彩语域系统：深色页面配 cream 文字，或橙色页面配深色墨字。不存在 cream/white 页面。
- Signature move：{colors.fire-orange} 既是点缀色（在深色上）也是环境色（在橙色上），永远不做次级颜色，永远是*那个*颜色。
- Signature move：单一字体系统：Barlow + 仅用于边框装饰的 IBM Plex Mono。没有衬线体，没有手写体，没有第三字体。
- Signature move：1px 发丝分隔线（深色上用 {colors.border-dark}；橙色上用 rgba(17,17,17,0.2)）提供全部层级结构。

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
