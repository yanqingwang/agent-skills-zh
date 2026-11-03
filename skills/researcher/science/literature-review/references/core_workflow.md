> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/literature-review/references/core_workflow.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 核心工作流

这是一份示意性工作流；其中的检索式、日期、计数与数值发现都不是真实执行综述所得的结果。
请在本 skill 目录下运行命令，并使用指向你自己综述工作区的路径。

完整包含七个阶段：计划与范围界定、系统检索、筛选与遴选、数据提取与质量评估、
综合与分析、引文核验，以及文档生成。

## 核心工作流

文献综述遵循结构化的多阶段流程：

### 阶段 1：计划与范围界定

1. **明确研究问题**：临床/生物医学综述使用 PICO 框架（人群、干预、对照、结局）
   - 示例："CRISPR-Cas9（I）治疗镰状细胞病（P）相比标准治疗（C）的疗效如何？"

2. **确定范围与目标**：
   - 定义清晰、具体的研究问题
   - 确定综述类型（叙事综述、系统综述、范围综述、Meta 分析）
   - 划定边界（时间跨度、地域范围、研究类型）

3. **设计检索策略**：
   - 从研究问题中提炼 2-4 个核心概念
   - 为每个概念列出同义词、缩写与相关词
   - 规划布尔运算符（AND、OR、NOT）来组合检索词
   - 选择与问题相适应的互补文献数据库与注册库
   - **可选：使用 parallel-web（`parallel-cli search`）做初始范围摸底**，在正式检索数据库之前快速了解整体面貌

4. **设定纳入/排除标准**：
   - 日期范围（例如明确采用历史区间 2015-2024）
   - 语言（通常为英文，或明确指定多语种）
   - 出版类型（同行评议论文、预印本、综述）
   - 研究设计（RCT、观察性研究、体外实验等）
   - 清楚记录全部标准

### 阶段 2：系统性文献检索

1. **多数据库检索**：

   选取与本领域相适应的文献数据库与注册库。可选使用网络检索做范围摸底与补充发现；
   须将其与数据库导出结果分开记录。

   **补充性网络发现（parallel-web）：**
   - 用 `parallel-cli search` 并启用学术域名过滤，以获得更广的学术覆盖
   - 可同时考虑学术检索与通用检索；排序后的样本不保证检索的完整性
   ```bash
   mkdir -p sources
   # Illustrative ranked sample; not a complete search
   parallel-cli search "your research topic" -q "keyword1" -q "keyword2" \
     --json --max-results 10 --excerpt-max-chars-total 27000 \
     --include-domains "scholar.google.com,arxiv.org,pubmed.ncbi.nlm.nih.gov,semanticscholar.org,biorxiv.org,medrxiv.org,ncbi.nlm.nih.gov,nature.com,science.org,ieee.org,acm.org,springer.com,wiley.com,cell.com,pnas.org,nih.gov" \
     -o sources/litreview_<topic>-academic.json

   # General search for supplementary sources
   parallel-cli search "your research topic" -q "keyword1" -q "keyword2" \
     --json --max-results 10 --excerpt-max-chars-total 27000 \
     -o sources/litreview_<topic>-general.json
   ```
   - 用 `parallel-cli extract --full-content` 请求可访问论文 URL 的正文内容；注意检查截断与抓取错误
   ```bash
   parallel-cli extract "https://arxiv.org/abs/1706.03762" --full-content --json
   ```

   **生物医学与生命科学：**
   - 通过 PubMed 界面或 E-utilities 检索；PMC 的全文覆盖范围不同
   - 检索 bioRxiv/medRxiv 界面，或取回日期区间的 API 元数据并显式过滤
   - 具体请求、认证方式与导出限制见 `database_strategies.md`

   **一般科学文献：**
   - 通过直连 API 检索 arXiv（物理、数学、计算机科学、量化生物学的预印本）
   - 视情况使用 Semantic Scholar 有文档说明的相关性检索或批量 API
   - 手动使用 Google Scholar 做补充发现与引文追溯；保留检索与筛选的限制记录

   生物实体数据库可以为背景提供参考，但仅仅因为其中含有参考文献，
   并不足以使其成为文献来源。

