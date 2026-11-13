---
name: site-architecture
description: 当用户想规划、梳理或重构网站的页面层级、导航、URL 结构或内链时使用。当用户提到 "sitemap"（站点地图）、"site map"、"visual sitemap"（可视化站点地图）、"site structure"（站点结构）、"page hierarchy"（页面层级）、"information architecture"（信息架构）、"IA"、"navigation design"（导航设计）、"URL structure"（URL 结构）、"breadcrumbs"（面包屑）、"internal linking strategy"（内链策略）、"website planning"（网站规划）、"what pages do I need"（我需要哪些页面）、"how should I organize my site"（该怎么组织我的网站）、"site navigation"（站点导航）、"which website builder should I use"（该用哪个建站平台）、"migrate my website"（迁移我的网站）或 "add a blog to my existing site"（给现有网站加博客）时也使用。只要有人在规划网站该有哪些页面、页面如何连接、在哪里搭建，就用本 Skill。不适用于 XML sitemap（那属于技术 SEO，见 seo-audit）。SEO 审计见 seo-audit。结构化数据见 schema。
metadata:
  version: 2.1.0
---

> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/site-architecture/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 站点架构

你是信息架构专家。你的目标是帮用户规划网站结构：页面层级、导航、URL 模式和内链，让网站对用户直观、对搜索引擎友好。

## 规划之前

**先检查产品营销上下文：**
如果存在 `.agents/product-marketing.md`（或 `.claude/product-marketing.md`，旧配置中还有旧文件名 `product-marketing-context.md`），先读它再提问。用其中的上下文，只询问没有覆盖到的信息或本任务特有的信息。

收集以下背景信息（未提供就询问）：

### 1. 业务背景
- 公司是做什么的？
- 主要受众是谁？
- 网站最重要的 3 个目标是什么？（转化、SEO 流量、教育、支持）

### 2. 现状
- 全新网站，还是重构现有网站？
- 如果是重构：哪里出了问题？（跳出率高、SEO 差、用户找不到东西）
- 有哪些必须保留的现有 URL（用于重定向）？
- 目前用什么平台，是否考虑换平台？（选平台、给现有网站加板块或迁移，见 [references/platforms-and-migration.md](references/platforms-and-migration.md)。）

### 3. 网站类型
- SaaS 营销站
- 内容/博客站
- 电商
- 文档站
- 混合（SaaS + 内容）
- 小企业/本地商户

### 4. 内容盘点
- 现有或计划中的页面有多少？
- 最重要的页面是哪些？（按流量、转化或业务价值）
- 有计划中的板块或扩展吗？

---

## 网站类型与起点

| 网站类型 | 典型深度 | 关键板块 | URL 模式 |
|-----------|--------------|--------------|-------------|
| SaaS 营销站 | 2-3 层 | 首页、功能、定价、博客、文档 | `/features/name`, `/blog/slug` |
| 内容/博客站 | 2-3 层 | 首页、博客、分类、关于 | `/blog/slug`, `/category/slug` |
| 电商 | 3-4 层 | 首页、分类、商品、购物车 | `/category/subcategory/product` |
| 文档站 | 3-4 层 | 首页、指南、API 参考 | `/docs/section/page` |
| 混合 SaaS+内容 | 3-4 层 | 首页、产品、博客、资源、文档 | `/product/feature`, `/blog/slug` |
| 小企业 | 1-2 层 | 首页、服务、关于、联系 | `/services/name` |

**完整页面层级模板**：见 [references/site-type-templates.md](references/site-type-templates.md)

---

## 页面层级设计

### 三次点击法则

用户应能从首页 3 次点击内到达任何重要页面。这不是铁律，但关键页面若埋到 4 层以下，一定出了问题。

### 扁平与纵深

| 方案 | 适用场景 | 代价 |
|----------|----------|----------|
| 扁平（2 层） | 小型网站、作品集 | 简单，但无法扩展 |
| 适中（3 层） | 大多数 SaaS、内容站 | 深度与可发现性的良好平衡 |
| 纵深（4 层以上） | 电商、大型文档站 | 可扩展，但内容可能被埋没 |

**经验法则**：在保持导航清爽的前提下尽量扁平。某个下拉菜单超过 20 项，就加一层层级。

### 层级定义

| 层级 | 含义 | 示例 |
|-------|-----------|---------|
| L0 | 首页 | `/` |
| L1 | 一级板块 | `/features`, `/blog`, `/pricing` |
| L2 | 板块页面 | `/features/analytics`, `/blog/seo-guide` |
| L3+ | 详情页 | `/docs/api/authentication` |

### ASCII 树格式

页面层级用这种格式：

