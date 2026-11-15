> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/testing.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Testing Specialist 评审清单

范围：Always-on（每次评审）
输出：JSON 对象，每条发现一行。Schema：
{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"testing","summary":"...","fix":"...","fingerprint":"path:line:testing","specialist":"testing"}
可选字段：line、fix、fingerprint、evidence、test_stub。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

如果调用方明确要求 ASCII 覆盖图，先在一次专用工具调用中直接读取
指定的源文件与测试文件。该工具调用只限这两次文件读取，可以使用原生
Read 调用，或 `cat -n src/file && echo ---- && cat -n test/file` 这类简单的
shell 展示方式。diff、包文件、配置或其他上下文放在单独的工具调用里读取。
然后在任何 JSON 发现之前输出覆盖图。每个公开或被修改的函数使用一个函数根，
把 `[OK]` 或 `[GAP]` 标记放在与已测或缺失路径相同的分支行上，
并把图例保留在同一覆盖图块内：

```text
src/billing.ts
processPayment(amount, currency)
├── valid USD happy path returns success [OK]
└── invalid amount / unsupported currency branches [GAP]
refundPayment(paymentId, reason)
└── refund success and guard branches not imported or untested [GAP]
Legend: [OK] tested [GAP] no test
```

不要把汇总表、散文段落或远处的嵌套标记当作唯一的覆盖证据。已覆盖的
happy path 行必须写出成功、有效或具体被测的输入路径；gap 行必须留在
拥有该缺失路径的函数之下。

---

## 类别

### 探索性假设

父代理会在 Fix-First 之前运行一次共享的探索式 QA pass，包括跳过 specialists 的小 diff。
向该 pass 提供高风险的变更契约、不利场景和原生测试候选；不要另起 explorer，不要编辑
product/tests，不要 commit。测试提案使用 `test_stub` 并保留调用方的审批要求。
在适用处核查真实的请求/队列/存储效果、重试、重复与中断恢复。覆盖图或测试数量不是
执行证据。对被提升为回归的发现，修复之前要求复现 bug 的失败证据，修复之后要求
绿色加上原有/相邻探针；绝不接受输出错误的 golden，也不接受被丢弃的有效红测试。
单测适合逻辑；真实的集成/E2E 测试保护 mock 藏起来的边界。

### 缺失负路径测试
- 处理错误、拒绝或无效输入的新代码路径，却没有对应测试
- 未测试的 guard 子句与提前返回
- try/catch、rescue 或错误边界中的错误分支，没有失败路径测试
- 代码中有断言的权限/鉴权检查，却从未测试"被拒绝"的情况

### 缺失边界情况覆盖
- 边界值：零、负数、max-int、空字符串、空数组、nil/null/undefined
- 单元素集合（循环差一错误）
- 用户可见输入中的 Unicode 与特殊字符
- 没有竞态测试的并发访问模式

### 负向断言
- 新增的"某物不存在"断言（`not.toContain`、`not in`、`assertNotIn`，或对过去
  能成功的调用加 `pytest.raises`）记录的是行为移除，不是覆盖。引用授权该移除的
  spec 行、计划条目或 PR 文本；都没有时，把它报告为"以测试形式发布的产品决策"。
- 本 diff 中的重命名或删除可能掏空一条既有的负向断言：断言旧 token 不存在的测试
  从此永远通过，什么也没守住。对 diff 重命名或删除的每个标识符、flag、标题或
  字符串，grep 整个测试套件中点名旧值的负向断言，包括断言其他事物的测试内部，
  把每一处报告为覆盖缺口，其 fix 写出新值。

### 测试隔离违规
- 测试共享可变状态（类变量、全局单例、未清理的 DB 记录）
- 顺序依赖的测试（按顺序通过，随机化后失败）
- 依赖系统时钟、时区或 locale 的测试
- 不用 stub/mock 而发起真实网络调用的测试

### 不稳定测试模式
- 依赖时序的断言（sleep、setTimeout、超时过紧的 waitFor）
- 对无序结果断言顺序（hash 键、Set 迭代、async 完成顺序）
- 依赖外部服务（API、数据库）且无回退的测试
- 无种子控制的随机测试数据

### 缺失安全强制测试
- controller 中的 auth/authz 检查，没有"未授权"情况的测试
- 限流逻辑没有测试证明它真的会拦截
- 输入清洗没有恶意输入测试
- CSRF/CORS 配置没有集成测试

