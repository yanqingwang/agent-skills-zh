> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/cip-prompt-engineering.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CIP 效果图（Mockup）提示词工程

## 基础提示词结构

```
Professional corporate identity mockup photograph showing [DELIVERABLE] for brand '[BRAND_NAME]', [STYLE] design style, using colors [COLORS], [TYPOGRAPHY] typography, logo placement: [PLACEMENT], [MATERIALS] materials with [FINISHES] finish, [CONTEXT] setting, [MOOD] mood, photorealistic product photography, soft natural lighting, high quality professional shot, 8k resolution detailed
```

## 按交付物的修饰词

### 名片
```
business card on marble surface, stack of cards, premium paper texture, soft shadows, 45 degree angle
```

### 信纸信头
```
letterhead flat lay with envelope and pen, velvet fabric background, brand stationery set, overhead view
```

### 办公室标识
```
3D logo signage on office wall, modern lobby interior, backlit LED, brushed metal finish, architectural photography
```

### 车辆品牌化
```
branded vehicle on urban street, 3/4 front angle view, professional car wrap, motion blur background optional
```

### 服装（Polo/T 恤）
```
folded polo shirt on clean background, embroidered logo on chest, premium fabric texture, product photography
```

## 风格修饰词

### 企业极简
```
clean minimal aesthetic, white space, subtle shadows, matte finish, professional
```

### 奢华高端
```
dark background, dramatic rim lighting, gold accents, premium materials, sophisticated
```

### 现代科技
```
gradient colors, geometric elements, clean surfaces, futuristic, innovative
```

### 温暖有机
```
natural materials, kraft paper texture, warm lighting, authentic, artisan
```

## 灯光修饰词

- **工作室：**`professional studio lighting, even illumination`
- **自然：**`soft natural daylight, window light`
- **戏剧化：**`dramatic rim light, dark background, high contrast`
- **温暖：**`warm golden hour lighting, cozy atmosphere`

## 场景修饰词

- **大理石桌面：**`white marble surface, soft shadows, luxury`
- **木桌：**`warm wood grain, natural, artisan`
- **办公室内景：**`modern office environment, architectural`
- **俯拍平铺：**`overhead view, organized arrangement`
- **生活方式：**`in-use context, human element`

## 质量修饰词

始终包含：
```
photorealistic, professional photography, high quality, 8k resolution, detailed, sharp focus
```

## 反向提示词（要避免的）

```
blurry, low quality, distorted text, misspelled, amateur, clipart, cartoon, illustration, watermark
```
