> **中文汉化版** · 上游：[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) · 原文件：`skills/2slides-ppt-generator/references/detailed-guide.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 2slides 演示文稿生成：详细指南

审阅更新 2026-10-23：下文 API/定价示例为历史快照；产生计费的调用前，请核对最新[API](https://2slides.com/api.md)与[定价](https://2slides.com/pricing)。订阅积分与购买套餐积分的过期规则不同。未做过实际生成测试。

> 本文件包含从 `SKILL.md` 中拆出的详细流程与参考材料，供按需加载。激活条件、示例、安全约束与限制由根 Skill 文件定义。

## 概述

使用 2slides AI API 生成专业演示文稿。本 Skill 支持基于内容的生成（主题驱动的 Fast PPT）、按参考图匹配风格、自定义 PDF 设计、文档摘要、AI 语音旁白，以及导出页面/音频。返回结果同时包含可交互的幻灯片 URL 和可下载的 PDF。

本 Skill 改编自 2slides 官方 Skill 仓库（[`2slides/slides-generation-2slides-skills`](https://github.com/2slides/slides-generation-2slides-skills)）。它调用 2slides 托管 API，需要用户自己的 API key 和积分。


## 准备条件

用户必须拥有 2slides API key 和积分：

1. **获取 API Key：** 访问 https://2slides.com/api 注册账号并创建 API key
   - 新用户获赠 **500 免费积分**（约 50 页 Fast PPT）
2. **购买积分（可选）：** 访问 https://2slides.com/pricing 购买更多积分
   - 按量付费，无需订阅
   - 积分永不过期
   - 大套餐最高优惠 20%
3. **设置 API Key：** 把 key 存入环境变量：`SLIDES_2SLIDES_API_KEY`

```bash
read -r -s SLIDES_2SLIDES_API_KEY
export SLIDES_2SLIDES_API_KEY
```

4. **安装脚本依赖：** 使用 Python 脚本之前，在本 Skill 目录下审查并解决最低版本的本地依赖要求，在隔离环境中安装（这不是 lockfile）：

```bash
python -m pip install -r requirements.txt
```

**积分消耗：**
- Fast PPT：10 积分/页
- Nano Banana 1K/2K：100 积分/页
- Nano Banana 4K：200 积分/页
- 语音旁白：210 积分/页
- 下载导出：免费

详细定价信息见 [references/pricing.md](../references/pricing.md)。


## 工作流决策树

根据用户请求选择合适的路径：

```
User Request
│
├─ "Create slides from this content/text"
│  └─> Use Content-Based Generation (Section 1)
│
├─ "Create slides like this image"
│  └─> Use Reference Image Generation (Section 2)
│
├─ "Create custom designed slides" or "Create PDF slides"
│  └─> Use Custom PDF Generation (Section 3)
│
├─ "Create slides from this document"
│  └─> Use Document Summarization (Section 4)
│
├─ "Add voice narration" or "Generate audio for slides"
│  └─> Use Voice Narration (Section 5)
│
├─ "Download slides as images" or "Export slides and voices"
│  └─> Use Download Export (Section 6)
│
└─ "Search for themes" or "What themes are available?"
   └─> Use Theme Search (Section 7)
```

---


## 1. 基于内容的生成

从用户提供的文本内容生成幻灯片。

### 适用场景
- 用户在消息里直接给出了内容
- 用户说"围绕 X 做一份演示文稿"
- 用户给出了结构化提纲或要点列表

### 工作流

**第 1 步：准备内容**

把内容组织清晰，效果最好：

```
Title: [Main Topic]

Section 1: [Subtopic]
- Key point 1
- Key point 2
- Key point 3

Section 2: [Subtopic]
- Key point 1
- Key point 2
```

**第 2 步：选择主题（必填）**

搜索合适的主题（themeId 必填）：

```bash
python scripts/search_themes.py --query "business"
python scripts/search_themes.py --query "professional"
python scripts/search_themes.py --query "creative"
```

从结果中挑一个主题 ID。

**第 3 步：生成幻灯片**

使用 `generate_slides.py` 脚本并传入主题 ID：

```bash
# Basic generation (theme ID required)
python scripts/generate_slides.py --content "Your content here" --theme-id "theme123"

# In different language
python scripts/generate_slides.py --content "Your content" --theme-id "theme123" --language "Spanish"

