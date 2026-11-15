> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/growth/product/site-architecture/references/navigation-patterns.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 导航模式

面向不同站点类型与场景的详细导航模式。

---

## 头部导航

### 简易头部（4-6 项）

适用：小型企业、简单 SaaS、作品集站点。

```
[Logo]   Features   Pricing   Blog   About   [CTA Button]
```

规则：
- Logo 始终链接到首页
- CTA 按钮放在最右，视觉上要突出（实心按钮、对比色）
- 各项按优先级排序（访问量最高的在前）
- 当前页面加视觉标识（下划线、加粗、配色）

### 巨型菜单头部

适用：功能众多的 SaaS、带分类的电商、大型内容站。

```
[Logo]   Product ▾   Solutions ▾   Resources ▾   Pricing   Docs   [CTA]
```

悬停或点击 "Product" 时：

```
┌─────────────────────────────────────────────────┐
│  Features           Platform        Integrations │
│  ─────────          ─────────       ──────────── │
│  Analytics           Security       Slack         │
│  Automation          API            HubSpot       │
│  Reporting           Compliance     Salesforce    │
│  Dashboards                         Zapier        │
│                                                   │
│  [See all features →]                             │
└─────────────────────────────────────────────────┘
```

巨型菜单规则：
- 最多 2-4 列
- 按逻辑分组（按功能域、使用场景或受众）
- 底部放一个 "See all" 链接
- 不要在巨型菜单里嵌套下拉菜单
- 标签表意不清时，给条目加说明

### 分离式导航

适用：营销导航与产品导航并存的应用。

```
[Logo]   Features   Pricing   Blog        [Login]   [Sign Up]
├── Marketing nav (left) ──────┘          └── Auth nav (right) ──┤
```

右侧放认证操作，左侧放页面导航。

---

## 页脚导航

### 分栏页脚（标准）

适用：多数站点。把链接整理成 3-5 个主题分栏。

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  Product          Resources        Company       Legal   │
│  ─────────        ──────────       ─────────     ─────   │
│  Features         Blog             About         Privacy │
│  Pricing          Guides           Careers       Terms   │
│  Integrations     Templates        Contact       GDPR    │
│  Changelog        Case Studies     Press                 │
│  Security         Webinars         Partners              │
│                                                          │
│  [Logo]  © 2026 Company Name                             │
│  Social: [Twitter] [LinkedIn] [GitHub]                   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 极简页脚

适用：简单站点、落地页。

```
┌──────────────────────────────────────────────────────────┐
│  [Logo]                                                  │
│  © 2026 Company  ·  Privacy  ·  Terms  ·  Contact        │
└──────────────────────────────────────────────────────────┘
```

### 扩展页脚

适用：把页脚用于 SEO 的站点（对比页、地区页、资源链接）。

```
┌──────────────────────────────────────────────────────────┐
│  Product     Resources    Compare         Use Cases      │
│  Features    Blog         vs Competitor A  For Startups  │
│  Pricing     Guides       vs Competitor B  For Enterprise│
│  API         Templates    vs Competitor C  For Agencies  │
│                                                          │
│  Integrations             Popular Posts                  │
│  Slack       Zapier       How to Do X                    │
│  HubSpot     Salesforce   Guide to Y                     │
│                           Template: Z                    │
│                                                          │
│  [Logo]  © 2026  ·  Privacy  ·  Terms  ·  Security      │
└──────────────────────────────────────────────────────────┘
```

---

## 侧边栏导航

### 文档侧边栏

常驻左侧栏，分区可折叠。

```
Getting Started
  ├── Installation
  ├── Quick Start
  └── Configuration

Guides
  ├── Authentication
  ├── Data Models
  └── Deployment

API Reference
  ├── REST API
  │   ├── Users
  │   ├── Projects
  │   └── Webhooks
  └── GraphQL

Examples
  ├── Next.js
  ├── Rails
  └── Python

Changelog
```

