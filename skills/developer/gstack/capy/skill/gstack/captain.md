> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/capy/skill/gstack/captain.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 在 Captain 手下工作：审批、计划请求与合并请求

本文件属于 gstack 的 Capy skill（所有者复制进自己 Drive 的那个文件夹）。它描述运行 gstack 的
Capy 线程如何请求决定、记录答复和请求合并。无论线程向 Captain（crew 线程）汇报还是直接向某人汇报，规则都适用。
`gstack-skill-start` 在 `GSTACK_CAPY=1`（Capy 启动行会设置它）时打印简短版作为 `capy-asks` 块。
`GSTACK_CAPY_ASKS=0` 让该块在一个会话内消失。这是 lane 这一侧的文件。控制者那一侧（READY 契约、合并列车、
digest、每日 flaky 检查，以及 crew 规则文件与 Captain drive 的模板）是 `/captain` skill 与 gstack checkout 里的
`crew/docs/captain.md`。

## 1. 审批如何按线程运作

- **一条路径。** crew 线程向它的 Captain 提出：经 Capy 的 agent 通道发"需要你"报告，绝不直接把问题抛给人。Captain
  用平实的语言转达，并把人的原话带回。没有 Captain 的线程用 Capy 提问直接问人。无论哪种，都绝不使用光秃秃的问题、
  门代码或槽位号。
- **范围。** 一条答复覆盖它被请求的线程与范围。它不是对后续工作的空白授权。
- **常设审批**是 Captain 列在自己规则里的那些，例如"绿了就合并，走合并列车"、"付费 eval 闸门预已批准"或
  "单用例 flaky 重跑一次"。引用该规则（带日期与原文）而不是再次询问。gstack 自己不内置任何常设审批。
- **永远重新请求：**
  - 产品或行为决定；
  - 超过既定上限的花费；
  - 仓库之外的任何发布（advisory、release、帖子）；
  - 对阈值、预算、试验次数或测试 kind 的任何变更；
  - 不落地就关闭别人的贡献；
  - 任何破坏性或不可逆的事。
- **可观察的问题不由人来回答。** 一条命令、一次渲染或一次测量能在本地、只读且免费解决的问题
  （"新路径是不是更快"、"测试端点接不接受这个载荷"、"测试是不是仍然失败"）由线程自己解决：它运行那个东西并报告结果。
  会改变状态、触达活系统或花钱的调用仍然是请求。只有产品或偏好判断才向上提，且带着已经做好的观察。收到可观察问题的
  Captain 会带着能回答它的检查把问题退回，而不是转达。
- **gstack 工作流在 Capy 里做什么。** 以 `GSTACK_SESSION_KIND=unattended` 启动的工作流会采纳每一条建议选项，
  把其余内容写成待处理闸门条目，然后停下。你的职责是把那些待处理条目以下面的格式带给 Captain 或人，再把答复带回来。

## 2. 审批记录

每条答复一行：日期、问了什么、人的原话、谁说的（以及谁转达）、答复覆盖什么、还有什么待处理，以及结果
（approved、rejected、pending，或引用的常设审批）。

```bash
gstack-approvals add --ask "Spend up to \$40 on a paid eval rerun for the ship cases" \
  --words "yes go" --by "Garry (via GStack Minder)" --scope "one rerun of the 6 ship cases, cap \$40"
gstack-approvals add --outcome standing --ask "Merge #3330 when green" \
  --words "yes merge when green" --by "Garry, 2026-10-16 (Captain rule)" --scope "every crew PR, through a train"
gstack-approvals import --autoplan <run dir> --by Garry   # after gstack-autoplan answer; idempotent
gstack-approvals import --autoplan <run dir> --by Garry --stack b1,b2   # a stacked PR set: every branch, or none
gstack-approvals render                                    # the ## Approvals section
```

- **存在哪里。** `<state root>/projects/<slug>/approvals/<branch key>.jsonl`，每分支一个文件，
  因为一个线程只发一个分支。`<slug>` 是仓库自己的 slug（`gstack-slug --get
  REPO_SLUG`）；`.gstack-project` 标记不改动它。Capy 上状态根随机器一起丢弃，所以每次写入同时镜像到 `GSTACK_APPROVALS_DIR`，否则镜像到挂载的 Captain
  drive 里的 `approvals/` 目录（`<captain drive>/approvals/<slug>/`，全 crew 可读），否则镜像到私有的项目用户
  Drive 文件夹。`gstack-approvals path` 打印所选镜像与 `READ_ALSO:` 根，读取会合并这些根。
  `GSTACK_APPROVALS_MIRROR=0` 关闭镜像，`gstack-approvals sync` 恢复本地副本。
