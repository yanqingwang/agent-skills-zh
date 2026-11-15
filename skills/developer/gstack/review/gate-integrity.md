> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/gate-integrity.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 闸门完整性（Gate Integrity）目录

改编自 just-say-no-to-process-porn-and-ceremony skill 的
REWARD-HACKING-CATALOG；模式名称原样保留，因为名称本身就是威慑。
每个条目指名其病理、gstack 的对策及其所在位置。这些 id 是 `/review` 与 `/ship`
在一条发现上记录的 `gate` 值；`gstack-gate-diff` 在其读取级清单中输出带标签的那些。
设计与理由：`docs/designs/HONEST_WORK_GATE_INTEGRITY.md`。

三个层级，处处分开：**listed**（登记：测试、CI、
runner/lint 配置、快照或 golden 路径中的每个 hunk；是清单，不是发现）、
**read**（带标签或删除行的已登记 hunk；Agent 对每个 hunk 只问一个问题：
*这次放宽是否让它当初要抓住的失败闭嘴，还是 diff 中可见的某次度量或某个决定证明了它的正当性？*）、
**finding**（没能通过那个问题的已读 hunk；每条发现或连贯的组对应一个人类决定）。
控制点是人类的处置，不是检测器：工具做登记和打标，它永不判断、永不抑制。

## 打标模式（由 `gstack-gate-diff` 输出）

### RH-1：测试被删除或禁用

Agent 删除、跳过或聚焦一个测试，而不是修复它所守护的代码：删除了
`test(`/`it(`/`def test_`/`func Test`/`@Test`，新增了
`.skip`、`.only`、`xit`、`xdescribe`、`@pytest.mark.skip`、`#[ignore]`、
`t.Skip(`、`@Disabled`、`@Ignore`、`XCTSkip` 或 `@tag :skip`。测试编码的那个失败从此不可见，
套件看起来是绿的。对策：
`gstack-gate-diff` 给 hunk 打标（打标是事实性的：与被删源码一起删除的测试也会被打标，
把它定为非发现的是 Agent 的判断，不是工具）；`/review` 的闸门完整性读取它，
并把发现路由到四选项 ASK（`review-gate-disposition`）；`/ship` 核心清单条目 2.5
运行同样的扫描，PR 正文的 `Gate edits:` 行承载保留的理由。测试专员的
"绝不接受被丢弃的有效红色测试"规则保留为大型 diff 的阅读。

### RH-2：证明类型注水

把 mock、fixture、回放或静态读取当作主张所需的证明："verified against production"（对照生产已验证），而实际应答的是 stub；
"路由可达"来自一次 grep。没有标签能看见它；这是文字检查。对策：
开篇的 Claims Need Evidence 内核（说出你手头证据的种类，
绝不用一种替代问题要求的另一种）、`/review` 的主张验证（Verification of claims），
以及闸门完整性类别中"不带标签直接从 diff 阅读 RH-2"的指令。`/ship` Step 16 的
"没有新鲜验证证据不做完成声明"是发布闸门。

### RH-3：快照或 golden 未连同其归属测试再生成

快照（`__snapshots__/<name>.snap`、`*.snap`）变了，而其
惯例归属（`<name>` 测试文件）在候选 diff 中没有 hunk，
说明新输出是被接受而不是被测试。`*.golden`、`testdata/` 与
项目的 `Snapshot paths:` 被打 `RH-3?`（归属未决）：登记并阅读，绝不推断。对策：标签加闸门完整性阅读；随其源码
一起更新的快照是清单，不是发现。gstack 自己的
SKILL.md golden 按设计在每次模板编辑时再生成，所以 RH-3 永不自动阻断；PR 正文的那一行
让产品快照的再生成对人类可见。

### RH-4：提交占位符

`todo!()`、`unimplemented!()`、`raise NotImplementedError`、`throw new
Error("not implemented")` 或 `pass  # TODO` 落进非测试代码，而工作被报告为完成。对策：标签让 hunk 经由内容兜底进入，
即使在产品代码里；计划完成审计的
`done/changed/partial` 分类与 `Linked to #N` 绝不自动关闭的规则
让义务保持开放。

### RH-5：同义反复测试

不可能失败的测试：断言自己的 setup、逐行镜像实现，或没有否定（不拒绝任何东西）。不是标签；从 diff 阅读。
对策：测试价值卡的 `protects=` / `fails_when=` 字段与 `no_claim=` 句（绿灯不能证明什么）、
拒绝缺卡测试的 `/ship` Step 7 编写闸门，以及闸门完整性中"在带标签 hunk 旁阅读 RH-5"的指令。

### RH-10：改规格冒充进度

计划或规格中的验收文字被改写，使已交付的工作与之一致，然后该条目按新文字报告完成。对策：
`/ship` 的计划完成审计把计划的验收小节与其基分支或首次 commit 基线做 diff，把被编辑的条目报告为
`ACCEPTANCE_EDITED`，绝不并入 `CHANGED`；原始义务仍被审计，PR 正文写明范围变更。已声明限制：在与计划引入
同一个 commit 里被改写的条目不可见。

### RH-12：产品代码中的环境嗅探

产品代码按 `process.env.CI`、`NODE_ENV === 'test'`、
`RAILS_ENV == 'test'`、`PYTEST_CURRENT_TEST` 或 `GITHUB_ACTIONS` 分支，
使被测代码与生产行为不同。对策：
测试路径之外的打标；闸门完整性阅读会问这个分支是为了通过检查，还是为了服务用户。

