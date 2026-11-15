> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/citation_validation.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 引文验证指南

验证 BibTeX 文件中引文准确性、完整性与格式的综合指南。

## 概述

引文验证确保：
- 所有引文准确且完整
- DOI 能正确解析
- 必填字段齐全
- 没有重复条目
- 格式与语法正确
- 链接可以访问

应在以下时机进行验证：
- 提取元数据之后
- 投稿之前
- 手动编辑 BibTeX 文件之后
- 对长期维护的文献库定期进行

## 验证类别

### 1. DOI 验证

**目的**：确保 DOI 有效且能正确解析。

#### 检查内容

**DOI 格式**：
```
Valid:   10.1038/s41586-021-03819-2
Valid:   10.1126/science.aam9317
Syntactically plausible but requires lookup: 10.1038/invalid
Invalid: doi:10.1038/... (should omit "doi:" prefix in BibTeX)
```

**DOI 解析**：
- DOI 应能通过 https://doi.org/ 解析
- 应跳转到真实文章
- 不应返回 404 或错误

**元数据一致性**：
- CrossRef 元数据应与 BibTeX 一致
- 作者姓名应能对应
- 标题应一致
- 年份应一致

#### 如何验证

**人工检查**：
1. 从 BibTeX 中复制 DOI
2. 访问 https://doi.org/10.1038/nature12345
3. 确认跳转到正确的文章
4. 核对元数据是否一致

**自动检查**（推荐）：
```bash
python scripts/validate_citations.py references.bib --check-dois
```

**流程**：
1. 从 BibTeX 文件提取所有 DOI
2. 查询 Crossref 的 `/works/{doi}`；返回 404 时再查 DataCite 的 `/dois/{doi}`
3. 若两者都没有记录，则 GET `doi.org/{doi}`，且不跟随重定向
4. 有注册记录或解析器重定向即确认已注册；解析器返回 404 才是错误
5. 超时、429/5xx 和格式异常的响应都报告为 `doi_unverified` 警告

该脚本不比对文献字段，也不测试出版商落地页。标题/作者/年份需人工核对；已注册的 DOI 仍可能对应错误的文献。是否被撤稿也需另行向出版商核实。

#### 常见问题

**失效 DOI**：
- DOI 有拼写错误
- 出版商更换了 DOI（少见）
- 被撤稿的文章通常仍保留其 DOI；发表状态需另行核实
- 解决方法：从出版商网站找到正确的 DOI

**元数据不匹配**：
- BibTeX 中是过时/不正确的信息
- 解决方法：从 CrossRef 重新提取元数据

**缺少 DOI**：
- 较老的文章可能没有 DOI
- 对 2000 年以前的文献可以接受
- 改为补充 URL 或 PMID

### 2. 必填字段

**目的**：确保所有必要信息齐全。

#### 各条目类型的必填字段

**@article**：
```bibtex
author   % REQUIRED
title    % REQUIRED
journal  % REQUIRED
year     % REQUIRED
volume   % Highly recommended
pages    % Highly recommended
doi      % Highly recommended for modern papers
```

**@book**：
```bibtex
author OR editor  % REQUIRED (at least one)
title            % REQUIRED
publisher        % REQUIRED
year             % REQUIRED
isbn             % Recommended
```

**@inproceedings**：
```bibtex
author     % REQUIRED
title      % REQUIRED
booktitle  % REQUIRED (conference/proceedings name)
year       % REQUIRED
pages      % Recommended
```

**@incollection**（书中章节）：
```bibtex
author     % REQUIRED
title      % REQUIRED (chapter title)
booktitle  % REQUIRED (book title)
publisher  % REQUIRED
year       % REQUIRED
editor     % Recommended
pages      % Recommended
```

**@phdthesis**：
```bibtex
author  % REQUIRED
title   % REQUIRED
school  % REQUIRED
year    % REQUIRED
```

**@misc**（预印本、数据集等）：
```bibtex
author  % REQUIRED
title   % REQUIRED
year    % REQUIRED
howpublished  % Recommended (bioRxiv, Zenodo, etc.)
doi OR url    % At least one required
```

#### 验证脚本

```bash
python scripts/validate_citations.py references.bib
```

