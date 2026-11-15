> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-javascript/COMMON_PATTERNS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 常用模式：JavaScript Code 节点

经过生产环境验证的 n8n Code 节点模式。这些模式已在真实工作流中得到检验。

> **Native first.** 下面每个模式都以能完成同样工作的原生节点开头。只有当任务通过了 SKILL.md 中的闸门
> （没有原生节点适用，且它在封闭清单上）时才使用 Code 版本，并给节点加一条 `Why Code:` 备注。
> `using-n8n-mcp-skills` 中的 job-to-node 对照表列出了这些原生节点。

---

## 概览

本指南覆盖 n8n 工作流中最有用的 10 个 Code 节点模式。每个模式包含：
- **适用场景**：何时使用本模式
- **关键技术**：所演示的重要编码技术
- **完整示例**：可改造使用的可运行代码
- **变体**：常见的修改方式

**模式分类：**
- 数据聚合（Pattern 1、5、10）
- 内容处理（Pattern 2、3）
- 数据校验与比较（Pattern 4）
- 数据转换（Pattern 5、6、7）
- 输出格式化（Pattern 8）
- 过滤与排名（Pattern 9）

---

## Pattern 1：多来源数据聚合

> **Native first:** Merge（`append`，或在共享键上用 `combineByFields`）负责连接多个来源；Edit Fields 让每个来源变成相同的形状。当各来源的形状差异太大、单个 Merge 处理不了时，才使用本模式。

**适用场景**：合并来自多个 API、RSS 源、webhook 或数据库的数据

**何时使用：**
- 从多个服务收集数据
- 归一化不同的 API 响应格式
- 把多个数据源合并成统一结构
- 构建聚合报告

**关键技术**：循环迭代、条件解析、数据归一化

### 完整示例

```javascript
// Process and structure data collected from multiple sources
const allItems = $input.all();
let processedArticles = [];

// Handle different source formats
for (const item of allItems) {
  const sourceName = item.json.name || 'Unknown';
  const sourceData = item.json;

  // Parse source-specific structure - Hacker News format
  if (sourceName === 'Hacker News' && sourceData.hits) {
    for (const hit of sourceData.hits) {
      processedArticles.push({
        title: hit.title,
        url: hit.url,
        summary: hit.story_text || 'No summary',
        source: 'Hacker News',
        score: hit.points || 0,
        fetchedAt: new Date().toISOString()
      });
    }
  }

  // Parse source-specific structure - Reddit format
  else if (sourceName === 'Reddit' && sourceData.data?.children) {
    for (const post of sourceData.data.children) {
      processedArticles.push({
        title: post.data.title,
        url: post.data.url,
        summary: post.data.selftext || 'No summary',
        source: 'Reddit',
        score: post.data.score || 0,
        fetchedAt: new Date().toISOString()
      });
    }
  }

  // Parse source-specific structure - RSS feed format
  else if (sourceName === 'RSS' && sourceData.items) {
    for (const rssItem of sourceData.items) {
      processedArticles.push({
        title: rssItem.title,
        url: rssItem.link,
        summary: rssItem.description || 'No summary',
        source: 'RSS Feed',
        score: 0,
        fetchedAt: new Date().toISOString()
      });
    }
  }
}

// Sort by score (highest first)
processedArticles.sort((a, b) => b.score - a.score);

return processedArticles.map(article => ({json: article}));
```

### 变体

```javascript
// Variation 1: Add source weighting
for (const article of processedArticles) {
  const weights = {
    'Hacker News': 1.5,
    'Reddit': 1.0,
    'RSS Feed': 0.8
  };

  article.weightedScore = article.score * (weights[article.source] || 1.0);
}

// Variation 2: Filter by minimum score
processedArticles = processedArticles.filter(article => article.score >= 10);

// Variation 3: Deduplicate by URL
const seen = new Set();
processedArticles = processedArticles.filter(article => {
  if (seen.has(article.url)) {
    return false;
  }
  seen.add(article.url);
  return true;
});
```

---

## Pattern 2：正则过滤与模式匹配

> **Native first:** 用 Filter 或 IF 条件配合 `regex` / `contains` 字符串运算符，即可保留或分流匹配的条目。当需要在每个条目内统计或提取大量匹配时，使用本模式。

**适用场景**：内容分析、关键词提取、提及追踪、文本解析

