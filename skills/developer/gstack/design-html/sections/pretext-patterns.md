<!-- AUTO-GENERATED from pretext-patterns.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`design-html/sections/pretext-patterns.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

### Pretext 接线模式

按 Step 2 选定的档位使用这些模式。它们是 Pretext API 的正确用法，
逐字照做。

**模式 1：基础高度计算（简单布局、卡片/网格）**
```js
import { prepare, layout } from '@chenglou/pretext'
// Vanilla HTML: omit the import; this code follows the inlined bundle in the same <script type="module">

// 1. PREPARE — one-time, after fonts load
await document.fonts.ready
const elements = document.querySelectorAll('[data-pretext]')
const prepared = new Map()

for (const el of elements) {
  const text = el.textContent
  const font = getComputedStyle(el).font
  prepared.set(el, prepare(text, font))
}

// 2. LAYOUT — cheap, call on every resize
function relayout() {
  for (const [el, handle] of prepared) {
    const { height } = layout(handle, el.clientWidth, parseFloat(getComputedStyle(el).lineHeight))
    el.style.height = `${height}px`
  }
}

// 3. RESIZE-AWARE
new ResizeObserver(() => relayout()).observe(document.body)
relayout()

// 4. CONTENT-EDITABLE — re-prepare when text changes
for (const el of elements) {
  if (el.contentEditable === 'true') {
    new MutationObserver(() => {
      const font = getComputedStyle(el).font
      prepared.set(el, prepare(el.textContent, font))
      relayout()
    }).observe(el, { characterData: true, subtree: true, childList: true })
  }
}
```

**模式 2：紧贴容器（聊天气泡）**
```js
import { prepareWithSegments, walkLineRanges } from '@chenglou/pretext'

// Tight-fit width: lay out at maxWidth, then shrink the bubble to its widest line
function shrinkwrap(text, font, maxWidth) {
  const segs = prepareWithSegments(text, font)
  let widest = 0
  const lineCount = walkLineRanges(segs, maxWidth, (line) => {
    widest = Math.max(widest, line.width)
  })
  return { width: Math.ceil(widest), lineCount }
}
```

**模式 3：文字绕排障碍物（编辑排版）**
```js
import { prepareWithSegments, layoutNextLine } from '@chenglou/pretext'

function layoutAroundObstacles(text, font, containerWidth, lineHeight, obstacles) {
  const segs = prepareWithSegments(text, font)
  let cursor = { segmentIndex: 0, graphemeIndex: 0 }
  let y = 0
  const lines = []

  while (true) {
    // Calculate available width at current y position, accounting for obstacles
    let availWidth = containerWidth
    for (const obs of obstacles) {
      if (y >= obs.top && y < obs.top + obs.height) {
        availWidth -= obs.width
      }
    }

    const result = layoutNextLine(segs, cursor, availWidth)
    if (!result) break

    lines.push({ text: result.text, width: result.width, x: 0, y })
    cursor = result.end
    y += lineHeight
  }

  return { lines, totalHeight: y }
}
```

**模式 4：逐行完整渲染（复杂编辑排版）**
```js
import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext'

const segs = prepareWithSegments(text, font)
const { lines, height } = layoutWithLines(segs, containerWidth, lineHeight)

// lines = [{ text, width, start, end }, ...] (no x/y: line i sits at y = i * lineHeight)
// Use for Canvas/SVG rendering or custom DOM positioning
lines.forEach((line, i) => {
  const span = document.createElement('span')
  span.textContent = line.text
  span.style.position = 'absolute'
  span.style.left = '0px'
  span.style.top = `${i * lineHeight}px`
  container.appendChild(span)
})
```

### Pretext API 参考

```
PRETEXT API CHEATSHEET:

prepare(text, font) → handle
  One-time text measurement. Call after document.fonts.ready.
  Font: CSS shorthand like '16px Inter' or 'bold 24px Georgia'.

layout(prepared, maxWidth, lineHeight) → { height, lineCount }
  Fast layout computation. Call on every resize. Sub-millisecond.

prepareWithSegments(text, font) → handle
  Like prepare() but enables line-level APIs below.

layoutWithLines(segs, maxWidth, lineHeight) → { lineCount, height, lines: [{text, width, start, end}...] }
  Full line-by-line breakdown (no x/y: line i is at y = i * lineHeight). For Canvas/SVG rendering.

walkLineRanges(segs, maxWidth, onLine) → lineCount
  Calls onLine({ width, start, end }) once per line at maxWidth (no text built).
  The widest line's width is the tight-fit container width. For chat bubbles.

layoutNextLine(segs, cursor, maxWidth) → { text, width, start, end } | null
  Iterator. Different maxWidth per line = text around obstacles.
  Start with cursor { segmentIndex: 0, graphemeIndex: 0 }; pass result.end next.
  Returns null when text is exhausted. Takes no lineHeight: advance y yourself.

clearCache() → void
  Clears internal measurement caches. Use when cycling many fonts.

setLocale(locale?) → void
  Retargets word segmenter for future prepare() calls.
```
