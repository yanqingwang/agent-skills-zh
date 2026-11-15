> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/social-photos-design.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 社交图片设计指南

通过 HTML/CSS 渲染 + 截图导出来设计社交媒体图片。编排内置的 `ui-ux-pro-max`、`brand` 和 `design-system` Skill；截图导出经 Chrome headless、Playwright 或 Puppeteer 完成。

## 平台尺寸

| 平台 | 类型 | 尺寸 (px) | 宽高比 |
|----------|------|-----------|--------|
| Instagram | Post | 1080 x 1080 | 1:1 |
| Instagram | Story/Reel | 1080 x 1920 | 9:16 |
| Instagram | Carousel | 1080 x 1350 | 4:5 |
| Facebook | Post | 1200 x 630 | ~1.9:1 |
| Facebook | Story | 1080 x 1920 | 9:16 |
| Twitter/X | Post | 1200 x 675 | 16:9 |
| Twitter/X | Card | 800 x 418 | ~1.91:1 |
| LinkedIn | Post | 1200 x 627 | ~1.91:1 |
| LinkedIn | Article | 1200 x 644 | ~1.86:1 |
| Pinterest | Pin | 1000 x 1500 | 2:3 |
| YouTube | Thumbnail | 1280 x 720 | 16:9 |
| TikTok | Cover | 1080 x 1920 | 9:16 |
| Threads | Post | 1080 x 1080 | 1:1 |

## 工作流

### 第 1 步：规划工作

用运行时原生的任务清单创建 TODO 任务。拆分为：
- 需求分析任务
- 创意生成任务（一个或多个）
- HTML 设计任务（可按尺寸/变体并行）
- 截图导出任务（可按文件并行）
- 报告生成任务

为独立任务派生并行子代理（例如为不同尺寸生成多个 HTML 文件）。

### 第 2 步：分析需求

从用户输入解析：
- **主题/话题**：社交图片要表达什么
- **目标平台**：需要哪些尺寸（默认：Instagram Post 1:1 + Story 9:16）
- **视觉风格**：极简、大胆、渐变、照片系等
- **品牌语境**：如存在则读取 `docs/brand-guidelines.md`
- **内容元素**：标题、副文、CTA、图片、图标
- **数量**：要多少个变体（默认：3）

### 第 3 步：生成创意

产出 3-5 个概念创意，要求：
- 匹配输入的提示词/需求
- 考虑平台特有的最佳实践
- 在构图、配色、字体排印方案上有变化
- 如有品牌指南则与其对齐

设计之前，通过 `AskUserQuestion` 向用户展示创意并请求确认。

### 第 4 步：设计 HTML 文件

依次使用这些内置 Skill：

1. **`brand`**：从用户项目中提取品牌色、字体、语气
2. **`design-system`**：获取设计 token（间距、字体阶梯、配色板）
3. **`ui-ux-pro-max`**：布局、层级、视觉平衡；每个概念搜索不同的风格、配色或字体搭配，制造设计多样性。

对每个已确认创意 + 每个目标尺寸，创建一个 HTML 文件：

```
output/social-photos/
├── idea-1-instagram-post-1080x1080.html
├── idea-1-instagram-story-1080x1920.html
├── idea-2-instagram-post-1080x1080.html
├── idea-2-instagram-story-1080x1920.html
└── ...
```

#### HTML 设计规则

- **视口**：设置与目标尺寸一致的精确像素尺寸
- **自包含**：内联全部 CSS，字体经 Google Fonts CDN 嵌入
- **无滚动**：所有内容装进一个视口
- **高对比**：文本在缩略图尺寸下可读
- **贴合品牌**：使用提取出的品牌色/字体
- **安全区**：关键内容放在中央 80% 区域内
- **字体排印**：1080px 宽度下标题至少 24px，正文至少 16px
- **视觉层级**：一个焦点，清晰的阅读动线

