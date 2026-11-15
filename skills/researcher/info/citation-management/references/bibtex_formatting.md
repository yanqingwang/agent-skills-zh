> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/bibtex_formatting.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# BibTeX 格式指南

BibTeX 条目类型、必填字段、格式约定与最佳实践的全面指南。

## 概述

BibTeX 是 LaTeX 文档的标准参考文献格式。正确的格式能保证：
- 引文渲染正确
- 格式一致
- 与引文样式兼容
- 不出现编译错误

本指南覆盖所有常见条目类型和格式规则。

## 条目类型

### @article - 期刊论文

**最常用的条目类型**，用于同行评审的期刊论文。

**必填字段**：
- `author`: 作者姓名
- `title`: 论文标题
- `journal`: 期刊名称
- `year`: 出版年份

**可选字段**：
- `volume`: 卷号
- `number`: 期号
- `pages`: 页码范围
- `month`: 出版月份
- `doi`: 数字对象标识符（DOI）
- `url`: URL
- `note`: 附加说明

**模板**：
```bibtex
@article{CitationKey2024,
  author  = {Last1, First1 and Last2, First2},
  title   = {Article Title Here},
  journal = {Journal Name},
  year    = {2024},
  volume  = {10},
  number  = {3},
  pages   = {123--145},
  doi     = {10.1234/journal.2024.123456},
  month   = jan
}
```

**示例**：
```bibtex
@article{Jumper2021,
  author  = {Jumper, John and Evans, Richard and Pritzel, Alexander and others},
  title   = {Highly Accurate Protein Structure Prediction with {AlphaFold}},
  journal = {Nature},
  year    = {2021},
  volume  = {596},
  number  = {7873},
  pages   = {583--589},
  doi     = {10.1038/s41586-021-03819-2}
}
```

### @book - 书籍

**用于整本书**。

**必填字段**：
- `author` 或 `editor`: 作者或编者
- `title`: 书名
- `publisher`: 出版社名称
- `year`: 出版年份

**可选字段**：
- `volume`: 卷号（多卷本时）
- `series`: 丛书名称
- `address`: 出版地
- `edition`: 版次
- `isbn`: ISBN
- `url`: URL

**模板**：
```bibtex
@book{CitationKey2024,
  author    = {Last, First},
  title     = {Book Title},
  publisher = {Publisher Name},
  year      = {2024},
  edition   = {3},
  address   = {City, Country},
  isbn      = {978-0-123-45678-9}
}
```

**示例**：
```bibtex
@book{Kumar2021,
  author    = {Kumar, Vinay and Abbas, Abul K. and Aster, Jon C.},
  title     = {Robbins and Cotran Pathologic Basis of Disease},
  publisher = {Elsevier},
  year      = {2021},
  edition   = {10},
  address   = {Philadelphia, PA},
  isbn      = {978-0-323-53113-9}
}
```

### @inproceedings - 会议论文

**用于会议论文集中的论文**。

**必填字段**：
- `author`: 作者姓名
- `title`: 论文标题
- `booktitle`: 会议/论文集名称
- `year`: 年份

**可选字段**：
- `editor`: 论文集编者
- `volume`: 卷号
- `series`: 丛书名称
- `pages`: 页码范围
- `address`: 会议地点
- `month`: 会议月份
- `organization`: 主办机构
- `publisher`: 出版商
- `doi`: DOI

**模板**：
```bibtex
@inproceedings{CitationKey2024,
  author    = {Last, First},
  title     = {Paper Title},
  booktitle = {Proceedings of Conference Name},
  year      = {2024},
  pages     = {123--145},
  address   = {City, Country},
  month     = jun
}
```

**示例**：
```bibtex
@inproceedings{Vaswani2017,
  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and others},
  title     = {Attention is All You Need},
  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS 2017)},
  year      = {2017},
  pages     = {5998--6008},
  address   = {Long Beach, CA}
}
```

**注意**：`@conference` 是 `@inproceedings` 的别名。

### @incollection - 书籍章节

**用于编辑出版的图书中的章节**。

**必填字段**：
- `author`: 章节作者
- `title`: 章节标题
- `booktitle`: 书名
- `publisher`: 出版社名称
- `year`: 出版年份

