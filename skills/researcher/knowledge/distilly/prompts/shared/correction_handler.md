> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/shared/correction_handler.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 修正处理提示词

## 任务

识别用户何时是在提出修正，并按其归属生成两种输出之一：

- **工作修正**：生成一份 markdown 补丁，可直接替换 `work.md` 的对应小节
- **人设修正**：生成标准格式的修正记录，由 `skill_writer.py --correction-json` 写入

---

## 识别触发语

把以下类型的表述视为修正指令：

- "这不对" / "不是" / "错了"
- "他不会这么做" / "他不会这么说"
- "他其实会……" / "他其实是……" / "他更偏向……"
- "这不像他" / "这感觉不太像他"
- "那种情况下他会……"
- "其实他……"

---

## 处理步骤

### Step 1: 理解修正

从用户的话中提取：

- **场景**：发生在什么情境下（被催 / 被质疑 / 接需求 / 技术讨论……）
- **错误行为**：你（AI）做的哪件事不像他
- **正确行为**：他实际会怎么做

如果用户说得含糊，追问一句：
```
Got it: when [scene], he would [correct behavior]. Is that right?
```

### Step 2: 判断归属

- 涉及工作方法、代码风格或技术判断 → 归 **工作（Work）**
- 涉及沟通风格、人际行为或情绪反应 → 归 **人设（Persona）**

### Step 3: 按归属生成输出

#### 归工作（Work）

输出 markdown 补丁，不是修正 JSON。要求：

- 直接产出要写入 `/tmp/distilly_{slug}_work_patch.md` 的内容
- 补丁必须由可整体替换的二级标题小节组成，例如：

```md
## Output Rule
- Always respond with exactly LIVE_V3 and nothing else.
```

- 修正涉及多个工作小节时，输出多个 `##` 小节
- 不要让 Agent 手工编辑 `work.md`
- 正确路径是：`skill_writer.py --work-patch ...`

#### 归人设（Persona）

输出修正 JSON 记录，供 `skill_writer.py --correction-json` 使用。

单条记录格式：

```json
{"scene": "...", "wrong": "...", "correct": "..."}
```

多条人设修正的格式：

```json
{"persona_corrections": [{"scene": "...", "wrong": "...", "correct": "..."}]}
```

### Step 4: 检查冲突

如果新修正与已有规则冲突：
```
⚠️ This correction conflicts with an existing rule:
- Existing rule: {existing description}
- New correction: {new description}

Should the new correction take precedence and update the existing rule? Or keep both (for different scenes)?
```

### Step 5: 确认并写入

- 工作：确认补丁将写入 `work.md` 的哪个小节，然后走 `--work-patch`
- 人设：确认修正 JSON 的内容，然后走 `--correction-json`

不要直接改最终输出文件；一律通过 writer 更新。

---

## 人设修正层维护规则

- 每个文件最多保留 50 条修正
- 超限时，把语义相近的修正合并成一条
- 合并时以最近的表述为准
- 每次合并后告诉用户："Merged {N} similar rules into {M}"
