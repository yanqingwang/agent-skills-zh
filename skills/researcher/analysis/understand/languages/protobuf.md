> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/protobuf.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Protobuf 语言提示词片段

## 核心概念

- **消息类型**：`message` 块定义结构化数据，字段带类型与编号
- **字段编号**：永久标识符（1-536870911），为向后兼容绝不复用已删除的编号
- **标量类型**：`int32`、`int64`、`string`、`bytes`、`bool`、`float`、`double` 等
- **枚举**：命名整数常量，表示分类值
- **服务**：`service` 块定义 RPC（远程过程调用）方法签名
- **Oneof**：互斥字段组，组内同一时刻只能设置一个字段
- **Repeated 字段**：`repeated` 关键字定义列表/数组字段
- **映射**：`map<key_type, value_type>` 定义字典/哈希字段
- **包与导入**：命名空间组织与跨文件引用
- **Proto2 与 Proto3**：Proto3（当前）取消 required/optional 之分，所有字段默认可选

## 重要文件模式

- `*.proto`：Protocol Buffer 定义文件
- `proto/**/*.proto`：按服务或领域组织的 proto 定义
- `buf.yaml` / `buf.gen.yaml`：Buf 工具配置，用于 lint 与代码生成
- `*_pb2.py` / `*.pb.go` / `*_pb.ts`：生成代码（应从分析中排除）

## 边模式

- Protobuf 文件为实现所声明 RPC 的 gRPC 服务处理器建立 `defines_schema` 边
- 消息类型引用在共享类型的 proto 文件之间创建 `related` 边
- proto `import` 语句在 proto 文件之间创建 `depends_on` 边
- 生成代码文件对其来源的 proto 源文件建立 `depends_on` 边

## 摘要风格

> "Protocol Buffer 定义：用户认证领域的 N 个消息类型与 M 个 RPC 服务。"
> "共享 proto 类型：定义通用请求/响应信封与错误码。"
> "gRPC 服务定义：N 个方法，面向实时数据流与批处理。"
