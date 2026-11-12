---
name: learn-taste
description: 把用户在一次会话中做出的设计纠正，变成下一个 Agent 会遵守的规则。收集每一条纠正（明确说出的、用户对你写的文件所做的修改、反复的提醒、回退），把每条泛化到合适的层级，确认原因，然后把规则连同原因写进项目的 DESIGN.md、某个项目 Skill 或一条 lint 检查。仅在显式调用时运行（Only runs when explicitly invoked）。
disable-model-invocation: true
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/learn-taste/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 学习品味

用户做出的每一次纠正，都是 Agent 本没有的品味。不写下来，下一次会话就会重犯同样的错误，用户又得纠正一遍。本 Skill 找出这些纠正，把每条变成带原因的规则，写到下一个 Agent 会读到的地方。

它只做一件事：写规则。它从不改组件代码，也从不添加用户没有表达过的规则。

## 硬性规则

1. **只写用户的品味。** 每条规则都要能追溯到用户说过、改过或确认过的东西。绝不要因为某条像最佳实践就加进去。那是你的品味，而你的品味正是用户在纠正的东西。
2. **绝不编造原因。** 如果用户没给理由，就提出一个并标注*推断*，写入之前先拿到确认。错误的原因比没有更糟：下一个 Agent 会把这套推理扩展到不适用的场景。
3. **先提议，然后停下。** 展示所有候选，只写用户批准的。一条错误的规则会在未来每次会话里重复出现，和那个错误本身一模一样。
4. **一个检查胜过一句话。** 如果违规可以通过匹配代码发现（被禁用的值、没用 token 的原始 hex、被禁止的属性），就提出 lint 规则、token 限制或测试。检查每次都会运行；长文件里的一句话，在 Agent 上下文满了之后会被跳过。
5. **为不在场的 Agent 写。** 不要写"像我们讨论过的"或"前面那张卡片"。写清组件的类别、值、token、文件。

## 工作流

### 第 1 阶段：收集纠正

从第一轮开始通读当前对话。如果用户点名了更早的会话、而你又能读到那些记录（Claude Code 把它们以 JSONL 形式存在 `~/.claude/projects/<project>/` 下），也一并读。

明确说出口的纠正是少数。把五种信号都找齐：

| 信号 | 例子 | 它告诉你什么 |
| --- | --- | --- |
| 明确纠正 | "不对，要半透明阴影，不是边框" | 规则本身，通常连原因一起给出 |
| 静默修改 | 用户把你在文件里写的 `duration: 400` 改成了 `200` | 你的默认值错了，他们改后的值就是规则。通过"文件在你的编辑之外被改动"的通知发现，或把文件和你最后写的版本做 diff |
| 反复提醒 | "小一点。" → "还是太大。" → "可以了" | 你的默认值偏差是两点的总距离。记录他们最终落在哪里，而不是中间步骤 |
| 回退或否决 | "撤销这个"、在变体里选 B 不选 A、删掉你加的东西 | 什么不该做。原因通常缺失，所以交给第 3 阶段的提问 |
| 确认过的非显然选择 | "对，图标就放在按钮外面" | 一个新起的 Agent 可能不会照做的选择。只有当新 Agent 确实可能做出不同选择时才记录 |

对每一条，记下用户的原话（或 diff）、你原本做了什么、他们想要的是什么，以及他们给出的任何理由。

跳过不属于品味的东西：功能性 bug、只针对某个屏幕的内容（"大标题应该写 Pricing"），以及对你理解任务的纠正。

**完成标准：**每一轮都被读过，每条纠正都列出了来源原话或 diff。

### 第 2 阶段：过滤

把每条纠正放进这棵树：

```
Would a fresh agent building a DIFFERENT component in this repo make the same mistake?
├── No (a one-off: this campaign's color, this page's layout) → Skipped
└── Yes
    ├── Does an existing rule cover it? Check DESIGN.md, CLAUDE.md / AGENTS.md, project skills.
    │   ├── Yes, and it says the same thing → The rule failed. Rewrite it stricter
    │   │   (a number, a token, "never") instead of adding a duplicate.
    │   ├── Yes, and it contradicts → Conflict. Show both; the user picks.
    │   └── No → continue
    ├── Can a violation be found by matching code? → Check candidate.
    │   Keep a one-line rule too, so the why is recorded somewhere.
    └── Did the user say it applies everywhere, not just here? → Ask where their global rules live.
        Otherwise it's a project rule.
```

### 第 3 阶段：泛化并找到原因

选出最窄的、却能在下一个不同组件上避免该错误的层级：

