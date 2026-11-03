---
name: design
description: "综合设计 Skill：品牌识别、设计 token、UI 样式、logo 生成（55 种风格，Gemini、Atlas Cloud 或 MuAPI AI）、企业形象计划（50 项交付物、CIP 样机）、HTML 演示文稿（Chart.js）、横幅设计（22 种风格，社交/广告/网页/印刷）、图标设计（15 种风格，SVG，Gemini 3.1 Pro）、社交配图（HTML→截图，多平台）。操作：设计 logo、创建 CIP、生成样机、制作幻灯片、设计横幅、生成图标、创建社交配图、社交媒体图片、品牌识别、设计系统。平台：Facebook、Twitter、LinkedIn、YouTube、Instagram、Pinterest、TikTok、Threads、Google Ads。"
argument-hint: "[design-type] [context]"
license: MIT
metadata:
  author: claudekit
  version: "2.1.0"
---

> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 设计（Design）

统一设计 Skill：品牌、token、UI、logo、CIP、幻灯片、横幅、社交配图、图标。

## 何时应用

- 品牌识别、品牌语气与品牌资产
- 设计系统的 token 与规格
- 使用 shadcn/ui + Tailwind 的 UI 样式
- logo 设计与 AI 生成
- 企业形象计划（CIP）交付物
- 演示文稿与路演幻灯片
- 面向社交媒体、广告、网页、印刷的横幅设计
- 面向 Instagram、Facebook、LinkedIn、Twitter、Pinterest、TikTok 的社交配图

## 子 Skill 路由

| 任务 | 子 Skill | 详情 |
|------|-----------|---------|
| 品牌识别、品牌语气与品牌资产 | `brand` | 随附同级 Skill |
| Token、规格、CSS 变量 | `design-system` | 随附同级 Skill |
| shadcn/ui、Tailwind、代码 | `ui-styling` | 随附同级 Skill |
| Logo 创建、AI 生成 | Logo（内置） | `references/logo-design.md` |
| CIP 样机、交付物 | CIP（内置） | `references/cip-design.md` |
| 演示文稿、路演幻灯片 | Slides（内置） | `references/slides.md` |
| 横幅、封面、页头 | Banner（内置） | `references/banner-sizes-and-styles.md` |
| 社交媒体图片/照片 | Social Photos（内置） | `references/social-photos-design.md` |
| SVG 图标、图标集 | Icon（内置） | `references/icon-design.md` |

## 脚本路径

本 Skill 及其 `references/` 中的脚本路径相对于包含本 SKILL.md 的目录，而非项目目录：`scripts/<file>` 指本 Skill 自身的 `scripts/` 文件夹，`../<skill>/scripts/<file>` 指随之一并安装的同级子 Skill。请基于该目录构建完整路径（Skill 加载时 Claude Code 会将其报告为该 Skill 的基准目录），并把工作目录保持在项目根目录——脚本会相对于项目根目录读写 `docs/brand-guidelines.md`、`assets/design-tokens.json`、`src/` 等项目文件。

## Logo 设计（内置）

55+ 种风格、30 套配色、25 份行业指南。Gemini Nano Banana、Atlas Cloud 与 MuAPI 图像生成。

### Logo：生成设计简报

```bash
python3 scripts/logo/search.py "tech startup modern" --design-brief -p "BrandName"
```

### Logo：检索风格/配色/行业

```bash
python3 scripts/logo/search.py "minimalist clean" --domain style
python3 scripts/logo/search.py "tech professional" --domain color
python3 scripts/logo/search.py "healthcare medical" --domain industry
```

### Logo：用 AI 生成

**务必**以白色背景生成输出的 logo 图片。

```bash
python3 scripts/logo/generate.py --brand "TechFlow" --style minimalist --industry tech
python3 scripts/logo/generate.py --prompt "coffee shop vintage badge" --style vintage
python3 scripts/logo/generate.py --brand "TechFlow" --provider atlas
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi --muapi-model nano-banana-pro
```