**何时使用：**
- 从文本中提取提及或标签
- 在非结构化数据中查找模式
- 统计关键词出现次数
- 校验格式（邮箱、电话号码）

**关键技术**：正则匹配、对象聚合、排序/排名

### 完整示例

```javascript
// Extract and track mentions using regex patterns
const etfPattern = /\b([A-Z]{2,5})\b/g;
const knownETFs = ['VOO', 'VTI', 'VT', 'SCHD', 'QYLD', 'VXUS', 'SPY', 'QQQ'];

const etfMentions = {};

for (const item of $input.all()) {
  const data = item.json.data;

  // Skip if no data or children
  if (!data?.children) continue;

  for (const post of data.children) {
    // Combine title and body text
    const title = post.data.title || '';
    const body = post.data.selftext || '';
    const combinedText = (title + ' ' + body).toUpperCase();

    // Find all matches
    const matches = combinedText.match(etfPattern);

    if (matches) {
      for (const match of matches) {
        // Only count known ETFs
        if (knownETFs.includes(match)) {
          if (!etfMentions[match]) {
            etfMentions[match] = {
              count: 0,
              totalScore: 0,
              posts: []
            };
          }

          etfMentions[match].count++;
          etfMentions[match].totalScore += post.data.score || 0;
          etfMentions[match].posts.push({
            title: post.data.title,
            url: post.data.url,
            score: post.data.score
          });
        }
      }
    }
  }
}

// Convert to array and sort by mention count
return Object.entries(etfMentions)
  .map(([etf, data]) => ({
    json: {
      etf,
      mentions: data.count,
      totalScore: data.totalScore,
      averageScore: data.totalScore / data.count,
      topPosts: data.posts
        .sort((a, b) => b.score - a.score)
        .slice(0, 3)
    }
  }))
  .sort((a, b) => b.json.mentions - a.json.mentions);
```

### 变体

```javascript
// Variation 1: Email extraction
const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;
const emails = text.match(emailPattern) || [];

// Variation 2: Phone number extraction
const phonePattern = /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g;
const phones = text.match(phonePattern) || [];

// Variation 3: Hashtag extraction
const hashtagPattern = /#(\w+)/g;
const hashtags = [];
let match;
while ((match = hashtagPattern.exec(text)) !== null) {
  hashtags.push(match[1]);
}

// Variation 4: URL extraction
const urlPattern = /https?:\/\/[^\s]+/g;
const urls = text.match(urlPattern) || [];
```

---

## Pattern 3：Markdown 解析与结构化数据提取

> **Native first:** Markdown 节点（转 HTML）+ HTML 节点用 CSS 选择器做 `extractHtmlContent`；CSV / XLSX / PDF 用 Extract From File。本模式只用于没有任何节点能解析的自由格式文本（属于解析例外）。

**适用场景**：解析格式化文本、提取结构化字段、内容转换

**何时使用：**
- 解析 markdown 或 HTML
- 从结构化文本中提取数据
- 把格式化内容转成 JSON
- 处理文档或文章

**关键技术**：正则分组、辅助函数、数据归一化、用 while 循环迭代

### 完整示例

```javascript
// Parse markdown and extract structured information
const markdown = $input.first().json.data.markdown;
const adRegex = /##\s*(.*?)\n(.*?)(?=\n##|\n---|$)/gs;

const ads = [];
let match;

// Helper function to parse time strings to minutes
function parseTimeToMinutes(timeStr) {
  if (!timeStr) return 999999;  // Sort unparseable times last

  const hourMatch = timeStr.match(/(\d+)\s*hour/);
  const dayMatch = timeStr.match(/(\d+)\s*day/);
  const minMatch = timeStr.match(/(\d+)\s*min/);

  let totalMinutes = 0;
  if (dayMatch) totalMinutes += parseInt(dayMatch[1]) * 1440;  // 24 * 60
  if (hourMatch) totalMinutes += parseInt(hourMatch[1]) * 60;
  if (minMatch) totalMinutes += parseInt(minMatch[1]);

  return totalMinutes;
}

// Extract all job postings from markdown
while ((match = adRegex.exec(markdown)) !== null) {
  const title = match[1]?.trim() || 'No title';
  const content = match[2]?.trim() || '';

  // Extract structured fields from content
  const districtMatch = content.match(/\*\*District:\*\*\s*(.*?)(?:\n|$)/);
  const salaryMatch = content.match(/\*\*Salary:\*\*\s*(.*?)(?:\n|$)/);
  const timeMatch = content.match(/Posted:\s*(.*?)\*/);

  ads.push({
    title: title,
    district: districtMatch?.[1].trim() || 'Unknown',
    salary: salaryMatch?.[1].trim() || 'Not specified',
    postedTimeAgo: timeMatch?.[1] || 'Unknown',
    timeInMinutes: parseTimeToMinutes(timeMatch?.[1]),
    fullContent: content,
    extractedAt: new Date().toISOString()
  });
}

// Sort by recency (posted time)
ads.sort((a, b) => a.timeInMinutes - b.timeInMinutes);

return ads.map(ad => ({json: ad}));
```

