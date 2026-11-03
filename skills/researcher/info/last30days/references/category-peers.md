> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/category-peers.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 同类社区扩展

在 Step 0.55 阶段，针对可识别产品所属的可识别类别阅读本文件。适用条件与是否必须扩展，仍以研究运行手册为准。

规范同类社区（唯一事实来源；`scripts/lib/categories.py` 为 `--auto-resolve` 引擎路径镜像了这份清单）：

| 类别 | 触发关键词 | 同类社区（按优先级排序） |
|----------|------------------|---------------------------|
| `ai_image_generation` | image generation, text to image, GPT Image, Nano Banana, Midjourney, Stable Diffusion, DALL-E, Flux.1, Imagen, Seedance, Ideogram, Recraft | `StableDiffusion, midjourney, dalle2, aiArt, PromptEngineering, MediaSynthesis` |
| `ai_video_generation` | video generation, text to video, Sora, Veo 3, Runway Gen, Kling, Pika Labs, Luma Dream Machine, Hailuo | `aivideo, StableDiffusion, runwayml, singularity, MediaSynthesis` |
| `ai_music_generation` | music generation, ai music, Suno, Udio, Riffusion, Stable Audio | `SunoAI, udiomusic, aimusic, artificial` |
| `ai_coding_agent` | Claude Code, Cursor IDE, GitHub Copilot, Windsurf, Aider, Cline, OpenClaw, Hermes Agent, Continue.dev, Codeium, Devin | `ChatGPTCoding, LocalLLaMA, singularity, PromptEngineering` |
| `ai_agent_framework` | agent framework, LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex, DSPy, smolagents | `LangChain, LocalLLaMA, AI_Agents, MachineLearning` |
| `ai_chat_model` | GPT-5/4, Claude Opus/Sonnet/Haiku, Gemini Pro/Flash, Llama 3/4, DeepSeek, Qwen, Mistral Large, Grok | `LocalLLaMA, ChatGPT, ClaudeAI, singularity, artificial` |
| `saas_screen_recording` | screen recording, screen recorder, Loom video, Tella screen, Vidyard | `SaaS, screenrecording, productivity, Entrepreneur` |
| `saas_productivity` | Notion app, Obsidian, Linear app, Asana, ClickUp, productivity app | `productivity, SaaS, ObsidianMD, Notion` |
| `prediction_markets` | Polymarket, Kalshi, prediction market, event contracts, Manifold Markets | `Polymarket, Kalshi, predictionmarkets` |
| `crypto_defi` | DeFi protocol, yield farming, liquidity pool, stablecoin, layer 2, L2 rollup | `defi, ethfinance, CryptoCurrency, ethereum` |

**合并规则。** 以 WebSearch 返回的社区为起点，按上表优先级顺序追加 2-3 个同类社区。忽略大小写去重（如果 WebSearch 已返回 `midjourney`，就不要重复列出）。总数上限为 10：若加上全部同类社区会超限，则保留每一个 WebSearch 返回的社区（它们是最新鲜的信号），并从优先级列表末尾开始丢弃同类社区。

**外推。** 若主题所属类别不在表中（新的 AI 工具、小众 SaaS），沿用同样的思路：挑选 2-3 个技术讨论最活跃的跨产品社区。新的图像生成工具仍然对应 `r/StableDiffusion, r/midjourney, r/aiArt`。新的代码编辑器仍然对应 `r/ChatGPTCoding, r/LocalLLaMA`。

**实例——出错的检索式。** 主题：`Prompting GPT Image 2`。

之前（2026-04-22 的失败形态）：
```
Resolved:
- Reddit: r/OpenAI, r/ChatGPT, r/singularity, r/ChatGPTpromptengineering, r/artificial
```

之后（加入同类社区扩展）：
```
Resolved:
- Reddit: r/OpenAI, r/ChatGPT, r/singularity, r/ChatGPTpromptengineering, r/StableDiffusion, r/midjourney, r/dalle2, r/aiArt (+ ai_image_generation peers)
```

括号中的 `(+ ai_image_generation peers)` 是新版 Resolved 块格式的可观测约定。Step 0.55 的同类社区自检见研究运行手册。
