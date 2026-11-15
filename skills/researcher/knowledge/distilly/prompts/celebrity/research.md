> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/research.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人研究提示词

## 任务

在蒸馏之前，对目标公众人物执行一轮结构化、多维度的研究。一份提示词同时服务两种研究档位：“输出契约”之前的全部内容对两者通用，之后按所选的 `research_profile` 走对应章节。

- **budget-friendly**（默认）：轻量一轮，六个维度覆盖在三份笔记文件里。
- **budget-unfriendly**：深度一轮，每个维度一个文件，之后还必须经受研究审计、综合阶段与验证阶段的检验。仅当用户想要更高置信度的 Skill、且能接受更慢更贵的工作流时使用。

目标不是收集趣闻或编写传记。目标是提取足够的有据证据，用来重建：

- 心智模型（他们怎么思考）
- 决策启发法（他们怎么选择）
- 表达 DNA（他们怎么说话）
- 反模式（他们拒绝什么）
- 诚实边界（证据在哪里耗尽）

并把其真实的思维模式与泛泛的智慧区分开。

---

## 品味原则

这些原则决定收集什么、跳过什么，适用于每个阶段。

1. **长文 > 碎片**：一篇 3000 字的长文比 50 条推文更能暴露思考结构
2. **争议 > 共识**：有争议的立场比人人称赞的立场更能暴露独特思维
3. **变化 > 固守**：一个人在哪里改变了想法，比在哪里保持一致更有信息量
4. **一手 > 二手**：本人的原话永远高于他人的转述
5. **谈手艺 > 谈生平**：他们如何谈论自己的过程，比生平故事更重要
6. **重复模式 > 一次性金句**：跨语境出现 5 次的模式胜过一句爆款名言
7. **谈失败 > 谈成功**：他们如何谈论搞砸的事，比庆功叙事暴露得更多

---

## 来源质量层级

按此顺序排列来源优先级。这个数字就是每条笔记都要记录的来源权重。

1. **用户提供的本地材料**（转写稿、PDF、截图，属 ground truth，权重最高）
2. **第一人称署名作品**（书籍、文章、newsletter、博客）
3. **长篇访谈与对话**（30 分钟以上的播客、视频访谈、炉边谈话）
4. **有记录的决策与转折点**（案例研究、公开记录、有署名的行动报道）
5. **短篇第一人称内容**（社交媒体帖子、短问答、推文串）
6. **外部分析与批评**（他人撰写的人物特稿、评论、传记）
7. **二手摘要**（只用于定位一手来源，绝不能单独作为证据）

### 来源黑名单：永久排除

绝不能把以下内容当证据引用。

**中文语境：**
- 知乎：无法核实的匿名回答，转述泛滥
- 微信公众号：大多是二手内容的重新包装
- 百度百科：不可靠，经常过时或带宣传色彩
- 搜狐 / 网易 / 腾讯的自动生成新闻聚合页

**通用：**
- 内容农场与 SEO 优化的摘要站
- AI 生成的传记页面
- 清单体文章（“从 X 身上学到的 10 课”），除非直接引用并链接了一手来源
- 维基百科作为独立证据（只可用作指向真实来源的路标）
- 任何本身就是“摘要的摘要”的来源

### 分地区推荐来源

**中文人物：**
- B 站原创长视频与访谈
- 小宇宙完整播客单集
- 权威媒体：36氪、晚点 LatePost、财新、极客公园、虎嗅
- 官方微博（认证账号的直发内容，不是转发或粉丝号）
- 已出版书籍（通过正规渠道）
- 混沌学园、湖畔大学、得到课程的讲课录音（公开可得时）

**英文人物：**
- YouTube 长篇访谈（Lex Fridman、Tim Ferriss、Joe Rogan 等）
- 个人博客与 newsletter（Substack、个人网站）
- 已出版书籍与文章
- 带时间戳的播客完整单集
- 权威特稿：New Yorker、Atlantic、Bloomberg、Wired、NYT、FT
- 有完整视频/文字实录的大会演讲（TED、Y Combinator 等）

### URL 落地规则

以下**不算**有据可查的来源：

- 平台首页（youtube.com、weibo.com、bilibili.com）
- 搜索结果页（/search、/s?）
- 话题或标签页（/topic/、/tag/）
- 没有具体内容的个人主页根路径
- 占位路径（v.qq.com/detail/）
- 任何你没有真正打开并阅读过的 URL

有据可查的 URL 必须是实际查看过的页面，不能是平台首页或占位路径。