**输出**：
```
Error: Entry 'Smith2024' missing required field 'journal'
Error: Entry 'Doe2023' missing required field 'year'
Warning: Entry 'Jones2022' missing recommended field 'volume'
```

### 3. 作者姓名格式

**目的**：确保作者姓名格式一致且正确。

#### 正确格式

**推荐的 BibTeX 格式**：
```bibtex
author = {Last1, First1 and Last2, First2 and Last3, First3}
```

**示例**：
```bibtex
% Correct
author = {Smith, John}
author = {Smith, John A.}
author = {Smith, John Andrew}
author = {Smith, John and Doe, Jane}
author = {Smith, John and Doe, Jane and Johnson, Mary}

% For many authors
author = {Smith, John and Doe, Jane and others}

% Incorrect
author = {John Smith}  % First Last format (not recommended)
author = {Smith, J.; Doe, J.}  % Semicolon separator (wrong)
author = {Smith J, Doe J}  % Missing commas
```

#### 特殊情况

**后缀（Jr.、III 等）**：
```bibtex
author = {King, Jr., Martin Luther}
```

**复姓（带连字符）**：
```bibtex
author = {Smith-Jones, Mary}
```

**Van、von、de 等**：
```bibtex
author = {van der Waals, Johannes}
author = {de Broglie, Louis}
```

**机构作为作者**：
```bibtex
author = {{World Health Organization}}
% Double braces treat as single author
```

#### 验证检查项

**自动验证**：
```bash
python scripts/validate_citations.py references.bib
```

**检查内容**：
- 分隔符正确（用 and，不用 &、; 等）
- 逗号位置
- 作者字段为空
- 姓名格式错误

### 4. 数据一致性

**目的**：确保所有字段的值有效且合理。

#### 年份验证

**有效年份**：
```bibtex
year = {2024}    % Current/recent
year = {1953}    % Watson & Crick DNA structure (historical)
year = {1665}    % Hooke's Micrographia (very old)
```

**无效年份**：
```bibtex
year = {24}      % Two digits (ambiguous)
year = {202}     % Typo
year = {3025}    % Implausible future year
year = {0}       % Obviously wrong
```

**检查项**：
- 四位数字
- 范围合理（1600 到当前年份+1）
- 不全是零

#### 卷号/期号验证

```bibtex
volume = {123}      % Numeric
volume = {12}       % Valid
number = {3}        % Valid
number = {S1}       % Supplement issue (valid)
```

**无效写法**：
```bibtex
volume = {Vol. 123}  % Should be just number
number = {Issue 3}   % Should be just number
```

#### 页码范围验证

**正确格式**：
```bibtex
pages = {123--145}    % En-dash (two hyphens)
pages = {e0123456}    % PLOS-style article ID
pages = {123}         % Single page
```

**错误格式**：
```bibtex
pages = {123-145}     % Single hyphen (use --)
pages = {pp. 123-145} % Remove "pp."
pages = {123–145}     % Unicode en-dash (may cause issues)
```

#### URL 验证

**检查项**：
- URL 可访问（返回 200 状态）
- 有条件时使用 HTTPS
- 没有明显拼写错误
- 永久链接（而非临时链接）

**有效写法**：
```bibtex
url = {https://www.nature.com/articles/nature12345}
url = {https://arxiv.org/abs/2103.14030}
```

**存疑写法**：
```bibtex
url = {http://...}  % HTTP instead of HTTPS
url = {file:///...} % Local file path
url = {bit.ly/...}  % URL shortener (not permanent)
```

### 5. 重复检测

**目的**：找出并移除重复条目。

#### 重复条目的类型

**完全重复**（相同 DOI）：
```bibtex
@article{Smith2024a,
  doi = {10.1038/nature12345},
  ...
}

@article{Smith2024b,
  doi = {10.1038/nature12345},  % Same DOI!
  ...
}
```

**近似重复**（标题/作者相似）：
```bibtex
@article{Smith2024,
  title = {Machine Learning for Drug Discovery},
  ...
}

@article{Smith2024method,
  title = {Machine learning for drug discovery},  % Same, different case
  ...
}
```

