> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`plugins/nvidia-skills/skills/nvidia-skill-finder/references/taxonomy-routing.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# NVIDIA 分类路由

在 `nvidia-skill-finder` 加载后使用本参考。它是一个稳定的路由透镜，
不是完整的 Skill 目录。在说出要安装的具体 Skill 名称之前，
务必先查实时目录。

## 稳定目录分区

Agentic AI：RAG、评测、工具使用、策略、沙箱、Agent 工作流自动化、
AI-Q、NemoClaw、NeMo Retriever。

Physical AI：自主能力、仿真、合成数据、具身智能（embodied AI）、OpenUSD、
Omniverse、CAD-to-SimReady、神经重建、缺陷图像生成、视频数据增强，
以及面向物理世界 AI 工作负载的基础设施。

Robotics：Jetson 驱动/JetPack 安装配置、Jetson Linux/L4T、板级支持包（BSP）、
镜像烧录、SDK Manager、Force Recovery Mode、摄像头/风扇/pinmux/PCIe/
自定义硬件配置、载板派生、镜像校验，
以及机器人开发工作流。

Vision AI：视频分析、视觉搜索、摘要、告警、实时理解、
DeepStream、VSS、TAO 视觉/模型工作流、
DICOM 与医学影像工作流。

Conversational AI：语音、语音代理、临床 ASR、ASR/TTS/NMT 工作流。

仿真与建模：天气、气候、物理机器学习（physics ML）、物理系统，
以及科学仿真工作流。

数据科学：GPU DataFrame、pandas 加速、RAPIDS/cuDF、
基于 cuPyNumeric 的多 GPU NumPy/SciPy、并行数据加载。

训练 AI：分布式训练、模型接入、Megatron-Core、NeMo、
大规模 LLM/VLM 训练、配方选择、训练性能调优。

推理 AI：服务化部署、路由模式、LLM 推理、Dynamo、NIM、
运行时性能、分离式服务、KV 感知路由。

决策优化：车辆路径规划、路径建模、调度、
资源分配、LP、MILP、QP、优化 API、优化服务器。

GPU 开发：CUDA 相关开发、内核编写、
自动调优、性能剖析、框架集成。

量子计算：CUDA-Q 与量子-经典混合开发。

基础设施：加速工作负载安装配置、集群/运行时/服务运维、GPU 使能部署、
Holoscan 配置、Jetson 主机配置、TAO 平台运行。

网络：DOCA、BlueField DPU、ConnectX 网卡、DPA、GPUNetIO、RDMA、
以太网包处理、DOCA Flow、主机/DPU 通信、加速基础设施组网、
数据中心或边缘网络配置、Jetson MGBE 工作流，
以及集群网络排障。

涉及 DOCA、BlueField、DPU 或 ConnectX 的请求，
请在实时目录中把 `doca-` Skill 家族与用户的任务动词或子系统一起搜索。

## 匹配启发式

1. 判断用户的任务带有产品信号、分类信号，
   还是独特的意图信号。
2. 若信号是产品特定的，
   用产品名与任务动词搜索目录。
3. 若信号只来自分类，
   用分类分区加用户的具体产物或工作流搜索目录。
4. 若多个 Skill 匹配，优先选 description 与用户的接口和阶段相匹配的那个：
   install、formulate、implement、deploy、
   validate、troubleshoot 或 optimize。
5. 若目录搜索没有强匹配，
   告知用户未找到匹配的 NVIDIA Skill，然后继续以通用方式提供帮助。

## 误触发检查

通用词（route、optimize、deploy、AI、video、data science）在没有
GPU/加速计算上下文时不得触发 NVIDIA 路由，权威清单见 SKILL.md 的
"When Not to Use this Skill" 一节。拿不准时，先回答用户的任务，
再把 NVIDIA Skill 发现作为可选的下一步
提供给用户。