2. **记录检索参数**：
   ```markdown
   ## Search Strategy

   ### Database: PubMed
   - **Date searched**: 2024-10-25
   - **Date range**: 2015-01-01 to 2024-10-25
   - **Search string**:
     ```
     ("CRISPR"[Title] OR "Cas9"[Title])
     AND ("Anemia, Sickle Cell"[MeSH Terms] OR "SCD"[Title/Abstract])
     AND 2015:2024[Publication Date]
     ```
   - **Results**: 247 articles
   ```

   每个检索过的数据库都要照此重复。

3. **导出并汇总结果**：
   - 从各数据库以 JSON 格式导出结果
   - 把原始的提供方响应规范化为 JSON 数组，同时把原始导出与来源信息分开保存
   - 用 `scripts/search_databases.py` 做后处理：
     ```bash
     python scripts/search_databases.py combined_results.json \
       --deduplicate \
       --format markdown \
       --output aggregated_results.md
     ```

### 阶段 3：筛选与遴选

1. **去重**：
   ```bash
   python scripts/search_databases.py results.json --deduplicate --format json --output unique_results.json
   ```
   - 保留首个规范化后的 DOI；标题回退匹配只比较没有 DOI 的记录。请复核匹配结果，并保留原始重复项用于信息补全
   - 记录被移除的重复项数量

2. **标题筛选**：
   - 对照纳入/排除标准审阅所有标题
   - 排除明显不相关的研究
   - 记录此阶段排除的数量

3. **摘要筛选**：
   - 阅读剩余研究的摘要
   - 严格应用纳入/排除标准
   - 记录排除理由

4. **全文筛选**：
   - 获取剩余研究的全文
   - 对照全部标准做详细审阅
   - 记录具体的排除理由
   - 记录最终纳入的研究数量

5. **绘制 PRISMA 流程图**：
   - 使用与新建/更新综述及来源类型相匹配的官方模板。
   - 跟踪筛选前识别并移除的记录数、已筛选并排除的记录数、
     寻求/未获取/已评估的报告数、附理由排除的报告数，以及纳入的研究
     及其报告数。
   - 逐步核对各环节的计数；不要用论文篇数臆造出一个纳入研究数。维护一份研究到报告的映射。

### 阶段 4：数据提取与质量评估

1. **从每项纳入研究中提取关键数据**：
   - 研究元数据（作者、年份、期刊、DOI）
   - 研究设计与方法
   - 样本量与人群特征
   - 关键发现与结果
   - 作者指出的局限
   - 资助来源与利益冲突

2. **评估偏倚风险与证据确定性**：
   - 选用与设计和问题相匹配的工具：随机对照试验结果用 RoB 2；非随机干预研究结果用
     ROBINS-I；医疗干预的系统综述用 AMSTAR 2。其他设计需要各自对应的评价工具。
   - 保留各领域的判断与理由。RoB 2 使用低风险、存在一些担忧、高风险三档；
     不要强行把所有工具套到同一数值尺度上。
   - GRADE 针对每个结局评估一整组证据（高/中/低/极低），而不是给每项单独研究打一个
     通用等级。参见 [Cochrane 证据确定性指南](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14)。
   - 预先规定偏倚如何影响综合；不要临时编造排除标准。

3. **按主题组织**：
   - 识别跨研究的 3-5 个主要主题
   - 按主题归类研究（同一研究可归入多个主题）
   - 记录模式、共识与争议

### 阶段 5：综合与分析

1. **从模板创建综述文档**：
   ```bash
   cp assets/review_template.md my_literature_review.md
   ```

