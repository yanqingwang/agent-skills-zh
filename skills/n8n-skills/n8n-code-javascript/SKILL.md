---
name: n8n-code-javascript
description: "在 n8n Code 节点中编写、审查或调试 JavaScript。当工作流中已有 Code 节点（编辑它、修复报错、选择其运行模式、让它更快），或有充分理由新建一个时使用：没有原生节点能胜任（先用 using-n8n-mcp-skills 中的 job-to-node 表核对），且任务在封闭清单上——没有节点能表达的循环或递归、跨执行的状态、没有节点能处理的解析、白名单内的库、重型的全量数据处理，或一个短节点可替代 4+ 个拼接节点。涵盖代码中的 $input/$json/$node、this.helpers、Luxon、SplitInBatches 循环、跨迭代数据、pairedItem、逐条执行性能，以及 \"Why Code:\"（为何用 Code）备注。过滤、汇总、去重、排序、连接、文件格式和 API 分页都有原生节点（Filter、Summarize、Remove Duplicates、Sort、Merge、Extract From File、HTTP Request）：参见 n8n-node-configuration。例外——对于可被 AI Agent 调用的 Custom Code Tool（@n8n/n8n-nodes-langchain.toolCode），请使用 n8n-code-tool；它有另一套运行时契约。"
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-javascript/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# JavaScript Code 节点

在 n8n Code 节点中编写 JavaScript 代码的专家指南。

---

## 写 Code 节点之前

新建 Code 节点必须先通过这道闸门：

1. **有原生节点能做这件事吗？** 查看 `using-n8n-mcp-skills` 中的 job-to-node 表：Filter、IF / Switch、
   Summarize、Aggregate、Split Out、Merge、Compare Datasets、Remove Duplicates、Sort + Limit、Date & Time、
   XML / HTML / Extract From File / Convert To File、HTTP Request（分页、批处理）和 Crypto 覆盖了 Code 的大多数用武之地。
   它们的配置在 `n8n-node-configuration` → NATIVE_NODES.md。
2. **在该节点里写一个短表达式就够了吗？** 一个表达式，没有函数体——辅助方法（`.pluck()`、
   `.sum()`、`.unique()`、`$ifEmpty()`、`.diffTo()`）在 `n8n-expression-syntax` 中，n8n-mcp 2.97.0+ 也在
   `tools_documentation({topic: "expression_helpers"})` 中。`{{ }}` 内含多条语句就算代码，因此应归入这里
   而不是 Edit Fields 字段。
3. **任务在封闭清单上吗？** 没有节点能表达的循环或递归、跨执行的状态
   （`$getWorkflowStaticData`）、没有节点能处理的解析、白名单内的库、重型的全量数据处理（数千条数据，
   用户明示或实测得出），或一个短 Code 节点（约 15 行）替代 4+ 个只做数据整形的拼接节点。

通过闸门后，编写 Code 节点并给它加一条备注，让下一个读者（以及审查 Hook）能看到理由：

```json
{ "name": "Flatten category tree", "type": "n8n-nodes-base.code", "notes": "Why Code: Split Out considered — the tree has arbitrary depth (recursion)", "notesInFlow": true }
```

编辑或调试已存在的 Code 节点不需要过闸门，但如果该节点在做原生节点能做的工作，请说明并提供原生替代方案。

---

## 快速开始

```javascript
// Basic template for Code nodes
const items = $input.all();

// Process data
const processed = items.map(item => ({
  json: {
    ...item.json,
    processed: true,
    timestamp: new Date().toISOString()
  }
}));

return processed;
```

### 基本规则

