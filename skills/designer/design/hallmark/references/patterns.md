> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/patterns.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 模式（Patterns）

每个页面都会重复的部分，写法都能通过检查关卡。代码的形状照抄即可；名称、文案、数值与构图由你决定。`tokens.css`、`base.css` 与占位脚本来自脚手架。

## 控件：全部八种状态

```css
.btn { display: inline-flex; align-items: center; gap: var(--space-xs); min-height: 48px; padding: 0 var(--space-lg); border: 1px solid var(--color-ink); border-radius: var(--radius-input, var(--radius-pill)); background: var(--color-ink); color: var(--color-paper); font: 500 var(--text-md)/1 var(--font-body); white-space: nowrap; text-decoration: none; cursor: pointer; transition: background-color var(--dur-short) var(--ease-out), transform var(--dur-micro) var(--ease-out); }
.btn:hover { background: var(--color-ink-2); }
.btn:active { transform: translateY(1px); }
.btn:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
.btn:disabled, .btn[aria-disabled="true"] { opacity: 0.55; cursor: not-allowed; transform: none; }
.btn[aria-busy="true"] { cursor: progress; }
.btn--quiet { background: transparent; color: var(--color-ink); border-color: var(--color-rule); }
.btn--quiet:hover { background: var(--color-paper-2); }
@media (prefers-reduced-motion: reduce) { .btn { transition: background-color var(--dur-short) linear; } }
```

每页一个实心主按钮（F4）；quiet 按钮放在别处。错误与成功状态属于表单，见下文。

## 槽位里的一张照片

```html
<figure class="photo" data-slot="hero" data-alt="The orchard in October, rows of trees heavy with fruit">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/.../1280px-....jpg"
       srcset=".../960px-....jpg 960w, .../1280px-....jpg 1280w, .../1920px-....jpg 1920w" sizes="(min-width: 60rem) 45vw, 100vw"
       width="4000" height="5000" alt="Rows of apple trees in October light" style="object-position: 50% 40%" fetchpriority="high">
</figure>
<p class="caption">Picking runs from September to the first frost.</p>
```

```css
.photo { aspect-ratio: 4 / 5; min-height: 440px; margin: 0; border-radius: var(--radius-card); }
.photo > img { outline: 1px solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
.caption { margin-top: var(--space-sm); font-size: var(--text-sm); color: var(--color-ink-2); }
```

其中的 `<img>` 来自 `theme.mjs photos`；`base.css` 提供封面式裁切、加载遮罩和主题的特有处理。署名放在页脚的 *Photographs* 行里；图注是来自提示词的事实，不在画面框内。产品样张用同一种槽位但不放 `<img>`：按实际尺寸构建的界面（`imagery.md` § 4）。

## 少数几个选项的选择

```html
<fieldset class="seg"><legend>Size</legend>
  <input type="radio" name="size" id="s1" value="1" checked><label for="s1">One box</label>
  <input type="radio" name="size" id="s2" value="2"><label for="s2">Two boxes</label>
</fieldset>
```

```css
.seg input { position: absolute; opacity: 0; width: 1px; height: 1px; }
.seg label { display: inline-flex; align-items: center; min-height: 44px; padding: 0 var(--space-md); border: 1px solid var(--color-rule); cursor: pointer; }
.seg input:checked + label { background: var(--color-ink); color: var(--color-paper); }
.seg input:focus-visible + label { outline: 2px solid var(--color-focus); outline-offset: 2px; }
```

单选按钮以一像素大小留在文档流里（53）；状态和焦点圈由 label 承担，用正文字体，句首大写。

## 横向轨道（rail）与切换器（switcher）

```html
<ul class="rail" tabindex="0" aria-label="Upcoming dates">
  <li><time datetime="2027-06-12">12 June</time> Whitby</li>
  <!-- five or more items; the next one cut by the edge -->
</ul>
<div class="switch" data-switch>
  <div class="seg" role="tablist" aria-label="Menu"><button role="tab" aria-selected="true" aria-controls="m1" id="t1">Lunch</button><button role="tab" aria-selected="false" aria-controls="m2" id="t2" tabindex="-1">Dinner</button></div>
  <section role="tabpanel" id="m1" aria-labelledby="t1">...</section>
  <section role="tabpanel" id="m2" aria-labelledby="t2" hidden>...</section>
</div>
```

```css
.rail { display: grid; grid-auto-flow: column; grid-auto-columns: minmax(16rem, 22%); gap: var(--gap-columns); overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-inline: var(--gutter); padding-inline: var(--gutter); overscroll-behavior-x: contain; }
.rail > * { scroll-snap-align: start; }
.rail:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 4px; }
```

轨道在获得焦点后可用触屏、滚轮和方向键滚动，并放在容器内边距之外，让边缘截断下一项。切换器的标签页用方向键移动（几行脚本负责设置 `aria-selected`、`tabindex` 与 `hidden`）；没有脚本时所有面板按顺序显示。固定成对出现时，在视觉列上加 `position: sticky; top: var(--space-2xl)`，60rem 以下解除。

## 提示词没给的一个事实

```html
<p>Doors at <span class="fill" data-fill="time">time to be announced</span>, at <a href="#venue">the venue</a>.</p>
```

```css
.fill { padding: 0 0.25em; border: 1px dashed color-mix(in oklch, var(--color-muted) 70%, transparent); border-radius: 3px; color: var(--color-muted); -webkit-box-decoration-break: clone; box-decoration-break: clone; }
```

