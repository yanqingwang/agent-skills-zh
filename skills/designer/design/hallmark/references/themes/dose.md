---
name: Dose
slug: dose
genre: modern-minimal
paper: light 97.6 88
display: grotesk-sans Schibsted Grotesk
accent: chromatic-green 160
posture: committed
keywords: health, medication, pharmacy, care, carer, family, reminders, schedule, app, mobile, medicine, patients, clinic, prescription, tracking, calm, trust, routine, elderly, parents
material: warm morning paper with a fibre grain and window light, translucent tinted plastic, green-black ink, Schibsted Grotesk over Instrument Sans with DM Mono pharmacy labels, moulded controls, one pharmacy green
photo: natural sat=-15 con=-6
pictured: Care Register, Organiser hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/dose.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Dose

半透明塑料与日光：带细纤维颗粒的暖调晨间纸面、横过的窗光、像分药盒一样的一条条软色塑料、绿黑墨色、Schibsted Grotesk 标题压 Instrument Sans，DM Mono 用于钟点与剂量、排成药房标签的样子。一种药房绿承担全部信号。它可信，因为它精确、从容，而且住在厨房里，不在诊所。它不是临床蓝门户，不是养生粉彩，也不是警报。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(97.6% 0.011 88); --color-paper-2: oklch(96.5% 0.02 160); --color-paper-3: oklch(93% 0.036 160);
  --color-ink: oklch(21% 0.025 170); --color-ink-2: oklch(31% 0.02 170); --color-muted: oklch(49% 0.024 165);
  --color-rule: oklch(86.5% 0.022 140);
  --color-accent: oklch(50% 0.13 160); --color-accent-deep: oklch(42% 0.11 162); --color-accent-soft: oklch(88% 0.08 160); --color-accent-ink: oklch(99% 0.006 160);
  --color-focus: oklch(45% 0.14 160);
  --p-mon: oklch(85% 0.052 22); --p-tue: oklch(87.5% 0.058 64); --p-wed: oklch(91.5% 0.064 98); --p-thu: oklch(86.5% 0.075 160);
  --p-fri: oklch(87% 0.048 210); --p-sat: oklch(84% 0.045 270); --p-sun: oklch(84% 0.048 322);
  --light: oklch(99.4% 0.016 84); --glint: oklch(100% 0 0);
  --font-display: "Schibsted Grotesk", ui-sans-serif, sans-serif; --font-body: "Instrument Sans", ui-sans-serif, sans-serif;
  --font-outlier: "DM Mono", ui-monospace, monospace;
  --radius-card: 14px; --radius-input: 10px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 1px 2px oklch(30% 0.03 165 / 0.08), 0 24px 48px -24px oklch(40% 0.08 165 / 0.35);
  --shadow-lift: 0 1px 1px oklch(30% 0.03 165 / 0.10), 8px 18px 28px -14px oklch(36% 0.06 165 / 0.32), 18px 40px 60px -30px oklch(40% 0.08 165 / 0.30);
  --tracking-display: -0.03em; --display-weight: 700;
}
```

committed（全力以赴）：纸面是暖的，绿色调与塑料承担颜色，薄荷绿（`--color-accent-soft`）标记已确认的东西，强调色本身只落在控件、焦点、一枚图章与一个数字上。地面，写入 stamp（印记）：**white**（默认，即上面的 Token）、**green**（drenched（浸满），`oklch(46% 0.12 160)` 之上覆白墨，表面内部保持白色，薄荷绿铺在地面）、**night**（`oklch(13% 0.01 170)` 之上覆 `oklch(96% 0.01 160)`，塑料 40% 亮度，薄荷绿配深墨）。

## 字体（Type）

- **展示字体：**Schibsted Grotesk 700，`--tracking-display`，行高 1.02，句首大写，等高表格数字。
- **正文：**Instrument Sans 400 与 500，16 至 18px，行高 1.5。
- **标签、图注、表头：**Instrument Sans 500 小一档，句首大写。
- **钟点、剂量、药房标签：**DM Mono 400 与 500（`08:00`、`500 mg`），句内用正文字号，时刻表第一列是时间时用标题字号，药房标签整张用它发声；绝不做标签页、表头或展示数字。每页三个字重：400、500、700。

## 表面（Surfaces）

- 地面是生成的，绝不是图片：纸面带分形噪声纤维颗粒（纸色之下的 `feTurbulence` data URI），Hero 带窗光：四片模糊的 `--light` 光斑斜跨纸面，漂移 90 秒。
- 塑料即表面：一个色调（`--p-*`，绝不表示状态）约 62% 不透明度，顶边一条 `--glint` 高光线，底部一圈更深的内影，透出的彩色光在下方纸面上聚成模糊的一片。它构成色带、托盘与分格；CSS 3D 可以让一组塑料以四分之三视角立在纸上。
- 标签是塑料上的纸：带颗粒的白，10px 圆角，虚线上一个可撕断的存根，通体 DM Mono，一枚双圈绿图章盖着确认、旋转 2 度、写明时间与谁；漏服或待服同样式但用灰色。
- 圆角读起来像应用：控件 10px，表面 14px，标签 999，手机屏幕约 28px。白色表面以 `--shadow-lift` 抬起；一条绿黑墨色色带可以承载一句陈述。
- 照片：给药发生的那个家，手与房间在柔和日光下，绝不正对镜头的脸，也绝不在诊所；14px 圆角，图注在下方。

## 版式（Range）

- **流程化作塑料色带：**每段是通栏色带、各自的色调，编号用 Schibsted 排展示字号，带上放两块产品手机屏，每分钟发生的事用 DM Mono 写在它的行旁。
- **记录化作标签：**照片旁两张药房标签，一张盖绿章"已给"，一张灰色"漏服"，各写明剂量、时间与人。
- **墨色色带上的陈述：**一句平实的话，Schibsted 700，`--text-display` 字号，其下一行薄荷绿。
- **托盘里的第一步：**表单在下陷的塑料托盘上，选项是塑料按键，旁边产品的屏幕实时作答。

## 控件（Controls）

- 模压塑料：52px 控件、10px 圆角，1px 沿口、底部 3px 沿口，顶部一圈 `--glint` 斜切高光、一片柔和投影；按下下沉 3px。主按钮是绿塑料，次按钮是透明的。
- 选项是塑料按键，勾选时转薄荷绿。链接悬停出现绿色下划线。输入框：52px、10px 圆角，1px `--color-muted` 边框。

## 动效（Motion）

光漂移 90 秒，屏幕外暂停。进入视野一次：盖子掀起、标签升起、图章落下、勾动向其他看到的人荡开一圈。Reduced motion（减少动效）或无脚本：呈现最终状态，光静止。

## 语气（Voice）

药剂师的平实，由一家人说出：药名、剂量、钟点、谁给的，用儿子或女儿的那个词（妈、你哥）。绝不说旅程，绝不用红色发警告。

## 禁止事项（Do-nots）

- 绝不用红或琥珀表示漏服或迟到；那是灰色。
- 绝不把塑料色调当信号或第二品牌色；绿承担一切信号。
- 绝不用临床素材：撒落的药片、特写泡罩包装、白大褂。
- 绝不用光亮的玩具塑料：色调保持浅淡，光是日光，除高光与内影外无渐变。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@700&family=Instrument+Sans:wght@400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: 700; letter-spacing: var(--tracking-display); line-height: 1.02; }
.btn { height: 52px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-input); font: 500 var(--text-md) var(--font-body); box-shadow: inset 0 1px 0 var(--glint), 0 0 0 1px var(--color-rule), 0 3px 0 var(--color-rule); transition: transform var(--dur-micro) var(--ease-out); }
.btn--primary { background: linear-gradient(var(--color-accent), var(--color-accent-deep)); color: var(--color-accent-ink); box-shadow: 0 0 0 1px var(--color-accent-deep), 0 3px 0 var(--color-accent-deep); }
.btn:active { transform: translateY(3px); }
.plastic { --t: var(--p-thu); position: relative; border-radius: var(--radius-card); background: linear-gradient(color-mix(in oklab, var(--glint) 32%, transparent), transparent 18%), color-mix(in oklab, var(--t) 62%, transparent); box-shadow: inset 0 1.5px 0 var(--glint), inset 0 -24px 36px -28px color-mix(in oklab, var(--t) 45%, var(--color-ink)); }
.dose, .label { font-family: var(--font-outlier); font-variant-numeric: tabular-nums; }
.band--ink { background: var(--color-ink); color: var(--color-paper); }
```
