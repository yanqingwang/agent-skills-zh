> **中文汉化版** · 上游：[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) · 原文件：`skills/2slides-ppt-generator/references/mcp-integration.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# MCP 集成指南

审阅更新 2026-10-23：下文 API/定价示例为历史快照；产生计费的调用前，请核对最新[API](https://2slides.com/api.md)与[定价](https://2slides.com/pricing)。订阅积分与购买套餐积分的过期规则不同。未做过实际生成测试。

2slides 提供 MCP（Model Context Protocol）服务器，可与 Claude Desktop 及其他兼容 MCP 的 AI Agent 无缝集成。

## MCP 服务器是什么？

2slides MCP 服务器暴露的功能与直接调用 API 相同，但通过标准化的工具接口供 Claude 直接使用，无需执行脚本。

**可用工具：**
1. `slides_generate` - 从内容生成幻灯片
2. `slides_create_like_this` - 从参考图生成幻灯片
3. `slides_create_pdf_slides` - 生成自定义设计的幻灯片（NEW）
4. `slides_generate_narration` - 添加 AI 语音旁白（NEW）
5. `slides_download_pages_voices` - 把幻灯片和语音导出为 ZIP（NEW）
6. `themes_search` - 搜索可用主题
7. `jobs_get` - 查询任务状态

**注意：** 新工具（3-5）可能需要把 MCP 服务器更新到最新版本。

## 安装与配置

2slides MCP 服务器支持两种集成模式：

### 模式 1：Streamable HTTP 协议

查询串里的 API key 可能经由日志/历史记录泄露。如果服务支持客户端侧的 secret/请求头机制，优先用它；只有查询串鉴权可用时，把整个 URL 当作凭据对待，不要放进共享配置、截图和日志。各客户端原生的配置语法不一，下面的 JSON 是上游示意，未在每个 Claude Desktop 版本上验证过。

使用 HTTP 端点的最简配置。无需本地安装。

**第 1 步：** 从 https://2slides.com/api 获取你的 API key

**第 2 步：** 配置 Claude Desktop

编辑：`~/Library/Application Support/Claude/claude_desktop_config.json`（macOS）

```json
{
  "mcpServers": {
    "2slides": {
      "url": "https://2slides.com/api/mcp?apikey=YOUR_2SLIDES_API_KEY"
    }
  }
}
```

**第 3 步：** 完全重启 Claude Desktop

**优点：**
- ✅ 不需要 Node.js 或 npm
- ✅ 始终使用最新版本
- ✅ 配置更快
- ✅ 无本地依赖

---

### 模式 2：NPM 包（stdio）

使用本地 npm 包运行 MCP 服务器。

**第 1 步：** 从 https://2slides.com/api 获取你的 API key

**第 2 步：** 配置 Claude Desktop

编辑：`~/Library/Application Support/Claude/claude_desktop_config.json`（macOS）

```json
{
  "mcpServers": {
    "2slides": {
      "command": "npx",
      "args": ["2slides-mcp@<reviewed-exact-version>"],
      "env": {
        "API_KEY": "YOUR_2SLIDES_API_KEY"
      }
    }
  }
}
```

**第 3 步：** 完全重启 Claude Desktop

**要求：**
- 已安装 Node.js 和 npm
- 首次下载包需要联网

---

### 验证安装

重启后，2slides 工具应该可用。可以这样测试：
"用 2slides 搜索 business 主题"

## 何时用 MCP，何时用直接 API

### 以下情况用 MCP 服务器：
- 在 Claude Desktop 或其他兼容 MCP 的环境中工作
- 想要无需管理脚本的无缝工具集成
- 希望由 Claude 直接处理 API 调用
- 需要实时交互与反馈

### 以下情况用直接 API 脚本：
- 在 Claude Code CLI 中工作
- MCP 服务器未配置或不可用
- 需要对参数和错误处理有更多控制
- 要集成进自定义工作流或自动化
- 需要批量处理多个请求

## MCP 工具详情

### slides_generate

从用户内容生成幻灯片。

**参数：**
- `userInput`（string，必填）：要转换的内容
- `themeId`（string，必填）：themes_search 返回的主题 ID
- `responseLanguage`（string，可选，默认 "Auto"）：语言名称
- `mode`（string，可选，默认 "sync"）："sync" 或 "async"

**示例：**
```
First search for a theme:
Use themes_search with:
- query: "business"