1. **选择 "Run Once for All Items" 模式**（大多数用例推荐）
2. **访问数据**：`$input.all()`、`$input.first()` 或 `$input.item`
3. **返回 `[{json: {...}}]`** —— 这是规范、跨模式可移植的形式。在 *Run Once for All Items* 模式下，n8n 也会自动包装裸的 `return {…}` 对象，所以那样也能运行；真正会失败的是返回原始值（字符串/数字）或 `null`。
4. **关键**：Webhook 数据在 `$json.body` 下（不是直接在 `$json` 下）
5. **可用的内建项**：`this.helpers.httpRequest()`（无鉴权 —— 裸 `$helpers` 全局在 task-runner 沙箱中**未定义**，因此 `$helpers.httpRequest()` 会抛出 `ReferenceError: $helpers is not defined`）、DateTime（Luxon）、$jmespath()。**不可用**：`this.helpers.httpRequestWithAuthentication`（在拒绝清单上）、$env（当 N8N_BLOCK_ENV_ACCESS_IN_NODE=true 时）、require()（除非在白名单上）。凡是超出简单无鉴权 GET（鉴权、分页、重试）的需求，优先使用 **HTTP Request 节点**，把 Code 节点留给纯逻辑。
6. **实例级白名单库**：自托管实例可通过 `N8N_RUNNERS_ALLOWED_BUILT_IN_MODULES` 和 `N8N_RUNNERS_ALLOWED_EXTERNAL_MODULES`（旧版：`NODE_FUNCTION_ALLOW_BUILTIN` / `NODE_FUNCTION_ALLOW_EXTERNAL`）将模块加入白名单。如果用户说其实例允许特定模块（如 `axios`、`lodash`、`crypto`），就用 `require()` 使用它们——不要拒绝。不确定时，先询问或默认只用内建模块。
7. **用错 Skill 了？** 如果你在为挂到 AI Agent 上的 **Custom Code Tool**（`@n8n/n8n-nodes-langchain.toolCode`）写代码，停下——那个节点有不同的契约（通过 `query` 输入、必须返回字符串、没有 `$input`/`$helpers`）。请使用 **n8n-code-tool** Skill。

---

## 模式选择指南

Code 节点提供两种执行模式。按用例选择：

### Run Once for All Items（推荐 - 默认）

**此模式适用于：** 95% 的用例

- **工作方式**：无论输入条数多少，代码只执行**一次**
- **数据访问**：`$input.all()` 或 `items` 数组
- **最适合**：需要一次性拿到所有条目、且通过了上述闸门的逻辑
- **性能**：多条数据时更快（单次执行）

```javascript
// Example: running balance — each item depends on the ones before it,
// which no native node expresses (Summarize gives one total per group, not a running one)
let balance = 0;
return $input.all().map(item => {
  balance += item.json.amount || 0;
  return { json: { ...item.json, balance } };
});
```

**何时使用：**
- ✅ 每条数据依赖更早的条目（累计值、事件会话化、间隔检测）
- ✅ 多趟算法，或对未知深度嵌套数据的递归
- ✅ 数千条数据上的重型转换，一个节点胜过一条长链（已实测）

原生优先：总计、平均与计数 → **Summarize**；排序或排名 → **Sort + Limit**；去重 →
**Remove Duplicates**；多条目并为一个数组 → **Aggregate**；连接两个列表 → **Merge**。

### Run Once for Each Item

**此模式适用于：** 仅特殊场景

- **工作方式**：代码对每条输入**分别**执行
- **数据访问**：`$input.item` 或 `$item`
- **最适合**：条目级逻辑、相互独立的操作、逐条校验
- **性能**：大数据集更慢（多次执行）

```javascript
// Example: Add processing timestamp to each item
const item = $input.item;

return [{
  json: {
    ...item.json,
    processed: true,
    processedAt: new Date().toISOString()
  }
}];
```

**何时使用：**
- ✅ 每条数据需要独立的 API 调用
- ✅ 逐条校验且需不同的错误处理
- ✅ 基于条目属性的条目级转换
- ✅ 业务逻辑要求条目必须分开处理

**决策捷径：**
- **需要查看多条数据？** → 用 "All Items" 模式
- **每条数据完全独立？** → 用 "Each Item" 模式
- **不确定？** → 用 "All Items" 模式（你总能在内部循环）

### 为什么 "All Items" 更快——逐条边界

模式选择是 Code 节点最大的单项性能杠杆。每个*逐条*执行上下文都有一笔启动税（在 n8n 2.x、小记录上实测）：

