> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/cip-design.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CIP 设计参考

企业视觉识别（Corporate Identity Program）设计：50+ 交付物、20 种风格、20 个行业。用 Gemini Nano Banana（Flash/Pro）生成 mockup。

## 脚本

| 脚本 | 用途 |
|--------|---------|
| `scripts/cip/search.py` | 检索交付物、风格、行业；生成 CIP 简报 |
| `scripts/cip/generate.py` | 用 Gemini（Flash/Pro）生成 CIP mockup |
| `scripts/cip/render-html.py` | 从 CIP mockup 渲染 HTML 演示页 |
| `scripts/cip/core.py` | CIP 数据的 BM25 检索引擎 |

## 命令

### CIP 简报（从这里开始）

```bash
python3 scripts/cip/search.py "tech startup" --cip-brief -b "BrandName"
```

### 检索域

```bash
# Deliverables
python3 scripts/cip/search.py "business card letterhead" --domain deliverable

# Design styles
python3 scripts/cip/search.py "luxury premium elegant" --domain style

# Industry guidelines
python3 scripts/cip/search.py "hospitality hotel" --domain industry

# Mockup contexts
python3 scripts/cip/search.py "office reception" --domain mockup
```

### 生成 mockup

```bash
# With logo (RECOMMENDED - uses image editing)
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card" --industry "consulting"

# Full CIP set with logo
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --industry "consulting" --set

# Pro model for 4K text rendering
python3 scripts/cip/generate.py --brand "TopGroup" --logo logo.png --deliverable "business card" --model pro

# Custom deliverables with aspect ratio
python3 scripts/cip/generate.py --brand "GreenLeaf" --logo logo.png --industry "organic food" --deliverables "letterhead,packaging,vehicle" --ratio 16:9

# Without logo (AI generates interpretation)
python3 scripts/cip/generate.py --brand "TechFlow" --deliverable "business card" --no-logo-prompt
```

### 渲染 HTML 演示页

```bash
python3 scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images /path/to/cip-output
python3 scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images ./topgroup-cip --output presentation.html
```

## 模型

- `flash`（默认）：`gemini-2.5-flash-image` - 快、省成本
- `pro`：`gemini-3-pro-image` - 重质量、4K 文字渲染

设置 `GEMINI_FLASH_IMAGE_MODEL` 或 `GEMINI_PRO_IMAGE_MODEL` 可改用其他 Gemini 模型 id。

## 交付物分类

| 分类 | 条目 |
|----------|-------|
| Core Identity | Logo, Logo Variations |
| Stationery | Business Card, Letterhead, Envelope, Folder, Notebook, Pen |
| Security/Access | ID Badge, Lanyard, Access Card |
| Office Environment | Reception Signage, Wayfinding, Meeting Room Signs, Wall Graphics |
| Apparel | Polo Shirt, T-Shirt, Cap, Jacket, Apron |
| Promotional | Tote Bag, Gift Box, USB Drive, Water Bottle, Mug, Umbrella |
| Vehicle | Car Sedan, Van, Truck |
| Digital | Social Media, Email Signature, PowerPoint, Document Templates |
| Product | Packaging Box, Labels, Tags, Retail Display |
| Events | Trade Show Booth, Banner Stand, Table Cover, Backdrop |

## 设计风格

| 风格 | 颜色 | 适用 |
|-------|--------|----------|
| Corporate Minimal | Navy, White, Blue | Finance, Legal, Consulting |
| Modern Tech | Purple, Cyan, Green | Tech, Startups, SaaS |
| Luxury Premium | Black, Gold, White | Fashion, Jewelry, Hotels |
| Warm Organic | Brown, Green, Cream | Food, Organic, Artisan |
| Bold Dynamic | Red, Orange, Black | Sports, Entertainment |

## HTML 演示页特性

- Hero 区带品牌名、行业、风格、情绪
- 交付物卡片带 mockup 图
- 描述：概念、用途、规格
- 响应式桌面/移动，暗色主题
- 图片以 base64 内嵌（单文件可携带）

## 工作流

1. 生成 CIP 简报 → `scripts/cip/search.py --cip-brief`
2. 带 logo 生成 mockup → `scripts/cip/generate.py --brand --logo --industry --set`
3. 渲染 HTML 演示页 → `scripts/cip/render-html.py --brand --industry --images`

**提示：** 没有 logo 时，先用内置的 Logo Design 生成一个。

## 详细参考

- `references/cip-deliverable-guide.md` - 交付物规格
- `references/cip-style-guide.md` - 设计风格描述
- `references/cip-prompt-engineering.md` - AI 生成 prompt

## 环境准备

```bash
export GEMINI_API_KEY="your-key"
pip install google-genai pillow
```