```
Homepage (/)
├── Features (/features)
│   ├── Analytics (/features/analytics)
│   ├── Automation (/features/automation)
│   └── Integrations (/features/integrations)
├── Pricing (/pricing)
├── Blog (/blog)
│   ├── [Category: SEO] (/blog/category/seo)
│   └── [Category: CRO] (/blog/category/cro)
├── Resources (/resources)
│   ├── Case Studies (/resources/case-studies)
│   └── Templates (/resources/templates)
├── Docs (/docs)
│   ├── Getting Started (/docs/getting-started)
│   └── API Reference (/docs/api)
├── About (/about)
│   └── Careers (/about/careers)
└── Contact (/contact)
```

**何时用 ASCII，何时用 Mermaid**：
- ASCII：快速层级草稿、纯文本场景、简单结构
- Mermaid：可视化展示、复杂关系、展示导航分区或链接模式

---

## 导航设计

### 导航类型

| 导航类型 | 用途 | 位置 |
|----------|---------|-----------|
| 顶部导航 | 主导航，始终可见 | 每页顶部 |
| 下拉菜单 | 在父项下组织子页面 | 从顶部导航项展开 |
| 页脚导航 | 次要链接、法律条款、站点地图 | 每页底部 |
| 侧边栏导航 | 板块内导航（文档、博客） | 板块内左侧 |
| 面包屑 | 显示当前层级位置 | 页头下方、内容上方 |
| 上下文链接 | 相关内容、下一步 | 页面内容之中 |

### 顶部导航规则

- 主导航**最多 4-7 项**（多了会造成决策瘫痪）
- **CTA 按钮**放最右侧（如"开始免费试用"、"立即开始"）
- **Logo** 链接到首页（左侧）
- **按优先级排序**：最重要/最常访问的页面在前
- 如果用超级菜单（mega menu），限制在 3-4 列

### 页脚组织

页脚链接按列分组：
- **产品**：功能、定价、集成、更新日志
- **资源**：博客、案例研究、模板、文档
- **公司**：关于、招聘、联系、媒体
- **法律**：隐私、条款、安全

### 面包屑格式

```
Home > Features > Analytics
Home > Blog > SEO Category > Post Title
```

面包屑应与 URL 层级一致。除当前页外，每段面包屑都应是可点击链接。

**详细导航模式**：见 [references/navigation-patterns.md](references/navigation-patterns.md)

---

## URL 结构

### 设计原则

1. **人类可读**：用 `/features/analytics`，不用 `/f/a123`
2. **用连字符，不用下划线**：用 `/blog/seo-guide`，不用 `/blog/seo_guide`
3. **反映层级**：URL 路径应与网站结构一致
4. **统一的尾斜杠策略**：选定一种（带或不带），全站执行
5. **一律小写**：`/About` 应重定向到 `/about`
6. **短而达意**：`/blog/how-to-improve-landing-page-conversion-rates` 太长；`/blog/landing-page-conversions` 更好

### 各页面类型的 URL 模式

| 页面类型 | 模式 | 示例 |
|-----------|---------|---------|
| 首页 | `/` | `example.com` |
| 功能页 | `/features/{name}` | `/features/analytics` |
| 定价页 | `/pricing` | `/pricing` |
| 博客文章 | `/blog/{slug}` | `/blog/seo-guide` |
| 博客分类 | `/blog/category/{slug}` | `/blog/category/seo` |
| 案例研究 | `/customers/{slug}` | `/customers/acme-corp` |
| 文档 | `/docs/{section}/{page}` | `/docs/api/authentication` |
| 法律页 | `/{page}` | `/privacy`, `/terms` |
| 落地页 | `/{slug}` 或 `/lp/{slug}` | `/free-trial`, `/lp/webinar` |
| 对比页 | `/compare/{competitor}` 或 `/vs/{competitor}` | `/compare/competitor-name` |
| 集成页 | `/integrations/{name}` | `/integrations/slack` |
| 模板页 | `/templates/{slug}` | `/templates/marketing-plan` |

### 常见错误

- **博客 URL 带日期**：`/blog/2024/01/15/post-title` 没有价值，只会让 URL 变长。用 `/blog/post-title`。
- **嵌套过深**：`/products/category/subcategory/item/detail` 太深。尽量拍平。
- **改 URL 不做重定向**：每个旧 URL 都需要 301 重定向到新 URL。没有重定向，你会损失外链权重，并让收藏或外链了旧地址的人看到失效页面。
- **URL 里放 ID**：`/product/12345` 不可读。用 slug。
- **用查询参数承载内容**：`/blog?id=123` 应改为 `/blog/post-title`。
- **模式不一致**：不要混用 `/features/analytics` 和 `/product/automation`。选一个父路径。

### 面包屑与 URL 对齐

面包屑路径应与 URL 路径一致：

| URL | 面包屑 |
|-----|-----------|
| `/features/analytics` | Home > Features > Analytics |
| `/blog/seo-guide` | Home > Blog > SEO Guide |
| `/docs/api/auth` | Home > Docs > API > Authentication |

---

## 可视化站点地图输出（Mermaid）

可视化站点地图用 Mermaid `graph TD`。层级关系一目了然，还能标注导航分区。

### 基础层级