- **耐久副本**是线程报告与 PR 正文里的 `## Approvals` 小节。把 `render` 输出粘贴进去；绝不手打行。在公开仓库
  （或可见性未知）上 `render` 只打印 `Approved: yes|no (record <id>)`；`gstack-approvals list` 显示完整记录。
- **无秘密。** 每个字段写入之前都过 gstack 的秘密扫描器。命中会拒绝该行
  （`APPROVAL_RECORD_SECRET`，它指名字段与规则，绝不指名文本）。在秘密的位置写 `[redacted]`，或请对方换一种说法。
- **仅展示。** 渲染出的表会转义 mention、链接、图片、HTML 以及任何形如
  `Approved by … via …` 的引用。gstack 强制的审批类别仍需要自己的引用行
  (docs/ship-policy.md#approval-classes)。
- 空表意味着"No approvals recorded"。在既无记录也无镜像的全新 Capy 机器上，它显示
  "Record unavailable"（`APPROVAL_RECORD_UNAVAILABLE`），因为丢失的记录不是空的记录。

## 3. 计划审批：格式

在 Captain 手下，构建东西的线程在任何产品代码之前先做计划。对它的 brief 跑一次大小与工作相称的
`/autoplan` 是它的第一个动作，闸门以下面的格式向上提，只有答复进入 run 且它报告 `APPROVED` 之后才开工。每个 Capy
线程都遵循的简短版（含豁免工作：只读线程、flaky 修复、槽位戳、CHANGELOG 解析、授权内的上限重设）是本文件夹
SKILL.md 的"Plan, approve, ship"小节；完整规则是 `crew/docs/captain.md` 的 Plan before build。

你带来审批的每个计划或闸门都有这些部分，按此顺序，写法要让项目外人能看懂：

1. **Before → after。** 用户或维护者今天看到的与之后看到的，配具体示例：一条命令及其输出、一个界面、
   一个成本或时间数字。
2. **为什么重要。** 今天谁受伤害、伤害多大，尽量带数字。
3. **什么触发了这项工作。** 触发器：issue 或 PR 链接、一次失败的运行、一份用户报告，或此人的请求（引用原话）。
4. **重大决定。** 每一项：考虑过的选项、选了哪个及为什么、什么会推翻它。
5. **需要你做什么。** 请求格式（`crew/docs/captain.md` 的 The ask format）：Captain 的名字，然后每个决定
   一行带字母，字母在全列表唯一："A: <code> hit problem p, which happens when h.
   We could fix it in these ways: 1) x; 2) y; 3) z. Recommendation: x because why. A1 to take recommendation."
   建议项是选项 1。绝不把"按最初写的计划"当默认选项。
6. **"do it"。** 每个请求都以"do it"收尾：全范围采纳列表里的每条建议，包括计划点名的后续项
   （docs、列车、清理），一路带到完成，不再追问。点名某选项（"A2"）则改取该选项。对 autoplan 闸门，"do it"
   按 `rec` 应答；记录原话。

对 autoplan run，用 `## ELI5`（5-10 句大白话）开计划，然后把第 1 到 4 部分写成
`## Before → after`、`## Why it matters`、`## What caused this work` 与 `## Big decisions` 小节。然后，在闸门处：

```bash
gstack-owner-brief render --captain --out <run dir> --captain-name "<Captain name>"
```

它打印一行头（"Decision needed … Reply **do it** …"）、`### ELI5` 小结（闸门带 `eli5` 的 run 上）、四个计划小节
（每节有上限，并指向计划看其余内容），以及"What we need from you"，按请求格式每个选项一行带字母，以"do it"收尾，
然后是 `### Cost` 小节（已花费、最坏情况，以及 `rec` 可重开阶段的估算）。最后一行"For the relaying agent"携带
run、`gate_rev`、`rec_hash` 与确切的
`gstack-autoplan answer` 命令。把该行之上的所有内容转达。答复回来时：

```bash
gstack-autoplan answer --out <run dir> --gate-rev <n> --reply rec --rec-hash <h> \
  --by agent:<your thread> --owner-reply "<their exact words>"
gstack-approvals import --autoplan <run dir> --by <name>
```