**预印本 + 已发表版本**：
```bibtex
@misc{Smith2023arxiv,
  title = {AlphaFold Results},
  howpublished = {arXiv},
  ...
}

@article{Smith2024,
  title = {AlphaFold Results},  % Same paper, now published
  journal = {Nature},
  ...
}
% Keep published version only
```

#### 检测方法

**按 DOI**（最可靠）：
- DOI 相同 = 完全重复
- 保留一个，删除另一个

**按标题相似度**：
- 归一化：转小写、去标点
- 计算相似度（如 Levenshtein 距离）
- 相似度超过 90% 即标记

**按作者-年份-标题**：
- 第一作者相同 + 年份相同 + 标题相似
- 很可能是重复

**自动检测**：
```bash
python scripts/validate_citations.py references.bib
```

**输出**：
```
Warning: Possible duplicate entries:
  - Smith2024a (DOI: 10.1038/nature12345)
  - Smith2024b (DOI: 10.1038/nature12345)
  Recommendation: Keep one entry, remove the other.
```

### 6. 格式与语法

**目的**：确保 BibTeX 语法有效。

#### 常见语法错误

**缺少逗号**：
```bibtex
@article{Smith2024,
  author = {Smith, John}   % Missing comma!
  title = {Title}
}
% Should be:
  author = {Smith, John},  % Comma after each field
```

**花括号不配对**：
```bibtex
title = {Title with {Protected} Text  % Missing closing brace
% Should be:
title = {Title with {Protected} Text}
```

**条目缺少右花括号**：
```bibtex
@article{Smith2024,
  author = {Smith, John},
  title = {Title}
  % Missing closing brace!
% Should end with:
}
```

**引用键含非法字符**：
```bibtex
@article{Smith&Doe2024,  % & not allowed in key
  ...
}
% Use:
@article{SmithDoe2024,
  ...
}
```

#### BibTeX 语法规则

**条目结构**：
```bibtex
@TYPE{citationkey,
  field1 = {value1},
  field2 = {value2},
  ...
  fieldN = {valueN}
}
```

**引用键**：
- 字母数字和部分标点（-、_、.、:）
- 不含空格
- 区分大小写
- 文件内唯一

**字段值**：
- 用 {花括号} 或 "引号" 包裹
- 复杂文本建议用花括号
- 数字可以不加引号：`year = 2024`

