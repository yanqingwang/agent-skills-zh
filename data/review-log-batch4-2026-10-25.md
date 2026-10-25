# 第四批校验报告（review log · batch 4）

**校验日期：2026-10-25** · **范围**：11 个上游（10 新 + ECC 追加 strategic-compact）、20 个翻译件（18 个 SKILL.md + 2 个 Agent 定义）、66 个原样配套件（累计 3984）
**校验者**：父会话 bash 机械检查 + 2 个独立忠实度子代理（A 组 10 件 / B 组 10 件）
**结论：AGREE（20/20 PASS，3984 件字节一致 diff=0）**

## A. 合规（PASS）

- 新上游 License：claude-plugins-official / OfficeCLI / NVIDIA / gamedev 为 Apache-2.0（NVIDIA SKILL 文件 frontmatter 实标 **CC-BY-4.0 AND Apache-2.0** 双许可，声明块与 manifest 均如实标注，CC-BY 署名由声明块承载）；其余 MIT
- **anthropics/claude-plugins-official（44.4k）为官方仓库首个合规收录**（anthropics/skills 本体仍无 License，继续排除）
- tradermonty 金融内容在 README 加"非投资建议"提示
- 声明块 20/20；无"官方中文版"声称

## B. 忠实度（20/20 PASS）

- A 组：9 PASS + 1 ISSUE → **ISSUE 经父会话直接查证为误报**（报告称 game-designer 行内代码被译、6 处专有名词拼写错误；实际 grep 核验 AskUserQuestion/Sirlin/Csikszentmihalyi/Bartle/Hunicke 拼写全部正确、路径与代理名完好——校验代理自身的报告渲染出错）
- B 组：10/10 PASS（52+ 代码块逐字节一致；strategic-compact 的 160k/250k/60k 阈值与 2.1.233 todo 警告等细节忠实）
- 创意性处理记录：bergside 上游原文笔误 "cerative" 按忠实原则保留并加译注

## C/D. 机械与管线（PASS）

- 机械检查：声明块/name/围栏 20/20；行差 -16~+4（creative-director -16 为中文密度所致，标题 15/15、列表项 122/122、代码块 4/4 独立核实）
- manifest 路径全量存在性 0 缺失（修复：game-studio/waza 的单文件 pairs 因 rglob 对文件路径返回空而漏登记，已手工补 4 条）
- classify 72 件全归类；**新增"规则型"收录模式**（Waza rules）与"Agent 定义抽取"模式（game-studio，先例：第一批 addyosmani agents/code-reviewer.md）
- 全量字节校验终态：**ok=3984 fail=0 diff=0**（过程中刷新 gstack 9 件 + rea 1 件上游漂移——gstack 日均多次提交，属常态）
- 教训：后台校验命令不要接 `| tail`（会截断 DIFF 清单，前两批的"汇总数与日志不符"疑象即此因）

## 已知事项

- Waza 的 chinese.md/english.md/durable-context.md/waza-routing.md 与其自带 skills（check/health/hunt/learn/read）未收录，后续候选
- wshobson/agents 其余 100+ 插件中旧式（无 SKILL.md）仍不适配，新式 plugins/*/skills/*/ 可继续抽取
