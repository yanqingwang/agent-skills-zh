> **中文汉化版** · 上游：[MengTo/Skills](https://github.com/MengTo/Skills) · 原文件：`agent-skills/web-design/add-shader-cursor-trail/references/implementation.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 光标轨迹实现契约

## 目录

- 安装
- 精确的 shader 图
- 分层
- 能力与生命周期门槛
- 框架适配
- 验证清单
- 常见故障

## 安装

用项目现有的包管理器安装 `shaders`。框架入口以 <https://shaders.com/docs/guide> 的文档为准。Vite 项目不要把 `shaders` 加进 `optimizeDeps.exclude`；它的依赖需要正常预打包。

shader 模块使用仅客户端渲染。语义区块及其静态背景必须保持可服务端渲染。React/Next 项目可以用 `assets/react/` 里的模板；门槛组件会把动态导入推迟到能力检查通过之后。

## 精确的 shader 图

只使用一个 `Shader` 根节点。子组件严格按以下顺序排列：

1. `DotGrid`：`id="trailDots"`、`density={40}`、`twinkle={0.9}`、`visible={false}`。用一个内联映射驱动 `dotSize`，来源 `source: "trailFlow"`，通道 `alpha`，输入 `0..1`，输出 `0..1`。
2. `ChromaFlow`：`id="trailFlow"`、`intensity={1.4}`、`radius={2.9}`、`visible={false}`。
3. `LinearGradient`：`#1e1e1f` 到 `#070708`，HSL，起点 `{x:0,y:1}`，终点 `{x:1,y:0}`。
4. `LinearGradient`：`#000000` 到 `#ffffff`，HSL，端点同上，`maskSource="trailDots"`。
5. `CursorRipples`，使用默认值。
6. `FilmGrain`，`strength={0.1}`。

这些不可见组件是数据源，不是死代码。`trailFlow` 控制圆点大小；`trailDots` 给白色渐变做遮罩。删掉任一不可见组件，或弄断任一 ID 链接，可见的轨迹就会消失。

框架 API 支持时，关闭库的遥测（telemetry）。图的 props 保持静态，不要放进组件 state。

## 分层

使用以下语义结构：

```text
section.cursor-trail-region (position: relative; isolation: isolate; overflow: hidden)
├─ static image or dark background (always present)
├─ div.cursor-trail-layer[aria-hidden=true] (absolute, full bleed)
│  └─ capability gate → one Shader canvas
└─ semantic content and controls (relative; higher z-index)
```

照片型 hero 区块，先用 `mix-blend-mode: screen`，不透明度取 `0.72–0.82` 左右。近黑色的独立区块用正常混合，让图中的深色渐变直接充当区块背景。绝不为效果牺牲文字对比度。

不要在链接上方再叠一个单独捕获指针的元素。让内容处于更高的堆叠层级，保证可点击。先在非交互区和交互区分别测试光标响应，再决定 canvas 能否忽略指针事件。

## 能力与生命周期门槛

所有条件都通过才加载并挂载 shader：

- 存在 `navigator.gpu`。
- 匹配 `(hover: hover) and (pointer: fine)`。
- 不匹配 `prefers-reduced-motion: reduce`。
- 不匹配 `prefers-reduced-transparency: reduce`。
- 文档可见，且窗口持有焦点。
- `IntersectionObserver` 报告区块已进入视口附近。

监听偏好设置、可见性、blur、focus 的变化。清理时断开 observer，并移除全部监听器。卸载 shader 就是暂停机制；不要留下一个隐藏的持续 GPU 循环在屏幕外空转。

在 JavaScript 门槛之外再加 CSS 媒体查询兜底。无障碍偏好发生变化时，CSS 能防止初始化过晚或失败导致 canvas 被暴露出来。

## 框架适配

React/Next：使用 `assets/react/` 里的双模块模式。`CursorTrailGate.tsx` 很轻量，只在资格检查通过后才懒加载 `CursorTrailShader.tsx`。App Router 项目中，两个文件都保持为 client component。

Vue、Svelte 或 Solid：把同样的拆分搬过去，变成一个轻量宿主组件加一个动态导入的 shader 组件。从框架专属的 Shaders 子路径导入。shader props 保持静态字面量，图的顺序和 ID 不变。

纯 JavaScript：如果有的话，遵循 Shaders 当前的 plain-JS 指南。保留同样的能力检查和静态兜底；不要用无关的 canvas 实现重造这个效果，还声称它就是这套图。

## 验证清单

- 只有一个 canvas、一个 shader 引擎。
- 图的顺序和两条 ID 链接保持精确不变。
- 服务端渲染的 HTML 里存在静态内容。
- 键盘聚焦和激活在 canvas 之上正常工作。
- 框架允许条件加载时，不支持 WebGPU、纯触屏或减弱动态的路径不请求任何 shader chunk。
- shader 在离开屏幕、失焦、标签页隐藏时都会卸载。
- 减弱动态、减弱透明度、强制配色、粗指针都会隐藏该层。
- 生产构建、lint 和重点测试通过。
- 不热链（hotlink）Shaders 的预览/数据域名。

## 常见故障

- 有渐变但看不到圆点：恢复 `source: "trailFlow"`、`id="trailFlow"`、`maskSource="trailDots"` 和 `id="trailDots"`。
- 到处都是静止的圆点：让 `dotSize` 保持为内联映射驱动，且两个驱动组件都设 `visible={false}`。
- 链接失效：修好堆叠层级；不要在内容上方放捕获指针的包裹元素。
- SSR 或 hydration 失败：把 Shaders 导入隔离在仅客户端的动态加载模块里。
- 初始包体积过大：在导入 shader 模块之前，先把能力检查挪进一个轻量门槛。
- GPU 在屏幕外仍在运行：用 `IntersectionObserver` 卸载，并清理 visibility/focus 监听器。
