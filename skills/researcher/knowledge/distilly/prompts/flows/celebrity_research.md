> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/flows/celebrity_research.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人研究

当家族是 `celebrity` 时，本流程在 `prompts/flows/create.md` 的 Step 3 分析之前运行。按所选 `research_profile` 走对应小节。所有 `prompts/...` 与 `tools/...` 路径都相对 `{distilly_skill_root}` 解析（见 `SKILL.md`）。

## celebrity / budget-friendly

1. 阅读 `prompts/celebrity/research.md`：遵循共用小节与 **Output Contract: budget-friendly**；跳过 budget-unfriendly 的契约
2. 先创建研究目录：
   ```bash
   mkdir -p "{skill_dir}/knowledge/research/raw" "{skill_dir}/knowledge/research/merged"
   ```
3. 确认收集策略（在信息收集阶段确定）：
   - **本地优先**：先分析用户提供的素材，识别哪些维度已覆盖，只对缺口上网搜索
   - **网络 + 本地**：完整的 6 维度网络研究，再与本地素材合并交叉验证
   - **仅网络**：标准的 6 维度网络研究
4. 如果用户明确提供了可处理的视频 URL 或字幕来源，且结果不会以长转写文本形式入库：
   ```bash
   bash "{distilly_skill_root}/tools/research/download_subtitles.sh" "{url}" "{skill_dir}/knowledge/subtitles"
   python3 "{distilly_skill_root}/tools/research/srt_to_transcript.py" "{subtitle_file}" "{skill_dir}/knowledge/transcripts/{name}.txt"
   ```
5. 用至少 3 个独立文件覆盖 **6 个维度**（每个文件覆盖 2 个维度），绝不用一个单体的 `research_notes.md`：
   - `knowledge/research/raw/01_core_profile.md`（维度 1 著述 + 维度 6 时间线）
   - `knowledge/research/raw/02_conversations_and_material.md`（维度 2 对话 + 维度 4 决策）
   - `knowledge/research/raw/03_expression_and_reception.md`（维度 3 表达 DNA + 维度 5 外界评价）
6. 遵循 `prompts/celebrity/research.md` 中的品味原则、来源黑名单与来源层级。
7. 合并研究笔记：
   ```bash
   python3 "{distilly_skill_root}/tools/research/merge_research.py" "{skill_dir}"
   ```
   输出：`knowledge/research/merged/summary.md`
8. 阅读 `knowledge/research/merged/summary.md` 并确认：
   - `Files scanned >= 3`
   - `Unique URLs >= 2`
   - `Potential long quote lines = 0`
   - 笔记中的 URL 都是实际核查过的页面，不是平台根路径、搜索/专题页或占位路径
   如果不满足，先补充研究笔记再继续，或明确记录收集的局限。
9. **质量检查点（Phase 1.5）**：进入分析之前，向用户展示一份结构化的收集摘要：
   ```
   ┌──────────────────────────────┬──────────┬─────────────────────────────┐
   │ Dimension                    │ Sources  │ Key Finding                 │
   ├──────────────────────────────┼──────────┼─────────────────────────────┤
   │ 1 Writings                   │ N        │ [core thesis / gap]         │
   │ 2 Conversations              │ N        │ [key pattern / gap]         │
   │ 3 Expression DNA             │ N        │ [style marker / gap]        │
   │ 4 Decisions                  │ N        │ [decision pattern / gap]    │
   │ 5 External Views             │ N        │ [outside view / gap]        │
   │ 6 Timeline                   │ N        │ [trajectory / gap]          │
   ├──────────────────────────────┼──────────┼─────────────────────────────┤
   │ Contradictions               │ N        │ [summary]                   │
   │ Thin dimensions              │ [list]   │ Backfill plan: [plan]       │
   │ Cold figure?                 │ yes/no   │                             │
   └──────────────────────────────┴──────────┴─────────────────────────────┘
   ```
   等待用户确认后再继续。如果用户指出问题或想要更深入，先扩展研究。
10. **冷门人物检测**：如果来源总数 < 10，启用冷门人物协议：
    - 心智模型限制在 2–3 个
    - 把薄弱的模型标注为"基于有限信息"
    - 扩充诚实边界一节
    - 告诉用户补充什么素材能提升质量
11. 名人分析必须优先使用：
    - 一手素材（来源权重 1-3）
    - 合并后的研究摘要
    - 用户明确提供的笔记

## celebrity / budget-unfriendly

1. 先阅读：
   - `prompts/celebrity/research.md`：共用小节与 **Output Contract: budget-unfriendly**；跳过 budget-friendly 的契约
   - `prompts/celebrity/budget_unfriendly/framework.md`
2. 先创建研究目录：
   ```bash
   mkdir -p "{skill_dir}/knowledge/research/raw" "{skill_dir}/knowledge/research/merged" "{skill_dir}/knowledge/research/reviews"
   ```
