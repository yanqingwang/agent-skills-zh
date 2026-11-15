> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/performance.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Performance Specialist 评审清单

范围：当 SCOPE_BACKEND=true OR SCOPE_FRONTEND=true 时
输出：JSON 对象，每条发现一行。Schema：
{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"performance","summary":"...","fix":"...","fingerprint":"path:line:performance","specialist":"performance"}
可选字段：line、fix、fingerprint、evidence、test_stub。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

---

## 类别

### N+1 查询
- ActiveRecord/ORM 关联在循环中遍历而没有预加载（.includes、joinedload、include）
- 迭代块（each、map、forEach）内本可批量化的数据库查询
- 触发懒加载关联的嵌套 serializer
- 逐字段查询而不批量的 GraphQL resolver（检查是否使用 DataLoader）

### 缺失数据库索引
- 无索引列上的新 WHERE 子句（检查 migration 文件或 schema）
- 非索引列上的新 ORDER BY
- 无复合索引的复合查询（WHERE a AND b）
- 新增外键列但没有索引

### 算法复杂度
- O(n^2) 或更差的模式：集合上的嵌套循环、Array.map 内嵌 Array.find
- 本可用 hash/map/set 查找的重复线性搜索
- 循环中的字符串拼接（改用 join 或 StringBuilder）
- 对大集合重复排序或过滤，而一次即可完成

### 包体积影响（前端）
- 已知很重的新生产依赖（moment.js、lodash 全量、jquery）
- Barrel import（import from 'library'）而非深路径 import（import from 'library/specific'）
- 未优化就提交的大体积静态资源（图片、字体）
- 缺少路由级 chunk 的代码分割

### 渲染性能（前端）
- 请求瀑布：本可并行（Promise.all）的串行 API 调用
- 不稳定引用导致的多余重渲染（render 中新建对象/数组）
- 昂贵计算缺少 React.memo、useMemo 或 useCallback
- 在循环中先读后写 DOM 属性造成的 layout 抖动
- 首屏以下图片缺少 loading="lazy"

### 缺失分页
- 返回无界结果的列表 endpoint（无 LIMIT、无分页参数）
- 无 LIMIT 且随数据量增长的数据库查询
- API 响应内嵌完整嵌套对象，而不是 ID 加展开

### 异步上下文中的阻塞
- async 函数内的同步 I/O（文件读取、subprocess、HTTP 请求）
- 事件循环型 handler 内的 time.sleep() / Thread.sleep()
- 无 worker 分流、阻塞主线程的 CPU 密集计算