**特殊字符**：
- `{` 和 `}` 用于分组
- `\` 用于 LaTeX 命令
- 保护大小写：`{AlphaFold}`
- 重音符号：`{\"u}`、`{\'e}`、`{\aa}`

#### 验证

```bash
python scripts/validate_citations.py references.bib
```

随附的解析器只检查它能解析的条目和重复键；它不是完整的 BibTeX 语法校验器。格式损坏的条目可能被跳过，`@string` 宏也不会展开。投稿前请对比输入/输出条目数，并用真正的 BibTeX/Biber 工具链编译参考文献表。

## 验证工作流

### Step 1: 基础验证

运行综合验证：

```bash
python scripts/validate_citations.py references.bib
```

**检查项**：
- 仅在传入 `--check-dois` 时才检查 DOI 注册
- 必填字段
- 作者格式
- 数据一致性
- 重复条目
- 语法

### Step 2: 查看报告

查看验证报告：

```json
{
  "total_entries": 150,
  "valid_entries": 140,
  "errors": [
    {
      "entry": "Smith2024",
      "error": "missing_required_field",
      "field": "journal",
      "severity": "high"
    },
    {
      "entry": "Doe2023",
      "error": "invalid_doi",
      "doi": "10.1038/broken",
      "severity": "high"
    }
  ],
  "warnings": [
    {
      "entry": "Jones2022",
      "warning": "missing_recommended_field",
      "field": "volume",
      "severity": "medium"
    }
  ],
  "duplicates": [
    {
      "entries": ["Smith2024a", "Smith2024b"],
      "reason": "same_doi",
      "doi": "10.1038/nature12345"
    }
  ]
}
```

### Step 3: 修复问题

**高优先级**（错误）：
1. 补齐缺失的必填字段
2. 修复失效 DOI
3. 移除重复条目
4. 改正语法错误

**中优先级**（警告）：
1. 补充推荐字段
2. 改进作者格式
3. 修正页码范围

**低优先级**：
1. 统一格式
2. 补充 URL 方便访问

### Step 4: 应用安全修正

`validate_citations.py` 只负责报告；真正改写文件的是 `format_bibtex.py`。把结果写到新文件，这样一次糟糕的运行不会毁掉原文件：

```bash
python scripts/format_bibtex.py references.bib \
  --output fixed_references.bib
```

**它可以**：
- 修正页码范围格式（- 改为 --），并展开缩写范围（1123-30）
- 去掉 pages 里的 "pp."
- 统一作者分隔符
- 去掉 DOI 中的 URL 前缀
- 规范字段顺序
- 把引用键重写为同一套方案（`--rekey`）
- 按 DOI 或键删除重复条目（`--deduplicate`）

**它不能**：
- 补充缺失的信息
- 找出正确的 DOI
- 判断该保留哪个重复条目（它保留第一个）
- 修复语义错误

### Step 5: 人工复查

复查自动修正后的文件：
```bash
# Check what changed
diff references.bib fixed_references.bib

# Review specific entries that had errors
grep -A 10 "Smith2024" fixed_references.bib
```

### Step 6: 重新验证

修复后再验证：

```bash
python scripts/validate_citations.py fixed_references.bib --verbose
```

查看 JSON 报告中的 `errors`、`warnings` 和 `duplicates`。高严重度错误为零不代表每个 DOI 都已验证：请检查 `doi_unverified` 警告，并单独编译参考文献表。

## 验证清单

最终提交前使用这份清单：

### DOI 验证
- [ ] 所有 DOI 都能正确解析
- [ ] BibTeX 与 CrossRef 元数据一致
- [ ] 没有失效或无效的 DOI

### 完整性
- [ ] 所有条目都有必填字段
- [ ] 已分配 DOI 的条目都包含 DOI；缺 DOI 必须经过核实，不能按年份推断
- [ ] 作者格式正确
- [ ] 期刊/会议名称正确

### 一致性
- [ ] 年份是四位数字
- [ ] 页码范围用 -- 而非 -
- [ ] 卷号/期号是数字
- [ ] URL 可访问

### 重复条目
- [ ] 没有相同 DOI 的条目
- [ ] 没有近似重复的标题
- [ ] 预印本已更新为正式发表版本

### 格式
- [ ] BibTeX 语法有效
- [ ] 花括号配对
- [ ] 逗号正确
- [ ] 引用键唯一

### 最终检查
- [ ] 参考文献表编译无错误
- [ ] 正文中的引用都出现在参考文献表里
- [ ] 参考文献表条目都在正文中被引用
- [ ] 引用格式符合期刊要求

## 最佳实践

### 1. 尽早并经常验证

```bash
# After extraction
python scripts/extract_metadata.py --doi ... --output refs.bib
python scripts/validate_citations.py refs.bib

# After manual edits
python scripts/validate_citations.py refs.bib

# Before submission
python scripts/validate_citations.py refs.bib --check-dois
```

### 2. 使用自动化工具

不要手动验证，改用脚本：
- 更快
- 更全面
- 能发现人容易漏掉的错误
- 生成报告

### 3. 写入新文件，替换前先 diff

`format_bibtex.py` 只写你指定的地方：既没有 `--output` 也没有 `--in-place` 时，它输出到 stdout，输入文件保持不动。

```bash
# Reformat into a separate file
python scripts/format_bibtex.py references.bib \
  --output references_fixed.bib

# Review changes
diff references.bib references_fixed.bib

# If satisfied, replace
mv references_fixed.bib references.bib
```

### 4. 先修高优先级问题

**优先级顺序**：
1. 语法错误（会导致编译失败）
2. 缺失必填字段（引文不完整）
3. 失效 DOI（链接打不开）
4. 重复条目（造成混淆、浪费篇幅）
5. 缺失推荐字段
6. 格式不一致

### 5. 记录例外情况

对无法修复的条目：

```bibtex
@article{Old1950,
  author = {Smith, John},
  title = {Title},
  journal = {Obscure Journal},
  year = {1950},
  volume = {12},
  pages = {34--56},
  note = {No DOI found in the checked publisher record}
}
```

### 6. 对照期刊要求验证

不同期刊有不同的要求：
- 引用格式（数字编号、作者-年份）
- 缩写（期刊名缩写）
- 参考文献条数上限
- 交稿格式（BibTeX、EndNote、手工排版）

务必查阅期刊作者指南！

## 常见验证问题

### 问题 1：元数据不匹配

**问题**：BibTeX 写的是 2023，CrossRef 显示 2024。

**原因**：
- 在线优先发表与正式出版不一致
- 勘误/更新
- 提取出错

**解决方法**：
1. 核对文章实际信息
2. 采用更新、更准确的日期
3. 更新 BibTeX 条目
4. 重新验证

### 问题 2：特殊字符

**问题**：LaTeX 编译在特殊字符处失败。

**原因**：
- 重音字符（é、ü、ñ）
- 化学式（H₂O）
- 数学符号（α、β、±）

**解决方法**：
```bibtex
% Use LaTeX commands
author = {M{\"u}ller, Hans}  % Müller
title = {Study of H\textsubscript{2}O}  % H₂O
% Or use UTF-8 with proper LaTeX packages
```

### 问题 3：提取不完整（必须联网搜索）

**问题**：提取出的元数据缺少字段（卷号、页码、DOI、期号）。

**原因**：
- 源 API 没有提供全部元数据
- 提取出错
- 数据库记录不完整
- 在线优先发表，还没有最终页码

**解决方法：必须联网搜索补全缺口**：

1. **确定缺失字段**：扫描 BibTeX 条目，找出为空或缺失的 `volume`、`pages`、`number`、`doi` 字段。

2. **用联网搜索查找缺失的元数据**（parallel-web skill）：
   ```bash
   # Search by author + title to find complete citation info
   parallel-cli search "AUTHOR_NAME PAPER_TITLE JOURNAL volume pages DOI" \
     --json --max-results 10 \
     -o sources/search_citation_CITATIONKEY.json
   ```

3. **DOI 已知时，从 DOI 解析页面提取**：
   ```bash
   parallel-cli extract "https://doi.org/DOI_HERE" --json \
     --objective "extract volume, issue number, page range, publication date" \
     -o sources/extract_doi_CITATIONKEY.json
   ```

4. **DOI 未知时，先搜索 DOI**：
   ```bash
   parallel-cli search "AUTHOR_NAME PAPER_TITLE JOURNAL_NAME DOI" \
     --json --max-results 10 \
     -o sources/search_find_doi_CITATIONKEY.json
   ```

5. **尝试其他元数据来源**：
   - CrossRef API（经 DOI）：卷号/页码最可靠
   - PubMed（经 PMID）：适合生物医学论文
   - Google Scholar：难找论文的兜底
   - 出版商网站：最后的手段

6. **用查到的元数据更新 BibTeX 条目**，并记录日志：
   ```
   [HH:MM:SS] METADATA ENRICHED: [CitationKey] - added volume, pages, doi ✅
   ```

7. **确实找不到时**（少见），添加 note 字段：
   ```bibtex
   note = {Complete pagination not yet assigned — online-first publication}
   ```

对照出版商记录核实适用的字段。在线优先发表的卷号/页码、无 DOI 的文章、以文章编号代替页码的期刊都是有效情形；记录字段缺失的原因，使用符合引用格式的定位符，不得编造元数据。

### 问题 4：重复条目查不出来

**问题**：同一篇论文出现两次，但没被检出。

**原因**：
- DOI 不同（应该少见）
- 标题不同（缩写、拼写差异）
- 引用键不同

**解决方法**：
- 手动按作者 + 年份搜索
- 检查相似的标题
- 手动移除

## 小结

验证确保引文质量：

✓ **准确**：DOI 可解析，元数据正确  
✓ **完整**：必填字段齐全  
✓ **一致**：全文格式统一  
✓ **无重复**：每篇论文只引一次  
✓ **语法有效**：BibTeX 编译无错误  

**最终提交前务必验证**！

使用自动化工具：
```bash
python scripts/validate_citations.py references.bib
```

遵循工作流：
1. 提取元数据
2. 验证
3. 修复错误
4. 重新验证
5. 提交
