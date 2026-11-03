> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/assets/citation_checklist.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 引文质量检查清单

使用本清单，确保最终提交前你的引文准确、完整且格式规范。

## 提交前检查清单

### ✓ 元数据准确性

- [ ] 所有作者姓名正确且格式规范
- [ ] 文章标题与实际发表版本一致
- [ ] 期刊/会议名称完整（除非必要，否则不缩写）
- [ ] 发表年份准确
- [ ] 卷号与期号正确
- [ ] 页码范围准确

### ✓ 必填字段

- [ ] 所有 @article 条目都有：author、title、journal、year
- [ ] 所有 @book 条目都有：author/editor、title、publisher、year
- [ ] 所有 @inproceedings 条目都有：author、title、booktitle、year
- [ ] 现代论文（2000 年以后）在可获得时包含 DOI
- [ ] 所有条目都有唯一的引文键

### ✓ DOI 验证

- [ ] 所有 DOI 格式规范（10.XXXX/...）
- [ ] DOI 能正确解析到对应文章
- [ ] BibTeX 字段中没有 DOI 前缀（没有 "doi:" 或 "https://doi.org/"）
- [ ] 来自 CrossRef 的元数据与你的 BibTeX 条目一致
- [ ] 运行：`python scripts/validate_citations.py references.bib --check-dois`

### ✓ 格式一致性

- [ ] 页码范围使用双连字符（--）而非单连字符（-）
- [ ] pages 字段中没有 "pp." 前缀
- [ ] 作者姓名使用 "and" 分隔（不用分号或 &）
- [ ] 标题中的大小写被保护（{AlphaFold}、{CRISPR} 等）
- [ ] 若包含月份，使用标准缩写
- [ ] 引文键遵循一致的格式

### ✓ 重复检测

- [ ] 参考文献中没有重复的 DOI
- [ ] 没有重复的引文键
- [ ] 没有近似重复的标题
- [ ] 预印本在有正式发表版本时已更新为正式版本
- [ ] 运行：`python scripts/validate_citations.py references.bib`

### ✓ 特殊字符