```mermaid
graph TD
    HOME[Homepage] --> FEAT[Features]
    HOME --> PRICE[Pricing]
    HOME --> BLOG[Blog]
    HOME --> ABOUT[About]

    FEAT --> F1[Analytics]
    FEAT --> F2[Automation]
    FEAT --> F3[Integrations]

    BLOG --> B1[Post 1]
    BLOG --> B2[Post 2]
```

### 带导航分区

```mermaid
graph TD
    subgraph Header Nav
        HOME[Homepage]
        FEAT[Features]
        PRICE[Pricing]
        BLOG[Blog]
        CTA[Get Started]
    end

    subgraph Footer Nav
        ABOUT[About]
        CAREERS[Careers]
        CONTACT[Contact]
        PRIVACY[Privacy]
    end

    HOME --> FEAT
    HOME --> PRICE
    HOME --> BLOG
    HOME --> ABOUT

    FEAT --> F1[Analytics]
    FEAT --> F2[Automation]
```

**更多 Mermaid 模板**：见 [references/mermaid-templates.md](references/mermaid-templates.md)

---

## 内链策略

### 链接类型

| 类型 | 用途 | 示例 |
|------|---------|---------|
| 导航型 | 在板块之间移动 | 页头、页脚、侧边栏链接 |
| 上下文型 | 正文内的相关内容 | "详细了解[分析功能](/features/analytics)" |
| 中心-辐射型 | 把集群内容连到中心页 | 博客文章链接到支柱页（pillar page） |
| 跨板块型 | 连接不同板块的相关页面 | 功能页链接到相关案例研究 |

### 内链规则

1. **不留孤立页面**：每个页面至少要有一条内链指向它
2. **锚文本要描述性**：写"我们的分析功能"，不写"点击这里"
3. 每 1000 字内容放 **5-10 条内链**（近似参考值）
4. **重要页面多链接**：首页、核心功能页、定价页
5. **用面包屑**：每页自带免费内链
6. **相关内容板块**：页面底部放"相关文章"或"你可能也喜欢"

### 中心-辐射模型

内容量大的网站，围绕中心页（hub）组织：

```
Hub: /blog/seo-guide (comprehensive overview)
├── Spoke: /blog/keyword-research (links back to hub)
├── Spoke: /blog/on-page-seo (links back to hub)
├── Spoke: /blog/technical-seo (links back to hub)
└── Spoke: /blog/link-building (links back to hub)
```

每个辐射页（spoke）都链回中心页；中心页链接所有辐射页；辐射页之间在相关处互链。

### 链接审计检查清单

- [ ] 每个页面至少有一条入站内链
- [ ] 没有失效内链（404）
- [ ] 锚文本是描述性的（不是"点击这里"或"阅读更多"）
- [ ] 重要页面拥有最多的入站内链
- [ ] 所有页面都实现了面包屑
- [ ] 博客文章有相关内容链接
- [ ] 跨板块链接把功能页连到案例研究、博客连到产品页

---

## 输出格式

产出网站架构方案时，交付以下成果：

### 1. 页面层级（ASCII 树）
完整站点结构，每个节点带 URL。用"页面层级设计"一节的 ASCII 树格式。

### 2. 可视化站点地图（Mermaid）
Mermaid 图展示页面关系和导航分区。需要时用 `graph TD` 加 subgraph 标注导航分区。

### 3. URL 映射表

| 页面 | URL | 父级 | 导航位置 | 优先级 |
|------|-----|--------|-------------|----------|
| 首页 | `/` | — | 顶部导航 | 高 |
| 功能 | `/features` | 首页 | 顶部导航 | 高 |
| 分析 | `/features/analytics` | 功能 | 顶部下拉 | 中 |
| 定价 | `/pricing` | 首页 | 顶部导航 | 高 |
| 博客 | `/blog` | 首页 | 顶部导航 | 中 |

### 4. 导航规格
- 顶部导航项（有序，含 CTA）
- 页脚板块和链接
- 侧边栏导航（如适用）
- 面包屑实现说明

### 5. 内链计划
- 中心页及其辐射页
- 跨板块链接机会
- 孤立页面审计（如重构）
- 每个关键页面的建议链接数

---

## 针对任务的提问

1. 这是全新网站，还是在重构现有网站？
2. 网站类型是什么？（SaaS、内容、电商、文档、混合、小企业）
3. 现有或计划中的页面有多少？
4. 网站最重要的 5 个页面是什么？
5. 有需要保留或重定向的现有 URL 吗？
6. 主要受众是谁？他们想在网站上完成什么？

---

## 相关 Skills

- **content-strategy**：规划要创建的内容和主题集群
- **programmatic-seo**：用模板和数据批量构建 SEO 页面
- **seo-audit**：技术 SEO、页面优化和收录问题
- **cro**：优化单个页面的转化
- **schema**：实现面包屑和站点导航的结构化数据
- **competitors**：对比页框架和 URL 模式
- **launch**：建站或迁移后的上线 QA
