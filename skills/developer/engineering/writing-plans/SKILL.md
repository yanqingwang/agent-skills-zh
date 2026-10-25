---
name: writing-plans
description: 当你拿到了一个多步骤任务的规格或需求时、在动代码之前使用
---

> **中文汉化版** · 上游：[obra/superpowers](https://github.com/obra/superpowers) · 原文件：`skills/writing-plans/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 编写计划

## 概述

为一位没有见过这个代码库、也没有见过这份规格的工程师编写实现计划。假设他们一旦知道确切的接口和确切的测试，就能用项目的语言写出地道的代码，并且凡是计划留白的地方他们都会做出合理选择。他们无法知道的是你决定了什么：哪些文件、哪些名字和签名、规格中的哪些取值、哪些测试证明每个任务。把这些写下来。把整个计划拆成一口大小的任务交给他们。DRY。YAGNI。TDD。频繁 commit。

**开始时声明：** "我正在使用 writing-plans 这个 Skill 来创建实现计划。"

**上下文：** 如果在隔离的 worktree 中工作，它应该在执行时通过 `superpowers:using-git-worktrees` 这个 Skill 创建。

**计划保存到：** `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`
- （用户对计划存放位置的偏好优先于此默认值）

## 范围检查

如果规格覆盖了多个相互独立的子系统，它应该在头脑风暴阶段就被拆分成子项目的规格。如果没有，建议把它拆成多份独立的计划，每个子系统一份。每份计划都应该能独立产出可工作的、可测试的软件。

## 文件结构

在定义任务之前，先梳理出将要创建或修改哪些文件，以及每个文件各自负责什么。拆分决策就在这里敲定。

- 用清晰的边界和良好定义的接口来设计单元。每个文件应该只有一个明确职责。
- 你对能一次性装进上下文里的代码推理得最好，而且文件聚焦时你的编辑也更可靠。比起什么都装的大文件，优先选择更小、更聚焦的文件。
- 一起变更的文件应该放在一起。按职责拆分，而不是按技术分层拆分。
- 在既有代码库中，遵循既有模式。如果代码库惯用大文件，不要单方面重构，但如果你要修改的某个文件已经变得臃肿到难以维护，在计划中包含一次拆分是合理的。

这个结构决定任务拆解。每个任务都应该产出自成一体的、独立来看也有意义的改动。

## 任务粒度

任务是最小的单元：它自带一个完整的测试循环，并且值得让一位全新的审查者把关。画任务边界时：把准备工作、配置、脚手架和文档步骤并入需要它们的那个交付物所在的任务；只有当审查者可能有理有据地否决一个任务而通过相邻任务时，才在这里拆开。每个任务都以一个可独立测试的交付物收尾。

## 步骤粒度

**每个步骤是一个动作，并带一个可检查的结果：**
- "写出失败的测试" - 一个步骤
- "运行它确认失败" - 一个步骤
- "实现最小代码让测试通过" - 一个步骤
- "运行测试确认全部通过" - 一个步骤
- "commit" - 一个步骤

## 计划文档头部

**每份计划都必须以下面这个头部开始：**

```markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

**Spec:** [path to the spec/design doc this plan implements — the plan
argues from the spec, so the spec travels with it; executors read both]

## Global Constraints

[The spec's project-wide requirements — version floors, dependency limits,
naming and copy rules, platform requirements — one line each, with exact
values copied verbatim from the spec. Every task's requirements implicitly
include this section.]

## Review Focus

[The five input classes or failure modes the spec implies but no task's
tests exercise that are most likely to bite a person using this software
— one line each, naming the input or condition and the behavior a
reasonable person would expect, most likely first. The spec is a vision
document: it says what the software must do, not everything it will
meet, and its silence on an input is not permission for that input to
break the program. Write the list here, once, with the spec in front of
you. Then, for each line, add the test that pins it to the task that
owns the code, in that task's own step style.]

---
```

## 任务结构

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Interfaces:**
- Consumes: [what this task uses from earlier tasks — exact signatures]
- Produces: [what later tasks rely on — exact function names, parameter
  and return types. A task's implementer sees only their own task; this
  block is how they learn the names and types neighboring tasks use.]

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Implement `function(input: InputType) -> ResultType` in `exact/path/to/file.py`**

One line on the approach when the signature and the test leave a choice
(which library call, which data structure); a code block only for an
algorithm they do not determine.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
````

## 一个步骤里该有什么

当执行者能够根据一个步骤写出恰好一件合理的东西时，这个步骤就算合格。这就是全部要求：无歧义，而不是完备。每种步骤只携带让它无歧义所必需的内容，不多写：

- **测试步骤：** 测试的名字和它的断言，以代码形式给出，其中含规格里的确切取值。
- **代码步骤：** 确切的签名（名字、参数、返回类型）、它所在的文件，以及规格钉死的那些具体取值。函数体由执行者来写。只有当签名和测试都无法确定算法时才给出函数体，或者当规格明确固定了某段文案时才给出原文。
- **验证步骤：** 要运行的命令，以及什么样的输出代表通过。
- **对另一个任务的引用：** 那个任务的 Interfaces 块写明了要用什么；计划不重复那个任务的代码。

计划就是执行者无法独自做出的那组决策。一份比它描述的代码还长的计划，其实是在写代码而不是在写计划。而那些什么都不决定的行（"TBD"、"处理边界情况"、"加上恰当的校验"、"为以上内容写测试"、某个没有任何任务定义的类型或函数）则是另一种相反的失败，自查环节要把这两种失败都抓住。

## 自查

写完完整计划之后，用全新的眼光重新审视规格，并对照它检查计划。这是你自己执行的清单，不是派发给子代理的工作。

**1. 规格覆盖：** 通读规格中的每个章节/需求。你能指出实现它的任务吗？列出所有缺口。

**2. 步骤扫描：** 每个步骤都必须让执行者写出恰好一件合理的东西，任何步骤携带的内容都不得超出这个量：一行什么都不决定的内容是缺口，而签名和测试已经决定得了的函数体则是逐字誊写。两种都要修。

**3. 类型一致性：** 你在后面的任务中使用的类型、方法签名和属性名，与你在前面的任务中定义的是否一致？一个函数在任务 3 里叫 `clearLayers()`、在任务 7 里叫 `clearFullLayers()`，就是一个 bug。

**4. Review Focus：** 对规格隐含的每一类输入或失败模式，是否有一个任务的测试覆盖到它？最可能坑到真实用户的五类未覆盖项进入 Review Focus 章节，其中每一行都要把对应的测试加进拥有该代码的任务里。这一节为空表示你检查过且没有发现，而不是你跳过了检查。

**5. 比例：** 把计划的长度和规格比较。一份比它所实现的规格长好几倍的计划，是程序的逐字誊写，而不是计划。如果代码块占了文档的大头，就把函数体换成签名、测试名和断言，然后确认每个步骤依然无歧义。

发现问题就直接就地修复。不需要重新走一遍自查，修完继续。如果发现某条规格需求没有对应任务，就把任务加上。

## 交接执行

计划保存并自查完毕后，把链接发给人类伙伴阅读。如果他们此前已经明确给出过执行方式，请他们审查计划并确认它捕捉到了他们想要的东西；等待审查完成后再开始实现，然后使用既定的执行方式。否则，请他们审查计划，并在实现之前选择一种执行方式。

**当此前没有给过执行方式时：**

**"计划已完成并保存到 `docs/superpowers/plans/<filename>.md`。请审查这份计划。你更倾向于哪种执行方式？**

- **子代理驱动** - 每个任务由一个全新的子代理实现，并由一位全新的审查者在下一个任务开始前检查它，最后再做一次整个分支的审查。最彻底；代价是每个任务和每次审查都要花费一个全新上下文。
- **原生** - 我在本次会话里按 Harness 的方式亲自实现每个任务，最后由一位使用最强模型的全新审查者检查整个分支。最省最快；结束前没有独立审查。用一个中等档位的会话模型就能跑得很好，因为设计都写在计划里。

**对这份计划，我推荐<两者之一>，因为<来自计划的一句话：任务之间对彼此接口的依赖程度、任务数量、一次发布上线的错误会付出多大代价>。计划捕捉到你想要的东西了吗？我们用哪种方式？"**

**当此前已经给过执行方式时：**

**"计划已完成并保存到 `docs/superpowers/plans/<filename>.md`。请审查这份计划。它捕捉到你想要的东西了吗？"**

**如果选择了子代理驱动：**
- **必用子 Skill：** 使用 superpowers:subagent-driven-development

**如果选择了原生：**
- **必用子 Skill：** 使用 superpowers:executing-plans
