> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/diagram-design/references/style-guide.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 风格指南

**颜色、字体排印与 token 的唯一事实来源。** 每个图表都取材于此，而不是内联在其他参考文件中的 hex 值。想改 Diagram Design 的视觉皮肤，就改这个文件。

默认皮肤是一套冷调编辑风配色：白烟色（white-smoke）纸面、墨黑（jet-black）墨色、焦橘色（burnt-tangerine）强调色、蓝灰石板色（blue-slate）弱化色。它开箱即好看；换掉这些值（或运行 [`onboarding.md`](onboarding.md)），所有新图表都会继承新皮肤，且不碰任何图型专属逻辑。

想从某个网站 URL 生成自己的皮肤，见 [`onboarding.md`](onboarding.md)。

---

## Token

### 语义角色

所有 token 都按**语义角色**引用，不按 hex 值引用。图型参考（`type-*.md`）和 SKILL.md 写的是 `accent`，不是 `#bf4520`。

| 角色 | 用途 | 默认（浅色） | 默认（深色） |
|---|---|---|---|
| `paper` | 页面背景，节点默认填充 | `#f5f5f5`（白烟色） | `#2d3142`（墨黑） |
| `paper-2` | 图表容器背景，次要填充 | `#ececec` | `#393e53` |
| `ink` | 主文字，主描边 | `#2d3142`（墨黑） | `#f5f5f5`（白烟色） |
| `ink-strong` | 暖色强调底上的高对比文字 | `#111111` | `#111111` |
| `muted` | 次要文字，箭头默认描边 | `#4f5d75`（蓝灰石板） | `#bfc0c0`（银色） |
| `soft` | 子标签，边界标签 | `#5a6580` | `#949eb2` |
| `rule` | 发丝线边框 | `rgba(45,49,66,0.12)` | `rgba(245,245,245,0.12)` |
| `rule-solid` | 更重的边框，基线 | `#bfc0c0`（银色） | `rgba(191,192,192,0.25)` |
| `accent` | 视觉焦点，每图至多 1–2 处 | `#bf4520`（焦橘色） | `#f08a59` |
| `accent-tint` | 强调描边盒子的填充 | `rgba(191,69,32,0.08)` | `rgba(240,138,89,0.10)` |
| `link` | HTTP/API 调用，外部箭头 | `#2e5aa8` | `#739fdf` |

> **品牌配色来源：**这套皮肤映射自一个五色品牌配色：`jet-black #2d3142`、`silver #bfc0c0`、`white-smoke #f5f5f5`、`atomic-tangerine`、`blue-slate #4f5d75`。浅色 `accent` 不是原始品牌橘色。原始 atomic-tangerine 在 `paper` 上只有 2.86:1，做箭头或标签太淡，所以皮肤改用 `#bf4520`，同一色相加深到文字对比度过 4.5:1。`soft`、`rule`、`link` 三个 token 是派生值（更深的石板色、带透明度的 ink、蓝灰石板色相族里的一个饱和变体），用来覆盖品牌配色未直接命名的角色。每个派生值都受下文对比度契约约束。

### 对比度契约

每个 token 在两种皮肤下、按它实际所在的背景，都必须达到其扮演的每个角色的阈值。`scripts/verify-contrast.py` 会为上表每行计算对所在皮肤 `paper` 的 WCAG 2.x 对比度（`ink-strong` 对它所标注的 0.85 `accent` 填充），任一不达标即让 CI 失败。

| 用途 | 对其实际背景的最低要求 |
|---|---|
| 普通文字，包括用作文字的 `soft`、`link` 或 `accent` | 4.5:1 |
| 大号文字（24px 以上，或 600 以上字重的 18.7px 以上） | 3:1 |
| 关键非文字记号：线条、箭头、边框、焦点轮廓、数据点 | 对相邻颜色 3:1 |
| 装饰性线条与半透明浅色（`rule`、`rule-solid`、`paper-2`、`accent-tint`、带透明度的填充） | 无下限，但绝不能是唯一的含义载体 |

- **一个 token 扮演多个角色，就要每个角色都达标。** `accent` 一处做描边、另一处做文字标签，因此按 4.5:1 把关，而不是仅按描边所需的 3:1。不要因为某 token 平时不是文字就默认它不是。
- **半透明颜色先合成再测。** `rgba()` 填充或描边先与 `paper` 混合，再测对比度。全强度达标的值，0.5 透明度下可能不达标。
- **`paper` 之外的表面都要吃掉对比度。** `accent-tint` 盒子内或 `paper-2` 上，所有比值都会下降。放在那里的文字要对着该表面测量，而不是对着 `paper`。
- **当前默认值：**浅色 `accent` 4.71:1、`soft` 5.34:1、`link` 6.13:1、`muted` 6.11:1（在 `#f5f5f5` 上）；深色 `accent` 5.21:1、`soft` 4.78:1、`link` 4.76:1（在 `#2d3142` 上）。

