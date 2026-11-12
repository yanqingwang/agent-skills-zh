---
name: n8n-multi-instance
description: 当一个 n8n-mcp 账户指向多个 n8n 实例时使用：`n8n_instances` 工具可用、用户提到多个 n8n 实例或环境（prod 与 staging、多个团队或客户）、多个 Agent 或聊天在同一账户上并行工作、workflow / datatable / credential / execution 调用返回意外的 NOT_FOUND 或读到你无法辨认的数据，或调用被 `INSTANCE_AMBIGUOUS` 或 `INSTANCE_NOT_FOUND` 拒绝。内容涵盖在每次调用中用 `instance` 参数指定目标实例、用 `switch` 设置默认值、在高风险操作（尤其是凭证写入）前核实目标，以及从误路由和失败关闭中恢复。在操作特定实例前、在多实例账户上进行任何凭证创建/更新/删除前，或当调用命中错误/空数据或实例错误时，务必先查阅本 Skill。
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-multi-instance/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 通过 MCP 操作多个 n8n 实例

当 `n8n_instances` 工具可用时，用户即启用了**多实例模式**：一条 MCP 连接可以触达多个 n8n 实例（例如 `prod`、`staging`，或每个客户/团队一个实例）。

有两种方式指定调用应命中哪个实例：

- **在调用中指定名称**：每个 n8n 工具（`n8n_get_workflow`、`n8n_list_workflows`、`n8n_update_partial_workflow`、`n8n_manage_datatable`、`n8n_manage_credentials`、`n8n_executions`、`n8n_test_workflow`、`n8n_health_check`、…）都接受可选的 `instance: "<name>"`。它只路由**这一次调用**，不改变其他任何东西。**优先使用这种方式。**
- **用 `switch` 设置默认值**：`n8n_instances({mode:"switch", name})` 设置那些*未*指定名称的调用所使用的实例。

默认值的共享范围比看上去更广。在 claude.ai（以及其他托管连接器）上，一条连接服务于使用它的**每一个聊天和 Agent**，因此某个聊天里的一次 `switch` 也会牵动其他所有聊天，它们的下一次未命名调用会悄悄落到你的实例上。目标错误通常是静默的：读取会返回错误的数据，写入会落到错误的位置。所以要指定实例名称。

如果 `n8n_instances` 工具**不**存在，则账户为单实例：忽略本 Skill，直接使用 n8n 工具。

> **可用性。** `instance` 参数需要托管版 n8n-mcp 后端 0.1.120+ / n8n-mcp 2.94.0+。当 n8n 工具的输入 schema 列出 `instance` 属性（`n8n_instances` 的 list 输出也带有相关的 `hint`）时，它即存在。如果未列出，说明服务器版本早于该功能：按 *Switching* 一节所述，在独立的轮次里回退到 `switch`。

## 黄金法则

1. **先探查。** 调用 `n8n_instances({mode:"list"})`，弄清确切的实例名称以及哪个是 `current`。绝不臆测名称。
2. **在需要时于每次调用中都指定实例名称**：只要你在多个实例上工作、操作的不是 `current` 实例，或与同一账户上的其他 Agent/聊天并行，就这样做，例如 `n8n_list_workflows({instance:"prod"})`。名称不区分大小写。在任务的每次调用里都以同样方式传入名称；事先没有任何需要"设置"的东西。
3. **你指定的 `instance` 绝不会被静默替换。** 未知名称会以 `INSTANCE_NOT_FOUND` 失败，并列出 `available` 名称，从该列表中选一个再重试。它绝不会回退到另一个实例。
4. **仅在需要更改默认值、且你是该连接的唯一用户时才使用 `switch`。** 在**独立的轮次**里切换，绝不与依赖它的调用放在同一批并行任务中（批处理顺序无保证）。
5. **凭证写入：指定实例名称。** `n8n_manage_credentials({action:"create", …, instance:"prod"})`。带名称的写入是显式的，因此绝不会触发 `INSTANCE_AMBIGUOUS`。先用 `list` 核对名称，指定*错误*的实例会把机密写到那里。
6. **意外的 `NOT_FOUND` 几乎总是实例错误的误路由，而非对象被删除。** 不要重建对象。把 `instance` 设成它所在的实例再重试（见"恢复手册"）。