| 每条数据上运行什么 | 大约成本 |
|---|---|
| Code **All Items**（整个集合一次运行） | ~0.02 ms/条 |
| 任意节点中的表达式（IF / Set 等） | ~0.2 ms/条 |
| Code **Each Item**（每条数据一个完整沙箱） | ~0.6 ms/条 —— 约为 All Items 的 25–30 倍 |

所以对 10k 条数据用 `Run Once for Each Item` 是约 6 秒的纯开销，而 `Run Once for All Items` 约为 0.2 秒。只有当某条数据确实需要隔离时（独立的错误处理，或无法批量的逐条 API 调用）才用 Each Item；否则在单个 All Items 节点*内部*循环。表达式复杂度本身几乎免费（约 90% 的成本来自逐条上下文，而非你的代码），而且每次节点→节点跳转都会重新复制全部条目——所以要减少的是*逐条边界的数量*，而不是微观优化每一个。

除逐条成本外，每次 Code 节点运行还要支付一笔固定的向 task runner 交接的开销。默认 internal 模式下，runner 在空闲 15 秒后停止（`N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT`），因此偶发运行的工作流在大多数运行中都要支付数百毫秒的冷启动。原生转换节点在一次进程内调用中处理所有条目，省去这笔交接。

**这对节点选择意味着什么。** 大多数工作流是 I/O 受限的，几百条以下这些成本都不重要：按可读性选择，也就是原生节点优先。只有重型全量处理——每次运行数千条、以转换而非 I/O 为主、用户明示或实测得出——性能才成为决定性论据。此时一个 All Items Code 节点可以胜过一长串节点，理由写进它的 `Why Code:` 备注。这组数字是本套件唯一的实测参考；其他 Skill 指向这里而不是各自重复。

**参见**：[DATA_ACCESS.md](DATA_ACCESS.md) → "Mode Performance"，了解推论、跳转成本和规模检查。

---

## 数据访问模式

四种从上游节点取数据的方式。注意 `$node["Name"]` 和 `$('Name')` 需要 `.first().json` 或 `.all()`——绝不能直接 `.json`。

```javascript
const allItems = $input.all();          // 1. All items — batch ops, aggregation (most common)
const data = $input.first().json;       // 2. First item — single objects, API responses
const item = $input.item;               // 3. Current item — "Each Item" mode ONLY (undefined otherwise)
const other = $node["Webhook"].json;    // 4. Named node — combine data across nodes
```

始终通过 `.json` 访问字段（例如 `item.json.name`，而非 `item.name`），并且优先使用显式的 `$input.first().json.field` 而不是裸的 `$json.field`。

**参见**：[DATA_ACCESS.md](DATA_ACCESS.md) 完整指南——每种模式都带示例、一棵决策树，以及常见错误（修改原始对象、缺少长度检查、在错误模式下使用 `$input.item`）。

---

## 关键：Webhook 数据结构

**最常见错误**：Webhook 数据嵌套在 `.body` 下

```javascript
// ❌ WRONG - Will return undefined
const name = $json.name;
const email = $json.email;

// ✅ CORRECT - Webhook data is under .body
const name = $json.body.name;
const email = $json.body.email;

// Or with $input
const webhookData = $input.first().json.body;
const name = webhookData.name;
```

**原因**：Webhook 节点把所有请求数据包装在 `body` 属性下。这包括 POST 数据、查询参数和 JSON 载荷。

**参见**：[DATA_ACCESS.md](DATA_ACCESS.md) 了解完整的 webhook 结构细节

---

## 返回格式要求

**规范形式**：`[{json: {...}}]` —— 由带 `json` 属性的对象组成的数组。它没有歧义，且在两种执行模式下行为一致，所以请以它为默认。

在 *Run Once for All Items* 模式下，n8n 会在出口自动规范化更松散的形状：单个裸对象，或裸对象数组，会被自动包装进 `json`。所以 `return {foo: 1}` 能运行。没有任何东西可包装——因此运行时真正报 "Code doesn't return items properly" 错误的——是原始值（字符串/数字/布尔）或 `null`/`undefined`。（n8n-mcp ≥ 2.63.0 不再把裸对象返回标记为错误；它反映了这一自动包装行为。）

### 正确的返回格式

