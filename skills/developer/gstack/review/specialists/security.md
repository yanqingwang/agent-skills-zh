> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/security.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Security Specialist 评审清单

范围：当 SCOPE_AUTH=true OR (SCOPE_BACKEND=true AND diff > 100 lines) 时
输出：JSON 对象，每条发现一行。Schema：
{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"security","summary":"...","fix":"...","fingerprint":"path:line:security","specialist":"security"}
可选字段：line、fix、fingerprint、evidence、test_stub。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

---

本清单比主 CRITICAL pass 更深入。主代理已检查 SQL 注入、竞态条件、LLM 信任与枚举完整性。本 specialist 专注于 auth/authz 模式、密码学误用与攻击面扩张。

## 类别

### 信任边界处的输入校验
- controller/handler 层接受用户输入而未做校验
- 查询参数直接用于数据库查询或文件路径
- 请求体字段未做类型检查或 schema 校验即接受
- 文件上传未做类型/大小/内容校验
- webhook payload 未做签名验证即处理

### Auth 与授权绕过
- endpoint 缺少鉴权中间件（检查路由定义）
- 授权检查默认"允许"而非"拒绝"
- 角色提升路径（用户可修改自己的角色/权限）
- 直接对象引用漏洞（用户 A 通过改 ID 访问用户 B 的数据）
- 会话固定或会话劫持机会
- token/API key 校验不检查过期
- 绕过正确守卫的错误页：共享的 403/404/500 渲染器在授权路径之外构建页面主体，被拦截的请求仍会返回该角色不应看到的内部名称、计数或导航。要读错误模板及其上下文构建器，而不只是守卫本身
- 角色降级后仍存续的所有权：创建时记录的授权，在用户角色被降低并再次登录后仍然能打开对象。每次读取都必须对照当前角色重新检查所有权
- 对同一对象的列表、详情与文件/下载访问要作为一个条目一起审计：每条通常经由不同的代码路径解析该对象，所以要分别对照角色矩阵逐条检查
- 在校验回调的 one-time state 值之前就清除、重生成或重绑会话的账号/身份切换：任何强制导航到该 URL 都会把用户登出（CSRF）。还要检查 denied、cancelled 与 error 分支，那些分支若保留先前会话，用户会继续以先前身份操作

### 注入向量（SQL 之外）
- 通过参数可控的 subprocess 调用注入命令
- 用户输入进入模板注入（Jinja2、ERB、Handlebars）
- 目录查询中的 LDAP 注入
- 用户可控 URL 导致的 SSRF（fetch、重定向、webhook 目标）
- 用户可控文件路径导致的路径穿越（../../etc/passwd）
- HTTP 头中用户可控值导致的 header 注入

### 密码学误用
- 安全敏感操作使用弱哈希算法（MD5、SHA1）
- token 或密钥使用可预测随机数（Math.random、rand()）
- 对密钥、token 或摘要使用非常量时间比较（==）
- 硬编码加密密钥或 IV
- 口令哈希缺少盐

### Secret 暴露
- 源码中的 API key、token 或密码（注释里也算）
- 应用日志或错误信息中记录的 secret
- URL 中的凭据（query 参数或 URL 内 basic auth）
- 返回给用户的错误响应中的敏感数据
- 应加密存储却以明文存放的 PII

### 经逃生舱口的 XSS
- Rails：对用户可控数据使用 .html_safe、raw()
- React：用 dangerouslySetInnerHTML 渲染用户内容
- Vue：用 v-html 渲染用户内容
- Django：对用户输入使用 |safe、mark_safe()
- 通用：用未清洗数据赋值 innerHTML

### 反序列化
- 反序列化不可信数据（pickle、Marshal、YAML.load、对可执行类型的 JSON.parse）
- 接受来自用户输入或外部 API 的序列化对象而未做 schema 校验
