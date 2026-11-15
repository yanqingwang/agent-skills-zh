> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/harden.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

只对完美数据有效的设计算不上生产就绪。要让界面经得起真实用户抛来的各种输入、错误、语言和网络状况。

## 评估加固需求

找出薄弱点和边界情况：

1. **用极端输入测试**：
   - 超长文本（姓名、描述、标题）
   - 超短文本（空、单个字符）
   - 特殊字符（emoji、RTL 文本、带变音符的字符）
   - 大数字（百万、十亿）
   - 大量条目（1000+ 个列表项、50+ 个选项）
   - 无数据（空状态）

2. **测试错误场景**：
   - 网络故障（离线、慢速、超时）
   - API 错误（400、401、403、404、500）
   - 校验错误
   - 权限错误
   - 限流
   - 并发操作

3. **测试国际化**：
   - 翻译文本变长（德语通常比英语长 30%）
   - RTL 语言（阿拉伯语、希伯来语）
   - 字符集（中文、日文、韩文、emoji）
   - 日期/时间格式
   - 数字格式（1,000 vs 1.000）
   - 货币符号

只对完美数据有效的设计算不上生产就绪。

## 加固维度

系统地提升健壮性：

### 文本溢出与换行

**长文本处理**：
```css
/* Single line with ellipsis */
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Multi-line with clamp */
.line-clamp {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Allow wrapping */
.wrap {
  word-wrap: break-word;
  overflow-wrap: break-word;
  hyphens: auto;
}
```

**Flex/Grid 溢出**：
```css
/* Prevent flex items from overflowing */
.flex-item {
  min-width: 0; /* Allow shrinking below content size */
  overflow: hidden;
}

/* Prevent grid items from overflowing */
.grid-item {
  min-width: 0;
  min-height: 0;
}
```

**响应式文字尺寸**：
- 使用 `clamp()` 做流式排版
- 设定最小可读字号（移动端正文 16px，与排版指导设定的下限一致；14px 只留给真正的次要文本。iOS Safari 会对字号低于 16px 的聚焦输入框强制缩放，破坏表单布局）
- 测试文字缩放（放大到 200%）
- 确保容器随文本扩展

### 国际化（i18n）

**文本膨胀**：
- 为翻译预留 30-40% 的空间预算
- 使用能适应内容的 flexbox/grid
- 用最长的语言测试（通常是德语）
- 避免给文本容器设置固定宽度

```jsx
// ❌ Bad: Assumes short English text
<button className="w-24">Submit</button>

// ✅ Good: Adapts to content
<button className="px-4 py-2">Submit</button>
```

**RTL（从右到左）支持**：
```css
/* Use logical properties */
margin-inline-start: 1rem; /* Not margin-left */
padding-inline: 1rem; /* Not padding-left/right */
border-inline-end: 1px solid; /* Not border-right */

/* Or use dir attribute */
[dir="rtl"] .arrow { transform: scaleX(-1); }
```

**阿拉伯文字的特别处理**（阿拉伯语、波斯语、乌尔都语、普什图语、库尔德语）：
- 保留零宽不连字（Zero-Width Non-Joiner, U+200C）。波斯语和库尔德语在复合词各部分之间用 ZWNJ 阻断连写、同时让词保持为一个整体。过滤器或消毒器把它剥掉会改变语义。绝不要把它归一化掉。
- 处理 Yeh 和 Kaf 变体。波斯语用 ی（U+06CC）和 ک（U+06A9），阿拉伯语用 ي（U+064A）和 ك（U+0643）。存储时保留原始形态。在搜索与校验场景把对应字母视为等价，使阿拉伯键盘输入能匹配波斯语文本。拒绝其中一种变体，就会把用另一种键盘的用户挡在门外。
- 支持随 locale 变化的数字。波斯语（`fa-IR`）和阿拉伯语 locale 使用东阿拉伯-印度数字（۰-۹ 和 ٠-٩）。使用带正确 locale 的 `Intl.NumberFormat`，不要硬编码西方数字。

```javascript
// ✅ Locale-aware digit formatting
new Intl.NumberFormat('fa-IR').format(1234); // ۱٬۲۳۴
new Intl.NumberFormat('ar-SA').format(1234); // ١٬٢٣٤
```

- 尊重历法体系。波斯用户期望 Solar Hijri（Jalali）历；许多阿拉伯语用户期望 Hijri（伊斯兰）历。使用带恰当 locale 或 calendar 参数的 `Intl.DateTimeFormat`。

```javascript
// ✅ Locale-appropriate calendar
new Intl.DateTimeFormat('fa-IR').format(new Date());
new Intl.DateTimeFormat('ar-SA-u-ca-islamic').format(new Date());
```

**字符集支持**：
- 各处都使用 UTF-8 编码
- 用中日韩（CJK）字符测试
- 用 emoji 测试（它们可能占 2-4 字节）
- 处理不同文字系统（拉丁、西里尔、阿拉伯等）

**日期/时间格式化**：
```javascript
// ✅ Use Intl API for proper formatting
new Intl.DateTimeFormat('en-US').format(date); // 1/15/2024
new Intl.DateTimeFormat('de-DE').format(date); // 15.1.2024

new Intl.NumberFormat('en-US', { 
  style: 'currency', 
  currency: 'USD' 
}).format(1234.56); // $1,234.56
```

**复数形式**：
```javascript
// ❌ Bad: Assumes English pluralization
`${count} item${count !== 1 ? 's' : ''}`

// ✅ Good: Use proper i18n library
t('items', { count }) // Handles complex plural rules
```

### 错误处理

**网络错误**：
- 显示清晰的错误信息
- 提供重试按钮
- 解释发生了什么
- 提供离线模式（如适用）
- 处理超时场景

