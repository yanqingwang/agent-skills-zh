> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/brand/references/asset-organization.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 素材整理指南

以结构化、可检索的方式组织营销素材的准则。

## 目录结构

```
project-root/
├── .assets/                          # Git-tracked metadata
│   ├── manifest.json                 # Central asset registry
│   ├── tags.json                     # Tagging system
│   ├── versions/                     # Version history
│   │   └── {asset-id}/
│   │       └── v{n}.json
│   └── metadata/                     # Type-specific metadata
│       ├── designs.json
│       ├── banners.json
│       ├── logos.json
│       └── videos.json
├── assets/                           # Raw files
│   ├── designs/
│   │   ├── campaigns/                # Campaign-specific designs
│   │   ├── web/                      # Website graphics
│   │   └── print/                    # Print materials
│   ├── banners/
│   │   ├── social-media/             # Platform banners
│   │   ├── email-headers/            # Email template headers
│   │   └── landing-pages/            # Hero/section images
│   ├── logos/
│   │   ├── full-horizontal/          # Full logo with wordmark
│   │   ├── icon-only/                # Symbol only
│   │   ├── monochrome/               # Single color versions
│   │   └── variations/               # Special versions
│   ├── videos/
│   │   ├── ads/                      # Promotional videos
│   │   ├── tutorials/                # How-to content
│   │   └── testimonials/             # Customer videos
│   ├── infographics/                 # Data visualizations
│   └── generated/                    # AI-generated assets
│       └── {YYYYMMDD}/               # Date-organized
```

## 命名规范

### 格式
```
{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}
```

### 组成部分
| 组件 | 格式 | 必填 | 示例 |
|-----------|--------|----------|----------|
| type | lowercase | 是 | banner, logo, design, video |
| campaign | kebab-case | 是* | claude-launch, q1-promo, evergreen |
| description | kebab-case | 是 | hero-image, email-header |
| timestamp | YYYYMMDD | 是 | 20251209 |
| variant | kebab-case | 否 | dark-mode, 1x1, mobile |

*非活动素材使用"evergreen"

### 示例
```
banner_claude-launch_hero-image_20251209_16-9.png
logo_brand-refresh_horizontal-full-color_20251209.svg
design_holiday-campaign_email-hero_20251209_dark-mode.psd
video_product-demo_feature-walkthrough_20251209.mp4
infographic_evergreen_pricing-comparison_20251209.png
```

## 元数据 Schema

### 素材条目（manifest.json）
```json
{
  "id": "uuid-v4",
  "name": "Campaign Hero Banner",
  "type": "banner",
  "path": "assets/banners/landing-pages/banner_claude-launch_hero-image_20251209.png",
  "dimensions": { "width": 1920, "height": 1080 },
  "fileSize": 245760,
  "mimeType": "image/png",
  "tags": ["campaign", "hero", "launch"],
  "status": "approved",
  "source": {
    "model": "imagen-4",
    "prompt": "...",
    "createdAt": "2025-12-09T10:30:00Z"
  },
  "version": 2,
  "createdBy": "agent:content-creator",
  "approvedBy": "user:john",
  "approvedAt": "2025-12-09T14:00:00Z"
}
```

### 版本条目（versions/{id}/v{n}.json）
```json
{
  "version": 2,
  "previousVersion": 1,
  "path": "assets/banners/landing-pages/banner_claude-launch_hero-image_20251209_v2.png",
  "changes": "Updated CTA button color to match brand refresh",
  "createdAt": "2025-12-09T12:00:00Z",
  "createdBy": "agent:ui-designer"
}
```

## 打标系统

### 标准标签
| 类别 | 取值 |
|----------|--------|
| status | draft, review, approved, archived |
| platform | instagram, twitter, linkedin, facebook, youtube, email, web |
| content-type | promotional, educational, brand, product, testimonial |
| format | 1x1, 4x5, 9x16, 16x9, story, reel, banner |
| source | imagen-4, veo-3, user-upload, canva, figma |

### 标签使用
- 每个素材应包含：status + platform + content-type
- 可选：format、source、campaign

## 文件组织最佳实践

1. **一个变体一个文件**：不要把深色/浅色合在一个文件里
2. **源文件单独放**：`.psd`/`.fig` 保留在同一结构中
3. **AI 素材加时间戳**：按生成日期自动归档
4. **归档而非删除**：移入 `archived/` 并加日期前缀
5. **大文件外置**：超过 100MB 的视频用云存储链接

## 检索模式

### 按类型
```bash
# Find all banners
ls assets/banners/**/*
```

### 按活动
```bash
# Find all assets for specific campaign
grep -l "claude-launch" .assets/manifest.json
```

### 按状态
```bash
# Find approved assets only
jq '.assets[] | select(.status == "approved")' .assets/manifest.json
```

## 清理工作流

1. 对新素材运行 `extract-colors.cjs`
2. 对照品牌指南校验
3. 把新条目写入 manifest.json
4. 打上合适的标签
5. 移除重复/过期版本
