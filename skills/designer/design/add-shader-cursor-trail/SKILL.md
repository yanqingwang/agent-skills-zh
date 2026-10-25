---
name: add-shader-cursor-trail
description: "添加 Tidal Commons 首屏（hero）所使用的 Shaders WebGPU 鼠标特效：由 ChromaFlow 驱动的白色闪烁半调（halftone）cursor trail，经 DotGrid 遮罩，辅以色差波纹（chromatic ripples）与胶片颗粒，并配有静态、触屏、无障碍、SSR 和性能多重回退保护。当用户询问这种 shader 鼠标特效、halftone cursor trail、交互式 WebGPU hero/contact 背景，或可在 React、Next.js、Vue、Svelte、Solid 或纯 Web 项目中复用的 cursor 跟随 shader 层时使用。"
---

> **中文汉化版** · 上游：[MengTo/Skills](https://github.com/MengTo/Skills) · 原文件：`agent-skills/web-design/add-shader-cursor-trail/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 添加 Shader Cursor Trail

将这一 trail 作为渐进增强（progressive enhancement）精确实现。保留宿主区块的语义内容、图像、控件和静态首帧。

## 工作流程

1. 检查框架、渲染模式、现有的动效技术栈、图层顺序、reduced-motion 规则和包管理器。不要引入另一套平滑滚动（smooth-scroll）引擎，也不要替换该区块的内容。
2. 使用现有的包管理器安装 `shaders`。从匹配的框架子路径导入：`shaders/react`、`shaders/vue`、`shaders/svelte` 或 `shaders/solid`。
3. 实现之前先阅读 [references/implementation.md](references/implementation.md)。保持六个 shader 节点及其顺序、两个不可见驱动（invisible driver）和两条 ID 关联完全一致。
4. 对于 React 或 Next.js，复制并适配 `assets/react/` 中的文件。将轻量级能力门（capability gate）与重量级 shader 模块分开保存，以免不符合条件的访客请求 shader bundle。
5. 在区块内容背后放置一个全出血（full-bleed）、`aria-hidden="true"` 的 shader 层。让链接和控件位于其上方。除非已验证 cursor 跟踪使用的是全局事件，否则不要在 canvas 上设置 `pointer-events: none`。
6. 以 WebGPU、精细悬停指针（fine hover pointer）、正常 motion/transparency 偏好、文档可见性、窗口焦点和区块交叉可见（intersection）作为加载门控。当区块离开视口时卸载，使 GPU 工作停止。
7. 保留原始图像或深色背景作为完整回退。对 reduced motion、reduced transparency、粗指针/无悬停指针和强制色彩（forced colors）场景隐藏该层。
8. 只调整呈现类变量，如透明度和混合模式（blend mode）。不要把节点图改成装饰性噪声，不要添加 WebGL/Three.js，也不要热链（hotlink）Shaders 预览资源。

## 验证

运行项目的 lint、typecheck/测试和生产构建。对于 React 实现，还要运行：

```bash
node /path/to/add-shader-cursor-trail/scripts/verify-cursor-trail.mjs \
  path/to/CursorTrailShader.tsx \
  path/to/CursorTrailGate.tsx \
  path/to/cursor-trail.css
```

验证以下场景：JavaScript 不可用时的静态区块、键盘可访问该层上方的内容、触屏行为、reduced motion、不支持 WebGPU、焦点/可见性清理，以及运行时不存在对 `previews.shaders.com` 或 `data.shaders.com` 的请求。

报告所选的混合模式、回退方案、能力门、生产构建结果以及任何浏览器限制。除非确实在兼容的浏览器中执行过 WebGPU 视觉验证，否则不要声称已验证。
