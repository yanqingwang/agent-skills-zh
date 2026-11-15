> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/context-degradation/references/patterns.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 上下文退化模式：技术参考

本文档提供诊断与度量上下文退化的技术细节。

## 注意力分布分析

### U 型曲线测量

测量注意力在上下文各位置上的分布：

```python
def measure_attention_distribution(model, context_tokens, query):
    """
    Measure how attention varies across context positions.
    
    Returns distribution showing attention weight by position.
    """
    attention_by_position = []
    
    for position in range(len(context_tokens)):
        # Measure model's attention to this position
        attention = get_attention_weights(model, context_tokens, query, position)
        attention_by_position.append({
            "position": position,
            "attention": attention,
            "is_beginning": position < len(context_tokens) * 0.1,
            "is_end": position > len(context_tokens) * 0.9,
            "is_middle": True  # Will be overwritten
        })
    
    # Classify positions
    for item in attention_by_position:
        if item["is_beginning"] or item["is_end"]:
            item["region"] = "attention_favored"
        else:
            item["region"] = "attention_degraded"
    
    return attention_by_position
```

### Lost-in-Middle（中段迷失）检测

检测关键信息何时落入注意力退化的区域：

```python
def detect_lost_in_middle(critical_positions, attention_distribution):
    """
    Check if critical information is in attention-favored positions.
    
    Args:
        critical_positions: List of positions containing critical info
        attention_distribution: Output from measure_attention_distribution
    
    Returns:
        Dictionary with detection results and recommendations
    """
    results = {
        "at_risk": [],
        "safe": [],
        "recommendations": []
    }
    
    for pos in critical_positions:
        region = attention_distribution[pos]["region"]
        if region == "attention_degraded":
            results["at_risk"].append(pos)
        else:
            results["safe"].append(pos)
    
    # Generate recommendations
    if results["at_risk"]:
        results["recommendations"].extend([
            "Move critical information to attention-favored positions",
            "Use explicit markers to highlight critical information",
            "Consider splitting context to reduce middle section"
        ])
    
    return results
```

## 上下文污染检测

### 幻觉跟踪

跨对话轮次跟踪潜在的幻觉：

```python
class HallucinationTracker:
    def __init__(self):
        self.claims = []
        self.verifications = []
    
    def add_claims(self, text):
        """Extract claims from text for later verification."""
        claims = extract_claims(text)
        self.claims.extend([{"text": c, "verified": None} for c in claims])
    
    def verify_claims(self, ground_truth):
        """Verify claims against ground truth."""
        for claim in self.claims:
            if claim["verified"] is None:
                claim["verified"] = check_claim(claim["text"], ground_truth)
    
    def get_poisoning_indicators(self):
        """
        Return indicators of potential context poisoning.
        
        High ratio of unverified claims suggests poisoning risk.
        """
        unverified = sum(1 for c in self.claims if not c["verified"])
        verified_false = sum(1 for c in self.claims if c["verified"] == False)
        
        return {
            "unverified_count": unverified,
            "false_count": verified_false,
            "poisoning_risk": verified_false > 0 or unverified > len(self.claims) * 0.3
        }
```

### 错误传播分析

跟踪错误如何在上下文中流动：

```python
def analyze_error_propagation(context, error_points):
    """
    Analyze how errors at specific points affect downstream context.

    Returns visualization of error spread and impact assessment.
    """
    impact_map = {}

    for error_point in error_points:
        # Find all references to content after error point
        downstream_refs = find_references(context, after=error_point)

        for ref in downstream_refs:
            if ref not in impact_map:
                impact_map[ref] = []
            impact_map[ref].append({
                "source": error_point,
                "type": classify_error_type(context[error_point])
            })

    # Assess severity
    high_impact_areas = [k for k, v in impact_map.items() if len(v) > 3]

    return {
        "impact_map": impact_map,
        "high_impact_areas": high_impact_areas,
        "requires_intervention": len(high_impact_areas) > 0
    }
```

## 干扰指标

### 相关性评分

为上下文元素对当前任务的相关性打分：