### 反转规则（浅色 → 深色）

浅色下任何 `rgba(45,49,66, X)` 在深色下变成 `rgba(245,245,245, X)`。透明度不变，RGB 对调。accent 稍作色相偏移并提亮，才能在深色纸面上读清。

### 系列配色（仅限多系列图表类型）

一小组去饱和、编辑风格的配色，供确实需要区分多个重叠实体的图表类型使用（目前：**radar**）。“单焦点”规则依然成立：`accent` 留给焦点系列，下表配色覆盖其余系列。

| Token | 浅色 | 深色 | 说明 |
|---|---|---|---|
| `series-1` | `#7c8f6f`（鼠尾草绿） | `#9caf8f` | 非焦点系列 |
| `series-2` | `#5e7a9b`（灰蓝） | `#82a0c0` | 非焦点系列 |
| `series-3` | `#b8915a`（芥末黄） | `#d3ad7a` | 非焦点系列 |
| `series-4` | `#9c6b50`（锈棕） | `#b88670` | 非焦点系列 |
| `series-5` | `#6e6479`（石板灰） | `#8d8298` | 非焦点系列 |

浅色下填充用 `0.18` 透明度，深色用 `0.22`；描边用全色。**不要把这些 token 回填给非图表类型**：architecture、swimlane 等继续使用 muted-ink 变体。系列配色是可选项，只在重叠形状必须可区分时使用，不是在别处加颜色的通行证。

### 终端皮肤（可选替代方案）

为终端窗口 primitive 准备的自包含配色（见 [primitive-terminal.md](primitive-terminal.md)），是给开发者工具类帖文和技术向社交卡片用的 CLI 框面风格。它不替换上面的默认皮肤，也不受 onboarding 影响；它是第二种固定皮肤，按图表逐个选择启用。

| Token | Hex | 用途 |
|---|---|---|
| `terminal-page` | `#0a0a0a` | 窗口背后的页面背景 |
| `terminal-paper` | `#141414` | 窗口主体，节点填充 |
| `terminal-bar` | `#1b1b1b` | 标题栏条 |
| `terminal-border` | `#2b2b2b` | 窗口边框，发丝线 |
| `terminal-ink` | `#f5f5f5` | 主文字，主描边（与默认 `ink` 同为白烟色） |
| `terminal-muted` | `#9a9a9a` | 次要文字，子标签，环描边 |
| `terminal-soft` | `#5c5c5c` | 三级层级：未激活圆点，辐条 |
| `terminal-accent` | `#ff5a36` | 唯一强调色：焦点站、提示符、激活圆点 |
| `terminal-accent-tint` | `rgba(255,90,54,0.12)` | 强调描边盒子的填充 |

**单强调色规则依然成立。** 凡不是 `terminal-ink` 或 `terminal-muted`/`terminal-soft` 的东西都应是 `terminal-accent`，绝不引入第二种色相。

---

## 字体排印

| 角色 | 字体族 | 字号 | 字重 | 用途 |
|---|---|---|---|---|
| `title` | Instrument Serif | 1.75rem | 400 | 页面 H1 |
| `node-name` | Geist（无衬线） | 12px | 600 | 人读标签 |
| `sublabel` | Geist Mono | 9px | 400 | 端口、协议、URL、字段类型 |
| `eyebrow` | Geist Mono | 7–8px | 500，字距 0.18em，全大写 | 类型标签，轴标签 |
| `arrow-label` | Geist Mono | 8px | 400，字距 0.06em | 箭头注释 |
| `callout` | Instrument Serif *斜体* | 14px | 400 | 仅限编辑性旁注 |