2. **撰写主题式综合**（而非逐篇罗列摘要）：
   - 结果部分按主题或研究问题组织
   - 在每个主题内综合多项研究的发现
   - 比较并对照不同方法与结果
   - 指出共识领域与争议焦点
   - 突出最有力的证据

   虚构的结构示例（请把其中每个计数与百分比替换为实际提取到的证据）：
   ```markdown
   #### 3.3.1 Theme: CRISPR Delivery Methods

   Multiple delivery approaches have been investigated for therapeutic
   gene editing. Viral vectors (AAV) were used in 15 studies^1-15^ and
   showed high transduction efficiency (65-85%) but raised immunogenicity
   concerns^3,7,12^. In contrast, lipid nanoparticles demonstrated lower
   efficiency (40-60%) but improved safety profiles^16-23^.
   ```

3. **批判性分析**：
   - 评估各研究在方法学上的优势与局限
   - 评估证据的质量与一致性
   - 识别知识空白与方法学空白
   - 指出需要未来研究的领域

4. **撰写讨论部分**：
   - 在更广的语境中解读发现
   - 讨论临床、实践或研究层面的意义
   - 承认本综述自身的局限
   - 如适用，与既往综述作比较
   - 提出具体的未来研究方向

### 阶段 6：引文核验

**关键要求**：所有引文在最终提交前都必须核验其准确性。

1. **核验全部 DOI**：
   ```bash
   python scripts/verify_citations.py my_literature_review.md
   ```

   该脚本会：
   - 从文档中提取全部 DOI
   - 通过 Handle API 检查 DOI 的注册情况
   - 取回可获取的 Crossref 元数据，并保留未解决的错误
   - 生成核验报告
   - 不核验主张是否被支持、出版方是否可访问，也不核验最终的引用样式

2. **复核核验报告**：
   - 检查是否存在失败的 DOI
   - 核对作者姓名、标题与出版信息是否吻合
   - 修正原文档中的任何错误
   - 对照来源解决错误；不要仅仅因为某个服务超时或缺少元数据就删除一条参考文献

3. **统一引用格式**：
   - 选定一种引用样式并全文统一（见 `references/citation_styles.md`）
   - 常用样式：APA、Nature、Vancouver、Chicago、IEEE
   - 用 CSL 处理器处理完整元数据；该脚本只提供元数据预览
   - 确保正文引用与参考文献表的格式一致

### 阶段 7：文档生成

1. **生成 PDF**：
   ```bash
   python scripts/generate_pdf.py my_literature_review.md \
     --bibliography my_literature_review.bib --csl styles/apa.csl \
     --output my_review.pdf
   ```

   该示例需要自行提供现成的 `.bib` 与 `.csl` 文件；仓库内并未捆绑。
   `[@key]` 形式的引文会被排版，手工键入的参考文献则保持原样。

   可用选项：
   - `--csl` / `--citation-style`：本地 CSL 的路径或名称；省略则使用 Pandoc 默认样式
   - `--bibliography`：参考文献文件；同目录下的 `.bib` 也会被自动识别
   - `--output`：PDF 输出位置
   - `--no-toc`：关闭目录
   - `--no-numbers`：关闭章节编号
   - `--check-deps`：检查是否安装了 pandoc/xelatex

2. **复核最终输出**：
   - 检查 PDF 的排版与版面
   - 确认所有章节齐备
   - 确保引文正确渲染
   - 检查图/表显示是否正常
   - 核对目录是否准确

3. **质量检查清单**：
   - [ ] 已检查 DOI 注册情况；元数据同一性与主张支撑情况已人工复核
   - [ ] 引文格式前后一致
   - [ ] 已附 PRISMA 流程图（系统综述需要）
   - [ ] 检索方法已完整记录
   - [ ] 纳入/排除标准表述清楚
   - [ ] 结果按主题组织（非逐篇罗列）
   - [ ] 已完成质量评估
   - [ ] 已承认局限性
   - [ ] 参考文献完整准确
   - [ ] PDF 生成无报错