```python
def score_context_relevance(context_elements, task_description):
    """
    Score each context element for relevance to current task.
    
    Returns scores and identifies high-distraction elements.
    """
    task_embedding = embed(task_description)
    
    scored_elements = []
    for i, element in enumerate(context_elements):
        element_embedding = embed(element)
        relevance = cosine_similarity(task_embedding, element_embedding)
        scored_elements.append({
            "index": i,
            "content_preview": element[:100],
            "relevance_score": relevance
        })
    
    # Sort by relevance
    scored_elements.sort(key=lambda x: x["relevance_score"], reverse=True)
    
    # Identify potential distractors
    threshold = calculate_relevance_threshold(scored_elements)
    distractors = [e for e in scored_elements if e["relevance_score"] < threshold]
    
    return {
        "scored_elements": scored_elements,
        "distractors": distractors,
        "recommendation": f"Consider removing {len(distractors)} low-relevance elements"
    }
```

## 退化监测系统

### 上下文健康看板

实现对上下文健康的持续监测：

```python
class ContextHealthMonitor:
    def __init__(self, model, context_window_limit):
        self.model = model
        self.limit = context_window_limit
        self.metrics = []
    
    def assess_health(self, context, task):
        """
        Assess overall context health for current task.
        
        Returns composite score and component metrics.
        """
        metrics = {
            "token_count": len(context),
            "utilization_ratio": len(context) / self.limit,
            "attention_distribution": measure_attention_distribution(self.model, context, task),
            "relevance_scores": score_context_relevance(context, task),
            "age_tokens": count_recent_tokens(context)
        }
        
        # Calculate composite health score
        health_score = self._calculate_composite(metrics)
        
        result = {
            "health_score": health_score,
            "metrics": metrics,
            "status": self._interpret_score(health_score),
            "recommendations": self._generate_recommendations(metrics)
        }
        
        self.metrics.append(result)
        return result
    
    def _calculate_composite(self, metrics):
        """Calculate composite health score from components."""
        # Weighted combination of metrics
        utilization_penalty = min(metrics["utilization_ratio"] * 0.5, 0.3)
        attention_penalty = self._calculate_attention_penalty(metrics["attention_distribution"])
        relevance_penalty = self._calculate_relevance_penalty(metrics["relevance_scores"])
        
        base_score = 1.0
        score = base_score - utilization_penalty - attention_penalty - relevance_penalty
        return max(0, score)
    
    def _interpret_score(self, score):
        """Interpret health score and return status."""
        if score > 0.8:
            return "healthy"
        elif score > 0.6:
            return "warning"
        elif score > 0.4:
            return "degraded"
        else:
            return "critical"
```

### 告警阈值

配置合适的告警阈值：

```python
CONTEXT_ALERTS = {
    "utilization_warning": 0.7,      # 70% of context limit
    "utilization_critical": 0.9,     # 90% of context limit
    "attention_degraded_ratio": 0.3, # 30% in middle region
    "relevance_threshold": 0.3,      # Below 30% relevance
    "consecutive_warnings": 3        # Three warnings triggers alert
}
```

## 恢复流程

### 上下文截断策略

当上下文退化到无法恢复时，进行战略性截断：

```python
def truncate_context_for_recovery(context, preserved_elements, target_size):
    """
    Truncate context while preserving critical elements.
    
    Strategy:
    1. Preserve system prompt and tool definitions
    2. Preserve recent conversation turns
    3. Preserve critical retrieved documents
    4. Summarize older content if needed
    5. Truncate from middle if still over target
    """
    truncated = []
    
    # Category 1: Critical system elements (preserve always)
    system_elements = extract_system_elements(context)
    truncated.extend(system_elements)
    
    # Category 2: Recent conversation (preserve more)
    recent_turns = extract_recent_turns(context, num_turns=10)
    truncated.extend(recent_turns)
    
    # Category 3: Critical documents (preserve key ones)
    critical_docs = extract_critical_documents(context, preserved_elements)
    truncated.extend(critical_docs)
    
    # Check size and summarize if needed
    while len(truncated) > target_size:
        # Summarize oldest category 3 elements
        truncated = summarize_oldest(truncated, category="documents")
        
        # If still too large, truncate oldest turns
        if len(truncated) > target_size:
            truncated = truncate_oldest_turns(truncated, keep_recent=5)
    
    return truncated
```
