> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/html.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# HTML 语言提示词片段

## 核心概念

- **语义化元素**：`<main>`、`<nav>`、`<header>`、`<footer>`、`<article>`、`<section>` 构建有意义的结构
- **文档结构**：`<!DOCTYPE html>`、`<html>`、`<head>`、`<body>` 构成页面骨架
- **表单**：`<form>`、`<input>`、`<select>`、`<textarea>` 配合校验属性收集用户数据
- **可访问性**：`aria-*` 属性、`role`、`alt` 文本与语义化标记服务屏幕阅读器
- **Meta 标签**：`<meta>` 提供 viewport、字符集、描述、Open Graph 与 SEO 元数据
- **脚本与样式加载**：`<script>`、`<link>`、`<style>` 引入 JavaScript 与 CSS
- **Data 属性**：`data-*` 自定义属性存储元素专属数据
- **模板语法**：框架专属模板（Jinja/Django 用 `{{ }}`，ERB 用 `<%= %>`）
- **Web Components**：`<template>`、`<slot>`、Custom Elements 封装可复用组件

## 重要文件模式

- `index.html`：应用入口或 SPA 外壳
- `*.html` / `*.htm`：静态 HTML 页面
- `templates/**/*.html`：服务端模板文件（Django、Jinja2、Go templates）
- `public/index.html`：SPA 根文档（React、Vue）
- `*.ejs` / `*.hbs` / `*.pug`：模板引擎文件

## 边模式

- HTML 文件对通过 `<script>` 与 `<link>` 标签引入的 JavaScript 与 CSS 文件建立 `depends_on` 边
- 模板 HTML 文件对渲染它们的服务端代码建立 `depends_on` 边
- HTML 入口文件是构建系统与 Web 服务器的 `deploys` 目标
- HTML 文件与其渲染的组件或路由之间为 `related` 边

## 摘要风格

> "单页应用外壳：含 viewport meta、CSS reset 与 React 挂载根节点。"
> "服务端渲染模板：用 Django 模板继承组织导航、内容区与页脚。"
> "静态落地页：响应式布局、表单与第三方脚本集成。"
