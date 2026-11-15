> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/doctor.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

报告并修复本项目 Impeccable 产物与已安装版本所读取内容之间的漂移（drift）：PRODUCT.md、DESIGN.md 及其 `.impeccable/design.json` sidecar、`.impeccable/config.json`、持久化的界面简报（surface briefs），以及 design hook。

这是维护，不是设计。不要重新设计任何东西，不要打开报告未点名的文件，也不要作为副作用运行任何其他命令。

## 它管什么，不管什么

三类漂移都顶着"过期"的名头行走。把它们分开：

- **Tool version。** 已安装的 skill 比已发布的旧。`impeccable context` 在启动时以 `UPDATE_AVAILABLE` 报告，`npx impeccable update` 修复，插件安装则走 Harness 的插件管理器。不是本命令的职责。
- **Schema drift。** 某个产物由更旧的 Impeccable 写出：没人读取的字段、现在被期待的字段、位于已废弃位置的文件。机械性，本命令能修复其中的大部分。
- **Truth drift。** 代码已经前进，文档不再描述它。没有文件对比能裁决这一点。`document` 管 DESIGN.md，`init` 管 PRODUCT.md，本命令的职责是把一个具体的缺口交到它们手上，而不是一个模糊的怀疑。

## Step 1: 运行检查

```
.claude/skills/impeccable/scripts/impeccable doctor --json
```

用户点名了 monorepo 中的工作区、文件或路由时，加 `--target <path>`。不加时报告描述的是仓库根，而在 monorepo 里那常常是错误的项目。

输出携带 `findings`（每条含 `id`、`artifact`、`path`、`severity`、`summary`、`fix`），在 monorepo 里还有 `workspaces`，含每个应用的 product 与 design 解析结果。`ruleRegistryAvailable: false` 表示被忽略的规则 id 无法验证；要说出来，而不是暗示那份清单是干净的。

空的 `findings` 数组就是好结果。用一行话说明并停下。

## Step 2: 按 severity 行动

severity 说的是应当发生什么，不是它有多糟。

- **`auto`** 不携带任何决策。运行一次 `.claude/skills/impeccable/scripts/impeccable doctor --fix` 应用这些修复，然后用一行话报告它改动了什么。不要先请求许可，之后也不要再来问它们。
- **`mention`** 需要用户知道，但不需要现在决定任何事。每条用一句话说明，并附它提供的修复。
- **`route`** 需要一条具体命令。点名该命令以及它会弥合的缺口。只有用户在本轮要求时才运行它；`init` 与 `document` 是对话，不是你可以无人值守执行的修复。

一次过完报告这三组。findings 不是错误，命令也不会因它们而失败。

## Step 3: 已废弃字段是有约束力的

报告某个已废弃字段（目前是 `## Register`）的 finding 不是风格备注。从此刻起的每个决策都把该字段当作不存在，无论它持有什么值，并提议删除该章节。"以防万一"地保留它，正是一条已退役的轴继续操控当前产出的方式。

## Step 4: 对 truth drift 不要夸大

`design-md-drift` 统计自 DESIGN.md 最后一次编辑以来视觉源目录的提交数。提交数不是矛盾。报告那个数字，说明它度量什么；如果用户想知道文档是否真的错了，就把 DESIGN.md 对照当前的 token 与组件来读，并据此回答。绝不因为数字大就断言 DESIGN.md 已过期。

同样的克制适用于 `workspace-context-inherited`。继承是设计出来的行为。一份 product 记录是否真实地描述了多个应用，是要问用户的问题，不是要修的缺陷。

## Monorepo 备注

- `workspace-platform-native-evidence` 是这里最重要的 finding：一个携带 native 构建文件、却继承解析为 web 的根记录的工作区，一辈子都会收到 web 指引，永远加载不了 [ios.md](ios.md) 或 [android.md](android.md)。修复是在该工作区里放一份子级 PRODUCT.md，因为一份继承的记录装不下两个平台。
- `config-project-roots-match-nothing` 表示每个 `projectRoots` glob 都落空，仓库根正无声地充当活动项目。改名过的工作区目录是常见原因。报告这些模式并询问它们应当指向哪些目录。
- `config-invalid-build-path` 与 `config-build-path-unset` 都关于同一个键：`.impeccable/config.json` 中的 `buildPath`（或 gitignore 的 `.impeccable/config.local.json`，它对该开发者优先）。它持有 `comp` 或 `code`，决定新的 Persuade 与 Experience 界面是从生成的 comp 构建还是直接写代码；无论它持有什么，Operate 与 Read 界面都以代码为先。读不到该值时不会回退到相反路径，所以一个本意是 `code` 的项目一直在以 comp 为先构建；要报告确切的值。unset finding 只在项目做过 direction 工作却从未记录偏好的地方触发，而该提议只有在你的工具面里有图像生成时才属于这个 finding。没有图像生成，就没有可选项，也没有什么可说的。
- 在提议任何变更之前，用 `workspaces` 表向用户展示哪些应用携带自己的上下文、哪些是继承的、哪些什么都没有。

## 关闭启动检查

`impeccable context` 在会话开始时报告这些 findings 的廉价子集，按项目每周最多一次。在 `.impeccable/config.json` 里设 `"stalenessCheck": false` 可以静默它，或对单个会话用 `IMPECCABLE_NO_STALENESS_CHECK=1`。检查关闭时本命令仍然可用，这正是想"只在要求时才看报告"的用户应当使用的组合。
