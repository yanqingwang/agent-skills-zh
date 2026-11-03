> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/hiring-signals.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 招聘信号

当招聘意图选中职位通道时阅读本文件。仅职位规划的例外条款只在本模式内适用。

### 招聘信号模式（`--hiring-signals`）

当用户问某家公司的职位页、招聘页、LinkedIn 职位或竞对的招聘情况暗示了什么战略重心时，使用 `--hiring-signals`。这个方法对早期创业公司最有效，对大公司则较弱，因为大公司里许多不相关的岗位只是招聘噪音。

**直取公司自己的职位板——这正是重点所在。** 引擎以招聘页优先的发现方式抓取公司的直连 ATS（Greenhouse、Ashby、Lever、Workable、SmartRecruiters）：它读取招聘页，从嵌入代码或链接中识别出 ATS 服务商与 slug，再调用该 API 获取完整的结构化职位板。聚合站点（Glassdoor、Indeed、ZipRecruiter、LinkedIn）是嘈杂且有损的最后手段，不是信源。引擎的输出会记录数据来自哪一层 `tier`（`ats` = 权威来源，`careers-jsonld` = 结构化页面数据，`web` = 嘈杂兜底）；请据此调整你的置信度，若本次运行降级到 `web` 层就明说。在 Claude Code 上你可以帮忙做发现：在预研究阶段读取公司的招聘页，找到 ATS 职位板 URL（例如 `jobs.ashbyhq.com/{slug}`），剩下的由引擎自行解析。

**按新颖性与偏离基线的幅度加权，而不是按岗位数量。** 一个战略性岗位的分量可能超过整个部门的人数。引擎会给出一个 `Strategic single-role signals` 清单（创始 / 职能首岗 / 专业化 / 新地区等标志），它**不**受数量门槛限制，要读它，并由你自己判断真正的新颖性，因为"这个领域对这家公司来说是新的吗？"需要关键词映射无法编码的世界知识。具体来说：公司在核心领域开出 5 个工程师岗位 = "加码"（规模信号）；在他们从未涉猎过的领域开出 2 个岗位 = "新下注"（方向信号），而且通常才是更重要的故事。一条 `Founding {Role}, {New Capability}` 职位公告（例如一家以真人访谈起家的公司发布的 "Founding Research Scientist, Human Simulation"）正是原始计数会淹没的高信号线索。在综合环节，要在行文中区分"新下注"与"加码"，而不是单纯按同一主题下有多少岗位来排序。

**限定范围报告的输出标题。** 这是一份限定范围的报告，不是一次通用运行，它使用限定范围的标题，而不是 `What I learned:` 标签。第 1 行放徽标，第 2 行空行，第 3 行写 `# {Company} - Hiring Signals`，然后是综合内容。先讲最强的战略信号（往往是一个新下注），再讲规模信号，最后是引擎的 `## Hiring Signals` 证据块。

**`--hiring-signals` 的范围仅限职位，不要为它构建多来源计划。** 设置 `--hiring-signals` 后，引擎只检索职位来源（会忽略你 `--plan` 中逐子检索词的 `sources`）。因此纯招聘信号运行可以跳过 Step 0.75 的多来源计划工作，一个单子检索词的计划（或干脆不传 `--plan`）就够用了，而一份丰富的 reddit/x/youtube 计划是白费力气，因为会被丢弃。如果用户想在一次运行中同时拿到招聘信号与社区情绪，就在 `--hiring-signals` 之外再显式传 `--search=reddit,x,jobs`（正是这个显式的 `--search` 标志让其他来源保留下来）。

输出必须区分证据与解读。好的写法："3 current roles mention SSO, SOC 2, and procurement workflows, which signals increased enterprise-readiness focus." 不好的写法："They will ship enterprise SSO next quarter." 在标准的 `/last30days Company` 运行中，只有当引擎浮出强信号时才纳入招聘信号；否则整个话题都不要提。

---
