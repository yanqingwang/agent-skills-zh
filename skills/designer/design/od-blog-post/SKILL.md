---
name: blog-post
description: |
  一篇长文 / 博客文章：报头、主视觉图片占位、
  含插图与引言的正文、作者署名、相关文章。
  当简报要求 "blog"、"article"、"post"、"essay" 或
  "case study" 时使用。
triggers:
  - "blog"
  - "blog post"
  - "article"
  - "essay"
  - "case study"
  - "newsletter"
  - "博客"
  - "文章"
od:
  mode: prototype
  platform: desktop
  scenario: marketing
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [typography, typography-hierarchy, typography-hierarchy-editorial, rtl-and-bidi]
---

> **中文汉化版** · 上游：[nexu-io/open-design](https://github.com/nexu-io/open-design) · 原文件：`design-templates/blog-post/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 博客文章 Skill

生成一个长文文章页面，采用编辑式排版，不含界面外壳。

## 工作流

1. **阅读当前生效的 DESIGN.md**（已在上方注入）。充分运用排版
   token：长文里排版占 70%、图片占 20%、界面外壳占 10%。
2. **选定主题**，从简报取材，写一篇真实文章：至少 600
   词，分布在 4–6 个 H2 章节。不要用 lorem ipsum 占位文本。
3. **各章节**，按顺序：
   - **报头**：小巧的文字标识 + 4–6 个导航链接，样式朴素。
   - **文章头部**：分类眉标、大标题（display token，大号）、
     导语（1–2 句副标题）、作者姓名 + 职务 + 日期。
   - **主视觉图**：用带 DS 色调的渐变或纯色填充做一块 16:9 占位块（不使用外部图片），
     下方加 1 行图注。
   - **正文**：交替排布的正文段落，至少包含：
     - 1 处引言（大号展示字体，在 inline-start 一侧加强调线条，使布局在 `dir="rtl"` 下能正确翻转）。
     - 1 个插图（图片占位 + 图注）。
     - 1 个列表（有序或无序）。
     - 1 处行内引用。
   - **作者页脚**：作者头像（圆圈内放姓名首字母）、简介段落。
   - **相关文章**：3 张链接到其他文章的卡片。每张卡片含小图片块、
     标题、1 行摘要、日期。
4. **编写**单个 HTML 文档：
   - 从 `<!doctype html>` 到 `</html>`，CSS 内联。
   - 正文使用 DS 正文字体，居中，最大宽度按 DS 布局
     规则设定（通常为 680–720px）。
   - 仅当 DS 风格偏编辑式 / 衬线时才用首字下沉（`first-letter`），
     技术风 DS 则跳过。
   - 在大标题、主视觉、正文、引言、相关文章网格上加 `data-od-id`。
5. **自检**：
   - 字体层级明确无误：H1 就是大标题，H2 用作章节分隔，引言不与 H1 争抢视觉重心。
   - 正文每行 60–75 字符。
   - 强调色最多出现两处（眉标 + 引言线条，或一处链接）。
   - 页面读起来像杂志，而非营销落地页。

## 输出约定

在 `<artifact>` 标签之间输出：


```
<artifact identifier="post-slug" type="text/html" title="Article Title">
<!doctype html>
<html>...</html>
</artifact>
```


在制品之前只写一句话，之后不放任何内容。