# Async mode for longer presentations
python scripts/generate_slides.py --content "Your content" --theme-id "theme123" --mode async
```

**第 4 步：处理结果**

**同步模式响应：**
```json
{
  "slideUrl": "https://2slides.com/slides/abc123",
  "pdfUrl": "https://2slides.com/slides/abc123/download",
  "status": "completed"
}
```

把两个 URL 都提供给用户：
- `slideUrl`：可交互的在线幻灯片
- `pdfUrl`：可下载的 PDF 版本

**异步模式响应：**
```json
{
  "jobId": "job123",
  "status": "pending"
}
```

轮询获取结果：
```bash
python scripts/get_job_status.py --job-id "job123"
```

---


## 2. 参考图生成

生成与参考图风格一致的幻灯片。

### 适用场景
- 用户给出图片 URL 并说"照这样做幻灯片"
- 用户想匹配现有的品牌/设计风格
- 用户有一张想模仿的模板图

### 工作流

**第 1 步：核验图片 URL**

确认参考图满足：
- URL 可公开访问
- 图片格式有效（PNG、JPG 等）
- 能代表想要的幻灯片风格

**第 2 步：生成幻灯片**

使用 `generate_slides.py` 脚本并带上 `--reference-image`：

```bash
python scripts/generate_slides.py \
  --content "Your presentation content" \
  --reference-image "https://example.com/template.jpg" \
  --language "Auto"
```

**可选参数（取值均来自 [2slides API](https://2slides.com/api.md)）：**
```bash
--language LANG                 # Auto, English, Spanish, Arabic, Portuguese, Indonesian,
                                 # Japanese, Russian, Hindi, French, German, Greek, Vietnamese,
                                 # Turkish, Polish, Italian, Korean, Simplified Chinese,
                                 # Traditional Chinese, Thai (default: Auto)
--mode sync|async                # default: sync for theme, async for reference-image
--aspect-ratio RATIO             # 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (default: 16:9)
--resolution 1K|2K|4K            # default: 2K
--page N                         # 0=auto, 1-100 (default: 1)
--content-detail concise|standard # default: concise
```

**注意：** 该路径使用 Nano Banana Pro 模式，积分消耗：
- 1K/2K：每页 100 积分
- 4K：每页 200 积分

**第 3 步：处理结果**

同步模式直接返回完成结果；异步模式返回一个待轮询的任务：
```json
{
  "slideUrl": "https://2slides.com/workspace?jobId=...",
  "pdfUrl": "https://...pdf...",
  "status": "completed",
  "message": "Successfully generated N slides",
  "slidePageCount": N
}
```

把两个 URL 都提供给用户：
- `slideUrl`：在 2slides 工作区查看幻灯片
- `pdfUrl`：PDF 直接下载（1 小时内有效）

**处理时长：** 每页约 30 秒（1-2 页通常 30-60 秒）

---


## 3. 自定义 PDF 生成

无需参考图，直接从文本生成自定义设计的幻灯片。

### 适用场景
- 用户想要自定义设计，但不提供参考图
- 用户要求"生成 PDF 幻灯片"
- 用户想指定设计特征
- 主题生成的替代方案，设计自由度更高

### 工作流

**第 1 步：准备内容**

把内容组织清晰：

```
Title: [Main Topic]

Section 1: [Subtopic]
- Key point 1
- Key point 2

Section 2: [Subtopic]
- Key point 1
- Key point 2
```

**第 2 步：生成幻灯片**

使用 `create_pdf_slides.py` 脚本：

```bash
# Basic generation
python scripts/create_pdf_slides.py --content "Your content here"

# With design style (API: designStyle)
python scripts/create_pdf_slides.py \
  --content "Sales Report Q4 2025" \
  --design-style "modern minimalist, blue color scheme"

# High resolution with auto page detection
python scripts/create_pdf_slides.py \
  --content "Marketing Plan" \
  --resolution 4K \
  --page 0 \
  --content-detail standard
