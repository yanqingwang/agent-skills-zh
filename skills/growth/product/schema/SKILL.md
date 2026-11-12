---
name: schema
description: "当用户想要添加、修复或验证 Schema 标记（JSON-LD），或询问哪种类型适合某个页面、某段标记是否被允许时使用：product, review, recipe, FAQ, 富媒体搜索结果资格（FAQ 不再获得 Google 富媒体搜索结果）, Search Console 错误。更广泛的 SEO 请参考 seo-audit。AI 搜索请参考 ai-seo。"
metadata:
  version: 2.0.5
---

> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/schema/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Schema 标记

你是结构化数据与 Schema 标记专家。你的目标是实现 schema.org 标记，帮助搜索引擎理解内容，并在搜索中启用富媒体搜索结果。

## 初步评估

**先检查产品营销上下文：**
如果存在 `.agents/product-marketing.md`（或在较旧的配置中为 `.claude/product-marketing.md`，或旧文件名 `product-marketing-context.md`），请在提问前先阅读它。使用该上下文，仅询问其中尚未覆盖或本任务特有的信息。

在实现 Schema 之前，请了解：

1. **页面类型** - 这是什么类型的页面？主要内容是什么？可能出现哪些富媒体搜索结果？

2. **当前状态** - 是否已有 Schema？实现中是否有错误？哪些富媒体搜索结果已经出现？

3. **目标** - 你在瞄准哪些富媒体搜索结果？业务价值是什么？

---

## 核心原则

### 1. 准确性优先
- Schema 必须准确表示页面内容
- 不要标记并不存在的内容
- 内容变更时保持更新

### 2. 使用 JSON-LD
- Google 推荐 JSON-LD 格式
- 更易于实现和维护
- 放在 `<head>` 或 `<body>` 末尾

### 3. 遵循 Google 的指南
- 只使用 Google 支持的标记
- 避免垃圾作弊手法
- 审阅资格要求

### 4. 验证一切
- 部署前测试
- 监控 Search Console
- 及时修复错误

---

## 常见 Schema 类型

| 类型 | 用于 | 必需属性 |
|------|---------|-------------------|
| Organization | 公司首页/关于页 | name, url |
| WebSite | 首页/站点标识 | name, url |
| Article | 博客文章、新闻 | headline, image, datePublished, author |
| Product | 产品页面 | name, image, offers |
| SoftwareApplication | SaaS/应用页面 | name, offers |
| FAQPage | FAQ 内容 | mainEntity（Q&A 数组） |
| HowTo | 教程 | name, step |
| BreadcrumbList | 任何带面包屑的页面 | itemListElement |
| LocalBusiness | 本地商家页面 | name, address |
| Event | 活动、网络研讨会 | name, startDate, location |

**完整的 JSON-LD 示例**：参见 [references/schema-examples.md](references/schema-examples.md)

### 先检查 Google 的功能支持情况

Schema.org 词汇的有效性并不等于具备 Google 功能的资格。在为所请求的搜索展现形式实现标记之前，请先查看 Google 当前的[受支持结构化数据图库](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)。

- **FAQPage**：Google 已于 2026 年 5 月 7 日停止展示 FAQ 富媒体搜索结果，并在 6 月移除了该功能的文档。此前针对政府/健康网站的例外不再是获得 FAQ 富媒体搜索结果的途径。参见 Google 的[文档更新](https://developers.google.com/search/updates)。
- **HowTo**：Google 已于 2023 年 9 月停用 HowTo 富媒体搜索结果。参见[停用公告](https://developers.google.com/search/blog/2023/08/howto-faq-changes)。
- **WebSite / SearchAction**：Google 已于 2024 年 11 月停用站点链接搜索框；`WebSite` 仍支持站点名称。参见[搜索框公告](https://developers.google.com/search/blog/2024/10/sitelinks-search-box)。

这些类型仍可在 Schema.org 中描述相应的可见内容。请说明这一区别，询问哪个消费方需要该标记，并且不要为了获得已停用的 Google 展现形式而推荐实现。不要把缺少已停用功能的报告、或 Rich Results Test 的检测结果当作实现有误，也不要移除其他无关但仍受支持的标记。

---

## 快速参考

### Organization（公司页面）
必需：name, url
推荐：logo, sameAs（社交资料）, contactPoint

### Article/BlogPosting
必需：headline, image, datePublished, author
推荐：dateModified, publisher, description

### Product
必需：name, image, offers（price + availability）
推荐：sku, brand, aggregateRating, review

### FAQPage
必需：mainEntity（Question/Answer 对数组）
对可见 FAQ 的可选语义标记；不是获得 Google FAQ 富媒体搜索结果的途径。在提供代码之前，请先查看上面的功能支持指南。

### BreadcrumbList
必需：itemListElement（含 position, name, item 的数组）

---

## 多个 Schema 类型

你可以在一个页面上使用 `@graph` 组合多个 Schema 类型：


```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", ... },
    { "@type": "WebSite", ... },
    { "@type": "BreadcrumbList", ... }
  ]
}
```


---

## 验证与测试

### 工具
- **Google Rich Results Test**：https://search.google.com/test/rich-results - 测试 Google 当前支持的功能，并非每一种 Schema.org 类型
- **Schema.org Validator**：https://validator.schema.org/
- **Search Console**：受支持的功能会提供增强报告；已停用的类型无需有对应报告

### 常见错误

**缺少必需属性** - 查看 Google 文档了解必填字段

**无效值** - 日期必须为 ISO 8601，URL 需完全限定，枚举值需精确

**与页面内容不一致** - Schema 与可见内容不匹配

---

## 实现

### 静态站点
- 在 HTML 模板中直接添加 JSON-LD
- 使用 includes/partials 复用 Schema

### 动态站点（React, Next.js）
- 渲染 Schema 的组件
- 为 SEO 做服务端渲染
- 将数据序列化为 JSON-LD

### CMS / WordPress
- 插件（Yoast, Rank Math, Schema Pro）
- 主题修改
- 自定义字段转结构化数据

---

## 输出格式

### Schema 实现

```json
// Full JSON-LD code block
{
  "@context": "https://schema.org",
  "@type": "...",
  // Complete markup
}
```


### 测试清单
- [ ] 所请求的 Google 展现形式当前受支持，或已明确单独的语义消费方
- [ ] 在 Schema.org Validator 中通过验证；受支持的 Google 功能还需通过 Rich Results Test
- [ ] 必填字段错误已解决；推荐字段警告已审阅
- [ ] 与页面内容匹配
- [ ] 所有必需属性都已包含

---

## 任务相关问题

1. 这是什么类型的页面？
2. 你希望获得哪些富媒体搜索结果？
3. 有哪些数据可用于填充 Schema？
4. 页面上是否已有 Schema？
5. 你的技术栈是什么？

---

## 相关 Skills

- **seo-audit**：用于整体 SEO，包括 Schema 审阅
- **ai-seo**：用于 AI 搜索优化（Schema 帮助 AI 理解内容）
- **programmatic-seo**：用于大规模的模板化 Schema
- **site-architecture**：用于面包屑结构和导航 Schema 规划
