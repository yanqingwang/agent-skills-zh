---
name: brand
description: 品牌语调、视觉识别、信息传达框架、素材管理与品牌一致性。当任务涉及品牌化内容、语气基调、营销素材、品牌合规或风格规范时启用本 Skill。
argument-hint: "[update|review|create] [args]"
metadata:
  author: claudekit
  version: "1.0.0"
---

> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/brand/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 品牌（Brand）

品牌识别、品牌语调、信息传达、素材管理与一致性框架。

## 何时使用

- 品牌语调定义与内容语气指引
- 视觉识别标准与风格规范制定
- 信息传达框架创建
- 品牌一致性审查与审计
- 素材整理、命名与审批
- 色板管理与字体排印规格

## 脚本路径

本 Skill 及其 `references/` 中的脚本路径，均相对于包含本 SKILL.md 的目录，而非相对于项目：`scripts/<file>` 指本 Skill 自己的 `scripts/` 文件夹；`../<skill>/scripts/<file>` 指随之一并安装的同级子 Skill。请基于该目录构建完整路径（Skill 加载时 Claude Code 会将其报告为 Skill 的基础目录），并将工作目录保持在项目根目录——脚本读取和写入项目文件（如 `docs/brand-guidelines.md`、`assets/design-tokens.json` 或 `src/`）时，都是相对于项目根目录进行的。

## 快速开始

**将品牌上下文注入提示词：**
```bash
node scripts/inject-brand-context.cjs
node scripts/inject-brand-context.cjs --json
```

**校验素材：**
```bash
node scripts/validate-asset.cjs <asset-path>
```

**提取/对比颜色：**
```bash
node scripts/extract-colors.cjs --palette
node scripts/extract-colors.cjs <image-path>
```

## 品牌同步工作流

```bash
# 1. Edit docs/brand-guidelines.md (or use /brand update)
# 2. Sync to design tokens
node scripts/sync-brand-to-tokens.cjs
# 3. Verify
node scripts/inject-brand-context.cjs --json | head -20
```

当检测到以下任一情况时，同步会停止：已存在的 token 文件；常见 CSS 入口文件及其本地 CSS 导入中的 `:root` 自定义属性或 Tailwind v4 `@theme` 变量；Tailwind 主题色与预设。在继续之前，请先核查工具报告的来源。如果检测到的文件是先前同步生成的受管 `assets/design-tokens.*` 输出，且替换它们正是你的本意，请加 `--force` 重新运行。

**同步的文件：**
- `docs/brand-guidelines.md` → 唯一事实来源
- `assets/design-tokens.json` → Token 定义
- `assets/design-tokens.css` → CSS 变量

## 子命令

| 子命令 | 描述 | 参考 |
|--------|------|------|
| `update` | 更新品牌识别并同步到所有设计系统 | `references/update.md` |

## 参考文档

| 主题 | 文件 |
|------|------|
| 语调框架 | `references/voice-framework.md` |
| 视觉识别 | `references/visual-identity.md` |
| 信息传达 | `references/messaging-framework.md` |
| 一致性 | `references/consistency-checklist.md` |
| 品牌规范模板 | `references/brand-guideline-template.md` |
| 素材组织 | `references/asset-organization.md` |
| 色板管理 | `references/color-palette-management.md` |
| 字体排印 | `references/typography-specifications.md` |
| logo 使用规则 | `references/logo-usage-rules.md` |
| 审批清单 | `references/approval-checklist.md` |

## 脚本

| 脚本 | 用途 |
|------|------|
| `scripts/inject-brand-context.cjs` | 提取品牌上下文，用于提示词注入 |
| `scripts/sync-brand-to-tokens.cjs` | 同步 brand-guidelines.md → design-tokens.json/css |
| `scripts/validate-asset.cjs` | 校验素材的命名、尺寸与格式 |
| `scripts/extract-colors.cjs` | 提取颜色并与色板对比 |

## 模板

| 模板 | 用途 |
|------|------|
| `templates/brand-guidelines-starter.md` | 面向新品牌的完整起始模板 |

## 路由

1. 从 `$ARGUMENTS` 解析子命令（第一个词）
2. 加载对应的 `references/{subcommand}.md`
3. 使用其余参数执行