**重要：**脚本运行失败时，请尝试直接修复。

生成之后，**务必**通过 `AskUserQuestion` 询问用户是否需要 HTML 预览；若需要，使用随附的 `ui-ux-pro-max` Skill 展示图库。

## CIP 设计（内置）

50+ 项交付物、20 种风格、20 个行业。Gemini Nano Banana（Flash/Pro）。

### CIP：生成简报

```bash
python3 scripts/cip/search.py "tech startup" --cip-brief -b "BrandName"
```

### CIP：按域检索

```bash
python3 scripts/cip/search.py "business card letterhead" --domain deliverable
python3 scripts/cip/search.py "luxury premium elegant" --domain style
python3 scripts/cip/search.py "hospitality hotel" --domain industry
python3 scripts/cip/search.py "office reception" --domain mockup
```

### CIP：生成样机

```bash
# With logo (RECOMMENDED)
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card" --industry "consulting"

# Full CIP set
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --industry "consulting" --set

# Pro model (4K text)
python3 scripts/cip/generate.py --brand "TopGroup" --logo logo.png --deliverable "business card" --model pro

# Without logo
python3 scripts/cip/generate.py --brand "TechFlow" --deliverable "business card" --no-logo-prompt
```

模型：`flash`（默认，`gemini-2.5-flash-image`）、`pro`（`gemini-3-pro-image`）。可用 `GEMINI_FLASH_IMAGE_MODEL` / `GEMINI_PRO_IMAGE_MODEL` 覆盖模型 id。

### CIP：渲染 HTML 演示

```bash
python3 scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images /path/to/cip-output
```

**提示：**如果还没有 logo，请先使用上方的 Logo 设计章节。

## 幻灯片（内置）

结合 Chart.js、设计 token 与文案公式的策略型 HTML 演示文稿。

创建工作流请加载 `references/slides-create.md`。

### 幻灯片：知识库

| 主题 | 文件 |
|-------|------|
| 创建指南 | `references/slides-create.md` |
| 布局模式 | `references/slides-layout-patterns.md` |
| HTML 模板 | `references/slides-html-template.md` |
| 文案写作 | `references/slides-copywriting-formulas.md` |
| 策略 | `references/slides-strategies.md` |

## 横幅设计（内置）

覆盖社交、广告、网页、印刷四种场景的 22 种艺术指导风格。该工作流不依赖捆绑包之外的任何内容：使用 `references/banner-sizes-and-styles.md` 和随附的 `ui-ux-pro-max` Skill 获取风格与配色指导。浏览器调研、图像生成与截图捕获是可选的运行时能力；不可用时，请使用现有素材、CSS 构建的视觉元素，以及运行时的标准预览或捕获工作流。

完整尺寸与风格参考请加载 `references/banner-sizes-and-styles.md`。

### 横幅：工作流

1. **收集需求**——通过 `AskUserQuestion` 了解用途、平台、内容、品牌、风格、数量
2. **调研**——阅读 `references/banner-sizes-and-styles.md`，并使用随附的 `ui-ux-pro-max` Skill 获取风格与配色指导；若浏览器调研可用且获许可，收集 3–5 个参考案例
3. **设计**——按平台精确尺寸创建 HTML/CSS 横幅；使用现有素材或 CSS 构建的视觉元素，若运行时提供经授权的图像生成能力也可使用
4. **导出**——使用运行时的浏览器或截图能力按精确尺寸捕获 PNG；不可用时，交付 HTML/CSS 源码并标注 PNG 导出待完成
5. **呈现**——并排展示所有选项，根据反馈迭代

### 横幅：常用尺寸速查

| 平台 | 类型 | 尺寸（px） |
|----------|------|-----------|
| Facebook | 封面 | 820 x 312 |
| Twitter/X | 页头 | 1500 x 500 |
| LinkedIn | 个人主页 | 1584 x 396 |
| YouTube | 频道封面 | 2560 x 1440 |
| Instagram | 快拍 | 1080 x 1920 |
| Instagram | 帖子 | 1080 x 1080 |
| Google Ads | 中矩形 | 300 x 250 |
| 网站 | Hero 图 | 1920 x 600-1080 |