### RH-13：添加抑制注记

`eslint-disable`、`@ts-ignore`、`@ts-expect-error`、`# type: ignore`、
`# noqa`、`#[allow(`、`// nolint`、`rubocop:disable` 或 `@SuppressWarnings`
让检查器闭嘴而不是满足它。对策：任何路径都打标；阅读会问被抑制的诊断
是否就是这个改动本该修复的失败。

### RH-14：绕过闸门

范围内的某个 commit 带 `[skip ci]`/`[ci skip]`，某个 workflow 获得
`continue-on-error: true` 或 `allow_failure: true`，或某个脚本或 hook 添加
`--no-verify`。对策：打标；被移除的 workflow 任务由路径底线列出并阅读
（任务移除检测不在 v1 内）。`/ship` 绝不带 `--no-verify` 推送，也绝不强推。

### RH-15：闸门阈值放宽

在测试、eval、CI 或配置文件里，一个数值闸门在单个 hunk 内向放宽方向移动：timeout、retry、retries、
tolerance、epsilon、delta、maxDiff 或 jitter 调**高**；threshold、min_score、minimum、coverage 或 required
调**低**；或把精确计数断言放宽为界限（`toBe(3)` →
`toBeGreaterThan(0)`）。未配对的值打 `RH-15?` 并阅读。工具把它找到的任何引用打印在 hunk 旁边（指名
`ship-measure` 报告的 commit 文本、`gstack-shortcut(dec-*)` 标记），且绝不在其上抑制，因为
`ship-measure` 报告被 gitignore 而 commit 文本可伪造。对策：
`/review` 从前笼统的"eval 阈值变更"抑制收窄为仅限代码质量意见；Agent 只读解析引用并把
"Keep — justified"选项标注 verified 或 unverified 后预填；`ship/sections/measure.md` 的先度量后修复循环
（"绝不为了拿到通过而提高预算、降低阈值、加重试或跳过用例"）是原生的修复路径。

### RH-16：异常被吞掉

在非测试代码中新增 `catch {}`、`catch (e) {}`、`except: pass`、`rescue nil` 或 `_ = err`
把失败变成沉默。对策：标签把它列在 RH id 之下；slop-scan 的空 catch 规则保留修复建议。
开篇的 stderr 规则（绝不引用 stderr 被静音的命令）覆盖证据命令的形式。

## 正向可观察项（零运行绿灯）

### PL-1：退出码不是证据

命令的 exit 0 被报告为成功，而没有任何工作确实发生的可观察项：什么都没选中的套件、
编译了零个文件的构建。对策：开篇的 Claims Need Evidence 内核（声称执行过就要指名命令
与其观察到的结果；查得的 null 结果按 null 报告，不是 pass）与 `/ship` Step 16 的回执检查。

### PL-2：零运行绿灯

一条测试通道 exit 0 但运行了零个测试：bun 的 `0 pass 0 fail`、jest 的 "No tests
found"、pytest 的 "no tests ran"、rspec 的 "0 examples"、只输出 `[no
test files]` 的 `go test`，或过滤后的空选择。对策：`/ship` Step 5 按 runner 的汇总行判定通道通过，
不单看 exit 0，配三个绝不合并的计数状态（`tests_ran: N` 通过；`tests_ran: 0` 记 ZERO-RUN，
按失败通道分诊；`tests_ran: unknown` 保留 exit-0 通过并在 PR 正文打印
`count unavailable`）；`gstack-evidence check` 把 ZERO-RUN 报告为 STALE 等价；PR 正文的
`## Test Coverage` 小节打印每条通道的 `tests ran` 计数。

## 控制点分布

| 位置 | 控制 |
|---|---|
| preamble | Claims Need Evidence 内核：执行、证据种类、失败披露、null 结果、stderr 规则 |
| `/review` Step 3.5 Diff scans | `GATE_SCAN_BLOCK` 运行 `gstack-gate-diff <base>`；UNAVAILABLE 与 partial 是缺失覆盖，绝不是 `none detected` |
| `/review` 清单 Pass 1 | 闸门完整性类别：三个层级、那个问题、ASK 绝不 AUTO-FIX、组是同一个决定、引用绝不移除发现 |
| `/review` Step 5c | `review-gate-disposition`（单向）：A) 恢复闸门，B) Keep — justified，C) Keep — other reason，D) Leave open for a later human；D 推荐给派生/无头会话 |
| `/review` Step 5.8 | 发现带 `gate`、`gate_id`、`reason`、logger 盖章的 `actor`；动作 `kept`/`restored`/`open`；`open` 计入 `issues_found`；不存储 hunk 文本 |
| `gstack-review-log` | 从 `gstack-session-kind` 盖章 `actor`，并对非交互 kind 强制 `action: "open"` |
| `/ship` 核心清单 2.5、Step 7 与 9.4 | 清单读取之前同一个块，测试生成子代理返回之后再读一次，父级修复之后再读一次 |
| `/ship` Step 5 与 Step 16 | runner 汇总通过、三个 `tests_ran` 状态、ZERO-RUN 按失败通道 |
| `/ship` Step 16 stage 5 | 每条闸门发现的处置、理由与 actor，或覆盖行；审计员的姿态 |
| `/ship` Step 19 | Pre-Landing Review 之下的 `Gate edits:` 行，Test Coverage 之下每条通道的 `tests ran`；任一发现为 `open` 时不起草 |
