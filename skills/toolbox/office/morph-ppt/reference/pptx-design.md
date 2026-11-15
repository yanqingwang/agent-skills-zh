---
name: pptx-design
description: Morph 专属设计要点：深场次感演示文稿的色彩与字号下限，另含场景演员（Scene Actors）、页面类型（Page Types）、形状索引（Shape Index）与 Morph 动画要点
---

> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/pptx-design.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Morph 设计要点

`skills/officecli-pptx/SKILL.md` 的 §Requirements / §Design Principles / §Visual delivery floor 是所有 pptx（无论是否 morph）中**字号层级、对比度与配色选择的权威依据**。本文件把这个下限收窄到 morph 演示文稿通常瞄准的**舞台感（stage-feel）档位**：更暗的背景、更大的主视觉字号、场景演员更宽的不透明度区间，以及能扛住 `#sN-*` 幽灵内容反复增删的更宽单页文本宽度。凡是 pptx SKILL.md 已给出规则的地方，本文件只是**幻灯片确实处于 morph 配对中**时的叠加式覆盖，否则一律向上回归上层规则。

---

## 1) 色彩原则（morph 舞台感档位）

### 对比度为王：始终计算，不要目测

morph 演示文稿偏暗；中灰正文（`#666666`）在 pptx 基础渲染里看着没问题，可一旦背景亮度低于 30，**在投影仪强光下就会消失**。选色之前先计算：

```
Brightness = (R × 299 + G × 587 + B × 114) / 1000
```

落地规则（morph 专属，比 pptx 基础版更严）：

- **深色背景**（亮度 < 128）→ 正文颜色亮度 ≥ 80%（`#FFFFFF`、`#EEEEEE`、`#CADCFC`）。图表系列填充与图标描边必须达到同样下限。
- **浅色背景**（亮度 ≥ 128）→ 正文颜色亮度 ≤ 20%（`#000000`、`#333333`）。
- **混合 / 渐变背景**：在整段文字后面加半透明衬底块（`opacity=0.3-0.6`）；不要指望渐变自己"平均"出对比度。

算例：

- `#000000` 亮度 0 → 深色 → 白字
- `#1E2761` 亮度 35 → 深色 → 白字
- `#2C3E50` 亮度 62 → 深色 → 白字
- `#E94560` 亮度 88 → 仍属深色 → 白字（常见错误：把亮红色当成"中间色"）
- `#F39C12` 亮度 160 → 浅色 → 深色字
- `#FFFFFF` 亮度 255 → 浅色 → 深色字

**拿不准就加大对比度。** 舞台风格的演示文稿是在投影仪加复杂环境光下观看的，以审阅者显示器的舒适度为基准是错误标准。

### 色彩层级：三个深度层

morph 演示文稿每页的可见元素比 pptx 基础版更多（场景演员 + 内容 + 图表系列 + 标注）。守住这个堆叠顺序：

```
Background fill  →  Scene actors  →  Content (text / data / KPI)
(weakest)           (medium)          (strongest)
```

`!!scene-*` 与 `!!actor-*` 形状的不透明度区间（morph 专属，比 pptx 基础版更紧）：

- **≤ 0.12**：整份文稿层面的装饰（`!!scene-grid`、`!!scene-band`、边角点缀）。不能在后场与内容抢视线。
- **0.3 – 0.6**：论据 / 数据衬底块（`!!actor-evidence-bg`、KPI 卡片填充）。足以框住内容，又不压过数字。
- **0.8 – 1.0**：保留给本身就是内容的 `!!actor-*` 形状（单个数据背后的主视觉圆环、作为信息本身的品牌色条）。克制使用：每页超过 2 个就显得杂乱。

场景演员若以 `opacity=0.7` 落在内容核心区，通常是分类错了：要么调低（它是装饰），要么改名为 `!!actor-*`（它是内容），并安排一页退场。

### 配色选择：按情绪选，不按习惯选

morph 演示文稿没有万能配色公式。pptx 的四套经典配色（Executive navy / Forest & moss / Warm terracotta / Charcoal minimal）依然适用，但跨页动效会放大色彩情绪，所以 morph 演示文稿在 52 套风格库里选得更自由。

决策路径：

1. **匹配主题情绪** → 科技 / 金融科技偏 `dark--*`；医疗 / 教育偏 `light--*` 或 `warm--*`；设计 / 品牌偏 `bw--*` 或 `mixed--*`。
2. **尊重用户指定的色值** → 如果简报指定了品牌色，去 `reference/styles/INDEX.md` 的 Quick Lookup 找最接近的色值三件套；不要硬套情绪标签。
3. **按项目变换**：不要重复最近三份演示文稿的配色家族。每份路演都用 `dark--premium-navy`，看起来是套模板，不是设计选择。
4. **在 `brief.md` 里写明配色名** → "warm--earth-organic palette" 是一种承诺；"warm tones" 不是。

`reference/styles/` 用来找灵感（配色 + 标志性动作），**不要**照抄坐标：按 `reference/styles/INDEX.md` L5-11 的说明，build.sh 里的坐标是为演示内容手工调的。