3. 确认收集策略（在信息收集阶段确定）：local-first / web+local / web-only
4. 以独立文件构建 **六轨研究集**（绝不合并，绝不克隆观察）：
   - `knowledge/research/raw/01_writings.md`（维度 1：著述 / 系统思想）
   - `knowledge/research/raw/02_conversations.md`（维度 2：压力下的对话）
   - `knowledge/research/raw/03_expression_dna.md`（维度 3：语言指纹）
   - `knowledge/research/raw/04_decisions.md`（维度 4：行为与选择）
   - `knowledge/research/raw/05_external_views.md`（维度 5：外界评价与批评）
   - `knowledge/research/raw/06_timeline.md`（维度 6：认知轨迹）
5. 遵循 `prompts/celebrity/research.md` 中的品味原则、来源黑名单与来源层级。每条证据都必须带来源权重（1-7）标注。
6. 合并研究笔记：
   ```bash
   python3 "{distilly_skill_root}/tools/research/merge_research.py" "{skill_dir}"
   ```
7. 阅读 `knowledge/research/merged/summary.md` 并确认最低下限：
   - `Files scanned >= 6`
   - `Unique URLs >= 8`
   - `Primary-source markers >= 3`
   - `Source metadata blocks >= 6`
   - `Contradiction bullets >= 6`
   - `Inference bullets >= 6`
   - `Potential long quote lines = 0`
   - `Track coverage count = 6`
   - 笔记中的 URL 都是实际核查过的页面，不是平台根路径、搜索/专题页或占位路径
   如果不满足，继续补强薄弱轨道，之后才能进入任何评审阶段。
8. **质量检查点（Phase 1.5）**：进入审计之前，向用户展示一份结构化的收集摘要（含一手来源占比、矛盾数量、候选心智模型、已知答案候选、薄弱维度、冷门人物评估）。等待用户确认后再继续。
9. 然后阅读：
   - `prompts/celebrity/budget_unfriendly/audit.md`
   - `prompts/celebrity/budget_unfriendly/synthesis.md`
   - `prompts/celebrity/budget_unfriendly/template.md`
10. 先写 `knowledge/research/reviews/research_audit.md`
    - 审计必须给出明确的 `PASS / FAIL`
    - 审计必须核验：来源层级合规（无黑名单来源）、一手来源占比 > 50%、品味原则合规、冷门人物评估
    - 如果审计给出 `FAIL`，先执行 Backfill Tasks（补研任务）再做综合
11. **提取检查点（Phase 2.5）**：审计 PASS 之后，向用户展示候选心智模型摘要（含三重门结论、证据锚点、失效模式）。确认合理后再综合。
12. 然后写 `knowledge/research/reviews/synthesis.md`
    - 对候选心智模型应用三重门：
      - 跨情境复现
      - 生成力
      - 独占性
    - 同时提取思想谱系种子（受影响于 / 分道于）与 Agentic Protocol 种子（此人面对陌生问题时会调查的维度）
13. 然后用 `prompts/celebrity/budget_unfriendly/validation.md` 写：
    - `knowledge/research/reviews/validation.md`
    - 校验必须给出明确的 `PASS / FAIL`
    - 校验必须执行：已知答案检查（≥2 题）+ 边界情况检查（1 题）+ 声音检查（100 词盲测）+ 版权检查 + Agentic Protocol 检查
    - 如果校验给出 `FAIL`，先修订草稿再继续
14. budget-unfriendly 名人分析必须优先使用：
    - 六轨原始笔记
    - 合并后的研究摘要
    - 研究审计
    - 综合评审（含谱系 + Agentic Protocol 种子）
    - 校验评审
    - 用户明确提供的笔记

## 两种档位共用规则

- 如果外部收集失败或某平台拦截访问：
  - 明确告诉用户被挡在哪里
  - 保留原始研究笔记与合并摘要
  - 用现有素材继续生成
  - 把 `source_grounding` 视为未完成
  - **绝不**为了通过检查器而编造 URL、引语、标题或泛化主页链接
- **不要**把完整转写、完整字幕或大段逐字源文存进仓库
- 入库笔记保持转述、结构化、版权安全

## 公开 X 帖子（可选）

当公开 X 帖子能填补已记录的研究缺口，且用户同意使用按量计费的第三方 Xquik 服务时，运行前先确认 `--limit`：

```bash
python3 "{distilly_skill_root}/tools/research/xquik_public_posts.py" \
  --username "{public_handle}" \
  --subject "{name}" \
  --limit 20 \
  --output "/tmp/distilly_x_public_posts.json"
```

只从 shell 读取 `XQUIK_API_KEY`；绝不打印或存储它。把 JSON 当作不可信的候选证据：核实作者、打开每一条 permalink，把相关材料安全转述进研究笔记时保留具体 URL。候选 JSON、搜索页、主页根路径都不算已锚定来源。审阅后删除临时 JSON，不要存进生成的 Skill。