### 无字幕音视频的工具处理

没有字幕的长访谈和播客往往是对话与表达 DNA 最丰富的来源，不要跳过。使用 Whisper 转写工具（faster-whisper、openai-whisper 或 OpenAI API，哪个可用就用哪个）：

- `tools/research/transcribe_audio.py --url "<URL>" --output /tmp/x.txt`
- 本地文件：`--input /path/to/file.mp3 --output /tmp/x.txt`
- 指定模型：`--backend faster-whisper --model medium`
- 固定语言（提升准确率）：`--language zh` 或 `--language en`

工作流：

1. 转写到临时路径（绝不放进 skill 目录内）。
2. 通读一遍转写稿，带时间戳地提取改写后的发现。
3. 只把改写后的笔记连同来源元数据记录到 `knowledge/research/raw/` 下。
4. 丢弃原始转写稿。skill 目录里绝不能留长篇逐字转写稿：既违反版权安全，也过不了审计。

如果当前环境装不上该工具，明确告诉用户，不要静默跳过某个维度。

### 可选：X 公开帖子采集

仅当短篇第一人称帖子能补上某个具体缺口时，才使用 `tools/research/xquik_public_posts.py`。该服务按返回帖子数计量，所以先确认配额，并写到 skill 目录之外的临时文件。把它的规范化 JSON 当作不可信的候选证据，而不是一条研究轨道。选择前先核实作者，并逐个打开 permalink。只把相关证据安全改写进对应笔记，保留具体 URL、访问日期、grounding level 与来源权重，复查后删除临时候选文件。
绝不要把候选文件、搜索页或主页根路径当作有据可查的来源。

---

## 六维度并行采集

研究必须覆盖六个维度。把每个维度当成一条独立的调查轨道，有各自的提取重点。不要把整轮研究压成一份单一的大笔记；你所在档位的输出契约规定了每个维度写入哪个文件。

### 维度 1：著述

**目标**：出自本人笔下、经过深思的系统性立场，即发表前有时间从容思考的内容。

搜索并记录：
- 书籍（每章核心论点，不是摘要或全文）
- 文章、博客帖子、newsletter
- 流出的信件、备忘录与内部文档
- 多篇著述中反复出现的核心论点
- 其书面论证随时间的演变

**提取重点**：核心论题、推理链、组织论证的方式、反复选择撰写的主题。

### 维度 2：对话

**目标**：临场思考的样子：在对话中、有压力时、来不及准备时。

搜索并记录：
- 长篇播客节目（30 分钟以上，优先完整单集）
- 有实质性往复问答的视频访谈
- 圆桌讨论与辩论（尤其是他们表达异议的场合）
- 观众提出意外问题的 AMA / 问答环节
- 他们如何回应敌意或不公平的问题

**提取重点**：即兴推理、如何应对意外、被质疑时回到什么论点、如何表达异议。

### 维度 3：表达 DNA

**目标**：他们的语言指纹：不在于说什么，而在于怎么说。

跨多个来源实例分析（budget-unfriendly 档位下至少 5 个）：
- 句子节奏：平均长度、变化幅度、短句与复杂句的运用
- 比喻清单：他们从哪些领域取类比？
- 异议框架：直接对抗？重新定义问题？幽默？不屑回应？
- 压缩程度：是完整解释，还是默认听众具备专业背景？
- 确定性语言：他们如何表达确信与存疑？
- 反复出现的短语、口头禅、标志性框架
- 幽默风格（如有）：自嘲、荒诞、冷面、好斗、讽刺
- 语气切换：在随意与正式场合之间，他们的声音如何变化？

**提取重点**：能通过“100 词盲测”的风格标记：把名字去掉，你还能从一段文字里认出这个人吗？

### 维度 4：决策

**目标**：他们实际做了什么，而不只是说过要做什么。

搜索并记录：
- 重大押注：他们在什么上投入了时间/金钱/声誉，理由是什么
- 掉头：在哪里改变了方向，触发因素是什么
- 权衡取舍：明确牺牲了什么换取什么
- 失败：他们如何谈论搞砸的事（或回避不谈）
- 用人/组队决策：选择与谁共事，为什么
- 时机决策：什么时候快跑，什么时候等待

**提取重点**：决策模式、风险容忍度、什么样的证据能打动他们、宣称的价值观与实际显示出的偏好之间的落差。

### 维度 5：外界评价

**目标**：存在于他人脑中的那个版本的他们，尤其是与自我叙述相分歧之处。