**可选字段**：
- `editor`: 书籍编者
- `volume`: 卷号
- `series`: 丛书名称
- `type`: 章节类型（如 "chapter"）
- `chapter`: 章节编号
- `pages`: 页码范围
- `address`: 出版地
- `edition`: 版次
- `month`: 月份

**模板**：
```bibtex
@incollection{CitationKey2024,
  author    = {Last, First},
  title     = {Chapter Title},
  booktitle = {Book Title},
  editor    = {Editor, Last and Editor2, Last},
  publisher = {Publisher Name},
  year      = {2024},
  pages     = {123--145},
  chapter   = {5}
}
```

**示例**：
```bibtex
@incollection{Brown2020,
  author    = {Brown, Peter O. and Botstein, David},
  title     = {Exploring the New World of the Genome with {DNA} Microarrays},
  booktitle = {DNA Microarrays: A Molecular Cloning Manual},
  editor    = {Eisen, Michael B. and Brown, Patrick O.},
  publisher = {Cold Spring Harbor Laboratory Press},
  year      = {2020},
  pages     = {1--45},
  address   = {Cold Spring Harbor, NY}
}
```

### @phdthesis - 博士学位论文

**用于博士学位论文**。

**必填字段**：
- `author`: 作者姓名
- `title`: 论文标题
- `school`: 授予机构
- `year`: 年份

**可选字段**：
- `type`: 类型（如 "PhD dissertation"、"PhD thesis"）
- `address`: 机构所在地
- `month`: 月份
- `url`: URL
- `note`: 附加说明

**模板**：
```bibtex
@phdthesis{CitationKey2024,
  author = {Last, First},
  title  = {Dissertation Title},
  school = {University Name},
  year   = {2024},
  type   = {{PhD} dissertation},
  address = {City, State}
}
```

**示例**：
```bibtex
@phdthesis{Johnson2023,
  author  = {Johnson, Mary L.},
  title   = {Novel Approaches to Cancer Immunotherapy Using {CRISPR} Technology},
  school  = {Stanford University},
  year    = {2023},
  type    = {{PhD} dissertation},
  address = {Stanford, CA}
}
```

**注意**：`@mastersthesis` 与之类似，用于硕士学位论文。

### @mastersthesis - 硕士学位论文

**用于硕士学位论文**。

**必填字段**：
- `author`: 作者姓名
- `title`: 论文标题
- `school`: 授予机构
- `year`: 年份

**模板**：
```bibtex
@mastersthesis{CitationKey2024,
  author = {Last, First},
  title  = {Thesis Title},
  school = {University Name},
  year   = {2024}
}
```

### @misc - 其他类型

**用于不适合其他类别的条目**（预印本、数据集、软件、网站等）。

**必填字段**：
- `author`（如已知）
- `title`
- `year`

**可选字段**：
- `howpublished`: 仓库、网站、发布形式
- `url`: URL
- `doi`: DOI
- `note`: 附加信息
- `month`: 月份

**预印本模板**：
```bibtex
@misc{CitationKey2024,
  author       = {Last, First},
  title        = {Preprint Title},
  year         = {2024},
  howpublished = {bioRxiv},
  doi          = {10.1101/2024.01.01.123456},
  note         = {Preprint}
}
```

**数据集模板**：
```bibtex
@misc{DatasetName2024,
  author       = {Last, First},
  title        = {Dataset Title},
  year         = {2024},
  howpublished = {Zenodo},
  doi          = {10.5281/zenodo.123456},
  note         = {Version 1.2}
}
```

**软件模板**：
```bibtex
@misc{SoftwareName2024,
  author       = {Last, First},
  title        = {Software Name},
  year         = {2024},
  howpublished = {GitHub},
  url          = {https://github.com/user/repo},
  note         = {Version 2.0}
}
```

### @techreport - 技术报告

**用于技术报告**。

**必填字段**：
- `author`: 作者姓名
- `title`: 报告标题
- `institution`: 出报告的机构
- `year`: 年份

**可选字段**：
- `type`: 报告类型
- `number`: 报告编号
- `address`: 机构所在地
- `month`: 月份

**模板**：
```bibtex
@techreport{CitationKey2024,
  author      = {Last, First},
  title       = {Report Title},
  institution = {Institution Name},
  year        = {2024},
  type        = {Technical Report},
  number      = {TR-2024-01}
}
```

### @unpublished - 未出版作品

**用于未出版作品**（不是预印本；预印本请用 @misc）。

