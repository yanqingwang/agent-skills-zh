# 上游仓库检索数据（upstream inventory）

**检索方式**：GitHub Search API（认证账号 yanqingwang）· **快照日期**：2026-10-24
**检索式**：`stars:>3000 created:>2026-01-01 sort:stars`（2026 年新仓星标榜）+ `stars:>2000 pushed:>2026-10-01`（活跃榜）
**用途**：确定汉化范围与优先级；收录门槛 = 星标 ≥ 100k 且 License 为宽松开源（MIT 等）。

## 一、候选仓库全景（2026 年星标榜）

| 仓库 | 星标 | License | 语言 | 主题 | 收录决策 |
|---|---:|---|---|---|---|
| obra/superpowers | 304,464 | MIT | Shell | Skills 框架 + 开发方法论 | ✅ 第一批（5 文件） |
| mattpocock/skills | 302,187 | MIT | Shell | 个人工程 Skills 合集 | ✅ 第一批（2 文件） |
| affaan-m/ECC | 287,688 | MIT | JavaScript | Harness 性能优化（skills/instincts/memory） | ⏳ 第二批候选 |
| garrytan/gstack | 137,453 | MIT | TypeScript | CEO/Designer 工具集 | ⏳ 第二批候选 |
| addyosmani/agent-skills | 110,103 | MIT | JavaScript | 生产级工程 Skills | ✅ 第一批（3 文件） |
| Leonxlnx/taste-skill | 101,829 | MIT | JavaScript | 设计品味 Skill | ✅ 第一批（1 文件） |
| **multica-ai/andrej-karpathy-skills** | **223,159** | **无 License** | — | Karpathy 人格 Skill | ❌ **排除（无 License 不翻译）** |
| JuliusBrussee/caveman | 114,736 | 待查 | Go | 省 token 的 viral skill + proxy | ⏳ 查 License 后定 |
| rtk-ai/rtk | 84,429 | 待查 | Rust | CLI 代理省 60-90% token | ⏳ 查 License 后定 |
| mvanhorn/last30days-skill | 65,252 | 待查 | Python | 跨平台近 30 天研究 skill | ⏳ 查 License 后定 |
| career-ops-hq/career-ops | 76,923 | MIT | JavaScript | 开源求职 Agent | ❌ 不收录（工具型 CLI，非 Skill 文件；中文机会走原创求职 Agent） |
| wshobson/agents | 41,625 | MIT | — | 多 Harness 插件市场 | ⏳ 第三批（量大，按热度挑） |

## 二、自动分类规则

分类由 `scripts/classify.py` 按 manifest 中文件路径关键词判定：

| 分类 | 匹配关键词 | 第一批文件 |
|---|---|---|
| 工程方法论 | tdd / test-driven / debug / plan / spec / verification / triage | 5 个 |
| 质量与审查 | code-review / reviewer / quality | 2 个 |
| 头脑风暴与构思 | brainstorm / idea / refine | 2 个 |
| 上下文工程 | context | 1 个 |
| 设计品味 | taste / design | 1 个 |

## 三、第一批收录清单（11 个文件）

| # | 上游 | 原文件 | 本地路径 | 分类 |
|:-:|---|---|---|---|
| 1 | obra/superpowers | skills/test-driven-development/SKILL.md | skills/superpowers/test-driven-development/SKILL.md | 工程方法论 |
| 2 | obra/superpowers | skills/systematic-debugging/SKILL.md | skills/superpowers/systematic-debugging/SKILL.md | 工程方法论 |
| 3 | obra/superpowers | skills/writing-plans/SKILL.md | skills/superpowers/writing-plans/SKILL.md | 工程方法论 |
| 4 | obra/superpowers | skills/verification-before-completion/SKILL.md | skills/superpowers/verification-before-completion/SKILL.md | 工程方法论 |
| 5 | obra/superpowers | skills/brainstorming/SKILL.md | skills/superpowers/brainstorming/SKILL.md | 头脑风暴与构思 |
| 6 | mattpocock/skills | skills/engineering/code-review/SKILL.md | skills/mattpocock-skills/code-review/SKILL.md | 质量与审查 |
| 7 | mattpocock/skills | skills/engineering/to-spec/SKILL.md | skills/mattpocock-skills/to-spec/SKILL.md | 工程方法论 |
| 8 | Leonxlnx/taste-skill | skills/taste-skill/SKILL.md | skills/taste-skill/SKILL.md | 设计品味 |
| 9 | addyosmani/agent-skills | skills/context-engineering/SKILL.md | skills/addyosmani-agent-skills/context-engineering/SKILL.md | 上下文工程 |
| 10 | addyosmani/agent-skills | skills/idea-refine/SKILL.md | skills/addyosmani-agent-skills/idea-refine/SKILL.md | 头脑风暴与构思 |
| 11 | addyosmani/agent-skills | agents/code-reviewer.md | skills/addyosmani-agent-skills/agents/code-reviewer.md | 质量与审查 |

**入选理由**：① 覆盖最高频使用场景（写码/调试/审查/计划）+ 最热话题（上下文工程/设计品味）；② 单文件自包含（第一批不引入 references/ 依赖链，降低同步负担）；③ 5 个分类各有代表，验证"自动分类 → 索引"管线。

## 四、第二批候选（待第一批验证管线后启动）

1. affaan-m/ECC 全量 skills（287k 星，覆盖面广，需按热度挑选 10-20 个）
2. caveman / rtk / last30days-skill（确认 License 后收录，工具说明类文件短、翻译快）
3. garrytan/gstack 的 23 个工具（CEO/产品视角，与工程类互补）
4. wshobson/agents 按分类抽取头部
