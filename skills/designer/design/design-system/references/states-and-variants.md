> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/design-system/references/states-and-variants.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 状态与变体

组件的状态定义与变体模式。

## 交互状态

### 状态定义

| 状态 | 触发方式 | 视觉变化 |
|-------|---------|---------------|
| default | 无 | 基础外观 |
| hover | 鼠标悬停 | 轻微颜色变化 |
| focus | Tab/点击 | 焦点环 |
| active | 鼠标按下 | 最深颜色 |
| disabled | disabled 属性 | 降低透明度 |
| loading | 异步操作 | 加载指示器 + 降低透明度 |

### 状态优先级

多个状态同时生效时，优先级从高到低：

1. disabled
2. loading
3. active
4. focus
5. hover
6. default

### 状态过渡

```css
/* Standard transition for interactive elements */
.interactive {
  transition-property: color, background-color, border-color, box-shadow;
  transition-duration: var(--duration-fast);
  transition-timing-function: ease-in-out;
}
```

| 过渡 | 时长 | 缓动 |
|------------|----------|--------|
| 颜色变化 | 150ms | ease-in-out |
| 背景 | 150ms | ease-in-out |
| Transform | 200ms | ease-out |
| Opacity | 150ms | ease |
| 阴影 | 200ms | ease-out |

## 焦点状态

### 焦点环规格

```css
/* Standard focus ring */
.focusable:focus-visible {
  outline: none;
  box-shadow: 0 0 0 var(--ring-offset) var(--color-background),
              0 0 0 calc(var(--ring-offset) + var(--ring-width)) var(--ring-color);
}
```

| 属性 | 值 |
|----------|-------|
| 焦点环宽度 | 2px |
| 焦点环偏移 | 2px |
| 焦点环颜色 | primary（blue-500） |
| 偏移层颜色 | background |

### 容器内焦点

```css
/* Container focus when child is focused */
.container:focus-within {
  border-color: var(--color-ring);
}
```

## 禁用状态

### 视觉处理

```css
.disabled {
  opacity: var(--opacity-disabled); /* 0.5 */
  pointer-events: none;
  cursor: not-allowed;
}
```

| 属性 | 禁用值 |
|----------|----------------|
| Opacity | 50% |
| 指针事件 | none |
| 光标 | not-allowed |
| 背景 | muted |
| 颜色 | muted-foreground |

### 可访问性

- 用 `aria-disabled="true"` 表达语义上的禁用
- 表单元素用 `disabled` 属性
- 保持足够对比度（至少 3:1）

## 加载状态

### 加载指示器位置

| 组件 | 指示器位置 |
|-----------|------------------|
| 按钮 | 替换图标或居中 |
| 输入框 | 尾部位置 |
| 卡片 | 居中覆盖 |
| 页面 | 视口中心 |

### 加载处理

```css
.loading {
  position: relative;
  pointer-events: none;
}

.loading::after {
  content: '';
  /* spinner styles */
}

.loading > * {
  opacity: 0.7;
}
```

## 错误状态

### 视觉指示

```css
.error {
  border-color: var(--color-error);
  color: var(--color-error);
}

.error:focus-visible {
  box-shadow: 0 0 0 2px var(--color-background),
              0 0 0 4px var(--color-error);
}
```

| 元素 | 错误处理 |
|---------|-----------------|
| 输入框边框 | red-500 |
| 输入框焦点环 | red/20% |
| 辅助文字 | red-600 |
| 图标 | red-500 |

### 错误消息

- 位于输入框下方
- 使用错误色
- 附带图标以利无障碍
- 输入合法后清除

## 变体模式

### 颜色变体

```css
/* Pattern for color variants */
.component {
  --component-bg: var(--color-primary);
  --component-fg: var(--color-primary-foreground);
  background: var(--component-bg);
  color: var(--component-fg);
}

.component.secondary {
  --component-bg: var(--color-secondary);
  --component-fg: var(--color-secondary-foreground);
}

.component.destructive {
  --component-bg: var(--color-destructive);
  --component-fg: var(--color-destructive-foreground);
}
```

### 尺寸变体

```css
/* Pattern for size variants */
.component {
  --component-height: 40px;
  --component-padding: var(--space-4);
  --component-font: var(--font-size-sm);
}

.component.sm {
  --component-height: 32px;
  --component-padding: var(--space-3);
  --component-font: var(--font-size-xs);
}

.component.lg {
  --component-height: 48px;
  --component-padding: var(--space-6);
  --component-font: var(--font-size-base);
}
```

## 无障碍要求

### 颜色对比

| 元素 | 最低对比度 |
|---------|---------------|
| 普通文本 | 4.5:1 |
| 大号文本（18px 以上） | 3:1 |
| UI 组件 | 3:1 |
| 焦点指示 | 3:1 |

### 状态指示

- 绝不只靠颜色
- 辅以图标、文字或图案
- 确保焦点可见
- 提供加载状态播报

### ARIA 状态

```html
<!-- Disabled -->
<button disabled aria-disabled="true">Submit</button>

<!-- Loading -->
<button aria-busy="true" aria-describedby="loading-text">
  <span id="loading-text" class="sr-only">Loading...</span>
</button>

<!-- Error -->
<input aria-invalid="true" aria-describedby="error-msg">
<span id="error-msg" role="alert">Error message</span>
```
