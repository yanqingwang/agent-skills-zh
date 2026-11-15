> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/launch/references/shipped-changes.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 从已发布代码到营销

大多数产品更新从未被营销，因为没人做转译。工程师写的 PR 描述是给彼此看的，等营销团队听说时，时机已经过去。能访问代码仓库的 Agent 每周都能弥合这个缺口：读本周发布了什么，判断哪些值得说，再用客户的语言起草出来。

## 输入

针对选定的时间窗口（通常是过去一周，或自上一个 release tag 以来）：
- **已合并的 PR**，含标题、描述和关联 issue。它们对“为什么”的解释比 commit 更到位。
- **Commit log**：覆盖没走 PR 的合并：`git log --since="1 week ago" --no-merges --pretty=format:"%h %s (%an, %ar)"`
- **变更文件**：凡标题没说清用户可感知影响的，就去读。
- **Release notes 或 tag**：如果团队本来就在写。
- **Feature flag**：哪些对客户真正生效，哪些还藏在 flag 后面。

只营销客户今天就能用的东西。藏在 flag 后、内部测试中、尚未部署的，一律先等。

## 先转译，再动笔

工程变更描述的是代码里改了什么；客户关心的是对他们而言改了什么。对每项变更写一句话：**“你现在可以___”** 或 **“___不再___了。”** 这句话填不出来，就说明该变更对客户不可见。重构、依赖升级、CI 和测试变更完全不进任何营销产出。

然后按 `SKILL.md` 的“持续发布策略”一节中的层级给可见变更分组：

| 层级 | 典型变更 | 产出 |
|------|-----------------|--------|
| **Major** | 新能力、新套餐、大的工作流变化 | Changelog + 博客文章 + 邮件 + 社交 + 应用内 |
| **Medium** | 新集成、明显的 UX 改进、客户能感知的性能提升 | Changelog + 定向邮件或应用内消息 + 一条社交帖子 |
| **Minor** | 修复、打磨、小补充 | 仅 Changelog，攒批发布 |

主题相同的几项 medium 变更（“报表的五项改进”）可以打包成一篇 major 层级的叙事。

## 每条说法都锚定在变更上

- 说清变更做了什么，而不是它可能给谁带来什么。“导出现在包含自定义字段”，而不是“解锁更深洞察”。
- 数字只能来自变更本身（PR 里的基准测试、实测的提速）。绝不编造客户成果、采用量或影响力。
- 如果 PR 说变更是部分的（“第一阶段”、“迈向……的第一步”），公告也要这样说。
- 在团队有此惯例且用户同意时，鸣谢提出该需求的用户。

## 留意刚变得失实的营销内容

每次发布也可能让已有说法失实：新增限制、套餐改名、移除集成、价格调整。检查官网、文档、对比页和广告里与该变更矛盾的说法。按固定节奏做，这就是 `marketing-loops` 里的 claim-drift 循环。

新能力还会打开新的搜索需求。新集成值得单独一页（“[Product] + [Tool] integration”），新功能可能让产品赢下以前赢不了的查询或对比。把这些加进内容待写清单（见 `content-strategy` 和 `competitors`）。

## 每周摘要格式

```markdown
## Shipped: [date range]

### For customers
- **[Major]** [You can now ...] (PR #123)
- **[Medium]** [You can now ...] (PR #130)
- **[Minor]** [Fixed ...] (PR #131, #134)

### Changelog entry
## [version or date]
### Added
- [Customer-facing description]
### Changed
- [...]
### Fixed
- [...]

### Drafts
- Blog post: [working title], [angle], [who it's for]
- Email: [subject line options] → [segment]
- Social: [one post per major or medium change, built on its single most useful detail]
- In-app: [message + where it appears]

### Pages to update
- [Page]: [statement that's now wrong or incomplete]

### New content opportunities
- [Query or comparison the change makes winnable]
```

采用 Keep a Changelog 的标题（Added、Changed、Deprecated、Removed、Fixed、Security），让 changelog 长期可扫读。

## 撰写草稿

- **Changelog：**每项变更一行，面向客户，用过去时或现在时写。不明显之处链接到文档。
- **博客文章（仅 major）：**客户原本的问题、改了什么、怎么用（配截图）、适合谁。`copywriting` skill 讲结构；其中的 AI 痕迹规则同样适用。
- **邮件：**开头就讲该细分人群关心的变更；一个行动号召，直达功能页。见 `emails`。
- **社交：**每条帖子一个具体细节，配功能实际运行的截图或 10 秒短片。见 `social`。

草稿只作暂存，供人工审阅后发送。本工作流中没有任何环节会自行发布。