```

**可选参数：**
```bash
--design-style "text"           # Design instructions (API: designStyle)
--language LANG                 # Same as generate_slides (default: Auto)
--aspect-ratio RATIO           # 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (default: 16:9)
--resolution 1K|2K|4K          # default: 2K
--page N                        # 0=auto, 1-100 (default: 1)
--content-detail concise|standard # default: standard
```

**第 3 步：处理结果**

返回结构与 create-like-this 相同：
```json
{
  "slideUrl": "https://2slides.com/workspace?jobId=...",
  "pdfUrl": "https://...pdf...",
  "status": "completed",
  "message": "Successfully generated N slides",
  "slidePageCount": N
}
```

**注意：**
- 积分消耗与 create-like-this 相同（1K/2K 每页 100 积分，4K 每页 200 积分）
- 处理时长：每页约 30 秒
- 自动生成 PDF
- 由 AI 根据内容和规格创建自定义设计

---


## 4. 文档摘要

从文档内容生成幻灯片。

### 适用场景
- 用户上传了文档（PDF、DOCX、TXT 等）
- 用户说"用这份文档做幻灯片"
- 用户想把长内容浓缩成演示文稿形式

### 工作流

**第 1 步：读取文档**

用合适的工具读取文档内容：
- PDF：使用 PDF 阅读工具
- DOCX：使用 DOCX 阅读工具
- TXT/MD：使用 Read 工具

**第 2 步：提取要点**

分析文档并提取：
- 主要话题与主题
- 每个章节的要点
- 重要的数据、引文或示例
- 逻辑脉络与结构

**第 3 步：组织内容**

把提取的信息整理成演示文稿结构：

```
Title: [Document Main Topic]

Introduction
- Context
- Purpose
- Overview

[Section 1 from document]
- Key point 1
- Key point 2
- Supporting detail

[Section 2 from document]
- Key point 1
- Key point 2
- Supporting detail

Conclusion
- Summary
- Key takeaways
- Next steps
```

**第 4 步：生成幻灯片**

使用基于内容的生成工作流（第 1 节）。先搜索主题，再生成：

```bash
# Search for appropriate theme
python scripts/search_themes.py --query "business"

# Generate with theme ID
python scripts/generate_slides.py --content "[Structured content from step 3]" --theme-id "theme123"
```

**提示：**
- 幻灯片保持精炼（每页 3-5 个要点）
- 聚焦关键洞见，不要全文照搬
- 用文档标题作为幻灯片标题
- 纳入重要统计数字或引文
- 询问用户是否要突出特定章节

---


## 5. 语音旁白

为幻灯片添加 AI 生成的语音旁白。

### 适用场景
- 用户想给幻灯片加音频
- 用户要求"加语音旁白"或"生成音频"
- 用户想要带口播内容的演示文稿
- 用户需要多说话人旁白

### 前提条件

**重要：** 添加旁白之前，幻灯片生成任务必须已完成。

1. 先用任意方法（第 1、2、3 或 4 节）生成幻灯片
2. 从生成结果中拿到 job ID
3. 确认任务状态为 "completed" 后再请求旁白

### 工作流

**第 1 步：选择音色**

可用 30 种音色，包括：
- Puck（默认）
- Aoede
- Charon
- Kore
- Fenrir
- Phoebe
- 以及另外 24 种……

列出全部音色：
```bash
python scripts/generate_narration.py --list-voices
```

**第 2 步：生成旁白**

使用 `generate_narration.py` 脚本并传入 job ID：

```bash
# Basic narration with default voice
python scripts/generate_narration.py --job-id "abc-123-def-456"

# Single speaker, specific voice
python scripts/generate_narration.py --job-id "abc-123-def-456" --voice Aoede

# Multi-speaker mode
python scripts/generate_narration.py --job-id "abc-123-def-456" --multi-speaker
```

**参数（与 [2slides API](https://2slides.com/api.md) 对齐）：**
- `--job-id`：任务 ID（必填，Nano Banana 为 UUID）
- `--voice`：音色名（默认 Puck）；用 `--list-voices` 查看全部 30 种
- `--language`：旁白语言（默认 Auto）
- `--multi-speaker`：启用多说话人模式
- `--list-voices`：打印支持的音色，不调用 API

**第 3 步：检查状态**

旁白生成是异步执行的：

```bash
python scripts/get_job_status.py --job-id "abc-123-def-456"
```

**第 4 步：处理结果**

完成后，任务结果会包含旁白文件。用下载端点（第 6 节）获取音频文件。

**注意：**
- **费用：** 每页 210 积分（文本 10 积分，音频 200 积分）
- 处理时长随页数变化
- 提供 30 种音色
- 支持 19 种语言并可自动检测
- 多说话人模式使用不同音色增加变化

---


## 6. 下载导出

把幻灯片下载为 PNG 图片，把语音旁白下载为 WAV 文件。

### 适用场景
- 用户想把幻灯片下载为图片
- 用户需要单独的语音文件
- 用户想要文字稿
- 用户需要图片格式的幻灯片供其他工具使用

### 工作流

**第 1 步：确认任务完成**

确认幻灯片（以及可选的旁白）已生成，任务状态为 completed。

**第 2 步：下载压缩包**

使用 `download_slides_pages_voices.py` 脚本：

```bash
# Download with default filename (<job_id>.zip)
python scripts/download_slides_pages_voices.py --job-id "abc-123-def-456"

