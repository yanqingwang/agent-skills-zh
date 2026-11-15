> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/component-review.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 计划与资产审查

在以 comp（设计稿）为先导的构建中，一旦每个光栅区域都有了它的 plate（贴片）且 plates 闸门已为它们评分、而任何页面代码尚不存在时，使用本检查点。已批准的 comp 是参照物。用户审查两样东西：将要交付的 plates，以及其余部分的生产计划，即哪些区域由代码绘制。"画出来的区域被计划成代码"是以 comp 为先导的构建中最昂贵的错误，而这正是用户抓住它的地方。文本、控件和界面镶边（chrome）留到组装出的首个视口中评判。

## Plan, capture, serve

运行 `.claude/skills/impeccable/scripts/impeccable component-review plan`。它会依据测量得到的规格、comp 和 plate 文件写出 `.impeccable/review/components.json`；只要任何光栅区域还缺 plate，它就拒绝执行并逐一报出名字。在本阶段绝不要亲手写或改那个文件：该数据包是从规格派生的，一切修改都应落在 regions 文件里。

如果 Harness 暴露了 `component_review`，调用它并把 `manifest_path` 设为 `.impeccable/review/components.json`。宿主会完成截图、呈现审查并返回用户的决定。一个被挂起的请求是在等待用户，它不是构建失败，也不是批准。

否则运行 `.claude/skills/impeccable/scripts/impeccable component-review capture --manifest .impeccable/review/components.json`，然后在后台启动 `.claude/skills/impeccable/scripts/impeccable component-review serve --session <returned session>`。在可用浏览器中打开它打印的 URL 并等待用户；用户提交后 `serve` 以 0 退出。用 `.claude/skills/impeccable/scripts/impeccable component-review status --session <id>` 读取决定；`.claude/skills/impeccable/scripts/impeccable component-review verify --manifest .impeccable/review/components.json` 确认批准，并对 pending、needs-work 和过期输入予以拒绝。绝不要替用户提交页面或写回执。

`serve` 在本会话没有浏览器时以 2 退出（与决策页相同的信号），在闲置 30 分钟无决定而关闭时以 4 退出。无论哪种，都没有人在审查：停止等待，不要自行批准任何东西，也不要越过本检查点继续构建。结束本次运行，并把计划与资产审查连同其会话 ID 一起报告为 pending，让用户可以恢复。一个等待中的审查是未完成的工作，不是已完成的构建。

## 依据回执行动

按用户给出的决定执行，绝不用你自己的"好评"取而代之。

- **approve**: 所有条目都获批准且清单得到确认后，进入 hero（首屏）。
- **revise**（针对 plate）：按用户的反馈在同一路径重新生成该 plate。
- **revise with split**（针对资产）：在 regions 文件中把该区域替换为它的图层：一个带透明开口的 frame plate（kind 为 `plate`，盒子相同）、开口盒子处作为独立 `image` 区域的内容，以及每个会动的部件（百叶、门）各作为一个 plate。每个图层按原区域命名，如 `<id>-frame`、`<id>-view` 或 `<id>-shutter-left`，这样下一轮会把它显示为用户请求的一部分。重跑 `.claude/skills/impeccable/scripts/impeccable comp-spec --comp <comp.png> --regions <regions.json>` 并产出 plates。
- **revise**（针对计划项）：按反馈修改 regions 文件（调整某个光栅区域的尺寸或扩展它、把材质拆成独立的 plate 区域、或调整代码区域），重跑 `.claude/skills/impeccable/scripts/impeccable comp-spec --comp <comp.png> --regions <regions.json>`，并产出任何新的 plates。
- **reclassify**（针对代码区域）：在 regions 文件中把该区域的 `kind` 改为用户选择的那种，并重写它的 `note` 以描述材质。重跑 `.claude/skills/impeccable/scripts/impeccable comp-spec --comp <comp.png> --regions <regions.json>`，然后产出新 plates；子代理可用时使用资产生产者。
- **missing**: 把该区域加入 regions 文件，重跑 `.claude/skills/impeccable/scripts/impeccable comp-spec --comp <comp.png> --regions <regions.json>`，若它是光栅则产出其 plate。