## 核心工作流


```
1. n8n_instances({mode:"list"})                        # names, current, default
2. n8n_list_workflows({instance:"client-a"})            # read on client-a
3. n8n_get_workflow({id:"…", instance:"client-b"})      # read on client-b — no switch needed
4. n8n_update_partial_workflow({id:"…", operations:[…], instance:"client-b"})
5. Credential write:
   n8n_manage_credentials({action:"create", name:"…", type:"…", data:{…}, instance:"client-a"})
```


每次调用都指定了目标，因此其他聊天在中途切换成什么都无关紧要；即便各调用指向不同实例，也能安全地放在同一批并行任务中运行。

## `instance` 参数

- **取值：** 来自 `n8n_instances` `list` 的实例**名称**（`available[].name`），不区分大小写匹配。不是 id，也不是 URL，同一个 URL 可以注册在多个名称下。
- **作用范围：** 只路由携带它的那次调用，**不**会为任何人更改 `current` 或默认值。
- **省略（或为空）：** 调用使用默认值，即此连接上最后一次 `switch`，或账户默认值。
- 在以下情况会**失败关闭**并返回 `INSTANCE_NOT_FOUND`（调用不会到达 n8n，不消耗配额）：
  - 名称不匹配任何实例，错误会列出 `available`；
  - 取值不是字符串；
  - 多实例模式关闭，且名称不是该连接所触达的那个唯一实例。


```json
{
  "error": "INSTANCE_NOT_FOUND",
  "message": "No n8n instance named \"clinet-a\". Pass one of the available names as `instance`, …",
  "available": ["client-a", "client-b"]
}
```


`n8n_instances` 自身不接受 `instance`，`switch` 用的是它自己的 `name` 参数。

## `n8n_instances` 工具

两种模式（`mode` 为必填，且会做枚举校验）：

- `{mode:"list"}` → `{ current, default, available, hint }`，无副作用。
  - `current` 和 `default` 各为一个实例 `{ id, name, url, isDefault }`（或 `null`）。
  - `available` 包含所有实例，每个额外带一个 `isCurrent` 布尔值。按 **`name`** 匹配；绝不硬编码 `id`。
- `{mode:"switch", name:"<name>"}` → `{ previous, current }`，并为未指定实例的调用设置默认值。`name` 不区分大小写。

### 错误返回结构（来自 `n8n_instances` 工具）

每个错误都返回 `{ error: "<CODE>", message, … }`。你实际会遇到的有：

| 代码 | 触发时机 | 处理方式 |
|---|---|---|
| `UNKNOWN_INSTANCE` | `switch` 的 `name` 不匹配任何实例 | 从错误载荷里的 `available` 列表挑一个名称再重试。 |
| `NAME_REQUIRED` | `switch` 未带 `name` | 带上 `name` 重新调用（错误会在 `available` 里列出有效名称）。 |
| `MULTI_INSTANCE_DISABLED` | 多实例模式关闭 | 没有可切换的对象，直接使用 n8n 工具。用户可在 n8n-mcp 控制台启用它。 |
| `NO_SESSION` | 请求**既没有** MCP session id，**也没有** credential id | 选择结果无处落地。重新连接 / 初始化会话后再切换，或者干脆在每次调用里指定 `instance`。 |
| `UNKNOWN_MODE` | `mode` 不是 `list`/`switch` | 使用 `list` 或 `switch`。 |
| `INVALID_CONTEXT` | 服务端元数据缺失 | 这是服务端的 bug，不是你的输入问题，请上报。 |

> 实例名称不能是 `default`、`current`、`list` 或 `switch`（保留字），所以你永远不会看到一个实例恰好以某个模式或字段来命名。