**必填字段**：
- `author`: 作者姓名
- `title`: 作品标题
- `note`: 说明

**可选字段**：
- `month`: 月份
- `year`: 年份

**模板**：
```bibtex
@unpublished{CitationKey2024,
  author = {Last, First},
  title  = {Work Title},
  note   = {Unpublished manuscript},
  year   = {2024}
}
```

### @online/@electronic - 在线资源

**用于网页和仅在线发布的内容**。

**注意**：这不是标准 BibTeX，但许多参考文献宏包（biblatex）支持。

**必填字段**：
- `author` 或 `organization`
- `title`
- `url`
- `year`

**模板**：
```bibtex
@online{CitationKey2024,
  author = {{Organization Name}},
  title  = {Page Title},
  url    = {https://example.com/page},
  year   = {2024},
  note   = {Accessed: 2024-01-15}
}
```

## 格式规则

### 引用键（Citation Keys）

**约定**：`FirstAuthorYEARkeyword`

**示例**：
```bibtex
Smith2024protein
Doe2023machine
JohnsonWilliams2024cancer  % Multiple authors, no space
NatureEditorial2024        % No author, use publication
WHO2024guidelines          % Organization author
```

**规则**：
- 字母数字，外加 `-`、`_`、`.`、`:`
- 不含空格
- 区分大小写
- 文件内唯一
- 有描述性

**避免**：
- 特殊字符：`@`、`#`、`&`、`%`、`$`
- 空格：改用 CamelCase 或下划线
- 以数字开头：`2024Smith`（部分系统不允许）

### 作者姓名

**推荐格式**：`Last, First Middle`

**单个作者**：
```bibtex
author = {Smith, John}
author = {Smith, John A.}
author = {Smith, John Andrew}
```

**多个作者**：用 `and` 分隔：
```bibtex
author = {Smith, John and Doe, Jane}
author = {Smith, John A. and Doe, Jane M. and Johnson, Mary L.}
```

**作者较多时**（10 人及以上）：
```bibtex
author = {Smith, John and Doe, Jane and Johnson, Mary and others}
```

**特殊情形**：
```bibtex
% Suffix (Jr., III, etc.)
author = {King, Jr., Martin Luther}

% Organization as author
author = {{World Health Organization}}
% Note: Double braces keep as single entity

% Multiple surnames
author = {Garc{\'i}a-Mart{\'i}nez, Jos{\'e}}

% Particles (van, von, de, etc.)
author = {van der Waals, Johannes}
author = {de Broglie, Louis}
```

**错误格式**（不要使用）：
```bibtex
author = {Smith, J.; Doe, J.}  % Semicolons (wrong)
author = {Smith, J., Doe, J.}  % Commas (wrong)
author = {Smith, J. & Doe, J.} % Ampersand (wrong)
author = {Smith J}             % No comma
```

### 标题大小写

**用花括号保护大小写**：

```bibtex
% Proper nouns, acronyms, formulas
title = {{AlphaFold}: Protein Structure Prediction}
title = {Machine Learning for {DNA} Sequencing}
title = {The {Ising} Model in Statistical Physics}
title = {{CRISPR-Cas9} Gene Editing Technology}
```

**原因**：引文样式可能改变大小写，花括号可以保护。

**示例**：
```bibtex
% Good
title = {Advances in {COVID-19} Treatment}
title = {Using {Python} for Data Analysis}
title = {The {AlphaFold} Protein Structure Database}

% Will be lowercase in title case styles
title = {Advances in COVID-19 Treatment}  % covid-19
title = {Using Python for Data Analysis}  % python
```

**整题保护**（很少需要）：
```bibtex
title = {{This Entire Title Keeps Its Capitalization}}
```

### 页码范围

**使用连接号 en-dash**（双连字符 `--`）：

```bibtex
pages = {123--145}     % Correct
pages = {1234--1256}   % Correct
pages = {e0123456}     % Article ID (PLOS, etc.)
pages = {123}          % Single page
```

**错误**：
```bibtex
pages = {123-145}      % Single hyphen (don't use)
pages = {pp. 123-145}  % "pp." not needed
pages = {123–145}      % Unicode en-dash (may cause issues)
```

### 月份名称

**使用三字母缩写**（不加引号）：

```bibtex
month = jan
month = feb
month = mar
month = apr
month = may
month = jun
month = jul
month = aug
month = sep
month = oct
month = nov
month = dec
```

