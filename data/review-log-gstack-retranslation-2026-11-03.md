# gstack 重译批次校验报告（review log · 2026-11-03）

**校验日期：2026-11-03** · **范围**：清空 2026-11-02 重译工单——13 个 gstack 翻译件全部重译（上游 v2.0.0 共享前导重构版），9112 行 / 549KB
**校验者**：父会话机械检查（围栏代码块逐字节比对 / YAML / 声明块）+ 10 组翻译代理自检回报
**结论：PASS（13/13 代码块与上游逐字节一致；工单全部销单；lint 0 信号）**

## 重译清单（13 件）

office-hours（683 行）、plan-ceo-review（1045）、design-review（1224）、review（958）、ship（989）、retro（951）、spec（646）、land-and-deploy（599）、plan-eng-review（552）、qa（530）、health（450）、investigate（355）、learn（130）。

## 上游结构变更要点（v2.0.0 共享前导重构）

- 各 skill 的大段共享前导（AskUserQuestion Format、Voice、计划模式、上下文恢复等）移入 `sections/preamble.md`，SKILL.md 正文改为"共享前导指针节 + 增量小节 + 三处 STOP 按需阅读"；旧译中随上游移出的内联章节未保留，增量小节全部译出
- ship：VERSION/CHANGELOG 提交时序改为留给 Step 16 `finish` 收尾（本轮会话中途上游又推 e85005482add，已按 unified diff 定点跟进；同批 verbatim 13 件自动刷新）
- learn：改表驱动模式表（show/search/stats/export/add/prune），version 1.1.0
- health：Step 1 改 `gstack-checks detect --for health` 检测器，新增 DIMENSION 行解析、127 退出码语义、GBrain 三读数
- retro：新增 Question Tuning 与 Step 7.5 工厂记分卡、FRICTION 指标

## 机械校验（全量）

- **代码块**：13/13 文件全部围栏块（含嵌套缩进围栏）与上游 HEAD（e85005482add）逐字节一致
- **frontmatter**：13/13 键结构与源一致，`name`/triggers/gbrain（含 render_as 模板串）逐字节原样，仅 `description` 译中文
- **声明块**：13/13 三行逐字、翻译日期与同步状态更新为 2026-11-03
- **lint_zh_style**：初检 2 件 H1 破折号超标（office-hours 4.39、spec 3.71/千字），两轮定点改写（定义式「——」改冒号、标题改括注、修辞性保留）后 **0 信号**
- **工单销单**：sync_daily 复跑，13 项全部因声明块同步日期 ≥ first_seen 而解除；STATUS 回到「待重译：无」

## 过程事件

- **design-review D<N> 模板回退**：翻译代理将 impeccable 安装提议的 D<N> 简报模板按"口号本地化试点"方式译出；因试点未推广（README 明确其他上游暂保持纯翻译版），父会话将该代码块还原为上游逐字节版本。教训：**试点批次未推广前，代码块逐字节原则无条件适用**。
- **gstack 上游当日三连更**：82db89ab（工单成因）→ 8965b915（重译基底）→ e85005482add（ship SKILL.md 再变）。重译完成后以 diff 定点跟进，最终与 HEAD 对齐。
- 平台并发限制同前批，10 组代理分 4 波派发。