### 横幅：热门艺术风格

| 风格 | 最适用于 |
|-------|----------|
| 极简 | SaaS、科技 |
| 粗体排印 | 公告 |
| 渐变 | 现代品牌 |
| 照片型 | 生活方式、电商 |
| 几何 | 科技、金融科技 |
| 玻璃拟态 | SaaS、应用 |
| 霓虹/赛博朋克 | 游戏、活动 |

### 横幅：设计规则

- 安全区：关键内容放在中央 70-80% 区域内
- 每条横幅一个 CTA，置于右下角，最小高度 44px
- 字体最多 2 种，正文最小 16px，标题 ≥32px
- 广告中文字占比低于 20%（Meta 会降权处理）
- 印刷：300 DPI、CMYK、3-5mm 出血

## 图标设计（内置）

15 种风格、12 个类别。Gemini 3.1 Pro Preview 生成 SVG 文本输出。

### 图标：生成单个图标

```bash
python3 scripts/icon/generate.py --prompt "settings gear" --style outlined
python3 scripts/icon/generate.py --prompt "shopping cart" --style filled --color "#6366F1"
python3 scripts/icon/generate.py --name "dashboard" --category navigation --style duotone
```

### 图标：批量生成变体

```bash
python3 scripts/icon/generate.py --prompt "cloud upload" --batch 4 --output-dir ./icons
```

### 图标：多尺寸导出

```bash
python3 scripts/icon/generate.py --prompt "user profile" --sizes "16,24,32,48" --output-dir ./icons
```

### 图标：热门风格

| 风格 | 最适用于 |
|-------|----------|
| outlined | UI 界面、Web 应用 |
| filled | 移动应用、导航栏 |
| duotone | 营销、落地页 |
| rounded | 亲和型应用、健康 |
| sharp | 科技、金融科技、企业 |
| flat | Material design、Google 风格 |
| gradient | 现代品牌、SaaS |

**模型：**`gemini-3.1-pro-preview` —— 仅文本输出（SVG 本质是 XML 文本）。无需图像生成 API。

## 社交配图（内置）

多平台社交图片设计：HTML/CSS → 截图导出。使用随附的 `ui-ux-pro-max`、`brand` 与 `design-system` Skill；截图导出通过 Chrome headless、Playwright 或 Puppeteer 完成（参见参考文档）。

尺寸、模板与最佳实践请加载 `references/social-photos-design.md`。

### 社交配图：工作流

1. **编排**——用运行时原生任务列表跟踪以下步骤；独立工作交给并行的子代理
2. **分析**——解析提示词：主题、平台、风格、品牌语境、内容元素
3. **构思**——产出 3-5 个概念，通过 `AskUserQuestion` 呈现
4. **设计**——依次使用随附的 `brand` → `design-system` → `ui-ux-pro-max` Skill；每个创意 × 尺寸各出一份 HTML
5. **导出**——用 Chrome headless、Playwright 或 Puppeteer 按精确 px 截图（工具支持时用 2x device scale factor；参见参考文档）
6. **校验**——在可用的浏览器或图片查看器中打开导出的 PNG 并逐一检查；修复布局/样式问题后重新导出
7. **汇报**——将摘要连同设计决策写入 `plans/reports/`
8. **归档**——把输出文件与报告整理进项目的资源目录

### 社交配图：关键尺寸

| 平台 | 尺寸（px） | 平台 | 尺寸（px） |
|----------|-----------|----------|-----------|
| IG 帖子 | 1080×1080 | FB 帖子 | 1200×630 |
| IG 快拍 | 1080×1920 | X 帖子 | 1200×675 |
| IG 轮播 | 1080×1350 | LinkedIn | 1200×627 |
| YT 缩略图 | 1280×720 | Pinterest | 1000×1500 |