### 变体

```javascript
// Variation 1: Parse HTML table to JSON
const tableRegex = /<tr>(.*?)<\/tr>/gs;
const cellRegex = /<td>(.*?)<\/td>/g;

const rows = [];
let tableMatch;

while ((tableMatch = tableRegex.exec(htmlTable)) !== null) {
  const cells = [];
  let cellMatch;

  while ((cellMatch = cellRegex.exec(tableMatch[1])) !== null) {
    cells.push(cellMatch[1].trim());
  }

  if (cells.length > 0) {
    rows.push(cells);
  }
}

// Variation 2: Extract code blocks from markdown
const codeBlockRegex = /```(\w+)?\n(.*?)```/gs;
const codeBlocks = [];

while ((match = codeBlockRegex.exec(markdown)) !== null) {
  codeBlocks.push({
    language: match[1] || 'plain',
    code: match[2].trim()
  });
}

// Variation 3: Parse YAML frontmatter
const frontmatterRegex = /^---\n(.*?)\n---/s;
const frontmatterMatch = content.match(frontmatterRegex);

if (frontmatterMatch) {
  const yamlLines = frontmatterMatch[1].split('\n');
  const metadata = {};

  for (const line of yamlLines) {
    const [key, ...valueParts] = line.split(':');
    if (key && valueParts.length > 0) {
      metadata[key.trim()] = valueParts.join(':').trim();
    }
  }
}
```

---

## Pattern 4：JSON 比较与校验

> **Native first:** Compare Datasets（输出：in A only / same / different / in B only）按一个键对比两个列表。要在同一对对象内部做深度差异比较时，使用本模式。

**适用场景**：工作流版本管理、配置校验、变更检测、数据完整性

**何时使用：**
- 比较数据的两个版本
- 检测配置中的变更
- 校验数据一致性
- 检查差异

**关键技术**：JSON 键排序、base64 解码、深度比较、对象操作

### 完整示例

```javascript
// Compare and validate JSON objects from different sources
const orderJsonKeys = (jsonObj) => {
  const ordered = {};
  Object.keys(jsonObj).sort().forEach(key => {
    ordered[key] = jsonObj[key];
  });
  return ordered;
};

const allItems = $input.all();

// Assume first item is base64-encoded original, second is current
const origWorkflow = JSON.parse(
  Buffer.from(allItems[0].json.content, 'base64').toString()
);
const currentWorkflow = allItems[1].json;

// Order keys for consistent comparison
const orderedOriginal = orderJsonKeys(origWorkflow);
const orderedCurrent = orderJsonKeys(currentWorkflow);

// Deep comparison
const isSame = JSON.stringify(orderedOriginal) === JSON.stringify(orderedCurrent);

// Find differences
const differences = [];
for (const key of Object.keys(orderedOriginal)) {
  if (JSON.stringify(orderedOriginal[key]) !== JSON.stringify(orderedCurrent[key])) {
    differences.push({
      field: key,
      original: orderedOriginal[key],
      current: orderedCurrent[key]
    });
  }
}

// Check for new keys
for (const key of Object.keys(orderedCurrent)) {
  if (!(key in orderedOriginal)) {
    differences.push({
      field: key,
      original: null,
      current: orderedCurrent[key],
      status: 'new'
    });
  }
}

return [{
  json: {
    identical: isSame,
    differenceCount: differences.length,
    differences: differences,
    original: orderedOriginal,
    current: orderedCurrent,
    comparedAt: new Date().toISOString()
  }
}];
```

### 变体

