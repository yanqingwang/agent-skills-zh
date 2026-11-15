> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/fonts.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 字体

定制（custom run）时加载。目录主题已经为自己的页面点过名，不要读这份文件去质疑它。

**读之前需要：** 页面的想法以及它展示什么。**产出：** 一款展示字体、一款正文字体、一款可选的离群字体（outlier），以及加载规则。

## 规则

一款展示字体加一款正文字体，或一个字族承担两者；可选的离群字体只承担一个角色（字标、标题中的大数字、代码）。定制 run 选择的展示字体不得与任何目录主题重复：`node <skill-dir>/scripts/theme.mjs check --face "<face>"` 会拒绝在用名单里的字体，所以写 token 前先跑它。下面的清单已经把这些字体排除在外。先按想法选择类别，再从中挑两三款，然后靠形状与页面上的色彩表现，在各自真实的标题排布中做决定；字体的名字、名声或题材联想都不是理由。除非用户已确认授权，只用免费字体；优先可变字体。

## 默认禁用

每个模型都会第一反应抓这些，所以它们读起来像"没选过"：Inter、Roboto、Open Sans、Lato、Poppins、Source Sans、Nunito、Montserrat、Raleway、Work Sans、DM Sans、Plus Jakarta Sans、system-ui，以及作为展示或正文用的 Arial 与 Helvetica；作为正文衬线的 Merriweather、Lora、Georgia；Courier New 或系统 mono。用户点名要求或预检在项目里发现它们时仍可使用；此时 stamp 上要注明。

**Saturated**（本身是好字体，但都是第一反应，在 Picks 块中使用需要给出理由）：Playfair Display、Cormorant Garamond、DM Serif Display、Fraunces、Instrument Serif、Recoleta、Space Grotesk、Hubot Sans、Bebas Neue、Unbounded 作为展示字体；Geist、Instrument Sans、Mona Sans 作为正文或整页字体。

## 来源

- **Google Fonts。** 免费，CDN 分发，处处可用。默认来源。
- **Fontshare**（Indian Type Foundry）。商业使用免费，铸字厂品质。一行接入：`<link href="https://api.fontshare.com/v2/css?f[]=<family>@<weights>&display=swap" rel="stylesheet">`。
- **铸字厂**（Klim、Pangram Pangram、Production Type、Lineto、Colophon）只在用户确认授权后使用；此时问清是哪一家，直接从中挑选。

## 目录未使用的展示字体

| 类别 | 字体（来源） |
| --- | --- |
| 罗马衬线 | EB Garamond, Cardo, Castoro, Piazzolla, Alegreya, Marcellus (Google); Gambetta, Recia (Fontshare) |
| 高对比衬线 | Gloock, Libre Bodoni, Abril Fatface, Rozha One, Besley (Google); Erode, Melodrama (Fontshare) |
| 板衬线（Slab） | Arvo, Hepta Slab, Domine, Alfa Slab One, Solway (Google); Bespoke Slab (Fontshare; 其 old-style 数字无视 `lining-nums`，数字要放进正文字体) |
| Grotesk 无衬线 | Rethink Sans, Reddit Sans, Albert Sans (Google); Clash Grotesk, Supreme (Fontshare) |
| 几何无衬线 | Lexend, League Spartan, Afacad (Google); Satoshi, Technor, Excon (Fontshare) |
| 圆体无衬线 | Inclusive Sans, Nunito Sans（仅 700 且需给出理由）, Varela Round (Google); Chubbo, Comico (Fontshare) |
| 窄体与重体 | Teko, Tektur, Michroma, Antonio (Google); Clash Display, Panchang, Khand, Telma, Stardom, Array (Fontshare) |
| Mono 作展示 | Space Mono, Fragment Mono, Red Hat Mono, Spline Sans Mono, Sometype Mono (Google) |
| 像素 | Press Start 2P, VT323, Pixelify Sans, Tiny5, DotGothic16, Workbench (Google) |
| 手写 | Shantell Sans, Caveat, Gochi Hand, Reenie Beanie (Google); Sharpie (Fontshare) |

## 正文字体

正文字体可以是目录在用的；正文不是主题的签名。无衬线：Hanken Grotesk、IBM Plex Sans、Figtree、Onest、Sofia Sans、Golos Text、Karla、Chivo、Albert Sans、Public Sans、Archivo、Manrope（Google）；Switzer、General Sans、Satoshi（Fontshare）。衬线：Newsreader、Source Serif 4、Literata、Spectral、Crimson Pro、EB Garamond、Piazzolla（Google）；Sentient（Fontshare）。代码、数字与度量用 mono：Geist Mono、JetBrains Mono、IBM Plex Mono、DM Mono、Fira Code、Azeret Mono、Chivo Mono、Overpass Mono（Google）。

## 字标（wordmark）

导航与页脚里的字标可以用不同于正文的字体，在色调丰富的页面上更应当如此：把它塌进正文字族会压平层级，页面读起来像没有品牌。当页面没有其他离群角色时，字标就是离群字体的那唯一角色：

```css
:root { --font-body: "Switzer", ui-sans-serif, system-ui, sans-serif; --font-outlier: "Gambetta", ui-serif, serif; }
.wordmark { font-family: var(--font-outlier); font-weight: 600; letter-spacing: -0.015em; }
```

只有当正文的声音就是品牌本身（一封信、一篇宣言、一份长文档）时才塌缩为单一字族；此时字标取该字族的展示切割或其最重的字重。产品页的字标用正文字体加 600 字重，就是未加设计的默认状态。

## 加载

- 只加载页面用到的字重，每个来源一条 `<link>`，带 `display=swap`；先 `<link rel="preconnect">` 到字体主机。
- 自托管字体的 `@font-face` 带 `font-display: swap` 和度量匹配的回退（`size-adjust`、`ascent-override`、`descent-override`、`line-gap-override`），让 swap 不会重排首屏。
- 永不合成粗体或斜体：`font-synthesis: none`，标题用到斜体就把斜体加载进来。
- 可变字体一次加载给全部字重；字族提供可变版本时优先用可变字体。