## 工作流

### 完整品牌包

1. **Logo** → `scripts/logo/generate.py` → 生成 logo 变体
2. **CIP** → `scripts/cip/generate.py --logo ...` → 创建交付物样机
3. **演示文稿** → 加载 `references/slides-create.md` → 构建路演幻灯片

### 新建设计系统

1. **品牌**（brand skill）→ 定义色彩、字体排印、语气
2. **Token**（design-system skill）→ 创建语义 token 层
3. **实现**（ui-styling skill）→ 配置 Tailwind 与 shadcn/ui

## 参考资料

| 主题 | 文件 |
|-------|------|
| 设计路由 | `references/design-routing.md` |
| Logo 设计指南 | `references/logo-design.md` |
| Logo 风格 | `references/logo-style-guide.md` |
| Logo 色彩 | `references/logo-color-psychology.md` |
| Logo 提示词 | `references/logo-prompt-engineering.md` |
| CIP 设计指南 | `references/cip-design.md` |
| CIP 交付物 | `references/cip-deliverable-guide.md` |
| CIP 风格 | `references/cip-style-guide.md` |
| CIP 提示词 | `references/cip-prompt-engineering.md` |
| 幻灯片创建 | `references/slides-create.md` |
| 幻灯片布局 | `references/slides-layout-patterns.md` |
| 幻灯片模板 | `references/slides-html-template.md` |
| 幻灯片文案 | `references/slides-copywriting-formulas.md` |
| 幻灯片策略 | `references/slides-strategies.md` |
| 横幅尺寸与风格 | `references/banner-sizes-and-styles.md` |
| 社交配图指南 | `references/social-photos-design.md` |
| 图标设计指南 | `references/icon-design.md` |

## 脚本

| 脚本 | 用途 |
|--------|---------|
| `scripts/logo/search.py` | 检索 logo 风格、配色、行业 |
| `scripts/logo/generate.py` | 用 Gemini AI 生成 logo |
| `scripts/logo/core.py` | logo 数据的 BM25 检索引擎 |
| `scripts/cip/search.py` | 检索 CIP 交付物、风格、行业 |
| `scripts/cip/generate.py` | 用 Gemini 生成 CIP 样机 |
| `scripts/cip/render-html.py` | 用 CIP 样机渲染 HTML 演示 |
| `scripts/cip/core.py` | CIP 数据的 BM25 检索引擎 |
| `scripts/icon/generate.py` | 用 Gemini 3.1 Pro 生成 SVG 图标 |

## 前置条件

**Python：**本 Skill 使用 Python 脚本。在 Windows 上请用 `python` 代替 `python3`（例如用 `python scripts/logo/search.py` 代替 `python3 scripts/logo/search.py`）。

检查 Python 是否已安装：
```bash
python3 --version || python --version
```

## 配置

```bash
export GEMINI_API_KEY="your-key"  # https://aistudio.google.com/apikey
pip install google-genai pillow

# Optional MuAPI provider (no extra Python package required)
export MUAPI_API_KEY="your-key"
```

MuAPI 使用异步模型端点与预测结果 API。身份验证参见 [MuAPI API reference](https://muapi.ai/docs/api-reference)，各模型当前的专属 schema 参见 [nano-banana model contract](https://api.muapi.ai/api/v1/models/nano-banana) 或 [nano-banana-pro model contract](https://api.muapi.ai/api/v1/models/nano-banana-pro)。logo 生成器同时支持文档中的两种模型 slug，发送两者共有的必填 `prompt` 字段和可选的 `aspect_ratio` 字段；Pro 模型还接受一个可选的 `resolution` 字段，本聚焦型 logo 工作流将其保持为提供商默认值。

> **Windows 注意：**必要时用 `python` 代替 `pip`（例如 `python -m pip install ...`）。

## 集成

**随附子 Skill：**brand、design-system、ui-styling
**相关 Skill：**ui-ux-pro-max
