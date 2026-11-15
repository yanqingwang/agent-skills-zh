> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/customer-research/references/source-guides.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 客户调研：来源指南

逐个来源的详细打法，用于从线上聚集地收集客户情报。

---

## Reddit 调研

### 找对 subreddit

先弄清你的 ICP（理想客户画像）在哪里泡着，而不是别人在哪聊你的产品。

**发现方法：**
- 搜索 `site:reddit.com "[job title] tools"` 或 `site:reddit.com "[problem category] software"`
- 用 [subreddit search tools](https://www.reddit.com/subreddits/search) 搜问题空间关键词
- 搜 ICP 的问题，看 Google 结果里冒出哪些 subreddit
- 查竞品客户在评价里提到哪些 subreddit

**按类目常见的高价值 subreddit：**
- B2B SaaS：r/sales, r/marketing, r/entrepreneur, r/startups, r/smallbusiness
- 开发者工具：r/programming, r/devops, r/webdev, r/cscareerquestions
- 分析/数据：r/analytics, r/dataengineering, r/BusinessIntelligence
- 营销：r/PPC, r/SEO, r/emailmarketing, r/content_marketing
- HR/招聘：r/recruiting, r/humanresources, r/jobs
- 财务/运营：r/accounting, r/financialplanning, r/projectmanagement

### 搜索运算符

```
site:reddit.com/r/[subreddit] "[keyword]"
site:reddit.com "[problem]" "recommend" OR "suggestion" OR "alternative"
site:reddit.com "[competitor name]" "vs" OR "alternative" OR "switched"
```

### 要找什么

**高信号帖型：**
- "你用什么工具做 X？" → 揭示竞品与行话词汇
- "对 [竞品] 失望，在找替代品" → 揭示痛点与切换触发器
- "你们怎么处理 X？" → 揭示工作流与变通办法
- "[你的品类] 值不值？" → 揭示异议与评估标准
- 针对竞品的吐槽帖 → 揭示你可能补上的空缺

**要提取什么：**
- 帖子里描述的确切问题
- 高赞解决方案（从业者实际推荐什么？）
- 评论区对现有方案的抱怨
- 所用语言：记下具体的词和短语
- 点赞模式：共识还是争议

### 工具
- Reddit 站内搜索（有限但快）
- Google：`site:reddit.com [query]`（效果更好）
- Pullpush.io：搜归档的 Reddit 帖（旧帖好用）

---

## G2 与评价站挖掘

### 自家产品的评价

按这个顺序读，信号最大：

1. **3 星评价**：最诚实。客户认可到愿意留下，但觉得缺点什么。
2. **1 星评价**：搞清失败模式。把产品问题与客服/上手问题分开。
3. **5 星评价**：提取"他们爱什么"的原话。这些是你的证明点。
4. **4 星评价**：夸奖里常埋着"唯一希望……"。

**要提取什么：**
- 他们说自己*拿它来做什么*（待完成任务）
- 他们说最难或最烦的部分
- 他们拿它和什么比（"从 [X] 转来""比 [Y] 好"）
- 评价者资料里的行业与角色信号

### G2 上的竞品评价

竞品的 4 星评价是金矿：喜欢产品但仍有不满的客户。

**可利用的 G2 结构：**
- "What do you like best?" → 他们的优势（你的销售对抗情报）
- "What do you dislike?" → 他们的弱点（你的机会）
- "What problems are you solving?" → 待完成任务

**Capterra** 结构类似。**Trustpilot** 偏 B2C。**AppSumo** 的评价对 SMB/准专业级 SaaS 有用。

### 评价挖掘模板

对每个竞品的 4 星评价，提取：

| 类别 | 记录 |
|----------|-------|
| 待完成任务 | 他们为什么用这个产品？ |
| 头号夸奖 | 他们爱什么（你可能难以匹敌）？ |
| 头号抱怨 | 什么让他们烦？ |
| 切换背景 | 提没提从别的产品切过来？ |
| 未满足需求 | "要是能……就好了"或"如果……会更好" |

---

## Indie Hackers 与 Product Hunt

### Indie Hackers

对创始人/独立开发者/SMB 型 ICP 信号很强。

**去哪看：**
- "Ask IH" 帖：关于你的产品所解决问题的提问
- 里程碑帖：创始人描述技术栈时会暴露工具偏好和痛点
- 你所在品类的产品发布帖的评论区

**搜索：**`site:indiehackers.com "[problem]"`，或用 IH 站内搜索。

### Product Hunt

竞品页的**讨论区**是调研金矿：
- 提出的问题 = 售前顾虑 = 异议
- 评论 = 早期采用者反应 = 市场接受度的领先指标
- "X 的替代品"合集揭示用户眼中的竞争格局

---

## Hacker News

对技术/开发者型 ICP 信号很强。偏建造者和怀疑论者。

**高价值搜索：**
- `site:news.ycombinator.com "[competitor or category]"`
- "Ask HN: best tools for X" 类帖子
- 竞品的 "Show HN" 帖：去读那些怀疑的评论

**HN 的不同之处：**
- 用户更爱批底层架构和商业模式
- 对定价模式观点强烈（尤其一切订阅制）
- 你在别处听不到的第一性原理式异议

---

## LinkedIn 调研

### 帖子与评论

搜从业者描述工作流的帖子：
- "[角色] at [公司规模]" + 问题关键词
- "我们以前 [旧做法]，现在 [新做法]"的故事
- 求工具推荐的帖子下面有活跃买家的评论

### 招聘启事

招聘启事就是公司对自己痛点的自白。

**看什么：**
- 哪些工具列为"加分项"而非"必备"？（揭示技术栈和相邻工具）
- 职位描述里提到哪些指标和成果？
- 这个岗位大部分时间在干什么？（揭示待完成任务）

**搜索：**`site:linkedin.com/jobs "[role title]" "[relevant tool or category]"`

---

## YouTube 评论

### 找高信号视频

- 讲你产品所解决问题的教程视频
- "[year] 年 X 最佳工具"盘点视频
- 竞品演示与走查视频

**评论里找什么：**
- "这个能用于 [具体场景] 吗？" → 边界情况与未满足需求
- "我试过，但是……" → 失败点
- "[竞品] 怎么样？" → 正在评估
- 带时间戳的提问 → 工作流中的困惑点

---

## Twitter / X 调研

### 搜索运算符

```
"[competitor]" -filter:replies min_faves:10
"[problem keyword]" "anyone know" OR "recommend" OR "alternative"
"[category] is broken" OR "frustrated with [category]"
```

### 能找到什么

- 对竞品的实时抱怨
- 从业者聊自己的技术栈
- 你的 ICP 关注的影响者/意见领袖（分发有用）

---

## 博客与论坛调研

### 对比类内容

用 Google 搜：`"[competitor 1] vs [competitor 2]"` 或 `"best [category] software [year]"`

读这些文章的评论：会搜对比内容的人正在评估中。他们的评论就是你的销售流程该回答的问题。

### 小众社区

- **Slack 社区**：很多行业有公开或半公开的 Slack 群。搜 "[industry] Slack community"。
- **Discord 服务器**：在开发者与创作者社区中持续增长。
- **Facebook 群组**：对 SMB、电商、代理商、教练/咨询类 ICP 仍然很强。
- **Circle/Mighty Networks 社区**：查查你的 ICP 所在领域有没有付费社区。

---

## B2C 与消费级应用调研

B2C 调研的来源和 B2B SaaS 不同。消费级买家不聚在 LinkedIn 或 G2 上，他们的痕迹留在应用商店、社交媒体、以及围绕你产品所服务的那种活动建起来的社区里。

### 应用商店评价（iOS App Store / Google Play）

移动/消费级产品最丰富的未过滤来源之一。

**按这个顺序读：**
1. **1-2 星评价**：失败模式、未满足的期待、怨气峰值
2. **3 星评价**：诚实的取舍，"不错，但是……"式反馈
3. **5 星评价**：用他们自己的话说爱什么（证明点与定位素材）

**要提取什么：**
- 他们"雇"这个应用来干什么（"我用它来……"）
- 它对他们失效的那一刻
- 他们拿它跟什么比、从什么切换过来
- 情绪化语言："我喜欢的是……""最让我抓狂的是……"

**搜索技巧：**先按 "Most Recent"（最新）排序拿新鲜信号，再按 "Most Critical"（最严厉）排序看痛点主题。

### Amazon 评价（实体产品或在 Amazon 有售的软件）

优先级顺序同应用商店：先读 3 星评价。

**消费级 SaaS 的 G2 等价物**：Trustpilot、Sitejabber，以及特定产品的评价聚合站。

### Reddit 消费者社区

B2C 的 Reddit 高度垂直：去爱好/生活方式 subreddit，别去大杂烩。

**按产品类型举例：**
- 健身应用：r/running, r/loseit, r/fitness, r/MyFitnessPal
- 个人理财：r/personalfinance, r/financialindependence, r/ynab
- 生产力/笔记：r/productivity, r/Notion, r/ObsidianMD
- 旅行：r/travel, r/solotravel, r/digitalnomad
- 育儿：r/Parenting, r/beyondthebump, r/daddit

**搜索句式：**`site:reddit.com/r/[community] "[app name OR problem]"`

### TikTok 与 Instagram 评论

对有视觉/生活方式吸引力的消费级产品信号很强。

**怎么找信号：**
- 在 TikTok 搜 "[product name] review" 或 "is [product] worth it"
- 看前 5-10 条视频；把所有评论都读一遍，别只看点赞
- Instagram 上查真实用户的被标记帖（不是品牌帖）

**要提取什么：**
- 评论里的提问 = 未满足需求或定位不清
- "这个能用来……吗？" = 他们想雇它干的活
- "我从 X 换过来的"评论 = 切换触发器
- 关于价格、缺功能或承诺落空的抱怨

### YouTube 评论（消费级）

方法同 B2B，但视频类型不同：

- "X 应用真实测评"或"X 应用用了 6 个月"
- "[year] 年最佳 [品类] 应用"对比视频
- 硬件/实体产品的开箱或"安装"视频

测评视频下的评论尤其值钱：这些人正处在考虑阶段。

### 消费者社区平台

- **Facebook 群组**：对许多消费垂类仍是主阵地（育儿、健身、本地服务、爱好）
- **Discord 服务器**：在游戏、创作者工具、生产力、加密货币、生活方式社区中增长
- **Nextdoor**：对本地服务业有用
- **Quora**：长问题的背后是决策焦虑和评估标准

---

## SparkToro（受众情报）

SparkToro 是行为型受众研究工具。它不逐帖逐评去挖，而是聚合点击流、搜索和社交数据，大规模呈现你的受众在做什么：读什么、看什么、听什么、关注谁、搜什么。

### 何时用 SparkToro，何时手动调研

- **先用 SparkToro**：要弄清 ICP 在哪出没、消费什么内容、关注哪些影响者时，它用聚合数据几秒出答案
- **先手动调研**（Reddit、G2、社区）：需要原始语言、精确引述、情绪语境和行为背后的"为什么"时
- **最好搭配用**：先用 SparkToro 定出哪些播客、subreddit 和网站重要，再去这些来源手动挖客户原声

### 要跑的关键查询

**按竞品：**
- "People who follow @competitor"（关注 @竞品 的人）：揭示受众的共同偏好
- "People who visit competitor.com"（访问 competitor.com 的人）：显示他们还消费什么

**按受众描述：**
- "People who frequently talk about [topic]"：找到受众行为
- "People whose bio contains [job title]"：刻画基于角色的细分人群

**按自己的受众：**
- "People who visit yourdomain.com"：理解你的真实受众
- 和竞品受众画像对比，找出差距

### 要提取什么

| 数据类型 | 它告诉你什么 | 用在哪 |
|-----------|------------------|------------|
| 常访问网站头部 | 你的受众在哪读 | 内容合作、投稿目标 |
| 播客头部 | 他们听什么 | 播客做客、赞助决策 |
| YouTube 频道头部 | 他们看什么 | 视频内容策略、广告投放 |
| subreddit 头部 | 他们在哪讨论 | 社区参与、Reddit 广告定向 |
| 搜索关键词 | 他们 Google 什么 | SEO 与内容选题规划 |
| AI 提示词话题 | 他们问 AI 工具什么 | 新兴内容机会 |
| 关注的社交账号 | 谁在影响他们 | 影响者合作、联合营销 |
| 人口属性 | 他们是谁 | 画像构建、广告定向 |

### 来源权重

SparkToro 的数据是聚合且匿名的：它呈现的是模式，不是个人观点。把它当作：
- **高可信**：行为数据（访问什么、关注什么、搜什么）
- **中等可信**：人口属性数据（自报，可能不全）
- **不能替代**定性研究（抓不到语言、情绪和"为什么"）

### 局限

- 免费档：每月 5 份报告，结果浅（前 5-10 条）
- 无公开 API：全部调研走网页界面
- 偏英语、以美国为中心
- 告诉你受众做什么，不告诉为什么：要与定性来源搭配

工具详情与价格见 [tools/integrations/sparktoro.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/sparktoro.md)。

---

## 整理你的调研

所有来源用一套简单的标签系统：

| 标签 | 含义 |
|-----|---------|
| `#pain` | 一个问题或不满 |
| `#trigger` | 触发搜寻的事件 |
| `#outcome` | 成功长什么样 |
| `#language` | 值得用进文案的原话 |
| `#alternative` | 他们考虑或在用的别的方案 |
| `#objection` | 犹豫或不买的理由 |
| `#competitor` | 关于竞品的一切 |

维护一份滚动更新的文档，列为：来源 | 日期 | 引述 | 标签 | 备注

记到 20-30 条后，模式会浮现。找那些出现在多个互不相关来源里的引述：那就是你置信度最高的洞察。

---

## 来源可靠性与置信度打分

各来源权重不同。打置信度标签时参照本指南。

### 来源权重

| 来源 | 信号强度 | 要注意的偏差 |
|--------|----------------|--------------|
| 客户访谈（非引导） | 很高 | 样本小；偏向高参与度客户的选择偏差 |
| 赢单/输单访谈 | 高 | 只有近期记忆；合理化常见 |
| 应用商店 / G2 评价 | 高 | 偏强烈观点（要么爱要么恨） |
| Reddit / 社区帖 | 中高 | 偏技术、多疑、爱发声的少数派 |
| 工单 | 中 | 偏问题；沉默的大多数不在场 |
| 问卷（开放题） | 中 | 被提问框架带偏 |
| 问卷（选择题） | 中低 | 你给的选项制造出的痕迹 |
| NPS 原话 | 中 | 与分数相关；受调研那一刻引导 |
| YouTube/TikTok 评论 | 中 | 偏高参与观众；社交表演成分 |
| SparkToro 受众数据 | 中高 | 聚合行为数据；擅长"是什么"，不擅长"为什么" |
| 招聘启事 | 中低 | 表达的是愿望，未必反映当前痛点 |

### 置信度标签实战

呈现洞察时，置信度放最前面：

```
[HIGH CONFIDENCE] Customers feel overwhelmed by manual reporting — appears in 12 of 20 interviews,
4 Reddit threads, and is the #1 complaint in 3-star G2 reviews. Consistent across SMB and mid-market.

[MEDIUM CONFIDENCE] Customers compare us to spreadsheets more than to direct competitors —
mentioned in 6 interviews and 3 Reddit threads, but not yet seen in review data.

[LOW CONFIDENCE] Enterprise buyers may have procurement concerns — mentioned by 2 interviewees
from companies 500+. Needs more signal before acting on it.
```

### 时效窗口

- **可作主来源**：最近 12 个月的数据
- **谨慎使用**：12-24 个月（产品和市场可能已变）
- **只作基线背景**：2 年以上

一个主题在新旧数据中反复出现，那就是值得行动的持久信号。
