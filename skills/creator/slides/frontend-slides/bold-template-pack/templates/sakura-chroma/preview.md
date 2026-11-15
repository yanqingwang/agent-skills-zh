> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/sakura-chroma/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Sakura Chroma 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/sakura-chroma/design.md`
- 预览卡：`bold-template-pack/templates/sakura-chroma/preview.md`

## 选型元数据

- Slug：`sakura-chroma`
- Tagline：复古日式卡带包装美学：米白纸张、对角彩虹缎带、压缩加粗字体、JIS 风格规格复选框。
- Mood：retro、playful、kawaii-tech、warm、tactile、product-catalogue
- Tone：playful、confident、warm、tactile、80s-Japanese-tech
- Formality：low
- Density：medium
- Scheme：light
- 适合：一切应当像复古日式卡带包装或 TDK / Sony / Sakura Color 产品目录的内容：独立硬件品牌演示、音乐厂牌发行排期、模拟时代工作室回顾、zine 与杂志提案、kawaii-tech 产品发布、创意工作室年报。同样适合任何想要大胆色彩、压缩展示字体与印刷产品触感个性的演示文稿。
- 避免：需要克制、企业感或安静排印的演示文稿：加粗压缩字组、缎带条纹与原色配色刻意喧闹、刻意产品页感。

## 视觉速览

一套卡带包装编辑系统：暖米白纸张、六色原色配色与暖棕油墨。展示字体用 Big Shoulders Display（字重 900 的压缩工业展示无衬线）；正文用 Albert Sans；表格与标签内容用 JetBrains Mono；零星日文点缀用 Noto Sans JP。美学借鉴 1970 年代消费级卡带包装、日本印刷目录与低保真产品 zine：花瓣簇 blob 团、对角多彩缎带、12 角爆炸印章、红色矩形戳记与带字距的大写微标签。效果是手工策展的工业编辑风：温暖而有纪律，俏皮而排印紧实，卡带就是它的视觉隐喻。

Sakura Chroma 是一套卡带包装编辑系统，把每页幻灯片当作一本小型日本音响产品目录里的印刷产品页。视觉隐喻是彻底的：花瓣簇 blob 印记、对角多彩缎带、12 角爆炸印章、红色矩形戳记、等宽字规格行、色码小片与均衡器风格柱状图。一切读起来像从 1970 年代消费级音响手册的封底跨页里撕下来的：温暖、手工策展、工业化排印。

## 预览要素

- Palette：paper #F1E6CB; paper-dk #E5D6B0; ink #3A2516; red #E5392A; pink #E54489; orange #F09131; green #3D9F47; blue #3F8BC4
- Typography：完整设计文档在选定后阅读。
- Signature move：暖米白纸张画布（{colors.paper}），暖棕油墨（{colors.ink}）作结构，六种原色点缀。
- Signature move：4px 周期的半调圆点纸张纹理（{components.paper-texture}）以 16% 不透明度盖在每页幻灯片上。必需。
- Signature move：每个展示时刻用 Big Shoulders Display 字重 900 配负字距；正文用 Albert Sans；表格/数据用 JetBrains Mono；日文点缀用 Noto Sans JP。
- Signature move：花瓣簇 blob 印记（4–5 个重叠正圆）是招牌装饰元素。
- Signature move：对角多彩缎带（5 条堆叠彩条，呈 -22° 或 +22°）作为氛围层次。

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
