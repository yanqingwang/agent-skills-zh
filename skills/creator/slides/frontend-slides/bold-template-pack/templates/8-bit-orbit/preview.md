> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/bold-template-pack/templates/8-bit-orbit/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 8-Bit Orbit 预览卡

本文件仅用于标题页预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/8-bit-orbit/design.md`
- 预览卡：`bold-template-pack/templates/8-bit-orbit/preview.md`

## 选型元数据

- Slug: `8-bit-orbit`
- Tagline: 深海军蓝虚空之上的像素霓虹街机美学。
- Mood: 复古科技、俏皮、赛博朋克、有活力
- Tone: 极客、霓虹、叛逆、科幻
- Formality: 低
- Density: 中
- Scheme: 深色
- Best for: 一切该有凌晨两点 CRT 屏幕质感的内容：赛博朋克、游戏、web3、独立开发工具、黑客松演示。同样适合想突出怀旧数字工艺的技术演讲、合成波品牌演示，或想做出主机开机感的创意评审。
- Avoid for: 深色霓虹配色会直接与信息相抵触的场合：安静的机构财务披露、面向患者的医疗材料、传统奢侈品。

## 视觉速览

一套复古未来主义像素艺术演示系统，把 16-bit 街机怀旧与编辑排印的克制揉在一起。展示字体用 Tektur（基于像素网格逻辑的粗几何展示字面），正文配 Chakra Petch，代码味标签与表格数据用 Space Mono。配色以深宇宙海军蓝（#0F1B3D / #0A0E27）为轴，由三种饱和霓虹点亮：青色、亮粉、高明度黄，另有柔和薰衣草浅彩作暖调缓冲。层次来自以 4px 为增量堆叠的硬边偏移阴影（像素单位）、CRT 扫描线、氛围颗粒、暗角与动态星空。效果介于街机机柜与《创》时代会议室之间：数字感明确，刻意低保真，像是刚开机启动。

8-Bit Orbit 是一套复古未来主义像素艺术演示系统。其底层前提是 4 像素单位：每一处阴影偏移、每一条边框、每一个角标、每一个标签高度都收敛到 4px 的倍数。布局像是在老 CRT 上栅格化后拖进 HTML，而氛围叠层（扫描线、颗粒、暗角辉光、动态星空）在每一处表面强化这种错觉。

## 预览要素

- Palette: dark-void #0A0E27; deep-navy #0F1B3D; neon-cyan #5EDCF4; neon-pink #F0A6CA; neon-yellow #F4D03F; soft-lavender #E2D5F2; white #FFFFFF
- Typography: 选定后阅读完整设计文档。
- Signature move: 三字体栈：Tektur（展示）、Chakra Petch（正文）、Space Mono（HUD/标签），不得替换，也不得越出各自角色混用。
- Signature move: 海军蓝底（{colors.dark-void} / {colors.deep-navy}）与彩色网格表面（粉、青、薰衣草）交替出现，两者都带 40px 蚀刻网格。
- Signature move: 三种霓虹（青、粉、黄）只留给展示文字、数字、分隔线与标签填充，绝不用于正文。
- Signature move: 一切尺寸对齐 4px 像素单位：边框 2-4px、阴影偏移 4px / 8px、角标 24×24 配 4px 描边。
- Signature move: 堆叠的硬边偏移阴影是这套系统的纵深语言，绝不模糊；文字阴影也不上色，唯一的例外是黄到海军蓝的级联。

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
- 永远不要在页面上放置用户需求备注（如期望气质、受众、内部使用标签），除非用户明确要求这些字面词出现在演示中。
- 可见边框装饰只使用真实演示内容：演示标题、真实的分节标题、日期、作者、公司、页码，或来自用户材料的真实内容短语。
- 生成预览时不要读取 `template.html`。
- 不要读取其他模板的 `design.md` 文件。
- 在用户为完整演示选定本模板后，先阅读完整设计文档再生成最终幻灯片。
