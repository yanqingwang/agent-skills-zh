> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/STYLE_PRESETS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 风格预设参考

为 Frontend Slides 精选的视觉风格。每个预设都取材于真实设计参考，摒弃泛泛的"AI 腔"美学。**只用抽象形状，不用插画。**

**Viewport CSS：** 必需的基底样式见 [viewport-base.css](viewport-base.css)。每份演示文稿都要引入。

---

## 深色主题

### 1. Bold Signal

**Vibe：** 自信、大胆、现代、冲击力强

**Layout：** 深色渐变上的彩色卡片。编号在左上，导航在右上，标题在左下。

**Typography：**
- Display: `Archivo Black` (900)
- Body: `Space Grotesk` (400/500)

**Colors：**
```css
:root {
    --bg-primary: #1a1a1a;
    --bg-gradient: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
    --card-bg: #FF5722;
    --text-primary: #ffffff;
    --text-on-card: #1a1a1a;
}
```

**Signature Elements：**
- 以醒目的彩色卡片作为视觉焦点（橙色、珊瑚色或鲜亮强调色）
- 大号分节编号（01、02 等）
- 带激活/未激活透明度状态的导航面包屑
- 网格布局，对齐精确

---

### 2. Electric Studio

**Vibe：** 大胆、干净、专业、高对比

**Layout：** 上下分栏，上白下蓝。品牌标记放在四角。

**Typography：**
- Display: `Manrope` (800)
- Body: `Manrope` (400/500)

**Colors：**
```css
:root {
    --bg-dark: #0a0a0a;
    --bg-white: #ffffff;
    --accent-blue: #4361ee;
    --text-dark: #0a0a0a;
    --text-light: #ffffff;
}
```

**Signature Elements：**
- 上下两栏分割
- 分栏边缘的强调条
- 引文排印作为主角元素
- 克制而自信的留白

---

### 3. Creative Voltage

**Vibe：** 大胆、创意、有活力、复古现代

**Layout：** 左右分栏，左侧电光蓝，右侧深色。配手写体点缀。

**Typography：**
- Display: `Syne` (700/800)
- Mono: `Space Mono` (400/700)

**Colors：**
```css
:root {
    --bg-primary: #0066ff;
    --bg-dark: #1a1a2e;
    --accent-neon: #d4ff00;
    --text-light: #ffffff;
}
```

**Signature Elements：**
- 电光蓝与霓虹黄的撞色
- 半调网纹肌理
- 霓虹徽标与标注
- 手写体排印增添创意气质

---

### 4. Dark Botanical

**Vibe：** 优雅、精致、艺术、高级感

**Layout：** 深色底上居中排布内容。四角放置抽象柔形。

**Typography：**
- Display: `Cormorant` (400/600) — 优雅衬线
- Body: `IBM Plex Sans` (300/400)

**Colors：**
```css
:root {
    --bg-primary: #0f0f0f;
    --text-primary: #e8e4df;
    --text-secondary: #9a9590;
    --accent-warm: #d4a574;
    --accent-pink: #e8b4b8;
    --accent-gold: #c9b896;
}
```

**Signature Elements：**
- 抽象柔和渐变圆（模糊、叠压）
- 暖色点缀（粉、金、陶土色）
- 细竖线装饰
- 斜体签名式排印
- **不用插画，只用抽象 CSS 形状**

---

## 浅色主题

### 5. Notebook Tabs

**Vibe：** 编辑感、有条理、优雅、有触感

**Layout：** 深色背景上的奶油色纸卡。右缘排列彩色标签。

**Typography：**
- Display: `Bodoni Moda` (400/700) — 经典编辑体
- Body: `DM Sans` (400/500)

**Colors：**
```css
:root {
    --bg-outer: #2d2d2d;
    --bg-page: #f8f6f1;
    --text-primary: #1a1a1a;
    --tab-1: #98d4bb; /* Mint */
    --tab-2: #c7b8ea; /* Lavender */
    --tab-3: #f4b8c5; /* Pink */
    --tab-4: #a8d8ea; /* Sky */
    --tab-5: #ffe6a7; /* Cream */
}
```

**Signature Elements：**
- 带柔和阴影的纸面容器
- 右缘彩色分节标签（竖排文字）
- 左侧活页孔装饰
- 标签文字须随视口缩放：`font-size: clamp(0.5rem, 1vh, 0.7rem)`

---

### 6. Pastel Geometry

**Vibe：** 友好、有条理、现代、亲和

**Layout：** 浅彩背景上的白色卡片。右缘竖排胶囊标签。

**Typography：**
- Display: `Plus Jakarta Sans` (700/800)
- Body: `Plus Jakarta Sans` (400/500)

**Colors：**
```css
:root {
    --bg-primary: #c8d9e6;
    --card-bg: #faf9f7;
    --pill-pink: #f0b4d4;
    --pill-mint: #a8d4c4;
    --pill-sage: #5a7c6a;
    --pill-lavender: #9b8dc4;
    --pill-violet: #7c6aad;
}
```