# Download to specific path
python scripts/download_slides_pages_voices.py \
  --job-id "abc-123-def-456" \
  --output "my-presentation.zip"
```

**第 3 步：解压使用**

ZIP 压缩包内含：
- **Pages：** 每页幻灯片的 PNG 文件
- **Voices：** WAV 音频文件（如果生成了旁白）
- **Transcripts：** 旁白的文字稿

**注意：**
- **费用：** 完全免费（不消耗积分）
- 下载 URL **仅 1 小时内有效**
- 包含全部页面和语音文件
- 高质量 PNG 导出
- 音频为 WAV 格式

---


## 7. 主题搜索

为演示文稿找到合适的主题。

### 适用场景
- 在按特定风格生成幻灯片之前
- 用户问"有哪些主题可用？"
- 用户想要专业或品牌化的外观

### 工作流

**搜索主题：**

```bash
# Search for specific style (query is required)
python scripts/search_themes.py --query "business"
python scripts/search_themes.py --query "creative"
python scripts/search_themes.py --query "education"
python scripts/search_themes.py --query "professional"

# Get more results
python scripts/search_themes.py --query "modern" --limit 50
```

**主题选择：**

1. 向用户展示可用主题的名称和描述
2. 请用户选择，或让用户用默认值
3. 在生成请求中使用该主题 ID

---


## 使用 MCP 服务器

如果 Claude Desktop 中已配置 2slides MCP 服务器，就用集成的工具，不用脚本。

**两种配置模式：**

1. **Streamable HTTP 协议（推荐）**
   - 配置最简单，无需本地安装
   - 配置：`"url": "https://2slides.com/api/mcp?apikey=YOUR_API_KEY"`

2. **NPM 包（stdio）**
   - 使用本地 npm 包
   - 配置：`"command": "npx", "args": ["2slides-mcp"]`

**可用的 MCP 工具：**
- `slides_generate` - 从内容生成幻灯片
- `slides_create_like_this` - 从参考图生成
- `themes_search` - 搜索主题
- `jobs_get` - 查询任务状态

完整配置说明与详细工具文档见 [mcp-integration.md](../references/mcp-integration.md)。

**MCP 与脚本如何取舍：**
- 已配置时在 Claude Desktop 中**用 MCP**
- 在 Claude Code CLI 中或 MCP 不可用时**用脚本**

---


## 进阶特性

### 同步与异步模式

**同步模式（默认）：**
- 等待生成完成（30-60 秒）
- 直接返回结果
- 适合快速出片

**异步模式：**
- 立即返回任务 ID
- 用 `get_job_status.py` 轮询结果
- 适合大型演示文稿或批量处理
- **轮询建议：** 每 20-30 秒查一次，避免给服务器造成压力

### 速率限制

不同端点的速率限制不同：

- **Fast PPT（generate）：** 每分钟 10 次请求
- **Nano Banana（create-like-this、create-pdf-slides）：** 每分钟 6 次请求

被限流就稍等再重试，或检查套餐限额。

### 积分消耗

- **Fast PPT（generate 端点）：** 每页 10 积分
- **Nano Banana 1K/2K（create-like-this、create-pdf-slides）：** 每页 100 积分
- **Nano Banana 4K：** 每页 200 积分
- **语音旁白：** 每页 210 积分（文本 10 积分，音频 200 积分）
- **下载导出：** 免费（不消耗积分）

### 购买积分

2slides 采用按量付费的积分体系，无需订阅。

**积分套餐：**（当前促销：最高优惠 20%）
- 2,000 积分：$5.00
- 4,000 积分：$9.50（优惠 5%）
- 10,000 积分：$22.50（优惠 10%）
- 20,000 积分：$42.50（优惠 15%）
- 40,000 积分：$80.00（优惠 20%）

**新用户获赠 500 免费积分**用于上手（约 50 页 Fast PPT）。

**积分永不过期**，按自己的节奏用。

**购买积分：** https://2slides.com/pricing

### 下载 URL 有效期

所有下载 URL（PDF、ZIP 压缩包）**仅 1 小时内有效**。生成后请尽快下载文件。

### 语言支持

可生成多种语言的幻灯片（使用完整语言名称）：

```bash
--language "Auto"                # Automatic detection (default)
--language "English"             # English
--language "Simplified Chinese"  # 简体中文
--language "Traditional Chinese" # 繁體中文
--language "Spanish"             # Español
--language "French"              # Français
--language "German"              # Deutsch
--language "Japanese"            # 日本語
--language "Korean"              # 한국어
```

另外还有：Arabic, Portuguese, Indonesian, Russian, Hindi, Vietnamese, Turkish, Polish, Italian

### 错误处理

**常见错误码：**

1. **缺少 API key**
   ```
   Error: API key not found
   Solution: Set SLIDES_2SLIDES_API_KEY environment variable
   ```

2. **RATE_LIMIT_EXCEEDED**
   ```
   Error: 429 Too Many Requests
   Solution: Wait 20-30 seconds before retrying
   Rate limits: Fast PPT (10/min), Nano Banana (6/min)
   ```

3. **INSUFFICIENT_CREDITS**
   ```
   Error: Not enough credits
   Solution: Add credits at https://2slides.com/api
   ```

4. **INVALID_JOB_ID**
   ```
   Error: Job ID not found or invalid
   Solution: Verify job ID format (must be UUID for Nano Banana)
   ```

5. **内容无效**
   ```
   Error: 400 Bad Request
   Solution: Verify content format and parameters
   ```

---


## 脚本参数参考（2slides API）

这些脚本只实现了 [2slides API](https://2slides.com/api.md) 参数的一个子集。允许取值定义在 `scripts/api_constants.py` 中，并在适用的地方强制校验。

| 脚本 | 关键参数 | 允许取值（见脚本 `--help` 或 api_constants.py） |
|--------|----------------|----------------------------------------------------------|
| `generate_slides.py` | `--language` | Auto, English, Spanish, Arabic, Portuguese, Indonesian, Japanese, Russian, Hindi, French, German, Greek, Vietnamese, Turkish, Polish, Italian, Korean, Simplified Chinese, Traditional Chinese, Thai |
| | `--mode` | sync, async |
| | `--aspect-ratio` | 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 |
| | `--resolution` | 1K, 2K, 4K |
| | `--content-detail` | concise, standard |
| `create_pdf_slides.py` | 同上，另加 `--design-style` / `--design-spec`（自由文本） | |
| `generate_narration.py` | `--voice` | 30 种音色（Puck, Aoede, Charon 等）；用 `--list-voices` |
| | `--language` | Auto, English, Spanish, Arabic, Portuguese, Indonesian, Japanese, Russian, Hindi, French, German, Vietnamese, Turkish, Polish, Italian, Korean, Simplified Chinese, Traditional Chinese |
| | `--multi-speaker` | 传入即启用 |
| `search_themes.py` | `--query`（必填）、`--limit`（1–100） | |
| `get_job_status.py` | `--job-id`（必填） | |
| `download_slides_pages_voices.py` | `--job-id`（必填）、`--output`（路径） | |

---


## 其他文档

### API 参考
详见 [api-reference.md](../references/api-reference.md)：
- 全部端点与参数
- 请求/响应格式
- 鉴权细节
- 速率限制与最佳实践
- 错误码与处理方式

### 定价信息
详见 [pricing.md](../references/pricing.md)：
- 积分套餐与定价
- 费用示例与计算
- 免费试用细节
- 退款政策
- 企业方案

---


## 取得最佳效果的提示

**内容结构：**
- 用清晰的标题和子标题
- 要点保持简洁
- 每节不超过 3-5 个要点
- 纳入相关的示例或数据

**主题选择：**
- 标准生成必须提供主题 ID
- 用与演示目的匹配的关键词搜索
- 常用搜索词："business"、"professional"、"creative"、"education"、"modern"
- 每个主题都有独特的样式和布局

**参考图：**
- 用高质量图片效果最好
- 可以用 URL 或 base64 编码图片
- 公开 URL 必须可访问
- 按质量需求选择分辨率（1K/2K/4K）
- 用 page=0 自动检测页数

**文档处理：**
- 只提取关键信息
- 别试图把整份文档塞进幻灯片
- 聚焦主要洞见和结论
- 询问用户要强调哪些章节

---


## 相关 Skill

- `@youtube-full`：获取源素材（字幕稿），可用本 Skill 摘要成演示文稿。