- [ ] 带变音符号的字符格式规范（例如用 {\"u} 表示 ü）
- [ ] 数学符号使用 LaTeX 命令
- [ ] 化学式格式规范
- [ ] 没有未转义的特殊字符（%、&、$、# 等）

### ✓ BibTeX 语法

- [ ] 所有条目的花括号 {} 平衡
- [ ] 字段以逗号分隔（末尾逗号是合法的）
- [ ] 条目类型合法（@article、@book 等）
- [ ] 运行：`python scripts/validate_citations.py references.bib`

### ✓ 文件组织

- [ ] 参考文献按逻辑顺序排序（按年份、作者或键）
- [ ] 全文格式一致
- [ ] 条目之间没有格式不一致之处
- [ ] 运行：`python scripts/format_bibtex.py references.bib --sort year`

## 自动化校验

### 第 1 步：格式化与清理

```bash
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --sort year \
  --descending \
  --output clean_references.bib
```

**这一步做了什么**：
- 移除重复项
- 统一格式
- 修复常见问题（页码范围、DOI 格式等）
- 按年份排序（最新在前）

### 第 2 步：校验

```bash
python scripts/validate_citations.py clean_references.bib \
  --check-dois \
  --report validation_report.json \
  --verbose
```

**这一步做了什么**：
- 检查必填字段
- 检查 DOI 注册情况；`doi_unverified` 警告需单独排查
- 检测重复项
- 校验语法
- 生成详细报告

### 第 3 步：审阅报告

```bash
cat validation_report.json
```

**需要处理**：
- **错误**：必须修复（字段缺失、DOI 失效、语法错误）
- **警告**：应当修复（推荐的字段缺失、格式问题）
- **重复项**：移除或合并

### 第 4 步：最终检查

```bash
python scripts/validate_citations.py clean_references.bib --verbose
```

**目标**：零错误、警告最少

## 人工审阅检查清单

### 关键引文（最重要的 10-20 篇）

对你最重要的引文，人工核实：

- [ ] 访问 DOI 链接，确认是对应的正确文章
- [ ] 对照实际发表版本核查作者姓名
- [ ] 核实年份与发表日期一致
- [ ] 确认期刊/会议名称正确
- [ ] 检查卷号/页码一致

### 常见问题清单

**信息缺失**：
- [ ] 2000 年以后发表的论文没有 DOI
- [ ] 期刊文章缺卷号或页码
- [ ] 图书缺出版商
- [ ] 会议论文缺会议地点

**格式错误**：
- [ ] 页码范围用了单连字符（123-145 → 123--145）
- [ ] 作者列表中用了 &（Smith & Jones → Smith and Jones）
- [ ] 标题中缩写词未加保护（DNA → {DNA}）
- [ ] DOI 带有 URL 前缀（https://doi.org/10.xxx → 10.xxx）

**元数据不匹配**：
- [ ] 作者姓名与发表版本不符
- [ ] 年份填的是 online-first 而非印刷版发表年份
- [ ] 期刊名称用了缩写而非全称
- [ ] 卷号/期号写反

**重复项**：
- [ ] 同一篇论文用了不同的引文键
- [ ] 预印本与正式发表版本同时被引用
- [ ] 会议版本与期刊版本同时被引用

## 领域专项检查

### 生物医学科学

- [ ] 可获得时包含 PubMed Central ID（PMCID）
- [ ] MeSH 词使用得当（若使用 MeSH）
- [ ] 包含临床试验注册号（若适用）
- [ ] 所有涉及治疗/药物的引用都准确无误

### 计算机科学

- [ ] 预印本包含 arXiv ID
- [ ] 会议论文集引用规范（不只是写 "NeurIPS"）
- [ ] 软件/数据集引用包含版本号
- [ ] GitHub 链接稳定且为永久链接

### 通用科学

- [ ] 数据可用性声明引用规范
- [ ] 已撤稿论文被识别并移除
- [ ] 预印本已检查是否有正式发表版本
- [ ] 关键补充材料已引用

## 最终提交前的步骤

### 提交前 1 周

- [ ] 运行带 DOI 检查的完整校验
- [ ] 修复所有错误与严重警告
- [ ] 人工核实最重要的 10-20 篇引文
- [ ] 检查是否有撤稿论文

### 提交前 3 天

- [ ] 任何人工编辑之后重新运行校验
- [ ] 确保所有正文引文都有对应的参考文献条目
- [ ] 确保所有参考文献条目都在正文中被引用
- [ ] 检查引文格式是否符合期刊要求

### 提交前 1 天

- [ ] 最终校验
- [ ] LaTeX 编译成功且没有警告
- [ ] PDF 中所有引文渲染正确
- [ ] 参考文献以正确格式呈现
- [ ] 没有占位引文（Smith et al. XXXX）

### 提交当天

- [ ] 最后再跑一次校验
- [ ] 没有未重新校验的临时改动
- [ ] 参考文献文件已包含在提交包中
- [ ] 正文提到的图表与参考文献一致

## 质量指标

### 优秀的参考文献

- ✓ 已分配 DOI 的都包含 DOI；无 DOI 的出版物已显式核实
- ✓ 零校验错误
- ✓ 零必填字段缺失
- ✓ 零失效 DOI
- ✓ 零重复项
- ✓ 全文格式一致
- ✓ 所有引文都经过人工抽查

### 可接受的参考文献

- ✓ 可获得的 DOI 元数据已对照权威记录核实
- ✓ 零高严重性错误
- ✓ 只有轻微警告（例如推荐的字段缺失）
- ✓ 关键引文经过人工核实
- ✓ 编译无错误通过

### 需要改进

- ✗ 近期论文缺 DOI
- ✗ 存在高严重性的校验错误
- ✗ DOI 失效或不正确
- ✗ 存在重复条目
- ✗ 格式不一致
- ✗ 编译有警告或错误

## 紧急修复

如果你在最后关头发现问题：

### DOI 失效

```bash
# Find correct DOI
# Option 1: Search CrossRef
# https://www.crossref.org/

# Option 2: Search on publisher website
# Option 3: Google Scholar

# Re-extract metadata
python scripts/extract_metadata.py --doi CORRECT_DOI
```

### 信息缺失

```bash
# Extract from DOI
python scripts/extract_metadata.py --doi 10.xxxx/yyyy

# Or from PMID (biomedical)
python scripts/extract_metadata.py --pmid 12345678

# Or from arXiv
python scripts/extract_metadata.py --arxiv 2103.12345
```

### 重复条目

```bash
# Auto-remove duplicates
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --output fixed_references.bib
```

### 格式错误

```bash
# Auto-fix common issues
python scripts/format_bibtex.py references.bib \
  --output fixed_references.bib

# Then validate
python scripts/validate_citations.py fixed_references.bib
```

## 长期最佳实践

### 研究阶段

- [ ] 发现一篇就往参考文献文件里加一条
- [ ] 立即用 DOI 提取元数据
- [ ] 每增加 10-20 条就校验一次
- [ ] 把参考文献文件纳入版本控制

### 写作阶段

- [ ] 边写边引用
- [ ] 使用一致的引文键
- [ ] 不要拖延添加参考文献
- [ ] 每周校验

### 提交前

- [ ] 为引文清理预留 2-3 天
- [ ] 不要等到最后一天
- [ ] 能自动化的都自动化
- [ ] 人工核实关键引文

## 工具速查

### 提取元数据

```bash
# From DOI
python scripts/doi_to_bibtex.py 10.1038/nature12345

# From multiple sources
python scripts/extract_metadata.py \
  --doi 10.1038/nature12345 \
  --pmid 12345678 \
  --arxiv 2103.12345 \
  --output references.bib
```

### 校验

```bash
# Basic validation
python scripts/validate_citations.py references.bib

# With DOI checking (slow but thorough)
python scripts/validate_citations.py references.bib --check-dois

# Generate report
python scripts/validate_citations.py references.bib \
  --report validation.json \
  --verbose
```

### 格式化与清理

```bash
# Format and fix issues
python scripts/format_bibtex.py references.bib

# Remove duplicates and sort
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --sort year \
  --descending \
  --output clean_refs.bib
```

## 摘要

**最低要求**：
1. 运行 `format_bibtex.py --deduplicate`
2. 运行 `validate_citations.py`
3. 修复所有错误
4. 编译成功

**推荐做法**：
1. 格式化、去重并排序
2. 用 `--check-dois` 校验
3. 修复所有错误与警告
4. 人工核实重点引文
5. 修复后重新校验

**最佳实践**：
1. 在研究全程中做校验
2. 持续一致地使用自动化工具
3. 保持参考文献整洁有序
4. 记录任何特殊情况
5. 提交前 1-3 天做最终校验

**记住**：引文错误会让你的学术声誉受损。花时间确保准确是值得的！
