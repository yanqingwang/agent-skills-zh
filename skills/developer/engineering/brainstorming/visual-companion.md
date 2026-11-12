> **中文汉化版** · 上游：[obra/superpowers](https://github.com/obra/superpowers) · 原文件：`skills/brainstorming/visual-companion.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 视觉伴侣指南

基于浏览器的可视化头脑风暴伴侣，用于展示原型样稿、图表和选项。

## 何时使用

逐个问题决定，不是逐个会话决定。检验标准：**用户看到它，是否比读到它理解得更好？**

**用浏览器**，当内容本身是可视化的：

- **UI 原型样稿**：线框图、布局、导航结构、组件设计
- **架构图**：系统组件、数据流、关系图
- **并排可视化对比**：比较两种布局、两种配色、两个设计方向
- **设计打磨**：当问题关于观感、间距、视觉层级
- **空间关系**：以图呈现的状态机、流程图、实体关系

**用终端**，当内容是文本或表格时：

- **需求与范围问题**："X 是什么意思？"、"哪些功能在范围内？"
- **概念性 A/B/C 选择**：在用文字描述的方案之间挑选
- **取舍清单**：优缺点、对比表
- **技术决策**：API 设计、数据建模、架构方案选择
- **澄清问题**：一切答案用文字、而非视觉偏好就能给出的问题

*关于* UI 话题的问题，并不自动就是可视化问题。"你想要什么样的向导？"是概念性的，用终端。"这几种向导布局哪个感觉对？"是可视化的，用浏览器。

## 工作原理

服务器监视一个目录中的 HTML 文件，并把最新的一个送到浏览器。你把 HTML 内容写入 `screen_dir`，用户在浏览器里看到它，可以点击选择选项。选择会记录到 `state_dir/events`，你在下一轮读取。

**内容片段 vs 完整文档：** 如果你的 HTML 文件以 `<!DOCTYPE` 或 `<html` 开头，服务器原样提供它（只注入辅助脚本）。否则，服务器会自动把你的内容包进框架模板，加上页头、CSS 主题、连接状态和全部交互基础设施。**默认写内容片段。** 只在需要完全控制页面时才写完整文档。

## 启动会话

```bash
# Start AFTER the user approves the companion. --open auto-opens their browser on
# the first screen; --project-dir persists mockups and enables same-port restart.
bash scripts/start-server.sh --project-dir /path/to/project --open

# Returns: {"type":"server-started","port":52341,
#           "url":"http://localhost:52341/?key=ab12…",
#           "screen_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/content",
#           "state_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/state"}
```

保存响应里的 `screen_dir` 和 `state_dir`。使用 `--open` 时，浏览器会在你推送第一屏时自动打开，你不需要请用户打开，但仍要把 URL 分享出来作为兜底（无头/远程环境不会自动打开）。

**URL 中包含会话密钥（`?key=…`）。** 服务器会拒绝任何不带它的请求，所以要把 `url` 字段里的**完整** URL 交给用户：绝不删掉查询字符串，也绝不给出裸的 `http://host:port`。这个密钥把守 HTTP 与 WebSocket 访问，让多余的浏览器标签页或网络上的其他机器无法读取画面或注入事件。首次加载后浏览器会用 cookie 记住密钥，刷新和 `/files/*` 资源无需重复携带。

**查找连接信息：** 服务器把启动 JSON 写入 `$STATE_DIR/server-info`。如果你在后台启动了服务器、没捕获 stdout，就读这个文件拿 URL 和端口。使用 `--project-dir` 时，到 `<project>/.superpowers/brainstorm/` 里找会话目录。

**注意：** 把项目根目录作为 `--project-dir` 传入，原型样稿就会持久保存在 `.superpowers/brainstorm/`，服务器重启后仍在。不传的话，文件会进 `/tmp` 并被清理。如果 `.gitignore` 里还没有 `.superpowers/`，提醒用户加上。

**按平台启动服务器：**

**Claude Code:**
```bash
# Default mode works — the script backgrounds the server itself.
bash scripts/start-server.sh --project-dir /path/to/project --open
```

在 Windows 上，脚本会自动检测并切换到前台模式（这会阻塞工具调用）。在 Bash 工具调用上使用 `run_in_background: true`，让服务器跨对话轮次存活，然后在下一轮读 `$STATE_DIR/server-info` 拿 URL 和端口。

**Codex:**
```bash
# Codex reaps background processes. The script auto-detects CODEX_CI and
# switches to foreground mode. Run it normally — no extra flags needed.
bash scripts/start-server.sh --project-dir /path/to/project --open
```

**Gemini CLI:**
```bash
# Use --foreground and set is_background: true on your shell tool call
# so the process survives across turns
bash scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**Copilot CLI:**
```bash
# Start it with Copilot CLI's non-blocking/background shell mechanism so the
# server survives across turns. Keep --foreground so the harness, not the
# script, owns backgrounding. The launcher is a .sh, so invoke it via bash
# (on Windows, call Git Bash's bash.exe from the PowerShell tool).
bash scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**其他环境：** 服务器必须在后台跨对话轮次持续运行。如果你的环境会回收脱离的进程，就用 `--foreground`，并用你平台的后台执行机制来启动命令。

如果你的浏览器访问不到该 URL（远程/容器化环境常见），绑定一个非回环主机：

```bash
bash scripts/start-server.sh \
  --project-dir /path/to/project \
  --host 0.0.0.0 \
  --url-host localhost
```

用 `--url-host` 控制返回的 URL JSON 里打印什么主机名。

## 循环

1. **确认服务器存活**，然后**把 HTML 写到** `screen_dir` 里的一个新文件：
   - **必须：在引用 URL 或推送画面之前，先确认服务器存活。** 检查 `$STATE_DIR/server-info` 存在、`$STATE_DIR/server-stopped` 不存在。如果已关闭，用 `start-server.sh` 以**相同的 `--project-dir`** 重启：端口不变，用户已打开的标签页会自行重连（服务器下线期间显示 "paused" 覆盖层），你无需发送新 URL。服务器空闲 4 小时后自动退出（可用 `--idle-timeout-minutes` 配置）。
   - 用语义化文件名：`platform.html`、`visual-style.html`、`layout.html`
   - **绝不复用文件名**，每一屏都要用新文件
   - 用你的文件创建工具，**绝不用 cat/heredoc**（会往终端倾倒噪音）
   - 服务器自动提供最新的文件

2. **告诉用户会看到什么，然后结束你的回合：**
   - 提醒他们 URL（每一步都提，不只是第一步）
   - 简述屏幕上有什么（例如："正在展示首页的 3 种布局选项"）
   - 请他们在终端回复："看一看，告诉我你的想法。愿意的话可以点击选一个选项。"

3. **在你的下一轮**（用户已在终端回复后）：
   - 如果 `$STATE_DIR/events` 存在就读它：里面以 JSON 行记录了用户的浏览器交互（点击、选择）
   - 与用户的终端文字合并，得到完整图景
   - 终端消息是主要反馈；`state_dir/events` 提供结构化的交互数据

4. **迭代或推进**：如果反馈需要改当前屏，就写一个新文件（如 `layout-v2.html`）。当前这一步得到确认后，才进入下一个问题。

5. **回到终端时撤下画面**：当下一步不需要浏览器（如澄清问题、取舍讨论），推送一个等待屏来清掉过期内容：

   ```html
   <!-- filename: waiting.html (or waiting-2.html, etc.) -->
   <div style="display:flex;align-items:center;justify-content:center;min-height:60vh">
     <p class="subtitle">Continuing in terminal...</p>
   </div>
   ```

   这样用户就不会在对话已经前进时，还盯着一个已经解决的问题。下一个可视化问题出现时，照常推送新的内容文件。

6. 重复直到完成。

## 编写内容片段

只写放进页面内部的内容。服务器会自动把它包进框架模板（页头、主题 CSS、连接状态，以及全部交互基础设施）。

**最小示例：**

```html
<h2>Which layout works better?</h2>
<p class="subtitle">Consider readability and visual hierarchy</p>

<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>Single Column</h3>
      <p>Clean, focused reading experience</p>
    </div>
  </div>
  <div class="option" data-choice="b" onclick="toggleSelect(this)">
    <div class="letter">B</div>
    <div class="content">
      <h3>Two Column</h3>
      <p>Sidebar navigation with main content</p>
    </div>
  </div>
</div>
```

就这么简单。不需要 `<html>`、CSS 或 `<script>` 标签，服务器全都提供了。

## 可用的 CSS 类

框架模板为你的内容提供这些 CSS 类：

### 选项（A/B/C 选择）

```html
<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>Title</h3>
      <p>Description</p>
    </div>
  </div>
</div>
```

**多选：** 在容器上添加 `data-multiselect`，让用户能选中多个选项。每次点击切换该项的选中样式。

```html
<div class="options" data-multiselect>
  <!-- same option markup — users can select/deselect multiple -->
</div>
```

### 卡片（视觉设计）

```html
<div class="cards">
  <div class="card" data-choice="design1" onclick="toggleSelect(this)">
    <div class="card-image"><!-- mockup content --></div>
    <div class="card-body">
      <h3>Name</h3>
      <p>Description</p>
    </div>
  </div>
</div>
```

### Mockup 容器

```html
<div class="mockup">
  <div class="mockup-header">Preview: Dashboard Layout</div>
  <div class="mockup-body"><!-- your mockup HTML --></div>
</div>
```

### 分栏视图（并排）

```html
<div class="split">
  <div class="mockup"><!-- left --></div>
  <div class="mockup"><!-- right --></div>
</div>
```

### 优缺点

```html
<div class="pros-cons">
  <div class="pros"><h4>Pros</h4><ul><li>Benefit</li></ul></div>
  <div class="cons"><h4>Cons</h4><ul><li>Drawback</li></ul></div>
</div>
```

### Mock 元素（线框图构件）

```html
<div class="mock-nav">Logo | Home | About | Contact</div>
<div style="display: flex;">
  <div class="mock-sidebar">Navigation</div>
  <div class="mock-content">Main content area</div>
</div>
<button class="mock-button">Action Button</button>
<input class="mock-input" placeholder="Input field">
<div class="placeholder">Placeholder area</div>
```

### 排版与区块

- `h2`：页面标题
- `h3`：区块标题
- `.subtitle`：标题下方的次要文字
- `.section`：带下边距的内容块
- `.label`：小号大写标签文字

## 浏览器事件格式

用户在浏览器里点击选项时，交互会被记录到 `$STATE_DIR/events`（每行一个 JSON 对象）。你推送新的一屏时，该文件自动清空。

```jsonl
{"type":"click","choice":"a","text":"Option A - Simple Layout","timestamp":1706000101}
{"type":"click","choice":"c","text":"Option C - Complex Grid","timestamp":1706000108}
{"type":"click","choice":"b","text":"Option B - Hybrid","timestamp":1706000115}
```

完整的事件流展示用户的探索路径：他们可能点过多个选项才定下来。最后一个 `choice` 事件通常是最终选择，但点击模式能暴露犹豫，或值得追问的偏好。

如果 `$STATE_DIR/events` 不存在，说明用户没有与浏览器交互，只用他们的终端文字。

## 设计提示

- **保真度匹配问题**：布局问题用线框图，打磨类问题才做打磨
- **每一页都写明问题**：写"哪种布局显得更专业？"，而不是只写"选一个"
- **推进前先迭代**：如果反馈需要改当前屏，就写一个新版本
- **每屏最多 2-4 个选项**
- **要紧的地方用真实内容**：摄影作品集就用真实图片（Unsplash）。占位内容会掩盖设计问题。
- **样稿保持简单**：聚焦布局与结构，不追求像素级完美

## 文件命名

- 用语义化名称：`platform.html`、`visual-style.html`、`layout.html`
- 绝不复用文件名：每一屏都必须是一个新文件
- 迭代时追加版本后缀，如 `layout-v2.html`、`layout-v3.html`
- 服务器按修改时间提供最新的文件

## 清理

```bash
bash scripts/stop-server.sh $SESSION_DIR
```

如果会话用了 `--project-dir`，样稿文件会保留在 `.superpowers/brainstorm/` 供日后参考。只有 `/tmp` 会话会在停止时删除。

## 参考

- 框架模板（CSS 参考）：`scripts/frame-template.html`
- 辅助脚本（客户端）：`scripts/helper.js`