### `INSTANCE_AMBIGUOUS`（来自凭证写入路径，而非工具本身）

当你在**未**指定 `instance` 的情况下调用 `n8n_manage_credentials`（或 `n8n_manage_agents` 的写入操作），且此次调用继承的默认值存在歧义时返回：本会话自身从未切换过，却沿用了别处执行的一次切换，指向一个**非默认**实例。为避免把机密误写到错误的实例，服务器会**拦截该写入**（它不会到达 n8n，不消耗配额）并返回：


```json
{
  "error": "INSTANCE_AMBIGUOUS",
  "message": "… the session issuing this request never switched there itself … Re-run n8n_instances({mode:\"switch\", name:\"…\"}) on this session to confirm the target …",
  "lastSelected": { "id": "…", "name": "…" },
  "default":      { "id": "…", "name": "…" }
}
```


**修复：** 确定你真正想要的实例（`lastSelected` 是继承来的切换，`default` 是账户默认值），然后**用 `instance:"<that name>"` 重试写入**。（在没有 `instance` 参数的服务器上，先在本会话执行 `n8n_instances({mode:"switch", name:"…"})`，再重试。）

## 目标定位的行为方式（心智模型）

- **带名称的调用**一律发往指定实例，没有例外。它是无状态的：既不读取也不更改默认值。
- **未命名调用**发往默认值：此连接上最后一次 `switch`，若无则为账户默认值。
- **谁共享默认值取决于客户端。** 托管连接器（claude.ai，以及任何把一个聊天分散到多个 MCP 会话上的东西）为**每条连接保留一个默认值**，由该连接上的每个聊天和 Agent 共享。拥有稳定 MCP 会话的直连客户端（Claude Code、Cursor）为每个终端保留一个默认值，但在重连后可能回退到该连接最后一次切换的结果。无论哪种情况，别处的工作都可能改动你的默认值，这正是第 2 条法则要求指定实例名称的原因。
- 一次 `switch` 会在重连、空闲和后端部署之间持续保留（~24h，即 MCP 会话的生命周期）。
- 未带 `instance` 的**读取与非凭证写入**会静默路由到默认值，误路由只会产生错误数据或一个 `NOT_FOUND`，而非报错。
- **若默认实例被删除**（用户在会话中途移除它），未命名调用会静默回退到**账户默认值**，不报错。指向已删除实例的带名称调用会以 `INSTANCE_NOT_FOUND` 失败。

## 切换（仅在需要更改默认值时）

当用户要求更改"那个"实例时，或在缺少 `instance` 参数的旧服务器上，使用 `switch`。


```
1. n8n_instances({mode:"switch", name:"prod"})   # its own turn
   → returns { previous, current }; confirm current.name == "prod"
2. (then, in a later turn) the unnamed calls
3. Before a credential write: n8n_instances({mode:"list"}) → re-confirm current, then write
```


绝不把切换与依赖它的工作放进同一批任务，并记住它会牵动共享该连接的所有聊天。

## 恢复手册

| 症状 | 通常意味着 | 处理方式 |
|---|---|---|
| `INSTANCE_NOT_FOUND` | `instance` 名称有误（拼写错误、臆测，或实例已被移除） | 从错误的 `available` 列表挑一个名称再重试。绝不要为了"让它跑通"而去掉 `instance`，那会让它静默运行在默认实例上。 |
| 凭证创建/更新/删除时出现 `INSTANCE_AMBIGUOUS` | 在一个从未选定目标的会话上执行了未命名的机密写入 | 用 `instance:"<target>"` 重试写入（错误会给出 `lastSelected` 和 `default`，挑你想要的那个）。绝不盲目重试。 |
| 对某个你**确信存在**的 workflow/datatable/credential 返回 `NOT_FOUND` | 你指向了错误的实例，**并非**它被删除 | 把 `instance` 设成它所在的实例再重试（用 `list` 核对名称）。**不要重建对象。** |
| 读取返回**为空或陌生**的数据 | 未命名调用落到了别人改动过的默认值，或在你的实例被删除后发生了回退 | 先带上 `instance:"<name>"` 重跑读取，再下结论。 |
| `switch` 报 `UNKNOWN_INSTANCE` | `name` 有误 | 读取错误里的 `available` 名称，切换到其中之一。 |
| `n8n_health_check` 报告了意料之外的 `instanceName` | 你的未命名调用正发往别处 | 在调用中指定实例名称（若你独占该连接，也可用 `switch`）。`n8n_health_check({instance:"…"})` 可确认某个名称能否解析。 |

