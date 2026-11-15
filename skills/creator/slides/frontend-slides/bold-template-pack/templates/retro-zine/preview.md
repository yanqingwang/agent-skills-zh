> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/retro-zine/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Retro Zine 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/retro-zine/design.md`
- 预览卡：`bold-template-pack/templates/retro-zine/preview.md`

## 选型元数据

- Slug：`retro-zine`
- Tagline：米黄纸张配绿色点缀色与 Bebas Neue + Caveat：一份 HTML 形态的孔版印刷 zine。
- Mood：crafted、lo-fi、underground、warm-retro
- Tone：scrappy、warm、intentional、DIY
- Formality：medium-low
- Density：medium
- Scheme：light
- 适合：一切应当显得印刷、低保真且手工打造的内容：独立 zine 与出版物、音乐/艺术品牌、创作者作品集、小批量手作发布、社区演示。对想要孔版印刷温暖感而非数字光鲜的科技、研究或商业演示而言，也是低调黑马之选。
- 避免：要求数字原生光鲜或快节奏现代科技能量的场景：分层 zine 美学刻意保留手工感。

## 视觉速览

一套孔版印刷 zine 编辑系统，铺在暖卡其纸上，配深森林绿点缀色与墨黑结构。展示字体用 Bebas Neue（压缩工业无衬线、大写、宽字距）；正文字体用 Space Grotesk 字重 300–500；手写强调用 Caveat。每页幻灯片上叠一层细微 SVG 颗粒，强化印刷纸张感。美学借鉴独立出版社、世纪中叶行动主义海报与 DIY zine 文化：略微旋转的印章印记、拼贴版式里的美纹纸胶带、段首大字下沉，以及纸叠纸的偏移阴影。效果是手工印刷的编辑风：温暖而有纪律，自信而有触感。

Retro Zine 是一套孔版印刷 zine 编辑系统，铺在暖卡其画布（{colors.bg}，#C8B99A）上，深森林绿（{colors.green}，#008F4D）作为有意义的点缀色，墨黑（{colors.black}，#1A1A1A）作为结构色。美学借鉴独立出版文化、世纪中叶行动主义海报与 DIY zine 版式：压缩工业展示字体、手写强调、略微旋转的印章、美纹纸胶带拼贴印记、段首下沉大字，以及把每片表面系回印刷纸张语域的印刷颗粒叠加。

## 预览要素

- Palette：bg #C8B99A; bg-dark #B8A98A; green #008F4D; green-light #00A85D; black #1A1A1A; white #F4EFE6
- Typography：完整设计文档在选定后阅读。
- Signature move：暖卡其纸张画布（{colors.bg}）+ 深森林绿点缀色（{colors.green}）+ 墨黑结构（{colors.black}）。
- Signature move：SVG 颗粒叠加（{components.grain-overlay}）以 0.07 不透明度盖在每页幻灯片上，强化印刷纸张语域。
- Signature move：每个展示时刻用 Bebas Neue 大写加字距；正文用小字号 Space Grotesk；手写强调用 Caveat。
- Signature move：3px 实线黑结构边框分隔区域；2px 与 1.5px 边框做次级划分。
- Signature move：纸叠纸偏移卡片：绿色厚板通过 ::before 垫在白卡片后方 12px 处。

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