```javascript
// Variation 1: Simple equality check
const isEqual = JSON.stringify(obj1) === JSON.stringify(obj2);

// Variation 2: Deep diff with detailed changes
function deepDiff(obj1, obj2, path = '') {
  const changes = [];

  for (const key in obj1) {
    const currentPath = path ? `${path}.${key}` : key;

    if (!(key in obj2)) {
      changes.push({type: 'removed', path: currentPath, value: obj1[key]});
    } else if (typeof obj1[key] === 'object' && typeof obj2[key] === 'object') {
      changes.push(...deepDiff(obj1[key], obj2[key], currentPath));
    } else if (obj1[key] !== obj2[key]) {
      changes.push({
        type: 'modified',
        path: currentPath,
        from: obj1[key],
        to: obj2[key]
      });
    }
  }

  for (const key in obj2) {
    if (!(key in obj1)) {
      const currentPath = path ? `${path}.${key}` : key;
      changes.push({type: 'added', path: currentPath, value: obj2[key]});
    }
  }

  return changes;
}

// Variation 3: Schema validation
function validateSchema(data, schema) {
  const errors = [];

  for (const field of schema.required || []) {
    if (!(field in data)) {
      errors.push(`Missing required field: ${field}`);
    }
  }

  for (const [field, type] of Object.entries(schema.types || {})) {
    if (field in data && typeof data[field] !== type) {
      errors.push(`Field ${field} should be ${type}, got ${typeof data[field]}`);
    }
  }

  return {
    valid: errors.length === 0,
    errors
  };
}
```

---

## Pattern 5：CRM 数据转换

> **Native first:** Edit Fields 配合短表达式就能把表单映射成 CRM 所需的形状；CRM 节点自身的字段槽位也能直接完成映射。只有当映射需要循环、或每个字段需要多条语句时，才使用本模式。

**适用场景**：线索数据补全、数据归一化、API 准备、表单数据处理

**何时使用：**
- 处理表单提交
- 为 CRM API 准备数据
- 归一化联系人信息
- 补全线索数据

**关键技术**：对象解构、数据映射、格式转换、字段拆分

### 完整示例

```javascript
// Transform form data into CRM-compatible format
const item = $input.all()[0];
const {
  name,
  email,
  phone,
  company,
  course_interest,
  message,
  timestamp
} = item.json;

// Split name into first and last
const nameParts = name.split(' ');
const firstName = nameParts[0] || '';
const lastName = nameParts.slice(1).join(' ') || 'Unknown';

// Format phone number
const cleanPhone = phone.replace(/[^\d]/g, '');  // Remove non-digits

// Build CRM data structure
const crmData = {
  data: {
    type: 'Contact',
    attributes: {
      first_name: firstName,
      last_name: lastName,
      email1: email,
      phone_work: cleanPhone,
      account_name: company,
      description: `Course Interest: ${course_interest}\n\nMessage: ${message}\n\nSubmitted: ${timestamp}`,
      lead_source: 'Website Form',
      status: 'New'
    }
  },
  metadata: {
    original_submission: timestamp,
    processed_at: new Date().toISOString()
  }
};

return [{
  json: {
    ...item.json,
    crmData,
    processed: true
  }
}];
```

### 变体

```javascript
// Variation 1: Multiple contact processing
const contacts = $input.all();

return contacts.map(item => {
  const data = item.json;
  const [firstName, ...lastNameParts] = data.name.split(' ');

  return {
    json: {
      firstName,
      lastName: lastNameParts.join(' ') || 'Unknown',
      email: data.email.toLowerCase(),
      phone: data.phone.replace(/[^\d]/g, ''),
      tags: [data.source, data.interest_level].filter(Boolean)
    }
  };
});

// Variation 2: Field validation and normalization
function normalizePContact(raw) {
  return {
    first_name: raw.firstName?.trim() || '',
    last_name: raw.lastName?.trim() || 'Unknown',
    email: raw.email?.toLowerCase().trim() || '',
    phone: raw.phone?.replace(/[^\d]/g, '') || '',
    company: raw.company?.trim() || 'Unknown',
    title: raw.title?.trim() || '',
    valid: Boolean(raw.email && raw.firstName)
  };
}

// Variation 3: Lead scoring
function calculateLeadScore(data) {
  let score = 0;

  if (data.email) score += 10;
  if (data.phone) score += 10;
  if (data.company) score += 15;
  if (data.title?.toLowerCase().includes('director')) score += 20;
  if (data.title?.toLowerCase().includes('manager')) score += 15;
  if (data.message?.length > 100) score += 10;

  return score;
}
```

