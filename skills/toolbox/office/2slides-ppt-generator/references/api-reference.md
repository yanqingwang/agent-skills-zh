> **中文汉化版** · 上游：[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) · 原文件：`skills/2slides-ppt-generator/references/api-reference.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 2slides API 参考

审阅更新 2026-10-23：下文 API/定价示例为历史快照；产生计费的调用前，请核对最新[API](https://2slides.com/api.md)与[定价](https://2slides.com/pricing)。订阅积分与购买套餐积分的过期规则不同。未做过实际生成测试。

2slides 幻灯片生成服务的完整 API 文档。

## 基础 URL

```
https://2slides.com/api/v1
```

## 鉴权

所有 API 请求都需要鉴权：在 Authorization 头中携带 Bearer token：

```
Authorization: Bearer YOUR_API_KEY
```

API key 获取地址：https://2slides.com/api

API key 存入环境变量：`SLIDES_2SLIDES_API_KEY`

## 端点

### 1. 生成幻灯片

从用户输入生成幻灯片，可选指定主题。

**端点：** `POST /slides/generate`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**请求体：**
```json
{
  "userInput": "string (required) - Content to convert into slides",
  "themeId": "string (required) - Theme ID from themes/search",
  "responseLanguage": "string (optional, default: 'Auto') - Language code",
  "mode": "string (optional, default: 'sync') - 'sync' or 'async'"
}
```

**支持的语言：**
Auto, English, Simplified Chinese (简体中文), Traditional Chinese (繁體中文), Spanish, Arabic, Portuguese, Indonesian, Japanese, Russian, Hindi, French, German, Vietnamese, Turkish, Polish, Italian, Korean

**响应（同步模式）：**
```json
{
  "slideUrl": "https://2slides.com/slides/...",
  "pdfUrl": "https://2slides.com/slides/.../download",
  "status": "completed"
}
```

**响应（异步模式）：**
```json
{
  "jobId": "abc123...",
  "status": "pending"
}
```

**注意：**
- **同步模式**：等待生成完成并直接返回结果（可能需要 30-60 秒）
- **异步模式**：立即返回 jobId，用 `/jobs/{jobId}` 轮询结果

---

### 2. 按图仿制（Create Like This，参考图）

生成与参考图风格一致的幻灯片（Nano Banana Pro 模式）。

**端点：** `POST /slides/create-like-this`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**请求体：**
```json
{
  "userInput": "string (required) - Content for slides",
  "referenceImageUrl": "string (required) - URL or base64 of reference image",
  "responseLanguage": "string (optional, default: 'Auto')",
  "aspectRatio": "string (optional, default: '16:9') - width:height format",
  "resolution": "string (optional, default: '2K') - '1K', '2K', or '4K'",
  "page": "number (optional, default: 1) - 0 for auto-detection, max 100",
  "contentDetail": "string (optional, default: 'concise') - 'concise' or 'standard'"
}
```

**分辨率选项：**
- **1K**：标准画质
- **2K**：高画质（默认）
- **4K**：超高画质

**内容详略选项：**
- **concise**：简短、以关键词为主的内容
- **standard**：全面、详细的内容

**page 参数：**
- 设为 `0` 启用自动页数检测
- 设为具体数字（1-100）指定确切页数

**响应：**
```json
{
  "success": true,
  "data": {
    "jobId": "608f8997-5207-480c-9ff2-d2475cba6b9d",
    "status": "success",
    "message": "Successfully generated N slides",
    "downloadUrl": "https://...pdf...",
    "jobUrl": "https://2slides.com/workspace?jobId=...",
    "createdAt": 1770108913384,
    "updatedAt": 1770108934015,
    "slidePageCount": 3,
    "successCount": 3,
    "failedCount": 0
  }
}
```

**响应字段：**
- `success`：布尔值，表示请求是否成功
- `data.jobId`：任务唯一标识
- `data.status`：生成状态（"success" 或 "failed"）
- `data.message`：人类可读的状态信息
- `data.downloadUrl`：PDF 直接下载 URL（临时的，1 小时内有效）
- `data.jobUrl`：在 2slides 工作区查看幻灯片
- `data.slidePageCount`：生成的幻灯片页数
- `data.successCount`：成功生成的页数
- `data.failedCount`：失败的页数

**注意：**
- 该端点按所选模式支持同步或异步
- 处理时长：每页约 30 秒
- 典型响应时间：1-2 页为 30-60 秒
- 自动生成 PDF
- 匹配参考图的风格与设计
- **超时建议**：把超时设为 `max(120, pages * 40)` 秒

---

### 3. 创建 PDF 幻灯片

从文本生成自定义设计的幻灯片，可选提供设计规格。

**端点：** `POST /slides/create-pdf-slides`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**请求体：**
```json
{
  "userInput": "string (required) - Content for slides",
  "responseLanguage": "string (optional, default: 'Auto')",
  "aspectRatio": "string (optional, default: '16:9') - width:height format",
  "resolution": "string (optional, default: '2K') - '1K', '2K', or '4K'",
  "page": "number (optional, default: 1) - 0 for auto-detection, max 100",
  "contentDetail": "string (optional, default: 'concise') - 'concise' or 'standard'",
  "designStyle": "string (optional) - Design specifications (e.g., 'modern minimalist')"
}
```

**响应：**
```json
{
  "success": true,
  "data": {
    "jobId": "608f8997-5207-480c-9ff2-d2475cba6b9d",
    "status": "success",
    "message": "Successfully generated N slides",
    "downloadUrl": "https://...pdf...",
    "jobUrl": "https://2slides.com/workspace?jobId=...",
    "slidePageCount": 3,
    "successCount": 3,
    "failedCount": 0
  }
}
```

**注意：**
- 与 create-like-this 类似，但不需要参考图
- 由 AI 根据内容和设计规格生成自定义设计
- 积分消耗相同：1K/2K 每页 100 积分，4K 每页 200 积分
- 处理时长：每页约 30 秒
- 请检查所选模式与返回的任务状态；不要凭 HTTP 成功就认定生成完成

---

### 4. 生成旁白

为幻灯片添加 AI 语音旁白，支持单说话人或多说话人模式。

**端点：** `POST /slides/generate-narration`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**请求体：**
```json
{
  "jobId": "string (required) - Job ID from slide generation (UUID format)",
  "language": "string (optional, default: 'Auto') - Language for narration",
  "voice": "string (optional, default: 'Puck') - Voice name from available voices",
  "multiSpeaker": "boolean (optional, default: false) - Enable multi-speaker mode"
}
```

**可用音色（共 30 种）：**
Puck, Aoede, Charon, Kore, Fenrir, Zephyr, Leda, Orus, Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, Sulafat

**响应：**
```json
{
  "success": true,
  "jobId": "abc123...",
  "status": "pending",
  "message": "Narration generation started"
}
```

**注意：**
- 添加旁白前任务必须已完成
- Nano Banana 任务的 Job ID 必须为 UUID 格式
- 费用：每页 210 积分（文本 10 积分，音频 200 积分）
- 异步执行：用 /jobs/{jobId} 轮询
- 多说话人模式使用不同音色增加变化
- 支持 19 种语言并可自动检测

---

### 5. 下载幻灯片页面与语音

把幻灯片导出为 PNG 文件、语音旁白导出为 WAV 文件，打包成 ZIP。

**端点：** `POST /slides/download-slides-pages-voices`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**请求体：**
```json
{
  "jobId": "string (required) - Job ID from slide generation"
}
```

**响应：**
```json
{
  "success": true,
  "downloadUrl": "https://...zip...",
  "message": "Download ready"
}
```

**压缩包内容：**
- Pages：每页幻灯片的 PNG 文件
- Voices：WAV 音频文件（如果生成了旁白）
- Transcripts：含旁白文字稿的文本文件

**注意：**
- **费用：完全免费**（不消耗积分）
- 下载 URL **仅 1 小时内有效**
- 高质量 PNG 导出
- 音频为 WAV 格式
- 包含全部幻灯片和语音文件

---

### 6. 搜索主题

搜索可用的演示文稿主题。

**端点：** `GET /themes/search`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
```