### 字体栈

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&family=Noto+Serif:ital@0;1&family=Noto+Sans+KR:wght@400;500;600&family=Noto+Serif+KR:wght@400&family=Noto+Sans+TC:wght@400;500;600&family=Noto+Serif+TC:wght@400&display=swap" rel="stylesheet">
```

### 字体来源

字体来源决定图表是否发起网络请求。它是皮肤设置，保存的 profile 也会携带它。

字体来源：`web`

| 取值 | 随附内容 | 网络 |
|---|---|---|
| `web`（默认） | 上面的 Google Fonts `<link>`；文字以 Instrument Serif、Geist、Geist Mono 渲染 | 向 `fonts.googleapis.com` 发一个样式表请求，外加字体文件 |
| `system` | 不放字体 `<link>`；每个字体族栈依次回退到平台自带的衬线、无衬线与等宽字体 | 无 |

用户要求离线输出、系统字体或不用 Google Fonts 时，或本行写着 `system` 时，用 `system`。`system` 模式下：

- 完全省去字体 `<link>`（以及导出时的 `@import`）。每个 `font-family` 栈照原样保留：每个栈都以通用字体族结尾（`serif`、`system-ui, sans-serif`、`ui-monospace, monospace`），装了 Geist 的查看者仍能看到 Geist，其他人则落到系统字体。
- 回退字体与 Geist 的度量不同，所以 8px 标签内边距保持原样，不要按 Geist 的量裁盒子。
- 用 `python3 scripts/export_svg.py <file> --system-fonts` 导出，再用 `python3 scripts/self_check.py --offline <file>` 验证；Google Fonts 链接仍在时它会报失败。

渲染 linter 的默认运行（`lint-render.py`，网络被屏蔽）测的正是这种回退渲染，因此所有随附模板与示例都已在系统字体模式下验证过。

想完全不联网也保留编辑风字体，就本地安装 Instrument Serif、Geist、Geist Mono（三者均为 SIL Open Font License）并使用 `system`：字体栈会优先解析到已安装的字体。

### 韩文标签

Geist 与 Instrument Serif 都没有谚文（Hangul）。韩文 `<text>` 元素扩展自己的字体族，绝不换皮肤：

```svg
<text font-family="'Geist', 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif">결제 서비스</text>
```

上面字体链接里已带两个 Noto 字体，因此网页字体先于本地安装的字体解析，同一文件在 macOS、Windows 和审阅者的浏览器上渲染一致。离线查看时本地字体族接着兜底。页面标题需要衬线对应项，即 `'Instrument Serif', 'Noto Serif KR', serif`，否则混排拉丁/韩文标题会让谚文落到平台通用衬线上，两半不协调。Google 的 `css2` 端点按 unicode-range 切分韩文，所以只有少量韩文标签的图表只下载用到的切片。四个模板都带这两个字体，因为新图表可能含谚文；随附的纯拉丁示例保留较短的链接，因为不含谚文的文件没有要解析的东西。

**宽度预算。** 按字符测量，不按文字体系测量：**每个 Unicode 宽字符或全角字符占 1em，其他字符按其字体的拉丁字幅计**（无衬线 0.60em，等宽 0.62em），非间距/封闭组合字符标记不占宽。对整串求和再乘以字号得出文字宽度，加上内边距，盒子尺寸向上取整到 4 的倍数。`verify-treemap.py` 对 treemap 单元格标签严格按这个文字宽度把关。本 skill 的 `scripts/self_check.py` 对任何类型可见盒子内的文字套用同样宽度（外加上字距），标签超出盒边 0.3em 以上即判失败。内边距、取整以及纸色箭头标签遮罩上的标签不在检查范围内，要靠你自己把住。

按文字体系计数是个陷阱。`주문 v2.1` 是两个全角音节加五个窄字符；只统计谚文、拉丁字母和空格的公式会悄悄丢掉 `2`、`.` 和 `1`，按七个字符中的四个来定盒子。每个渲染出来的字符都占宽度：按字符测，绝不按文字体系测。

从谚文度量可推出三条规则：

- **子标签保持拉丁文。** 端口、协议、字段类型和 URL 本来就是拉丁文：继续用 `Geist Mono`，不要翻译它们。9px 等宽子标签里的谚文无法阅读，也没有等宽字体可回退。
- **12px 下限。** 谚文低于 12px 就发糊。韩文名字在 12px 放不下，就删减名字，不要缩小字号。
- **箭头标签、eyebrow 和图例文字要换语域。** 这些槽位是 7–8px Geist Mono、全大写加字距，谚文既没有对应字体也没有可读性。落在这些槽位里的韩文标签改用 12px 无衬线、字重 500、无字距、不做大写转换，其遮罩矩形随之放大（高 16px，宽度按上文预算，仍取整到 4 的倍数）。同一图表里的拉丁标签维持等宽处理。

**承重规则：**等宽字体只用于*技术*内容（端口、命令、URL、字段类型）。名字用 Geist 无衬线。页面标题用 Instrument Serif。斜体 Instrument Serif 只留给注释旁注（见 [primitive-annotation.md](primitive-annotation.md)）。**绝不把 JetBrains Mono** 当万能“开发”字体。

### 繁体中文标签

Geist 与 Instrument Serif 都没有汉字。繁体中文 `<text>` 元素扩展自己的字体族，绝不换皮肤：

```svg
<text font-family="'Geist', 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif">請求項比對</text>
```

上面字体链接里已带两个 Noto TC 字体，因此网页字体先于本地安装的字体解析，同一文件在 macOS、Windows 和审阅者的浏览器上渲染一致。离线查看时本地字体族接着兜底。页面标题需要衬线对应项，即 `'Instrument Serif', 'Noto Serif TC', serif`，否则混排拉丁/汉字标题会让汉字落到平台通用衬线上，两半不协调。Google 的 `css2` 端点按 unicode-range 切分中文，所以只有少量中文标签的图表只下载用到的切片。

**宽度预算。** 上文按字符计宽的约定不变：每个 Unicode 宽字符或全角字符占 1em，其他字符按其字体的拉丁字幅计，非间距标记不占宽。全角标点（`（）「」，。：`）也是宽字符、同样占 1em，这恰恰是最常被漏算的部分。

按文字体系计数是个陷阱。`請求項 v2.1` 是三个全角字符加五个窄字符；只统计汉字和拉丁字母的公式会悄悄丢掉 `2`、`.` 和 `1`，按九个字符中的六个来定盒子。

从汉字度量可推出三条规则，与谚文那三条对应：

- **子标签保持拉丁文。** 端口、协议、字段类型和 URL 本来就是拉丁文：继续用 `Geist Mono`，不要翻译它们。9px 等宽子标签里的汉字无法阅读，也没有等宽字体可回退。子标签若是叙述性文字而非取值，可以用中文，但随后要按下面第三条规则换语域。
- **12px 下限。** 汉字在同样的 em 方框里塞进的笔画比谚文更多，所以 12px 下限在这里只紧不松。中文名字在 12px 放不下，就删减名字，不要缩小字号。
- **箭头标签、eyebrow 和图例文字要换语域。** 这些槽位是 7–8px Geist Mono、全大写加字距，汉字既没有对应字体也没有可读性。落在这些槽位里的中文标签改用 12px 无衬线、字重 500、无字距、不做大写转换，其遮罩矩形随之放大（高 16px，宽度按上文预算，仍取整到 4 的倍数）。同一图表里的拉丁标签维持等宽处理。

简体中文适用同样三条规则，字体栈换成简体版（`'Noto Sans SC'`、`'PingFang SC'`、`'Microsoft YaHei'`）。该字体不在链接里，所以简体标签仍靠查看者本地有什么字体来解析。

### 西里尔文标签

Geist 与 Geist Mono 自带西里尔文（Google Fonts 上的 `cyrillic` 与 `cyrillic-ext`），所以保加利亚语、俄语、乌克兰语或塞尔维亚语的名字、子标签、箭头标签、eyebrow 和图例文字沿用拉丁文的处理：同样的字体、字号、字距和大写。这里没有语域切换：谚文和汉字要换语域是因为 Geist Mono 没有它们的字体，而 Geist Mono 覆盖西里尔文。

Instrument Serif 不含西里尔文。页面标题要扩展字体族，写成 `'Instrument Serif', 'Noto Serif', serif`，否则混排拉丁/西里尔标题会让西里尔文落到后面随便哪个字体上，两半不协调。上面字体链接里带了 Noto Serif（正体与斜体都有），所以西里尔文的斜体旁注也用同一个栈。

**Noto Serif 要排在 CJK 衬线之前。** 栈里同时列有 `'Noto Serif KR'` 或 `'Noto Serif TC'` 时，把 `'Noto Serif'` 放在它们前面。Google Fonts 把西里尔文也切分进那些字体，先命中 CJK 字体的栈就会用 CJK 字体来画西里尔文。模板把 `'Noto Serif'` 放在 `'Instrument Serif'` 与 `'Noto Serif KR'` 之间就是这个原因；Noto Serif 没有谚文和汉字，韩文与中文标题会直接穿过它落到后面的字体。

**宽度预算。** 上文按字符计宽的约定不变：每个字符按其字体的拉丁字幅计（无衬线 0.60em，等宽 0.62em）。这在 Geist Mono 上完全准确，在 Geist 无衬线上只是平均数。Geist Mono 是等宽字体：西里尔字形与拉丁字形的步进完全相同，所以子标签、箭头标签、eyebrow、图例文字及其遮罩矩形都按拉丁文尺寸定。Geist 无衬线不是。它的宽西里尔字母（大小写皆然，如 `Ж Ш Щ Ю Ы`、`ж ш щ ы ю`）远超 0.60em 的平均值：`Шкаф ODF-2` 在 12px 下按预算是 72px，实际画出来约 76px。盒子向上取整到 4 的倍数至多找回 3px，救不了场。把超出量留给盒子内边距，并在浏览器里实测西里尔无衬线名字的宽度：`verify-treemap.py` 只对预算把关，不量实际绘制宽度，抓不住这种超出。

按文字体系计数依旧是陷阱。`Шкаф ODF-2` 是四个西里尔字母、一个空格、三个拉丁字母、一个连字符加一个数字；只统计西里尔字母、拉丁字母和空格的公式会悄悄丢掉 `-` 和 `2`，按十个字符中的八个来定盒子。

**保住印制标签。** 读者要拿它与实物对号的标签（机柜、接续盒、端口映射图）必须带着与印制完全一致的字符串。不要转写，也不要改大小写；若必须放进 eyebrow 这类大写槽位，宁可对该标签去掉大写转换，也不要改印制字符串的大小写。`Шкаф ODF-2` 就保持 `Шкаф ODF-2`，不要写成 `Shkaf ODF-2`。

---

## 描边、圆角、间距

| Token | 取值 | 用途 |
|---|---|---|
| `stroke-thin` | `0.8` | 标签盒轮廓，叶节点 |
| `stroke-default` | `1` | 大多数描边 |
| `stroke-strong` | `1.2` | 强调描边 |
| `radius-sm` | `4` | 小标签 |
| `radius-md` | `6` | 节点盒 |
| `radius-lg` | `8` | 容器，环 |
| `grid` | `4` | 所有坐标、尺寸与间距都是 4 的倍数（硬规则） |

---

## 节点类型 → 处理方式

语义角色组合。图型规格里按名称引用它们。

| 类型 | 填充 | 描边 |
|---|---|---|
| `focal`（至多 1–2 个） | `accent-tint` | `accent` |
| `backend` | `#ffffff`（白） | `ink` |
| `store` | `ink @ 0.05` | `muted` |
| `external` | `ink @ 0.03` | `ink @ 0.30` |
| `input` | `muted @ 0.10` | `soft` |
| `optional` | `ink @ 0.02` | `ink @ 0.20` 虚线 `4,3` |
| `security` | `accent @ 0.05` | `accent @ 0.50` 虚线 `4,4` |

