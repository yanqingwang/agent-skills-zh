> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/mat/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Mat 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/mat/design.md`
- 预览卡：`bold-template-pack/templates/mat/preview.md`

## 选型元数据

- Slug：`mat`
- Tagline：暗鼠尾草绿画布配骨白纸张与焦橙点缀色；世纪中叶现代风，带木质底色。
- Mood：warm-modern、considered、tactile、mid-century
- Tone：warm、design-led、intentional、considered
- Formality：medium
- Density：medium
- Scheme：mixed
- 适合：一切应当显得世纪中叶、有材质触感且用心的内容：设计工作室资历介绍、建筑/室内品牌、陶瓷/手作/家具、咨询演示。对想要用心模拟质感而非数字冷感的科技、研究或商业演示而言，也是一个温暖而独特的选择。
- 避免：需要快速科技能量或机构式克制的场景：低饱和鼠尾草绿与焦橙配色刻意保持温暖与缓慢。

## 视觉速览

一套温暖、材质触感强、灵感来自高端产品落地页的演示系统。暗森林绿是主导环境，每页暗色幻灯片的右下角透出低沉的木质棕色氛围光。米白文字直接浮在色场上；暖橙充当唯一点缀色。字体栈把 Bricolage Grotesque（厚重圆润的怪诞体）用于展示，DM Sans 用于正文，DM Mono 用于标签：成品读起来像工业设计作品集遇上精品产品发布，绝不是技术演示。

Mat 是一套材质触感演示系统，围绕单一的环境前提构建：深森林绿表面，右下角透出低沉的木质棕色光晕。氛围承担了主要工作：在任何内容落位之前，幻灯片就已经像午后光线里的工作台。米白文字直接浮在绿色场面上；没有卡片、没有面板、没有边框。系统需要打破绿色时，只用一个米白内嵌盒（信息卡），读起来像铺在深色表面上的一张暖纸。

## 预览要素

- Palette：bg-dark #232E26; bg-dark-alt #2E3D30; bg-cream #EDE6D0; bg-cream-alt #E4DAC4; ink-cream #F0E8D2; ink-dark #1E2820; accent-orange #C07030; wood-glow #7A4E24
- Typography：Bricolage Grotesque; DM Sans; DM Mono; {typography.label.fontFamily}
- Signature move：暗森林绿画布（{colors.bg-dark}），每页暗色幻灯片右下角锚定一圈温暖的木质棕色径向光晕（{components.atmospheric-glow}）。
- Signature move：米白文字（{colors.ink-cream}）直接浮在绿色场面上，周围没有任何卡片、面板或边框。
- Signature move：Bricolage Grotesque 展示字体始终大小写混排，从不大写。大写只保留给 DM Mono 标签。
- Signature move：唯一点缀色暖橙（{colors.accent-orange}），只用作小型行内强调（眉题、列表符、行内 <em>、引号字形、一根图表柱）。
- Signature move：米白信息卡（{components.info-card}）是招牌的材质对比组件：嵌在暗色场面上的一块暖纸矩形。

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
