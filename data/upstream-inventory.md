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

## 六、第三批候选：接下来 20 个（2026-10-25 检索）

**检索方式**：GitHub Search API，三路查询——`topic:claude-skills` + `topic:agent-skills`（stars:>2000）、`claude skills in:name,description`（stars:>3000）、`topic:ai-agents topic:skills`（stars:>3000），与第一、二批已收录/已排除项去重。
**核实口径**：每项均经 gh api 核实 License 与目录结构（SKILL.md 有无、语言、skill/工具性质）；网络失败重试 ≥5 次后仍失败才标待查。已完成收录的项目不再列入。

### 收录候选（按星标排序，20 个）

| # | 仓库 | 星标 | License | 类型 | 收录方式与旗舰建议 |
|:-:|---|---:|---|---|---|
| 1 | garrytan/gstack | 137,471 | MIT | 整仓型工具链 | **"整仓收录"模式**（第二批已预登记）：office-hours / plan-ceo-review / qa 三个旗舰 + 根 bin/ 依赖 |
| 2 | wshobson/agents | 41,627 | MIT | Agent 定义型插件市场 | 旗舰抽取；产出物为 Agent 定义而非 SKILL.md，收录前需确认管线适配（如按 harness 分组） |
| 3 | alirezarezvani/claude-skills | 28,641 | MIT | 380 件大合集 | 按热度抽 3-5 个旗舰 skill |
| 4 | phuryn/pm-skills | 27,343 | MIT | PM 技能市场（5 组） | 旗舰：create-prd / intended-vs-implemented / ab-test-analysis |
| 5 | AgriciDaniel/claude-seo | 20,063 | MIT | SEO 26 子 skill + extensions | 旗舰：skills/seo-agentic + seo-audit；extensions/*（第三方集成）排除 |
| 6 | teng-lin/notebooklm-py | 19,878 | MIT | skill + Python 包 | SKILL.md + notebooklm/ 包原样（skill 依赖 CLI/API） |
| 7 | wanshuiyin/Auto-claude-code-research-in-sleep | 18,006 | MIT | 科研自动化 skills | 旗舰：auto-paper-improvement-loop / auto-review-loop / arxiv |
| 8 | yusufkaraaslan/Skill_Seekers | 15,212 | MIT | 文档→skill 转换器 | skills/skill-seekers（"造 skill 的 skill"） |
| 9 | Orchestra-Research/AI-Research-SKILLs | 13,904 | MIT | AI 研究 skills | 旗舰：0-autoresearch-skill + 01~06 领域件按需 |
| 10 | Vincentwei1021/video-shotcraft | 13,373 | Apache-2.0 | 单 skill（电影级产品视频） | 整目录（自带 README_CN，中欧受众明确） |
| 11 | Jeffallan/claude-skills | 12,039 | MIT | 67 全栈 skills | 旗舰抽取（code-reviewer / api-designer / cloud-architect 等） |
| 12 | tw93/Waza | 7,356 | MIT | 规则插件型（无 SKILL.md） | **结构待评估**：plugins/waza/rules/*.md 习惯规则集；需先定义"规则型收录"管线再动手 |
| 13 | MengTo/Skills | 6,989 | MIT | 设计师/构建者 skills | agent-skills/ 目录旗舰抽取 |
| 14 | czlonkowski/n8n-skills | 6,517 | MIT | n8n 工作流 skills | 旗舰：n8n-code-javascript / n8n-error-handling 等按热度 |
| 15 | gamedev-skills/awesome-gamedev-agent-skills | 3,912 | Apache-2.0 | 74 游戏开发 skills | 旗舰抽取（Godot/Unity/Unreal 各一） |
| 16 | HughYau/qiushi-skill | 3,825 | MIT | 单 skill（先调查后动手） | 整目录 |
| 17 | foryourhealth111-pixel/Vibe-Skills | 3,764 | Apache-2.0 | skill 路由编排 | 整目录 |
| 18 | NVIDIA/skills | 3,718 | Apache-2.0 + CC-BY-4.0 | 官方产品 skills | 旗舰：nvidia-skill-finder（元 skill）+ 1-2 个通用件；双许可需在 NOTICES 分别声明 |
| 19 | bergside/awesome-design-skills | 3,329 | MIT | 67 设计 skills 合集 | 旗舰抽取 |
| 20 | tradermonty/claude-trading-skills | 3,250 | MIT | 交易分析 skills | 旗舰抽取（backtest-expert / data-quality-checker 等）；金融内容加免责声明 |

### 检索后排除（新证据）

| 仓库 | 星标 | 排除理由 |
|---|---:|---|
| Imbad0202/academic-research-skills | 53,725 | **License 为 CC BY-NC 4.0（非商业）**——非宽松许可，与仓库变现路径（Sponsors/咨询）冲突，原则 #2 排除。GitHub API 显示 NOASSERTION，LICENSE 原文核实 |
| Graphify-Labs/graphify | 134,312 | 工具型（Docker 服务，无 SKILL.md），非 Skill 文件 |
| code-yeongyu/oh-my-openagent | 70,303 | 工具型 + License NOASSERTION（非标准），双项不合格 |
| SnailSploit/Claude-Red | 8,813 | **内容政策排除**：攻击性安全（offensive security）技能库，超出合规汉化范围 |
| elementalsouls/Claude-BugHunter | 5,271 | 内容政策排除：外部红队/漏洞挖掘技能包，同上 |
| KKKKhazix/khazix-skills | 21,621 | 中文原生（SKILL.md 正文为中文，leader 实核），无需翻译；可作原创仓引流参考 |
| zenstory-ai/oh-story-claudecode | 7,962 | 中文原生（story-long-write description 实核为中文），无需翻译 |
| tradecatlabs/vibe-coding-cn | 17,745 | 中文原生工具箱 |
| zLanqing/codex-claude-academic-skills | 5,255 | 中文原生（学术 skills） |
| diet103/claude-code-infrastructure-showcase | 10,039 | 个人基础设施展示（配置范例），非 Skill 产品 |
| ruvnet/ruflo / zhayujie/CowAgent / nanocoai/nanoclaw 等 | — | Harness/Agent 框架或 App，非 Skill 文件 |

**第三批启动顺序建议**：gstack 整仓模式（含管线改造）→ 单 skill 仓 6 个（video-shotcraft / qiushi / notebooklm / Vibe-Skills / Skill_Seekers / Orchestra）→ 合集旗舰抽取 9 个。wshobson/agents 与 Waza 的"非 SKILL.md 产出物"需先出管线决策。

## 七、第三批实抓结果（2026-10-25，21 个 SKILL.md 收录）

第六节候选中 13 个上游完成收录（wshobson/agents 与 tw93/Waza 因"非 SKILL.md 产出物"管线决策未定继续挂起）：

| 上游 | 模式 | 收录 |
|---|---|---|
| garrytan/gstack | **整仓收录（新模式）** | 整仓原样（排除 .github/test 40MB QA）+ 3 旗舰翻译件 office-hours / plan-ceo-review / qa（各 1300/780 行级）。⚠️ gstack 内置 auto-update 会拉回英文上游覆盖译文，使用中文旗舰时需关闭其自动更新或接受回退 |
| Vincentwei1021/video-shotcraft | 整目录 | **上游 SKILL.md 正文即中文**（中欧双语定位）→ 中文原生收录，逐字节保留；整目录 60MB（Remotion 模板/素材被引用，不可省） |
| teng-lin/notebooklm-py | 单文件 | SKILL.md（Python 包经 pip 安装，仓库文件零引用） |
| foryourhealth111-pixel/Vibe-Skills | 引用集 | SKILL.md + core/ + protocols/（根 SKILL.md 仅引用这两个目录；bundled/ 21MB 兄弟库未收录） |
| yusufkaraaslan/Skill_Seekers | 单文件 | skills/skill-seekers/SKILL.md |
| Orchestra-Research/AI-Research-SKILLs | 整目录 | 0-autoresearch-skill（references + templates 全套） |
| alirezarezvani/claude-skills | 旗舰抽取 | engineering/hivemind + product-team/skills/product-discovery |
| phuryn/pm-skills | 旗舰抽取 | create-prd + intended-vs-implemented |
| AgriciDaniel/claude-seo | 旗舰抽取 | seo-agentic + seo-audit（含各 6 个 references；extensions/ 排除） |
| wanshuiyin/…-in-sleep (ARIS) | 旗舰抽取 | auto-paper-improvement-loop + arxiv |
| Jeffallan/claude-skills | 旗舰抽取 | code-reviewer + api-designer |
| MengTo/Skills | 旗舰抽取 | workflow/workflow-ship-change |
| czlonkowski/n8n-skills | 旗舰抽取 | n8n-code-javascript + n8n-error-handling（各 5 个配套 .md） |

**额外发现与调整**：
- HughYau/qiushi-skill 实核为**中文原生**（矛盾分析等 3 个 skill 正文中文）→ 移出翻译清单，记为中文原生参考。
- video-shotcraft / qiushi 两个"伪英文仓"说明：检索期需抽验 SKILL.md 正文语言，description 英文 ≠ 正文英文。
- fetch_verbatim.py 新增 `--trees` 模式：整仓收录后 verbatim 达 2739 件（累计 3900+），逐文件 API 校验不可行，改为一仓一次 trees API + 本地 `git hash-object` blob SHA 比对（内容哈希等价于逐字节比对）。
- 合计：35 上游 / 52 翻译件（51 实译 + 1 中文原生收录）/ 3918 原样件。

## 八、第四批实抓结果（2026-10-25，20 个 SKILL.md 收录）

11 个上游（10 新 + ECC 追加）：

| 上游 | 模式 | 收录 |
|---|---|---|
| **anthropics/claude-plugins-official**（44.4k） | 旗舰抽取 | frontend-design / claude-md-improver / build-mcp-server（**官方仓库首个合规收录**，Apache-2.0） |
| wshobson/agents（41.6k） | 旗舰抽取 | before-you-build / fastapi-templates（v2 格式实为标准 skills/；挂起解除） |
| iOfficeAI/OfficeCLI（32.4k） | 旗舰抽取 | officecli（Office 文档 CLI 核心 skill） |
| Donchitos/Claude-Code-Game-Studios（27.4k） | Agent 定义抽取 | game-designer / creative-director（沿用第一批 agents/code-reviewer.md 先例） |
| tw93/Waza（7.4k） | **规则型（新模式）** | rules/anti-patterns + clarity（工程习惯规则翻译） |
| NVIDIA/skills（3.7k） | 旗舰抽取 | nvidia-skill-finder / accelerated-computing-cudf（SKILL 文件实为 CC-BY-4.0 AND Apache-2.0 双许可，声明块如实标注） |
| gamedev-skills（3.9k） | 旗舰抽取 | godot-gdscript / unity-csharp-scripting / unreal-cpp-gameplay |
| bergside/awesome-design-skills（3.3k） | 旗舰抽取 | creative |
| tradermonty/claude-trading-skills（3.3k） | 旗舰抽取 | backtest-expert / data-quality-checker（金融内容，README 加风险提示） |
| browser-act/skills（6.3k） | 旗舰抽取 | browser-act |
| affaan-m/ECC（追加） | 旗舰抽取 | strategic-compact（上下文压缩，第二批上游追加） |

**合计：45 上游 / 72 翻译件 / 3984 原样件。**
