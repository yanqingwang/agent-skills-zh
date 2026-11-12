# 变更记录（change.md）

> **结果导向**：只记录产出了什么（件数、规模、文件）。过程、检索依据与逐项校验见 [data/review-log-*.md](data/)、[data/upstream-inventory.md](data/upstream-inventory.md) 与 [data/sync-log/](data/sync-log/)。
> **口径**：`SKILL 译件` = manifest `files`；`已译散文` = `translated_prose`；`原样件` = `verbatim`。累计规模以 [data/STATUS.md](data/STATUS.md) 为准。

## 当前结果（2026-11-12）

| 指标 | 结果 |
|---|---:|
| 登记上游 / 纳入监控 | 61 / 60 |
| SKILL 译件 | 215 |
| 已译散文 | 204 |
| 翻译件合计 | 419 |
| 原样件 | 5,043 |
| 收录文件合计 | 5,462 |
| 已汉化 `SKILL.md` | 210 |

按用户角色分布（SKILL 译件）：开发者 87 · 产品与增长 26 · 通用工具 26 · 设计师 20 · 研究者 17 · 企业职能 16 · 游戏开发者 15 · 写作者 6 · 创作者 2。

## 逐批结果

| 批次 | 日期 | 结果 |
|---|---|---|
| 第一批 | 2026-10-24 | 11 个 SKILL 译件 + 55 原样件；4 个上游（MIT） |
| 第二批 | 2026-10-24 | 20 个 SKILL 译件（全生态 Top 20） |
| 第三批 | 2026-10-25 | 21 个 SKILL 译件；13 个新上游；确立整仓模式与旗舰抽取 |
| 第四批 | 2026-10-25 | 20 个 SKILL 译件（官方插件 / Agent 定义 / 规则型）；11 个上游 |
| 第五批 | 2026-10-25 | 35 个 SKILL 译件（企业职能 15 + 旗舰追加 20）；5 个新上游；工作状态自动化 |
| 第六批 | 2026-11-03 | 20 个 SKILL 译件（12 个既有上游）+ 新上游收录；首例重译闭环 |
| 第七批 | 2026-11-03 | pixelfx 新上游 + ui-ux-pro-max 姊妹件 + gsap 全量补齐；累计 168 SKILL 译件 / 5,114 原样件 |
| 散文首批 | 2026-11-03 | 69 篇散文引用件汉化；建立 `translated_prose` 清单与重译工单路径 |
| 第九批 | 2026-11-12 | 20 个 SKILL 译件（7 个存量合集）；累计 195 / 5,168 |
| 第十批 | 2026-11-12 | 20 个 SKILL 译件（6 个存量合集）；累计 215 / 5,181；翻译改用 prose-only 占位标记流水线 |
| 遗留 WIP 落地 | 2026-11-12 | 138 篇散文译文入库：已译散文 66 → 204，原样件 5,181 → 5,043 |

## 遗留 WIP 落地（2026-11-12）

`stash@{0}`（2026-11-01 未提交 WIP）已处理并清理：

- **落地 138 篇**散文译文：逐字节比对确认其英文原件与当前上游一致，登记为 `translated_prose`，写入 `data/file-shas.json` 基线，声明块「原文件」修正为上游路径。
- **保留 14 篇**英文：上游自 11-01 已变化，不引入基于旧版的译文，交由每日同步的重译工单处理。
- **2 个 skills 已收录**（impeccable、unity-navmesh），无重复入库。
- **15 篇**译文中当前 HEAD 已是中文（后续批次已覆盖），无需重复入库。
- **17 个已发现未收录 skills**：源文件为 11-01 旧快照，未直接入库，列入下方清单。

### 待收录清单（17 项，9 项来自 5 个新上游）

🆕 = 尚未登记的新上游。5 个新上游 License 已核实（MIT / Apache-2.0，符合原则 #2）；收录时需补 `THIRD-PARTY-NOTICES.md`、README 上游登记表与 `data/sync-state.json`，正文一律从当前上游 HEAD 重取。

| Skill | 上游 | License | 上游路径 | 目标目录 |
|---|---|---|---|---|
| `2slides-ppt-generator` | sickn33/agentic-awesome-skills 🆕 | MIT | `skills/2slides-ppt-generator/SKILL.md` | `skills/toolbox/office/2slides-ppt-generator/SKILL.md` |
| `bento` | bergside/awesome-design-skills | MIT | `skills/bento/SKILL.md` | `skills/designer/design/bento/SKILL.md` |
| `chaos-engineer` | Jeffallan/claude-skills | MIT | `skills/chaos-engineer/SKILL.md` | `skills/developer/quality/chaos-engineer/SKILL.md` |
| `cold-email` | coreyhaines31/marketingskills | MIT | `skills/cold-email/SKILL.md` | `skills/writer/writing/cold-email/SKILL.md` |
| `content-brief` | Ryze-AI-Adgent/open-seo-mcp-skills 🆕 | MIT | `skills/content-brief/SKILL.md` | `skills/growth/product/content-brief/SKILL.md` |
| `egm-brainstorm` | google/elephant-goldfish-model 🆕 | Apache-2.0 | `skills/egm-brainstorm/SKILL.md` | `skills/developer/engineering/egm-brainstorm/SKILL.md` |
| `egm-draft` | google/elephant-goldfish-model 🆕 | Apache-2.0 | `skills/egm-draft/SKILL.md` | `skills/developer/engineering/egm-draft/SKILL.md` |
| `egm-review` | google/elephant-goldfish-model 🆕 | Apache-2.0 | `skills/egm-review/SKILL.md` | `skills/developer/quality/egm-review/SKILL.md` |
| `frontend-patterns` | affaan-m/ECC | MIT | `skills/frontend-patterns/SKILL.md` | `skills/developer/engineering/frontend-patterns/SKILL.md` |
| `github-actions-templates` | wshobson/agents | MIT | `plugins/cicd-automation/skills/github-actions-templates/SKILL.md` | `skills/developer/engineering/github-actions-templates/SKILL.md` |
| `keyword-research` | Ryze-AI-Adgent/open-seo-mcp-skills 🆕 | MIT | `skills/keyword-research/SKILL.md` | `skills/growth/product/keyword-research/SKILL.md` |
| `n8n-agents` | czlonkowski/n8n-skills | MIT | `skills/n8n-agents/SKILL.md` | `skills/toolbox/automation/n8n-agents/SKILL.md` |
| `od-blog-post` | nexu-io/open-design 🆕 | Apache-2.0 | `design-templates/blog-post/SKILL.md` | `skills/designer/design/od-blog-post/SKILL.md` |
| `od-critique` | nexu-io/open-design 🆕 | Apache-2.0 | `design-templates/critique/SKILL.md` | `skills/designer/design/od-critique/SKILL.md` |
| `open-code-review` | alibaba/open-code-review 🆕 | Apache-2.0 | `skills/open-code-review/SKILL.md` | `skills/developer/quality/open-code-review/SKILL.md` |
| `parallel-feature-development` | wshobson/agents | MIT | `plugins/agent-teams/skills/parallel-feature-development/SKILL.md` | `skills/developer/engineering/parallel-feature-development/SKILL.md` |
| `sql-queries` | phuryn/pm-skills | MIT | `pm-data-analytics/skills/sql-queries/SKILL.md` | `skills/growth/product/sql-queries/SKILL.md` |

## 每次同步的结果

每日 UTC 02:00 的自动同步只产生三种结果：原样件刷新、翻译件变更转重译工单、HEAD 快照推进。逐日记录见 [data/sync-log/](data/sync-log/)，不在本文件重复。
