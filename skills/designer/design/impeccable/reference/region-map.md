> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/region-map.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 区域映射（Region map）

区域映射在素材生产之前，点名已批准设计稿中实际可见的内容。它不是页面构建，也不是素材批准。

1. 运行 `.claude/skills/impeccable/scripts/impeccable comp-spec --comp <comp.png> --grid`，打开原图与加了网格的图。
2. 运行 `.claude/skills/impeccable/scripts/impeccable comp-spec --schema` 查看 JSON 字段。写出带 `regions` 数组的 `regions.json`。每个区域需要一个稳定的 `id`、`kind`、`note`，以及 `pixelBox`、归一化 `box`、`grid` 三者中的恰好一个。尺寸用原设计稿的尺寸。
3. 运行 `.claude/skills/impeccable/scripts/impeccable comp-spec --comp <comp.png> --regions regions.json --inspect-map`。输出指向一份报告、叠加层、精确裁剪，以及带掩膜参照的 `COMPARE` 对比页。默认打印发现；`--json` 打印完整报告，对比页路径在 `comparisonSheets`。
4. 先打开对比页，把受影响的裁剪放在一起检查；需要更多细节时再打开单个裁剪。把它们的边界与原图对照。几何错误要查，被排除的前景像素也要查。每个重叠的非容器代码框都被完整掩膜，包括框内空白。分离的文本元素各自单独定框，让间隙里的图形保持可见；容器描述的是它们的版面范围，绝不取代其子元素。修正映射后再次检查；每次使用新的输出目录。零错误不等于裁剪准确。覆盖率警告只是提示，不是完整性的证明。

如果请求止步于映射，就带着映射、检查报告和未解决的发现停下。要继续构建，用 `comp-spec --comp <comp.png> --regions regions.json` 量测这份检查过的映射，并遵循 [new-work.md](new-work.md)。

`--auto` 产出的是水平条带脚手架，不是元素识别。它是可选项，替代不了手写映射。

## 包含关系

`parentId` 指向一个包住它的 `container: true` 区域。父与子各自保留独立的 ID 与裁剪。包含关系不转移批准。

## 独立变化的维度

按独立变化的维度切分区域：站点会替换的内容（房间照片、产品、人物）、运动部件（hover 或签名交互会动的任何东西）、结构（框、边框、装饰）。一扇百叶敞开、望进房间的窗是三种区域：外框作为带透明开口的图版，房间作为其下的图像区域，每扇百叶各是一个图版。重叠区域由页面合成。`comp-spec` 会标记 note 同时点名框与其透出画面的光栅区域（`baked-composite`），计划与素材审查会先把它拿给用户看。

## 画出来的材质

量测时，`comp-spec` 会标记裁剪看起来是画出来的 `text`、`control` 或 `chrome` 区域（容器也包括在内），标记为 `painted-pixels`（色彩多、渐变软），并在其汇总中列出。计划与素材审查会先把被标记的区域，以及标记为 `codeDrawn`（你选择用代码画出来的绘画材质）的区域拿给用户看。不要把兜底留给他们：某区域是绘画材质（一个人物、一张照片、金属或纸面）时，现在就把它归类为 `plate`、`image` 或 `texture`。

设计稿裁剪只是参照证据，绝不是生产素材。映射检查器会把它的 PNG 标记为 comp-derived。
