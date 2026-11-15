> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/optimize.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

性能是一项功能。找出这个界面真正的瓶颈，修好它，然后测量。不慢的东西不要优化。

## 评估性能问题

了解当前性能并找出问题：

1. **测量现状**：
   - **Core Web Vitals**：LCP、INP、CLS 分数
   - **加载时间**：可交互时间、首次内容绘制
   - **包体积**：JavaScript、CSS、图片大小
   - **运行时性能**：帧率、内存占用、CPU 占用
   - **网络**：请求数、载荷大小、瀑布图

2. **定位瓶颈**：
   - 什么慢？（首屏加载？交互？动画？）
   - 原因是什么？（大图？昂贵的 JavaScript？布局抖动？）
   - 有多糟？（可感知？恼人？阻塞？）
   - 影响谁？（所有用户？只有移动端？慢网络？）

前后都要测量。没有测量就优化，是把力气花在不重要的事上。

## 优化策略

制定系统性的改进计划：

### 加载性能

**优化图片**：
- 用现代格式（WebP、AVIF）
- 尺寸合适（300px 的显示区域不要加载 3000px 的图）
- 首屏以下的图片懒加载
- 响应式图片（`srcset`、`picture` 元素）
- 压缩图片（80-85% 质量通常感知不到）
- 用 CDN 加快分发

```html
<img 
  src="hero.webp"
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="(max-width: 400px) 400px, (max-width: 800px) 800px, 1200px"
  alt="Hero image"
/>
```

**减小 JavaScript 包**：
- 代码分割（按路由、按组件）
- Tree shaking（移除未用代码）
- 移除未用的依赖
- 非关键代码懒加载
- 大组件用动态导入

```javascript
// Lazy load heavy component
const HeavyChart = lazy(() => import('./HeavyChart'));
```

**优化 CSS**：
- 移除未用的 CSS
- 关键 CSS 内联，其余异步
- 压缩 CSS 文件
- 独立区域用 CSS containment

**优化字体**：
- 用 `font-display: swap` 或 `optional`
- 字体子集化（只要用到的字符）
- 预加载关键字体
- 合适时用系统字体
- 限制加载的字重数量

```css
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-display: swap; /* Show fallback immediately */
  unicode-range: U+0020-007F; /* Basic Latin only */
}
```

**优化加载策略**：
- 关键资源优先（非关键的 async/defer）
- 预加载关键资源
- 预取可能访问的下一页
- Service worker 处理离线/缓存
- HTTP/2 或 HTTP/3 多路复用

### 渲染性能

**避免布局抖动**：
```javascript
// ❌ Bad: Alternating reads and writes (causes reflows)
elements.forEach(el => {
  const height = el.offsetHeight; // Read (forces layout)
  el.style.height = height * 2; // Write
});

// ✅ Good: Batch reads, then batch writes
const heights = elements.map(el => el.offsetHeight); // All reads
elements.forEach((el, i) => {
  el.style.height = heights[i] * 2; // All writes
});
```

**优化渲染**：
- 独立区域用 CSS `contain` 属性
- 降低 DOM 深度（越扁平越快）
- 缩小 DOM 规模（元素更少）
- 长列表用 `content-visibility: auto`
- 超长列表用虚拟滚动（react-window、TanStack Virtual）

**减少绘制与合成**：
- 位移用 `transform` 和 `opacity` 最可靠，但当模糊、滤镜、遮罩、裁剪路径、阴影和颜色变化能带来有意义的质感时，尽管用
- 不要随手动画驱动布局的属性（`width`、`height`、`top`、`left`、margin）
- `will-change` 只在已知昂贵的操作上少用
- 模糊/滤镜/阴影效果要圈定绘制区域（越小越隔离越快）

### 动画性能

**GPU 加速**：
```css
/* ✅ GPU-accelerated (fast) */
.animated {
  transform: translateX(100px);
  opacity: 0.5;
}

/* ❌ CPU-bound (slow) */
.animated {
  left: 100px;
  width: 300px;
}
```

**流畅 60fps**：
- 每帧目标 16ms（60fps）
- JS 动画用 `requestAnimationFrame`
- 滚动处理器做防抖/节流
- 能用 CSS 动画就用 CSS 动画
- 动画期间避免长时间运行的 JavaScript

**Intersection Observer**：
```javascript
// Efficiently detect when elements enter viewport
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Element is visible, lazy load or animate
    }
  });
});
```

### React/框架优化

**React 专属**：
- 昂贵组件用 `memo()`
- 昂贵计算用 `useMemo()` 和 `useCallback()`
- 长列表虚拟化
- 路由代码分割
- 避免在 render 里创建内联函数
- 用 React DevTools Profiler

**跨框架通用**：
- 减少重渲染
- 昂贵操作做防抖
- 计算值做记忆化
- 路由和组件懒加载

### 网络优化

**减少请求**：
- 合并小文件
- 图标用 SVG sprite
- 小的关键资源内联
- 移除未用的第三方脚本

**优化 API**：
- 用分页（不要一次全加载）
- GraphQL 只请求需要的字段
- 响应压缩（gzip、brotli）
- HTTP 缓存头
- 静态资源走 CDN

**慢网络优化**：
- 按连接状况自适应加载（navigator.connection）
- 乐观 UI 更新
- 请求优先级
- 渐进增强

## Core Web Vitals 优化

### Largest Contentful Paint（LCP < 2.5s）
- 优化首屏大图
- 内联关键 CSS
- 预加载关键资源
- 用 CDN
- 服务端渲染

### Interaction to Next Paint（INP < 200ms）
- 拆分长任务
- 推迟非关键 JavaScript
- 重计算放 web worker
- 减少 JavaScript 执行时间

### Cumulative Layout Shift（CLS < 0.1）
- 给图片和视频设置尺寸
- 不要在现有内容上方注入内容
- 用 CSS `aspect-ratio` 属性
- 给广告/嵌入预留空间
- 避免引起布局位移的动画

```css
/* Reserve space for image */
.image-container {
  aspect-ratio: 16 / 9;
}
```

## 性能监控

**可用工具**：
- Chrome DevTools（Lighthouse、Performance 面板）
- WebPageTest
- Core Web Vitals（Chrome UX Report）
- 包分析器（webpack-bundle-analyzer）
- 性能监控（Sentry、DataDog、New Relic）

**关键指标**：
- LCP、INP、CLS（Core Web Vitals；INP 于 2024 年 3 月取代 FID）
- 可交互时间（TTI）
- 首次内容绘制（FCP）
- 总阻塞时间（TBT）
- 包体积
- 请求数

在真实设备、真实网络条件下测量。快速网络下的桌面 Chrome 不代表真实情况。

**避免**：
- 不测量就优化（过早优化）
- 为性能牺牲可访问性
- 优化过程中弄坏功能
- 到处用 `will-change`（会创建新图层、占用内存）
- 首屏内容懒加载
- 忽略大问题去做微优化（先优化最大的瓶颈）
- 忘掉移动端性能（设备往往更慢、网络更差）

## 验证改进

确认优化起效：

- **前后指标**：对比 Lighthouse 分数
- **真实用户监控**：跟踪真实用户的改善
- **不同设备**：在低端 Android 上测，不只是旗舰 iPhone
- **慢网络**：限速到 3G，测体验
- **无回归**：确保功能仍然正常
- **用户感受**：*感觉*变快了吗？

面向用户的数字动起来之后，交给 `/impeccable polish` 做最后一遍打磨。
