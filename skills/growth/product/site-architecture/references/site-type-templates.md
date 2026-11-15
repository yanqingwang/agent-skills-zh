> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/growth/product/site-architecture/references/site-type-templates.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 站点类型模板

常见站点类型的完整页面层级模板，含 ASCII 树、URL 映射和导航建议。

---

## SaaS 营销站

### 页面层级

```
Homepage (/)
├── Features (/features)
│   ├── Feature A (/features/feature-a)
│   ├── Feature B (/features/feature-b)
│   └── Feature C (/features/feature-c)
├── Pricing (/pricing)
├── Customers (/customers)
│   ├── Case Study 1 (/customers/company-name)
│   └── Case Study 2 (/customers/company-name-2)
├── Resources (/resources)
│   ├── Blog (/blog)
│   │   └── [Posts] (/blog/post-slug)
│   ├── Templates (/resources/templates)
│   │   └── [Template] (/resources/templates/template-slug)
│   └── Guides (/resources/guides)
│       └── [Guide] (/resources/guides/guide-slug)
├── Integrations (/integrations)
│   └── [Integration] (/integrations/integration-name)
├── Docs (/docs)
│   ├── Getting Started (/docs/getting-started)
│   ├── Guides (/docs/guides)
│   └── API Reference (/docs/api)
├── About (/about)
│   ├── Careers (/about/careers)
│   └── Contact (/contact)
├── Compare (/compare)
│   └── [Competitor] (/compare/competitor-name)
├── Privacy (/privacy)
└── Terms (/terms)
```

### URL 映射

| 页面 | URL | 导航位置 | 优先级 |
|------|-----|-------------|----------|
| 首页 | `/` | 头部（logo） | 关键 |
| 功能 | `/features` | 头部 | 高 |
| 功能页 | `/features/{slug}` | 头部下拉 | 中 |
| 定价 | `/pricing` | 头部 | 关键 |
| 客户 | `/customers` | 头部 | 中 |
| 案例研究 | `/customers/{slug}` | 客户下拉 | 中 |
| 博客 | `/blog` | 头部（资源） | 高 |
| 博客文章 | `/blog/{slug}` | — | 中 |
| 集成 | `/integrations` | 头部 | 中 |
| 文档 | `/docs` | 头部 | 中 |
| 对比 | `/compare/{slug}` | 页脚 | 高（SEO） |
| 关于 | `/about` | 页脚 | 低 |
| 定价 CTA | `/pricing` | 头部（CTA 按钮） | 关键 |

### 导航

**头部（6 项 + CTA）**：功能 | 定价 | 客户 | 资源 | 集成 | 文档 | [开始使用]

**页脚分栏**：
- 产品：功能、定价、集成、更新日志、安全
- 资源：博客、模板、指南、案例研究
- 公司：关于、招聘、联系、媒体
- 法律：隐私、条款、安全

---

## 内容 / 博客站

### 页面层级

```
Homepage (/)
├── Blog (/blog)
│   ├── [Category: Topic A] (/blog/category/topic-a)
│   ├── [Category: Topic B] (/blog/category/topic-b)
│   ├── [Category: Topic C] (/blog/category/topic-c)
│   └── [Posts] (/blog/post-slug)
├── Newsletter (/newsletter)
├── Resources (/resources)
│   ├── Guides (/resources/guides)
│   │   └── [Guide] (/resources/guides/guide-slug)
│   └── Tools (/resources/tools)
│       └── [Tool] (/resources/tools/tool-slug)
├── About (/about)
├── Contact (/contact)
├── Privacy (/privacy)
└── Terms (/terms)
```

### URL 映射

| 页面 | URL | 导航位置 | 优先级 |
|------|-----|-------------|----------|
| 首页 | `/` | 头部（logo） | 关键 |
| 博客索引 | `/blog` | 头部 | 高 |
| 分类 | `/blog/category/{slug}` | 头部下拉 | 中 |
| 文章 | `/blog/{slug}` | — | 中 |
| 订阅通讯 | `/newsletter` | 头部（CTA） | 高 |
| 指南 | `/resources/guides` | 头部 | 中 |
| 关于 | `/about` | 头部 | 低 |

### 导航

**头部（4 项 + CTA）**：博客 | 资源 | 关于 | 联系 | [订阅]

**侧边栏**（博客页）：分类、热门文章、订阅通讯注册

---

## 电商

### 页面层级

```
Homepage (/)
├── Shop (/shop)
│   ├── Category A (/shop/category-a)
│   │   ├── Subcategory (/shop/category-a/subcategory)
│   │   │   └── [Product] (/shop/category-a/subcategory/product-slug)
│   │   └── [Product] (/shop/category-a/product-slug)
│   ├── Category B (/shop/category-b)
│   │   └── [Product] (/shop/category-b/product-slug)
│   └── Category C (/shop/category-c)
│       └── [Product] (/shop/category-c/product-slug)
├── Collections (/collections)
│   └── [Collection] (/collections/collection-slug)
├── Sale (/sale)
├── Blog (/blog)
│   └── [Posts] (/blog/post-slug)
├── About (/about)
│   └── Our Story (/about/our-story)
├── Help (/help)
│   ├── FAQ (/help/faq)
│   ├── Shipping (/help/shipping)
│   ├── Returns (/help/returns)
│   └── Contact (/contact)
├── Cart (/cart)
├── Account (/account)
├── Privacy (/privacy)
└── Terms (/terms)
```

