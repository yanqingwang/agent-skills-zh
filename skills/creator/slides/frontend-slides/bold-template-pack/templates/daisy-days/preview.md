> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/daisy-days/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Daisy Days 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/daisy-days/design.md`
- 预览卡：`bold-template-pack/templates/daisy-days/preview.md`

## 选型元数据

- Slug：`daisy-days`
- Tagline：欢快的粉彩演示文稿，配手绘雏菊、星星与彩虹。友好、柔软、温暖。
- Mood：cheerful、playful、warm、sunny、wholesome
- Tone：friendly、soft、encouraging、approachable、lighthearted
- Formality：low
- Density：medium
- Scheme：light
- 适合：一切应当显得友好、柔软、喜悦的内容：教育内容、儿童与家庭、健康计划、社区工作坊、手作/插画创作者作品集。用于出人意料的俏皮内部启动会、婚礼策划演示，或任何以温暖为信息本身的场合也很讨喜，科技或商业语境亦不例外。
- 避免：受众明确期待权威与精准的场景：手绘粉彩 SVG 装饰与一丝不苟恰好处在反面。

## 视觉速览

一套欢快、童趣的演示系统，围绕厚实的展示字体 Fredoka One 与圆润人文无衬线 Quicksand 构建。配色是一座阳光花园：米白画布、青绿、柔粉、黄油黄、薄荷绿、薰衣草紫、蜜桃橙、天空蓝，外加单一珊瑚红点缀色，并用炭棕色 2D 轮廓包裹每个形状。深炭色硬偏移阴影、慷慨的圆角，以及手绘 SVG 装饰（雏菊、星星、太阳、云朵、彩虹），把美学锚定在儿童绘本跨页与贴纸页 kawaii zine 之间。

Daisy Days 是一套欢快童趣的演示系统，根植于单一的排印搭配：每个标题用圆胖圆润的展示字体 Fredoka One，每行正文与元数据文字用亲切的人文无衬线 Quicksand。视觉语言源自绘本插画与贴纸页 kawaii：每个形状带炭色 2D 轮廓，每个抬升元素投出实色偏移阴影，每片表面都是阳光花园配色中的一种粉彩。

## 预览要素

- Palette：cream #F5F0E6; turquoise #7ECDC0; soft-pink #F7C8D4; butter #FDE68A; mint #A8E6CF; lavender #D4A5E8; peach #FFCBA4; sky #A8D8F0
- Typography：完整设计文档在选定后阅读。
- Signature move：米白（{colors.cream}）默认画布，配轮换的粉彩表面：每页幻灯片可以选用不同的表面色。
- Signature move：所有标题/展示/引语文字用 Fredoka One；所有正文与元数据文字用 Quicksand 500/600。
- Signature move：每个形状与卡片带 3px 实线炭色轮廓（{colors.text-dark}）加硬偏移阴影（{shadows.default} 或 {shadows.small}）。
- Signature move：慷慨的圆角：标准卡片 20px，featured 卡片 28px，徽章用胶囊（{spacing.radius-pill}），圆点与头像为正圆。
- Signature move：手绘 SVG 装饰（雏菊、星星、太阳、云朵、彩虹）聚集在角落并裁出幻灯片边缘，作为氛围层。

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