---

## 2) 字体排印（morph 舞台感档位）

### 推荐组合

morph 演示文稿常在舞台上或投影为主的场合观看，这时字重比选哪款字体更管用。最多两种字体：一种标题，一种正文。

| 内容类型 | 主力组合                              | 备选                              |
| ------------ | ----------------------------------------- | --------------------------------- |
| 英文         | Montserrat（标题）+ Inter（正文）         | Segoe UI / Helvetica Neue         |
| 中文         | Source Han Sans 思源黑体（标题 + 正文）   | PingFang SC / Microsoft YaHei     |
| 中英混排     | Montserrat + Source Han Sans              | Segoe UI + System Font            |

morph 页面正文避免用 Georgia / Times：形状中途插值时衬线端点会消失。衬线字体留给没有切换动效的 pptx 基础版演示文稿。

### 字号阶梯：比 pptx 基础版大一档

morph 演示文稿的观看距离更远（舞台布置、大屏幕），而且每一帧除了文字还要承载动效。字号加大：

| 角色                | pptx 基础版  | morph 舞台版（用这个）  |
| ------------------- | ---------- | ----------------------- |
| 主视觉 / 封面标题   | 44-60pt    | **54-72pt**，bold/black |
| 章节标题            | 24-32pt    | **28-40pt**，bold       |
| 正文 / 辅助文字     | 16-22pt    | **18-24pt**             |
| 说明文字 / 脚注     | 12-14pt    | **13-16pt**（下限 13）  |

任何一页都不要低于 13pt：投影强光最先吃掉最小的两档字号。

### 文本宽度指引：居中要加宽，幽灵增删频繁也要加宽

静态演示文稿里换行会破坏视觉层级；morph 演示文稿里换行**还会破坏动效**（插值会带着换行后的基线走，文字在过渡中途看起来是斜的）。文本框宁可比你以为的更宽。

| 内容类型                         | 最小宽度         | 最佳实践                                                     |
| -------------------------------- | ---------------- | ------------------------------------------------------------ |
| 居中标题（64-72pt）              | 28cm             | 10-15 字符标题用 28-30cm，主视觉大句用 25cm                  |
| 居中副标题（28-40pt）            | 25cm             | 始终 25-28cm，避免词中间断行                                 |
| 左对齐标题                       | 20cm             | 视内容长度 20-25cm                                           |
| 正文 / 卡片                      | 8cm（单栏）      | 单栏 8-12cm，双栏 16-18cm                                    |
| 幽灵目标内容（`#sN-*`）          | 与源形状相同     | 宽度必须与页面上那份一致：幽灵更窄会让 morph 变成"缩放加移动的倾斜" |

morph 演示文稿里的常见错误：

- 长居中副标题只给 10-15cm → 换行别扭 + 过渡时明显倾斜。
- 文本框紧到"刚好装下"文字 → 克隆页多出一个字符就破版。
- 幽灵目标（x=36cm）尺寸做得比源形状小 → morph 看起来像缩小挪走，而不是滑出。

**经验法则：** 拿不准就加宽。morph 插值过程中，留白多一点好过文字换行。

---

## 3) 场景演员（动画引擎）：展开版

**用途：** 通过跨相邻幻灯片持续存在、只改变属性的形状，做出平滑的 Morph 动画。

### 布置

如果整份文稿讲的是一个连续的视觉故事，就在第 1 页定义 6-8 个演员：

- **大**（5-8cm）：主视觉锚点（主圆环、色带、主卡片）
- **中**（2-4cm）：辅助元素（指标卡片、点缀圆环）
- **小**（1-2cm）：点缀与细节（圆点、短线、图标）

**形状类型**（经 `--prop preset=` 设置）：`ellipse | rect | roundRect | triangle | diamond | star5 | hexagon`。完整列表见 `officecli help pptx shape`。

### 命名（以 SKILL.md 为准）

三前缀体系：`!!scene-*` / `!!actor-*` / `#sN-*`。权威出处：`SKILL.md` §What is Morph? 的核心机制部分。本文件只补充下面这条 Python 与 shell 的引号差异。

**Python：** `#` 和 `!!` 不需要特殊引号，在 `subprocess.run([..., "--prop", "name=#s1-title", ...])` 里当普通字符串传即可。

**Shell（bash/zsh）：** 一律用单引号，避免 `!!` 触发历史展开、`#` 被当成行首注释：`--prop 'name=!!scene-ring'` / `--prop 'name=#s1-title'`。

### 配对示例：3 个演员 × 3 页

```
Slide 1: !!scene-ring (x=5cm, y=3cm, w=8cm, fill=E94560, opacity=0.3)
         !!scene-dot  (x=28cm, y=15cm, w=1cm)
         !!actor-headline (x=4cm, y=8cm, w=26cm, size=48)

Slide 2: !!scene-ring (x=20cm, y=2cm, w=12cm, opacity=0.6)   ← same name, new position+size
         !!scene-dot  (x=3cm, y=16cm, w=1.5cm)                ← moved to opposite corner
         !!actor-headline (x=1.5cm, y=1cm, w=12cm, size=24)  ← shrunk + moved to top-left

Slide 3: !!scene-ring (x=36cm)                                ← ghosted off-canvas
         !!scene-dot  (x=10cm, y=2cm, w=1cm)
         !!actor-headline (x=36cm)                            ← ghost: new headline takes over
         !!actor-subpoint (x=4cm, y=8cm, w=26cm, size=36)    ← new actor enters (no pair on S2 = fade in)
```