**查询参数：**
```
query: string (required) - Search keyword
limit: number (optional, default: 20, max: 100)
```

**响应：**
```json
{
  "themes": [
    {
      "id": "theme_id_123",
      "name": "Professional Blue",
      "description": "Clean professional theme with blue accents",
      "previewUrl": "https://..."
    }
  ],
  "count": 1
}
```

---

### 7. 查询任务状态

获取异步生成任务的状态和结果。

**端点：** `GET /jobs/{jobId}`

**请求头：**
```
Authorization: Bearer YOUR_API_KEY
```

**路径参数：**
```
jobId: string (required) - Job ID from async generation
```

**响应：**
```json
{
  "jobId": "abc123",
  "status": "completed|pending|failed",
  "slideUrl": "https://2slides.com/slides/...",
  "pdfUrl": "https://2slides.com/slides/.../download",
  "narrationStatus": "completed|pending|not_started",
  "error": "error message if failed"
}
```

**状态取值：**
- `pending`：任务仍在处理
- `completed`：幻灯片已就绪
- `failed`：生成失败（见 error 字段）

**旁白状态取值：**
- `not_started`：未请求旁白
- `pending`：旁白正在生成
- `completed`：旁白已就绪

**轮询建议：**
每 20-30 秒轮询一次，避免给服务器造成压力

