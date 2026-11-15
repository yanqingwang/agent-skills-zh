> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/design-routing.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 设计路由指南（Design Routing Guide）

何时使用各个设计子 Skill。

## Skill 概览

| Skill | 用途 | 关键文件 |
|-------|---------|-----------|
| brand | 品牌识别、语气、素材 | SKILL.md + 10 个参考文件 + 3 个脚本 |
| design-system | 令牌架构、规格 | SKILL.md + 7 个参考文件 + 2 个脚本 |
| ui-styling | 组件实现 | SKILL.md + 7 个参考文件 + 2 个脚本 |
| logo-design | AI logo 生成（55 种风格、30 套配色） | SKILL.md + 4 个参考文件 + 2 个脚本 |
| cip-design | 企业形象计划 CIP（50 项交付物） | SKILL.md + 3 个参考文件 + 3 个脚本 |
| slides | 带 Chart.js 的 HTML 演示文稿 | SKILL.md + 4 个参考文件 |
| banner-design | 社交、广告、网页、印刷横幅（22 种风格） | SKILL.md + 1 个参考文件 |
| icon-design | SVG 图标生成（15 种风格，Gemini 3.1 Pro） | SKILL.md + 1 个参考文件 + 1 个脚本 |

## 按任务类型路由

### 品牌识别任务
**→ brand**

- 定义品牌颜色与字体排印
- 编写 logo 使用规范
- 确立品牌语气与调性
- 整理并校验素材
- 创建信息传达框架
- 审计品牌一致性

### 令牌体系任务
**→ design-system**

- 创建设计令牌 JSON
- 生成 CSS 变量
- 定义组件规格
- 将令牌映射到 Tailwind 配置
- 校验代码中的令牌使用
- 编写状态与变体文档

### 实现类任务
**→ ui-styling**

- 添加 shadcn/ui 组件
- 用 Tailwind 类做样式
- 实现深色模式
- 创建响应式布局
- 构建无障碍组件

### Logo 设计任务
**→ logo-design**

- 用 AI 创建 logo（Gemini Nano Banana）
- 搜索 logo 风格、配色方案、行业指南
- 生成设计简报
- 探索 55+ 种风格（极简、复古、奢华、几何等）

### 企业形象计划（CIP）任务
**→ cip-design**

- 生成 CIP 交付物（名片、信纸、标识牌、车身、服饰）
- 结合行业/风格分析创建 CIP 简报
- 生成带/不带 logo 的效果图（Gemini Flash/Pro）
- 从 CIP 效果图渲染 HTML 演示文稿

### 演示文稿任务
**→ slides**

- 创建战略性 HTML 演示文稿
- 用 Chart.js 做数据可视化
- 将文案公式应用到幻灯片内容
- 使用布局模式与设计令牌

### 横幅设计任务
**→ banner-design**

- 设计社交媒体横幅（Facebook、Twitter、LinkedIn、YouTube、Instagram）
- 创建广告横幅（Google Ads、Meta Ads）
- 网站首屏（hero）横幅与页头
- 印刷横幅与封面
- 22 种艺术指导风格（极简、粗体排印、渐变、玻璃拟态等）

### 图标设计任务
**→ icon-design**

- 用 AI 生成 SVG 图标（Gemini 3.1 Pro Preview）
- 以多种风格批量生成图标变体
- 多尺寸导出（16px、24px、32px、48px）
- 15 种风格：线性、面性、双色、圆角、锐角、渐变等
- 12 个类别：导航、操作、通信、媒体、商务、数据

## 按问题类型路由

| 问题 | Skill |
|----------|-------|
| “这里该用什么颜色？” | brand |
| “怎么为 X 创建令牌？” | design-system |
| “怎么构建按钮组件？” | ui-styling |
| “这符合品牌调性吗？” | brand |
| “这里该用 CSS 变量吗？” | design-system |
| “怎么加深色模式？” | ui-styling |
| “给我的品牌做个 logo” | logo-design |
| “生成名片效果图” | cip-design |
| “做一份路演幻灯片” | slides |
| “设计一套品牌识别包” | cip-design |
| “哪种 logo 风格适合我的行业？” | logo-design |
| “设计一张 Facebook 封面” | banner-design |
| “给 Google 做广告横幅” | banner-design |
| “做一张网站首屏横幅” | banner-design |
| “生成一个设置图标” | icon-design |
| “为我的应用创建 SVG 图标” | icon-design |
| “设计一套图标” | icon-design |

## 多 Skill 协作流程

### 新项目搭建

```
1. brand → Define identity
   - Colors, typography, voice

2. design-system → Create tokens
   - Primitive, semantic, component

3. ui-styling → Implement
   - Configure Tailwind, add components
```

### 设计体系迁移

```
1. brand → Audit existing
   - Extract brand colors, fonts

2. design-system → Formalize tokens
   - Create three-layer architecture

3. ui-styling → Update code
   - Replace hardcoded values
```

### 组件创建

```
1. design-system → Reference specs
   - Button states, sizes, variants

2. ui-styling → Implement
   - Build with shadcn/ui + Tailwind
```

## Skill 依赖关系

```
brand
    ↓ (colors, typography)
design-system
    ↓ (tokens, specs)
ui-styling
    ↓ (components)
Application Code
```

## 快捷命令

**品牌：**
```bash
node ../brand/scripts/inject-brand-context.cjs
node ../brand/scripts/validate-asset.cjs <path>
```

**令牌：**
```bash
node ../design-system/scripts/generate-tokens.cjs -c tokens.json
node ../design-system/scripts/validate-tokens.cjs -d src/
```

**组件：**
```bash
npx shadcn@latest add button card input
```

## 何时同时使用多个 Skill

需要**全部八个**时：
- 从零打造完整品牌包（logo → CIP → 演示文稿）

用 **brand + design-system + ui-styling** 时：
- 设计体系的搭建与实现

用 **logo-design + cip-design** 时：
- 完整品牌识别包，带交付物效果图

用 **logo-design + cip-design + slides** 时：
- 品牌路演：生成 logo、制作 CIP 效果图、搭建路演幻灯片

用 **banner-design + brand** 时：
- 社交媒体阵地：全平台品牌化横幅

用 **icon-design + design-system** 时：
- 与设计令牌、组件规格匹配的自定义图标集

用 **brand + design-system** 时：
- 只定义设计语言，不做实现

用 **design-system + ui-styling** 时：
- 把既有品牌落到代码里
- 构建组件库
