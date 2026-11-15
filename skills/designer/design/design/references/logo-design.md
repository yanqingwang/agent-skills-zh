> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/design/references/logo-design.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Logo Design Reference

AI 驱动的 Logo 设计：55+ 种风格、30 套配色、25 份行业指南。默认提供商为 Gemini Nano Banana；Atlas Cloud 与 MuAPI 也可作为显式选择（opt-in）的提供商使用。

## 脚本

| 脚本 | 用途 |
|--------|---------|
| `scripts/logo/search.py` | 搜索风格、配色、行业；生成设计简报 |
| `scripts/logo/generate.py` | 使用 Gemini Nano Banana、Atlas Cloud 或 MuAPI 生成 Logo |
| `scripts/logo/core.py` | Logo 数据的 BM25 搜索引擎 |

## 命令

### 设计简报（从这里开始）

```bash
python3 scripts/logo/search.py "tech startup modern" --design-brief -p "BrandName"
```

### 搜索领域

```bash
# Styles
python3 scripts/logo/search.py "minimalist clean" --domain style

# Color palettes
python3 scripts/logo/search.py "tech professional" --domain color

# Industry guidelines
python3 scripts/logo/search.py "healthcare medical" --domain industry
```

### 生成 Logo

**务必**使用白色背景输出 Logo。

```bash
python3 scripts/logo/generate.py --brand "TechFlow" --style minimalist --industry tech
python3 scripts/logo/generate.py --prompt "coffee shop vintage badge" --style vintage
python3 scripts/logo/generate.py --brand "TechFlow" --provider atlas
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi --muapi-model nano-banana-pro
```

选项：`--style`、`--industry`、`--prompt`、`--provider`、`--atlas-model`、`--muapi-model`

## 可用风格

| 类别 | 风格 |
|----------|--------|
| 通用 | 极简（Minimalist）、字标（Wordmark）、字母标（Lettermark）、图形标（Pictorial Mark）、抽象标（Abstract Mark）、吉祥物（Mascot）、徽章（Emblem）、组合标（Combination Mark） |
| 美学 | 复古/怀旧（Vintage/Retro）、装饰艺术（Art Deco）、奢华（Luxury）、趣味（Playful）、商务（Corporate）、有机（Organic）、霓虹（Neon）、垃圾摇滚（Grunge）、水彩（Watercolor） |
| 现代 | 渐变（Gradient）、扁平设计（Flat Design）、3D/等轴测（3D/Isometric）、几何（Geometric）、线稿（Line Art）、双色调（Duotone）、动效适配（Motion-Ready） |
| 巧思 | 负空间（Negative Space）、单线（Monoline）、分割/碎片化（Split/Fragmented）、响应式/自适应（Responsive/Adaptive） |

## 色彩心理学

| 颜色 | 心理联想 | 最适合 |
|-------|------------|----------|
| 蓝色 | 信任、稳定 | 金融、科技、医疗 |
| 绿色 | 成长、自然 | 环保、健康、有机 |
| 红色 | 活力、激情 | 食品、体育、娱乐 |
| 金色 | 奢华、高端 | 时尚、珠宝、酒店 |
| 紫色 | 创意、创新 | 美妆、创意、科技 |

## 行业默认配置

| 行业 | 风格 | 配色 | 字体 |
|----------|-------|--------|------------|
| 科技 | 极简、抽象 | 蓝色系、紫色系、渐变 | 几何无衬线体 |
| 医疗 | 专业、线稿 | 蓝色系、绿色系、蓝绿色系 | 干净的无衬线体 |
| 金融 | 商务、徽章 | 藏青、金色 | 衬线体或干净的无衬线体 |
| 食品 | 复古徽章、吉祥物 | 暖红、橙色 | 亲和、手写体 |
| 时尚 | 字标、奢华 | 黑、金、白 | 优雅衬线体 |

## 工作流程

1. 生成设计简报 → `scripts/logo/search.py --design-brief`
2. 生成 Logo 变体 → `scripts/logo/generate.py --brand --style --industry`
3. 询问用户是否需要 HTML 预览 → `AskUserQuestion` 工具
4. 若需要，使用内置的 `ui-ux-pro-max` skill 制作 HTML 画廊

## 详细参考

- `references/logo-style-guide.md` - 详细的风格说明
- `references/logo-color-psychology.md` - 颜色的含义与搭配
- `references/logo-prompt-engineering.md` - AI 生成提示词

## 环境配置

```bash
export GEMINI_API_KEY="your-key"
pip install google-genai

# Optional Atlas Cloud provider (no extra Python package required)
export ATLASCLOUD_API_KEY="your-key"

# Optional MuAPI provider (no extra Python package required)
export MUAPI_API_KEY="your-key"
```

MuAPI 使用异步模型端点与预测结果 API。认证方式见
[MuAPI API reference](https://muapi.ai/docs/api-reference)，各模型当前的字段结构见 [nano-banana model contract](https://api.muapi.ai/api/v1/models/nano-banana)
或 [nano-banana-pro model contract](https://api.muapi.ai/api/v1/models/nano-banana-pro)。
Logo 生成器同时支持这两个已文档化的模型 slug，发送它们共有的必填 `prompt` 字段与可选的 `aspect_ratio`
字段；Pro 模型还接受一个可选的 `resolution` 字段，本聚焦的 Logo 工作流将其保留为提供商默认值。
