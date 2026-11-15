> **中文汉化版** · 上游：[caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram) · 原文件：`skills/designer/design/stack-diagram/references/tsx.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# TSX 输出

把构建好的 HTML 转成单个自包含的 React 组件，用户可直接放进代码库。几何和内容与 HTML 完全一致，变的只是包装形式。

## 形态

```tsx
// ArchDiagram.tsx — no props required, no dependencies
const ICONS = {
  hono: "data:image/svg+xml;base64,...",
  // one entry per node, copied from the built HTML's data URIs
} as const;

const T = {
  paper: "oklch(98.5% 0.004 250)",
  ink: "oklch(24% 0.02 258)",
  accent: "oklch(58% 0.2 256)",
  rule2: "oklch(83% 0.011 255)",
  // ... mirror every :root token: drop the "--color-" prefix and camelCase the rest
  // (--color-paper-2 → paper2, --color-rule-2 → rule2, --color-g1-ink → g1Ink, --color-accent-soft → accentSoft)
} as const;

export default function ArchDiagram() {
  return (
    <div style={{ overflowX: "auto", border: `1px solid ${T.rule2}`, borderRadius: 10 }}>
      <div style={{ position: "relative", width: 1000, height: 540, background: T.paper, /* grid via backgroundImage */ }}>
        {/* groups, svg edges, nodes — same coordinates as the HTML */}
      </div>
    </div>
  );
}
```

## 规则

- **自包含**：data-URI 图标放进一个 const，token 放进一个 const，内联 `style` 对象。不要 CSS 文件，不要假设 Tailwind，除 React 外不引入任何 import。它必须能在任意 TSX 项目里原样编译通过。
- **不要内嵌 woff2 字体。** 组件是装进一个自带字体管线的应用里。用 fallback 栈（`ui-monospace...`、`system-ui...`），并在开头注释里说明：加载 "Geist" / "JetBrains Mono" 可恢复参考外观。
- 把 CSS 类转成小的局部组件或映射后的样式对象（`<Node cx={342} top={190} icon="tanstack" name="TanStack Start" role="frontend / ssr" dark? />`）——这样文件可读、用户以后改起来也容易，而可改正是用户要 TSX 的意义。
- SVG 连线 overlay 原样搬过来（属性名改成 JSX 写法：`stroke-width` → `strokeWidth`、`marker-end` → `markerEnd`、`paint-order` → `paintOrder`）。
- 模板里的 hover 态（tile 上的 accent 边框）改成 `onMouseEnter`/`Leave` 状态，或干脆去掉——只在用户在意时才问。
- 以 `<Name>Diagram.tsx` 交付到工作区；不要把 TSX 当 artifact 发布（它是给用户仓库的代码，不是页面）。
