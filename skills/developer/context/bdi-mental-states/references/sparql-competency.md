> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/bdi-mental-states/references/sparql-competency.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# SPARQL 能力问题查询

基于能力问题（competency questions）对 BDI 本体实现进行验证的查询。

## 心智实体查询

### CQ1: 所有心智实体有哪些？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?entity ?type WHERE {
    ?entity rdf:type ?type .
    ?type rdfs:subClassOf* bdi:MentalEntity .
}
```

### CQ2: Agent 持有哪些信念？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?label WHERE {
    ?agent bdi:hasMentalState ?belief .
    ?belief a bdi:Belief .
    OPTIONAL { ?belief rdfs:label ?label }
}
```

### CQ3: Agent 有哪些愿望？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?desire ?label WHERE {
    ?agent bdi:hasDesire ?desire .
    ?desire a bdi:Desire .
    OPTIONAL { ?desire rdfs:label ?label }
}
```

### CQ4: Agent 承诺了哪些意图？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?intention ?label WHERE {
    ?agent bdi:hasIntention ?intention .
    ?intention a bdi:Intention .
    OPTIONAL { ?intention rdfs:label ?label }
}
```

## 动机链查询

### CQ5: 哪些信念促成了某个愿望的形成？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?beliefLabel WHERE {
    ?desire bdi:isMotivatedBy ?belief .
    ?belief a bdi:Belief .
    OPTIONAL { ?belief rdfs:label ?beliefLabel }
}
```

### CQ6: 某个意图实现的是哪个愿望？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?desire ?desireLabel WHERE {
    ?intention bdi:fulfils ?desire .
    ?desire a bdi:Desire .
    OPTIONAL { ?desire rdfs:label ?desireLabel }
}
```

### CQ7: 哪些信念支撑某个意图？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?label WHERE {
    ?intention bdi:isSupportedBy ?belief .
    ?belief a bdi:Belief .
    OPTIONAL { ?belief rdfs:label ?label }
}
```

### CQ8: 追踪某个意图的完整认知链

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?intention ?desire ?belief ?worldState WHERE {
    ?intention a bdi:Intention ;
               bdi:fulfils ?desire ;
               bdi:isSupportedBy ?belief .
    ?desire bdi:isMotivatedBy ?belief .
    ?belief bdi:refersTo ?worldState .
}
```

## 心智过程查询

### CQ9: 哪个心智过程生成了某个信念？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?process ?processType WHERE {
    ?process bdi:generates ?belief .
    ?belief a bdi:Belief .
    ?process a ?processType .
    FILTER(?processType != owl:NamedIndividual)
}
```

### CQ10: 什么触发了心智过程？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?process ?trigger ?triggerType WHERE {
    ?process a bdi:MentalProcess ;
             bdi:isTriggeredBy ?trigger .
    ?trigger a ?triggerType .
}
```

### CQ11: 心智过程对什么进行了推理？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?process ?input WHERE {
    ?process a bdi:MentalProcess ;
             bdi:reasonsUpon ?input .
}
```

## 计划与目标查询

### CQ12: 意图指定了什么计划？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?intention ?plan ?goal WHERE {
    ?intention bdi:specifies ?plan .
    ?plan a bdi:Plan ;
          bdi:addresses ?goal .
}
```

### CQ13: 计划中任务的有序序列是什么？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?plan ?task ?nextTask WHERE {
    ?plan a bdi:Plan ;
          bdi:hasComponent ?task .
    OPTIONAL { ?task bdi:precedes ?nextTask }
}
ORDER BY ?task
```

### CQ14: 计划的第一个和最后一个任务是什么？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?plan ?firstTask ?lastTask WHERE {
    ?plan a bdi:Plan ;
          bdi:beginsWith ?firstTask ;
          bdi:endsWith ?lastTask .
}
```

### CQ15: 哪些动作执行了哪些任务？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?action ?task ?time WHERE {
    ?action bdi:isExecutionOf ?task ;
            bdi:atTime ?time .
}
ORDER BY ?time
```

## 时间查询

### CQ16: 哪些心智状态在特定时间点有效？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?mentalState ?type WHERE {
    ?mentalState bdi:hasValidity ?interval .
    ?interval bdi:hasStartTime ?start ;
              bdi:hasEndTime ?end .
    ?mentalState a ?type .
    FILTER(?start <= "2026-01-04T10:00:00"^^xsd:dateTime && 
           ?end >= "2026-01-04T10:00:00"^^xsd:dateTime)
}
```

