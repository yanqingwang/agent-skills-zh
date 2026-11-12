---
name: game-jam
description: >
  针对固定截止时间为 Game Jam 参赛作品做规划并发布上线：阅读赛事规则、按时间预算限定范围、
  维护一份删减清单，并在提交前检查构建。适用于 Ludum Dare、GMTK、Global
  Game Jam 或任意 itch.io 赛事、48 小时游戏，以及"我们进度落后了，该砍掉什么"的情形。
  不适用于无时限的实验（`prototype-fast`）或上传命令（`itch-publish`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/workflows/game-jam/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Game Jam

把一个主题和一个固定截止时间，变成一个已提交、可游玩的游戏。胜利条件是在赛事截止前把构建挂到赛事上，
而不是做出最初设想的那个游戏。Agent 把计划写进文件，先构建最小的循环，按计划删减，并自行运行构建检查；
用户决定创意、试玩构建并点击提交。

## 适用场景

- 参加限时 Jam、为 48 到 96 小时或一周的开发划定范围、决定为赶上截止时间该砍掉什么，或把 Jam 作品提交上去。

**不适用于：** 核心循环的引擎代码（如 `godot-2d-movement` 或 `phaser-core` 之类的引擎 Skill，或
`platformer` 之类的类型 Skill）；没有截止时间的实验（`prototype-fast`）；商业发行（`steam-publish`、
`itch-publish`）。

## 工作流

1. **在主题揭晓前拿到规则。** 向用户索要 Jam 页面 URL 并阅读（或让用户把规则粘贴过来）。在项目根目录的
   `JAM.md` 中记录：时长、主题揭晓时间、以 UTC 和用户本地时间表示的提交截止时间、组队与素材规则、生成式 AI
   规则、要求的平台、作品提交到哪里、评分期间是否锁定上传，以及给他人作品评分是否影响结果。上述每一项都曾
   让已完成的游戏被取消资格。周期性赛事的现行规则汇总在版本说明中；以实时页面为准。
2. **提前准备好规则允许的内容：** 一个能导出的空项目、输入处理、标题/结束画面的 stub、一条已成功运行过
   一次的导出命令，以及有授权的字体与 SFX 来源。第一天的时间太宝贵，不该花在这些事上。
3. **把主题浓缩成一句话。** 快速给出大约十个创意，再帮助用户敲定一个能套进
   *"你[verb]以实现[goal]，同时[constraint]。"* 的点子。如果一句话装不下，就说明它太大了。把它写进
   `JAM.md`。
4. **按时间划定范围。** 使用预算表（模式 1）：一个核心机制、一个钩子，其余全部放进 `JAM.md` 的延展清单。
5. **先做垂直切片：** 用基础图元实现开始、游玩、胜或负、重开。一个完整的小循环胜过半成品的大循环。
6. **对照时间线检查**（模式 2），在每个时间段边界进行。当循环进度落后时，按分级规则（模式 3）从延展
   清单中删减，并把删减记录到 `JAM.md`。
7. **把最后约 20% 的时间留给发布上线：** 导出、运行验证检查、截取截图、撰写页面。构建往往在最后几小时
   出问题。
8. **尽早提交，在允许期间再更新。** 在截止时间前很早就上传一个可运行的构建。截止之后，很多 Jam 会锁定
   上传，或只允许申报过的 bug 修复，因此截止时挂载的那个构建就是别人评分的对象。

## 模式

### 1. 按 Jam 时长划分范围预算（从截止时间倒推）


```text
              | 48-hour jam            | 72-96 hour jam        | 1-week jam
--------------|------------------------|-----------------------|------------------------
Core mechanic | 1, proven by hour 6    | 1-2                   | 2-3 interacting
Levels/content| 1 hand-made or gen'd   | 3-5                   | 8-12 + progression
Art           | placeholder/1 palette  | cohesive 1-artist set | themed set + UI
Audio         | 3-5 SFX + 1 loop       | SFX + 1-2 tracks      | adaptive music
SHIP BUFFER   | last 8-10 h            | last 12-16 h          | last full day
```


### 2. 48 小时时间线


```text
H0-2    Lock the one-sentence concept; name the core mechanic and win/lose.
H2-8    Core loop with primitives. Playable, no art.
H8-12   Sleep. Tired code is tomorrow's bug list.
H12-24  One level or encounter, tune difficulty, add the hook.
H24-30  Sleep; the user plays the build (and ideally one other person); cut what isn't landing.
H30-38  Art and audio pass, then juice (see `game-feel`).
H38-44  Feature freeze: fix only crashes and soft-locks.
H44-48  Export, Verify, screenshots, page, SUBMIT by about H46.
```


### 3. 功能分级


```text
For every feature, in order:
  1. Does the core loop work without it?  -> yes: stretch goal, not MVP.
  2. Would a player notice it missing?    -> no: cut it.
  3. Is it under 30 minutes of work?      -> no: defer past the ship buffer.
Under deadline pressure the default is CUT; it can return in a post-jam version.
```


### 4. `JAM.md` 骨架


```text
Jam: <name + URL>     Deadline: <UTC> / <local>     Upload lock: yes/no
Rules: team | assets | AI | platforms | submit where
Concept: You <verb> to <goal> while <constraint>.
MVP: <core mechanic>, <hook>, start/play/end/restart
Stretch (in cut order): ...
Cut log: <hour> cut <feature> because <reason>
```


