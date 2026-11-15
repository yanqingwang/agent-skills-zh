> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/browse/PLAN-snapshot-dropdown-interactive.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 计划：Snapshot 下拉框/自动补全交互元素检测

## 问题

`snapshot -i` 在现代 Web 应用上会漏掉下拉框/自动补全的选项。这些元素：
1. 往往是带 click handler 但没有语义化 ARIA 角色的 `<div>`/`<li>`
2. 存活在动态创建的 portal/popover（浮动容器）里
3. 不出现在 Playwright 的无障碍树（`ariaSnapshot()`）中

`-C` 标志（cursor-interactive 扫描）本是为这种情况设计的，但：
- 需要单独传标志。用 `-i` 的 agent 不会自动获得它
- 会跳过已有 ARIA 角色的元素（即使无障碍树漏掉了它们）
- 不优先扫描 dropdown 选项所在的 popover/portal 容器

## 根因

Playwright 的 `ariaSnapshot()` 基于浏览器的无障碍树构建。动态渲染的 popover（React portal、Radix Popover 等）可能不在无障碍树中，原因包括：
- 组件没有设置 ARIA 角色
- portal 渲染在带作用域的 `body` locator 子树时机之外
- DOM 变更后浏览器尚未更新无障碍树

## 变更

### 1. `-i` 标志自动启用 cursor-interactive 扫描

**文件：** `browse/src/snapshot.ts`

传入 `-i`（interactive）时，自动包含 cursor-interactive 扫描。这样 agent 请求交互元素时总能看到可点击的非 ARIA 元素。

`-C` 标志保留，作为非 interactive snapshot 的独立选项。

```
if (opts.interactive) {
  opts.cursorInteractive = true;
}
```

### 2. 增加 popover/portal 优先扫描

**文件：** `browse/src/snapshot.ts`（cursor-interactive evaluate 块内）

在通用 cursor:pointer 扫描之前，先专门扫描可见的浮动容器（popover、dropdown、menu），并把它们的全部直接子元素纳入交互元素：

浮动容器的检测启发式：
- `position: fixed` 或 `position: absolute` 且 `z-index >= 10`
- 具有 `role="listbox"`、`role="menu"`、`role="dialog"`、`role="tooltip"`、`[data-radix-popper-content-wrapper]`、`[data-floating-ui-portal]` 等属性
- 最近才出现在 DOM 中（不在初始页面加载里）
- 可见（`offsetParent !== null` 或 `position: fixed`）

对每个浮动容器，纳入满足以下条件的子元素：
- 有文本内容
- 可见
- 具备 cursor:pointer 或 onclick 或 role="option" 或 role="menuitem"
- 打上原因标签 `popover-child` 以便区分

### 3. 移除 cursor-interactive 扫描中的 `hasRole` 跳过

**文件：** `browse/src/snapshot.ts`

现状：`if (hasRole) continue;` —— 跳过任何带 ARIA 角色的元素，默认无障碍树已捕获它们。

问题：如果无障碍树漏掉了该元素（时机、portal、糟糕的 DOM 结构），它会同时逃过两套系统。

修复：仅当元素的 role 在 `INTERACTIVE_ROLES` 中且确实被主 refMap 捕获时才跳过。否则纳入。

由于在 `page.evaluate()` 内部难以检查 refMap，更简单的修复：对位于已检测浮动容器内的元素，完全移除 `hasRole` 跳过。对浮动容器外的元素，保留 `hasRole` 跳过（避免普通页面内容出现重复）。

### 4. 增加 dropdown 测试 fixture 与测试

**文件：** `browse/test/fixtures/dropdown.html`

HTML 页面包含：
- 一个 combobox 输入框，聚焦/输入时显示 dropdown
- 以 `<div>` 加 click handler 实现的 dropdown 选项（无 ARIA 角色）
- 以 `<li>` 加 `role="option"` 实现的 dropdown 选项
- 一个 React-portal 风格的容器（`position: fixed`，高 z-index）

**文件：** `browse/test/snapshot.test.ts`

新测试用例：
- dropdown 页面上的 `snapshot -i` 通过 cursor 扫描找到 dropdown 选项
- dropdown 页面上的 `snapshot -i` 包含 popover-child 元素
- dropdown 扫描产生的 `@c` ref 可点击
- 浮动容器内带 ARIA 角色的元素即使无障碍树漏掉也会被捕获

## 上线风险

**低。** `-C` 扫描是增量的：只增加 `@c` ref，从不移除 `@e` ref。随 `-i` 自动启用会增大输出，但 agent 本就处理混合 ref 类型。

**一个顾虑：** `-C` 扫描查询全部元素（`document.querySelectorAll('*')`），在重页面上可能很慢。popover 专项扫描只限于已检测浮动容器内的元素，很快（子树小）。

## 测试

```bash
cd /data/gstack/browse && bun test snapshot
```

## 变更文件

1. `browse/src/snapshot.ts` — 随 -i 自动启用 -C、popover 扫描、移除浮动容器内的 hasRole 跳过
2. `browse/test/fixtures/dropdown.html` — 新测试 fixture
3. `browse/test/snapshot.test.ts` — 新增 dropdown/popover 测试用例