#### HTML 模板结构

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width={WIDTH}, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family={FONT}&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: {WIDTH}px;
      height: {HEIGHT}px;
      overflow: hidden;
      font-family: '{FONT}', sans-serif;
    }
    .canvas {
      width: {WIDTH}px;
      height: {HEIGHT}px;
      position: relative;
      /* Background: gradient, solid, or image */
    }
    /* Design tokens from brand/design-system */
  </style>
</head>
<body>
  <div class="canvas">
    <!-- Content layers -->
  </div>
</body>
</html>
```

### 第 5 步：截图导出

用 Chrome headless、Playwright 或 Puppeteer 截取精确尺寸的截图。

**重要：** 页面加载后务必加一段延迟（3-5 秒），让字体/图片在截图前完整渲染。

#### 方案 A：Chrome Headless CLI（推荐，零依赖）

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DELAY=5  # seconds for fonts/images to load

"$CHROME" \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --hide-scrollbars \
  --window-size="${WIDTH},${HEIGHT}" \
  --virtual-time-budget=$((DELAY * 1000)) \
  --screenshot="output.png" \
  "file:///path/to/file.html"
```

关键 flag：
- `--virtual-time-budget=5000`：等 5 秒虚拟时间，让资源（Google Fonts、图片）加载
- `--hide-scrollbars`：避免滚动条残影出现在截图里
- `--window-size=WxH`：设置精确像素尺寸

#### 方案 B：运行时提供的浏览器自动化

如果运行时提供浏览器自动化或截图能力（例如浏览器 MCP 服务器），用它来：
1. 在浏览器打开每个 HTML 文件
2. 把视口设为精确目标尺寸
3. 等 3-5 秒让字体/图片完整加载
4. 全页截图为 PNG
5. 保存到 `output/social-photos/exports/`

#### 方案 C：Playwright 脚本

```javascript
const { chromium } = require('playwright');

async function captureScreenshots(htmlFiles) {
  const browser = await chromium.launch();

  for (const file of htmlFiles) {
    const [width, height] = file.match(/(\d+)x(\d+)/).slice(1).map(Number);

    const page = await browser.newPage();
    await page.setViewportSize({ width, height });
    await page.goto(`file://${file}`, { waitUntil: 'networkidle' });
    // Wait for fonts/images to fully render
    await page.waitForTimeout(3000);

    const outputPath = file.replace('.html', '.png').replace('social-photos/', 'social-photos/exports/');
    await page.screenshot({ path: outputPath, type: 'png' });
    await page.close();
  }

  await browser.close();
}
```

#### 方案 D：Puppeteer 脚本

```javascript
const puppeteer = require('puppeteer');

async function captureScreenshots(htmlFiles) {
  const browser = await puppeteer.launch();

  for (const file of htmlFiles) {
    const [width, height] = file.match(/(\d+)x(\d+)/).slice(1).map(Number);

    const page = await browser.newPage();
    await page.setViewport({ width, height, deviceScaleFactor: 2 }); // 2x for retina
    await page.goto(`file://${file}`, { waitUntil: 'networkidle0' });
    // Wait for fonts/images to fully render
    await new Promise(r => setTimeout(r, 3000));

    const outputPath = file.replace('.html', '.png').replace('social-photos/', 'social-photos/exports/');
    await page.screenshot({ path: outputPath, type: 'png' });
    await page.close();
  }

  await browser.close();
}
```

**重要：** 用 `deviceScaleFactor: 2` 获得视网膜品质输出（仅 Puppeteer）。

### 第 6 步：校验并修复设计

在可用的浏览器或图片查看器中打开每张导出的 PNG 并检查：

1. 打开导出的截图，检查布局/样式问题
2. 核验：字体正确渲染、颜色符合品牌、文本在缩略图尺寸下可读
3. 检查：无溢出、无内容被裁、安全区合规、视觉层级清晰
4. 发现问题 → 修 HTML 源码 → 重新导出截图 → 再核验
5. 重复，直到所有设计通过视觉 QA

**需检查的常见问题：**
- 字体未加载（回退到系统字体）
- 文本溢出或被裁
- 元素越出安全区（中央 80%）
- 低对比文本（低于 WCAG AA 4.5:1）
- 元素错位或布局破碎

### 第 7 步：生成总结报告

把报告保存为 `plans/reports/{YYMMDD}-social-photos-{topic}.md`。

报告结构：

```markdown
# Social Photos Design Report