---

## Pattern 6：Release 信息处理

> **Native first:** GitHub 节点负责抓取 releases；Sort + Limit 挑出最新的；Edit Fields 给它们整形。需要做 semver 比较或解析 changelog 时，使用本模式。

**适用场景**：版本管理、changelog 解析、发布说明生成、GitHub API 处理

**何时使用：**
- 处理 GitHub releases
- 过滤稳定版本
- 生成 changelog 摘要
- 提取版本信息

**关键技术**：数组过滤、条件字段提取、日期格式化、字符串操作

### 完整示例

```javascript
// Extract and filter stable releases from GitHub API
const allReleases = $input.first().json;

const stableReleases = allReleases
  .filter(release => !release.prerelease && !release.draft)
  .slice(0, 10)
  .map(release => {
    // Extract highlights section from changelog
    const body = release.body || '';
    let highlights = 'No highlights available';

    if (body.includes('## Highlights:')) {
      highlights = body.split('## Highlights:')[1]?.split('##')[0]?.trim();
    } else {
      // Fallback to first 500 chars
      highlights = body.substring(0, 500) + '...';
    }

    return {
      tag: release.tag_name,
      name: release.name,
      published: release.published_at,
      publishedDate: new Date(release.published_at).toLocaleDateString(),
      author: release.author.login,
      url: release.html_url,
      changelog: body,
      highlights: highlights,
      assetCount: release.assets.length,
      assets: release.assets.map(asset => ({
        name: asset.name,
        size: asset.size,
        downloadCount: asset.download_count,
        downloadUrl: asset.browser_download_url
      }))
    };
  });

return stableReleases.map(release => ({json: release}));
```

### 变体

```javascript
// Variation 1: Version comparison
function compareVersions(v1, v2) {
  const parts1 = v1.replace('v', '').split('.').map(Number);
  const parts2 = v2.replace('v', '').split('.').map(Number);

  for (let i = 0; i < Math.max(parts1.length, parts2.length); i++) {
    const num1 = parts1[i] || 0;
    const num2 = parts2[i] || 0;

    if (num1 > num2) return 1;
    if (num1 < num2) return -1;
  }

  return 0;
}

// Variation 2: Breaking change detection
function hasBreakingChanges(changelog) {
  const breakingKeywords = [
    'BREAKING CHANGE',
    'breaking change',
    'BC:',
    '💥'
  ];

  return breakingKeywords.some(keyword => changelog.includes(keyword));
}

// Variation 3: Extract version numbers
const versionPattern = /v?(\d+)\.(\d+)\.(\d+)/;
const match = tagName.match(versionPattern);

if (match) {
  const [_, major, minor, patch] = match;
  const version = {major: parseInt(major), minor: parseInt(minor), patch: parseInt(patch)};
}
```

---

## Pattern 7：带上下文的数组转换

> **Native first:** 这通常就是 Edit Fields 能做的事：计算字段用短表达式（`{{ $json.price * $json.qty }}`），数组场景在外面配合 Split Out / Aggregate。只有当字段需要多语句逻辑时才用 Code。

**适用场景**：快速数据转换、字段映射、添加计算字段

**何时使用：**
- 带附加上下文转换数组
- 添加计算字段
- 简化复杂对象
- 单复数处理逻辑

**关键技术**：数组方法链式调用、三元运算符、计算属性

### 完整示例

```javascript
// Transform releases with contextual information
const releases = $input.first().json
  .filter(release => !release.prerelease && !release.draft)
  .slice(0, 10)
  .map(release => ({
    version: release.tag_name,
    assetCount: release.assets.length,
    assetsCountText: release.assets.length === 1 ? 'file' : 'files',
    downloadUrl: release.html_url,
    isRecent: new Date(release.published_at) > new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
    age: Math.floor((Date.now() - new Date(release.published_at)) / (24 * 60 * 60 * 1000)),
    ageText: `${Math.floor((Date.now() - new Date(release.published_at)) / (24 * 60 * 60 * 1000))} days ago`
  }));

return releases.map(release => ({json: release}));
```

### 变体

