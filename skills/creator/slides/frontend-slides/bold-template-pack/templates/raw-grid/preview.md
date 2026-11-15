> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/raw-grid/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Raw Grid 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/raw-grid/design.md`
- 预览卡：`bold-template-pack/templates/raw-grid/preview.md`

## 选型元数据

- Slug：`raw-grid`
- Tagline：新粗野主义演示：厚边框、偏移阴影与粉/鼠尾草绿/墨色配色。
- Mood：raw、punchy、energetic、confident
- Tone：direct、modern、no-nonsense、graphic
- Formality：medium-low
- Density：high
- Scheme：light
- 适合：一切应当显得直接且图形自信的内容：创始人提案、加速器演示、品牌演示、独立产品发布、创作者作品集。统计幻灯片、对比表格与流程图上表现出色。当演讲者想让演示显得野性自信而非规整拘谨时，用于科技、研究或金融同样出色。
- 避免：需要显得柔软、温暖或刻意安静的场景：粗野主义边框与偏移阴影押注于图形化语气。

## 视觉速览

一套新粗野主义演示系统，3px 实线黑边框就是版式本身。展示字体用系统原生无衬线字体栈（Segoe UI / system-ui），字重 900、严格大写：不加载任何 Web 字体。配色是白画布 + 黑结构 + 两种低饱和粉彩点缀色（腮红粉 #F2D4CF 与鼠尾草绿 #E5EDD6）+ 一个中性灰。深度来自 4px 与 6px 的实黑硬偏移阴影：从不模糊，从不变色。美学借鉴粗野主义编辑网页设计与 zine 版式：边框无间隙相接，对比强烈但被粉彩点缀色烘暖，大数字以极低不透明度躺在内容背后充当装饰壁纸。效果锐利、系统原生、数字感十足：更像 Notion 遇上抗议海报，而非打磨过的提案演示。

Raw Grid 是一套新粗野主义演示系统，建立在单一的结构前提上：3px 实线黑边框就是版式。区域之间没有外边距，单元格之间没有间隙，没有圆角，没有渐变。两个区域相遇时，一条 3px 黑线隔开它们：这条线就是整个网格系统。

## 预览要素

- Palette：black #0A0A0A; white #FFFFFF; pink #F2D4CF; green #E5EDD6; gray #F5F5F5; darkgray #333333
- Typography：Segoe UI
- Signature move：白色（{colors.white}）画布，3px 实线黑（{colors.black}）边框分隔每个区域。单元格之间没有间隙：边框边到边相接。
- Signature move：系统无衬线字体字重 900 大写用于所有展示文字；字重 500 常规大小写（sentence case）用于所有正文文字。
- Signature move：硬偏移阴影 6px 与 4px，实黑，永不模糊。
- Signature move：两种低饱和粉彩点缀表面：腮红粉与鼠尾草绿，只用作区域填充，从不用作文字颜色。
- Signature move：招牌黑胶囊标签组件（{components.label}）：小黑矩形里的白色大写文字，充当通用分节标签。

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