**Signature Elements：**
- 带柔和阴影的圆角卡片
- **右缘竖排胶囊标签**，高度错落（类似标签页）
- 胶囊宽度统一，高度依次为：短 → 中 → 高 → 中 → 短
- 角落的下载/操作图标

---

### 7. Split Pastel

**Vibe：** 俏皮、现代、友好、有创意

**Layout：** 双色竖向分割（左桃色，右薰衣草色）。

**Typography：**
- Display: `Outfit` (700/800)
- Body: `Outfit` (400/500)

**Colors：**
```css
:root {
    --bg-peach: #f5e6dc;
    --bg-lavender: #e4dff0;
    --text-dark: #1a1a1a;
    --badge-mint: #c8f0d8;
    --badge-yellow: #f0f0c8;
    --badge-pink: #f0d4e0;
}
```

**Signature Elements：**
- 分割的双色背景
- 带图标的俏皮胶囊徽标
- 右栏叠加网格纹
- 圆角 CTA 按钮

---

### 8. Vintage Editorial

**Vibe：** 机敏、自信、编辑感、个性鲜明

**Layout：** 奶油色底上居中排布内容。抽象几何形状作点缀。

**Typography：**
- Display: `Fraunces` (700/900) — 独特衬线
- Body: `Work Sans` (400/500)

**Colors：**
```css
:root {
    --bg-cream: #f5f3ee;
    --text-primary: #1a1a1a;
    --text-secondary: #555;
    --accent-warm: #e8d4c0;
}
```

**Signature Elements：**
- 抽象几何形状（圆形轮廓 + 线 + 点）
- 粗边框的 CTA 方框
- 机敏、口语化的文案风格
- **不用插画，只用几何 CSS 形状**

---

## 特色主题

### 9. Neon Cyber

**Vibe：** 未来感、科技感、自信

**Typography：** `Clash Display` + `Satoshi`（Fontshare）

**Colors：** 深海军蓝（#0a0f1c）、青色强调（#00ffcc）、洋红（#ff00aa）

**Signature：** 粒子背景、霓虹辉光、网格纹

---

### 10. Terminal Green

**Vibe：** 面向开发者、黑客美学

**Typography：** `JetBrains Mono`（仅等宽）

**Colors：** GitHub 深色（#0d1117）、终端绿（#39d353）

**Signature：** 扫描线、闪烁光标、代码语法着色

---

### 11. Swiss Modern

**Vibe：** 干净、精确、包豪斯风

**Typography：** `Archivo` (800) + `Nunito` (400)

**Colors：** 纯白、纯黑、红色强调（#ff3300）

**Signature：** 可见网格、非对称布局、几何形状

---

### 12. Paper & Ink

**Vibe：** 编辑感、文学感、沉静

**Typography：** `Cormorant Garamond` + `Source Serif 4`

**Colors：** 暖奶油（#faf9f7）、炭黑（#1a1a1a）、绯红强调（#c41e3a）

**Signature：** 首字下沉、拉页引文、雅致的分隔横线

---

## 字体搭配速查

| 预设 | 展示字体 | 正文字体 | 来源 |
|--------|--------------|-----------|--------|
| Bold Signal | Archivo Black | Space Grotesk | Google |
| Electric Studio | Manrope | Manrope | Google |
| Creative Voltage | Syne | Space Mono | Google |
| Dark Botanical | Cormorant | IBM Plex Sans | Google |
| Notebook Tabs | Bodoni Moda | DM Sans | Google |
| Pastel Geometry | Plus Jakarta Sans | Plus Jakarta Sans | Google |
| Split Pastel | Outfit | Outfit | Google |
| Vintage Editorial | Fraunces | Work Sans | Google |
| Neon Cyber | Clash Display | Satoshi | Fontshare |
| Terminal Green | JetBrains Mono | JetBrains Mono | JetBrains |

---

## 请勿使用（泛泛的 AI 套路）

**Fonts：** Inter、Roboto、Arial、系统字体用作展示字体

**Colors：** `#6366f1`（泛用靛蓝）、白底紫色渐变

**Layouts：** 全部居中、套路化主视觉、一模一样的卡片网格

**Decorations：** 写实插画、无谓的玻璃拟态、毫无目的的投影

---

## CSS 易错点

### 对 CSS 函数取负

**WRONG — 浏览器会静默忽略（不报控制台错误）：**
```css
right: -clamp(28px, 3.5vw, 44px);   /* Browser ignores this */
margin-left: -min(10vw, 100px);      /* Browser ignores this */
```

**CORRECT — 用 `calc()` 包裹：**
```css
right: calc(-1 * clamp(28px, 3.5vw, 44px));  /* Works */
margin-left: calc(-1 * min(10vw, 100px));     /* Works */
```

CSS 不允许在函数名前直接加前导 `-`。浏览器会静默丢弃整条声明，不报错，元素只是出现在错误的位置。**对 CSS 函数取负一律用 `calc(-1 * ...)`。**