---

## 自定义皮肤

四种方式：

1. **运行 onboarding**：见 [`onboarding.md`](onboarding.md)。丢进一个 URL，skill 会提取配色与字体并重写本文件。
2. **手工编辑**：改上面各表里的 hex 值。改完跑一遍输出前品味闸门，确认新纸面颜色下 accent 仍然读作“焦点”。
3. **品牌交接**：把你现有的设计 token JSON 粘贴到这里新增一节，并把它的 token 映射到上述语义角色。
4. **客户 profile**：用 [`profiles.md`](profiles.md) 保存和切换命名皮肤，或把皮肤绑定到某个项目。

### 约束（不许破坏）

- **对比度**：两种皮肤下，每个文字 token（`ink`、`muted`、`soft`、`link`、`accent`）在 `paper` 上都必须过 4.5:1。见[对比度契约](#contrast-contract)；`scripts/verify-contrast.py` 负责检查。
- **单一强调色**：`accent` 只选一种颜色。两种强调色会抹掉焦点信号。
- **不做彩虹配色**：品牌有 8 个颜色也只挑 3 个（paper、ink、accent），其余归入 `muted` 变体。
- **衬线 + 无衬线 + 等宽**：三个字体族，不再多。品牌字体全是无衬线时，`title` 和 `callout` 仍要保留 Instrument Serif，这个对比是承重的。
- **纸面是暖中性色，不是纯白**：纯白会让设计变冷。选奶油色、米白色或带一点暖意的浅灰。
- **圆点纹理是可选项，不是默认**：22×22 圆点纹理是可选的“点纹纸”变体（适合长篇编辑风 hero 图表）。默认背景是干净的 `paper` 填充，无纹理。启用纹理时，以 `paper` 上约 10% 透明度的 `ink` 呈现：看得见，但不吵。
- **容器默认干净**：图表直接放在页面纸面上，不加次要容器背景或边框。带框变体（`paper-2` 背景 + `rule` 边框 + 8px 圆角 + 内边距）作为可选项留给卡片密集的布局，但默认不要伸手去拿：多出来的框面会和图形打架。
