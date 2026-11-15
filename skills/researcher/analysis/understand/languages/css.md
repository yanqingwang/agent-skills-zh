> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/css.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CSS 语言提示词片段

## 核心概念

- **选择器**：元素、类（`.name`）、ID（`#name`）、属性（`[attr]`）与伪类（`:hover`）定位
- **优先级**：内联 > ID > 类 > 元素的层叠优先级，决定哪条规则胜出
- **盒模型**：`margin`、`border`、`padding`、`content` 尺寸控制元素大小
- **Flexbox**：`display: flex` 配合 `justify-content`、`align-items` 做一维布局
- **Grid**：`display: grid` 配合 `grid-template-columns/rows` 做二维布局
- **自定义属性（变量）**：`--name: value` 配合 `var(--name)` 定义可复用的设计 token
- **媒体查询**：`@media (max-width: ...)` 定义响应式断点
- **SCSS/Sass 特性**：嵌套、`$variables`、`@mixin`、`@include`、`@extend`、`@use`、`@forward`
- **CSS Modules**：作用域化的类名（`.module.css`），避免全局样式冲突
- **层叠层**：`@layer` 显式控制层叠顺序

## 重要文件模式

- `*.css`：标准 CSS 样式表
- `*.scss` / `*.sass`：Sass/SCSS 预处理器文件
- `*.less`：Less 预处理器文件
- `*.module.css` / `*.module.scss`：CSS Modules（作用域化样式）
- `globals.css` / `reset.css` / `normalize.css`：全局基础样式
- `tailwind.config.js`：Tailwind CSS 配置（虽是 JS 文件）
- `variables.scss` / `_variables.scss`：设计 token 定义

## 边模式

- CSS 文件与导入它们做样式化的 HTML 或组件文件之间为 `related` 边
- 主样式表 `@use` SCSS 分部文件（`_*.scss`）时对其建立 `depends_on` 边
- CSS 变量定义文件与引用这些变量的所有样式表之间为 `related` 边
- CSS Modules 与导入它们的组件文件之间为 `related` 边

## 摘要风格

> "全局样式表：为设计系统的色板与字体定义 CSS 自定义属性。"
> "响应式布局样式：用 flexbox 与 grid 为仪表盘页面覆盖 3 个断点。"
> "SCSS 分部文件：定义间距、阴影与媒体查询断点的共享 mixin。"
