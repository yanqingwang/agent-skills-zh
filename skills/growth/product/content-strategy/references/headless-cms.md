> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/content-strategy/references/headless-cms.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Headless CMS 指南

为营销内容选择、建模和实施 headless CMS 的参考文档。

## 何时使用本参考文档

适用于：为新项目选择 CMS、为营销站点设计内容模型、搭建编辑工作流，或将 CMS 内容接入程序化页面。

---

## Headless CMS 与传统 CMS

Headless CMS 把内容管理与呈现分离。内容存储在结构化的后端中，通过 API 交付给任意前端。

### 何时适合 Headless

- 多个前端消费同一份内容（Web、移动端、邮件）
- 开发者希望完全掌控前端技术栈
- 内容需要跨渠道复用
- 你在使用现代框架构建（Next.js、Remix、Astro）
- 营销团队需要结构化、可复用的内容块

### 何时传统 CMS 更合适

- 小团队，没有专职开发者
- 简单的博客或宣传页站点
- 所见即所得编辑是硬性要求
- 预算紧张，WordPress/Webflow 就够用

### 决策清单

| 因素 | Headless | 传统 |
|--------|----------|-------------|
| 多渠道交付 | 是 | 有限 |
| 开发者掌控度 | 完全 | 受限 |
| 非技术人员编辑 | 需要配置 | 内置 |
| 上线时间 | 更长 | 更快 |
| 内容复用 | 原生支持 | 手动 |
| 托管灵活性 | 任意前端 | 取决于平台 |

---

## 面向营销的内容建模

### 核心原则

1. **按类型思考，而不是按页面思考。** "Landing Page"（落地页）是带字段的内容类型，不是一个 HTML 文件。这让你能跨页面复用组件。
2. **内容与呈现分离。** 存储标题文本，而不是带样式的标题。呈现属于前端。
3. **为复用而设计。** 如果客户评价出现在 5 个页面上，就创建一个 Testimonial 类型并通过引用使用它，不要复制粘贴。
4. **保持模型扁平。** 深层嵌套的结构难以查询和维护。优先用引用（reference）而不是嵌套。

### 常见营销内容类型

| 类型 | 关键字段 | 备注 |
|------|-----------|-------|
| **Landing Page** | title, slug, hero, sections[], seo | 模块化 section，灵活组合 |
| **Blog Post** | title, slug, body, author, category, tags, publishedAt, seo | 富文本或 Portable Text 正文 |
| **Case Study** | title, customer, challenge, solution, results, metrics[], logo | 链接到相关产品/功能 |
| **Testimonial** | quote, author, role, company, avatar, rating | 从落地页引用 |
| **FAQ** | question, answer, category | 按类别分组，供程序化页面使用 |
| **Author** | name, bio, avatar, social links | 从博客文章引用 |
| **CTA Block** | heading, body, buttonText, buttonUrl, variant | 跨页面复用 |

### SEO 字段清单

每个页面级内容类型都需要：

- `metaTitle`：50-60 个字符
- `metaDescription`：150-160 个字符
- `ogImage`：1200x630px 社交预览图
- `slug`：URL 路径片段
- `canonicalUrl`：可选覆盖项
- `noIndex`：布尔值，用于排除出搜索索引
- `structuredData`：可选的 JSON-LD 覆盖

---

## 编辑工作流

### 草稿 → 审核 → 发布循环

1. **草稿**：作者创建或编辑内容
2. **审核**：编辑检查准确性、品牌语调、SEO
3. **批准**：利益相关者签字确认
4. **排期**：设定发布日期/时间
5. **发布**：内容通过 API 上线

### 预览 API

所有主流 headless CMS 平台都支持草稿预览：

- **Sanity**：通过 `useLiveQuery` 或 Presentation 工具实现实时预览
- **Contentful**：Preview API（`preview.contentful.com`），使用独立的访问令牌
- **Strapi**：Draft & Publish 机制，配合 `status=draft` 查询参数（v5；取代 v4 的 `publicationState`）

在前端设置一个预览路由（如 `/api/preview`），负责鉴权并渲染草稿内容。

### 角色与权限

| 角色 | 可创建 | 可编辑 | 可发布 | 可删除 |
|------|:----------:|:--------:|:-----------:|:----------:|
| Author | 是 | 自己的 | 否 | 自己的草稿 |
| Editor | 是 | 全部 | 是 | 草稿 |
| Admin | 是 | 全部 | 是 | 全部 |

