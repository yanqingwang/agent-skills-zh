> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/anatomy/references/react.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# React 与 Next.js

## 单个 figure 的文件布局
```
components/iso/                 the kit: iso-kit.ts, iso.css, react/draw.tsx, react/live.tsx
components/figures/rig/
  model.ts       pure model: true numbers, springs, readout text (no DOM)
  view.ts        world layout constants, the projection P (fitProjection), helpers like at(point)
  geometry.ts    every static path, computed once at module load
  frame.ts       paths for the parts that change shape: frameOf(state) -> { glass, coils, needle, ... }
  art.tsx        server component: static parts as JSX constants, passed to the live component
  live.tsx       "use client": refs, loop, pointer and keyboard, aria, writes the readout
  rig.css        scoped tokens and styles (e.g. .rig { … })
  figure.tsx     <Plate fig title hint readout keys caption><RigArt /></Plate>
```
`examples/test-rig/` 采用这一布局。它用到 `rig.ts`、`view.ts`、`geometry.ts`、`pose.ts`、`art.tsx`、`live.tsx` 与 `figure.tsx`。

## 服务端/客户端分工
- 几何计算是纯 TypeScript，跑在服务端，客户端拿到的是现成的 path 字符串。除非某个运动部件需要每帧重算，否则不向客户端发送任何几何代码；需要时，`frame.ts` 由 `live.tsx` 导入并发往客户端。
- `art.tsx` 把静态部件构建成 JSX（`<Solid paths={BASE_ART.slab} tone="mid" />` 等），并作为元素 props（如 `base`、`rail`、`carriage`、`dial`）传给 `"use client"` 的 live 组件。live 组件按画家顺序摆放它们，并把运动部件包进 `<g ref>`。
- 只有 live 组件和 `kit/react/live.tsx` 是客户端代码。`draw.tsx` 可安全地在服务端运行。

## 大页面 key 警告陷阱
大页面上服务端负载很大，React 会把一些元素 props 作为延迟（lazy）分块流式传输。客户端把 `{props.dial}` 渲染在同级元素中间。React 无法把一个 lazy 标记为已做 key 检查，所以一旦 lazy 解析成一个没有 key 的元素，React 就会记录 "Each child in a list should have a unique key"，指向你的 live 组件或 `IsoFigure`。同一个 figure 放在小测试页上什么都不会打印，所以逐个检查 figure 会漏掉它。

有两个修法，应该从一开始就两个都做：

1. **给每个元素 prop 的根节点一个稳定 key：** `const DIAL = (<g key="dial">…</g>)`，fragment 用 `<React.Fragment key="sled">`。单元素上加 key 没有任何代价。
2. **不要把 `"use client"` 组件放进服务端构建的静态图里。** 服务端树内的每个客户端组件元素都会变成 lazy 引用，连带把它的所有祖先也变成 lazy。如果图的部分部件需要交互（比如悬停高亮），把它们写成普通的 `<g data-part="…">`，事件在 live 组件里用事件委托处理。

用 `.map` 构建的数组照常需要 key。

## 样式
- `iso.css` 只导入一次，全局或在该 figure 内。在包裹元素（或 `<body>`）上放 `className="iso"` 以获得 tokens，浅色主题再加 `data-theme="light"`。
- 把每个 figure 自己的 tokens 限定在该 figure 的类里（`.rig { --rig-glass-top: … }`），仅在卡片需要时才在 `.iso-plate` 内覆盖 kit 的 tokens。
- 不要把 figure 的 tokens 放到 `:root` 上。

## Readout
`useReadout()` 从其 `anchor` 出发找到最近的 `.iso-plate [data-readout]`，`say(text)` 直接写入读数而不触发重渲染。静止文本在服务端渲染好，水合之前就是对的。

## Hydration（水合）
静止姿态在服务端和客户端首次渲染时都渲染；运动只在 effect 里启动。渲染期间不要读 `window`。`asksForStillness()` 是安全的，因为它只在 effect 和循环内被调用。
