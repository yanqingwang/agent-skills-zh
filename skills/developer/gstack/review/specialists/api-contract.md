> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/api-contract.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API Contract Specialist 评审清单

范围：当 SCOPE_API=true 时
输出：JSON 对象，每条发现一行。Schema：
{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"api-contract","summary":"...","fix":"...","fingerprint":"path:line:api-contract","specialist":"api-contract"}
可选字段：line、fix、fingerprint、evidence、test_stub。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

---

## 类别

### 破坏性变更
- 从响应体中移除字段（客户端可能依赖它们）
- 更改字段类型（string → number、object → array）
- 给既有 endpoint 增加新的必填参数
- 更改 HTTP 方法（GET → POST）或状态码（200 → 201）
- 重命名 endpoint 且不把旧路径保留为 redirect/alias
- 更改鉴权要求（public → authenticated）

### 版本策略
- 破坏性变更不做版本升级（v1 → v2）
- 同一 API 混用多种版本策略（URL vs header vs query param）
- 弃用 endpoint 却没有 sunset 时间表或迁移指南
- 版本相关逻辑散落在各 controller 中而不集中管理

### 错误响应一致性
- 新 endpoint 返回与既有 endpoint 不同的错误格式
- 错误响应缺少标准字段（error code、message、details）
- HTTP 状态码与错误类型不匹配（错误返回 200、校验失败返回 500）
- 错误信息泄露内部实现细节（stack trace、SQL）

### 限流与分页
- 相似 endpoint 都有限流时，新 endpoint 却没有
- 分页方式变更（offset → cursor）而不向后兼容
- 更改页大小或默认 limit 却不写文档
- 分页响应缺少总数或下一页指示

### 文档漂移
- OpenAPI/Swagger spec 未随新 endpoint 或变更参数更新
- 变更后 README 或 API 文档仍描述旧行为
- 示例请求/响应已失效
- 新 endpoint 或变更参数缺少文档

### 向后兼容
- 旧版本客户端：会不会被破坏？
- 无法强更的移动应用：API 对它们仍然可用吗？
- webhook payload 变更而未通知订阅方
- 使用新功能需要改动 SDK 或客户端库
