> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/design/references/logo-prompt-engineering.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Logo AI 提示词工程

## 核心提示词结构

```
Professional logo design for [brand/industry]:
[Visual description]
Style: [style keywords]
Colors: [color palette]
Requirements: [technical specs]
```

## 各风格的有效关键词

### 极简
```
minimalist, clean lines, simple geometric shapes, essential elements only,
high white space, flat design, single color, modern, uncluttered,
negative space, subtle, refined
```

### 复古/怀旧
```
vintage, retro, heritage, established, classic, nostalgic, weathered,
distressed texture, badge style, hand-lettered, craft, artisan,
sepia tones, muted colors, aged paper effect
```

### 奢华/高端
```
luxury, elegant, sophisticated, premium, refined, exclusive, high-end,
gold accents, metallic, minimal, tasteful, upscale, prestige,
thin lines, serif typography, foil effect
```

### 现代/科技
```
modern, innovative, digital, tech-forward, sleek, futuristic,
gradient colors, geometric, abstract, dynamic, cutting-edge,
clean sans-serif, circuit-like, data visualization
```

### 活泼/趣味
```
playful, fun, colorful, friendly, approachable, cheerful, whimsical,
bouncy, rounded shapes, bright colors, cartoon-like, energetic,
bubbly, hand-drawn elements
```

### 有机/自然
```
organic, natural, flowing, botanical, eco-friendly, sustainable,
earth tones, leaf elements, hand-drawn, imperfect lines, growth,
green, nature-inspired, biophilic
```

## 负面提示词（要避免什么）

始终加上以下内容，以避免不想要的结果：
```
NOT: photorealistic, 3D render with realistic textures, photograph,
stock image, clip art, multiple logos, busy background, text watermarks,
low quality, blurry, distorted, complex detailed patterns
```

## 行业专用提示词

### 科技初创
```
Modern tech company logo, abstract geometric mark, gradient blue to purple,
clean minimal design, innovative feel, scalable vector style,
professional quality, silicon valley aesthetic
```

### 医疗健康
```
Healthcare medical logo, clean professional design, cross or heart symbol,
calming blue and teal colors, trustworthy appearance, caring feel,
simple scalable mark, HIPAA-appropriate conservative style
```

### 餐饮/食品
```
Restaurant logo, warm inviting colors, appetizing feel, vintage badge style,
chef or utensil iconography, friendly welcoming design, rustic charm,
established look, readable at small sizes
```

### 时尚品牌
```
Fashion brand logo, elegant sophisticated wordmark, luxury aesthetic,
black and gold color scheme, thin refined typography, haute couture feel,
minimal exclusive design, high-end positioning
```

### 环保/可持续
```
Eco-friendly sustainable brand logo, organic natural elements, leaf motif,
earth green and brown colors, growth symbolism, environmental awareness,
clean modern yet natural feel, recyclable-look design
```

## 需要包含的技术要求

### 可缩放性
```
vector-style, scalable at any size, clear silhouette,
works as favicon, recognizable small scale, simple shapes
```

### 多场景适用性
```
works on light and dark backgrounds, single color version possible,
horizontal and stacked layouts, brand mark can stand alone
```

### 质量
```
professional quality, print-ready, high resolution,
crisp edges, balanced composition, centered design
```

## 提示词模板

### 快速生成
```
Professional [industry] logo, [style] design, [color] colors,
clean modern aesthetic, scalable vector style
```

### 详细简报
```
Professional logo design for [brand name], a [industry] company.

Visual style: [style keywords]
Primary colors: [hex codes]
Mood: [emotional keywords]
Symbols: [iconography hints]

Technical: Vector-style illustration, scalable, works in single color,
centered on plain background, no text unless specified.
```

### 变体请求
```
Alternative version of [brand] logo:
Keep: [elements to preserve]
Change: [elements to modify]
Style direction: [new style keywords]
```

## 常见坑

1. **过于详细**：AI 会生成复杂图案；要求"simple"
2. **背景不明确**：指定"plain white background"
3. **文字问题**：AI 不擅长文字；单独生成图形标记
4. **比例错误**：指定"1:1 square"或"horizontal"
5. **写实风格**：加上"illustration, vector-style, not photorealistic"