```jsx
// Error states with recovery
{error && (
  <ErrorMessage>
    <p>Failed to load data. {error.message}</p>
    <button onClick={retry}>Try again</button>
  </ErrorMessage>
)}
```

**表单校验错误**：
- 在字段旁内联显示错误
- 消息清晰、具体
- 建议修正方式
- 不要不必要地阻止提交
- 出错时保留用户已输入的内容

**API 错误**：
- 按状态码分别处理
  - 400：显示校验错误
  - 401：重定向到登录
  - 403：显示权限错误
  - 404：显示未找到状态
  - 429：显示限流提示
  - 500：显示通用错误，并提供支持渠道

**优雅降级**：
- 核心功能在没有 JavaScript 时也能工作
- 图片带有 alt 文本
- 渐进增强
- 为不支持的功能准备回退方案

### 边界情况与边界条件

**空状态**：
- 列表没有条目
- 没有搜索结果
- 没有通知
- 没有数据可展示
- 提供明确的下一步操作

**加载状态**：
- 首次加载
- 分页加载
- 刷新
- 显示正在加载的内容（"Loading your projects..."）
- 为长时间操作给出时间预估

**大数据集**：
- 分页或虚拟滚动
- 搜索/筛选能力
- 性能优化
- 不要一次加载全部 10,000 条

**并发操作**：
- 防止重复提交（加载期间禁用按钮）
- 处理竞态条件
- 乐观更新并支持回滚
- 冲突解决

**被打断的手势**（自定义滑块、拖拽表面、可滚动控制条）：
- 第二根手指或第二个指针在拖拽中途落下：第一次拖拽保住自己的指针或干净地结束，绝不跳到新的指针上
- 浏览器取消手势转而滚动（`pointercancel`）、捕获丢失（`lostpointercapture`）、指针在控件外释放，或拖拽中途窗口失焦（`blur`）：清除拖拽状态并释放捕获
- 以上每种情况之后，下一次点按或拖拽无需刷新即可正常工作

**权限状态**：
- 没有查看权限
- 没有编辑权限
- 只读模式
- 清楚解释原因

**浏览器兼容性**：
- 为现代特性提供 polyfill
- 为不支持的 CSS 提供回退
- 使用特性检测（而不是浏览器检测）
- 在目标浏览器中测试

### 输入校验与消毒

**客户端校验**：
- 必填字段
- 格式校验（邮箱、电话、URL）
- 长度限制
- 模式匹配
- 自定义校验规则

**服务端校验**（永远要做）：
- 绝不只依赖客户端
- 校验并消毒所有输入
- 防范注入攻击
- 限流

**约束处理**：
```html
<!-- Set clear constraints -->
<input 
  type="text"
  maxlength="100"
  pattern="[A-Za-z0-9]+"
  required
  aria-describedby="username-hint"
/>
<small id="username-hint">
  Letters and numbers only, up to 100 characters
</small>
```

### 无障碍韧性

**键盘导航**：
- 所有功能都能通过键盘使用
- 符合逻辑的 Tab 顺序
- 模态框中的焦点管理
- 为长内容提供跳转链接（skip links）

**屏幕阅读器支持**：
- 恰当的 ARIA 标签
- 播报动态变化（live regions）
- 有描述性的 alt 文本
- 语义化 HTML

**高对比模式**：
- 在 Windows 高对比模式下测试
- 不要只依赖颜色
- 提供替代性的视觉线索

### 性能韧性

**慢速连接**：
- 渐进式图片加载
- 骨架屏
- 乐观 UI 更新
- 离线支持（service worker）

**内存泄漏**：
- 清理事件监听器
- 取消订阅
- 清除定时器/interval
- 组件卸载时中止进行中的请求

**节流与防抖**：
```javascript
// Debounce search input
const debouncedSearch = debounce(handleSearch, 300);

// Throttle scroll handler
const throttledScroll = throttle(handleScroll, 100);
```

## 测试策略

**手动测试**：
- 用极端数据测试（超长、超短、空）
- 用不同语言测试
- 离线测试
- 慢速连接测试（限速到 3G）
- 用屏幕阅读器测试
- 只用键盘导航测试
- 在旧浏览器上测试

**自动化测试**：
- 边界情况的单元测试
- 错误场景的集成测试
- 关键路径的 E2E 测试
- 每个已确认的手势修复配一个行为回归测试（当项目的测试运行器能驱动输入时）
- 视觉回归测试
- 无障碍测试（axe、WAVE）

**避免**：
- 假设输入是完美的（一切都要校验）
- 无视国际化（面向全球设计）
- 错误信息太笼统（"Error occurred"）
- 忘记离线场景
- 只信客户端校验
- 给文本用固定宽度
- 假设文本只有英语的长度
- 一个组件出错就阻塞整个界面

## 验证加固效果

用边界情况彻底测试：

- **长文本**：试 100+ 字符的名字
- **emoji**：在所有文本字段里用 emoji
- **RTL**：用阿拉伯语或希伯来语测试
- **CJK**：用中文/日文/韩文测试
- **网络问题**：断网、给连接限速
- **大数据集**：用 1000+ 条目测试
- **并发操作**：快速连点提交 10 次
- **被打断的手势**：拖拽中途加第二根手指、横跨控件滚动、在控件外释放、拖拽中切窗口；然后再次拖拽
- **错误**：强制 API 出错，测试所有错误状态
- **空数据**：清空所有数据，测试空状态

对手势，说明证据来自哪里（模拟视口、合成触摸、哪个引擎、物理设备），并指出哪些还没有测到。

边界情况都覆盖之后，交给 `/impeccable polish` 做最后一遍打磨。