要确认未命名调用去向何处，请读取 `n8n_instances({mode:"list"})` 里的 `current`（主要依据）。`n8n_health_check` 也会在 `details.instanceName` 下返回解析出的实例，但在某些路径（旧版/聊天）上可能缺失，因此把它当作辅助确认。

## 凭证操作（风险最高）

凭证承载真实有效的机密，误路由的凭证写入会把机密放到**错误的实例**上。因此：

- **在每次凭证创建/更新/删除时都指定实例名称：** `n8n_manage_credentials({action:"create", …, instance:"client-a"})`。名称取自 `list`，即便带名称，写到错误的实例上也照样会落在那里。
- 不带 `instance` 时，写入会发往默认值，而它可能已被其他聊天改动。服务器只会拦截*有歧义*的情况（`INSTANCE_AMBIGUOUS`）；在别人显式切换之后，未命名写入会径直落到他们的实例上。
- 凭证**读取**（`action:"list"`/`"get"`/`"getSchema"`）不会写入机密，但从错误的实例读取会返回错误的 schema 或列表，因此也要指定实例名称。
- 关于 `n8n_manage_credentials` 工具本身（CRUD 形态、`getSchema` 探查、绝不把机密内联进文本字段），参见 `n8n-mcp-tools-expert`。

## 常见的多实例任务：在实例之间复制对象

要在实例 B 上重建来自实例 A 的凭证或工作流：


```
1. read the source on A:  n8n_get_workflow({id:"…", instance:"A"})
                          (credentials: n8n_manage_credentials({action:"get", id:"…", instance:"A"}))
2. create it on B:        n8n_create_workflow({…, instance:"B"})
                          (credentials: n8n_manage_credentials({action:"create", …, instance:"B"}))
3. verify on B:           n8n_get_workflow({id:"<new id>", instance:"B"})
```


全程不做切换，因此在读取与写入之间没有任何东西能改动目标。n8n 不会返回凭证的机密值，所以对于凭证，需要用户为在 B 上的创建再次提供这些值。

## 速查

- 查看实例：`n8n_instances({mode:"list"})` → `{ current, default, available, hint }`
- 定位单次调用：在任意 n8n 工具调用里加上 `instance:"<name>"`，推荐做法
- 更改未命名调用的默认值：`n8n_instances({mode:"switch", name:"<name>"})`，放在独立的轮次里；托管连接上由每个聊天共享
- `INSTANCE_NOT_FOUND` → 使用错误里 `available` 列表中的名称
- `INSTANCE_AMBIGUOUS`（未命名的凭证写入）→ 用 `instance:"<target>"` 重试
- 意外的 `NOT_FOUND` → 用正确的 `instance` 重试；**不要重建**
- 工具 schema 中没有 `instance` 属性 → 旧服务器：把 `switch` 放在独立的轮次里，凭证写入前核实 `current`

## 与其他 Skill 的协作

- **n8n-mcp-tools-expert**：负责 `n8n_manage_credentials`（CRUD + `getSchema`），以及机密必须经由凭证系统、绝不进入文本字段这一规则。本 Skill 在其之上叠加了"用哪个实例？"这一层。
- **using-n8n-mcp-skills**：路由器；某个构建步骤由哪个 Skill 负责，请查阅它。