```javascript
// Variation 1: Add ranking
const items = $input.all()
  .sort((a, b) => b.json.score - a.json.score)
  .map((item, index) => ({
    json: {
      ...item.json,
      rank: index + 1,
      medal: index < 3 ? ['🥇', '🥈', '🥉'][index] : ''
    }
  }));

// Variation 2: Add percentage calculations
const total = $input.all().reduce((sum, item) => sum + item.json.value, 0);

const itemsWithPercentage = $input.all().map(item => ({
  json: {
    ...item.json,
    percentage: ((item.json.value / total) * 100).toFixed(2) + '%'
  }
}));

// Variation 3: Add category labels
const categorize = (value) => {
  if (value > 100) return 'High';
  if (value > 50) return 'Medium';
  return 'Low';
};

const categorized = $input.all().map(item => ({
  json: {
    ...item.json,
    category: categorize(item.json.value)
  }
}));
```

---

## Pattern 8：Slack Block Kit 格式化

> **Native first:** Slack 节点可以在其 Blocks 字段里用表达式传入 blocks（`={{ { "blocks": [...] } }}`，参见 n8n-node-configuration 中的 NODE_FAMILY_GOTCHAS.md）。只有当 blocks 的数量取决于对数据的循环时，才在 Code 里构建。

**适用场景**：聊天通知、富文本消息格式化、交互式消息

**何时使用：**
- 发送格式化的 Slack 消息
- 创建交互式通知
- 为聊天平台构建富内容
- 状态报告与告警

**关键技术**：模板字符串、嵌套对象、Block Kit 语法、日期格式化

### 完整示例

```javascript
// Create Slack-formatted message with structured blocks
const date = new Date().toISOString().split('T')[0];
const data = $input.first().json;

return [{
  json: {
    text: `Daily Report - ${date}`,  // Fallback text
    blocks: [
      {
        type: "header",
        text: {
          type: "plain_text",
          text: `📊 Daily Security Report - ${date}`
        }
      },
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*Status:* ${data.status === 'ok' ? '✅ All Clear' : '⚠️ Issues Detected'}\n*Alerts:* ${data.alertCount || 0}\n*Updated:* ${new Date().toLocaleString()}`
        }
      },
      {
        type: "divider"
      },
      {
        type: "section",
        fields: [
          {
            type: "mrkdwn",
            text: `*Failed Logins:*\n${data.failedLogins || 0}`
          },
          {
            type: "mrkdwn",
            text: `*API Errors:*\n${data.apiErrors || 0}`
          },
          {
            type: "mrkdwn",
            text: `*Uptime:*\n${data.uptime || '100%'}`
          },
          {
            type: "mrkdwn",
            text: `*Response Time:*\n${data.avgResponseTime || 'N/A'}ms`
          }
        ]
      },
      {
        type: "context",
        elements: [{
          type: "mrkdwn",
          text: `Report generated automatically by n8n workflow`
        }]
      }
    ]
  }
}];
```

### 变体

```javascript
// Variation 1: Interactive buttons
const blocksWithButtons = [
  {
    type: "section",
    text: {
      type: "mrkdwn",
      text: "Would you like to approve this request?"
    },
    accessory: {
      type: "button",
      text: {
        type: "plain_text",
        text: "Approve"
      },
      style: "primary",
      value: "approve",
      action_id: "approve_button"
    }
  }
];

// Variation 2: List formatting
const items = ['Item 1', 'Item 2', 'Item 3'];
const formattedList = items.map((item, i) => `${i + 1}. ${item}`).join('\n');

// Variation 3: Status indicators
function getStatusEmoji(status) {
  const statusMap = {
    'success': '✅',
    'warning': '⚠️',
    'error': '❌',
    'info': 'ℹ️'
  };

  return statusMap[status] || '•';
}

// Variation 4: Truncate long messages
function truncate(text, maxLength = 3000) {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength - 3) + '...';
}
```

---

## Pattern 9：Top N 过滤与排名

> **Native first:** Filter（设阈值）→ Sort（按分数降序）→ Limit（取 N 条）。当分数本身需要多步计算时，使用本模式。

**适用场景**：RAG 管道、排名算法、结果过滤、排行榜

**何时使用：**
- 按分数获取前几名结果
- 过滤表现最好/最差的条目
- 构建排行榜
- 相关性排名

**关键技术**：排序、切片、空值合并、分数计算

### 完整示例

```javascript
// Filter and rank by similarity score, return top results
const ragResponse = $input.item.json;
const chunks = ragResponse.chunks || [];

