> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/texture.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 纹理与印刷质感：一份有预算的词汇表

只在所选主题配得上纹理（见下方亲和表）或自定义绘制的血统是印刷时加载。纹理是有预算的处理手法，绝不是氛围：每页一个质感家族，不透明度进令牌，绝不做动画，正文之下最多轻声一层。到处抹颗粒是 `flow.md` § Harnesses 拒绝的癖好；来自本文件、用在配得上它的主题上的颗粒，是手艺。

## 预算（约束每件质感）

- **每页一个质感家族。**颗粒、半调网、套印错位、扫描线或毛边，绝不同时两个。riso 印刷是一个家族：它的颗粒与套印错位来自同一个滚筒。作为照片处理手段的半调网属于图像，不属于页面，不计入。
- **不透明度进令牌，在令牌块中声明：**`--texture-opacity` 全页 <= 0.08，限定在卡片或版面内 <= 0.15。正文行文之下 <= 0.05 或为零。低频薄染（base frequency 0.02 或更低：纤维、纸张色调）是染色而非斑点，全页可到 0.12，对比度按最终结果测量。
- **绝不做动画。**颗粒不漂移，圆点不脉动。
- 每个覆盖层都加 **`pointer-events: none` 与 `aria-hidden="true"`**；纹理绝不拦截输入，复古信号是氛围，绝不是画出来的显示器外壳（47a）。
- **性能：**纯 CSS 或 data-URI SVG 滤镜；纹理不发图片请求。

## 1 · 颗粒（纸张）

斑点颗粒，令牌化：

```css
:root { --texture-opacity: 0.08; }
.grained { position: relative; isolation: isolate; }
.grained::after {
  content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 1;
  background-size: 200px 200px; opacity: var(--texture-opacity);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 -4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
}
```

颜色矩阵把噪声变成离散斑点（alpha = 噪声 × 9 − 4），颗粒因此在预算内 1x 就能读出；未处理的 `feTurbulence` 在这些不透明度下是一层没人看得见的雾。暗色地面上斑点必须是亮的：把矩阵前三行改成 `0 0 0 0 1`，让每个斑点是白色，不透明度保持。用在版面、一张强调卡上，或主题点名颗粒时全页 0.08 及以下。

## 2 · 半调网（点阵）

一个带尺寸令牌的网点屏：

```css
:root { --halftone-size: 12px; --halftone-dot: 1.5px; }
.halftone { background-image: radial-gradient(var(--color-ink) var(--halftone-dot), transparent var(--halftone-dot));
  background-size: var(--halftone-size) var(--halftone-size); }
```

用于版面填充与区块色带。绝不在文字之下或与文字重叠。圆点用墨色或一个专色，强调色绝不整面铺满。

## 3 · 套印错位（色差回声）

Riso 的招牌，可移植到任何印刷血统的自定义方案：

```css
.misreg { position: relative; display: inline-block; isolation: isolate; }
.misreg::before, .misreg::after {
  content: attr(data-text); position: absolute; inset: 0; z-index: -1;
  white-space: nowrap; pointer-events: none;
}
.misreg::before { color: var(--color-accent);   transform: translate(-2px, -2px); }
.misreg::after  { color: var(--color-accent-2, var(--color-focus)); transform: translate(2px, 2px); }
```

**每页一个焦点词，放在首屏，在主题的 `waive 38iii` 之下；绝不用于每个标题。**span 是行内块，无论标题行高如何，副本都贴在字形上；它们印在墨色之后，词保住自己的颜色，只有边缘带走回声。回声色是主题声明的专色油墨（此处为 `--color-accent` 与 `--color-accent-2`，或主题自己的回声令牌）；偏移保持 1 到 3px（再大读起来就是坏的，不像印出来的）。至多在加载时随 `--dur-long` 落定一次，减少动效下保持静止；绝不循环。

## 4 · 扫描线（CRT）

Arcade 的配方；复古信号是氛围，绝不是画出来的显示器外壳（47a）：

```css
:root { --scanline: oklch(from var(--color-ink) l c h / 0.06); }
body::after { content: ""; position: fixed; inset: 0; z-index: var(--z-raised);
  pointer-events: none;
  background: repeating-linear-gradient(transparent 0 2px, var(--scanline) 2px 3px); }
```

`--scanline` 是低透明度的页内装饰令牌。仅限 Arcade 及其近似血统的自定义方案。

## 5 · 毛边（纸缘）

用于印刷血统页面上的版面、票券与票根：

```css
.deckled { box-shadow: inset 0 0 0 1px var(--color-rule);
  mask-image: radial-gradient(6px at 0 50%, transparent 97%, black);
  mask-size: 12px 24px; mask-repeat: repeat-y; mask-position: left; }
```

每页一条边、一个元素类（票券边缘、邮票齿孔）。一般绝不用在卡片上；它是质感件，不是边框样式。

## 亲和：谁配得上纹理

主题在其表面章节点名某种质感，才算配得上；自定义绘制的血统是印刷（risograph、活版印刷、票券纸、行式打印机）才算配得上，并选用该血统用过的那一件质感。上面的预算约束每个主题，无论其文件怎么写：全页颗粒 0.08 及以下，单个版面内 0.15，行文之下 0.05 或为零。例子：Riso（颗粒与套印错位）、Halftone（网点屏）、Paste-up（纤维薄染）、Darkroom（胶片颗粒）、Arcade（扫描线）。

**绝不做：**主题未点名的质感、modern-minimal 页面上的颗粒、一页两个质感家族，或因为页面显得平而把质感当氛围铺满一切。

## 减少动效与无障碍

只有落定一次的套印错位会动，其余一律不动；这里的一切在 `prefers-reduced-motion: reduce` 下表现完全一致，因为没有任何动画。纹理绝不把文本对比度降到 gate-40/41 阈值之下：在加了质感的最终结果上测对比度，不是在平色令牌上。