每页最多两个，每个都要在交接说明中点名（`craft.md` § 8）。

## 暂时无处提交的表单

```html
<form class="signup" data-endpoint="" novalidate>
  <label for="email">Email address</label>
  <div class="signup__row">
    <input id="email" name="email" type="email" autocomplete="email" required>
    <button class="btn" type="submit">Send me the date</button>
  </div>
  <p class="signup__help" id="email-help" aria-live="polite"></p>
</form>
```

```js
document.querySelectorAll('form[data-endpoint]').forEach((form) => {
  const input = form.querySelector('input'), help = form.querySelector('[aria-live]');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const ok = input.checkValidity();
    input.toggleAttribute('aria-invalid', !ok);
    if (!ok) { input.setAttribute('aria-describedby', help.id); help.textContent = 'That address looks incomplete. Write it as name@example.com.'; input.focus(); return; }
    if (!form.dataset.endpoint) { help.textContent = 'Nothing was sent: this form is not connected yet.'; return; }
    fetch(form.dataset.endpoint, { method: 'POST', body: new FormData(form) })
      .then((r) => { help.textContent = r.ok ? 'Thanks. The date goes to ' + input.value.trim() + '.' : 'That did not go through. Try again in a minute.'; })
      .catch(() => { help.textContent = 'That did not go through. Try again in a minute.'; });
  });
});
```

```css
.signup__row { display: flex; gap: var(--space-xs); }
.signup input { flex: 1; min-width: 0; min-height: 48px; padding: 0 var(--space-md); border: 1px solid var(--color-muted); border-radius: var(--radius-input, var(--radius-pill)); background: var(--color-paper); color: var(--color-ink); outline: 2px solid transparent; outline-offset: -3px; }
.signup input:focus-visible { outline-color: var(--color-focus); }
.signup input[aria-invalid] { border-color: var(--color-error); }
.signup__help { min-height: 1lh; margin-top: var(--space-2xs); font-size: var(--text-sm); color: var(--color-muted); }
```

## 无脚本也能成立的一次显现动画

```html
<script>document.documentElement.classList.add('js');</script>
```

```css
.js [data-reveal] { opacity: 0; transform: translateY(8px); transition: opacity var(--dur-long) var(--ease-out), transform var(--dur-long) var(--ease-out); transition-delay: calc(var(--i, 0) * 40ms); }
.js [data-reveal].is-in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .js [data-reveal] { opacity: 1; transform: none; transition: none; } }
```

```js
const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -10% 0px' });
document.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));
```

关掉脚本时也可见（62），在减少动效偏好下直接呈现终态，只播放一次，且只用在主题允许动效的地方。

## 用于对比的数字

```css
.stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); }
.stats > * { padding-inline: var(--space-lg); border-left: 1px solid var(--color-rule); }
.stats > :first-child { padding-left: 0; border-left: 0; }
.stats b { display: block; font: 600 var(--text-3xl)/1 var(--font-display); font-variant-numeric: tabular-nums; }
@media (max-width: 60rem) { .stats { grid-template-columns: minmax(0, 1fr); } .stats > * { padding: var(--space-md) 0; border-left: 0; border-top: 1px solid var(--color-rule); } .stats > :first-child { border-top: 0; } }
```

只用用户给出的数字（46a），每个都带上单位和计量对象。

## 可暂停的循环

任何持续移动超过 5 秒的东西（跑马灯、环境动效循环、循环播放的视频）在脚本运行前保持静止，移出视口或开启减少动效时停止，悬停或聚焦时暂停，并带一个可见的暂停控件（18、WCAG 2.2.2）。

```html
<figure data-loop>
  <!-- the drawing, the loop or the video -->
  <button class="btn btn--quiet" type="button" data-loop-toggle>Pause</button>
</figure>
```

```css
[data-loop]:not(.is-running), [data-loop]:not(.is-running) *, [data-loop]:not(.is-running) *::before, [data-loop]:not(.is-running) *::after { animation-play-state: paused !important; }
html:not(.js) [data-loop-toggle] { display: none; }
@media (prefers-reduced-motion: reduce) { [data-loop-toggle] { display: none; } }
```

```js
document.querySelectorAll('[data-loop]').forEach((el) => {
  const btn = el.querySelector('[data-loop-toggle]');
  const s = { seen: false, hover: false, focus: false, held: matchMedia('(prefers-reduced-motion: reduce)').matches };
  const sync = () => {
    const run = s.seen && !s.hover && !s.focus && !s.held;
    el.classList.toggle('is-running', run);
    el.querySelectorAll('video').forEach((v) => (run ? v.play().catch(() => {}) : v.pause()));
    btn.textContent = s.held ? 'Play' : 'Pause';
  };
  btn.addEventListener('click', () => { s.held = !s.held; sync(); });
  [['pointerenter', 'hover', true], ['pointerleave', 'hover', false], ['focusin', 'focus', true], ['focusout', 'focus', false]].forEach(([t, k, v]) => el.addEventListener(t, () => { s[k] = v; sync(); }));
  new IntersectionObserver(([e]) => { s.seen = e.isIntersecting; sync(); }).observe(el);
});
```

## 绕过导航的途径

```html
<a class="skip" href="#main">Skip to content</a>
```

```css
.skip { position: absolute; left: var(--space-md); top: calc(-1 * var(--space-3xl)); z-index: var(--z-toast); padding: var(--space-xs) var(--space-md); background: var(--color-ink); color: var(--color-paper); }
.skip:focus-visible { top: var(--space-md); }
```
