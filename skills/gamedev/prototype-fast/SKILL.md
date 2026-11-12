---
name: prototype-fast
description: >
  用大约一小时搭出一个用完即弃、可试玩的原型，用来回答一个问题，通常是“这个机制好玩吗？”：
  一份只问一个问题的简报、一个 greybox、一个调试 HUD、一次试玩，以及 keep、kill 或 retune
  的结论。适用于“做个原型”、“先弄出个能玩的东西”，或判断原型代码是否保留。不适用于限时
  jam（`game-jam`）或关卡白模（`level-design`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/workflows/prototype-fast/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 快速原型

让一个机制尽快变得可玩，以此判断它值不值得正式开发。产出是写进仓库里的一份**决策**（keep、kill 或 retune），而不是产品。Agent 撰写 brief、搭出能回答该问题的最小东西、给它装好调试仪表，然后请用户试玩；由用户的反馈来定夺。

## 何时使用

- 验证某一个机制或“如果……会怎样”，快速切出一小段交互，或在投入真正的时间之前先降低想法的风险。

**不适用于：** 有截止时间和提交要求的 jam（`game-jam`）；关卡布局与白模（`level-design`）；发布上线（`steam-publish`、`itch-publish`）；已验证功能的正式生产版本（引擎或品类 Skill）。

## 工作流

1. **先写 brief**，放到 `prototypes/<idea>/BRIEF.md`（模式 1）并与用户确认：一个问题、核心动词、keep 与 kill 信号、一个时间盒。两个问题意味着两个原型；想一次测遍所有东西的原型什么也决定不了。
2. **默认用完即弃。** 把数值写死，一个文件也无妨，不做架构。只有当用户说代码以后会扩展时，才选可保留的结构，因为假装成生产代码的原型会烂进发布上线的代码库里。
3. **把它圈起来。** 在 `prototypes/<idea>/` 里构建（一个主游戏永不 import 的独立项目或文件夹），或放在用完即弃的分支上。
4. **除动词外，一切都用 greybox。** 方块、圆形、胶囊体、引擎默认字体，不加音频或只留一声调试提示音。问题不依赖的东西，一点功夫都别花。
5. **给问题装上仪表。** 画一个调试 HUD，显示被评判的数值（速度、跳跃高度、判定窗口、首次成功耗时），并把可调数值作为具名常量放在文件顶部，让 retune 只需改一行。
6. **先自己跑一遍**（验证），然后**请用户试玩**，不作任何解释，再请对方反馈：是否未经提示就做出了核心动词、花了多久、有没有重玩、哪里感觉不对。若有别人能试玩，就请用户观察他们并给出同样的反馈。
7. **对照 brief 做出结论**，把它追加到 `BRIEF.md`：keep（在真正的项目里安排重写）、kill（用一行写清学到了什么），或 retune（改一个常量再玩一次）。

## 模式

### 1. `BRIEF.md`


```text
QUESTION:   The one thing this must prove, ideally yes/no.
CORE VERB:  The single action the player repeats.
THROWAWAY:  yes (default) | no, because ...
TIMEBOX:    e.g. 60 min; stop when it ends, even if unfinished.
KEEP IF:    observable signal (see Pattern 3).
KILL IF:    observable signal.
RESULT:     <date> keep | kill | retune - evidence from the playtest
```


### 2. 只有动词是真实的（引擎无关的伪代码）


```text
const RUN_SPEED = 8.0, JUMP_VELOCITY = 12.0, GRAB_WINDOW = 0.15   # tune here

on update(dt):
    read_input()
    apply_core_mechanic(dt)                  # the only thing being tested
    draw_box(player)                         # a box, not a sprite
    draw_debug_hud(speed, airtime, window_hits, time_to_first_success)
    # enemies, menus, saves, audio, art: stubbed or absent
```


### 3. keep、kill 或 retune


```text
KEEP when, with placeholder art:
  - a fresh player does the core verb on purpose within about 30 s, unprompted, and
  - they replay the loop without being asked.
KILL when:
  - the verb only feels good after it is explained, or
  - making it fun needs systems far beyond the prototype, or
  - art or levels are being added to avoid admitting the verb is flat.
RETUNE when one value is clearly off (too slow, window too tight): change it, play again.
```


## 验证

把原型交给用户之前，先自己跑完这些检查：

1. 能从命令行启动（引擎的运行或 headless 命令，或 `127.0.0.1` 上的本地 web 服务器），日志或控制台没有报错。
2. 循环能跑完：开始、执行动词、成功或失败、重开。在引擎允许的情况下，用脚本化输入或一段简短的自动运行来驱动；否则自己玩一遍。
3. 调试 HUD 会显示 brief 里点名的数值，且它们按预期变化。
4. `git status`（或搜索 import）显示 `prototypes/<idea>/` 之外没有任何改动，且主游戏没有 import 它。
5. 用户试玩之后，`BRIEF.md` 里有一行 RESULT。

## 易踩的坑

- **过早打磨。** 美术、菜单和音频会让平淡的动词显得已经完成，反而拖慢结论。
- **没有 kill 判据。** 不写下“满足什么就 kill”，每个原型都“有潜力”，结果一个都砍不掉。在谁都还没对代码产生感情之前，先把信号定下来。
- **做成了系统，而不是机制。** 背包、存档和设置都不是要回答的问题。给它们留个 stub 即可。
- **spike 变成了产品。** keep 授权的是在真正的项目里重写，而不是把原型代码连同它的假设直接复制粘贴过去。
- **在真实代码库里做原型。** 它会把实验和发布上线的系统缠在一起，让这段 spike 难以删除。
- **只有作者自己试玩。** 作者清楚操作和意图。一个未经指导的玩家两分钟里暴露的问题，胜过一小时自玩，所以始终请用户给出反馈，而不是自己下判断。

## 相关 Skill

- `game-jam`：有截止时间和提交要求时，同样这套范围纪律。
- `level-design`：当问题关乎关卡布局而非机制时。
- `game-feel`：手感打磨（juice），只在动词被验证之后才做。
- 引擎核心（`godot-gdscript`、`phaser-core`、`love2d-core`、`unity-csharp-scripting`，……）用于 greybox 本身，以及 keep 之后的重写。
