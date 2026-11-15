> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/icon-design.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 图标设计参考

用 Gemini 3.1 Pro Preview 做 AI 驱动的 SVG 图标生成。15 种风格、12 个分类、多尺寸导出。

## 脚本

| 脚本 | 用途 |
|--------|---------|
| `scripts/icon/generate.py` | 用 Gemini 3.1 Pro Preview 生成 SVG 图标 |

## 命令

### 生成单个图标

```bash
python3 scripts/icon/generate.py --prompt "settings gear" --style outlined
python3 scripts/icon/generate.py --prompt "shopping cart" --style filled --color "#6366F1"
python3 scripts/icon/generate.py --name "dashboard" --category navigation --style duotone
```

### 批量生成变体

```bash
python3 scripts/icon/generate.py --prompt "cloud upload" --batch 4 --output-dir ./icons
python3 scripts/icon/generate.py --prompt "notification bell" --batch 6 --style outlined --output-dir ./icons
```

### 生成多种尺寸

```bash
python3 scripts/icon/generate.py --prompt "user profile" --sizes "16,24,32,48" --output-dir ./icons
```

### 列出风格/分类

```bash
python3 scripts/icon/generate.py --list-styles
python3 scripts/icon/generate.py --list-categories
```

## CLI 选项

| 选项 | 说明 | 默认值 |
|--------|-------------|---------|
| `--prompt, -p` | 图标描述 | 必填 |
| `--name, -n` | 图标名（用于文件名） | - |
| `--style, -s` | 图标风格（15 种） | - |
| `--category, -c` | 图标分类，用作上下文 | - |
| `--color` | 主色 hex | currentColor |
| `--size` | 显示尺寸（px） | 24 |
| `--viewbox` | SVG viewBox 尺寸 | 24 |
| `--output, -o` | 输出文件路径 | 自动 |
| `--output-dir` | 输出目录（批量） | ./icons |
| `--batch` | 变体数量 | - |
| `--sizes` | 逗号分隔的尺寸 | - |

## 可用风格

| 风格 | 描边 | 填充 | 适用 |
|-------|--------|------|----------|
| outlined | 2px | none | UI 界面、Web 应用 |
| filled | 0 | solid | 移动应用、导航栏 |
| duotone | 0 | dual | 营销、落地页 |
| thin | 1-1.5px | none | 奢侈品牌、编辑排版 |
| bold | 3px | none | 标题区、hero 区 |
| rounded | 2px | none | 亲和应用、健康 |
| sharp | 2px | none | 科技、金融科技、企业 |
| flat | 0 | solid | Material 设计、Google 风 |
| gradient | 0 | gradient | 现代品牌、SaaS |
| glassmorphism | 1px | semi | 现代 UI、浮层 |
| pixel | 0 | solid | 游戏、复古 |
| hand-drawn | varies | none | 手作、创意 |
| isometric | 1-2px | partial | 技术文档、信息图 |
| glyph | 0 | solid | 系统 UI、紧凑场景 |
| animated-ready | 2px | varies | 交互 UI、引导流程 |

## 图标分类

| 分类 | 图标 |
|----------|-------|
| navigation | arrows, menus, home, chevrons |
| action | edit, delete, save, download, upload |
| communication | email, chat, phone, notification |
| media | play, pause, volume, camera |
| file | document, folder, archive, cloud |
| user | person, group, profile, settings |
| commerce | cart, bag, wallet, credit card |
| data | chart, graph, analytics, dashboard |
| development | code, terminal, bug, git, API |
| social | heart, star, bookmark, trophy |
| weather | sun, moon, cloud, rain |
| map | pin, location, compass, globe |

## SVG 最佳实践

- **viewBox**：用 `0 0 24 24`（标准）或 `0 0 16 16`（紧凑）
- **颜色**：用 `currentColor` 走 CSS 继承，避免写死颜色
- **无障碍**：始终带上 `<title>` 元素
- **优化**：路径节点尽量少，不内嵌字体或位图
- **尺寸**：按 24px 设计，在 16px 和 48px 下测清晰度
- **描边**：outlined 类风格用 `stroke-linecap="round"` 和 `stroke-linejoin="round"`

## 模型

- **gemini-3.1-pro-preview**：最佳思考、token 效率、事实一致性
- 纯文本输出（SVG 是 XML 文本），不需要图像生成 API
- 支持结构化输出，保证 SVG 格式一致

## 工作流

1. 描述图标 → `--prompt "settings gear"`
2. 选风格 → `--style outlined`
3. 生成 → 脚本输出 .svg 文件
4. 可选批量 → `--batch 4` 出变体
5. 多尺寸导出 → `--sizes "16,24,32,48"`

## 环境准备

```bash
export GEMINI_API_KEY="your-key"
pip install google-genai
```