| 层级 | 例子 | 判定 |
| --- | --- | --- |
| 实例 | "定价卡片用阴影，不用边框" | 太窄：只保护这一张卡片 |
| 类别 | "凸起表面（卡片、popover、菜单）用 `shadow-raised` 与背景区分，绝不用实色边框" | 写这一条 |
| 普适 | "绝不用边框" | 太宽：会破坏输入框、分隔线、表格 |

同一条纠正出现在两个或更多不同组件上，就是类别层级的证据。如果两个层级看起来都对，就问用户。

规则要写得严格：用这个代码库里的值和 token 名，用"总是"或"绝不"，不要"尽量"或"试着"。只有当用户把它说成偏好时，才用更软的措辞。

然后是原因。用户给了理由，就用他们的原话。否则写出你的最佳候选，标注*推断*，放进给用户的问题里。

**提议前自测：**只读规则和它的原因，然后在脑中重现原始任务。一个不掌握其他任何信息的 Agent，能产出用户想要的东西吗？如果仍可能产出错误版本，说明规则太模糊。补上值、token 或例外。

### 第 4 阶段：决定写到哪里

```
Check candidate?
├── Yes → lint rule, token restriction, or test, plus a one-line rule in DESIGN.md
└── No
    ├── Is DESIGN.md's section for this aspect over ~40 lines, AND relevant to only some tasks
    │   (motion rules don't matter when building a settings form)?
    │   └── Yes → move the whole section into a project skill and leave a one-line pointer in DESIGN.md
    └── Default → DESIGN.md at the repo root, under the matching section:
        Surfaces · Color · Typography · Spacing & layout · Motion · Interaction · Copy
```

DESIGN.md 或对应章节不存在就创建。

**确保它会被读到。** 没有任何 Agent 加载的 DESIGN.md 改变不了任何事。如果 CLAUDE.md 和 AGENTS.md 都没有指向它，提议在项目实际用的那一个里加这一行：`Before building or changing UI, read DESIGN.md.`

条目格式：

```md
## Surfaces

- **Raised surfaces (cards, popovers, menus) use `shadow-raised`, never a solid border.**
  Why: a solid border makes a raised surface look flat and heavy; a semi-transparent shadow separates it from the background and adapts to both themes.
  <!-- 2026-11-12: "no, semi-transparent shadow, not a border" -->
```

注释里放日期和用户原话。以后某条纠正与之冲突时，它能说明哪条规则更新、用户当时到底说了什么。

### 第 5 阶段：报告并停止

展示下面的报告，然后停止。

### 第 6 阶段：批准后写入

只写批准的条目。展示 DESIGN.md（以及任何 Skill 或配置文件）写入后的 diff。对于检查，实现它并在整个代码库上跑一遍。如果它标记了现有代码，报告数量，并问用户是降级为警告还是修复这些违规。绝不不经询问就修复，因为那会改动组件代码。

## 必需的输出格式

### 待添加的规则

| # | 你说过 | 规则 | 原因 | 位置 |
| --- | --- | --- | --- | --- |
| 1 | "不对，要半透明阴影，不是边框" | 凸起表面用 `shadow-raised`，绝不用实色边框 | 实色边框显得又平又重；阴影能同时适应两套主题 | DESIGN.md › Surfaces |
| 2 | 在 `Dropdown.tsx` 里把 `duration: 400` 改成了 `200` | 下拉和 popover 在 150–200ms 内打开 | *推断：*对一个一天要打开很多次的表面，400ms 感觉迟滞 | DESIGN.md › Motion |

### 需要你回答

每一条*推断*的原因、每一个拿不准的泛化层级、每一个全局还是项目的归属问题。每条一行，附上你的建议。

### 冲突

现有规则、新纠正，以及你会保留哪一个。

### 做成检查

每个检查候选及其确切实现（规则配置或测试），以及它在当前代码库里会标记出什么。

### 跳过

每条被跳过的纠正一行，写明原因，供用户推翻。

收尾说："输入 `write all` 或 `write 1, 3`，并回答上面的问题。"

如果本次会话没有任何品味纠正，用一行说明。这是好结果，不是失败。

## 调用变体

| 调用方式 | 行为 |
| --- | --- |
| `/learn-taste` | 当前会话，完整工作流，停在报告 |
| `/learn-taste <sessions>` | 同时读取点名或最近 N 个会话的记录 |
| `write all` / `write 1, 3` | 写入上一次报告中已批准的条目 |
| `/learn-taste prune` | 读取 DESIGN.md，对重复项提议合并、对矛盾提议修复、对模糊规则提议更严格的措辞。同样遵守先提议后停止 |