### URL 映射

| 页面 | URL | 导航位置 | 优先级 |
|------|-----|-------------|----------|
| 首页 | `/` | 头部（logo） | 关键 |
| 商店 | `/shop` | 头部 | 关键 |
| 分类 | `/shop/{category}` | 头部巨型菜单 | 高 |
| 商品 | `/shop/{category}/{product}` | — | 高 |
| 合集 | `/collections/{slug}` | 头部 | 中 |
| 促销 | `/sale` | 头部（高亮） | 高 |
| 购物车 | `/cart` | 头部（图标） | 关键 |
| 账户 | `/account` | 头部（图标） | 中 |

### 导航

**头部（5 项 + 购物车/账户）**：商店（巨型菜单） | 合集 | 促销 | 博客 | 帮助 | [购物车图标] [账户图标]

**商店下的巨型菜单**：按分类分栏，带精选商品和图片

---

## 文档站

### 页面层级

```
Docs Home (/docs)
├── Getting Started (/docs/getting-started)
│   ├── Installation (/docs/getting-started/installation)
│   ├── Quick Start (/docs/getting-started/quick-start)
│   └── Configuration (/docs/getting-started/configuration)
├── Guides (/docs/guides)
│   ├── Guide A (/docs/guides/guide-a)
│   ├── Guide B (/docs/guides/guide-b)
│   └── Guide C (/docs/guides/guide-c)
├── API Reference (/docs/api)
│   ├── Authentication (/docs/api/authentication)
│   ├── Endpoints (/docs/api/endpoints)
│   └── Webhooks (/docs/api/webhooks)
├── Examples (/docs/examples)
│   └── [Example] (/docs/examples/example-slug)
├── Changelog (/docs/changelog)
└── FAQ (/docs/faq)
```

### URL 映射

| 页面 | URL | 导航位置 | 优先级 |
|------|-----|-------------|----------|
| 文档首页 | `/docs` | 头部 | 高 |
| 入门 | `/docs/getting-started` | 侧边栏（顶部） | 关键 |
| 指南 | `/docs/guides` | 侧边栏 | 高 |
| API 参考 | `/docs/api` | 侧边栏 | 高 |
| 更新日志 | `/docs/changelog` | 侧边栏（底部） | 低 |

### 导航

**头部**：文档 | API | 博客 | 社区 | GitHub | [控制台]

**侧边栏**（常驻左侧）：入门、指南、API 参考、示例、更新日志，子分区可展开

**页内**：每篇文档底部放上一篇/下一篇导航

---

## SaaS + 内容混合站

### 页面层级

```
Homepage (/)
├── Product (/product)
│   ├── Feature A (/product/feature-a)
│   ├── Feature B (/product/feature-b)
│   └── Feature C (/product/feature-c)
├── Solutions (/solutions)
│   ├── By Use Case (/solutions/use-case-slug)
│   └── By Industry (/solutions/industry-slug)
├── Pricing (/pricing)
├── Blog (/blog)
│   ├── [Category] (/blog/category/slug)
│   └── [Posts] (/blog/post-slug)
├── Resources (/resources)
│   ├── Guides (/resources/guides)
│   ├── Templates (/resources/templates)
│   ├── Webinars (/resources/webinars)
│   └── Case Studies (/resources/case-studies)
├── Docs (/docs)
│   ├── Getting Started (/docs/getting-started)
│   └── API (/docs/api)
├── Integrations (/integrations)
│   └── [Integration] (/integrations/slug)
├── Compare (/compare)
│   └── [Competitor] (/compare/competitor-slug)
├── About (/about)
│   ├── Careers (/about/careers)
│   └── Contact (/contact)
├── Privacy (/privacy)
└── Terms (/terms)
```

### 导航

**头部（7 项 + CTA）**：产品 | 方案 | 定价 | 资源 | 博客 | 文档 | 集成 | [开始免费试用]

产品（功能清单）、方案（使用场景 + 行业）、资源（博客、指南、模板、网络研讨会、案例研究）都用巨型菜单。

---

## 小型企业 / 本地商家

### 页面层级

```
Homepage (/)
├── Services (/services)
│   ├── Service A (/services/service-a)
│   ├── Service B (/services/service-b)
│   └── Service C (/services/service-c)
├── About (/about)
├── Testimonials (/testimonials)
├── Blog (/blog)
│   └── [Posts] (/blog/post-slug)
├── Contact (/contact)
├── Privacy (/privacy)
└── Terms (/terms)
```

### URL 映射

| 页面 | URL | 导航位置 | 优先级 |
|------|-----|-------------|----------|
| 首页 | `/` | 头部（logo） | 关键 |
| 服务 | `/services` | 头部 | 高 |
| 服务页 | `/services/{slug}` | 头部下拉 | 高 |
| 关于 | `/about` | 头部 | 中 |
| 客户评价 | `/testimonials` | 头部 | 中 |
| 博客 | `/blog` | 头部 | 中 |
| 联系 | `/contact` | 头部（CTA） | 高 |

### 导航

**头部（5 项 + CTA）**：服务 | 关于 | 客户评价 | 博客 | [联系我们]

保持简单。小型企业站点要扁平（最多 1-2 层）。每个页面都能从头部导航到达。
