> **中文汉化版** · 上游：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) · 原文件：`references/print.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 可打印图版（A4）

完成的图（figure）还可以打印：一份 A4（或 US Letter）PDF，在纸面上讲解这台机器，取材于与实时图相同的页面和同一个模型。只有当用户要可打印的东西时才做：讲义、海报、PDF、A4 或 Letter 图版、教室墙上或活页夹里的资料。

`scripts/print.mjs` 负责这件事。它在无头 Chrome 中打开构建好的 light 页面，播放你列出的姿态，并把每个姿态定格为矢量 SVG（WebGL 图层存为 2× PNG）。然后它把静帧按三种格式之一排版，并用 Chrome 打印 PDF。

```bash
node scripts/print.mjs examples/raptor-engine/sheet.mjs                 # poster, A4
node scripts/print.mjs examples/raptor-engine/sheet.mjs --format all --png
node scripts/print.mjs examples/arcade-cabinet/sheet.mjs --format detailed --letter
```

它会把 `<out>-<format>-a4.pdf` 和 `.html` 写在规格文件旁边（`--letter` 时为 `-letter`），加 `--png` 时另有预览 `.png`。当某个格式超出其页数上限时，以 1 退出。

## 三种格式

| 格式 | 页数 | 版面上有什么 | 适用场景 |
|---|---|---|---|
| `poster`（默认） | 1 | 大字号的名称，问题与一段简短导语，一列大数字，带编号图钉的图，然后是每个部件及其一句话说明 | 贴墙、封面页、第一眼 |
| `drawing` | 1 | 带编号的工程图版头，带图钉的图，零件清单，规格表，另一姿态的小幅内嵌图，然后是一条步骤长条，工作中被点亮的部件 | 技术讲义 |
| `detailed` | 2 | 第 1 页：带图钉与字母标注特写记号的图，问题、导语、数字、每个部件及其一句话，图下方的圆形特写。第 2 页：每个步骤为一大幅被点亮的静帧，配两三句话、原因说明与规格表 | 作业、活页夹、想彻底弄懂它的人 |

三种格式都极简，黑白打印效果好：发丝级细线，文字只用一款无衬线体，mono 大写仅用于标签，黑色图钉，白纸上的 light 主题图。

## 规格（spec）

图版是示例旁边的一个模块 `sheet.mjs`，其默认导出声明了页面在哪、捕获什么、写什么文字。其中的每个数字和句子都必须来自图的模型或图注，与图本身遵守同一条真实规则。

```js
export default {
  page: "raptor-engine-light.html",             // the built light page, relative to this file
  out: "raptor-engine",                         // output base name
  layers: ".rp-stage > svg.rp-back, .rp-stage > svg.rp-front", // the SVG layers to freeze, back to front
  rasterSelector: ".rp-stage",                  // the box that WebGL shots are cropped from
  strip: [".rp-deckglow"],                      // elements to drop from every still
  reduced: true,                                // emulate reduced motion (calm, no tour); false to catch animation
  views: {                                      // poses, captured in this order, each after its actions
    rest: {},
    apart: { actions: [["key", " "], ["wait", 2500]], reset: [["key", " "], ["wait", 2500]] },
    firing: { actions: [["key", "i"], ["wait", 3500]], raster: { region: [250, 150, 432, 530] } },
  },
  name, title, number, tagline, question, lead, quote,
  numbers: [["230", "tf", "thrust at sea level"]],
  spec: [["Chamber", "300 bar"]],
  why: { title: "Why full flow?", text: "…" },
  parts: [{ id: "otp", name: "Oxygen turbopump", say: "…", select: '.it[data-piece="otp"]', at: [x, y] }],
  main: { view: "apart", crop: [x, y, w, h], layers: [1], hide: ["stand"] },
  inset: { label: "Assembled", view: "rest", crop: [x, y, w, h] },
  steps: [{ view: "apart", title: "…", text: "…", focus: ["otp", "ftp"] }],
  details: [{ title: "…", text: "…", around: ["otp"], focus: ["otp"] }],
};
```

- **Actions** 是 `drive.mjs` 的动作。先 `["slow", 0.03]` 再 `["until", js]` 可以精确抓到动画的某个瞬间（街机落币槽里的硬币）；`reset` 把页面恢复到下一个 view 之前的状态。
- **Parts** 是对实时 SVG 的 CSS 选择器，所以任何图都适用：Raptor 的组件是 `.it[data-piece]` 分组，街机的是来自其 recorder 名称的 `[data-name^="mech"]` 前缀。没有 `name` 的 part 不会被列出或打钉，但 steps 仍可点亮它（`coin`）或隐藏它（`stand`）。图钉位于该 part 最大形状的中心；当落点在空白处时，用 `at`（viewBox 单位）指定。彼此拥挤的图钉会散开，并画一条发丝细线指回各自的点。
- **Focus** 点亮列出的 part（黑色线条），其余一律变灰，无论有无标签。**Hide** 把某个 part 从该静帧中移除：隐藏挡在特写前面的东西（街机中挡在机括前的投币门）。
- **Crops** 使用图的 viewBox 单位。不指定时，主视图裁到其绘制内容；steps 与特写围绕各自的 focus 或 `around` part 裁切，且绝不小于主裁切宽度的 42%。
- **Rasters** 只用于 WebGL。把 view 标记为 `raster` 并给出要拍摄的 viewBox `region`；羽流会以 2× PNG 的形式印在矢量页面内。
- **Text** 必须放得下：steps 的标题不超过五个词，每个 part 一行，每个 step 两三句话。当某个格式挤到下一页时，脚本会失败。

## 检查成品

1. 先构建 light 页面（`node build.mjs --light`）。
2. 用 `--format all --png` 运行并逐张查看 PNG。留意：打在空白处的图钉、特写展示了错误的部件、被点亮的部件藏在另一个部件后面、页面底部被切断的文字。
3. 把 PDF 或 HTML 放大到 4 倍检查（在 `<name>.html?print` 上用 `drive.mjs` 的 `["shot", out, ".ps", 4, [x, y, w, h]]`）：线条必须是矢量且清晰锐利，被点亮的部件在 step 静帧的尺寸下必须醒目。
4. 可以的话真的打印一页。浅灰的暗面与发丝线在办公室激光打印机上必须仍然可读。

## 图上的 PDF 链接

`kit/pdf-button.mjs` 导出 `pdfButton(href)`：卡片右上角一个带图标的小"PDF"链接，自带 CSS，所以没有它的页面不受影响。把它放在 plate body 内的第一个位置，且只在文件确实存在时使用（`examples/push-button/build.mjs`）。顺序：先构建 light 页面，再打印，然后重新构建让按钮出现。

## 更长的 detailed 图版

`detailed` 可运行 2–4 页，由规格决定：

1. 总览（必有）：带图钉的图、数字、每个部件一句话、圆形特写（`details`）。
2. 工作原理：每页六个 steps，`why` 占最后一格；更多 steps 溢出到下一页。
3. 组件（规格含 `assemblies` 时）：每页最多四个，每个 `{ title, text, parts: [ids] }` 画成大幅被点亮的特写，带自己的图钉与零件编号。有十个以上部件的图给三或四个分组。
4. 规格表收尾最后一页。

`maxPages`（2–4，默认 4）限制页数：组件页最先被裁掉，而 steps 超出上限就是错误。`examples/raptor-engine/sheet.mjs`（3 页）是参照；`push-button` 与 `arcade-cabinet` 保持 2 页。
