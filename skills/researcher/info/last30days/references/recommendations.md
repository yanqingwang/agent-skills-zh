> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/recommendations.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 推荐

在排序与渲染之前，遇到推荐意图就阅读本文件。根文件的引用法则与输出法则优先于这里的展示示例。

### 当 QUERY_TYPE = RECOMMENDATIONS — 按信号加权挑选，而不是按提及次数

**RECOMMENDATIONS 查询的失败模式是“本该判断时却在数数”。** 提及次数只会奖励本来就热门的东西，而这很少等于真正值得推荐的。改按信号质量排序。

**信号权重（从高到低）：**
1. **从业者证言**（权重 5）- 第一人称“我在用 X，理由是……”，带具体理由、版本号或工作流细节
2. **专家转向 / 权威动作**（权重 4）- 领域内部人士公开改用、背书或做出选择（例如 Flask 作者从 Python 转向 Go）
3. **可度量的主张**（权重 4）- 具体数字、基准测试、生产环境采用证据（例如“延迟降低 43.7%”“LinkedIn 和 Uber 在生产环境运行它”）
4. **有理由的比较**（权重 3）- 并排分析，并明确点出取舍
5. **独立来源之间的一致模式**（权重 2）- 多个互不隶属的声音收敛到同一个选择
6. **描述性提及**（权重 1）- “X 是一个 Python 框架”— 只说明存在，不是推荐
7. **推广 / 训练营 / 课程标题**（权重 0）- “评论 CODE 领取我的课程”— 完全跳过，不计数

**排序前，先把“存在什么”与“推荐什么”分开：**
- EXISTS = 描述性提及、推广内容、训练数据惯性、训练营课程、“先学 X”一类不涉利害的帖子
- RECOMMENDED = 来自与结果有利害关系的声音的有理由选择（从业者、专家、案例研究、实际改用的人）
- 只有 RECOMMENDED 项驱动排序顶部。存在但未被推荐的项放在底部的“另外提到”里，并用一行说明它们为何只是提及而非首选。

**以 30 天 DELTA 开场，而不是以现状基线开场。** 有意思的变化是什么？谁在改用？反向信号是什么？一个毫无动静的现状领跑者是页脚条目，不是头条。“Python 有 15 次提及”不是 delta；“Flask 作者本月改用了 Go”才是。

**输出形态：**

```
🏆 Top recommendations (ranked by signal quality, not mention count):

**[Pick 1]** - [one-line why it is the top recommendation based on the strongest signal in the research]
- Evidence: [specific practitioner testimony, benchmark number, or expert pick - quote the actual signal]
- Best for: [specific use case]
- Voices: [real @handles, publications, or r/subreddits with stakes in the outcome]

**[Pick 2]** - [same shape]

**[Pick 3]** - [same shape]

Also mentioned (exists, not recommended): [comma-separated list with one-line note on WHY each is a mention rather than a pick - e.g., "Python (status-quo default across bootcamp content; @javitm: 'agents have a strong bias for Python despite it probably not being the best')"]
```

**要避免的反模式：**
- 因为某个选项出现得最频繁就让它领跑（“Python 有 15 次提及，所以它排第一”）。这是数数，不是判断。
- 把每次提及等同看待。Flask 作者改用 Go（专家转向，权重 4）的排位高于 10 条“先学 Python”的训练营标题（推广，权重 0）。那些训练营标题根本不该进入排序。
- 把“最适合什么？”压成一张总榜。RECOMMENDATIONS 查询通常会分成 2-4 个子问题（最适合生产规模、最适合让 Agent 可靠生成、最适合学习、最适合基准测试）。如果研究内容支持，就分开呈现。
- 忽略反向信号引用。如果语料里有这样一条引用：“@javitm: agents have a strong bias for Python despite it probably not being the best — they prioritize the strongest signal in training data over the right choice,”，那是在告诉你：对本话题而言，提及次数是一个有偏的度量。读它、呈现它，不要无视它。
- 输出前先压力测试你的首选。问自己：“研究真的能向持怀疑态度的专家证明这个主张吗？”如果不能，重新排序。

**RECOMMENDATIONS 的糟糕综合（在数数）：**
> "🏆 Most mentioned: Python (15 mentions), TypeScript (10x), Go (7x), Rust (5x)."

**RECOMMENDATIONS 的良好综合（在判断）：**
> "🏆 Top recommendations (ranked by signal quality, not mention count):
>
> **Go** - Flask creator Miguel Grinberg publicly switched this month for a specific technical reason
> - Evidence: @miguelgrinberg blog post "Why I am moving Python projects to Go for AI agents" — cites reliability and concurrency model; 1.2K upvotes on r/programming
> - Best for: production agent infrastructure
> - Voices: @miguelgrinberg, r/programming, r/golang
>
> **Rust** - Hardest numbers in the corpus
> - Evidence: production benchmark showing 43.7% latency reduction and 16x throughput growth in agent workloads; LangChain Rust port announcement
> - Best for: performance-critical agent runtimes
> - Voices: @langchainai, r/rust, Hacker News
>
> **TypeScript** - Strongest production-adoption signal
> - Evidence: LinkedIn, Uber, and Klarna running LangGraph.js in prod per LangChain blog
> - Best for: agents that integrate with existing web stacks
> - Voices: @hwchase17, @LangChainAI, r/LocalLLaMA
>
> Also mentioned (exists, not recommended): Python (status-quo default across training data and bootcamp content; @javitm: 'agents have a crazy strong bias for Python despite it probably not being the best — they prioritize the strongest signal in training data over the right choice'), Java/Kotlin (enterprise mentions only, no practitioner testimony in the 30-day window)."

注意良好版本的特点：
- 以变化开场（Flask 作者改用了），而不是以数量开场（Python 提及最多）
- 引用具体证据，能对怀疑者站得住
- 把 Python 的数量当作反向信号（@javitm 那条引用），而不是支持
- 把推广与描述性提及放进“另外提到”，并明确交代其性质


**渲染：** 使用上面的信号质量模板；提及次数不决定排序。

**RECOMMENDATIONS 的关键要求：**
- 每一项都必须有一行 "Voices:"，填入来自 X 帖子的真实 @handle（例如 @LONGLIVE47、@ByDobson）
- 包含 subreddit 名称（r/hiphopheads）与 web 来源（Complex、Variety）
- 从研究输出中解析 @handle，并纳入互动量最高的那几个
- 自然排版，宽终端适合表格，窄终端适合堆叠卡片
- **关键的空白规则：** 任何两个内容块之间绝不超过一个空行。对比表格应紧跟在前一段之后，中间恰好一个空行。不要在表格前垫 3-6 个空行。