## Overview
- Prompt/requirements: {original input}
- Platforms: {target platforms}
- Variations: {count}
- Style: {chosen style}

## Ideas Generated
1. **{Idea name}** — {brief description, rationale}
2. ...

## Design Decisions
- Color palette: {colors used, why}
- Typography: {fonts, sizes, why}
- Layout: {composition approach, why}
- Brand alignment: {how brand guidelines influenced design}

## Output Files
| File | Size | Platform | Preview |
|------|------|----------|---------|
| exports/{filename}.png | {WxH} | {platform} | {description} |

## Why This Works
- {Platform-specific reasoning}
- {Brand alignment reasoning}
- {Visual hierarchy reasoning}
- {Engagement potential reasoning}

## Recommendations
- {A/B test suggestions}
- {Platform-specific tips}
- {Iteration opportunities}
```

### 第 8 步：整理产出

整理所有输出文件与报告：
- 把导出的 PNG 移动/复制到正确的素材目录
- 确保报告按第 7 步的命名放在 `plans/reports/` 下
- 如有要求，清理中间 HTML 文件
- 给产出打上元数据标签（平台、尺寸、创意名）

## 设计最佳实践

### 平台特有技巧

- **Instagram**：视觉优先，少文字（<20%），强色彩，生活方式感
- **Facebook**：信息型，可以多些文字，信息流里抓眼球
- **Twitter/X**：大胆标题，深/浅色模式都要有对比，信息清晰
- **LinkedIn**：专业、干净、数据型视觉，思想领导力
- **Pinterest**：竖版构图，图上叠文字，教程风格
- **YouTube**：人脸特写效果最好，亮色，小尺寸下可读
- **TikTok**：潮流、有活力、大胆字体排印，面向年轻人

### 美术风格（沿用 Banner 的分类）

| 风格 | 适用 | 关键元素 |
|-------|----------|--------------|
| Minimalist | SaaS、科技、奢侈品牌 | 留白、单一强调色、干净字体 |
| Bold Typography | 公告、语录 | 大字号、高对比、少图像 |
| Gradient Mesh | 现代品牌、App | 流动色彩过渡、悬浮元素 |
| Photo-Based | 生活方式、电商 | 主视觉图、轻微叠色、图上文字 |
| Geometric | 科技、金融科技 | 形状、图案、结构化布局 |
| Glassmorphism | SaaS、现代 App | 磨砂玻璃、模糊效果、透明感 |
| Flat Illustration | 教育、健康 | 定制插画、友好、亲和 |
| Duotone | 创意、编辑出版 | 照片的双色处理 |
| Collage | 时尚、文化 | 混合媒介、元素叠放 |
| 3D/Isometric | 科技、产品 | 纵深、阴影、现代透视 |

### 颜色与对比

- 所有文本保证 WCAG AA 对比度（最低 4.5:1）
- 以 50% 尺寸测试设计，验证可读性
- 考虑平台深色/浅色模式兼容
- 品牌主色作主导，辅色作强调

### 字体层级

| 元素 | 最小字号（1080px 下） | 字重 |
|---------|---------------------|--------|
| Headline | 48px | Bold/Black |
| Subheadline | 32px | Semibold |
| Body | 24px | Regular |
| Caption | 18px | Regular/Light |
| CTA | 28px | Bold |

## 安全与边界

这个子 Skill 只负责社交媒体图片设计。不负责：
- 视频内容制作
- 动画/动态图形
- 印刷生产文件（CMYK、出血）
- 直接发布/排期到社交媒体
- AI 图像生成（提供图片，或用另一个获得授权的能力生成）
