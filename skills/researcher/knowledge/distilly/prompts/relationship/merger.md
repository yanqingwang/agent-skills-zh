> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/relationship/merger.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 关系型人格合并

## 任务

把新增的关系材料合并进已有的关系型 Skill，同时不压平已有的情感模式。

---

## 更新规则

- 除非新材料明确与之矛盾，保留此前确立的核心关系规则
- 只在有真实材料支撑时添加新的情感触发点
- 区分：
  - 这个人明确说过的话
  - 这个人反复表现出的行为
  - 用户事后推断出的内容
- 如果这个人随时间发生了变化，保留矛盾

---

## 合并目标

### 新材料包含以下内容时，更新 `persona.md`：

- 聊天记录
- 信件
- 冲突场景
- 重逢场景
- 疏远 / 沉默模式
- 记忆中的语言习惯

### 仅在以下情况更新 `work.md`：

- 该关系型 Skill 还包含面向任务的分支
- 且新材料明确补充的是执行方法而非情感

---

## 输出格式

```text
=== persona.md update ===
{patch}

=== summary ===
- added {n} new relationship patterns
- updated {n} expression details
- preserved {n} contradictions
```
