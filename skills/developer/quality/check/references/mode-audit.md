> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/check/references/mode-audit.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 项目审计模式（全项目记分卡）

当请求是全项目质量记分卡时，从 `check` Mode Picker 加载。区别于默认审查（限 diff）与分诊（issue 批处理）。

一次跑完的全项目质量评估。

**流程**

1. 在目标仓库运行 `python3 <skill-base-dir>/scripts/audit_signals.py --root <project>`，其中 `<skill-base-dir>` 替换为本 Skill 的基目录。脚本输出带标签的块（`=== FILE SIZE HOTSPOTS ===` 至 `=== DENYLIST IN BUILD ===`），每块以 `status: PASS|WARN|FAIL|N/A` 结尾。
2. 粗读 `FILE SIZE HOTSPOTS` 列出的最大源文件（通常 3-5 个；架构已清楚时可提前停止）。
3. 先读 `CLAUDE.md` / `AGENTS.md` / `README.md`，了解项目自己声明的约定，再用通用标准评判。仓库的 Agent 指引本身也属于被审计表面：核实其中的命令与路径仍然存在，把过时、冲突或可删除的规则作为发现报告。
4. 应用下面的四轴评分标准。每轴独立打 0-10 分。总分 = 算术平均。
5. 报告每条会移动轴分的发现，尽量附 file:line 引用、严重级别（CRIT/STRUCT/INCR）和一行修复方案。某轴零发现是合法结果；不要凑数。
6. 只输出到**终端**。不要在目标仓库创建文件。如果用户随后说"保存一下"，再提供 `./docs/<project>-audit.md`；默认是临时输出。

**评分轴**

| 轴 | 覆盖内容 |
|---|---|
| 架构 | 模块边界、耦合、抽象层对比平铺重复、单一事实来源 |
| 代码质量 | 文件大小纪律、去重、可读性、对非显而易见行为的注释 |
| 工程 | 测试、CI 闸门、版本协调、安装 URL 锁定、打包姿态 |
| 性能与风险 | 危险点、范围蔓延、分发风险、隐私姿态、第三方影响范围 |

**打分锚点**

- 9-10：纪律出色，只剩打磨项
- 7-8.5：扎实，有明确的针对性改进
- 5-7：能用，但有结构性欠债
- 5 以下：建议大幅返工

项目已在其自身文档或注释中明确给出理由的 WARN 不是发现；引用该理由并跳过。不要机械地把 WARN 升级为 CRIT。`status: N/A` 的块表示该表面不存在（例如没有打包脚本）；当作沉默处理，不要当作正面信号。

**输出模板（终端）**

```
Project: <name>
Overall: X.X / 10

Architecture: X / 10 -- one-line summary
Code Quality: X / 10 -- one-line summary
Engineering:  X / 10 -- one-line summary
Perf & Risk:  X / 10 -- one-line summary

Findings
[CRIT] <file:line> -- <issue>
       why: <reason grounded in signal or read>
       fix: <concrete action>
[STRUCT] ...
[INCR] ...

Top 3 highest-leverage moves
1. ...
2. ...
3. ...
```

报告之后即停，除非用户要求后续实现。审计模式不修改目标仓库的文件。