不再问新东西的后续闸门会用你记录的原话替你自动应答（`CARRIED:`，然后 `APPROVED:`）；
brief 会说"Nothing pending. Carried forward"，直接 import 并开工，无需第二次请求。`CARRY_CHECK:` 表示
先由另一个模型族的一位评审者阅读未评审的增量（`gstack-autoplan check`）。其他任何情况打印
`CARRY: no (<why>)` 并像今天一样交给人（docs/unattended.md#carry-forward）。

如果此人用文字答复（"split it into two PRs"），把文字映射为 token，应答，并用一行确认你记录的内容
（"Recorded: 拆成两个 PR；其余按建议执行"）。点名某选项（"B2"）按 `--reply "rec except <token>"` 应答，
token 来自最后一行的字母映射。缺小节的计划渲染"Not ready for approval"且不带回复邀请，并以 exit 1 退出
（`CAPTAIN_BRIEF_INCOMPLETE`）：补齐小节，运行 `gstack-autoplan revise --plan <file>`，再渲染一次。对不属于
autoplan 闸门的决定，手写同样的五个部分。

## 4. 合并请求：格式

你发送 READY 的每个 PR，以及 READY 报告本身，都包含：

1. **改了什么。** 一到三张前后对比图，信号最强的在前，每张配一行说明（改了什么、为什么），下面附折叠的文字版。
   - UI：base 与分支上的截图，同尺寸。
   - Skill 或提示词：`gstack-pr-shots --path <file> --heading "<section>" --caption "<…>"`。
   - CLI：`gstack-pr-shots --before <capture> --after <capture> --kind terminal --caption "<…>"`，其中
     capture 是仓库内的文件。
   - 内部：最能展示该变更的源码小节或测试输出。
   `gstack-pr-shots` 只读文本、不运行任何东西、拒绝匹配到秘密的输入，并打印 `SHOT_PNG:`。
   没有浏览器时该行显示 `unavailable`：用你自己的浏览器截取打印出的 `shot.html`。
   仅对公开仓库，用 Capy 的 PR 资产工具（`tools.pr.uploadAsset`）上传每张 PNG，并以其返回的 URL 配说明文字嵌入。
2. **为什么。** 先用此人的话陈述问题，再用两三句话说明原因与用户将看到的效果。
3. **影响半径。** 该变更还触碰什么，以及让这件事安全的那一个事实，连同该事实到达的 evidence-ladder 层级。
4. **审批。** `gstack-approvals render`。
5. **证据。** head 上为绿的检查、闸门或列车结果、flaky 用例，以及一行 `Unverified:`：
   你没有亲自检查的每个主张及其原因，或 `none`。这一项由你写，/ship 不代写。

READY 报告附上关键图片（Capy 消息附件），Captain 可以内联展示它。
当 `GSTACK_CAPY=1` 时 /ship 会做第 1-4 项（其 `capy-pr` 小节）。Capy 之外，PR 正文保持不变。

**谁盯 CI。** 直到 READY 为止，你拥有自己 PR 的检查与审查：自己盯住它并修好变红的东西（flake 重跑一次），
让检查永远不要吵醒你的 Captain。其 PR 带来大量检查、审查与合并唤醒的 Captain，会把 PR 与 CI 盯守交给一个
合并 lane 线程而不是自己订阅，因为每次在上次唤醒约五分钟之后的唤醒，都会以数倍于热价格的成本重写它的整个上下文缓存。
合并 lane 只向 Captain 报告落地、决定或阻塞
（gstack checkout 里的 `crew/docs/captain.md`，Roles）。

brief 里的 token 上限以 `--token-cap <n>` 传给 /ship。每次 /ship 都在全新的子代理中运行，标题为
`ship #<n> at <head7> <4-char nonce>`（唯一），brief 里带 `GSTACK_SHIP_TASK_TITLE=<that title>` 与指令：
从根线程 `tasks` 的自己那一行读取每次读数（start、notes、close），并以
`--reading-from task` 起算预算，使其默认封顶 100M；绝不给已完成的 /ship 子代理发消息让它再跑一个。当 /ship 因此停下时
（`STOP:
reason=budget_exhausted`、`status=incomplete`），lane 报告 BUDGET 与 RECOVER 行并询问所有者；它绝不自行提高上限。
所有者的答复以 `--approved-by <who> --words "<their words>"` 运行 RECOVER 行，`gstack-approvals add` 记录同样的原话。
