> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/retro-windows/preview.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Retro Windows 预览卡

本文件仅用于标题页（title slide）预览。若要生成完整演示文稿，请阅读下方列出的完整设计文档。

## 文件

- 完整设计文档：`bold-template-pack/templates/retro-windows/design.md`
- 预览卡：`bold-template-pack/templates/retro-windows/preview.md`

## 选型元数据

- Slug：`retro-windows`
- Tagline：Windows 95 界面装饰：灰色标题栏、MS Sans Serif、像素排印、满满怀旧感。
- Mood：nostalgic、retro、geeky、playful
- Tone：winking、nostalgic、geeky、fun
- Formality：low
- Density：medium
- Scheme：light
- 适合：一切应当显得心照不宣地怀旧的内容：复古游戏、Y2K 美学品牌、带 90 年代气息的创作者作品集、科技史讲座、刻意戏谑的演示。凡是俏皮的复古梗本身就是全部意义的地方，它都是佳选。
- 避免：需要读起来现代、优雅或有机构可信度的演示文稿：Win95 界面装饰永远像戏服。

## 视觉速览

一套把 Windows 95 / 98 桌面操作系统美学渲染成演示系统的设计。每页幻灯片都是一扇窗口：斜面装饰、海军蓝渐变标题栏、MS Sans Serif 正文字体，图表区、组合框与面板的排布一如 1995 年的软件 UI。配色是原版 Win9x 系统色（灰色按钮面、海军蓝标题栏、白色下陷输入框），复古点缀色相（DOS 绿、砖红、芥末黄、青绿）只留给状态文字与图表数据。像素字体（Press Start 2P）与终端字体（VT323）克制地出现，充当怀旧标点。效果一半是俏皮怀旧，一半是功能仪表盘：整套演示读起来像运行在 CRT 显示器上的软件产品。

Retro Windows 是把 Windows 95 / 98 桌面操作系统美学渲染成幻灯片模板的设计。每页幻灯片都构造成一个 win-window：带海军蓝渐变标题栏的斜面矩形装饰、右上角三个按钮图标（_, [], X），以及承载应用式内容的主体区域。构图理念是"这页幻灯片是运行在 1995 年桌面上的软件，内容就是软件显示的东西"。设定是彻底的：没有现代演示意义上的幻灯片标题，只有伪装成文件名的窗口标题（README.DOC、DATAVIEW.CSV、METRICS.LOG）。

## 预览要素

- Palette：bg-gray #C0C0C0; bg-light #D4D0C8; bg-dark #808080; white #FFFFFF; black #000000; text-dark #222222; blue-navy #000080; blue-bright #0000A0
- Typography：MS Sans Serif
- Signature move：每页幻灯片都是一个 {components.win-window}：斜面装饰配海军蓝渐变标题栏与三个系统按钮（_, [], X）。
- Signature move：固定周期的 3px CRT 扫描线叠加（{components.crt-overlay}），以 3% 不透明度盖在所有内容之上。
- Signature move：基于斜面的深度：凸起（{components.panel-raised}、{components.btn-retro}）与下陷（{components.panel-sunken}、{components.group-box}），不用模糊阴影。
- Signature move：字体栈是 MS Sans Serif / Segoe UI / Tahoma 回退，Press Start 2P 与 VT323 充当怀旧点缀。
- Signature move：状态色（绿/红/黄/青）承载语义：绿 = OK，红 = 警告，黄 = 中等，青 = 第三级数据。

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