### CQ17: 信念是在什么时候形成的？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?formationTime WHERE {
    ?process bdi:generates ?belief ;
             bdi:atTime ?formationTime .
    ?belief a bdi:Belief .
}
```

### CQ18: 意图的时间有效期是怎样的？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?intention ?start ?end WHERE {
    ?intention a bdi:Intention ;
               bdi:hasValidity ?interval .
    ?interval bdi:hasStartTime ?start ;
              bdi:hasEndTime ?end .
}
```

## 证成查询

### CQ19: 什么证成了信念？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?justification ?justLabel WHERE {
    ?belief a bdi:Belief ;
            bdi:isJustifiedBy ?justification .
    OPTIONAL { ?justification rdfs:label ?justLabel }
}
```

### CQ20: 什么证成了意图？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?intention ?justification ?justLabel WHERE {
    ?intention a bdi:Intention ;
               bdi:isJustifiedBy ?justification .
    OPTIONAL { ?justification rdfs:label ?justLabel }
}
```

## 组成查询

### CQ21: 复杂信念由哪些部分组成？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?part ?partLabel WHERE {
    ?belief a bdi:Belief ;
            bdi:hasPart ?part .
    OPTIONAL { ?part rdfs:label ?partLabel }
}
```

### CQ22: 查找组合式心智实体

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?composite (COUNT(?part) AS ?partCount) WHERE {
    ?composite bdi:hasPart ?part .
}
GROUP BY ?composite
HAVING (COUNT(?part) > 1)
```

## 世界状态查询

### CQ23: 信念指向的是哪个世界状态？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief ?worldState ?wsComment WHERE {
    ?belief a bdi:Belief ;
            bdi:refersTo ?worldState .
    OPTIONAL { ?worldState rdfs:comment ?wsComment }
}
```

### CQ24: 哪些动作造就了某个世界状态？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?action ?worldState WHERE {
    ?action bdi:bringsAbout ?worldState .
    ?worldState a bdi:WorldState .
}
```

### CQ25: Agent 感知到了哪些世界状态？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?agent ?worldState ?time WHERE {
    ?agent bdi:perceives ?worldState .
    OPTIONAL { ?worldState bdi:atTime ?time }
}
```

## 验证查询（OWLUnit 风格）

### V1: 每个意图必须恰好实现一个愿望

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?intention WHERE {
    ?intention a bdi:Intention .
    FILTER NOT EXISTS { ?intention bdi:fulfils ?desire }
}
# Expected: Empty result set
```

### V2: 每个信念必须指向一个世界状态

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief WHERE {
    ?belief a bdi:Belief .
    FILTER NOT EXISTS { ?belief bdi:refersTo ?worldState }
}
# Expected: Empty result set (or only abstract beliefs)
```

### V3: 心智过程必须有推理对象

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?process WHERE {
    ?process a bdi:MentalProcess .
    FILTER NOT EXISTS { ?process bdi:reasonsUpon ?input }
}
# Expected: Empty result set
```

### V4: BeliefProcess 只能生成 Belief

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?process ?generated WHERE {
    ?process a bdi:BeliefProcess ;
             bdi:generates ?generated .
    FILTER NOT EXISTS { ?generated a bdi:Belief }
}
# Expected: Empty result set
```

### V5: 计划必须有起始任务和结束任务

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?plan WHERE {
    ?plan a bdi:Plan .
    FILTER NOT EXISTS { 
        ?plan bdi:beginsWith ?first ;
              bdi:endsWith ?last 
    }
}
# Expected: Empty result set
```

## 多 Agent 查询

### CQ26: 哪些信念被多个 Agent 共享？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?belief (COUNT(DISTINCT ?agent) AS ?agentCount) WHERE {
    ?agent bdi:hasMentalState ?belief .
    ?belief a bdi:Belief .
}
GROUP BY ?belief
HAVING (COUNT(DISTINCT ?agent) > 1)
```

### CQ27: 哪些 Agent 共享同一个愿望？

```sparql
PREFIX bdi: <https://w3id.org/fossr/ontology/bdi/>

SELECT ?desire ?agent1 ?agent2 WHERE {
    ?agent1 bdi:hasDesire ?desire .
    ?agent2 bdi:hasDesire ?desire .
    FILTER(?agent1 != ?agent2)
}
```
