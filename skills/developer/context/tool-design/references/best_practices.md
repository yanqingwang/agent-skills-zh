> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/tool-design/references/best_practices.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 工具设计最佳实践

本文档为面向 Agent 系统的工具设计提供补充性的最佳实践与指引。

## 工具哲学

工具是 Agent 与世界之间的主要接口。传统 API 面向理解底层系统的开发者，而工具必须面向从描述推断意图、从自然语言请求生成调用的语言模型来设计。这一根本差异要求我们重新思考如何设计和记录工具接口。

目标是造出 Agent 无需大量试错就能发现、理解并正确使用的工具。工具定义里的每一处歧义都是一个潜在失败模式。每个含糊的参数名都在逼 Agent 猜。每个缺失的示例都让 Agent 在边界情况面前没有指引。

## 描述工程原则

### 原则 1：回答根本性问题

每条工具描述都应清楚回答四个问题。工具做什么？用具体措辞准确说明工具完成什么，避免"有助于""可用于"这类含糊说法。何时使用？给出具体的触发条件和场景，既包括直接触发，也包括表明工具适用的间接信号。接受哪些输入？记录参数的类型、约束和默认值，说明每个参数控制什么。返回什么？描述输出的格式与结构，包括成功响应和错误情况的示例。

### 原则 2：保持结构一致

在你代码库的所有工具描述之间保持结构一致。Agent 遇到新工具时，应能凭借从其他工具学到的模式，预测到哪里找特定信息。这能降低认知负担，并防止格式不一致导致的错误。

推荐的结构包括：第一句简短描述、带使用场景的详细说明、类型信息清晰的参数部分、描述输出结构的返回部分，以及列出可能的失败模式和恢复指引的错误部分。

### 原则 3：给出具体示例

示例弥合抽象描述与实际使用之间的鸿沟。要包含：展示常见参数组合的典型调用示例、边界情况及其处理方式的示例、错误响应及相应恢复动作的示例。

好示例具体而非泛泛。不要写"Use an ID like '123'"，要写"Use format: 'CUST-######' (e.g., 'CUST-000001')"。不要写"Provide a date"，要写"Format: 'YYYY-MM-DD' (e.g., '2024-01-15')"。

## 命名约定

### 参数命名

参数名应能自解释。用的名字要能清楚表明用途，无需额外解释。除 "id"、"url" 这类广为人知的缩写外，优先用完整单词而非缩写。相似概念在各工具间使用一致的命名。

好的参数名如 customer_id、search_query、output_format、max_results、include_details。差的参数名如 x、val、param1、info。

### 枚举值

当参数接受枚举值时，所有工具使用一致的命名。布尔风格选项用前缀模式：肯定选项用 "include_"（include_history、include_metadata），否定选项用 "exclude_"（exclude_archived、exclude_inactive）。类别值用一致的术语，如 "format": "concise" | "detailed"，不要在部分工具里用 "format": "short" | "long"、另一些里用 "format": "brief" | "complete"。

## 错误消息设计

### 双重受众

错误消息服务两类需求不同的受众。调试问题的开发者需要详细的技术信息，包括栈跟踪和内部状态。从失败中恢复的 Agent 需要可执行的指引，告诉它哪里出了错、如何纠正。

设计错误消息时，把 Agent 的恢复当作首要考量。用清晰的语言说明具体哪里出错了。提供解决指引，描述 Agent 接下来该做什么。输入错误要附上正确格式。加上有效输入的示例。

### 错误消息结构

```json
{
    "error": {
        "code": "INVALID_CUSTOMER_ID",
        "category": "validation",
        "message": "Customer ID 'CUST-123' does not match required format",
        "expected_format": {
            "description": "Customer ID must be 9 characters",
            "pattern": "CUST-######",
            "example": "CUST-000001"
        },
        "resolution": "Provide a customer ID matching pattern CUST-######",
        "retryable": true
    }
}
```

### 常见错误模式

校验错误应说明收到了什么、期望什么格式、如何纠正。限流错误应说明等待时间和重试指引。未找到错误应建议替代方法或验证步骤。系统错误应说明重试是否合适，并给出替代方案。

