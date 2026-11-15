> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`plugins/frontend-slides/skills/frontend-slides/animation-patterns.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动画模式参考

生成演示文稿时参考本文件。让动画贴合想要传达的感觉。

## 效果与感觉对照

| 感觉 | 动画 | 视觉线索 |
|---------|-----------|-------------|
| **戏剧 / 电影感** | 慢速淡入（1-1.5s）、大幅缩放过渡（0.9 到 1）、视差滚动 | 深色背景、聚光效果、全出血图片 |
| **科技 / 未来感** | 霓虹辉光（`box-shadow`）、故障/字符乱码文字、网格揭示 | 粒子系统（canvas）、网格纹、等宽点缀、青/洋红/电光蓝 |
| **俏皮 / 亲和** | 弹性缓动（弹簧物理）、漂浮/上下浮动 | 圆角、柔和/明亮配色、手绘元素 |
| **专业 / 商务** | 克制快速的动画（200-300ms）、干净的滑动 | 海军蓝/石板灰/炭黑、精确间距、以数据可视化为主 |
| **平静 / 极简** | 极慢的细微运动、柔和淡入淡出 | 大量留白、低饱和配色、衬线排印、宽裕内边距 |
| **编辑 / 杂志感** | 文字错落揭示、图文互动 | 强字体层级、拉页引文、破格布局、衬线标题配无衬线正文 |

## 入场动画

```css
/* Fade + Slide Up (most versatile) */
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s var(--ease-out-expo),
                transform 0.6s var(--ease-out-expo);
}
.visible .reveal {
    opacity: 1;
    transform: translateY(0);
}

/* Scale In */
.reveal-scale {
    opacity: 0;
    transform: scale(0.9);
    transition: opacity 0.6s, transform 0.6s var(--ease-out-expo);
}

/* Slide from Left */
.reveal-left {
    opacity: 0;
    transform: translateX(-50px);
    transition: opacity 0.6s, transform 0.6s var(--ease-out-expo);
}

/* Blur In */
.reveal-blur {
    opacity: 0;
    filter: blur(10px);
    transition: opacity 0.8s, filter 0.8s var(--ease-out-expo);
}
```

## 背景效果

```css
/* Gradient Mesh — layered radial gradients for depth */
.gradient-bg {
    background:
        radial-gradient(ellipse at 20% 80%, rgba(120, 0, 255, 0.3) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 255, 200, 0.2) 0%, transparent 50%),
        var(--bg-primary);
}

/* Noise Texture — inline SVG for grain */
.noise-bg {
    background-image: url("data:image/svg+xml,..."); /* Inline SVG noise */
}

/* Grid Pattern — subtle structural lines */
.grid-bg {
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 50px 50px;
}
```

## 交互效果

```javascript
/* 3D Tilt on Hover — adds depth to cards/panels */
class TiltEffect {
    constructor(element) {
        this.element = element;
        this.element.style.transformStyle = 'preserve-3d';
        this.element.style.perspective = '1000px';

        this.element.addEventListener('mousemove', (e) => {
            const rect = this.element.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            this.element.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 10}deg)`;
        });

        this.element.addEventListener('mouseleave', () => {
            this.element.style.transform = 'rotateY(0) rotateX(0)';
        });
    }
}
```

## 故障排查

| 问题 | 修复 |
|---------|-----|
| 字体加载失败 | 检查 Fontshare/Google Fonts 的 URL；确认 CSS 里的字体名一致 |
| 动画不触发 | 确认 Intersection Observer 在运行；检查是否添加了 `.visible` 类 |
| 滚动吸附失效 | 确认 html 上有 `scroll-snap-type: y mandatory`；每页需要 `scroll-snap-align: start` |
| 移动端问题 | 在 768px 断点关闭重效果；测试触摸事件；减少粒子数量 |
| 性能问题 | 谨慎使用 `will-change`；优先用 `transform`/`opacity` 动画；对滚动处理函数做节流 |
