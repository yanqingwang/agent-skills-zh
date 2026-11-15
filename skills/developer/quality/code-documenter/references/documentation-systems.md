> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/code-documenter/references/documentation-systems.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 文档系统与基础设施

## 静态站点生成器

### Docusaurus（Meta）

```bash
# Setup
npx create-docusaurus@latest docs classic
cd docs && npm start

# Structure
docs/
├── docs/           # Documentation pages
├── blog/           # Blog posts
├── src/
│   └── pages/      # Custom pages
└── docusaurus.config.js
```

**docusaurus.config.js：**
```javascript
module.exports = {
  title: 'My API',
  tagline: 'Build amazing things',
  url: 'https://docs.example.com',
  baseUrl: '/',

  themeConfig: {
    navbar: {
      items: [
        {to: '/docs/intro', label: 'Docs', position: 'left'},
        {to: '/api', label: 'API', position: 'left'},
      ],
    },

    // Algolia search
    algolia: {
      apiKey: '<algolia-search-api-key>',
      indexName: 'your_index',
      contextualSearch: true,
    },

    prism: {
      theme: lightCodeTheme,
      darkTheme: darkCodeTheme,
      additionalLanguages: ['python', 'rust'],
    },
  },
};
```

### MkDocs（Python）

```yaml
# mkdocs.yml
site_name: My API Documentation
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate
    - search.suggest
    - search.highlight
  palette:
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: true
  - git-revision-date-localized

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - admonition
  - codehilite

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - API Reference: api/
```

### VitePress（Vue）

```typescript
// .vitepress/config.ts
export default defineConfig({
  title: 'API Docs',
  description: 'Developer documentation',

  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/' },
      { text: 'API', link: '/api/' },
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Introduction',
          items: [
            { text: 'Getting Started', link: '/guide/getting-started' },
            { text: 'Configuration', link: '/guide/config' },
          ],
        },
      ],
    },

    search: {
      provider: 'local',
    },

    editLink: {
      pattern: 'https://github.com/user/repo/edit/main/docs/:path',
    },
  },
});
```

## 多版本文档

### 版本切换器

```javascript
// Docusaurus versions
{
  versions: {
    current: {
      label: '2.0 (Next)',
      path: 'next',
    },
  },
  onlyIncludeVersions: ['current', '1.5', '1.4'],
}
```

### 迁移指南

```markdown
# Migration Guide: v1 to v2

## Breaking Changes

### Authentication
**v1:**
```python
client.authenticate(api_key)
```

**v2:**
```python
client = Client(api_key=api_key)  # Pass in constructor
```

### Renamed Methods
| v1 | v2 | Notes |
|----|----|----- |
| `get_user()` | `fetch_user()` | Async now |
| `delete_user()` | `remove_user()` | Returns Promise |

## Deprecation Timeline
- v1.x: Supported until Dec 2025
- v2.0: Released Jan 2025
- v2.1: Current (June 2025)
```

## 搜索实现

### Algolia DocSearch

```html
<!-- Add to theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3" />

<script src="https://cdn.jsdelivr.net/npm/@docsearch/js@3"></script>
<script>
  docsearch({
    appId: '<algolia-app-id>',
    apiKey: '<algolia-search-api-key>',
    indexName: 'your_index',
    container: '#docsearch',
  });
</script>
```

### 本地搜索（Lunr.js）

```javascript
const idx = lunr(function() {
  this.ref('id');
  this.field('title', { boost: 10 });
  this.field('content');

  documents.forEach(doc => this.add(doc));
});

// Search
const results = idx.search('authentication');
```

## 文档测试

### 链接检查

```bash
# linkcheck (Python)
pip install linkchecker
linkchecker http://localhost:3000/docs

# broken-link-checker (Node)
npm install -g broken-link-checker
blc http://localhost:3000 -ro
```

### 代码示例测试

```python
# doctest for Python examples
"""
>>> add(2, 3)
5
>>> add(-1, 1)
0
"""

# Run tests
python -m doctest -v docs/*.md
```

```javascript
// Jest for TypeScript examples
// Extract code blocks and test
import { runExamples } from './test-docs';

test('API examples work', async () => {
  const examples = extractExamples('./docs/api.md');
  await expect(runExamples(examples)).resolves.toBeTruthy();
});
```

## 性能优化

### 构建优化

```javascript
// Webpack/Vite config
export default {
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor': ['react', 'react-dom'],
        },
      },
    },
  },

  optimizeDeps: {
    include: ['prismjs'],
  },
};
```

### CDN 与缓存

```nginx
# nginx.conf
location /docs {
  expires 1y;
  add_header Cache-Control "public, immutable";
}

location ~* \.(html)$ {
  expires 1h;
  add_header Cache-Control "public, must-revalidate";
}
```

## 分析集成

### Google Analytics

```javascript
// Docusaurus
gtag: {
  trackingID: 'G-XXXXXXXXXX',
  anonymizeIP: true,
},
```

### 自定义分析

```javascript
// Track search queries
function trackSearch(query, results) {
  analytics.track('docs_search', {
    query,
    resultCount: results.length,
    timestamp: new Date(),
  });
}
```

## 速查表

| 工具 | 适用场景 | 技术栈 |
|------|----------|-----------|
| Docusaurus | React 项目、版本管理 | React, MDX |
| MkDocs | Python 项目、搭建简单 | Python, Jinja2 |
| VitePress | Vue 项目、构建快 | Vue, Vite |
| Nextra | 集成 Next.js | React, Next.js |
| Mintlify | 现代界面、AI 搜索 | React |

| 搜索方案 | 成本 | 特性 |
|----------------|------|----------|
| Algolia DocSearch | 免费（开源项目） | 快，容忍拼写错误 |
| 本地（Lunr.js） | 免费 | 离线，无需服务端 |
| Typesense | 免费（自托管） | 注重隐私 |
| Meilisearch | 免费（自托管） | 快，相关性好 |
