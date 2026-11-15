> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-error-handling/NODE_ERROR_OUTPUTS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 节点级错误输出

本文件讲**单个节点上的错误输出**（该节点抛错时触发的第二个 `main` 输出），以及几乎人人会栽跟头的两步配置。工作流级兜底（Error Trigger 工作流）和 webhook/Respond 形态见 `n8n-error-handling` 其余文件。

核心在于：节点失败应路由到*你*控制的地方，而不是让运行中止。漏配一半的代价是 n8n 最恶劣的静默失败之一：运行显示绿色，工作却被悄悄丢掉。

---

## 两步配置（缺一不可）

路由一个节点的失败恰好需要两处改动。只做任何一处，看起来都像配置完了，实际行为却是错的。

### Step 1：创建错误输出

在节点上设置 `onError: "continueErrorOutput"`。这一步才*添加*出第二个输出。没做之前，`main[1]` 不存在，接上去的任何东西都不会触发。

```javascript
{ type: "updateNode", nodeName: "Google Sheets",
  changes: { onError: "continueErrorOutput" } }
```

若只改这一个字段，可用更精准的替代：

```javascript
{ type: "patchNodeField", nodeName: "Google Sheets",
  fieldPath: "onError", value: "continueErrorOutput" }
```

`onError` 的合法取值：

| 取值 | 效果 |
|---|---|
| `"stopWorkflow"`（默认） | 错误使整个工作流中止。对你盯着看的运行，这是正确的默认。 |
| `"continueRegularOutput"` | 错误条目从**普通**输出（`main[0]`）与成功条目一起流出。少见，而且通常是失误：下游拿到错误形态的数据还继续跑。 |
| `"continueErrorOutput"` | 错误条目从**单独的**错误输出（`main[1]`）流出。就是下面要接的那个。 |

### Step 2：接线错误输出

设了 `onError: "continueErrorOutput"` 之后，节点有两个输出：

- `main[0]` → 成功路径（`sourceIndex: 0`）
- `main[1]` → 错误路径（`sourceIndex: 1`）

把错误输出接到真正的处理器上：

```javascript
{ type: "addConnection",
  source: "Google Sheets",
  target: "Handle Error",
  sourceIndex: 1 }
```

`sourceIndex: 1` 就是错误输出。（IF 节点接受友好别名 `branch: "true"` / `branch: "false"` 对应索引 0/1；普通可能出错的节点没有这种别名，请显式写 `sourceIndex: 1`。）

---

## 失败模式：为什么"两步只做一步"如此危险

### 设了 `onError`，错误输出没接线

```javascript
// onError: "continueErrorOutput" set on the node,
// but no addConnection from sourceIndex 1.
```

失败时节点向 `main[1]` 发出数据，而它**没有任何目标**。错误数据被静默丢弃，下游永不触发，而且（陷阱在此）这次执行被记为**成功**，因为在 n8n 看来，错误已被一条恰好通向虚无的分支"处理"了。没有失败执行记录，仪表板上什么都没有。集成"就是不好使了"，且查无实据。

**修法：**把 `sourceIndex: 1` 接到真正的处理器，*或者*把 `onError` 改回 `"stopWorkflow"`，让失败重新响亮。

### 接了错误输出，`onError` 没设

```javascript
// addConnection from "Some Node" sourceIndex 1 → "Handle Error" exists,
// but the node still has the default onError: "stopWorkflow".
```

连接躺在 JSON 里，但它来源的槽位永不触发。处理器成为死代码。失败时工作流直接**中止**（默认行为）。比第一种模式危险性低（至少它是响的），但你建好的处理器什么也不做。

**修法：**在节点上设置 `onError: "continueErrorOutput"`。

### 为什么校验救不了你

接线只做一半的错误输出**校验照样通过**。`validate_workflow` 和 `n8n_validate_workflow` 不会标记"设了 `onError` 但 `main[1]` 为空"或其反向——两者在结构上都合法。这是运行时行为，不是 schema 违规。唯一可靠的检查是把工作流读回来（见下文"验证"）。

---

## 常见接线形态

### 单个易错节点 → 错误处理器

```javascript
// Node config: onError: "continueErrorOutput"
{ type: "addConnection", source: "HTTP Request", target: "Respond Error", sourceIndex: 1 }
```

### 成功路径扇出，错误路径另走一路

```javascript
{ type: "addConnection", source: "HTTP Request", target: "Save Result",  sourceIndex: 0 }
{ type: "addConnection", source: "HTTP Request", target: "Notify Slack",  sourceIndex: 0 }
{ type: "addConnection", source: "HTTP Request", target: "Respond Error", sourceIndex: 1 }
```

### 多个易错节点 → 共享一个错误处理器（扇入）

```javascript
// Each of these nodes needs onError: "continueErrorOutput" on its own config.
{ type: "addConnection", source: "Fetch User",     target: "Respond Error", sourceIndex: 1 }
{ type: "addConnection", source: "Call External",  target: "Respond Error", sourceIndex: 1 }
{ type: "addConnection", source: "Write Database", target: "Respond Error", sourceIndex: 1 }
```

扇入让图保持可读：一个错误响应器，多个来源。处理器可以查看是哪个节点失败（错误负载里带失败节点的名称），据此区分响应。

### 同一次失败既记日志又响应

把错误输出接到两个目标并不冲突，两者都收到错误数据：

```javascript
{ type: "addConnection", source: "Call External", target: "Log Full Error", sourceIndex: 1 }
{ type: "addConnection", source: "Call External", target: "Respond Error",  sourceIndex: 1 }
```

适用于同一次失败既要脱敏响应*又*要私有的全量明细日志。（或者串起来：错误输出 → 日志 → 响应，让日志先跑。）

---

## 什么算"易错"

任何运行时可能抛错的，都给它接错误输出：

- 网络调用：HTTP Request、第三方 API 节点、数据库。
- 鉴权失败：凭据过期、令牌轮换。
- schema 不匹配：缺数据库列、JSON 解析失败。
- 限流：上游 429（先配 `retryOnFail`，让这类错误自愈）。
- 文件/二进制操作：路径缺失、权限被拒（见 **n8n-binary-and-data**）。
- 可能抛错的 Code 节点。

通常**不值得**接错误输出的：

- 对已校验数据做 Set / Edit Fields。
- 带简单表达式的 IF / Switch：如果这些抛错，那是该修的 bug，不是该捕获的路径。
- 无 I/O 的纯转换。

拿不准就接。代价只是一条连线；不接的代价是静默中止。

---

## 验证（每次都做）

任何创建/更新之后，用 `n8n_get_workflow` 把工作流拉回来，对每个易错节点检查**两半**：

1. **节点配置**：`onError` 是 `"continueErrorOutput"`（或你想要的任何值）。
2. **连接**：`connections["<node>"].main[1]` 包含预期的处理器。

缺了任何一半，就是一个静默失败配置。激活前先修。

`n8n_autofix_workflow` 能修一些结构问题，但它推断不出你*本想*接一条错误路径，对某个节点失败的处理意图得由你自己表达。把读回检查当作必做项。

---

## 什么时候该改用错误工作流

节点级输出处理的是*你记得接线的某一个节点*的失败。它们**接不住**：

- 你忘了接线的节点上的失败。
- 节点之间的崩溃。
- 整个工作流超时。
- 触发器失败。

这些要靠工作流级**错误工作流**（Error Trigger 节点）。注意反向情形：接到丢弃数据的空操作上的节点级错误输出算"已处理"，因此会*压制*错误工作流。只有当你真的要对错误采取行动时才做节点级捕获。见 **ERROR_WORKFLOWS.md**。