规则：
- 高亮当前页面
- 分区可折叠（当前所在分区默认展开）
- 搜索框放在侧边栏顶部
- 内容区底部放 "Previous / Next" 翻页导航
- 滚动时吸附（不随页面滚走）

### 博客分类侧边栏

```
Categories
  ├── SEO (24)
  ├── CRO (18)
  ├── Content (15)
  ├── Paid Ads (12)
  └── Analytics (9)

Popular Posts
  ├── How to Improve SEO
  ├── Landing Page Guide
  └── Analytics Setup

Newsletter
  └── [Email signup form]
```

---

## 面包屑

### 标准格式

```
Home > Features > Analytics
Home > Blog > SEO Category > How to Do Keyword Research
Home > Docs > API Reference > Authentication
```

规则：
- 分隔符：`>` 或 `/`（保持一致）
- 除当前页面外，每一段都是链接
- 当前页面用纯文本（不加链接）
- 若标题已作为 H1 显示，就不要再列当前页面

### 带 Schema 标记

```html
<nav aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/"><span itemprop="name">Home</span></a>
      <meta itemprop="position" content="1" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/features"><span itemprop="name">Features</span></a>
      <meta itemprop="position" content="2" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name">Analytics</span>
      <meta itemprop="position" content="3" />
    </li>
  </ol>
</nav>
```

或者用 JSON-LD（推荐）：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/" },
    { "@type": "ListItem", "position": 2, "name": "Features", "item": "https://example.com/features" },
    { "@type": "ListItem", "position": 3, "name": "Analytics" }
  ]
}
```

---

## 移动端导航

### 汉堡菜单

移动端标准做法。所有导航项收进一个菜单图标。

规则：
- 汉堡图标（三条线）放右上或左上
- 全屏或侧滑面板
- 不打开菜单也能看到 CTA 按钮（吸附头部）
- 移动端菜单里能进搜索
- 嵌套项用手风琴模式

### 底部标签栏

适用：Web 应用、PWA、移动优先产品。

```
┌──────────────────────────────────────┐
│                                      │
│           [Page Content]             │
│                                      │
├──────────────────────────────────────┤
│  Home    Search    Create    Profile │
│   🏠       🔍        ➕       👤    │
└──────────────────────────────────────┘
```

规则：
- 最多 3-5 项
- 图标 + 文字（不能只有图标）
- 明确标出选中态
- 最重要的操作放中间

---

## 反模式

### 应避免的做法

- **头部项目过多**（8 项以上）：引发决策瘫痪，小屏上导航难以阅读
- **下拉套娃**：下拉里再套下拉，层层嵌套
- **看不懂的图标**：图标不带文字说明，用户不知道它代表什么
- **隐藏主导航**：桌面端把重要页面埋进汉堡菜单
- **各页导航不一致**：全站导航应完全一致（应用与营销站除外）
- **不考虑移动端**：桌面导航无法迁移到移动端
- **页脚当站点地图倾倒场**：50 多个链接堆在页脚，毫无组织
- **面包屑与 URL 不符**：面包屑写 "Products > Widget"，URL 却是 `/shop/widget-pro`

### 常见修法

| 问题 | 修法 |
|---------|-----|
| 导航项过多 | 收进下拉菜单或巨型菜单 |
| 用户找不到页面 | 加搜索，改进标签措辞 |
| 导航导致高跳出 | 精简选项，标签写得更清楚 |
| SEO 页面没有入口链接 | 加进页脚或资源板块 |
| 移动端导航失效 | 用真机测试，采用汉堡菜单模式 |

---

## 面向 SEO 的导航

导航里的内链会传递 PageRank。要有策略地用：

- **头部导航链接权重最高**，把最重要的页面放这里
- **页脚链接传递的权重较低**，但仍有用，适合对比页、地区页
- **侧边栏链接**有助于板块级权威，适合博客分类、文档分区
- **面包屑**向搜索引擎给出结构信号，配合 schema 标记实现
- **别用纯 JavaScript 导航**，搜索引擎需要可抓取的 HTML 链接
- **锚文本要具体**，写 "Analytics Features"，别只写 "Features"
