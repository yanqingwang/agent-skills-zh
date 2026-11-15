> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/scatterbrain/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Scatterbrain 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/scatterbrain/design.md`
- 预览卡：`bold-template-pack/templates/scatterbrain/preview.md`

## 选型元数据

- Slug：`scatterbrain`
- Tagline：便签贴启发：粉彩便利贴、Caveat 手写体、Shrikhand 与 Zilla Slab 字体栈。
- Mood：playful、creative、warm、messy-on-purpose、workshop
- Tone：informal、warm、expressive、human
- Formality：low
- Density：high
- Scheme：light
- 适合：一切应当像设计师白板的内容：头脑风暴、工作坊、创意代理商资历介绍、设计思维研讨、构思提案、艺术指导评审。对任何想要呈现进行时思考而非抛光结论的演示文稿（包括科技、研究或商业）同样有趣。
- 避免：要求精准与机构分量的场景：便签贴美学刻意呈现温暖与未完成感。

## 视觉速览

一套便签贴加软木板演示系统。每个内容块都是贴在带纹理纸张或软木表面上的彩色便利贴，层层叠加红色图钉、美纹纸胶带与装饰涂鸦。展示字体用 Shrikhand（厚实的装饰展示衬线）承担每个标题；正文字体用 Zilla Slab（亲切的粗衬线）；手写强调用 Caveat。配色是粉彩便签色（黄、蓝、粉、绿、橙、紫），铺在米白纸/软木/暖渐变背景上。美学借鉴创意工作坊墙面艺术、头脑风暴板与独立工作室情绪板：散落的轻微旋转、每页多种背景纹理变体、图钉/胶带/投影组合。效果是温暖、游戏感与可触的创作过程能量。

Scatterbrain 是一套便签贴加软木板演示系统。每个内容块都是一张彩色便利贴（{components.post-it}），分层贴到三种带纹理背景变体之一（软木板、桌面纸或暖渐变）上，红/蓝/绿/金图钉把便签钉住，有时再叠上半透明美纹纸胶带。视觉隐喻是彻底的：整套演示是一面创意工作坊墙、一块头脑风暴板或一张思考者的书桌，内容就是钉满其上的便利贴群。

## 预览要素

- Palette：yellow #FFE066; yellow-deep #FFD43B; blue #A5D8FF; blue-deep #74C0FC; pink #FFC9C9; pink-deep #FF9F9F; green #B2F2BB; green-deep #8CE99A
- Typography：完整设计文档在选定后阅读。
- Signature move：三种带纹理背景变体：软木（{components.bg-cork}）、纸张（{components.bg-paper}）、暖渐变（{components.bg-warm}）。每页选其一。
- Signature move：固定 4% 不透明度的 SVG 颗粒叠加盖在所有内容之上，强化纸张语域。
- Signature move：七种便签色：黄、蓝、粉、绿、橙、紫、白边。每种以渐变填充（橙/紫/白除外）。
- Signature move：每张便签带柔和投影 + 小旋转。相邻便签的旋转方向交替。
- Signature move：红色图钉（另有蓝/绿/金变体）用 ::before 实现，美纹纸胶带用 ::after 实现。两者常叠加在同一张便签上。

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