```javascript
// ✅ Single result
return [{
  json: {
    field1: value1,
    field2: value2
  }
}];

// ✅ Multiple results
return [
  {json: {id: 1, data: 'first'}},
  {json: {id: 2, data: 'second'}}
];

// ✅ Transformed array
const transformed = $input.all()
  .filter(item => item.json.valid)
  .map(item => ({
    json: {
      id: item.json.id,
      processed: true
    }
  }));
return transformed;

// ✅ Empty result (when no data to return)
return [];

// ✅ Conditional return
if (shouldProcess) {
  return [{json: processedData}];
} else {
  return [];
}
```

### 非规范返回（自动包装——仍推荐规范形式）

```javascript
// ⚠️ Auto-wrapped in All Items mode → [{json: {field: value}}]. Runs, but prefer the array form.
return {
  json: {field: value}
};

// ⚠️ Auto-wrapped → [{json: {field: value}}]. Runs, but add the json wrapper for clarity.
return [{field: value}];

// ✅ Fine — input items already carry a json property, so returning them unchanged is a valid passthrough
return $input.all();
```

### 真正会出错的返回

```javascript
// ❌ FAILS: primitive — n8n errors "Code doesn't return items properly"
return "processed";

// ❌ FAILS: null / undefined — nothing to pass to the next node
return null;
```

**为何重要**：规范的 `[{json: {...}}]` 没有歧义，且在两种模式下行为相同。n8n 在 All Items 模式下会自动规范化裸对象和对象数组，但原始值或 `null` 返回没有东西可包装，会导致执行中断。

**参见**：[ERROR_PATTERNS.md](ERROR_PATTERNS.md) #3 查看详细的错误解决方案

---

## 常见模式总览

来自生产工作流的最有用的 Code 节点形态，供 Code 通过闸门后使用。其中几个有原生等价物（总计 → Summarize，top-N → Sort + Limit，JSON 对比 → Compare Datasets，字符串聚合 → Aggregate 或 Summarize 的 `concatenate`）；模式库中的每个模式开头都会给出其原生替代。完整库覆盖 10 种模式：多源聚合、正则过滤、markdown/结构化文本解析、JSON 对比、CRM/表单转换、发布处理、带计算字段的数组转换、Slack Block Kit 格式化、top-N 排名和字符串聚合报表——各带变体。

**参见**：[COMMON_PATTERNS.md](COMMON_PATTERNS.md) 查看 10 个详细的生产模式（以及最佳实践部分：校验输入、try-catch、尽早过滤、数组方法优于循环、console.log 调试）。

---

## 错误预防——高频错误

Code 节点反复出现的失败，按大致频率排序：

1. **空代码 / 缺少 return** —— 始终以 `return [...]` 结尾，并确保*每个*分支都有返回。
2. **把表达式语法当代码** —— 不要在属于 JavaScript 的地方写 `{{ }}`（`return {{ $json.x }}` 是语法错误）。使用 `` `${$json.field}` `` 或 `$input.first().json.field`。*字符串字面量内部*的 `{{ }}` 没问题——那只是 n8n 不会求值的字面文本。
3. **返回形状** —— 优先 `return [{json:{...}}]`。裸的 `return {…}` 在 All Items 模式下会自动包装，但返回原始值（字符串/数字）或 `null` 才是真正会失败的。
4. **缺少空值检查** —— 使用可选链：`item.json?.user?.email || 'fallback'`。
5. **Webhook body 嵌套** —— `$json.email` 是 undefined；使用 `$json.body.email`。
6. **鉴权辅助被禁**（`httpRequestWithAuthentication`）且 `$env` 被禁——密钥走凭据/HTTP Request 节点，不走 Code 节点沙箱。

**参见**：[ERROR_PATTERNS.md](ERROR_PATTERNS.md) 综合指南——每个错误的错误/正确代码、转义规则、沙箱限制（错误 #6–#7）、预防清单和快速错误信息查找表。

---

## 内建函数与辅助工具