### 覆盖缺口
- 零测试覆盖的新公开方法/函数
- 已改动的方法，现有测试只覆盖旧行为，不覆盖新分支
- 多处调用的工具函数却只有间接测试
- 只有弱测试（★ smoke/存在性/平凡测试，或未通过下方 authoring gate 的新测试）的路径，
  按既有严重级别保持为覆盖缺口；低价值测试永远填不上缺口

### 低价值或与实现耦合的测试
范围：diff 中新增或改动的测试，以及仅供测试用的 production seam。发现一律为
INFORMATIONAL，绝不 CRITICAL，也绝不自动删除：建议在所属边界处重写、扩展现有测试，
或持完整退役卡退役（`test, detects, non_test_callers, search_command, stronger_proof, history, unlocks,
validation`）。每条发现的 `fix` 以 `Repo-wide sweep: run /test-audit.` 结尾。

新增或改动的测试只有四个答案齐备才通过 authoring gate（diff 中若有
`Value: protects=...; fails_when=...; why_new=...; seam=...` 头注释则先读它；可选的
`no_claim=...` 说明绿色不能证明什么、哪些 fixture 或 mock 替代了什么，且绝不豁免
必需的实机检查）：
1. 它保护什么可观察行为、不变量或独立契约？
2. 什么可信回归会让它失败？
3. 现有覆盖为何没有抓住它？优先给现有表驱动测试或共享 fixture 加一行，而不是近乎重复地新建。
4. 它是否需要没有任何生产调用方需要的 production seam（export、flag、wrapper、注入钩子）？需要的话，改在真实边界测试。

Patterns：
- 无断言的覆盖探针
- 自比较与恒等复制
- 复制的 fixture、清单或导出列表
- 未声明为契约的精确源码、import 或字符串 grep
- 在真实边界重复的私有谓词或调用形态测试
- 同一契约的重复调用
- 逐调用方重放共享 helper 的测试
- 唯一目的是保住仅测试可见的 export、全局或 wrapper 的测试
- 唯一调用方是测试的生产代码

Retention bar（永不标记）：独立强制以下契约的测试：公开 API、协议、config、迁移、
存储、安全、平台、默认值、prompt 字节、生成产物（SKILL.md golden）、包、发布或架构
契约；顺序可观察时的调用顺序；源码检查是最便宜的独立守卫时；任何可从包入口
（`package.json` 的 exports/main、index 再导出）到达的东西。静态或慢不是删除的理由。

每条发现的证据放入 `evidence`，字段为 `detects`（该测试实际能检测到什么失败）、
`non_test_callers`、`search_command` 与 `stronger_proof`。对后两种 pattern，对 diff 新增或
导出的每个符号运行 caller 检查，仅当符号匹配 `^[A-Za-z_][A-Za-z0-9_]*$`（否则记录 "caller check
unavailable: unsupported symbol"），符号必须加引号，绝不以未加引号的形式插值：

```bash
git grep -n -F -w -e '<symbol>' -- . ':!test/' ':!tests/' ':!spec/' ':!**/__tests__/**' ':!**/*.test.*' ':!**/*.spec.*' ':!**/*_test.*' ':!**/test_*.py'
```

记录命令、排除项与命中数，并把证据标记为 "grep-only"（它看不到再导出、动态分发或
生成代码）。搜索失败时记录：caller check unavailable: <command>。发现保持
INFORMATIONAL，不提议删除任何东西；手工运行搜索补全证据。（见
~/.claude/skills/gstack/docs/test-value-bar.md#caller-check-unavailable）

跳过带有 `gstack:test-value keep reason="<why>"` 的测试（任意注释语法）。若有跳过，
把其数量与原因合并为一条 INFORMATIONAL 行。对你评审后保留的测试，不发任何发现。

拒绝用词，当发现要说明新测试为何未过 gate 时：
`duplicate_protects`、`needs_seam`、`incomplete_card`、`no_credible_regression`、
`covered_elsewhere`、`implementation_coupled`。

### 无红证据的回归测试
- diff 新增了一个命名或注释为回归的测试，而提交历史与 PR 正文都没有展示它在修复
  之前失败。从未可证失败过的回归测试证明的是 mock，不是修复。INFORMATIONAL；
  要求提供 fails-at-HEAD / passes-after-fix 的记录。
