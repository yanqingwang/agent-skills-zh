> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/scroll-choreography.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 滚动编排：唯一凭本事挣来的模式

默认依然是没有滚动动效：`craft.md` § 5 的一次性显现（reveal-once）才是页面常态。本文件是那个例外：一种滚动联动（scroll-linked）模式，只使用一次、只用在结构上，且内容确有值得钉住（pin）或擦洗（scrub）的序列时才用。sloplint 的 F8 会统计模式家族的数量，并把第二个标出来。

## 预算

- **每页一种模式。**两种滚动行为会争夺同一份注意力。
- **绝不用于正文文本。**目标只能是结构性元素：一个被钉住的区块、一个展示元素、一条 2px 竖线、插图。散文绝不在读者眼皮底下移动。
- **Hero 入场规则不变。**`craft.md` § 5 的页面加载编排保持原样；滚动编排绝不取代它，也没有元素同时承担两者。
- **必须有静态终态。**基础 CSS 直接呈现完成后的布局。整套编排完全放在 `@supports (animation-timeline: view())` 与 `@media (prefers-reduced-motion: no-preference) and (min-width: 40rem)` 之内；减弱动效的用户、小屏幕与不支持的浏览器拿到的都是完整页面。
- **顺序很重要：**`animation` 简写会重置 `animation-timeline` 与 `animation-range`，所以要在它之后声明这两项。
- **`linear` 在这里是正确的：**擦洗把滚动距离一比一映射为进度；缓动曲线会让页面与滚动条脱钩。
- 一种模式计入页面三个动效原语之一（`microinteractions.md`）。

## 1 · 钉住的章节：区块被钉住期间步骤逐条显现

高个轨道拥有命名的 view-timeline；被钉住窗格里的步骤分段消费它。（钉住的窗格内部的元素驱动不了自己的 `view()`：它们并不在移动。）

```html
<section class="chapter">
  <div class="chapter__pin">
    <h2>How it works</h2>
    <ol class="chapter__steps"><li>…</li><li>…</li><li>…</li></ol>
  </div>
</section>
```
```css
.chapter { min-height: 280vh; }                          /* track length = pin duration */
.chapter__pin { position: sticky; top: calc(var(--banner-height, 0px) + var(--space-xl)); }
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) and (min-width: 40rem) {
    .chapter { view-timeline: --chapter block; }
    .chapter__steps li { animation: chapter-step linear both; animation-timeline: --chapter; }
    .chapter__steps li:nth-child(1) { animation-range: contain 5% contain 30%; }
    .chapter__steps li:nth-child(2) { animation-range: contain 30% contain 55%; }
    .chapter__steps li:nth-child(3) { animation-range: contain 55% contain 80%; }
    @keyframes chapter-step { from { opacity: 0.2; transform: translateY(8px); } to { opacity: 1; transform: none; } }
  }
}
```

## 2 · 擦洗联动的大标题：一个展示元素，剪裁擦除

用于页面中部的 Statement 标题（`layout.md` § 5），绝不用于 Hero 的 `h1`，后者的入场就是加载显现。每页一个元素。

```css
.statement__head { /* base: fully drawn */ }
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) and (min-width: 40rem) {
    .statement__head {
      animation: head-wipe linear both;
      animation-timeline: view();
      animation-range: entry 20% cover 45%;
    }
    @keyframes head-wipe {
      from { clip-path: inset(0 100% 0 0); transform: translateX(-0.25em); }
      to   { clip-path: inset(0 0 0 0); transform: none; }
    }
  }
}
```

## 3 · 进度竖线：用 `scroll(root)` 缩放一条 2px 细线

阅读进度呈发丝线状，而不是浏览器控件条。它是功能性指示器，所以 `linear` 是标准选择。低于 40rem 时隐藏（它会吃掉移动端的留白）。

```css
.spine { position: fixed; inset-block: 0; left: max(1rem, 2vw); width: 2px; background: var(--color-rule); }
.spine::after { content: ""; position: absolute; inset: 0; background: var(--color-accent);
  transform-origin: top; transform: scaleY(0); }
@media (max-width: 40rem) { .spine { display: none; } }
@supports (animation-timeline: scroll()) {
  @media (prefers-reduced-motion: no-preference) and (min-width: 40rem) {
    .spine::after { animation: spine-grow linear both; animation-timeline: scroll(root); }
    @keyframes spine-grow { to { transform: scaleY(1); } }
  }
}
```

## 4 · 粘性双联：两窗格钉住

结构是分栏（Split，`layout.md` § 5）且其中一栏被钉住：`.sticky-stack { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: var(--gap-columns); }`、`.pane-sticky { position: sticky; top: calc(var(--banner-height, 0px) + var(--space-xl)); align-self: start; z-index: var(--z-sticky); }`（它停靠在 sticky 导航之下，56）、`.pane-scroll { display: grid; gap: var(--space-2xl); }`，每张插图为 16:10、高 440px 或更多；低于 60rem 时改单列、`position: static`。编排只添加这一点：滚动一侧的插图在各自的 `view()` 上淡入（它们在移动，所以自时间线可用）；钉住的一侧从一副双联撑到下一副。

```css
/* base: .sticky-stack grid + .pane-sticky pin, above; the pinned side holds down the page */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) and (min-width: 40rem) {
    .pane-scroll figure { animation: fig-in linear both; animation-timeline: view();
      animation-range: entry 0% entry 60%; }
    @keyframes fig-in { from { opacity: 0.3; transform: translateY(12px); } to { opacity: 1; transform: none; } }
  }
}
```

## JS 回退（可选，共用）

当有 JS 而 `animation-timeline` 不受支持时，唯一的回退是 `craft.md` § 5 的一次性显现，绝不用滚动监听器或擦洗 polyfill：

```html
<script>
  if (!CSS.supports('animation-timeline: view()')) {
    const io = new IntersectionObserver((es) => es.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('is-seen'); io.unobserve(e.target); }
    }), { rootMargin: '0px 0px -20%' });
    document.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));
  }
</script>
```

再配一个 `--dur-long` 的 `--ease-out` 过渡到终态，并且只在脚本添加的 `.js` 类之下隐藏 `[data-reveal]`（62）。没有脚本也没有支持时，静态布局本身就是完成的页面。
