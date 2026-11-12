> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/export-registry.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 导出块注册表（`--registry`）

为一个可追溯块分解图的 `data-block-*` 元数据生成机器可读的 `.registry.json` 伴随文件。**仅限手动触发：绝不无提示自动运行，且只在 `--registry` 时运行。**

## 触发条件

在以下情况加载本文件：

- 用户调用 `/diagram-design:export-diagram <html-file> --registry`（单独使用，或与 `--svg-only`/`--png-only`/`--scale`/`--output` 组合）。
- 用户用自然语言索要某个可追溯块分解图（见 [`semantic-patterns.md` § 8](semantic-patterns.md)）背后的块元数据、ID 列表、注册表或追溯数据，且要的是结构化数据而不是一张图。

本参考只管辖 `--registry`。SVG/PNG 栅格化是另一套流程，见 [`export.md`](export.md)。两者可以在同一次命令调用中运行，但不共享任何逻辑；把这一套当作独立流程，而不是那一套的扩展。

## 范围

注册表捕获的恰恰是源 HTML 的 `data-block-*` 属性中已经写下的内容（定义见 [`semantic-patterns.md` § 8](semantic-patterns.md)），仅此而已。它是**投影，不是第二个事实来源**：JSON 里的每个值都必须能追溯到文件中字面存在的某个属性值。本流程绝不根据图面文字、节点位置或自身判断去推断、概括或补充某个块的记录。

只适用于使用可追溯块分解模式（携带 `data-block-id` 的 Tree 节点）的图。任何其他图（包括未使用该模式的普通 Tree 图）没有块可提取，见*边界情况*。

## JSON schema

```json
{
  "source": "example-tree-block-decomposition.html",
  "blocks": [
    {
      "id": "PAY-001",
      "name": "Payment Gateway",
      "output": "Settled transaction record",
      "constraint": "Every transaction reaches exactly one terminal state",
      "impl": "src/payments/gateway/"
    },
    {
      "id": "PAY-001-01",
      "parent": "PAY-001",
      "name": "Card Authorization",
      "input": "Raw card details from checkout",
      "output": "Authorization token or decline",
      "constraint": "Never persists a raw card number",
      "assumption": "Runs behind the PCI-scoped boundary",
      "impl": "src/payments/authorization/"
    }
  ]
}
```

- `source`：注册表所源自的 HTML 文件名（basename）。
- `blocks`：每个携带 `data-block-id` 的节点一条记录，按文档顺序：即匹配节点在源文件中出现的顺序，绝不按父节点重排。按行逐条书写的树（先写完每个 Tier 1 节点，再写每个 Tier 2 节点）就按行的顺序导出；只有按深度优先书写的树才按深度优先导出。
- `id`、`name`：始终存在；该模式中每个块都要求这两个属性。
- `parent`：仅非根块存在，对应 `data-block-parent` 自身"缺省即根"的约定。根块省略该键，绝不写 `null`。
- `input`、`output`、`constraint`、`assumption`、`impl`：仅当该节点上存在对应的 `data-block-*` 属性时存在。宁可整个省略键，也不写空字符串。

没有其他键，也没有生成时间戳：注册表的设计意图是按需重新生成、在版本控制中做 diff，一个实时时钟字段会让对同一源文件的两次运行产生不同输出。来源与时间信息来自 git 历史，不来自文件自身内容。

## 流程

1. 读取源 HTML 文件。
2. 找出每个携带 `data-block-id` 属性的元素。没有该属性的节点不属于该模式：静默跳过，包括在混合了模式节点与非模式 Tree 节点的图中。
3. 对每个匹配节点，读取 `data-block-id`、`data-block-parent`、`data-block-name`、`data-block-input`、`data-block-output`、`data-block-constraint`、`data-block-assumption`、`data-block-impl` 中存在的那些。`data-block-name` 映射为 JSON 键 `name`；其余去掉 `data-block-` 前缀即可。
4. 属性值逐字保留：除去除去首尾空白外不做修剪，不改大小写，不重新格式化 `impl` 路径。
5. 按上文 *JSON schema* 所定义的文档顺序组装 `blocks` 数组。
6. 写到源文件旁边的 `<basename>.registry.json`（如 `example-tree-block-decomposition.html` → `example-tree-block-decomposition.registry.json`）。若用户在父导出命令中提供了显式 `--output` 路径，则遵从之。

## 边界情况

- **源中没有任何 `data-block-id` 属性**：拒绝并告知用户；不要写出一个空的 `{"blocks": []}` 文件。这很可能是在一张根本没用该模式的图上请求了 `--registry`，要这样说出来。
- **`data-block-id` 值重复**：按文档顺序输出每条匹配记录；不去重、也不挑一条。重复 ID 是正确性问题，该由 `scripts/verify-block-registry.py` 去抓，不该由导出悄悄解决。
- **`data-block-parent` 指向文件中不存在的 ID，或父引用成环**：按原样输出数据，包括断裂或循环的引用。理由与重复 ID 相同：导出镜像源文件；`scripts/verify-block-registry.py` 才是结构检查，运行它是独立的显式步骤，不是 `--registry` 自带的含义。
- **源是 `assets/index.html`**（画廊）：拒绝，与 SVG/PNG 路径相同，追问具体是哪张图文件。
- **`--registry` 与 `--svg-only` 或 `--png-only` 组合**：输出相互独立，在请求的栅格/矢量格式之外额外产出注册表 JSON。`--registry` 与 `--scale` 没有交互；它不产出图片。

## 它永远不做的事

- 校验 ID 唯一性、父解析或环。那是 `scripts/verify-block-registry.py` 的事：作为独立步骤运行，不是导出附带的。
- 把块的元数据与其绘制位置或连接线几何做关联。这完全不在注册表的范围内，不是"延后"：JSON 是元数据投影，不是几何审计。
- 写入生成时间戳、工具版本，或任何不是字面来自 `data-block-*` 属性的字段。
- 修改源 HTML。
- 在未显式传入 `--registry` 时自动产出 `.registry.json`。每次调用都要手动，与 SVG/PNG 导出一致。
