> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/multi-agent-patterns/references/frameworks.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 多 Agent 模式：技术参考

本文档给出多 Agent 架构在不同框架下的实现细节。

## 主管模式（Supervisor）

### LangGraph 主管实现

实现一个把任务路由到工作节点的主管：

```python
from typing import TypedDict, Union
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    task: str
    current_agent: str
    task_output: dict
    messages: list

def supervisor_node(state: AgentState) -> AgentState:
    """
    Supervisor decides which worker to invoke next.
    
    Returns routing decision and updates state.
    """
    task = state["task"]
    messages = state.get("messages", [])
    
    # Determine next agent based on task and history
    if "research" in task.lower():
        next_agent = "researcher"
    elif "write" in task.lower() or "create" in task.lower():
        next_agent = "writer"
    elif "review" in task.lower() or "analyze" in task.lower():
        next_agent = "reviewer"
    else:
        next_agent = "coordinator"
    
    return {
        "task": task,
        "current_agent": next_agent,
        "task_output": {},
        "messages": messages + [{"supervisor": f"Routing to {next_agent}"}]
    }

def researcher_node(state: AgentState) -> AgentState:
    """Research worker that gathers information."""
    # Perform research task
    output = perform_research(state["task"])
    
    return {
        "task": state["task"],
        "current_agent": "researcher",
        "task_output": output,
        "messages": state["messages"] + [{"researcher": "Research complete"}]
    }

def writer_node(state: AgentState) -> AgentState:
    """Writer worker that creates content based on research."""
    output = create_content(state["task"], state["task_output"])
    
    return {
        "task": state["task"],
        "current_agent": "writer",
        "task_output": output,
        "messages": state["messages"] + [{"writer": "Content created"}]
    }

def build_supervisor_graph():
    """Build the supervisor workflow graph."""
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("writer", writer_node)
    
    # Add edges
    workflow.add_edge("supervisor", "researcher")
    workflow.add_edge("researcher", "supervisor")
    workflow.add_edge("supervisor", "writer")
    workflow.add_edge("writer", "supervisor")
    
    # Set entry point
    workflow.set_entry_point("supervisor")
    
    return workflow.compile()
```

### AutoGen 主管

用 GroupChat 模式实现主管：

```python
from autogen import AssistantAgent, UserProxyAgent, GroupChat

# Define specialized agents
researcher = AssistantAgent(
    name="researcher",
    system_message="""You are a research specialist.
    Your goal is to gather accurate, comprehensive information
    on topics assigned by the supervisor. Always cite sources
    and note confidence levels.""",
    llm_config=llm_config
)

writer = AssistantAgent(
    name="writer",
    system_message="""You are a content creation specialist.
    Your goal is to create well-structured content based on
    research provided by the supervisor. Follow style guidelines
    and ensure factual accuracy.""",
    llm_config=llm_config
)

# Define supervisor
supervisor = AssistantAgent(
    name="supervisor",
    system_message="""You are the project supervisor.
    Your goal is to coordinate researchers and writers to
    complete tasks efficiently.
    
    Process:
    1. Break down the task into research and writing phases
    2. Route to appropriate specialists
    3. Synthesize results into final output
    4. Ensure quality before completing""",
    llm_config=llm_config
)

# Configure group chat
group_chat = GroupChat(
    agents=[supervisor, researcher, writer],
    messages=[],
    max_round=20
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)
```

## Swarm 模式实现

### LangGraph Swarm

实现同级代理之间的移交（handoff）：

```python
def create_agent(name, system_prompt, tools):
    """Create an agent node for the swarm."""
    
    def agent_node(state):
        # Process current state with agent
        response = invoke_agent(name, system_prompt, state["input"], tools)
        
        # Check for handoff
        if "handoff" in response:
            return {"next_agent": response["handoff"], "output": response["output"]}
        else:
            return {"next_agent": END, "output": response["output"]}
    
    return agent_node

def build_swarm():
    """Build a peer-to-peer agent swarm."""
    workflow = StateGraph(State)
    
    # Create agents
    triage = create_agent("triage", TRIAGE_PROMPT, [search, read])
    research = create_agent("research", RESEARCH_PROMPT, [search, browse, read])
    analysis = create_agent("analysis", ANALYSIS_PROMPT, [calculate, compare])
    writing = create_agent("writing", WRITING_PROMPT, [write, edit])
    
    # Add to graph
    workflow.add_node("triage", triage)
    workflow.add_node("research", research)
    workflow.add_node("analysis", analysis)
    workflow.add_node("writing", writing)
    
    # Define handoff edges
    workflow.add_edge("triage", "research")
    workflow.add_edge("triage", "analysis")
    workflow.add_edge("research", "writing")
    workflow.add_edge("analysis", "writing")
    
    workflow.set_entry_point("triage")
    
    return workflow.compile()
```

## 层级模式实现

### CrewAI 风格层级