### 每页内容（`#sN-*`）工作流

1. **克隆上一页** → 继承下来的 `#s(N-1)-*` 内容带着旧页前缀。
2. **幽灵化继承内容** → 把所有 `#s(N-1)-*` 形状移到 `x=36cm`。
3. **添加新内容** → 使用当前页前缀 `#sN-*`。

缺了第 2 步，各页形状会不断累积 → 视觉重叠在整份文稿里悄悄叠加。

---

## 4) 页面类型（混搭出节奏）

混用页面类型避免单调。每种类型承担不同的叙事任务：

| 类型 | 何时使用 | 视觉结构 |
|---|---|---|
| **hero** | 开场、收尾 | 大号居中标题 + 散布的场景演员 |
| **statement** | 关键信息、过渡 | 一句有冲击力的话 + 戏剧性的演员位移（8cm 以上） |
| **pillars** | 多点结构 | 2-4 根等宽立柱，演员变成卡片背景（opacity 0.12） |
| **evidence** | 数据、统计 | 1-2 个大的不对称块 + 支撑细节（opacity 0.3-0.6） |
| **timeline** | 流程、时序 | 横向或纵向流，带步骤背景 |
| **comparison** | A 对比 B | 左右分栏（50/50 或 60/40），对比色 |
| **grid** | 多项罗列 | 散点或网格布局，观感更轻 |
| **quote** | 呼吸口 | 居中文字，极简装饰 |
| **cta** | 行动号召 | 回到大胆的居中设计 |
| **showcase** | 重点展示 | 大块中心区域放产品/截图 |

**设计备注：**

- **pillars**：多栏均布；场景演员 morph 成卡片背景（roundRect，opacity=0.12）。
- **evidence**：不对称：1 个大演员（占画布 30-40%）+ 1 个中演员（20-30%），数据背景可用 opacity 0.3-0.6。
- **grid**：必须与 pillars 和 evidence 区分开：轻、散，而不是结构化。
- **变化很重要**：避免连续使用同一种页面类型。

---

## 5) 形状索引机制

每页上的形状按顺序编号：`shape[1]`、`shape[2]`、`shape[3]`…… 应用 `transition=morph` 之后，CLI 会自动给名称加 `!!` 前缀，**此后请改用索引路径**（见 SKILL.md §Known Issues M-1）。

### 索引行为

- **创建时：** 按顺序添加的形状索引递增。
- **克隆后：** 新页继承所有形状，索引完全相同。
- **向克隆页添加后：** 新形状拿下一个可用索引。
- **修改后：** 索引不变。

### 构建脚本的模式

```
Slide 1: 6 actors + 2 content = 8 shapes total
Slide 2: Clone (8) → Ghost content (shape[7-8]) → Add new (shape[9+])
Slide 3: Clone (10) → Ghost content (shape[9-10]) → Add new (shape[11+])
```

**公式：** 下一页第一个新形状的索引 = 上一页形状总数 + 1。

**调试：** 用 `officecli get $FILE '/slide[N]' --depth 1` 查看实际索引。

---

## 6) Morph 动画要点

### 最低要求

1. 第 2 页起必须设置 `transition=morph`（`officecli set /slide[N] --prop transition=morph`）。
2. 场景演员在各页的 `name=` 必须完全一致。
3. 添加新内容之前，上一页内容必须已幽灵化（`x=36cm`）。
4. 相邻两页的空间布局应当不同（≥ 3 个形状满足位移 ≥ 5cm 或旋转 ≥ 15° 或尺寸变化 ≥ 30%）。

### 制造运动

在相邻两页之间改动至少 3 个场景演员属性：

- 改位置（x, y）
- 改尺寸（width, height）
- 改旋转（rotation 角度）
- 改颜色（fill、opacity）

**目标：** 有运动 + 变形的感觉，而不只是淡入淡出。

### morph 页上的入场效果

Morph 会自动处理形状过渡，入场动画通常没必要。确需使用时（例如让新的 `#sN-*` 卡片淡入），用 `with` 触发器让它与 morph 同步播放：

```
animation=fade-entrance-300-with
```

格式：`EFFECT[-DIRECTION][-DURATION][-TRIGGER]`。预设列表见 `officecli help pptx animation`。

---

## 7) 风格参考

`reference/styles/` 下有 52 个视觉风格目录，目录清单见 `reference/styles/INDEX.md`。查找工作流在 SKILL.md §Style library lookup workflow。关键规则：**学思路，别抄坐标**（按 `INDEX.md` L5-11，各风格的 build.sh 有已知排版问题）。
