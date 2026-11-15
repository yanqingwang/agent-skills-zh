> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/SYSTEM_PROMPT.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 系统提示词

系统提示词是 Agent 的承重配置。多数"Agent 不按我想的做"的问题，都能追到一条太长、太含糊或混装多个关注的系统提示词上。

本文件立场鲜明：系统提示词只管**人设与全局行为**，工具专属指令推进工具描述里，然后持续迭代。系统提示词放在 Agent 节点的 `options.systemMessage` 里。

---

## 系统提示词管什么

1. **人设/角色。** 是谁、范围、语气。
2. **全局输出规则。** 格式约定、展示协议（例如"用 `![]()` markdown 展示图片"）、语言。
3. **拒绝与安全行为。** Agent 不该做什么：具体的边界胜过通用的套话。
4. **通用上下文。** 当前日期、用户姓名/角色、公司/产品背景。
5. **跨工具流程规则。** "生成之后，总是通过展示协议展示"、"破坏性操作前先确认"，这类涉及多个工具的事。
6. **文件处理注入。** 聊天里带上传文件时，注入存储键，让 Agent 能在工具调用中引用它们（机制 → **n8n-binary-and-data**）。

它不管：单个工具的用法说明。那些放进工具的描述。

---

## 总要带上当前日期

写死的日期立刻过时。在运行时注入：

```
Current date: {{ $now }}
```

或带格式：

```
The current time is {{ $now.format('DDDD TTTT') }}
```

---

## 模块化分工

```
System prompt    → Persona, global behavior, format rules, file handling
Tool description → How to use THIS tool, its parameters, when to pick it over others
$fromAI desc.    → What value to put in this specific parameter
```

为什么这样分：

- **复用。** 描述到位的工具在任何 Agent 里都能用，系统提示词不用再教一遍。
- **token 效率。** 工具细节只在模型考虑那个工具时才"加载"。塞进系统提示词的每个工具说明，每一轮都在烧 token。
- **可维护性。** 改一处工具描述，而不是翻找 5000 token 提示词里埋着的一段。

### 什么该挪到哪

| 原在系统提示词里 | 更好的位置 |
|---|---|
| "使用 Generate Image 时，偏好真实摄影风格而非 `8k cinematic`" | `Generate Image` 工具描述 |
| "用户上传图片并要求改背景时，去编辑它，不要新生成" | `Edit Image` 工具描述（并在 `Generate Image` 上加"不要使用"边界） |
| "视频工具用 9:16 宽高比" | `Generate Video` 工具描述 |
| "用 markdown 图片嵌入回复：`![alt](url)`" | **系统提示词**（全局展示规则） |
| "未经同意拒绝生成真人图片" | **系统提示词**（全局安全） |
| "今天是 2026-04-25" | **系统提示词**，写成 `{{ $now }}`（通用上下文，运行时计算） |

前三条挪出去；后三条留下来。

---

## 提示词的存放

内联（直接写进 `systemMessage`）对第一个 Agent 或任何只在一处使用的提示词都合适。1500 token 的内联提示词是正常形态，别劝新手去做外置。

外置的真正理由是**拼装**，不是长度。可复用的上下文块（`COMPANY_DESCRIPTION`、`BRAND_VOICE`、`CURRENT_PROMOTION`）各自有一个权威存放处，需要它们的每条提示词都引用那个存放处。看到以下情况之一时建议这么做：

- 多个 Agent 共享同一份上下文（相同的产品描述、相同的合规措辞）。
- 各块按自己的节奏漂移（`COMPANY_DESCRIPTION` 按季度，`CURRENT_PROMOTION` 按周）。
- 提示词的一部分归非工程师所有（市场部管品牌语气，法务管披露文案）。
- 你想对某一块做 A/B 测试而不动其余部分。

都不沾就保持内联。没有第二个消费者来回本时，中途重构提示词的成本高于收益。

### 拼装怎么做

工作流开始时把每个块加载进来（一块一个节点：一个 Data Table 的 `Get Row`、一次 HTTP 抓取，或一个 Set 节点），然后在 `systemMessage` 里内联引用它们该出现的位置：

```
=You are the assistant for {{ $('Company Description').first().json.value }}.

## Market positioning
{{ $('Market Fit').first().json.value }}

## Brand voice
{{ $('Brand Voice').first().json.value }}

Current date: {{ $now }}
User: {{ $('Lookup').first().json.name }}
```

来源可混搭：**Data Table**（共享块的默认选择，UI 里可编辑）、**n8n Variables**（`$vars.X`，付费计划，适合品牌名这类短共享值）、或**运行时计算**（`$now`、当前用户、可用文件）。

---

## 常见模式

### 要放进去

- **展示协议**，输出需要特定格式时（markdown 图片语法、链接格式、代码块约定）。
- **会话风格提示**，面向用户的 Agent（"破坏性动作前先问一个澄清问题"）。
- **边界**，这个 Agent 特有的（"只回答领域 X 的问题，否则转介"）。
- **通用上下文**，每次执行都会变的（日期、用户身份、文件）。

### 别放进去

- **单个工具的用法说明**，挪去工具描述。
- **泛泛的安全话术**，模型内置就有；重复只加 token 不改行为。留给具体风险。
- **"You are a helpful assistant" 式开场白**，换成一个具体角色。
- **没有挣到 token 的冗长示例**，一个锋利的示例胜过五个平庸的。

---

## 迭代循环

把系统提示词当代码对待：

1. 用有代表性的输入跑 Agent。
2. 记下它哪里做错了。
3. 判断：改系统提示词、改工具描述，还是改下游校验？
4. 做能解决它的最小改动。
5. 在同一批输入**加上**一两个新输入上重测。
6. 盯住之前正常输入上的回归。

多数"Agent 不听我的指令"问题，是系统提示词、工具描述和模型默认行为三者之间的冲突。先解决冲突。

---

## 反模式

| 反模式 | 症状 | 修法 |
|---|---|---|
| "You are a helpful assistant" 加零 specifics | 回复千篇一律，没有身份 | 换成具体角色和范围 |
| 5000 token 提示词，每个工具一节 | token 开销大、响应慢、难改 | 把工具小节挪去工具描述 |
| 写死日期 / "当前年份" | 立刻过时 | 运行时注入 `{{ $now }}` |
| 一堆 `DON'T` 规则 | 模型变得防御性强，动不动拒绝 | 尽量改写成正向指令 |
| 堆叠粘贴的"示例" | 货崇拜式照搬，通常不值这些 token | 一个锋利的示例，或干脆没有 |
| 每次执行变化的上下文被写死 | 难以更新 | 用模板 + 变量构建提示词 |

---

## 交叉引用

- 工具描述是分工的另一半 → **TOOLS.md**
- 结构化输出的系统提示词那一半 → **STRUCTURED_OUTPUT.md**
- 文件处理注入的机制 → **n8n-binary-and-data**
