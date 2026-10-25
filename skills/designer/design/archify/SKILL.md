---
name: archify
description: "创建经验证（validated）的架构（architecture）、流程（workflow）、时序（sequence）、数据流（dataflow）、生命周期/状态（lifecycle/state）、ERD、类图（class）、树（tree）、时间轴（timeline）与瀑布图（waterfall），输出为可交互探索的独立 HTML，支持深/浅色主题、动态效果与图片/SVG/WebM 导出。接受需求描述或 Mermaid 输入；为基于代码的图表检查仓库证据。适用于可视化系统、API 调用、管道、schema、历史、时序，或日常的步骤、组成、关系与状态。当用户要求把答案做成页面（a page）、一页纸（one page）、讲解页（an explainer）或可分享的答案（做成一页, 用页面讲）时，还可将答案转成结论先行、带结构化面板、原生图表和图表的一页式讲解页（explainer）；当用户的规则以一行 [archify explainer: ...] 选择加入时也可主动制作。不适用于仪表盘（dashboard）。"
license: Apache-2.0
metadata:
  version: "3.2"
  author: tt-a1i
---

> **中文汉化版** · 上游：[tt-a1i/archify](https://github.com/tt-a1i/archify) · 原文件：`archify/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Archify

创建经过校验的独立 HTML，形式为原生图表，或回答某个问题的一页式讲解页（explainer）。

命令请从你的工作目录运行。除非用户指定其他位置，否则为每个新的产物请求在该目录下分配独立文件夹 `.archify/<type>-<slug>-<YYYYMMDD-HHMMSS>/`（本地时间，一次性选定）：将候选文件和 `<slug>.html` 放在其中，并在修复时复用该文件夹。原生图表使用 `candidate.json`，其 `meta.output` 相对于工作目录；explainer 可使用 `candidate.archify.md` 和可移植的输出文件名。后续请求会获得新文件夹。每条命令中的 `bin/archify.mjs` 都要替换为已安装包的绝对路径，或相对于你工作目录的路径；CLI 的输入输出路径均从该目录解析。

若要为真实代码库绘制原生图表，请在追踪所请求行为的同时阅读 [仓库绘制](references/repository-authoring.md)。系统描述使用下方的原生步骤；已冻结的候选文件走交接路径。

## 选择产物

- 当用户要求绘制或可视化系统、流程、schema 或历史时，使用原生图表和类型路由。
- 当用户要求把答案做成页面时使用 `explainer`：一个页面、一页纸、讲解页、可分享的东西（"做成一页"、"用页面讲"、"answer with a page"）。没有此类请求时，用文本回答或绘制所请求的图表。应请求制作的页面在回复结尾附上 Output 一节中的一行模式提议。
- 上下文中的规则行会改变这一点。`[archify explainer: proactive]`：对于需要表格、步骤或多个小节的解释、对比、权衡、决策、诊断、评审或计划，即使未被要求也额外制作页面。`[archify explainer: always-on]`：每个得出结论的回复都附带一个最多四个小节的紧凑页面，不主动打开它，以其链接收尾回复。`[archify explainer: on-demand]`：仅在被要求时制作，且从不提议模式。
- 在任何模式下，页面都需要一个有结构支撑的结论：闲聊、单行回答、原始命令输出以及纯文本请求都不制作页面。
- 使用 `explainer` 时，阅读 [Explainer 绘制](references/explainer-authoring.md) 了解其结论、理由、范围、面板布局和可选的原生图表。先写出完整草稿，再运行 `finalize explainer` 进行验证、原子交付和产物检查。局部内容修订使用面板补丁（panel patch）。

## 已有候选文件交接

当用户提供已冻结的候选文件时，先以单次 CLI 调用运行 `finalize`。其通过的回执即完成自动化门禁；在声称视觉质量达标前，按 Delivery 一节处理任何视觉审查建议。修复则遵循第 5 步。

`finalize` 的交付回执中包含一次有界的更新检查；参见更新感知（Update awareness）一节。

## 原生图表绘制

普通生成走此路径。仅在分支参考文件所述触发条件成立时才阅读它们。

1. 根据问题选择 `architecture`、`workflow`、`sequence`、`dataflow`、`lifecycle`、`erd`、`class`、`tree`、`timeline` 或 `waterfall`。
2. 使用 Type router 中给出的确切 schema 与示例路径，不要列目录。将 [绘制默认值](references/authoring-defaults.md) 与该模式的示例放在一个有边界的批次中读取，与项目文档和完整 schema 分开，以免任何一方被截断；写入前补读任何缺失的小节。Architecture 使用与之匹配的 showcase 示例。除 Architecture 外的每种模式，还要阅读该模式 schema 与公共 schema。在选择任何新字段、枚举或受限文本之前，先阅读相关 schema 定义，尤其是边界种类（boundary kinds）。示例教的是形状，不是事实。使用全新的 ID、措辞与布局。直接产出候选文件，不要先做帮助查询、doctor、入门验证、临时图表或输出路径列举。仅当用户明确要求某个品牌标识时才查询品牌；对带有用户提供 URL 的未知标识，阅读 [品牌标识](references/brand-marks.md)。
3. 在覆盖了所请求的范围，以及（对真实代码库而言）[源码证据](references/repository-authoring.md)之后，直接写出完整候选文件，不要用散文规划坐标。在确定坐标之前，先依据绘制默认值选择 Architecture 的抽象层级与连通布局：呈现主要用户旅程和必要分支，保留控制角色与改变行为的条件，并为实际关系标签留出足够空间。任何节点、关系、来源、视图、卡片或边界的数量都不是目标或上限。优先使用自动布线；只有必要的分支、返回、既定几何或经测量确认的修复才添加显式布线。除非用户要求密集的 `standard`，否则将 `meta.quality_profile` 设为 `"showcase"`。ERD 采用表优先布局：在 `entities[].attributes` 中呈现每个物理列，保留其 SQL 类型和来源注释，声明列承担的每个键角色（`key` 接受单个角色或列表，因此连接表列是 `["pk", "fk"]`，且每个 `fk` 列还需要 `references`，如 `"orders.id"`），绝不用把列挪进卡片来替代表格。布局前先将表归入功能域，给每个域一个简洁的 `tag`，并把其成员放进一个实心的网格单元格矩形，单行、单列或填满的矩形块，而不是 L 形或对角线。打了 `tag` 的表必须给出 `row`/`col`，因为绝对坐标没有网格单元格，而表未填满一个矩形的域无法画成色带：渲染器会报 `erd/domain-not-drawn`，而不是发布一个叫不出域名称的图表。多域 schema 以每域占一列最易读（每个 `tag` 是一列纵贯）因为阅读者会把宽画布放大到阅读宽度、把高画布缩小到页面放得下，所以宽排布才是能在笔记本视口内保持完整且清晰的那种。schema 优先的 ERD 超过约 8 张表或 50 个字段时本身就是一张密集地图：首轮完整字段绘制用 `standard`，只有布局仍然可读时才升级。
4. 完整的首个候选文件写好后，直接运行 `finalize`。它的第一道门禁是 showcase 验证；成功的初稿无需单独预验证。命令运行期间保持候选文件不变：

   ```bash
   node bin/archify.mjs finalize <type> <candidate.json> <output.html> --quality showcase --json
   ```

   对于基于仓库的候选文件，初稿就应附上证据，并使用完整命令：`node bin/archify.mjs finalize <type> <candidate.json> <output.html> --repo-root <repo-root> --quality showcase --json`。`--quality` 要与 `meta.quality_profile` 匹配，例如密集的首轮 ERD 用 `standard`。

   通过的回执证明所包含的 `validate`、`deliver`、严格 `check` 以及真实浏览器 `browser-check` 门禁均已通过。使用其紧凑摘要；只有单独请求或针对失败的聚焦诊断才运行独立命令。

5. 非零退出码永远不算成功。阅读紧凑 stdout 或 `evidence.summaryReceipt`，然后按 [修复失败的门禁](references/delivery-contract.md#failed-finalize-and-candidate-repair) 操作，包括其修复次数上限。保留所请求的含义和源码证据。多条纠缠的 Architecture 布线，阅读 [Architecture 布局修复](references/architecture-layout-repair.md)；经测量确认的字段或几何失败，阅读 [绘制契约](references/authoring-contract.md)。编辑相连的邻域并从第 4 步重跑完整 `finalize` 命令。一旦某次运行到达 `browser-check`，输出路径就拥有该证据：此后的每次运行都使用自己的 `--out-dir <folder>/review-<n>`。

## 更新感知

`finalize` 和独立 `deliver` 的回执中包含 `update`。同一次交付不要另行检查。若 `update.noticeRequired` 为 true，阅读 `references/update-awareness.md`，并在给用户的最终回复中保留一条紧凑的更新提示，即使质量门禁失败也要如此。包含多张图表的任务，在最终回复中只提一次更新。只有在用户明确要求时才推迟或忽略提醒；绝不自作主张地安装或更新。

首个候选文件之前，使用绘制参考文件和相关仓库源码，而非 Archify 的实现或测试。只有聚焦修复之后诊断信息仍不可操作时，才去查看 Archify 实现。


## 类型路由（Type router）

| 类型 | 适用场景 | Schema | 示例 |
|---|---|---|---|
| `architecture` | 组件、服务、云/安全边界、基础设施；日常事物由什么组成 | `schemas/architecture.schema.json` | 系统描述、服务、库与 CLI 仓库：`examples/web-app.architecture.json`；部署仓库：`examples/production-deployment.architecture.json` |
| `workflow` | 流程、审批门、工具调用、runbook、CI/CD；计划与分步骤的生命过程 | `schemas/workflow.schema.json` | `examples/agent-tool-call.workflow.json` |
| `sequence` | API 调用链、请求生命周期、异步追踪、返回；人与人之间的来回 | `schemas/sequence.schema.json` | `examples/cache-miss-request.sequence.json` |
| `dataflow` | 管道、ETL/ELT、血缘、治理、消费方；钱或单据流向哪里 | `schemas/dataflow.schema.json` | `examples/product-analytics.dataflow.json` |
| `lifecycle` | 状态/状态机转换、重试、等待与终止状态；申请或订单进行到哪一步 | `schemas/lifecycle.schema.json` | `examples/deployment-release.lifecycle.json` |
| `erd` | 表/实体、属性、主键/外键/唯一键、它们之间的基数关系 | `schemas/erd.schema.json` | `examples/orders.erd.json` |
| `tree` | 单亲包含关系：仓库/模块树、能力或功能拆解、组织式分解 | `schemas/tree.schema.json` | `examples/payment-platform.tree.json` |
| `class` | 类、接口、选定的成员，以及类型之间的依赖/关联/继承/实现/组合关系 | `schemas/class.schema.json` | `examples/payments.class.json` |
| `timeline` | 事情何时发生：事故复盘、发布历史、按比例时间轴上带来源泳道的时间戳事件 | `schemas/timeline.schema.json` | `examples/payment-incident.timeline.json` |
| `waterfall` | 时间花在了哪里：同一时间轴上单个请求或 Agent 运行的 span 时长、重叠与嵌套 | `schemas/waterfall.schema.json` | `examples/checkout-request.waterfall.json` |

在原生图表类型之间难以抉择时，运行 `node bin/archify.mjs guide "<scenario>" --json`。场景验证示例是结构参考，不是可照抄的事实。

对日常题材，沿用相同的图表模式与语义类型，再用读者熟悉的名称称呼它们：按 [节点图标](references/authoring-contract.md#node-icons) 所述使用日常化的 `icon` 取值和 `meta.legend` 标签。缺失的个人事实要向用户询问，而不是编造日期、金额或规则。

## Mermaid 输入

从 Mermaid 中读取拓扑与含义，然后重新创作全新的 Archify JSON；不要机械照搬 Mermaid 的样式。

- `flowchart` / `graph` → `workflow`，组件地图则用 `architecture`。
- `sequenceDiagram` → `sequence`；参与者变为语义参与者，箭头变为消息。
- `stateDiagram` → `lifecycle`；状态与转换保留含义，而非 Mermaid 样式。
- `erDiagram` → `erd`；实体与关系名称、键和基数保留含义，而非 Mermaid 样式。
- `classDiagram` → `class`；类型种类、选定成员和关系种类保留含义，而非 Mermaid 样式。

## 交付

首个候选文件以及每次修复后，使用上文中的 `finalize` 命令。

`finalize` 在第一个未通过的门禁处停止。其紧凑 stdout 和 `<output-stem>.finalize-summary.json` 是普通证据。通过的运行不生成截图，并报告 `visualReview: "not-requested"`。

当通过的 Architecture 回执报告 `visualReviewRecommendation.signals.resolvedCrossovers` 时，把候选文件另存一份，在一次编辑中套用提示，且只改动节点位置和尺寸：每个节点、关系（包括其 `from` 和 `to`）、标签和来源都保持原样。用 `--out-dir <folder>/review-2` 完整重跑一次 `finalize`，因为之前的 HTML 已拥有其浏览器证据。`--out-dir` 只迁移新的 browser-check 与默认 finalize 回执，不迁移 HTML 及其交付回执。成功交付会在请求的输出路径重写这一对文件；更早的审查证据仍绑定其原始产物字节。参见 [审查证据路径](references/delivery-contract.md#a-new-candidate-at-an-existing-output-path)。若该次运行失败、报告更多交叉，或以更多 `signals.routesOverSuggestedBends` 报告相同交叉，则还原副本并用 `--out-dir <folder>/review-3` 完成定稿。不要开始第二轮摆位。仅关于额外拐点的提示是可选的。

当 `layoutReviewRecommendation.action` 为 `inspect-sequence-width` 时，在交付新绘制的 Sequence 之前，先按 [Sequence 宽度审查](references/delivery-contract.md#sequence-width-review) 操作。

普通生成（包括重新摆位的 Architecture）不强制进行感知审查。当用户要求视觉审查、开发审计期间，或存在具体的布线/浏览器疑虑时，使用 [可选捕获证据](references/delivery-contract.md#optional-capture-evidence) 并配 `--out-dir <folder>/visual-check`。`visualReviewRecommendation` 仅供参考。声称视觉质量达标前先检查捕获图；未进行感知审查时，任何检查结论都要注明是自动化的。

失败门禁、独立命令、来源/恢复、重复交付、导出或打开等事项，阅读 [交付契约](references/delivery-contract.md)。原生图表恢复依次为 `deliver` → 严格来源 `check` → `browser-check`；捕获要求严格来源。Explainer 的交付按其绘制指南所述使用 validate、deliver 和 check。

遇到 workflow 视口溢出，在下一次布局编辑前先阅读 [Workflow 视口修复](references/authoring-contract.md#workflow-viewport-repair)。

报告验证细节时，要区分产物检查、浏览器证据、捕获图与实际的感知审查。对于明确要求的即时预览或活动桌面循环，参见 [可选打开](references/delivery-contract.md#optional-opening)。

## 可选查看器能力

每张渲染的图表默认启用动态效果；省略 `meta.animation`。查看器的 Live/Still 按钮控制播放。

仅当用户明确要求 Share Cards、Route/Reach 卡片、动态、深链接、演示、搜索/聚焦或其他 Viewer Runtime 功能时，才阅读 `references/viewer-runtime.md`。

## 安装与降级

Skill 包内无需安装。安装诊断用以下命令验证：

```bash
node bin/archify.mjs doctor
node bin/archify.mjs demo <output-directory>
```

原生图表在 shell 不可用时，手工将 architecture SVG 放入 `assets/template.html`，使用 CSS 语义类而非内联颜色，并遵循 `references/delivery-contract.md` 中的视觉审查契约。Explainer 依赖其渲染器和真实交付门禁；若不可用，报告该限制并在有用时给出文本回答，不得声称已交付 HTML。

## 输出

用用户的语言回复，篇幅以结果允许的限度尽量简短；图表承载内容，因此单张图表通常只需一行。

- 以可点击的 Markdown 链接指向 HTML 开头：用描述性标题而非文件名，附绝对路径，路径含空格时用 `<...>` 包裹。
- 当用户想理解系统或代码库而非绘制所述对象时，附一两句关键结论。跳过只是复述图表显而易见内容的句子。
- 说明任何会影响图表解读方式的事项：读者可能期待但被刻意省略的部分或抽象层级、示意性而非实测的数值、缺失的源码证据，以及修复中被舍弃或合并的所请求内容。
- 多张图表时，一次性报告完成，附指向现有总览的链接或紧凑的逐图链接，而非目录路径。

不要复述命令、修复轮次、哈希、质量档位或检查清单；它们留在回执里。若被问图表是否经过验证，用一行回答，例如"自动化检查已通过；未做视觉审查"。只有在需要复现或排障时才给出回执链接与细节。无法运行的、被要求的视觉审查要如实披露；只有实际做过才可声称经过目视检查。保留更新感知一节要求的更新提示。

示例：`Created [Checkout request timing](/abs/path/checkout-timing.html). Durations are illustrative, not measured.`

Explainer 用两三行回复：结论与页面链接。仅在某道门禁失败或仍存写作警告时提及门禁；不要粘贴草稿。

应请求制作 explainer 之后，若上下文中没有 `[archify explainer: ...]` 行，回复结尾加一行可选提议，介绍主动模式，每次对话一次，例如："需要的话，以后遇到解释、对比、排查这类问题，我可以主动做成这样的页面，要开启吗？"若用户接受，将 `[archify explainer: proactive] Make an Archify explainer page, unasked, for explanations, comparisons, decisions, diagnoses, reviews and plans that need a table, steps or several sections.` 加入当前 Agent 的全局规则文件（如 `~/.claude/CLAUDE.md`、`~/.codex/AGENTS.md` 或 `~/.config/devin/AGENTS.md`）并告知文件名；删除该行即关闭。若用户拒绝，则提议添加 `[archify explainer: on-demand]`，让这个问题不再出现。