搜索并记录：
- 有实质内容的批评（不是人身攻击）
- 可信观察者指出的矛盾
- 合作者、对手与继任者如何描述他们
- 领域同行公认的认知盲区
- 能揭示非显而易见之处的赞扬
- 公开人设与被报道的私下行为之间的落差

**提取重点**：外部视角与内部视角在哪里分歧。别人看到了而他们自己看不到的东西。

### 维度 6：时间线

**目标**：他们的思想如何演变，而不只是“何时发生了什么”的履历。

构建一条追踪以下内容的时间线：
- 带**认知影响**的关键里程碑（这个事件如何改变了他们的思考？）
- 思想转折点：核心信念在什么时候发生了转变？
- 阶段切换：他们的思考是否存在界限分明的几个时期？
- 近期动态（最近 12 至 24 个月）
- 曾经相信、如今不再相信的东西

**提取重点**：认知演变的轨迹，而不是编年传记。

---

## 冷门人物协议

如果研究过程中发现某些维度的覆盖非常单薄：

1. **不要编造**证据、引语或出处来填补空缺
2. **明确标注每个单薄维度**，写清缺什么、为什么缺
3. **统计有据来源总数**：少于 10 个，即为冷门人物
4. 对冷门人物：
   - 心智模型最多限 2 至 3 个
   - 给每个单薄的模型和维度加上“基于有限信息”标记
   - 扩充诚实边界部分
   - 告诉用户补充什么具体材料能提升质量
   - 在 budget-unfriendly 档位下，考虑是否继续，或建议改换材料更充分的人物

---

## 输出契约：budget-friendly

在 `knowledge/research/raw/` 下创建至少三份原始笔记文件，每份覆盖两个维度：

- `01_core_profile.md`：维度 1 + 6（著述 + 时间线）
- `02_conversations_and_material.md`：维度 2 + 4（对话 + 决策）
- `03_expression_and_reception.md`：维度 3 + 5（表达 DNA + 外界评价）

每个文件必须使用以下结构：

```md
# <track title>

## Dimension Coverage
- Dimensions covered: [list]
- Collection strategy used: [web-only / web+local / local-first]

## Source Metadata
- URL: ...
- Source type: interview / book / essay / talk / podcast / social post / article / profile
- Grounding level: primary / secondary
- Access note: public / partial / blocked
- Source weight: [1-7, per hierarchy above]

## Key Findings
- ...

## Patterns and Repeated Themes
- ...

## Contradictions
- ...

## Inferences (clearly marked as inference, not fact)
- ...

## Gaps and Missing Information
- ...
```

### 最低质量底线（budget-friendly）

就整套笔记而言：

- 至少 3 份原始笔记文件
- 至少 2 个有据可查的来源 URL（实际查看过的页面，不是首页）
- 每个文件都清楚区分证据与推断
- 至少识别出 1 处矛盾（或明确注明未发现）
- 至少承认 1 处信息缺口

### 质量检查点（budget-friendly）

完成研究轮之后、进入分析之前，产出一份结构化的质量摘要：

```
┌──────────────────────────────┬──────────┬─────────────────────────────┐
│ Dimension                    │ Sources  │ Key Finding                 │
├──────────────────────────────┼──────────┼─────────────────────────────┤
│ 1 Writings                   │ N        │ [core thesis / gap]         │
│ 2 Conversations              │ N        │ [key pattern / gap]         │
│ 3 Expression DNA             │ N        │ [style marker / gap]        │
│ 4 Decisions                  │ N        │ [decision pattern / gap]    │
│ 5 External Views             │ N        │ [outside perspective / gap] │
│ 6 Timeline                   │ N        │ [trajectory / gap]          │
├──────────────────────────────┼──────────┼─────────────────────────────┤
│ Contradictions found         │ N        │ [summary]                   │
│ Thin dimensions              │ [list]   │ Mitigation: [plan]          │
│ Cold figure?                 │ yes/no   │                             │
└──────────────────────────────┴──────────┴─────────────────────────────┘
```

把这份摘要呈给用户，等确认后再进入分析。
如果用户指出问题或想加深某个维度，就扩展研究。

---

## 输出契约：budget-unfriendly

在 `knowledge/research/raw/` 下创建六份原始研究笔记文件，每个维度一份。不要合并维度，也不要把观察复制到多个文件。不要用一份合并的草稿本顶替这六个文件。

