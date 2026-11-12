---
name: meeting-analyzer
description: "当用户分享会议转录文件（.vtt、.srt、.txt、Otter、Granola、Zoom）或询问自己在会议中给人的印象时使用。衡量发言占比、填充词与回避模式，并给出辅导建议。"
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`project-management/skills/meeting-analyzer/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 会议洞察分析器

> 最初由 [maximcoding](https://github.com/maximcoding) 贡献，后由 claude-skills 团队增强并整合。

将会议转录转化为关于沟通模式、领导行为与人际互动的具体、有证据支撑的反馈。

## 核心工作流

### 1. 摄取与盘点

扫描目标目录中的转录文件（`.txt`、`.md`、`.vtt`、`.srt`、`.docx`、`.json`）。

对每个文件：
- 从文件名或内容中提取会议日期（预期为 `YYYY-MM-DD` 前缀或内嵌时间戳）
- 识别说话人标签：查找诸如 `Speaker 1:`、`[John]:`、`John Smith  00:14:32`、VTT/SRT 字幕提示格式之类的模式
- 确认用户身份：若有歧义则询问，否则根据出现最频繁的说话人或文件名线索推断
- 记录：文件名、日期、时长（来自时间戳）、参与人数、字数

打印一份简明的清单表格，以便用户在进入繁重的分析之前确认范围。

### 2. 规范化转录

不同工具生成的格式差异极大。分析前先将所有内容规范化为统一的内部结构：


```
{ speaker: string, timestamp_sec: number | null, text: string }[]
```


各格式的处理方式：
- **VTT/SRT**：解析字幕提示时间戳与文本。说话人标签可能内嵌（`<v Speaker>`）或作为前缀。
- **纯文本**：逐行查找 `Name:` 或 `[Name]` 前缀。若不存在说话人标签，则提醒用户按说话人的分析会受到限制。
- **Markdown**：去除格式，然后按纯文本处理。
- **DOCX**：提取文本内容，然后按纯文本处理。
- **JSON**：预期为包含 `speaker`/`text` 字段的对象数组（常见的 Otter/Fireflies 导出格式）。

若缺少时间戳，则优雅降级：跳过依赖时间的指标（语速、停顿分析），但仍执行基于文本的分析。

### 3. 分析

运行下方所有适用的分析模块。每个模块相互独立，可跳过不适用的模块（例如没有说话人标签时跳过发言占比）。

---

#### 模块：发言动态

按说话人计算：
- **字数与百分比**：占会议总字数的比例
- **发言轮次**：每人发言的次数
- **平均轮次长度**：每次连续发言的字数
- **最长独白**：标记超过 60 秒或 200 字的发言
- **打断检测**：在前一位说话人最后一个时间戳的 2 秒内开始的发言，或在句子中途的中断

若存在多份转录，生成单次会议摘要与跨会议平均值。

需要提示的风险信号：
- 在一对多（1:many）会议中用户发言占比 > 60%（过于主导）
- 在用户主持的会议中其发言占比 < 15%（投入不足或过度授权）
- 某位参与者全程未发言（被忽略的声音）
- 打断比 > 2:1（用户打断他人的次数是被打断次数的两倍）

---

#### 模块：冲突与直率度

扫描用户的发言，查找对冲与回避标记：

**对冲语言**（逐例计分，按会议汇总）：
- 限定词："maybe"、"kind of"、"sort of"、"I guess"、"potentially"、"arguably"
- 征求许可："if that's okay"、"would it be alright if"、"I don't know if this is right but"
- 推诿回避："whatever you think"、"up to you"、"I'm flexible"
- 表达异议前的软化语："I don't want to push back but"、"this might be a dumb question"

**冲突回避模式**（需要更多上下文，附带置信度标记）：
- 紧张之后转移话题（说话人 A 提出问题 → 用户转向后勤事务）
- 同意却不承诺："yeah totally" 之后没有任何行动或跟进
- 把他人的担忧重新描述得比其表述更轻："it's probably not that big a deal"
- 在本应讨论绩效话题的 1:1s 中缺少反馈

对每个被标记的实例，提取：
- 完整引述（含上下文：前后各 2 个发言轮次）
- 严重度标签：`low`（单个对冲词）、`medium`（一次交流中的对冲模式）、`high`（明显回避了必要的对话）
- 改写建议：更直接的版本会是什么样子

---

#### 模块：填充词与语言习惯

统计以下用法的出现次数："um"、"uh"、"like"（非比较用法）、"you know"、"actually"、"basically"、"literally"、"right?"（附加问句）、"so yeah"、"I mean"

报告：
- 每场会议的总次数
- 每 100 words 的比率（用于在不同会议时长之间归一化）
- 按填充词类型细分
- 情境性激增：填充词是否在特定情境下增多？（例如回应资深利益相关者、给出负面反馈、被突然提问时）

只有当比率超过 ~3 per 100 words 时才将其标记为问题。低于该值属于正常言语。

---

#### 模块：提问质量与倾听

对用户的提问分类：
- **封闭式**（是/否）："Did you finish the report?"
- **引导式**（答案已内含）："Don't you think we should ship sooner?"
- **真正开放式**："What's blocking you on this?"
- **澄清式**（引用前一位说话人）："When you said X, did you mean Y?"
- **延展式**（拓展他人观点）："That's interesting — what if we also Z?"

良好倾听的指标：
- 澄清式与延展式提问（体现主动加工）
- 复述："So what I'm hearing is..."
- 引用会议早些时候某人提出的观点
- 邀请较安静的参与者发言

倾听不佳的指标：
- 提出一个已经被回答过的问题
- 未回应对方答复就重述自己的观点
- 用一个不相关的话题来回应提问

报告开放式/澄清式/延展式提问与封闭式/引导式提问的比率。

---

#### 模块：引导与决策

仅当用户是会议组织者或主持人时适用。

评估：
- **议程遵循度**：会议是否按结构进行，还是跑题？
- **时间管理**：每个议题实际耗时与预期的对比？
- **包容性**：主持人是否主动带动安静的参与者？
- **决策清晰度**：决策是否被明确表述？（"So we're going with option B — Sarah owns the follow-up by Friday."）
- **行动项**：是否指定了负责人和截止日期，还是含糊带过？
- **暂存区纪律**：离题事项是否被确认并延后处理，还是让会议跑偏？

---

#### 模块：情绪与能量

追踪用户语言在整场会议中的情绪走向：
- **正向标记**：热情赞同、鼓励、幽默、表扬
- **负向标记**：沮丧、轻慢、讽刺、简短生硬的回应
- **中性/平淡**：低能量回应、单字回答

标记能量下降：用户投入明显降低的时刻（发言变短、回应缺乏实质内容）。这些往往与不适、无聊或回避相关。

---

### 4. 输出报告

将最终输出组织为一份连贯的单一报告。采用以下框架，数据不足的章节可省略：


```markdown
# Meeting Insights Report