## 验证

在提交前执行以下检查，针对导出的构建，而不是编辑器：

1. **从命令行导出**，使用引擎 Skill 的导出路径（例如 `godot-export` 或 `unity-build-pipeline`），
   并确认退出码为 0。
2. **干净路径测试。** 把导出物打成 zip，解压到项目之外的一个全新临时文件夹，并在那里启动（若是网页构建，
   则用 `127.0.0.1` 提供该文件夹，在无头浏览器中加载）。缺失的素材和错误的工作目录只会在这里暴露。
   查看日志或浏览器控制台中的报错。
3. **打包检查。** 列出 zip 内容：顶层应有可执行文件或 `index.html`，不含项目文件、编辑器目录或调试符号。
   对于 itch.io，运行 `itch-publish` 里的 `butler push
   --dry-run` 检查。
4. **规则检查。** 对照构建重读 `JAM.md` 中的规则块：平台、操作方式（如要求键盘和鼠标）、页面上的署名与
   素材授权、AI 规则。
5. **请用户** 把解压后的构建从头到尾玩一遍，从开始到重开，并报告任何软锁死；然后提交，确认作品出现在
   Jam 的作品列表页面。仅把游戏上传到游戏页面并不等于参赛。

## 常见陷阱

- **范围蔓延。** 如果到时间的第一个三分之一时循环还不可玩，立刻删减。
- **没有发布上线缓冲。** 导出、打包 zip 与撰写页面要花 1 到 3 小时，而且通常会暴露一个构建 bug。
  把截止时间当成比实际早两小时来对待。
- **提交到了页面，而不是赛事。** 在 itch.io 上，Jam 参赛作品是与 Jam 页面分开的一次独立提交。
- **截止后修补。** 在上传锁定的赛事里，被评分的是锁定的那个构建，在别处链接一个"修复版"构建可能让作品被
  取消资格。在允许修补的赛事里（Ludum Dare），只修 bug 并列出改动。
- **未经测试的导出。** "能在编辑器里跑"不等于"能在构建产物里跑"。
- **未授权或 AI 生成的素材。** 从网上抓取的音乐、字体或精灵图可能违反 Jam 规则，并影响后续分发；
  为每一项素材标注来源。各赛事的 AI 规则差异很大：有的直接取消含 AI 美术或音频的作品资格，另一些只要求
  你选择不参与相应评分类别。
- **在循环变好玩之前就打磨。** 打磨能放大乐趣，却无法创造乐趣。
- **截止时间时区。** 赛事以单一时区公布截止时间；GGJ 各站点使用本地时间。两者都记入 `JAM.md`。

## 参考资料

- `prototype-fast`：在把 Jam 时间投入某个机制之前，阅读它了解灰盒搭建以及"用完即弃还是保留"的抉择。
- `itch-publish`：当赛事在 itch.io 上举办时，阅读它了解页面、渠道与 `butler push`。

## 相关 Skill

- 引擎核心（`phaser-core`、`love2d-core`、`godot-gdscript` 等）与类型 Skill（`platformer`、
  `roguelike` 等）构建出 Jam 所围绕的核心循环。

## 版本说明

最后核实：2026-11-11。各届之间规则会变化；请阅读所参加那一届的实时页面。

- **Ludum Dare：** Compo 为单人、48 小时，全部内容须在活动期间制作，包含源代码。Jam 为 72 小时，可单人
  或组队，允许任意基础代码；使用第三方或旧素材意味着要退出对应的评比类别。每届赛事以一个 Submission
  Hour 收尾用于打包；移植可随后进行。允许使用 AI 工具，但只要生成器完成了大部分（约 90%）工作，作品就要
  退出相应类别。作品发布在 ldjam.com 上，并链接到托管在别处的构建。主办方已宣布 2028 年 10 月为最后一届
  计划内赛事。
- **GMTK Game Jam 2026**（itch.io，2026 年 7 月 22 日至 26 日）：可单人或组队；须能在 Windows 上运行，
  或在浏览器中用键盘或鼠标运行；在游戏内或页面上使用生成式 AI 制作美术或音频会取消作品资格。为期五天的
  评分期内上传会锁定，链接到另一个构建也会取消资格。网页上传器接受最大 1 GB 的文件；更大的构建需通过
  butler 上传。
- **Global Game Jam 2027：** 赛事周为 2027 年 1 月 25 日至 31 日；各站点按本地时间运行各自的 48 小时
  窗口与截止时间。团队自选授权协议，须上传可执行文件或浏览器链接；政策页面已不再要求源代码，但较旧的
  "Upload your game" 页面仍会要求，因此请核对你所在站点的规则。除既有的版权与 IP 政策外，对 AI 工具没有
  额外限制。
- 来源：[Ludum Dare 规则](https://ldjam.com/events/ludum-dare/rules)、
  [Ludum Dare AI 常见问题](https://ludumdare.com/resources/questions/can-i-use-ai)、
  [Ludum Dare 结束日期（Game Developer）](https://www.gamedeveloper.com/production/ludum-dare-will-officially-end-in-october-2028)、
  [GMTK Game Jam 2026](https://itch.io/jam/gmtk-jam-2026)、
  [GGJ 政策](https://globalgamejam.org/policies)、[GGJ 上传指南](https://globalgamejam.org/upload-your-game)、[GGJ](https://globalgamejam.org/)。
