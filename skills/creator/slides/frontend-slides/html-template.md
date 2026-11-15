> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/html-template.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# HTML 演示文稿模板

生成幻灯片演示文稿的参考架构。每份演示文稿都遵循固定的 16:9 舞台模型：幻灯片按 1920×1080 编写，整个舞台再缩放以适配浏览器窗口。

## 基础 HTML 结构

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentation Title</title>

    <!-- Fonts: use Fontshare or Google Fonts — never system fonts -->
    <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=...">

    <style>
        /* ===========================================
           CSS CUSTOM PROPERTIES (THEME)
           Change these to change the whole look
           =========================================== */
        :root {
            /* Colors — from chosen style preset */
            --bg-primary: #0a0f1c;
            --bg-secondary: #111827;
            --text-primary: #ffffff;
            --text-secondary: #9ca3af;
            --accent: #00ffcc;
            --accent-glow: rgba(0, 255, 204, 0.3);

            /* Typography — authored at 1920×1080 stage size */
            --font-display: 'Clash Display', sans-serif;
            --font-body: 'Satoshi', sans-serif;
            --title-size: 112px;
            --subtitle-size: 34px;
            --body-size: 28px;

            /* Spacing — authored at 1920×1080 stage size */
            --slide-padding: 72px;
            --content-gap: 32px;

            /* Animation */
            --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
            --duration-normal: 0.6s;
        }

        /* ===========================================
           BASE STYLES
           =========================================== */
        * { margin: 0; padding: 0; box-sizing: border-box; }

        /* --- PASTE viewport-base.css CONTENTS HERE --- */

        /* ===========================================
           ANIMATIONS
           Trigger via .visible class on the active slide
           =========================================== */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity var(--duration-normal) var(--ease-out-expo),
                        transform var(--duration-normal) var(--ease-out-expo);
        }

        .slide.visible .reveal {
            opacity: 1;
            transform: translateY(0);
        }

        /* Stagger children for sequential reveal */
        .reveal:nth-child(1) { transition-delay: 0.1s; }
        .reveal:nth-child(2) { transition-delay: 0.2s; }
        .reveal:nth-child(3) { transition-delay: 0.3s; }
        .reveal:nth-child(4) { transition-delay: 0.4s; }

        /* ... preset-specific styles ... */
    </style>
</head>
<body>
    <div class="deck-viewport">
        <main class="deck-stage" id="deckStage">
            <section class="slide title-slide active">
                <h1 class="reveal">Presentation Title</h1>
                <p class="reveal">Subtitle or author</p>
            </section>

            <section class="slide">
                <div class="slide-content">
                    <h2 class="reveal">Slide Title</h2>
                    <p class="reveal">Content...</p>
                </div>
            </section>

            <!-- More slides... -->
        </main>
    </div>

    <script>
        /* ===========================================
           SLIDE PRESENTATION CONTROLLER
           =========================================== */
        class SlidePresentation {
            constructor() {
                this.slides = document.querySelectorAll('.slide');
                this.currentSlide = 0;
                this.stage = document.getElementById('deckStage');
                this.setupStageScale();
                this.setupKeyboardNav();
                this.setupTouchNav();
                this.showSlide(0);
            }

            setupStageScale() {
                const scale = () => {
                    const factor = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
                    const x = (window.innerWidth - 1920 * factor) / 2;
                    const y = (window.innerHeight - 1080 * factor) / 2;
                    this.stage.style.transform = `translate(${x}px, ${y}px) scale(${factor})`;
                };
                scale();
                window.addEventListener('resize', scale);
            }

            setupKeyboardNav() {
                // Arrow keys, Space, Page Up/Down
            }

            setupTouchNav() {
                // Touch/swipe support for mobile
            }

            showSlide(index) {
                this.currentSlide = Math.max(0, Math.min(index, this.slides.length - 1));
                this.slides.forEach((slide, i) => {
                    slide.classList.toggle('active', i === this.currentSlide);
                    slide.classList.toggle('visible', i === this.currentSlide);
                });
            }
        }

        new SlidePresentation();
    </script>
</body>
</html>
```

## 必需的 JavaScript 功能

每份演示文稿必须包含：

1. **SlidePresentation Class**：主控制器，负责：
   - 键盘导航（方向键、空格、Page Up/Down）
   - 触摸/滑动支持
   - 鼠标滚轮导航
   - 可选的进度指示或页码，放在幻灯片舞台之外

2. **Stage Scaling**：实现固定的 16:9 演示行为：
   - 所有幻灯片在 `.deck-stage` 内保持 1920×1080
   - 用一次 transform 缩放整个舞台
   - 按需加黑边或左右留黑；绝不按设备重排幻灯片内容

3. **Optional Enhancements**（与所选风格匹配）：
   - 带拖尾的自定义光标
   - 粒子系统背景（canvas）
   - 视差效果
   - 悬停时的 3D 倾斜
   - 磁吸按钮
   - 数字滚动动画

4. **Inline Editing**（草稿生成后默认包含）：
   - 编辑切换按钮（默认隐藏，通过悬停热区或 `E` 键显现）
   - 自动保存到 localStorage
   - 导出/保存文件功能
   - 见下文"Inline Editing Implementation"一节

## 行内编辑实现

行内编辑是草稿生成后的轻量附加能力。在生成前的问询阶段，不要问用户是否需要。默认包含，除非用户明确要求锁定/仅导出的演示文稿，或不要任何编辑控件。

**不要用 CSS `~` 兄弟选择器做基于悬停的显示/隐藏。** 纯 CSS 方案（`edit-hotzone:hover ~ .edit-toggle`）会失败，因为切换按钮上的 `pointer-events: none` 会打断悬停链：用户悬停热区 -> 按钮显现 -> 鼠标移向按钮 -> 离开热区 -> 按钮在点击前消失。

**必需方案：基于 JS 的悬停，配 400ms 延迟超时。**

HTML：
```html
<div class="edit-hotzone"></div>
<button class="edit-toggle" id="editToggle" title="Edit mode (E)">✏️</button>
```

CSS（可见性只由 JS 类控制）：
```css
/* Do NOT use CSS ~ sibling selector for this!
   pointer-events: none breaks the hover chain.
   Must use JS with delay timeout. */