**或用数字**：
```bibtex
month = {1}   % January
month = {12}  % December
```

**或用花括号括起的全称**：
```bibtex
month = {January}
```

**标准缩写不加引号即可使用**，因为它们已在 BibTeX 中定义。

### 期刊名称

**使用全称**（不用缩写）：

```bibtex
journal = {Nature}
journal = {Science}
journal = {Cell}
journal = {Proceedings of the National Academy of Sciences}
journal = {Journal of the American Chemical Society}
```

**参考文献样式**会在需要时处理缩写。

**避免手动缩写**：
```bibtex
% Don't do this in BibTeX file
journal = {Proc. Natl. Acad. Sci. U.S.A.}

% Do this instead
journal = {Proceedings of the National Academy of Sciences}
```

**例外**：如果样式要求缩写，则使用完整缩写形式：
```bibtex
journal = {Proc. Natl. Acad. Sci. U.S.A.}  % If required by style
```

### DOI 格式

`doi` 字段中**只放裸标识符**：

```bibtex
doi = {10.1038/s41586-021-03819-2}
```

**不要这样**：
```bibtex
doi = {https://doi.org/10.1038/s41586-021-03819-2}  % Don't include URL
doi = {doi:10.1038/s41586-021-03819-2}              % Don't include prefix
```

**LaTeX** 会自动把它格式化为 URL。

**注意**：DOI 字段值后面不要加句号！

### URL 格式

```bibtex
url = {https://www.example.com/article}
```

**适用场景**：
- 没有 DOI 时
- 用于网页
- 用于补充材料

**不要重复**：
```bibtex
% Don't include both if DOI URL is same as url
doi = {10.1038/nature12345}
url = {https://doi.org/10.1038/nature12345}  % Redundant!
```

### 特殊字符

**重音与变音符**：
```bibtex
author = {M{\"u}ller, Hans}        % ü
author = {Garc{\'i}a, Jos{\'e}}    % í, é
author = {Erd{\H{o}}s, Paul}       % ő
author = {Schr{\"o}dinger, Erwin}  % ö
```

**或直接使用 UTF-8**（需正确配置 LaTeX）：
```bibtex
author = {Müller, Hans}
author = {García, José}
```

**数学符号**：
```bibtex
title = {The $\alpha$-helix Structure}
title = {$\beta$-sheet Prediction}
```

**化学式**：
```bibtex
title = {H$_2$O Molecular Dynamics}
% Or with chemformula package:
title = {\ce{H2O} Molecular Dynamics}
```

### 字段顺序

**推荐顺序**（便于阅读）：

```bibtex
@article{Key,
  author  = {},
  title   = {},
  journal = {},
  year    = {},
  volume  = {},
  number  = {},
  pages   = {},
  doi     = {},
  url     = {},
  note    = {}
}
```

**规则**：
- 重要字段在前
- 各条目保持一致
- 用格式化工具统一

## 最佳实践

### 1. 格式一致

全文使用同一格式：
- 作者姓名格式
- 标题大小写
- 期刊名称
- 引用键风格

### 2. 必填字段

始终包含：
- 条目类型的全部必填字段
- 已分配的 DOI，无论出版年份
- 已分配的卷、页码或文章编号
- 书籍的出版商

### 3. 保护大小写

对以下内容用花括号：
- 专有名词：`{AlphaFold}`
- 缩写词：`{DNA}`、`{CRISPR}`
- 公式：`{H2O}`
- 名称：`{Python}`、`{R}`

### 4. 完整作者列表

尽量收录全部作者：
- 保留核实过的完整作者列表
- 需要截断显示时交给参考文献样式处理
- 不要手动缩写成 "et al."

### 5. 使用标准条目类型

选择正确的条目类型：
- 期刊论文 → `@article`
- 书籍 → `@book`
- 会议论文 → `@inproceedings`
- 预印本 → `@misc`

### 6. 校验语法

检查：
- 花括号配对
- 字段后有逗号
- 引用键唯一
- 条目类型有效

### 7. 使用格式化工具

使用自动化工具：
```bash
python scripts/format_bibtex.py references.bib
```

好处：
- 格式一致
- 捕获语法错误
- 统一字段顺序
- 修复常见问题

## 常见错误

### 1. 作者分隔符错误