## 响应格式优化

### token 与准确性的权衡

冗长的响应信息全面，但消耗大量上下文 token。简洁的响应省 token，但可能缺必要细节。最优做法是提供格式选项，让 Agent 按需选择合适的详细程度。

### 格式选项模式

```python
def get_customer_response(format: str = "concise"):
    """
    Retrieve customer information.
    
    Args:
        format: Response format - 'concise' for key fields only,
                'detailed' for complete customer record
    """
    if format == "concise":
        return {
            "id": customer.id,
            "name": customer.name,
            "status": customer.status
        }
    else:  # detailed
        return {
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "address": customer.address,
            "status": customer.status,
            "created_at": customer.created_at,
            "history": customer.history,
            "preferences": customer.preferences
        }
```

### 各格式的适用时机

快速验证或简单查询、只需要确认、以及初次检索后的后续工具调用，用简洁格式。要基于客户数据做决策、输出要作为其他处理的输入、以及正确性需要完整上下文时，用详细格式。

## 工具集合设计

### 管理工具膨胀

随着 Agent 系统增长，工具集合容易膨胀。更多工具带来更多能力，但也带来选择难题。研究表明，工具描述重叠会造成模型混淆。关键认识是：如果人类工程师都无法明确说出某情况下该用哪个工具，就不能指望 Agent 做得更好。

### 合并准则

把表示同一工作流中先后步骤的工具合并为一个处理整个工作流的工具。例如，与其用 list_users、list_events 和 create_event，不如实现 schedule_event，一次调用完成查询空闲时段并完成排期。

行为根本不同的工具，即使共享部分功能，也应保持独立。在不同上下文中使用的工具应维持分离，避免混淆。

即使工具工作在相近领域，也要维持清晰边界。通过精心设计把功能重叠降到最低。

### 工具选择指引

设计工具集合时，考虑 Agent 做出正确选择需要什么信息。如果多个工具都可能适用于某情况，在描述中澄清区别。用命名空间建立逻辑分组，帮助 Agent 在工具空间中导航。

## 测试工具设计

### 评估标准

按清晰度、完整性、可恢复性、效率和一致性评估工具设计。清晰度衡量 Agent 能否判断何时使用该工具。完整性衡量描述是否包含全部必要信息。可恢复性衡量 Agent 能否从错误中恢复。效率衡量工具是否支持合适的响应格式。一致性衡量工具是否遵循命名与模式约定。

### Agent 测试模式

用有代表性的 Agent 请求来测试工具，并评估由此产生的工具调用：

1. 准备包含多样化 Agent 请求的测试用例
2. 让 Agent 为每个请求构造工具调用
3. 对照预期模式评估调用正确性
4. 识别常见失败模式
5. 根据发现改进工具定义

## 需要避免的反模式

### 模糊的描述

差："Search the database for customer information."。这留下太多未回答的问题。哪个数据库？能查到什么信息？查询该是什么格式？

好："Retrieve customer information by ID or email. Use when user asks about specific customer details, history, or status. Returns customer object with id, name, email, account_status, and optional order history."

### 难懂的参数名

差：参数名叫 x、val 或 param1，逼 Agent 猜含义。

好：参数名叫 customer_id、max_results 或 include_history，自解释。

### 缺失错误处理

差：工具失败时只有笼统的错误，或根本没有错误处理。

好：工具提供具体的错误类型、消息和解决指引。

### 命名不一致

差：相似概念在部分工具里用 id、另一些用 identifier，部分用 customer_id、另一些用 user_id。

好：相似概念在所有工具间保持一致的命名模式。

## 工具设计检查清单

部署新工具之前，逐项确认：描述清楚说明工具做什么、何时使用。所有参数都有描述性名称和清晰的类型信息。返回值有结构和示例的文档。错误情况都有可执行的错误消息覆盖。工具遵循其他地方使用的命名约定。示例展示了常见使用模式。响应大小差异明显时提供格式选项。