Then generate with the theme ID:
Use slides_generate with:
- userInput: "Introduction to Python: Variables, Functions, Classes"
- themeId: "theme_abc123"
- mode: "sync"
```

### slides_create_like_this

生成与参考图风格一致的幻灯片。

**参数：**
- `userInput`（string，必填）：幻灯片内容
- `referenceImageUrl`（string，必填）：参考图的 URL 或 base64
- `responseLanguage`（string，可选，默认 "Auto"）：语言名称
- `aspectRatio`（string，可选，默认 "16:9"）：width:height 格式
- `resolution`（string，可选，默认 "2K"）："1K"、"2K" 或 "4K"
- `page`（number，可选，默认 1）：页数（0 为自动检测，最大 100）
- `contentDetail`（string，可选，默认 "concise"）："concise" 或 "standard"

**示例：**
```
Use slides_create_like_this with:
- userInput: "Sales Report Q4 2025"
- referenceImageUrl: "https://example.com/template.jpg"
- resolution: "2K"
- page: 0  # Auto-detect slide count
- contentDetail: "standard"
```

### themes_search

搜索可用主题。

**参数：**
- `query`（string，必填）：搜索关键词
- `limit`（number，可选，默认 20，最大 100）：结果数上限

**示例：**
```
Use themes_search with:
- query: "business"
- limit: 10
```

**注意：** query 参数必填。用 "business"、"professional"、"creative"、"education"、"modern" 之类的关键词搜索合适的主题。

### slides_create_pdf_slides

无需参考图，从文本生成自定义设计的幻灯片。

**参数：**
- `userInput`（string，必填）：幻灯片内容
- `responseLanguage`（string，可选，默认 "Auto"）：语言名称
- `aspectRatio`（string，可选，默认 "16:9"）：width:height 格式
- `resolution`（string，可选，默认 "2K"）："1K"、"2K" 或 "4K"
- `page`（number，可选，默认 1）：页数（0 为自动检测，最大 100）
- `contentDetail`（string，可选，默认 "concise"）："concise" 或 "standard"
- `designStyle`（string，可选）：设计规格

**示例：**
```
Use slides_create_pdf_slides with:
- userInput: "Sales Report Q4 2025"
- designSpec: "modern minimalist, blue color scheme"
- resolution: "2K"
- page: 0  # Auto-detect slide count
```

### slides_generate_narration

为已完成的幻灯片添加 AI 语音旁白。

**参数：**
- `jobId`（string，必填）：幻灯片生成任务的 Job ID（UUID 格式）
- `language`（string，可选，默认 "Auto"）：旁白语言
- `voice`（string，可选，默认 "Puck"）：音色名（共 30 种可选）
- `multiSpeaker`（boolean，可选，默认 false）：启用多说话人模式

**可用音色：**
Puck, Aoede, Charon, Kore, Fenrir, Zephyr, Leda, Orus, Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, Sulafat

**示例：**
```
Use slides_generate_narration with:
- jobId: "abc-123-def-456"
- voice: "Aoede"
- multiSpeaker: true
- language: "English"
```

**注意：** 添加旁白前任务必须已完成。费用：每页 210 积分。

### slides_download_pages_voices

把幻灯片下载为 PNG 图片、语音文件下载为 WAV，打包成 ZIP。

**参数：**
- `jobId`（string，必填）：幻灯片生成任务的 Job ID

**示例：**
```
Use slides_download_pages_voices with:
- jobId: "abc-123-def-456"
```

**注意：** 完全免费（不消耗积分）。下载 URL 1 小时内有效。

### jobs_get

查询异步任务状态。

**参数：**
- `jobId`（string，必填）：异步生成任务的 Job ID

**响应包含：**
- 幻灯片生成状态
- 旁白状态（如适用）
- 下载 URL（完成后）

**示例：**
```
Use jobs_get with:
- jobId: "abc123..."
```

## 故障排查

### 工具不出现

1. 确认配置文件语法是合法 JSON
2. HTTP 模式：检查 API key 在 URL 中填写正确
3. npm 模式：确认 API key 在 `env` 段设置正确
4. 完全重启 Claude Desktop（彻底退出，不是只关窗口）
5. 查看 Claude Desktop 控制台中的错误信息

### API Key 问题

- 到 https://2slides.com/api 确认 API key 处于启用状态
- 检查配置里有没有拼写错误
- 确认 key 前后没有多余的引号或空格
- HTTP 模式：API key 必须放在 URL 查询参数中

### HTTP 模式问题

- 核对 URL 格式：`https://2slides.com/api/mcp?apikey=YOUR_KEY`
- 检查网络连通性
- 确认 API key 不含需要 URL 编码的特殊字符

### NPM 模式问题

- 确认 `npx` 可用（需要 Node.js）
- 手动运行 `npx 2slides-mcp` 看是否报错
- 确认下载包时网络可用
- 检查 Node.js 版本兼容性

## GitHub 仓库

更多信息见：https://github.com/2slides/mcp-2slides
