> **中文汉化版** · 上游：[Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) · 原文件：`0-autoresearch-skill/references/skill-routing.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Skill 路由：何时用哪个领域 Skill

autoresearch skill 负责编排 — 领域 skill 负责执行。本参考把研究活动映射到 skill 库。

## 路由原则

研究过程中遇到领域特定任务时，到 skill 库里找合适的工具。开始之前先读相关 skill 的 SKILL.md — 里面包含工作流、常见问题和可直接投产的代码示例。

## 完整路由表

### 数据与预处理

| 任务 | Skill | 位置 |
|---|---|---|
| 大规模数据处理 | Ray Data | `05-data-processing/ray-data/` |
| 数据清洗与筛选 | NeMo Curator | `05-data-processing/nemo-curator/` |
| 自定义分词器训练 | HuggingFace Tokenizers | `02-tokenization/hf-tokenizers/` |
| 子词分词 | SentencePiece | `02-tokenization/sentencepiece/` |

### 模型架构与训练

| 任务 | Skill | 位置 |
|---|---|---|
| 大规模预训练 | Megatron-Core | `01-model-architecture/megatron-core/` |
| 轻量级 LLM 训练 | LitGPT | `01-model-architecture/litgpt/` |
| 状态空间模型 | Mamba | `01-model-architecture/mamba/` |
| 线性注意力模型 | RWKV | `01-model-architecture/rwkv/` |
| 小规模预训练 | NanoGPT | `01-model-architecture/nanogpt/` |

### 微调

| 任务 | Skill | 位置 |
|---|---|---|
| 多方法微调 | Axolotl | `03-fine-tuning/axolotl/` |
| 基于模板的微调 | LLaMA-Factory | `03-fine-tuning/llama-factory/` |
| 快速 LoRA 微调 | Unsloth | `03-fine-tuning/unsloth/` |
| PyTorch 原生微调 | Torchtune | `03-fine-tuning/torchtune/` |

### 后训练（RL / 对齐）

| 任务 | Skill | 位置 |
|---|---|---|
| PPO、DPO、SFT 流水线 | TRL | `06-post-training/trl/` |
| 组相对策略优化 | GRPO | `06-post-training/grpo-rl-training/` |
| 可扩展 RLHF | OpenRLHF | `06-post-training/openrlhf/` |
| 无参考对齐 | SimPO | `06-post-training/simpo/` |

### 可解释性

| 任务 | Skill | 位置 |
|---|---|---|
| Transformer 回路分析 | TransformerLens | `04-mechanistic-interpretability/transformerlens/` |
| 稀疏自编码器训练 | SAELens | `04-mechanistic-interpretability/saelens/` |
| 干预实验 | NNsight | `04-mechanistic-interpretability/nnsight/` |
| 因果追踪 | Pyvene | `04-mechanistic-interpretability/pyvene/` |

### 分布式训练

| 任务 | Skill | 位置 |
|---|---|---|
| ZeRO 优化 | DeepSpeed | `08-distributed-training/deepspeed/` |
| 全分片数据并行 | FSDP | `08-distributed-training/fsdp/` |
| 多 GPU 抽象 | Accelerate | `08-distributed-training/accelerate/` |
| 训练框架 | PyTorch Lightning | `08-distributed-training/pytorch-lightning/` |
| 分布式数据 + 训练 | Ray Train | `08-distributed-training/ray-train/` |

### 评测

| 任务 | Skill | 位置 |
|---|---|---|
| 标准 LLM 基准 | lm-evaluation-harness | `11-evaluation/lm-eval-harness/` |
| NeMo 集成评测 | NeMo Evaluator | `11-evaluation/nemo-evaluator/` |
| 自定义评测任务 | Inspect AI | `11-evaluation/inspect-ai/` |

### 推理与服务化

| 任务 | Skill | 位置 |
|---|---|---|
| 高吞吐服务化 | vLLM | `12-inference-serving/vllm/` |
| NVIDIA 优化推理 | TensorRT-LLM | `12-inference-serving/tensorrt-llm/` |
| CPU / 边缘推理 | llama.cpp | `12-inference-serving/llama-cpp/` |
| 结构化生成服务化 | SGLang | `12-inference-serving/sglang/` |

### 实验跟踪

| 任务 | Skill | 位置 |
|---|---|---|
| 完整实验跟踪 | Weights & Biases | `13-mlops/wandb/` |
| 开源实验跟踪 | MLflow | `13-mlops/mlflow/` |
| 训练可视化 | TensorBoard | `13-mlops/tensorboard/` |

### 优化技术

| 任务 | Skill | 位置 |
|---|---|---|
| 高效注意力 | Flash Attention | `10-optimization/flash-attention/` |
| 4/8 位量化 | bitsandbytes | `10-optimization/bitsandbytes/` |
| GPTQ 量化 | GPTQ | `10-optimization/gptq/` |
| AWQ 量化 | AWQ | `10-optimization/awq/` |
| GGUF 格式（llama.cpp） | GGUF | `10-optimization/gguf/` |
| PyTorch 原生量化 | Quanto | `10-optimization/quanto/` |

### 安全与对齐

| 任务 | Skill | 位置 |
|---|---|---|
| Constitutional AI 训练 | Constitutional AI | `07-safety-alignment/constitutional-ai/` |
| 内容安全分类 | LlamaGuard | `07-safety-alignment/llamaguard/` |
| 护栏流水线 | NeMo Guardrails | `07-safety-alignment/nemo-guardrails/` |
| 提示注入检测 | Prompt Guard | `07-safety-alignment/prompt-guard/` |

### 基础设施

| 任务 | Skill | 位置 |
|---|---|---|
| 无服务器 GPU 计算 | Modal | `09-infrastructure/modal/` |
| 多云编排 | SkyPilot | `09-infrastructure/skypilot/` |
| GPU 云实例 | Lambda Labs | `09-infrastructure/lambda-labs/` |

### 代理与 RAG

| 任务 | Skill | 位置 |
|---|---|---|
| 代理流水线 | LangChain | `14-agents/langchain/` |
| 知识检索代理 | LlamaIndex | `14-agents/llamaindex/` |
| 轻量级代理 | Smolagents | `14-agents/smolagents/` |
| 基于 Claude 的代理 | Claude Agent SDK | `14-agents/claude-agent-sdk/` |
| 向量存储（本地） | Chroma | `15-rag/chroma/` |
| 向量相似度检索 | FAISS | `15-rag/faiss/` |
| 文本嵌入 | Sentence Transformers | `15-rag/sentence-transformers/` |
| 托管向量数据库 | Pinecone | `15-rag/pinecone/` |
| 可扩展向量数据库 | Milvus | `15-rag/milvus/` |

### 提示词工程与结构化输出

| 任务 | Skill | 位置 |
|---|---|---|
| 提示词优化 | DSPy | `16-prompt-engineering/dspy/` |
| 结构化 LLM 输出 | Instructor | `16-prompt-engineering/instructor/` |
| 受约束生成 | Guidance | `16-prompt-engineering/guidance/` |
| 基于语法的生成 | Outlines | `16-prompt-engineering/outlines/` |

### 多模态

| 任务 | Skill | 位置 |
|---|---|---|
| 视觉-语言模型 | CLIP | `18-multimodal/clip/` |
| 语音识别 | Whisper | `18-multimodal/whisper/` |
| 视觉指令微调 | LLaVA | `18-multimodal/llava/` |
| 视觉-语言（Qwen） | Qwen2-VL | `18-multimodal/qwen2-vl/` |
| 视觉-语言（Mistral） | Pixtral | `18-multimodal/pixtral/` |
| 视觉理解 | Florence-2 | `18-multimodal/florence-2/` |
| 文档检索 | ColPali | `18-multimodal/colpali/` |

### 可观测性

| 任务 | Skill | 位置 |
|---|---|---|
| LLM 追踪与调试 | LangSmith | `17-observability/langsmith/` |
| LLM 可观测性平台 | Phoenix | `17-observability/phoenix/` |

### 新兴技术

| 任务 | Skill | 位置 |
|---|---|---|
| 混合专家（MoE）训练 | MoE Training | `19-emerging-techniques/moe-training/` |
| 组合已训练模型 | Model Merging | `19-emerging-techniques/model-merging/` |
| 扩展上下文窗口 | Long Context | `19-emerging-techniques/long-context/` |
| 草稿式加速推理 | Speculative Decoding | `19-emerging-techniques/speculative-decoding/` |
| 师生式压缩 | Knowledge Distillation | `19-emerging-techniques/knowledge-distillation/` |
| 缩小模型规模 | Model Pruning | `19-emerging-techniques/model-pruning/` |

### 研究产出

| 任务 | Skill | 位置 |
|---|---|---|
| 生成研究创意 | Research Ideation | `21-research-ideation/` |
| 撰写可投稿论文 | ML Paper Writing | `20-ml-paper-writing/` |

## 常见研究工作流

### 「我需要微调一个模型并评测它」

1. 按需求挑微调 skill（求速度选 Unsloth，求灵活性选 Axolotl）
2. 用 lm-evaluation-harness 跑标准基准
3. 用 W&B 或 MLflow 做跟踪

### 「我需要弄清模型学到了什么」

1. 用 TransformerLens 做回路级分析
2. 用 SAELens 训练 SAE，做特征级理解
3. 用 NNsight 或 Pyvene 跑干预实验

### 「我需要做 RL 训练」

1. 标准 PPO/DPO 从 TRL 起步
2. DeepSeek-R1 式训练用 GRPO skill
3. 需要更大规模时用 OpenRLHF

### 「我需要在云 GPU 上跑实验」

1. 快速的无服务器运行用 Modal
2. 多云优化用 SkyPilot
3. 专用实例用 Lambda Labs

## 查找 Skill

不确定用哪个 skill 时：

```bash
# Search by keyword in skill names
ls */*/SKILL.md | head -20

# Search skill descriptions for a keyword
grep -l "keyword" */*/SKILL.md
```

也可以搜索仓库的 README.md，那里列出了全部 skill 及其描述。