**Period**: [earliest date] – [latest date]
**Meetings analyzed**: [count]
**Total transcript words**: [count]
**Your speaking share (avg)**: [X%]

---

## Top 3 Findings

[Rank by impact. Each finding gets 2-3 sentences + one concrete example with a direct quote and timestamp.]

## Detailed Analysis

### Speaking Dynamics
[Stats table + narrative interpretation + flagged red flags]

### Directness & Conflict Patterns
[Flagged instances grouped by pattern type, with quotes and rewrites]

### Verbal Habits
[Filler word stats, contextual spikes, only if rate > 3/100 words]

### Listening & Questions
[Question type breakdown, listening indicators, specific examples]

### Facilitation
[Only if applicable — agenda, decisions, action items]

### Energy & Sentiment
[Arc summary, flagged drops]

## Strengths
[3 specific things the user does well, with evidence]

## Growth Opportunities
[3 ranked by impact, each with: what to change, why it matters, a concrete "try this next time" action]

## Comparison to Previous Period
[Only if prior analysis exists — delta on key metrics]
```


### 5. 后续选项

交付报告后，提供：
- 深入剖析某场具体会议或某个模式
- 一份 1-page 的 "communication cheat sheet"，列出用户最需要改变的 top 3 习惯
- 跟踪设置：将当前指标保存为基线，供日后对比
- 导出为 markdown 或结构化 JSON，用于绩效评估

---

## 边界情况

- **无说话人标签**：提前提醒用户。运行文本层面的分析（填充词、对整份转录的提问类型），但跳过按说话人的指标。建议重新导出并启用说话人分离。
- **极短会议**（< 5 minutes 或 < 500 words）：仍做分析，但需注明短会议得出的模式可能不具代表性。
- **非英语转录**：填充词与对冲词典以英语为中心。对于其他语言，说明该局限并聚焦结构性分析（发言占比、轮流发言、提问次数）。
- **单次会议 vs. 语料库**：若只有一份转录，跳过趋势/对比类表述。将结论集中于该次会议本身。
- **未识别用户**：若扫描后仍无法确定哪位说话人是用户，先询问再继续。不要猜测。

## 转录来源提示

仅当用户似乎不确定如何获取转录时，才在输出中包含本节：

- **Zoom**：Settings → Recording → 启用 "Audio transcript"。从云端录制下载 `.vtt`。
- **Google Meet**：自动转录会保存到日历事件 Drive 文件夹中的 Google Docs。
- **Granola**：导出为 markdown。消费级工具中说话人标签质量最好。
- **Otter.ai**：从网页控制台导出为 `.txt` 或 `.json`。
- **Fireflies.ai**：导出为 `.docx` 或 `.json`，两者均可。
- **Microsoft Teams**：转录出现在会议聊天中。下载为 `.vtt`。

推荐采用 `YYYY-MM-DD - Meeting Name.ext` 命名约定，便于按时间顺序分析。

---

## 反模式

| 反模式 | 为何失败 | 更好的做法 |
|---|---|---|
| 无说话人标签就分析 | 无法得出按人统计的指标，结果只是泛泛的词云 | 请用户重新导出并启用说话人识别 |
| 对 5 分钟的站会跑全部模块 | 小题大做：填充词与冲突分析需要 20+ min 的会议 | 自动检测会议时长并跳过无关模块 |
| 呈现原始指标而不给上下文 | "You said 'um' 47 times" 没有基准会让人沮丧 | 始终与常态对比，并展示随时间的变化轨迹 |
| 孤立地分析单次会议 | 一次会议只是快照，不是模式，结论不可靠 | 基于趋势的辅导至少要求 3+ meetings |
| 把发言时长均等当作目标 | 主持人本应少说；演示者本应多说 | 按会议类型与角色为发言占比加权 |
| 把每个对冲词都标为负面 | "I think" 与 "maybe" 在头脑风暴中是恰当的 | 区分决策会议（对冲不利）与构思会议（对冲无妨） |

---

## 相关 Skill

| Skill | 关系 |
|-------|-------------|
| `project-management/senior-pm` | 更宽泛的 PM 范畴，用于项目规划、风险、利益相关者 |
| `project-management/scrum-master` | 敏捷仪式：与 meeting-analyzer 搭配用于回顾质量 |
| `project-management/confluence-expert` | 将会议分析输出存储为 Confluence 页面 |
| `c-level-advisor/executive-mentor` | 高管沟通辅导：互补视角 |