// Sort by similarity (highest first)
const topChunks = chunks
  .sort((a, b) => (b.similarity || 0) - (a.similarity || 0))
  .slice(0, 6);

return [{
  json: {
    query: ragResponse.query,
    topChunks: topChunks,
    count: topChunks.length,
    maxSimilarity: topChunks[0]?.similarity || 0,
    minSimilarity: topChunks[topChunks.length - 1]?.similarity || 0,
    averageSimilarity: topChunks.reduce((sum, chunk) => sum + (chunk.similarity || 0), 0) / topChunks.length
  }
}];
```

### 变体

```javascript
// Variation 1: Top N with minimum threshold
const threshold = 0.7;
const topItems = $input.all()
  .filter(item => item.json.score >= threshold)
  .sort((a, b) => b.json.score - a.json.score)
  .slice(0, 10);

// Variation 2: Bottom N (worst performers)
const bottomItems = $input.all()
  .sort((a, b) => a.json.score - b.json.score)  // Ascending
  .slice(0, 5);

// Variation 3: Top N by multiple criteria
const ranked = $input.all()
  .map(item => ({
    ...item,
    compositeScore: (item.json.relevance * 0.6) + (item.json.recency * 0.4)
  }))
  .sort((a, b) => b.compositeScore - a.compositeScore)
  .slice(0, 10);

// Variation 4: Percentile filtering
const allScores = $input.all().map(item => item.json.score).sort((a, b) => b - a);
const percentile95 = allScores[Math.floor(allScores.length * 0.05)];

const topPercentile = $input.all().filter(item => item.json.score >= percentile95);
```

---

## Pattern 10：字符串聚合与报告

> **Native first:** 用 Summarize 节点的 `concatenate`（按分组）或 Aggregate 节点完成聚合，再在消息字段里放一个带 `.join('\n')` 的表达式。需要带循环、分多个章节的报告时，使用本模式。

**适用场景**：报告生成、日志聚合、内容拼接、摘要创建

**何时使用：**
- 合并多个文本输出
- 从数据生成报告
- 聚合日志或消息
- 创建格式化摘要

**关键技术**：数组合并、字符串拼接、模板字符串、时间戳处理

### 完整示例

```javascript
// Aggregate multiple text inputs into formatted report
const allItems = $input.all();

// Collect all messages
const messages = allItems.map(item => item.json.message);

// Build report
const header = `🎯 **Daily Summary Report**\n📅 ${new Date().toLocaleString()}\n📊 Total Items: ${messages.length}\n\n`;
const divider = '\n\n---\n\n';
const footer = `\n\n---\n\n✅ Report generated at ${new Date().toISOString()}`;

const finalReport = header + messages.join(divider) + footer;

return [{
  json: {
    report: finalReport,
    messageCount: messages.length,
    generatedAt: new Date().toISOString(),
    reportLength: finalReport.length
  }
}];
```

### 变体

```javascript
// Variation 1: Numbered list
const numberedReport = allItems
  .map((item, index) => `${index + 1}. ${item.json.title}\n   ${item.json.description}`)
  .join('\n\n');

// Variation 2: Markdown table
const headers = '| Name | Status | Score |\n|------|--------|-------|\n';
const rows = allItems
  .map(item => `| ${item.json.name} | ${item.json.status} | ${item.json.score} |`)
  .join('\n');

const table = headers + rows;

// Variation 3: HTML report
const htmlReport = `
<!DOCTYPE html>
<html>
<head><title>Report</title></head>
<body>
  <h1>Report - ${new Date().toLocaleDateString()}</h1>
  <ul>
    ${allItems.map(item => `<li>${item.json.title}: ${item.json.value}</li>`).join('\n    ')}
  </ul>
</body>
</html>
`;