```javascript
// HTTP requests (no auth — see sandbox note below)
const res = await this.helpers.httpRequest({ method: 'GET', url: 'https://api.example.com/data' });

// DateTime (Luxon): now, formatting, arithmetic
const now = DateTime.now();
const formatted = now.toFormat('yyyy-MM-dd');
const tomorrow = now.plus({ days: 1 });

// $jmespath() — query JSON structures
const adults = $jmespath($input.first().json, 'users[?age >= `18`]');

// $getWorkflowStaticData() — data that persists across executions
```

**沙箱（自 n8n v2.0 起，JsTaskRunnerSandbox）：** 访问器是 `this.helpers.httpRequest()` —— 裸 `$helpers` 全局在这里**未定义**（`$helpers.httpRequest()` 会抛出 `ReferenceError`）。在 `this` 丢失的嵌套 async 函数中，用 `await fn.call(this, ...)` 调用。`this.helpers.httpRequestWithAuthentication` 和 `this.helpers.requestWithAuthenticationPaginated` 在拒绝清单上（→ `UnsupportedFunctionError`）；鉴权调用请使用带凭据的 **HTTP Request 节点**（首选）、子工作流，或仅当 token 本来就作为数据流经工作流时，才在 `this.helpers.httpRequest()` 上手动加 `Authorization: Bearer ${token}` 头。`N8N_BLOCK_ENV_ACCESS_IN_NODE=true` 时 `$env` 被禁；`require()` 仅对白名单模块可用。`Buffer`、`URL` 和标准 JS 全局对象（Math、JSON、Object、Array）始终可用。

**参见**：[BUILTIN_FUNCTIONS.md](BUILTIN_FUNCTIONS.md) 完整参考——httpRequest 全部选项、全部 DateTime/Luxon 操作、JMESPath 模式、静态数据用例和沙箱限制细节。

---

## 最佳实践

- **先校验输入** —— 处理前防护空数组 / 缺失的 `.json`。
- **对有风险的工作（HTTP 调用）用 try-catch**，返回错误对象而不是崩溃。
- **优先数组方法**（`filter`/`map`/`reduce`）而非手写循环。
- **尽早过滤，延后转换** —— 在昂贵操作之前先缩小数据集。
- **描述性命名**，用 `console.log()` 调试（输出到浏览器控制台）。

**参见**：[COMMON_PATTERNS.md](COMMON_PATTERNS.md) → "Best Practices" 查看各条目的代码示例。

---

## 生产环境注意事项

来自真实部署的血泪教训——此处为摘要，代码在 [DATA_ACCESS.md](DATA_ACCESS.md) → "Production Gotchas"：

- **SplitInBatches 的输出反直觉**：`main[0]` = **done**（在全部批次完成后触发一次），`main[1]` = **每个批次**（循环体）。在 done 输出之后加一个 **Limit 1** 节点作为保险。
- **迭代次数就是成本**：每次循环迭代都让整个循环体重新穿过引擎（每次约 0.8 ms 开销）。`batchSize: 1` 等价于循环版的 *Each Item* —— 在真实约束（速率限制、页大小、内存）允许下用最大批次，或者干脆不循环。
- **跨迭代累积（关键）**：循环结束后，`$('Node Inside Loop').all()` 只返回最后一次迭代的数据。通过 `$getWorkflowStaticData('global')` 累积（循环前重置、循环内推入、循环后读取）。
- **pairedItem**：当输出的条目与输入不是 1:1 映射时，设置 `pairedItem: { item: i }`，否则下游 Set 节点会报 `paired_item_no_info` 失败。
- **节点引用语法**：`$('Node').first().json` 或 `$('Node').all()` —— 绝不在引用上直接 `.json`。
- **浮点精度**：货币比较放在分一级 —— `Math.round(a*100) !== Math.round(b*100)` —— 以避免浮点噪声造成误判。

---

## 何时使用 Code 节点

Code 是最后一级，排在该服务自己的节点、能胜任的原生节点、以及该节点内一个短表达式之后。
本 Skill 开头的闸门就是那道测试；这是它核对的封闭清单：

