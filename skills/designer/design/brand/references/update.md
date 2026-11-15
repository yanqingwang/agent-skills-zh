> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/brand/references/update.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

更新品牌颜色、字体与风格，自动同步到所有设计系统文件。

<args>$ARGUMENTS</args>

## 概览

本命令系统性地更新：
1. `docs/brand-guidelines.md` - 人类可读的品牌文档
2. `assets/design-tokens.json` - token 的唯一事实来源
3. `assets/design-tokens.css` - 生成的 CSS 变量

## 工作流

### 第 1 步：收集品牌输入

用 `AskUserQuestion` 收集：

**主题选择：**
- 主题名（如 "Ocean Professional"、"Electric Creative"、"Forest Calm"）

**主色：**
- 颜色名（如 "Ocean Blue"、"Coral"、"Forest Green"）
- Hex 色值（如 #3B82F6）

**辅色：**
- 颜色名（如 "Golden Amber"、"Electric Purple"）
- Hex 色值

**强调色：**
- 颜色名（如 "Emerald"、"Neon Mint"）
- Hex 色值

**品牌情绪（用于 AI 图像生成）：**
- 情绪关键词（如 "professional, trustworthy, premium" 或 "bold, creative, energetic"）

### 第 2 步：更新品牌指南

编辑 `docs/brand-guidelines.md`：

1. **Quick Reference 表格** - 更新颜色名和 hex 色值
2. **Brand Concept 小节** - 更新主题名和描述
3. **Color Palette 小节** - 更新 Primary、Secondary、Accent 颜色及其色阶
4. **AI Image Generation 小节** - 更新基础 prompt、关键词、情绪描述词

### 第 3 步：同步到设计 token

运行同步脚本：
```bash
node scripts/sync-brand-to-tokens.cjs
```

如果脚本报告已存在 token 来源，先查看它点名的文件再继续。检测范围覆盖常见 CSS 入口文件及其本地导入中的 `:root` 自定义属性、Tailwind v4 `@theme` 变量，以及 Tailwind 主题颜色或预设。不要在这些来源旁边另建一套平行的 token 系统。只有当检测到的来源就是此前一次同步生成的受管 `assets/design-tokens.*` 输出、且你确实打算替换它时，才用 `--force`：
```bash
node scripts/sync-brand-to-tokens.cjs --force
```

这一步会：
- 把新的颜色名和值写进 `assets/design-tokens.json`
- 重新生成 `assets/design-tokens.css`，带正确的 CSS 变量

### 第 4 步：核验同步

确认所有文件都已更新：
```bash
# Check brand context extraction
node scripts/inject-brand-context.cjs --json | head -30

# Check CSS variables
grep "primary" assets/design-tokens.css | head -5
```

### 第 5 步：汇报

输出汇总：
- Theme: [name]
- Primary: [name] ([hex])
- Secondary: [name] ([hex])
- Accent: [name] ([hex])
- Files updated: brand-guidelines.md, design-tokens.json, design-tokens.css

## 修改的文件

| 文件 | 用途 |
|------|---------|
| `docs/brand-guidelines.md` | 人类可读的品牌文档 |
| `assets/design-tokens.json` | token 定义（primitive→semantic→component） |
| `assets/design-tokens.css` | UI 组件用的 CSS 变量 |

## 用到的 Skills

- `brand` - 品牌上下文提取与同步
- `design-system` - token 生成

## 示例

```bash
# Interactive mode
/brand:update

# With theme hint
/brand:update "Ocean Professional"

# Quick preset
/brand:update "midnight purple"
```

## 颜色预设

如果用户指定了预设名，用这些默认值：

| 预设 | 主色 | 辅色 | 强调色 |
|--------|---------|-----------|--------|
| ocean-professional | #3B82F6 Ocean Blue | #F59E0B Golden Amber | #10B981 Emerald |
| electric-creative | #FF6B6B Coral | #9B5DE5 Electric Purple | #00F5D4 Neon Mint |
| forest-calm | #059669 Forest Green | #92400E Warm Brown | #FBBF24 Sunlight |
| midnight-purple | #7C3AED Violet | #EC4899 Pink | #06B6D4 Cyan |
| sunset-warm | #F97316 Orange | #DC2626 Red | #FACC15 Yellow |

## 重要事项

- **三个文件必须同步** - 绝不只更新 brand-guidelines.md 一个
- **核验提取** - 更新后运行 inject-brand-context.cjs 确认
- **测试图像生成** - 可选：生成一张测试图，验证品牌应用效果