**错误**：
```bibtex
author = {Smith, J.; Doe, J.}    % Semicolon
author = {Smith, J., Doe, J.}    % Comma
author = {Smith, J. & Doe, J.}   % Ampersand
```

**正确**：
```bibtex
author = {Smith, John and Doe, Jane}
```

### 2. 缺少逗号

**错误**：
```bibtex
@article{Smith2024,
  author = {Smith, John}    % Missing comma!
  title = {Title}
}
```

**正确**：
```bibtex
@article{Smith2024,
  author = {Smith, John},   % Comma after each field
  title = {Title}
}
```

### 3. 大小写未保护

**错误**：
```bibtex
title = {Machine Learning with Python}
% "Python" will become "python" in title case
```

**正确**：
```bibtex
title = {Machine Learning with {Python}}
```

### 4. 页码用单连字符

**错误**：
```bibtex
pages = {123-145}   % Single hyphen
```

**正确**：
```bibtex
pages = {123--145}  % Double hyphen (en-dash)
```

### 5. 页码中多余的 "pp."

**错误**：
```bibtex
pages = {pp. 123--145}
```

**正确**：
```bibtex
pages = {123--145}
```

### 6. DOI 带 URL 前缀

**错误**：
```bibtex
doi = {https://doi.org/10.1038/nature12345}
doi = {doi:10.1038/nature12345}
```

**正确**：
```bibtex
doi = {10.1038/nature12345}
```

## 完整参考文献示例

```bibtex
% Journal article
@article{Jumper2021,
  author  = {Jumper, John and Evans, Richard and Pritzel, Alexander and others},
  title   = {Highly Accurate Protein Structure Prediction with {AlphaFold}},
  journal = {Nature},
  year    = {2021},
  volume  = {596},
  number  = {7873},
  pages   = {583--589},
  doi     = {10.1038/s41586-021-03819-2}
}

% Book
@book{Kumar2021,
  author    = {Kumar, Vinay and Abbas, Abul K. and Aster, Jon C.},
  title     = {Robbins and Cotran Pathologic Basis of Disease},
  publisher = {Elsevier},
  year      = {2021},
  edition   = {10},
  address   = {Philadelphia, PA},
  isbn      = {978-0-323-53113-9}
}

% Conference paper
@inproceedings{Vaswani2017,
  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and others},
  title     = {Attention is All You Need},
  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS 2017)},
  year      = {2017},
  pages     = {5998--6008}
}

% Book chapter
@incollection{Brown2020,
  author    = {Brown, Peter O. and Botstein, David},
  title     = {Exploring the New World of the Genome with {DNA} Microarrays},
  booktitle = {DNA Microarrays: A Molecular Cloning Manual},
  editor    = {Eisen, Michael B. and Brown, Patrick O.},
  publisher = {Cold Spring Harbor Laboratory Press},
  year      = {2020},
  pages     = {1--45}
}

% PhD thesis
@phdthesis{Johnson2023,
  author  = {Johnson, Mary L.},
  title   = {Novel Approaches to Cancer Immunotherapy},
  school  = {Stanford University},
  year    = {2023},
  type    = {{PhD} dissertation}
}

% Preprint
@misc{Zhang2024,
  author       = {Zhang, Yi and Chen, Li and Wang, Hui},
  title        = {Novel Therapeutic Targets in {Alzheimer}'s Disease},
  year         = {2024},
  howpublished = {bioRxiv},
  doi          = {10.1101/2024.01.001},
  note         = {Preprint}
}

% Dataset
@misc{AlphaFoldDB2021,
  author       = {{DeepMind} and {EMBL-EBI}},
  title        = {{AlphaFold} Protein Structure Database},
  year         = {2021},
  howpublished = {Database},
  url          = {https://alphafold.ebi.ac.uk/},
  doi          = {10.1093/nar/gkab1061}
}
```

## 总结

BibTeX 格式要点：

✓ **选择正确的条目类型**（@article、@book 等）  
✓ **包含全部必填字段**  
✓ **多作者用 `and` 分隔**  
✓ **用花括号保护大小写**  
✓ **页码范围用 `--`**  
✓ **现代论文包含 DOI**  
✓ **编译前校验语法**  

用格式化工具保证一致性：
```bash
python scripts/format_bibtex.py references.bib
```

格式规范的 BibTeX 能保证所有参考文献样式下引文正确且一致！
