> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/peer-review/references/security_validation.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 安全验证记录

历史验证日期：**2026-07-23**（本地项目日期）。下文各项计数与扫描结果描述
的是那一次运行，不代表一次新的安全认证。

## 基线

仓库的 `SECURITY.md` 条目记录了 **10 项发现**，最高严重级别为
**CRITICAL**：

- 跨文件的环境变量与网络数据外泄
- 一条多文件收集与传输链路
- 两个示意图脚本中的环境信息采集
- 向外部模型服务传输 API 密钥
- 把完整环境传递给子进程
- 反复执行代价高昂的模型与图像操作
- 强制依赖外部示意图与跨 skill 行为

受影响的文件是：

- 已删除：scripts/generate_schematic.py
- 已删除：scripts/generate_schematic_ai.py
- 原有的 `SKILL.md`

## 修复措施

- 删除了两个外部示意图脚本。
- 移除了凭据、环境访问、`.env` 加载、子进程串联、网络请求、模型调用、图像
  生成、强制图表以及跨 skill 调用。
- 用有大小上限的确定性本地 JSON/CSV/Markdown 校验器与生成器取代它们。
- 加入了严格 schema、重复键与表头检测、体积/行数/单元格上限、符号链接拒绝、
  仅限本人可读的原子写入，以及禁止隐式覆盖。
- 加入了报告最小化：输出 ID、计数、规则代码与行号，而不是稿件与评审正文。
- 加入了 AST 测试，拒绝网络库、可执行序列化、动态代码执行以及环境凭据访问。
- 加入了保密、不得再利用、授权、利益冲突、胜任力、AI 政策、披露以及删除/留
  存等关卡。

## 验证结果

- Agent Skills 引用校验器：**PASS**
- 无依赖的 CLI 帮助检查：**PASS**
- 合成标准库测试：**26 项通过**
- 关闭字节码后显式 AST 解析：**8 个脚本完成解析**
- 字节码产物：**0**
- IDE lint：**0**
- 已记录本地路径的链接测试：**PASS**
- Markdown 链接检查：**PASS**（访问受控返回 HTTP 403 视为可达）
- 直接行为安全扫描：**SAFE，0 项发现**
- 带 `--fail-on HIGH` 的拉取请求关卡：**PASS**
- CRITICAL: 0
- HIGH: 0
- LOW: 3

## 残留的 LOW 级发现

最后一次由 LLM 辅助的拉取请求扫描报告：

1. **缺少 `allowed-tools` 声明** — 仅供参考。按照 Agent Skills 规范，该字段
  是可选的。compatibility 与正文已明确把随附工具限定为本地标准库处理，不涉
  及网络、模型、图像、凭据或环境访问。
2. **描述过于宽泛** — 接受为受范围约束的能力描述。强制授权与发表载体政策关
  卡会在读取机密内容之前生效，正文也把所有功能限制在同行评审评估之内。
3. **有上限的 CSV/JSON 处理** — 属于防御性观察，扫描器输出中标注"无需处理"。
  输入本来就已经限定为 4 MiB、5,000 行 CSV、每单元格 12,000 字符以及有限的
  列表长度；测试覆盖了超限拒绝。

这些 LOW 级发现都不允许数据传输或凭据访问。没有遗留 CRITICAL 或 HIG
H 问题。

## 复现方式

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/peer-review -q

uv run skills-ref validate skills/peer-review

uv run skill-scanner scan skills/peer-review --use-behavioral

uv run python scan_pr_skills.py \
  --fail-on HIGH \
  --output /tmp/peer-review-pr-scan.md \
  skills/peer-review
```

仓库层的 `SECURITY.md` 在这次范围受限的更新中有意未做改动；它生成的快照
会通过仓库的常规扫描流程更新。

## 2026-10-01 的维护检查

受理环节现在能区分"已披露但等待放行的利益冲突"与"编辑已实际放行"。报告目
录新增了 SPIRIT-AI 方案与以非预测为目的的 LLM 研究。标准库合成测试通过
（30 项测试与 7 项 CLI 帮助子测试），`skills-ref validate` 也通过。新增
的集合级安全扫描另行协调；上面的历史扫描器计数没有为这份记录重跑。
这些检查使用合成输入，不构成对真实稿件的评审。