| Code 适合 | 示例 | 不适合 Code |
|---|---|---|
| 没有节点能表达的循环或递归 | 展平未知深度的树；多趟匹配 | 只有一层嵌套 → Split Out |
| 跨执行的状态 | `$getWorkflowStaticData` 中的计数器或游标 | "只要新条目" → 跨执行的 Remove Duplicates |
| 没有节点能处理的解析 | 定宽记录、自定义日志格式 | CSV / XLSX / PDF / XML / HTML → Extract From File、XML、HTML |
| 白名单内的库 | 实例允许的 `require('some-lib')` | 哈希 / HMAC / UUID → Crypto |
| 重型全量处理 | 数千条数据、转换受限、用户明示或实测得出 | 几百条 → 原生节点 |
| 一个短节点替代 4+ 个拼接节点 | 约 15 行，否则是一条只做数据整形的 Set → Split Out → Set → Aggregate 链 | 链中含真实路由或 I/O |

不在清单上，所以不用 Code：过滤（Filter）、路由（IF / Switch）、总计与计数（Summarize）、top-N（Sort + Limit）、
去重（Remove Duplicates）、连接（Merge）、对比（Compare Datasets）、日期（Date & Time 或 Luxon 表达式）、API 调用
与分页（HTTP Request）、加密与 XML（Crypto、XML）。

每个留下的 Code 节点都带备注 `Why Code: <考虑过的原生节点> — <理由>`（设置 `notes`，并
设 `notesInFlow: true` 以显示在画布上）。create/update Hook 会在 Code 节点没有此类备注时提醒你。

---

## 与其他 Skill 的集成

### 协作的 Skill：

**n8n Expression Syntax**：
- 表达式在其他节点中使用 `{{ }}` 语法
- Code 节点直接使用 JavaScript（无 `{{ }}`）
- 何时用表达式 vs 代码

**n8n MCP Tools Expert**：
- 如何找到 Code 节点：`search_nodes({query: "code"})`
- 获取配置帮助：`get_node({nodeType: "nodes-base.code"})`
- 校验代码：`validate_node({nodeType: "nodes-base.code", config: {...}})`

**n8n Node Configuration**：
- 模式选择（All Items vs Each Item）
- 语言选择（JavaScript vs Python）
- 理解属性依赖

**n8n Workflow Patterns**：
- 转换步骤中的 Code 节点
- Webhook → Code → API 模式
- 工作流中的错误处理

**n8n Validation Expert**：
- 校验 Code 节点配置
- 处理校验错误
- 自动修复常见问题

---

## 快速参考清单

部署 Code 节点前，核对：

- [ ] **通过了闸门** - 没有原生节点适用；`notes` 以 `Why Code:` 开头
- [ ] **代码非空** - 必须有实际逻辑
- [ ] **存在 return 语句** - 返回 items，而不是原始值/`null`
- [ ] **规范返回格式** - 每条：`{json: {...}}`（裸对象会自动包装，但请显式写出）
- [ ] **数据访问正确** - 使用 `$input.all()`、`$input.first()` 或 `$input.item`
- [ ] **没有把 `{{ }}` 写成代码** - 使用 JavaScript 模板字面量：`` `${value}` ``
- [ ] **错误处理** - 对 null/undefined 输入使用守卫子句
- [ ] **Webhook 数据** - 来自 webhook 的数据通过 `.body` 访问
- [ ] **模式选择** - 大多数情况用 "All Items"
- [ ] **性能** - 优先 map/filter 而非手写循环
- [ ] **输出一致** - 所有代码路径返回相同结构

---

## 附加资源

### 相关文件
- [DATA_ACCESS.md](DATA_ACCESS.md) - 全面的数据访问模式
- [COMMON_PATTERNS.md](COMMON_PATTERNS.md) - 10 个经过生产检验的模式
- [ERROR_PATTERNS.md](ERROR_PATTERNS.md) - 5 大错误及解决方案
- [BUILTIN_FUNCTIONS.md](BUILTIN_FUNCTIONS.md) - 完整的内建参考

### n8n 文档
- Code Node 指南：https://docs.n8n.io/code/code-node/
- 内建方法：https://docs.n8n.io/code-examples/methods-variables-reference/
- Luxon 文档：https://moment.github.io/luxon/

---

**准备好在 n8n Code 节点中编写 JavaScript 了！** 从简单的转换开始，用错误模式指南避开常见错误，需要生产级示例时参考模式库。