具体权限模型因平台而异。Sanity 使用基于角色的访问控制。Contentful 有 space 级别的角色。Strapi 有细粒度的 RBAC。

---

## 平台对比

| 特性 | Sanity | Contentful | Strapi |
|---------|--------|------------|--------|
| 托管 | 云（托管） | 云（托管） | 自托管或云 |
| 查询语言 | GROQ | REST / GraphQL | REST / GraphQL |
| 免费额度 | 大方 | 有限 | 开源（免费） |
| 实时协作 | 是（内置） | 有限 | 无 |
| 最适合 | 开发者灵活性 | 企业多语言 | 预算敏感 / 自托管 |
| 内容建模 | Schema 即代码 | Web 界面 | Web 界面或代码 |
| 媒体处理 | 内置 DAM | 内置 | 插件 |

### Sanity

**优势**：GROQ 查询语言强大且灵活。Schema 以代码形式定义（可版本控制）。实时协作编辑。Portable Text 处理富内容。免费额度大方。

**注意事项**：非开发者的学习曲线较陡。Studio 定制需要 React 知识。GROQ 查询存在厂商锁定。

**营销适配**：最适合开发者与营销紧密协作的团队。对内容量大、模型复杂的站点尤其有优势。

### Contentful

**优势**：成熟的企业级平台。出色的多语言支持。丰富的集成生态。通过 Studio 实现可组合内容。API 文档完善。

**注意事项**：定价随内容类型和语言数量增长。两套独立的 API（Delivery 和 Management）。低档套餐的速率限制可能偏紧。

**营销适配**：最适合有多市场内容需求的企业。需要成熟可靠的供应商时也是好选择。

### Strapi

**优势**：开源，可自托管。完全掌控数据。无按席位定价。管理面板可定制。有插件生态。默认 REST，通过插件支持 GraphQL。

**注意事项**：自托管意味着基础设施自理。生态比 Sanity/Contentful 小。从 V4 迁移到 V5 可能工作量不小。

**营销适配**：最适合有 DevOps 能力、想要完全掌控且不被厂商锁定的团队。预算敏感的项目也合适。

### 其他值得了解的平台

- **Hygraph**：GraphQL 原生，擅长联邦查询和多源内容
- **Keystatic**：基于 Git，适合开发者与内容混合的工作流
- **Payload**：TypeScript 优先，自托管，像 Sanity 一样用代码配置
- **Builder.io**：可视化编辑器 + headless 后端，适合非技术营销人员
- **Prismic**：基于 Slice 的内容建模，与 Next.js 集成出色

---

## 与营销 Skills 的集成

### 程序化 SEO

把 CMS 作为程序化页面的数据源。将结构化数据（FAQ、对比、城市页）存为内容类型，再从查询生成页面。参见 **programmatic-seo** skill。

### 文案写作

CMS 内容模型强制结构一致。定义与你文案框架对应的字段（headline、subheadline、social proof、CTA）。参见 **copywriting** skill。

### 站点架构

URL 结构、导航层级和内链都取决于内容在 CMS 中的组织方式。把内容模型和站点架构放在一起规划。参见 **site-architecture** skill。

### 邮件序列

把 CMS 内容拉入邮件模板，让 Web 和邮件的信息传达保持一致。案例研究、客户评价和博客文章都可以喂给邮件培育序列。参见 **emails** skill。

---

## 实施清单

- [ ] 基于页面类型和可复用块定义内容类型
- [ ] 为每个页面级内容类型添加 SEO 字段
- [ ] 在前端设置预览/草稿模式
- [ ] 为团队配置角色与权限
- [ ] 在搭建前端之前，先为每个类型创建示例内容
- [ ] 为内容变更配置 webhook 通知（触发重新构建）
- [ ] 为编辑人员编写内容规范文档（字段说明、字符限制）
- [ ] 测试内容交付性能（CDN、缓存、ISR）
- [ ] 如果从现有 CMS 迁移，提前规划迁移策略

---

## 相关集成指南

- [Sanity](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/sanity.md)：GROQ 查询、mutations、CLI
- [Contentful](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/contentful.md)：Delivery/Management API、发布
- [Strapi](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/strapi.md)：REST CRUD、过滤器、document API
