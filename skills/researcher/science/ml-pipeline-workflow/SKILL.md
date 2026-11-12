---
name: ml-pipeline-workflow
description: 构建端到端的 MLOps 流水线，覆盖从数据准备到模型训练、验证与生产部署的全过程。适用于创建 ML 流水线、落地 MLOps 实践，或将模型训练与部署工作流自动化的场景。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/machine-learning-ops/skills/ml-pipeline-workflow/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# ML 流水线工作流

覆盖从数据准备到模型部署的完整端到端 MLOps 流水线编排。

## 概述

本 Skill 为构建生产级 ML 流水线提供全面指导，覆盖完整生命周期：数据摄取 → 准备 → 训练 → 验证 → 部署 → 监控。

## 何时使用本 Skill

- 从零构建新的 ML 流水线
- 为 ML 系统设计工作流编排
- 实现数据 → 模型 → 部署的自动化
- 搭建可复现的训练工作流
- 创建基于 DAG 的 ML 编排
- 将 ML 组件集成到生产系统

## 本 Skill 提供的内容

### 核心能力

1. **流水线架构**
   - 端到端工作流设计
   - DAG 编排模式（Airflow、Dagster、Kubeflow）
   - 组件依赖与数据流
   - 错误处理与重试策略

2. **数据准备**
   - 数据校验与质量检查
   - 特征工程流水线
   - 数据版本管理与血缘
   - 训练集/验证集/测试集划分策略

3. **模型训练**
   - 训练任务编排
   - 超参数管理
   - 实验跟踪集成
   - 分布式训练模式

4. **模型验证**
   - 验证框架与指标
   - A/B 测试基础设施
   - 性能回归检测
   - 模型对比工作流

5. **部署自动化**
   - 模型服务化模式
   - 金丝雀部署
   - 蓝绿部署策略
   - 回滚机制

### 参考文档

详细指南参见 `references/` 目录：

- **data-preparation.md** - 数据清洗、校验与特征工程
- **model-training.md** - 训练工作流与最佳实践
- **model-validation.md** - 验证策略与指标
- **model-deployment.md** - 部署模式与服务化架构

### 资产与模板

`assets/` 目录包含：

- **pipeline-dag.yaml.template** - 用于工作流编排的 DAG 模板
- **training-config.yaml** - 训练配置模板
- **validation-checklist.md** - 部署前验证检查清单

## 使用模式

### 基础流水线搭建


```python
# 1. Define pipeline stages
stages = [
    "data_ingestion",
    "data_validation",
    "feature_engineering",
    "model_training",
    "model_validation",
    "model_deployment"
]

# 2. Configure dependencies
# See assets/pipeline-dag.yaml.template for full example
```


### 生产工作流

1. **数据准备阶段**
   - 从数据源摄取原始数据
   - 执行数据质量检查
   - 应用特征变换
   - 对处理后的数据集做版本管理

2. **训练阶段**
   - 加载带版本管理的训练数据
   - 执行训练任务
   - 跟踪实验与指标
   - 保存训练好的模型

3. **验证阶段**
   - 运行验证测试套件
   - 与基线对比
   - 生成性能报告
   - 审批以进入部署

4. **部署阶段**
   - 打包模型制品
   - 部署到服务化基础设施
   - 配置监控
   - 验证生产流量

## 最佳实践

### 流水线设计

- **模块化**：每个阶段都应可独立测试
- **幂等性**：重复运行各阶段应当安全
- **可观测性**：在每个阶段记录指标
- **版本管理**：跟踪数据、代码与模型版本
- **故障处理**：实现重试逻辑与告警

### 数据管理

- 使用数据校验库（Great Expectations、TFX）
- 用 DVC 或类似工具管理数据集版本
- 记录特征工程变换
- 维护数据血缘追踪

### 模型运维

- 分离训练与服务化基础设施
- 使用模型注册表（MLflow、Weights & Biases）
- 为新模型实施渐进式上线
- 监控模型性能漂移
- 保留回滚能力

### 部署策略

- 从影子部署开始
- 用金丝雀发布做验证
- 搭建 A/B 测试基础设施
- 设置自动回滚触发器
- 监控延迟与吞吐量

## 集成点

### 编排工具

- **Apache Airflow**：基于 DAG 的工作流编排
- **Dagster**：基于资产的流水线编排
- **Kubeflow Pipelines**：Kubernetes 原生的 ML 工作流
- **Prefect**：现代数据流自动化

### 实验跟踪

- MLflow 用于实验跟踪与模型注册表
- Weights & Biases 用于可视化与协作
- TensorBoard 用于训练指标

### 部署平台

- AWS SageMaker 提供托管的 ML 基础设施
- Google Vertex AI 用于 GCP 部署
- Azure ML 用于 Azure 云
- OCI Data Science 用于 Oracle Cloud Infrastructure 部署
- Kubernetes + KServe 用于与云无关的服务化

## 渐进式展开

从基础开始，逐步增加复杂度：

1. **Level 1**：简单线性流水线（数据 → 训练 → 部署）
2. **Level 2**：加入验证与监控阶段
3. **Level 3**：实现超参数调优
4. **Level 4**：加入 A/B 测试与渐进式上线
5. **Level 5**：带集成策略的多模型流水线

## 常见模式

### 批量训练流水线


```yaml
# See assets/pipeline-dag.yaml.template
stages:
  - name: data_preparation
    dependencies: []
  - name: model_training
    dependencies: [data_preparation]
  - name: model_evaluation
    dependencies: [model_training]
  - name: model_deployment
    dependencies: [model_evaluation]
```


### 实时特征流水线


```python
# Stream processing for real-time features
# Combined with batch training
# See references/data-preparation.md
```


### 持续训练


```python
# Automated retraining on schedule
# Triggered by data drift detection
# See references/model-training.md
```


## 故障排查

### 常见问题

- **流水线失败**：检查依赖与数据可用性
- **训练不稳定**：检查超参数与数据质量
- **部署问题**：校验模型制品与服务化配置
- **性能下降**：监控数据漂移与模型指标

### 调试步骤

1. 检查每个阶段的流水线日志
2. 校验边界处的输入/输出数据
3. 隔离测试各组件
4. 复查实验跟踪指标
5. 检查模型制品与元数据

## 后续步骤

搭建好流水线之后：

1. 探索 **hyperparameter-tuning** Skill 以做优化
2. 学习 **experiment-tracking-setup**，了解 MLflow/W&B
3. 查阅 **model-deployment-patterns**，了解服务化策略
4. 用可观测性工具实现监控

## 相关 Skill

- **experiment-tracking-setup**：MLflow 与 Weights & Biases 集成
- **hyperparameter-tuning**：自动化超参数优化
- **model-deployment-patterns**：进阶部署策略
