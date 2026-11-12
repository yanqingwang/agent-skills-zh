---
name: 2slides-ppt-generator
description: "通过 2slides API 实现 AI 驱动的演示文稿生成：从文本创建幻灯片、匹配参考图片风格、将文档总结为演示文稿、添加 AI 语音旁白，并导出页面/音频。用于任何“制作幻灯片”“创建演示文稿”或“根据此文档生成幻灯片”的请求。"
category: api-integration
risk: critical
source: community
source_repo: 2slides/slides-generation-2slides-skills
source_type: community
date_added: "2026-06-05"
author: 2slides
tags: [presentations, slides, powerpoint, ai, api-integration, pdf, narration, document-summarization]
tools: [claude, cursor, gemini, codex, antigravity]
plugin:
  setup:
    type: manual
    summary: "Install Python requirements and configure a 2slides API key before running generation scripts."
    docs: SKILL.md
---

> **中文汉化版** · 上游：[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) · 原文件：`skills/2slides-ppt-generator/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 2slides 演示文稿生成

## 详细指南

执行本 Skill 前请阅读[详细指南](references/detailed-guide.md)。其中保留了完整的流程与参考资料。请将其中的安全、前置条件与验证要求视为强制项。针对聚焦任务，加载相关章节；针对端到端任务，则完整阅读该指南。

## 何时使用本 Skill

- 当用户要求根据文本或大纲 "create a presentation"、"make slides" 或 "generate a deck" 时使用。
- 当用户希望幻灯片匹配参考图片的风格时使用（"create slides like this image"）。
- 当用户希望在没有参考图片的情况下获得定制设计的 PDF 幻灯片时使用。
- 当用户上传文档并要求 "create slides from this document" 时使用。
- 当用户希望为生成的幻灯片添加 AI 语音旁白，或将幻灯片导出为 PNG 图片、旁白导出为 WAV 音频时使用。
- 当用户询问 "what themes are available?" 或希望浏览/选择主题时使用。

## 安全与防护说明

- **凭据：** 本 Skill 从 `SLIDES_2SLIDES_API_KEY` 环境变量读取 API key。切勿在命令中硬编码该密钥、将其 commit，或回显给用户。脚本仅通过 HTTPS 将其作为 bearer/`apikey` 值发送到 `https://2slides.com`。
- **网络 + 付费变更：** 每次生成调用都会向 2slides API 发起一次对外网络请求，并**消耗用户的 credits**（视模式不同为 10–210 credits/page）。请将生成、参考图片、定制 PDF 与旁白调用视为计费操作：在生成大规模或高分辨率（4K）演示文稿前确认用户意图，并在页数/成本较高时明确给出预期页数与开销。
- **本地输出：** 下载仅限于当前工作区、公共 HTTPS 与 128 MiB；已存在的输出文件会被拒绝。签名下载 URL 属于 bearer 能力凭证：避免将其记录到日志或分享给预期接收者以外的对象。解包前先校验 ZIP 条目与解压后的大小。
- **输入处理：** 参考图片与文档输入会被发送到 2slides 服务进行处理。不要提交用户未授权交由第三方处理的机密材料。
- **下载 URL 的有效期仅 1 hour**：请及时获取产物，不要将 URL 当作持久存储。

## 局限性

- 请求超时仍可能让已付费的服务端作业继续运行。重试前先检查作业/账户状态；这些脚本不提供幂等键，也不办理退款。`page=0` 会选定未知的页数，因此在进行计费生成前先设定双方认可的明确预算/数量。
- API 响应结构、定价、语音、速率限制与 URL 过期时间依版本而异；以当前来源优先于快照。


- 需要有效的 2slides 账户、API key 和充足的 credits；本 Skill 不负责开通或支付 credits。
- 结果是 AI 生成的草稿，仅作为起点，并非经过事实核查的最终交付物；使用前请审阅内容。
- 本 Skill 不替代针对具体环境的验证或专家评审。若缺少 API key、必需输入，或预期的成本/范围不明确，请停下来询问澄清。
- 存在速率限制（Fast PPT 10/min、Nano Banana 6/min）；每 20–30s 轮询一次异步作业，不要紧凑循环轮询。