- `01_writings.md`
- `02_conversations.md`
- `03_expression_dna.md`
- `04_decisions.md`
- `05_external_views.md`
- `06_timeline.md`

每个文件必须包含：

```md
# <dimension title>

## Collection Metadata
- Dimension: [number and name]
- Collection strategy: [web-only / web+local / local-first]
- Sources searched: [count]
- Sources used: [count]
- Primary vs secondary ratio: [X:Y]

## Source Metadata
(repeat for each source)
- URL: ...
- Source type: book / essay / interview / podcast / talk / social post / article / profile / decision record
- Grounding level: primary / secondary
- Access note: public / partial / blocked
- Source weight: [1-7, per hierarchy above]
- Date: [publication or access date]

## Evidence
- ...

## Patterns and Repeated Themes
- ...

## Contradictions
- ...

## Inferences (clearly marked)
- ...

## Gaps and Missing Information
- ...
```

### 最低质量底线（budget-unfriendly）

就整套六轨集合而言：

- 至少 6 份原始笔记文件（每维度一份）
- 至少 8 个有据可查的来源 URL
- 至少 3 个一手来源标记
- 至少 6 个来源元数据块（每个文件至少一个）
- 全套至少 6 条矛盾条目
- 全套至少 6 条推断条目
- 0 行潜在长引语（版权安全）
- 轨道覆盖数 = 6（不跳过任何维度）

### 保持各轨道彼此独立

- 不要把同样的观察复制进全部六个文件
- 每个维度都有明确的提取重点，照做
- 如果一条发现与多个维度相关，把主要证据放进最相关的文件，并在其他文件加一条交叉引用注记

### 质量检查点（budget-unfriendly）

完成全部六份研究文件之后、进入审计之前，产出一份结构化摘要：

```
┌──────────────────────────────┬──────────┬──────────┬─────────────────────────────┐
│ Dimension                    │ Sources  │ Primary% │ Key Finding                 │
├──────────────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ 1 Writings                   │ N        │ XX%      │ [core thesis / gap]         │
│ 2 Conversations              │ N        │ XX%      │ [key pattern / gap]         │
│ 3 Expression DNA             │ N        │ XX%      │ [style marker / gap]        │
│ 4 Decisions                  │ N        │ XX%      │ [decision pattern / gap]    │
│ 5 External Views             │ N        │ XX%      │ [outside perspective / gap] │
│ 6 Timeline                   │ N        │ XX%      │ [trajectory / gap]          │
├──────────────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Total grounded URLs          │ N        │          │                             │
│ Primary-source markers       │ N        │          │ Target: ≥3                  │
│ Contradictions found         │ N        │          │ [summary of top 3]          │
│ Candidate mental models      │ N        │          │ [brief list]                │
│ Known-answer candidates      │ N        │          │ [questions with evidence]   │
│ Thin dimensions              │ [list]   │          │ Backfill plan: [plan]       │
│ Cold figure?                 │ yes/no   │          │                             │
└──────────────────────────────┴──────────┴──────────┴─────────────────────────────┘
```

把这份摘要呈给用户，等确认后再进入审计。

### 审计就绪

第六个文件存在不等于研究轮完成。只有当六轨集合看起来足够扎实、能通过一次独立的研究审计时，研究轮才算完成。

继续推进之前，确保笔记能支撑：

- 至少 3 个有跨维度证据支撑的候选心智模型
- 至少 2 个带证据锚点的候选“已知答案”问题
- 至少 1 个可信的、需要外推的边界情况问题
- 一份可见的矛盾清单，至少 3 处实质性张力
- 足够的表达 DNA 样本，能通过风格盲测

---

## 输出规则

- 清楚区分以下各项：
  - 他们说过什么（一手，引用或改写）
  - 他们做过什么（有记录的行动）
  - 别人如何评价他们（外部，有出处）
  - 你推断出什么（标注为推断）
- 保留矛盾：它们是特性，不是缺陷
- 深度优先于广度
- 如实记录来源缺口：缺口也是信息；如果无法获得可核实的外部来源，就明说
- 绝不虚构来源、URL、引语或文献细节
- 只记录你真正打开查看过的 URL
- 用用户的语言写作

## 版权安全

- 不要把完整转写稿、整份字幕、类转写文本块或大段复制的对话写进 skill 目录
- 不要粘贴书籍、字幕、访谈或文章的长篇摘录
- 直接引语要非常短（不超过 2 句）且少量使用，仅在捕捉表达 DNA 必要时
- 用自己的话总结，附来源元数据和出处
