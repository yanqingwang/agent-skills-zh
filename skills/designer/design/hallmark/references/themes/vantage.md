---
name: Vantage
slug: vantage
genre: modern-minimal
paper: dark 13.5 235
display: grotesk-sans Geologica
accent: chromatic-lime 126
posture: restrained
keywords: lidar, scan, survey, mapping, 3d, spatial, point cloud, robotics, autonomy, drone, construction, digital twin, geospatial, measurement, sensor, inspection, engineering, heritage, digitisation, infrastructure, reality capture, terrain
material: blue-black ground, a live point cloud of the real thing as the hero's light, a sweep that lights it, pale steel ink, Geologica with sharpened corners at a light weight, hairline frames with corner ticks, one lime signal for what was found
pictured: Feature Ledger, Stage hero
photo: muted con=6 sat=-20
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/vantage.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Vantage

夜里的现实捕捉：事物本身（一处工地、一道山脊、一件物体）被渲染成数万个测得的点，落在蓝黑底上缓慢旋转，一道扫掠穿过并点亮它们。四周的页面是仪器般的安静：削尖了角的 Geologica、钢灰墨色、只标出四角的发丝线框、带单位的数字。一个青柠信号表示：发现了、测过了、在实时。它不是粒子网络，不是霓虹赛博页，也不是发光贴片的仪表盘。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(13.5% 0.012 235); --color-paper-2: oklch(17% 0.014 235); --color-paper-3: oklch(21% 0.016 235);
  --color-ink: oklch(95% 0.006 230); --color-ink-2: oklch(82% 0.012 230); --color-muted: oklch(66% 0.016 230);
  --color-rule: oklch(27% 0.014 235); --color-rule-2: oklch(34% 0.016 235);
  --color-accent: oklch(89% 0.19 126); --color-accent-hi: oklch(93% 0.17 126); --color-accent-ink: oklch(19% 0.04 126); --color-focus: oklch(89% 0.19 126);
  --point-lo: oklch(42% 0.04 245); --point-mid: oklch(70% 0.04 232); --point-hi: oklch(96% 0.02 215);
  --color-slot: oklch(21% 0.016 235);
  --font-display: "Geologica", ui-sans-serif, system-ui, sans-serif; --font-body: "Geologica", ui-sans-serif, system-ui, sans-serif;
  --radius-card: 4px; --radius-pill: 999px; --rule-hair: 1px; --tick: 10px;
  --shadow-card: none;
  --tracking-display: -0.035em; --display-weight: 300;
}
```

两个旋钮，写入 stamp（印记）：`vantage: terrain/steel`。同一次运行里的两个 Vantage 页面，两者都不同。

| 旋钮 | 选项 |
| --- | --- |
| **主体**（点云是什么） | `terrain`（默认）：自上方斜角看地面、构筑物与树冠。`object`：一件物体被整体扫描，绕轴旋转。`interior`：从内部看一个房间或隧道 |
| **配色** | `steel`（默认），如上。`sodium`：底 `oklch(13% 0.012 55)`，点从 `oklch(40% 0.05 50)` 到 `oklch(95% 0.03 80)`，墨色偏暖，青柠保留为信号色 |

## 字体（Type）

- **展示字体：**Geologica 300 加 `"SHRP" 100`（削尖的角），`--tracking-display`，行高 1.0，句首大写；小标题用 400。标题短，坐在干净地面上，绝不压在密集点云上。
- **正文：**Geologica 300，17px，`"SHRP" 0`，行高 1.6，用 `--color-ink-2`。
- **测量值：**Geologica 400，`tabular-nums`，单位小一档、用 `--color-muted`，前面留一个细空格；陈述字号的大数字用 200。标签用 Geologica 400 小一档，句首大写。绝不用等宽，绝不用加字距的大写。

## 表面（Surfaces）

- **点云：**一块只含点的生成画布或 WebGL 场景，点之间不连线，不发光：大小随距离，颜色随高度从 `--point-lo` 到 `--point-hi`，一层柔和的深度淡出。一道扫掠平面每隔几秒经过，把触到的点抬向白；任何被发现的点都是青柠。它充满 Hero，在标题旁边或身后，向边缘淡出到纸色。
- **框：**发丝线 `--color-rule` 框只画四角（`--tick` 长度的刻度），围住一个被测量的东西或一块面板；完整的发丝线框只给输入框。圆角至多 `--radius-card`。
- **引注：**一个测得的点带一条指引线（发丝线，点端一个 3px 圆点）指向它的数字与单位；一块屏幕至多两个。
- **色带：**paper，加一条安静的 paper-2 色带；无受光或染色色带。深度是平的，无阴影。
- **照片：**平光日光下的真实工地或物体，压低色彩，`--radius-card`；绝不用科幻渲染图。

## 版式（Range）

- **一个剖面：**穿过点云的一片薄切片，通栏展开成一排点的轮廓，两三个高度用指引线与数字标出。
- **扫描日志排成表格：**一行行采集记录，日期、面积、点数与精度用表格数字，进行中的一行以青柠圆点标记。
- **图层化作可用开关：**地面、构筑物、树冠与发现的物体排成划线的开关列表，真的会重新着色或隐藏旁边的点云。
- **一个被测量的数字：**陈述字号的一个数字收在四角刻度内，容差在下方用淡色。

## 控件（Controls）

- 主胶囊：`--color-accent` 之上覆 `--color-accent-ink`，48px，Geologica 400；悬停取 `--color-accent-hi`。次按钮：`--color-rule-2` 发丝线胶囊，墨色文字。
- 输入框：`--color-paper-2` 凹槽带发丝线框，青柠光标与焦点。开关打开时转青柠。
- 青柠只标记被发现、实时或主要的东西；绝不做标题，也绝不做大于胶囊的填色。

## 动效（Motion）

点云缓慢旋转（两分钟一圈，物体七十秒），扫掠每六到八秒经过一次、缓入缓出，指针让视角倾斜几度。面板与行淡入一次。画布在屏幕外暂停。Reduced motion（减少动效）：一帧静止，扫掠停在场景中途。

## 语气（Voice）

测过才说的精确：扫了什么、多大、多准、多快。

## 禁止事项（Do-nots）

- 绝不连点成线，绝不发光或辉光，绝不铺向地平线退去的网格地面。
- 点上除青柠表示发现外，绝不用第二种色相。
- 绝不让点云压在正文之下或藏在表单后面。
- 绝不用等宽标签；数字用表格数字的 Geologica。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght,CRSV,SHRP@200..500,0,0..100&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); font-variation-settings: "SHRP" 100; letter-spacing: var(--tracking-display); line-height: 1; }
body { font-weight: 300; font-variation-settings: "SHRP" 0; }
.num { font-variant-numeric: tabular-nums; font-weight: 400; } .num .u { color: var(--color-muted); font-size: 0.75em; }
.ticks { position: relative; } .ticks::before, .ticks::after { content: ""; position: absolute; inset: 0; pointer-events: none; border: var(--rule-hair) solid var(--color-rule-2); -webkit-mask: conic-gradient(at var(--tick) var(--tick), transparent 75%, var(--color-ink) 0) 0 0 / calc(100% - var(--tick)) calc(100% - var(--tick)); mask: conic-gradient(at var(--tick) var(--tick), transparent 75%, var(--color-ink) 0) 0 0 / calc(100% - var(--tick)) calc(100% - var(--tick)); }
.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-pill); background: var(--color-accent); color: var(--color-accent-ink); font: 400 var(--text-md)/1 var(--font-body); transition: background var(--dur-short) var(--ease-out); }
.btn:hover { background: var(--color-accent-hi); }
.btn--line { background: transparent; color: var(--color-ink); box-shadow: inset 0 0 0 var(--rule-hair) var(--color-rule-2); }
```