然后再次运行 `plan`、`capture` 和 `serve`。未改变的决定会被沿用，用户只会看到变化的部分。任何规格变更，或验收后又被替换的 plate，都需要新一轮；构建阶段闸门保持关闭，直到当前规格的审查被接受。

## 组装与审查

用已批准的 plates 和计划构建首个视口，并运行 hero 闸门。人工审查不能豁免其完整性检查。hero 尝试失败三次之后，或在任何首个视口被接受之前响应式尝试失败三次之后，停止迭代，带着当前构建呈现首屏审查；用户的眼晴来裁决读数裁决不了的事。

在 `.impeccable/review/hero.json` 呈现第二份清单（manifest）。这份由你来写，其形状是固定的：

```json
{
  "schemaVersion": 2,
  "stage": "hero",
  "id": "hero",
  "title": "First viewport",
  "comp": {"path": ".impeccable/mocks/comp.png", "width": 1536, "height": 1024},
  "components": [{
    "id": "first-viewport",
    "name": "First viewport",
    "medium": "HTML / CSS",
    "note": "Assembled first viewport",
    "box": {"x": 0, "y": 0, "w": 1, "h": 1},
    "preview": {"kind": "page", "path": "index.html"},
    "dependencies": ["styles.css", "assets/plates/sky.png", "fonts/display.woff2"]
  }]
}
```

- `schemaVersion` 为 2。版本 3 是计划审查数据包，要求 stage 为 `components`。`codeRegions` 与 `specSha256` 只存在于版本 3，在此会被拒绝。`reviewGroup` 也被拒绝：版本 3 一律拒绝它，其他版本只在 `components` 阶段清单的页面预览上接受它，绝不在 hero 清单中接受。
- `comp.path` 是 `.impeccable/build/spec.json` 中的 `comp` 值，`width` 与 `height` 是该 PNG 的像素尺寸。
- 恰好一个组件，`box` 恰好为 `{"x": 0, "y": 0, "w": 1, "h": 1}`，`name`、`medium` 与 `note` 为字符串。
- `preview.path` 是构建闸门检查的页面入口（`.impeccable/build/state.json` 中的 `artifact`）。
- `dependencies` 以裸字符串列出页面加载的每个其他文件（样式表、脚本、plates、图片、字体）。这里和上面的每个路径都是项目相对的纯路径：不以 `./` 或 `/` 开头，没有 `..`，没有 URL，没有 `?`、`#`、`%`、`:` 或反斜杠。对清单外文件的请求，或对其他主机的请求，都会使截图失败。

参照物仍是已批准的 comp。调用同一个宿主审查工具，或用这份清单运行 `capture`、`serve` 和 `verify`。needs-work 反馈会开启又一轮组装。

验收为本此构建关闭人工审查：绝不再请求计划、资产或组装的批准。只要页面呈现的是用户接受的样子，hero 分数、调色板检查和所有数值读数都只是建议；实质性否决仍然有效（缺失或未被引用的 plate、SVG 插画、有机剪裁、被裁切的 plate、凭空杜撰的墨迹、渲染存在性检查失败）。被接受的截图中同样没有的文本、控件或镶边区域，由验收一并了结；截图中缺失的 plate 则是一个要问用户的问题，闸门的理由会把它写明：不要自作主张偏离用户接受的内容，而要执行他们的答复，包括放置该 plate。当截图不再匹配被接受的截图时，恢复用户所接受的样子；在此之前这些读数继续适用。以被接受的首屏为视觉方向完成页面其余部分、响应式行为、收尾检查与文档。这是首屏校准，不等于声称用户审查过页面其余部分。共享样式表的编辑不会重开批准。保持被接受的方向；用户此后明确提出的变更是新任务。

组装页面的截图会内联执行来自固定输入的已声明本地脚本。网络 API、frame 与 worker 均不可用；首个视口必须在截图前稳定下来。保留真实页面并声明其脚本，而不是为了让审查通过而删掉行为。