```python
class ManagerAgent:
    def __init__(self, name, system_prompt, llm):
        self.name = name
        self.system_prompt = system_prompt
        self.llm = llm
        self.workers = []
    
    def add_worker(self, worker):
        """Add a worker agent to the team."""
        self.workers.append(worker)
    
    def delegate(self, task):
        """
        Analyze task and delegate to appropriate worker.
        
        Returns work assignment and expected output format.
        """
        # Analyze task requirements
        requirements = analyze_task_requirements(task)
        
        # Select best worker
        best_worker = select_worker(self.workers, requirements)
        
        # Create assignment
        assignment = {
            "worker": best_worker.name,
            "task": task,
            "context": self.get_relevant_context(task),
            "output_format": requirements.output_format,
            "deadline": requirements.deadline
        }
        
        return assignment
    
    def review_output(self, worker_output, requirements):
        """
        Review worker output against requirements.
        
        Returns approval or revision request.
        """
        quality_score = assess_quality(worker_output, requirements)
        
        if quality_score >= requirements.threshold:
            return {"status": "approved", "output": worker_output}
        else:
            return {
                "status": "revision_requested",
                "feedback": generate_feedback(worker_output, requirements),
                "revise_worker": requirements.revise_worker
            }
```

## 上下文隔离模式

### 全上下文委派

```python
def delegate_with_full_context(planner_state, subagent):
    """
    Pass entire planner context to subagent.
    
    Use for complex tasks requiring complete understanding.
    """
    return {
        "context": planner_state,
        "subagent": subagent,
        "isolation_mode": "full"
    }
```

### 指令传递

```python
def delegate_with_instructions(task_spec, subagent):
    """
    Pass only instructions to subagent.
    
    Use for simple, well-defined subtasks.
    """
    return {
        "instructions": {
            "objective": task_spec.objective,
            "constraints": task_spec.constraints,
            "inputs": task_spec.inputs,
            "outputs": task_spec.output_schema
        },
        "subagent": subagent,
        "isolation_mode": "minimal"
    }
```

### 文件系统协作

```python
class FileSystemCoordination:
    def __init__(self, workspace_path):
        self.workspace = workspace_path
    
    def write_shared_state(self, key, value):
        """Write state accessible to all agents."""
        path = f"{self.workspace}/{key}.json"
        with open(path, 'w') as f:
            json.dump(value, f)
        return path
    
    def read_shared_state(self, key):
        """Read state written by any agent."""
        path = f"{self.workspace}/{key}.json"
        with open(path, 'r') as f:
            return json.load(f)
    
    def acquire_lock(self, resource, agent_id):
        """Prevent concurrent access to shared resources."""
        lock_path = f"{self.workspace}/locks/{resource}.lock"
        if os.path.exists(lock_path):
            return False
        with open(lock_path, 'w') as f:
            f.write(agent_id)
        return True
```

## 共识机制

### 加权投票

```python
def weighted_consensus(agent_outputs, weights):
    """
    Calculate weighted consensus from agent outputs.
    
    Weight = verbalized_confidence * domain_expertise
    """
    weighted_sum = sum(
        output.vote * weights[output.agent_id]
        for output in agent_outputs
    )
    total_weight = sum(weights[output.agent_id] for output in agent_outputs)
    
    return weighted_sum / total_weight
```

### 辩论协议

```python
class DebateProtocol:
    def __init__(self, agents, max_rounds=5):
        self.agents = agents
        self.max_rounds = max_rounds
        self.history = []
    
    def run_debate(self, topic):
        """Execute structured debate on topic."""
        # Initial statements
        statements = {agent.name: agent.initial_statement(topic) 
                      for agent in self.agents}
        
        for round_num in range(self.max_rounds):
            # Generate critiques
            critiques = {}
            for agent in self.agents:
                critiques[agent.name] = agent.critique(
                    topic, 
                    statements,
                    exclude=[agent.name]
                )
            
            # Update statements with critique integration
            for agent in self.agents:
                statements[agent.name] = agent.integrate_critique(
                    statements[agent.name],
                    critiques
                )
            
            # Check for convergence
            if self.check_convergence(statements):
                break
        
        # Final evaluation
        return self.evaluate_final(statements)
```

## 故障恢复

### 熔断器

```python
class AgentCircuitBreaker:
    def __init__(self, failure_threshold=3, timeout_seconds=60):
        self.failure_count = {}
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
    
    def call(self, agent, task):
        """Execute agent task with circuit breaker protection."""
        if self.is_open(agent.name):
            raise CircuitBreakerOpen(f"Agent {agent.name} temporarily unavailable")
        
        try:
            result = agent.execute(task)
            self.record_success(agent.name)
            return result
        except Exception as e:
            self.record_failure(agent.name)
            if self.failure_count[agent.name] >= self.failure_threshold:
                self.open_circuit(agent.name)
            raise
```

### 检查点与恢复

```python
class CheckpointManager:
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(checkpoint_dir, exist_ok=True)
    
    def save_checkpoint(self, workflow_id, step, state):
        """Save workflow state for potential resume."""
        checkpoint = {
            "workflow_id": workflow_id,
            "step": step,
            "state": state,
            "timestamp": time.time()
        }
        path = f"{self.checkpoint_dir}/{workflow_id}.json"
        with open(path, 'w') as f:
            json.dump(checkpoint, f)
    
    def load_checkpoint(self, workflow_id):
        """Load last saved checkpoint for workflow."""
        path = f"{self.checkpoint_dir}/{workflow_id}.json"
        with open(path, 'r') as f:
            return json.load(f)
```
