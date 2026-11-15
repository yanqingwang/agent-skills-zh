> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/long-table/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Long Table 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/long-table/design.md`
- 预览卡：`bold-template-pack/templates/long-table/preview.md`

## 选型元数据

- Slug：`long-table`
- Tagline：暖米白与锈红的晚宴俱乐部美学：加粗大写怪诞体标题、Fraunces 衬线与胶囊形描边按钮。
- Mood：warm、intimate、modern、friendly、small-batch、social、hospitality
- Tone：warm、playful、considered、social、magazine-friendly、modern-editorial
- Formality：medium
- Density：medium
- Scheme：light
- 适合：一切应当像温暖、亲密、现代的待客/社区品牌的内容：晚宴俱乐部、晚宴系列、小餐厅、创意工作室活动、会员招募提案、生活方式与葡萄酒品牌。同样适合任何想要单一暖点缀色、混字重排印与社媒意识现代编辑语气的演示文稿。
- 避免：需要企业光鲜感、技术密度或冷调/极简语域的演示文稿：锈红配色与加粗衬线混搭刻意保持温暖与亲人的姿态。

## 视觉速览

一套温暖的单一油墨编辑系统，语域接近晚宴俱乐部海报、小批量 zine 或孔版印刷的节目单。整个系统只用一种油墨色：暖锈陶土色（#B53D2A），铺在奶油米白纸面底色（#FAF1E2）上，叠加一层 4px 径向圆点纹理，赋予表面"印刷纸张"质感。展示字体用 Bricolage Grotesque 字重 700–800 大写；正文与元数据用 Fraunces 衬线字重 400–600 并开启光学尺寸轴。胶囊按钮、描边版次徽章、斜体版次数字与虚线/实线 1.5px 边框，补齐了印刷节目单的词表。

Long Table 是一套单一油墨编辑系统，语域接近晚宴俱乐部海报、孔版印刷 zine 或小出版社晚宴节目单。奠基性前提是单色：系统中每个可见印记，每个标题、每段正文、每条边框、每条横线、每个胶囊、每个页码，都以单一暖锈陶土油墨（{colors.ink}，#B53D2A）渲染在奶油米白纸面底色（{colors.paper}，#FAF1E2）上。唯一的色彩变化是不透明度：同一油墨，主印记 100%，弱化元数据 78%，虚线内部分隔线 32%，纸张纹理圆点 10%。

## 预览要素

- Palette：paper #FAF1E2; paper-d #F2E5CF; paper-vd #E8D7B6; ink #B53D2A; ink-dp #8E2D1F; rule #B53D2A
- Typography：完整设计文档在选定后阅读。
- Signature move：Bricolage Grotesque 字重 700 与 800、严格大写，承担每个展示时刻：封面、标题、卡片标题、课程名、引语正文、信息值、人物标签。Bricolage 是一种宽幅、略压缩的怪诞体，个性强烈；其大写形式 upp...
- Signature move：Fraunces 字重 400–600 承担每段正文、每个元数据字段、每个胶囊、每个页码、每个版次标签。斜体 Fraunces 是默认正文样式：倾斜衬线是系统的正文声音，赋予温暖与编辑 personali...
- Signature move：单一油墨色（{colors.ink}，暖锈陶土）配米白纸张（{colors.paper}）。不透明度变体是唯一的色彩变化。
- Signature move：展示时刻一律 Bricolage Grotesque 字重 700–800 大写；正文与元数据一律 Fraunces 400–600 默认斜体。
- Signature move：每页幻灯片通过 .stage::before 叠加细微的 4px 径向圆点纸张纹理：远看不可见，近看才显现。

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
