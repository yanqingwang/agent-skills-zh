<!-- AUTO-GENERATED from exploratory.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`qa/sections/exploratory.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

# 共享探索式 QA

**调用方**（/qa、/qa-only、/review 或 /ship）拥有决策、测试、修复与
发布。探索只写报告/证据与自有 fixture 状态；不做工作流、框架安装或
发布。

写 charter 或探测之前按序完成这些 Read。等它们的结果回来再做第一个
探测，绝不放在同一条回复里。不重复本次调用已完成的 Read。
1. 相对已安装 `qa`/`gstack-qa` SKILL.md 目录完整读 `sections/scope.md`
   并选定表面。
2. 完整读下方选定的表面方法。

**功能性表面：**
完整读 `sections/system-functional.md`。

**仅浏览器表面：**
完整读 `sections/qa-patterns.md`。

资产缺失或不可读、前提缺失或未授权都会阻塞受影响探测，不影响独立
安全检查。报告 QA setup 阻塞项。

## 1. Charter 与预检

复用已解析的 REPORT_DIR；否则自有一个新的 `.gstack/qa-reports` 子
目录。每个行为写一份**charter**：契约、风险、入口、隔离、退出条件、
来源、命令与输入。charter 以 Markdown 存进报告。

/review 与 /ship 不要求计划/服务器。
5 分钟或 12 个探测先到为止（跨表面共享 SECONDS=300）。
显式的计划检查与重验证在此冒烟预算之外仍然必需。
/qa 与 /qa-only：
- Browser Quick：SECONDS=180。Browser Full/Regression：SECONDS=900。
- Functional Full、Quick 与 Regression 无默认总计时器。
SECONDS 取模式/调用方限制中较短者；无限制模式用调用方的边界。
没有总时间限制时不创建 DEADLINE_FILE；宣布有限的命令超时。
范围内的契约测完或被阻塞即停：每个字段的每条文档化输入规则都需要一
个只破坏它、满足其余全部规则的探测；探测/时间上限内未覆盖的规则进
limits。时钟/检查点用 REPORT_DIR；混合独立运行用 REPORT_DIR/browser
与 REPORT_DIR/functional，最终一份报告落在 REPORT_DIR。调用方路径
优先。
下文用名（每个路径都加引号）：
- PROBE_DIR：按上一行约定的本表面自有探测目录。DEADLINE_FILE：
  `PROBE_DIR/deadline.json`，仅在有界运行时存在。
- SECONDS：上方设定的总探测预算。NNN：每次捕获/检查点用新的三位 ID
  （001、002……）；绝不复用。
- DEADLINE_TOOL =
  `$HOME/.claude/skills/gstack/bin/gstack-qa-deadline`，deadline
  守卫：`start` 创建 DEADLINE_FILE，`status` 打印 `remainingMs` 与
  `expired`，`run` 执行一条命令并在 deadline 到时停掉它。
- EVIDENCE_TOOL =
  `$HOME/.claude/skills/gstack/bin/gstack-qa-evidence`，功能性证据
  记录器：`capture` 运行一条命令，把 exit code、stdout 与 stderr 存
  到 `PROBE_DIR/.qa-evidence/NNN/`，并打印状态 `complete`、
  `incomplete` 或 `sensitive`。

基线之前启动一次：有界时
`bun DEADLINE_TOOL start DEADLINE_FILE SECONDS [EARLIER_UTC]`。
EARLIER_UTC = 调用方的绝对 deadline（若有）。
功能性：`bun EVIDENCE_TOOL capture PROBE_DIR NNN [--public] --deadline DEADLINE_FILE -- COMMAND ARGS`。
无界时用 `--timeout-ms MS` 替代 `--deadline DEADLINE_FILE`。
--public 需要获批的公开/合成输出；EVIDENCE_TOOL 会筛凭证。完整的
私有捕获，等待对 `PROBE_DIR/.qa-evidence/NNN/observation.json`
（解码后的 stdout）的安全 Read。sensitive/incomplete 捕获不能锚定
检查点。
有界浏览器：`bun DEADLINE_TOOL run DEADLINE_FILE -- COMMAND ARGS`。
不做分离式探测。
绝不重置 DEADLINE_FILE/绕过 DEADLINE_TOOL。过期或 DEADLINE_FILE 无
效/缺失即停止探测；报告未完成的覆盖。QA_DEADLINE 回执不是观察。

## 2. 探测循环

每个探测是一条原生命令/交互加检查，不含记账。
绝不批量探测。

1. 先证明成功：输出**与**持久效果。有界时加守卫；等它完成。
2. **判断是否需要下一个探测。** 有界时跑
   `bun DEADLINE_TOOL status DEADLINE_FILE`。
   已过期或没有安全的下一探测时，STOP 探索；写报告（§4），不是检查
   点。
   **先发布再探测。** 在探测目录创建（浏览器）或组装（功能性）
   `exploration-NNN.json`，有界时与 deadline 同目录，顶层恰好四个
   字段：
   observationCommand：上一个已完成探测的完整外层命令，含守卫。
   observed：其精确解码后的子 JSON（无包装/多余键），或完整非 JSON
   文本。
   hypothesis：为什么 nextCommand。nextCommand：精确命令/请求，有界
   时带守卫。
   保持每个安全的程序 JSON 键值与身份哈希不变。
   扣留不安全的值，披露局限并终止该链条。
   发布前检查字段。不要草稿/占位符或虚构的安全路径脱敏；更正无法修复
   已发布的笔记。
   功能性：不写这个文件；下一次捕获即发布：
   `bun EVIDENCE_TOOL capture PROBE_DIR NNN --deadline DEADLINE_FILE --after PREV --hypothesis 'why' -- CMD`
   （PREV：上一个完整捕获的 ID）。observed 由 EVIDENCE_TOOL 提供；
   绝不手抄。
   浏览器检查点用 Write。
   等检查点成功发布后再派发。
   绝不回填或覆盖笔记。
3. 跑那个精确探测；有界时 DEADLINE_TOOL 强制 deadline。
   拒绝按 not-run 报告；保留初始状态/输入/结果。回到第 2 步。
4. 修复之前，从同一初始 fixture 状态经第 2-3 步回放那条精确的失败
   命令/请求（同一原生命令、新捕获 ID），再经这些门做最小化。过期使
   确认/最小化保持未完成。
   另一个输入或一个回归测试不是那次回放。
5. 源码/命令/fixture 变更之后，重新评审并为每个受影响的重验证回到
   第 2 步（未证实 = 受影响）。保留 limits/笔记；状态需要新证据。

## 3. 交还父级

- **/qa：** 父级在验证修复之前拥有严重度、根因与 Phase 8 回归门。
- **/review：** 在 Fix-First 之前返回；test_stub 提案需要 ASK 批准。
- **规划：** 只提议 charter；不执行。

选最小的原生测试：逻辑用单元，状态/请求用集成；只有更小的测试漏掉
旅程时才用 E2E，不自动两者都做。
只 mock 无关服务。
绝不冻结错误输出、削弱测试或删除有效的红色测试。

## 4. 最终报告

用表面报告模板；链接每个检查点。分开写浏览器分数、功能性结果与拟议/
已执行测试。
写 PROBE_DIR/annotations.json
{evidence: [{capture, command, contract, expected, classification}],
limits: ["checkpoint 001"]}（limits：非空字符串数组，不是对象；仅
浏览器时 evidence 为 []）；Markdown 之前跑
`bun EVIDENCE_TOOL materialize PROBE_DIR annotations.json`（填
observed/metadata；打印 reportLinks；每个 PROBE_DIR 跑一次）；分类由
你做。为每个安全捕获做注释，包括失败/回放：漏掉的捕获就是被扣留，
判定保持 inconclusive。输入变更之前拍的捕获归类 `superseded`；同一
命令在当前输入上重跑后它才关闭。修复之后，所有更早的捕获都算
superseded，即使客户端不打印快照：重跑你判定所依赖的每一个，或将其
报告为开放残留。披露被扣留/不完整的证据。
证据是调用局部的；/ship 每次调用重跑一遍。
前提/预期/观察缺失、超时与拒绝绝不通过。
通过要求全部必需的当前输入契约通过且无必需残留。
必需的失败使 /review 不完整、/ship 受阻，除非用户显式接受那个点名
风险；非交互运行返回 blocked。只有非行为性 diff 才可 not applicable
（给理由）；提示词/模板是行为性的。