---

## 错误处理

所有端点返回标准 HTTP 状态码：

- `200 OK`：请求成功
- `400 Bad Request`：参数无效
- `401 Unauthorized`：API key 缺失或无效
- `404 Not Found`：资源不存在
- `429 Too Many Requests`：超出速率限制
- `500 Internal Server Error`：服务器错误

**错误响应格式：**
```json
{
  "error": "Error message",
  "code": "ERROR_CODE"
}
```

**常见错误码：**
- `INSUFFICIENT_CREDITS`：账户积分不足
- `INVALID_JOB_ID`：任务 ID 不存在或格式无效
- `RATE_LIMIT_EXCEEDED`：请求过多（见下方速率限制）
- `JOB_NOT_COMPLETED`：添加旁白前任务必须完成
- `INVALID_UUID`：Job ID 必须为 UUID 格式（Nano Banana 任务）

---

## 积分消耗

- **Fast PPT（generate 端点）**：每页 10 积分
- **Nano Banana 1K/2K（create-like-this、create-pdf-slides）**：每页 100 积分
- **Nano Banana 4K**：每页 200 积分
- **语音旁白**：每页 210 积分（文本 10 积分，音频 200 积分）
- **下载导出**：免费（不消耗积分）

## 购买积分

2slides 采用**按量付费的积分体系**，无需订阅。

**积分套餐**（当前促销：最高优惠 20%）：

| 积分 | 价格 | 每千积分成本 | 优惠 |
|---------|-------|---------------|---------|
| 2,000 | $5.00 | $2.50 | 无 |
| 4,000 | $9.50 | $2.38 | 5% |
| 10,000 | $22.50 | $2.25 | 10% |
| 20,000 | $42.50 | $2.13 | 15% |
| 40,000 | $80.00 | $2.00 | 20% |

**主要权益：**
- 新用户获赠 **500 免费积分**（约 50 页 Fast PPT）
- **积分永不过期**
- 无月度订阅
- 3 天退款期
- 购买地址：https://2slides.com/pricing

**费用示例：**
- 10 页 Fast PPT 演示文稿：100 积分（按最大套餐折合约 $0.25）
- 10 页 Nano Banana 2K 演示文稿：1,000 积分（按最大套餐折合约 $2.00）
- 10 页含旁白演示文稿：2,100 积分（按最大套餐折合约 $4.20）

## 速率限制

不同端点的速率限制不同：

- **Fast PPT（generate）**：每分钟 10 次请求
- **Nano Banana（create-like-this、create-pdf-slides）**：每分钟 6 次请求

**最佳实践：**
- 异步任务每 20-30 秒轮询一次，避免给服务器造成压力
- 被限流（429 错误）时先等待再重试
- 到 https://2slides.com/api 查看你所在套餐的速率限制

## 下载 URL 有效期

所有下载 URL（PDF、ZIP 压缩包）**仅 1 小时内有效**。生成后请尽快下载文件。

---

## 最佳实践

### 内容格式

**为获得最佳效果，把内容组织清晰：**

```
Title: Introduction to AI

Section 1: Machine Learning
- Definition
- Key concepts
- Applications

Section 2: Deep Learning
- Neural networks
- Training process
- Use cases
```

### 同步与异步模式的选择

- 快速生成（<5 页）时**用同步**
- 较大的演示文稿（>5 页）**用异步**
- 集成到可轮询的工作流时**用异步**

### 主题选择

1. 用相关关键词搜索主题
2. 如有预览 URL 可先预览
3. 在生成请求中使用主题 ID
4. 留空主题则使用默认样式

### 语言支持

指定 `responseLanguage` 生成不同语言的幻灯片：
- `"Auto"` - 自动检测语言（默认）
- `"English"` - English
- `"Simplified Chinese"` - 简体中文
- `"Traditional Chinese"` - 繁體中文
- `"Spanish"` - Español
- `"Arabic"` - العربية
- `"Portuguese"` - Português
- `"Indonesian"` - Bahasa Indonesia
- `"Japanese"` - 日本語
- `"Russian"` - Русский
- `"Hindi"` - हिन्दी
- `"French"` - Français
- `"German"` - Deutsch
- `"Vietnamese"` - Tiếng Việt
- `"Turkish"` - Türkçe
- `"Polish"` - Polski
- `"Italian"` - Italiano
- `"Korean"` - 한국어
