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

## 五、第二批：全生态 Top 20（2026-10-24 检索与收录）

**检索方式**：GitHub Search API，`topic:claude-skills` + `topic:agent-skills` 双主题搜索（stars:>2000），并与既有候选库合并排序。
**收录口径**：① License 为 MIT/Apache-2.0 等宽松许可；② 产出物是可 drop-in 的 Skill 文件（工具型 CLI/App/榜单仓库除外）；③ 按星标排序取前 20 个 SKILL.md 翻译件。

### 生态全景新发现（第二批检索补充）

| 仓库 | 星标 | License | 决策 |
|---|---:|---|---|
| morluto/rea | 376,608 | MIT | ✅ 收录 reverse-engineer-anything |
| **anthropics/skills** | 183,439 | **NONE** | ❌ **官方仓库亦无 License，原则 #2 排除** |
| DietrichGebert/ponytail | 175,291 | MIT | ✅ 收录 ponytail（主 skill；5 个变体列第三批候选） |
| JuliusBrussee/caveman | 114,756 | Apache-2.0 | ✅ 收录 caveman 主 skill（3.0 起全仓 Apache-2.0；proxy/CLI 为工具不收录） |
| paperclipai/paperclip | 106,797 | MIT | ❌ App 产品，非 Skill 文件 |
| thedotmack/claude-mem | 102,727 | Apache-2.0 | ❌ 记忆插件/工具，非 Skill 文件 |
| tt-a1i/archify | 88,591 | MIT | ✅ 收录 archify 主 skill（4 个辅助 skill 列第三批候选） |
| Egonex-AI/Understand-Anything | 88,031 | MIT | ✅ 收录 understand 主 skill（8 个 understand-* 子 skill 列第三批候选） |
| mvanhorn/last30days-skill | 65,265 | MIT | ✅ 收录 last30days（不含未引用的 assets/ 14MB） |
| cathrynlavery/diagram-design | 60,572 | MIT | ✅ 收录 diagram-design |
| blader/humanizer | 60,170 | MIT | ✅ 收录 humanizer |
| ayghri/i-have-adhd | 58,558 | MIT | ✅ 收录 i-have-adhd（单文件自包含） |
| coreyhaines31/marketingskills | 56,336 | MIT | ✅ 收录旗舰 product-marketing（上游声明其为所有 skill 的前置基础） |
| K-Dense-AI/scientific-agent-skills | 54,395 | MIT | ✅ 收录 experimental-design（177 个科学 skill 中方法论级、跨域可复用者） |
| virgiliojr94/book-to-skill | 35,953 | MIT | ✅ 收录 book-to-skill |
| OthmanAdi/planning-with-files | 27,618 | MIT | ✅ 收录 planning-with-files |
| titanwings/distilly | 25,974 | MIT | ✅ 收录 distilly |
| latent-spaces/brag | 18,286 | MIT | ✅ 收录 brag（含 assets/music 音频素材，audio.md 引用） |
| nidhinjs/prompt-master | 14,986 | MIT | ✅ 收录 prompt-master |
| VoltAgent/awesome-agent-skills 等 | — | — | ❌ 榜单/精选集，非 Skill 本体 |

### 多 Skill 仓库旗舰抽取（与既有计划对应）

| 仓库 | 星标 | 抽取依据 | 收录 |
|---|---:|---|---|
| affaan-m/ECC | 287,772 | 避开与 superpowers 重叠的 TDD/验证类，选其定位独有旗舰：search-first（research-first 定位主打）、security-review（安全检查清单）、continuous-learning-v2（instinct 学习，ECC 招牌）、autonomous-loops（Harness 自动循环） | ✅ 4 个 |
| garrytan/gstack | 137,471 | office-hours/plan-ceo-review/qa 均引用仓库根 `bin/` 工具链 30+ 处，上游安装形态=整仓克隆（77MB）；单目录收录必悬空 | ⏳ **第三批"整仓收录"模式** |

### 第二批收录清单（20 个 SKILL.md 翻译件）

| # | 上游 | skill | 分类 | 特殊说明 |
|:-:|---|---|---|---|
| 1 | morluto/rea | reverse-engineer-anything | 分析与逆向 | 生态第一大单 skill 仓库 |
| 2 | DietrichGebert/ponytail | ponytail | 工程方法论 | "最懒高级工程师"最小改动哲学 |
| 3 | JuliusBrussee/caveman | caveman | 省 token | 示例电报体保留英文（功能性） |
| 4 | tt-a1i/archify | archify | 图表与可视化 | 整目录含 examples/renderers |
| 5 | Egonex-AI/Understand-Anything | understand | 代码理解 | 931 行，含构建脚本 |
| 6 | mvanhorn/last30days-skill | last30days | 调研与信息 | 170+ 文件自包含运行时（assets 排除） |
| 7 | cathrynlavery/diagram-design | diagram-design | 图表与可视化 | 语义模式体系 |
| 8 | blader/humanizer | humanizer | 写作质量 | 英文 AI 腔示例保留英文 |
| 9 | ayghri/i-have-adhd | i-have-adhd | 输出格式 | 单文件 |
| 10 | coreyhaines31/marketingskills | product-marketing | 市场营销 | 上游钦定基础 skill |
| 11 | K-Dense-AI/scientific-agent-skills | experimental-design | 科学研究 | 4 references + 2 scripts |
| 12 | affaan-m/ECC | search-first | 工程方法论 | research-before-coding |
| 13 | affaan-m/ECC | security-review | 安全 | + cloud-infrastructure-security.md |
| 14 | affaan-m/ECC | continuous-learning-v2 | 记忆与学习 | hooks/scripts 原样（单测排除） |
| 15 | affaan-m/ECC | autonomous-loops | 自动化 | 611 行长文 |
| 16 | virgiliojr94/book-to-skill | book-to-skill | 知识转化 | SKILL.md + book_to_skill/ + scripts/ + tools/ |
| 17 | OthmanAdi/planning-with-files | planning-with-files | 工程方法论 | 24 个脚本 + 模板 |
| 18 | titanwings/distilly | distilly | 知识转化 | tools/ + prompts/ |
| 19 | latent-spaces/brag | brag | 写作质量 | 含 assets/music（被 audio.md 引用） |
| 20 | nidhinjs/prompt-master | prompt-master | 提示词工程 | + references/ |

**第二批落选与延后**：wshobson/agents（41,627，MIT，产出物为 Agent 定义而非 Skill，维持第三批）、alirezarezvani/claude-skills（28,633，380 件大合集，第三批按热度抽取）、alchaincyf/huashu-design 与 JimLiu/baoyu-skills（中文原生，无需翻译）、video-shotcraft/brag-slim/ponytail 变体/rea 与 archify 辅助 skill（第三批候选）。

