---
name: hackernews-frontpage
description: 抓取 Hacker News 首页（标题、票数、评论数）。
host: news.ycombinator.com
trusted: true
source: human
version: 1.0.0
args: []
triggers:
  - scrape hacker news frontpage
  - scrape hn frontpage
  - get hn top stories
  - latest hacker news stories
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`browser-skills/hackernews-frontpage/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Hacker News 首页抓取器

抓取 Hacker News（`news.ycombinator.com`）首页，返回排名前 30 的故事
（JSON 格式）。每条故事含排名、标题、链接 URL、票数和评论数。

## 用法

```
$ $B skill run hackernews-frontpage
{
  "stories": [
    { "rank": 1, "title": "...", "url": "...", "points": 412, "comments": 87 },
    ...
  ],
  "count": 30
}
```

## 工作原理

1. 通过 daemon 访问 `https://news.ycombinator.com`。
2. 读取页面 HTML。
3. 把每行故事（HN 稳定的 `tr.athing` 结构）解析为类型化的
   `Story` 记录。
4. 在 stdout 输出单个 JSON 文档。

## 为什么它是参考 Skill

`hackernews-frontpage` 是最小而完整的浏览器 Skill：无需登录、HTML 稳定、
输出确定、便于文件 fixture。每个 Phase 1 组件（SDK、受限 token、三层
查找、spawn 生命周期）都被 `$B skill run hackernews-frontpage` 和随附的
`script.test.ts` 覆盖。

当 HN 的 HTML 改版、选择器失效时，测试会在用户察觉之前、基于已捕获
的 fixture 先失败。这就是它的意义。
