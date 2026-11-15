> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# wcag-audit-patterns：详细模式与实操示例

## 审计清单

### 可感知（原则 1）

````markdown
## 1.1 Text Alternatives

### 1.1.1 Non-text Content (Level A)

- [ ] All images have alt text
- [ ] Decorative images have alt=""
- [ ] Complex images have long descriptions
- [ ] Icons with meaning have accessible names
- [ ] CAPTCHAs have alternatives

Check:

```html
<!-- Good -->
<img src="chart.png" alt="Sales increased 25% from Q1 to Q2" />
<img src="decorative-line.png" alt="" />

<!-- Bad -->
<img src="chart.png" />
<img src="decorative-line.png" alt="decorative line" />
```
````

## 1.2 时基媒体

### 1.2.1 纯音频与纯视频（Level A）

- [ ] 音频有文字稿
- [ ] 视频有音频描述或文字稿

### 1.2.2 字幕（Level A）

- [ ] 所有视频都有同步字幕
- [ ] 字幕准确且完整
- [ ] 包含说话人标识

### 1.2.3 音频描述（Level A）

- [ ] 视频对视觉内容有音频描述

## 1.3 可适应

### 1.3.1 信息与关系（Level A）

- [ ] 标题使用正确的标签（h1-h6）
- [ ] 列表使用 ul/ol/dl
- [ ] 表格有表头
- [ ] 表单输入有标签
- [ ] 有 ARIA 地标区域

检查：

```html
<!-- Heading hierarchy -->
<h1>Page Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
<h2>Another Section</h2>

<!-- Table headers -->
<table>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Price</th>
    </tr>
  </thead>
</table>
```

### 1.3.2 有意义的顺序（Level A）

- [ ] 阅读顺序合理
- [ ] CSS 定位不破坏顺序
- [ ] 焦点顺序与视觉顺序一致

### 1.3.3 感官特征（Level A）

- [ ] 指引不单独依赖形状/颜色
- [ ] "点击红色按钮" → "点击提交（红色按钮）"

## 1.4 可辨别

### 1.4.1 颜色的使用（Level A）

- [ ] 颜色不是传达信息的唯一手段
- [ ] 链接不靠颜色也能区分
- [ ] 错误状态不只靠颜色表达

### 1.4.3 对比度（最低）（Level AA）

- [ ] 文本：4.5:1 对比度
- [ ] 大号文本（18pt 及以上）：3:1
- [ ] UI 组件：3:1

工具：WebAIM Contrast Checker、axe DevTools

### 1.4.4 文本缩放（Level AA）

- [ ] 文本放大到 200% 无内容丢失
- [ ] 320px 宽度下无横向滚动
- [ ] 内容正确重排

### 1.4.10 重排（Level AA）

- [ ] 400% 缩放下内容重排
- [ ] 无二维滚动
- [ ] 320px 宽度下所有内容可访问

### 1.4.11 非文本对比度（Level AA）

- [ ] UI 组件有 3:1 对比度
- [ ] 焦点指示可见
- [ ] 图形对象可区分

### 1.4.12 文本间距（Level AA）

- [ ] 加大间距后无内容丢失
- [ ] 行高为字号的 1.5 倍
- [ ] 段落间距为字号的 2 倍
- [ ] 字符间距为字号的 0.12 倍
- [ ] 词间距为字号的 0.16 倍

````

### Operable (Principle 2)

```markdown
## 2.1 Keyboard Accessible

### 2.1.1 Keyboard (Level A)
- [ ] All functionality keyboard accessible
- [ ] No keyboard traps
- [ ] Tab order is logical
- [ ] Custom widgets are keyboard operable

Check:
```javascript
// Custom button must be keyboard accessible
<div role="button" tabindex="0"
     onkeydown="if(event.key === 'Enter' || event.key === ' ') activate()">
````

### 2.1.2 无键盘陷阱（Level A）

- [ ] 焦点能移出所有组件
- [ ] 模态对话框正确约束焦点
- [ ] 模态关闭后焦点返回

## 2.2 充足时间

### 2.2.1 时间可调（Level A）

- [ ] 会话超时可延长
- [ ] 超时前提醒用户
- [ ] 可选择禁用自动刷新

### 2.2.2 暂停、停止、隐藏（Level A）

- [ ] 移动内容可暂停
- [ ] 自动更新内容可暂停
- [ ] 动画尊重 prefers-reduced-motion

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```

## 2.3 癫痫与身体反应

### 2.3.1 三次闪烁（Level A）

- [ ] 内容闪烁不超过每秒 3 次
- [ ] 闪烁面积小（小于视口的 25%）

## 2.4 可导航

### 2.4.1 绕过区块（Level A）

- [ ] 有"跳到主内容"链接
- [ ] 定义了地标区域
- [ ] 标题结构正确

```html
<a href="#main" class="skip-link">Skip to main content</a>
<main id="main">...</main>
```

### 2.4.2 页面标题（Level A）

- [ ] 页面标题唯一且有描述性
- [ ] 标题反映页面内容

### 2.4.3 焦点顺序（Level A）

- [ ] 焦点顺序与视觉顺序一致
- [ ] 正确使用 tabindex

### 2.4.4 链接目的（结合上下文）（Level A）

- [ ] 链接脱离上下文也能看懂
- [ ] 不单独使用"点击这里"或"阅读更多"

```html
<!-- Bad -->
<a href="report.pdf">Click here</a>