// Variation 4: JSON summary
const summary = {
  generated: new Date().toISOString(),
  totalItems: allItems.length,
  items: allItems.map(item => item.json),
  statistics: {
    total: allItems.reduce((sum, item) => sum + (item.json.value || 0), 0),
    average: allItems.reduce((sum, item) => sum + (item.json.value || 0), 0) / allItems.length,
    max: Math.max(...allItems.map(item => item.json.value || 0)),
    min: Math.min(...allItems.map(item => item.json.value || 0))
  }
};
```

---

## 如何选择合适的模式

### 模式选择指南

| 你的目标 | 使用模式 |
|-----------|-------------|
| 合并多个 API 响应 | Pattern 1（多来源聚合） |
| 提取提及或关键词 | Pattern 2（正则过滤） |
| 解析格式化文本 | Pattern 3（Markdown 解析） |
| 检测数据中的变更 | Pattern 4（JSON 比较） |
| 为 CRM 准备表单数据 | Pattern 5（CRM 转换） |
| 处理 GitHub releases | Pattern 6（Release 处理） |
| 添加计算字段 | Pattern 7（数组转换） |
| 格式化 Slack 消息 | Pattern 8（Block Kit 格式化） |
| 获取前几名结果 | Pattern 9（Top N 过滤） |
| 创建文本报告 | Pattern 10（字符串聚合） |

### 组合多个模式

很多真实工作流会组合多个模式：

```javascript
// Example: Multi-source aggregation + Top N filtering
const allItems = $input.all();
const aggregated = [];

// Pattern 1: Aggregate from different sources
for (const item of allItems) {
  // ... aggregation logic
  aggregated.push(normalizedItem);
}

// Pattern 9: Get top 10 by score
const top10 = aggregated
  .sort((a, b) => b.score - a.score)
  .slice(0, 10);

// Pattern 10: Generate report
const report = `Top 10 Items:\n\n${top10.map((item, i) => `${i + 1}. ${item.title} (${item.score})`).join('\n')}`;

return [{json: {report, items: top10}}];
```

---

## 总结

**最有用的模式**：
1. 多来源聚合 - 合并来自 API、数据库的数据
2. Top N 过滤 - 排名、排行榜、最佳结果
3. 数据转换 - CRM 数据、字段映射、数据补全

**各模式共用的关键技术**：
- 数组方法（map、filter、reduce、sort、slice）
- 用正则表达式做模式匹配
- 对象操作与解构
- 用可选链做错误处理
- 用模板字符串做格式化

**另见**：
- [DATA_ACCESS.md](DATA_ACCESS.md) - 数据访问方法
- [ERROR_PATTERNS.md](ERROR_PATTERNS.md) - 避免常见错误
- [BUILTIN_FUNCTIONS.md](BUILTIN_FUNCTIONS.md) - 内置辅助函数

---

## 最佳实践

### 1. 始终校验输入数据

```javascript
const items = $input.all();

// Check if data exists
if (!items || items.length === 0) {
  return [];
}

// Validate structure
if (!items[0].json) {
  return [{json: {error: 'Invalid input format'}}];
}

// Continue processing...
```

### 2. 用 Try-Catch 处理错误

```javascript
try {
  const response = await this.helpers.httpRequest({
    url: 'https://api.example.com/data'
  });

  return [{json: {success: true, data: response}}];
} catch (error) {
  return [{
    json: {
      success: false,
      error: error.message
    }
  }];
}
```

### 3. 优先用数组方法而非循环

```javascript
// ✅ GOOD: Functional approach
const processed = $input.all()
  .filter(item => item.json.valid)
  .map(item => ({json: {id: item.json.id}}));

// ❌ SLOWER: Manual loop
const processed = [];
for (const item of $input.all()) {
  if (item.json.valid) {
    processed.push({json: {id: item.json.id}});
  }
}
```

### 4. 尽早过滤，延后处理

```javascript
// ✅ GOOD: Filter first to reduce processing
const processed = $input.all()
  .filter(item => item.json.status === 'active')  // Reduce dataset first
  .map(item => expensiveTransformation(item));  // Then transform

// ❌ WASTEFUL: Transform everything, then filter
const processed = $input.all()
  .map(item => expensiveTransformation(item))  // Wastes CPU
  .filter(item => item.json.status === 'active');
```

### 5. 使用见名知义的变量名

```javascript
// ✅ GOOD: Clear intent
const activeUsers = $input.all().filter(item => item.json.active);
const totalRevenue = activeUsers.reduce((sum, user) => sum + user.json.revenue, 0);

// ❌ BAD: Unclear purpose
const a = $input.all().filter(item => item.json.active);
const t = a.reduce((s, u) => s + u.json.revenue, 0);
```

### 6. 用 console.log() 调试

```javascript
// Debug statements appear in browser console
const items = $input.all();
console.log(`Processing ${items.length} items`);

for (const item of items) {
  console.log('Item data:', item.json);
  // Process...
}

return result;
```