.edit-hotzone {
    position: fixed; top: 0; left: 0;
    width: 80px; height: 80px;
    z-index: 10000;
    cursor: pointer;
}
.edit-toggle {
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
    z-index: 10001;
}
.edit-toggle.show,
.edit-toggle.active {
    opacity: 1;
    pointer-events: auto;
}
```

JS（三种交互方式）：
```javascript
// 1. Click handler on the toggle button
document.getElementById('editToggle').addEventListener('click', () => {
    editor.toggleEditMode();
});

// 2. Hotzone hover with 400ms grace period
const hotzone = document.querySelector('.edit-hotzone');
const editToggle = document.getElementById('editToggle');
let hideTimeout = null;

hotzone.addEventListener('mouseenter', () => {
    clearTimeout(hideTimeout);
    editToggle.classList.add('show');
});
hotzone.addEventListener('mouseleave', () => {
    hideTimeout = setTimeout(() => {
        if (!editor.isActive) editToggle.classList.remove('show');
    }, 400);
});
editToggle.addEventListener('mouseenter', () => {
    clearTimeout(hideTimeout);
});
editToggle.addEventListener('mouseleave', () => {
    hideTimeout = setTimeout(() => {
        if (!editor.isActive) editToggle.classList.remove('show');
    }, 400);
});

// 3. Hotzone direct click
hotzone.addEventListener('click', () => {
    editor.toggleEditMode();
});

// 4. Keyboard shortcut (E key, skip when editing text)
document.addEventListener('keydown', (e) => {
    if ((e.key === 'e' || e.key === 'E') && !e.target.getAttribute('contenteditable')) {
        editor.toggleEditMode();
    }
});
```

## 图片流程（无图片时跳过）

如果用户在 Phase 1 选择了"No images"，整节跳过。若提供了图片，先处理再生成 HTML。

**Dependency：** `pip install Pillow`

### 图片处理

```python
from PIL import Image, ImageDraw

# Circular crop (for logos on modern/clean styles)
def crop_circle(input_path, output_path):
    img = Image.open(input_path).convert('RGBA')
    w, h = img.size
    size = min(w, h)
    left, top = (w - size) // 2, (h - size) // 2
    img = img.crop((left, top, left + size, top + size))
    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size, size], fill=255)
    img.putalpha(mask)
    img.save(output_path, 'PNG')

# Resize (for oversized images that inflate HTML)
def resize_max(input_path, output_path, max_dim=1200):
    img = Image.open(input_path)
    img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    img.save(output_path, quality=85)
```

| 情形 | 操作 |
|-----------|-----------|
| 圆润风格上的方形 logo | `crop_circle()` |
| 图片大于 1MB | `resize_max(max_dim=1200)` |
| 宽高比不对 | 用 `img.crop()` 手动裁切 |

处理后的图片保存时加 `_processed` 后缀。绝不覆盖原图。

### 图片放置

**使用直接文件路径**（不用 base64）：演示文稿在本地查看。

```html
<img src="assets/logo_round.png" alt="Logo" class="slide-image logo">
<img src="assets/screenshot.png" alt="Screenshot" class="slide-image screenshot">
```

```css
.slide-image {
    max-width: 100%;
    max-height: min(50vh, 400px);
    object-fit: contain;
    border-radius: 8px;
}
.slide-image.screenshot {
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
.slide-image.logo {
    max-height: min(30vh, 200px);
}
```

**调整边框/阴影颜色以贴合所选风格的强调色。** 绝不在多张幻灯片上重复同一张图片（标题页与结束页的 logo 除外）。

**Placement patterns：** 标题页上 logo 居中。截图放在带文字的两栏布局里。全出血图片作幻灯片背景并叠加文字（少用）。

---

## 代码质量

**Comments：** 每一节都要有清晰的注释，说明它做什么、如何修改。

**Accessibility：**
- 语义化 HTML（`<section>`、`<nav>`、`<main>`）
- 键盘导航完整可用
- 需要处加 ARIA 标签
- 支持 `prefers-reduced-motion`（已包含在 viewport-base.css 中）

## 文件结构

单份演示文稿：
```
presentation.html    # Self-contained, all CSS/JS inline
assets/              # Images only, if any
```

一个项目里放多份演示文稿：
```
[name].html
[name]-assets/
```