<!-- Good -->
<a href="report.pdf">Download Q4 Sales Report (PDF)</a>
```

### 2.4.6 标题与标签（Level AA）

- [ ] 标题描述内容
- [ ] 标签描述用途

### 2.4.7 焦点可见（Level AA）

- [ ] 所有元素上焦点指示可见
- [ ] 自定义焦点样式满足对比度要求

```css
:focus {
  outline: 3px solid #005fcc;
  outline-offset: 2px;
}
```

### 2.4.11 焦点不被遮挡（Level AA）- WCAG 2.2

- [ ] 焦点元素不被完全遮挡
- [ ] 吸顶头部不遮挡焦点

````

### Understandable (Principle 3)

```markdown
## 3.1 Readable

### 3.1.1 Language of Page (Level A)
- [ ] HTML lang attribute set
- [ ] Language correct for content

```html
<html lang="en">
````

### 3.1.2 部分内容的语言（Level AA）

- [ ] 标记了语言变化

```html
<p>The French word <span lang="fr">bonjour</span> means hello.</p>
```

## 3.2 可预期

### 3.2.1 获得焦点时（Level A）

- [ ] 仅获得焦点不引发上下文变化
- [ ] 获得焦点时不出现意外弹窗

### 3.2.2 输入时（Level A）

- [ ] 不自动提交表单
- [ ] 上下文变化前提醒用户

### 3.2.3 一致的导航（Level AA）

- [ ] 导航在各页面间一致
- [ ] 重复组件顺序相同

### 3.2.4 一致的标识（Level AA）

- [ ] 相同功能 = 相同标签
- [ ] 图标使用一致

## 3.3 输入辅助

### 3.3.1 错误识别（Level A）

- [ ] 错误被清晰标识
- [ ] 错误消息描述问题
- [ ] 错误与字段关联

```html
<input aria-describedby="email-error" aria-invalid="true" />
<span id="email-error" role="alert">Please enter valid email</span>
```

### 3.3.2 标签或说明（Level A）

- [ ] 所有输入有可见标签
- [ ] 标明必填字段
- [ ] 提供格式提示

### 3.3.3 错误建议（Level AA）

- [ ] 错误附带修正建议
- [ ] 建议具体

### 3.3.4 错误预防（Level AA）

- [ ] 法律/财务类表单可撤销
- [ ] 提交前检查数据
- [ ] 用户提交前可复查

````

### Robust (Principle 4)

```markdown
## 4.1 Compatible

### 4.1.1 Parsing (Level A) - Obsolete in WCAG 2.2
- [ ] Valid HTML (good practice)
- [ ] No duplicate IDs
- [ ] Complete start/end tags

### 4.1.2 Name, Role, Value (Level A)
- [ ] Custom widgets have accessible names
- [ ] ARIA roles correct
- [ ] State changes announced

```html
<!-- Accessible custom checkbox -->
<div role="checkbox"
     aria-checked="false"
     tabindex="0"
     aria-labelledby="label">
</div>
<span id="label">Accept terms</span>
````

### 4.1.3 状态消息（Level AA）

- [ ] 状态更新有播报
- [ ] 正确使用 live region

```html
<div role="status" aria-live="polite">3 items added to cart</div>

<div role="alert" aria-live="assertive">Error: Form submission failed</div>
```

````

## Automated Testing

```javascript
// axe-core integration
const axe = require('axe-core');

async function runAccessibilityAudit(page) {
  await page.addScriptTag({ path: require.resolve('axe-core') });

  const results = await page.evaluate(async () => {
    return await axe.run(document, {
      runOnly: {
        type: 'tag',
        values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']
      }
    });
  });

  return {
    violations: results.violations,
    passes: results.passes,
    incomplete: results.incomplete
  };
}

// Playwright test example
test('should have no accessibility violations', async ({ page }) => {
  await page.goto('/');
  const results = await runAccessibilityAudit(page);

  expect(results.violations).toHaveLength(0);
});
````

```bash
# CLI tools
npx @axe-core/cli https://example.com
npx pa11y https://example.com
lighthouse https://example.com --only-categories=accessibility
```

## 修复模式

### 修复：缺少表单标签

```html
<!-- Before -->
<input type="email" placeholder="Email" />

<!-- After: Option 1 - Visible label -->
<label for="email">Email address</label>
<input id="email" type="email" />

<!-- After: Option 2 - aria-label -->
<input type="email" aria-label="Email address" />

<!-- After: Option 3 - aria-labelledby -->
<span id="email-label">Email</span>
<input type="email" aria-labelledby="email-label" />
```

### 修复：颜色对比度不足

```css
/* Before: 2.5:1 contrast */
.text {
  color: #767676;
}

/* After: 4.5:1 contrast */
.text {
  color: #595959;
}

/* Or add background */
.text {
  color: #767676;
  background: #000;
}
```

### 修复：键盘导航

```javascript
// Make custom element keyboard accessible
class AccessibleDropdown extends HTMLElement {
  connectedCallback() {
    this.setAttribute("tabindex", "0");
    this.setAttribute("role", "combobox");
    this.setAttribute("aria-expanded", "false");

    this.addEventListener("keydown", (e) => {
      switch (e.key) {
        case "Enter":
        case " ":
          this.toggle();
          e.preventDefault();
          break;
        case "Escape":
          this.close();
          break;
        case "ArrowDown":
          this.focusNext();
          e.preventDefault();
          break;
        case "ArrowUp":
          this.focusPrevious();
          e.preventDefault();
          break;
      }
    });
  }
}
```
