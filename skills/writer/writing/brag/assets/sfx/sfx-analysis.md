> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/writer/writing/brag/assets/sfx/sfx-analysis.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 音效分析摘要

来源：[Kenney](https://kenney.nl/)。

把这份文件当作挑选有品味精效的规划参考。打磨过的视频优先用低/中高频风险的声音；明亮/高风险的文件留给极小的点缀、混乱基调或刻意为之的故障效果。

## 信号说明

- `brightness`：warm / balanced / bright，基于频谱质心和高频能量。
- `highFrequencyRisk`：low / medium / high。高风险音效听感可能尖锐、带嘶声、有咔哒感，重复时容易疲劳。
- `brightBurden`：按响度和时长加权的高频能量。它把持续的玻璃质感鸣响与短促咔哒声区分开。
- `highActiveDuration`：明亮能量在有意义的水平上持续活跃多久。
- `envelopeShape`：transient / textured / continuous。连续的明亮声音比稀疏的质感声音更容易造成疲劳。
- `transient.sharpness`：数值越高，听感越咔哒、越打击乐。
- `duration`：短声音适合 UI 和打字；长声音适合揭示和转场。

## 最安全的通用之选

- `impact/impactSoft_medium_001.ogg`：0.18s, warm, low HF risk, transient；用于硬转场、重大揭示
- `impact/impactSoft_medium_004.ogg`：0.15s, warm, low HF risk, transient；用于硬转场、重大揭示
- `impact/impactSoft_medium_002.ogg`：0.14s, warm, low HF risk, transient；用于硬转场、重大揭示
- `interface/bong_001.ogg`：0.12s, warm, low HF risk, textured；用于一般点缀
- `impact/impactSoft_medium_003.ogg`：0.14s, warm, low HF risk, textured；用于硬转场、重大揭示
- `impact/impactSoft_medium_000.ogg`：0.12s, warm, low HF risk, textured；用于硬转场、重大揭示
- `interface/click_003.ogg`：0.01s, balanced, low HF risk, continuous；用于按钮按下、选择、模拟用户操作
- `interface/click_002.ogg`：0.01s, balanced, low HF risk, continuous；用于按钮按下、选择、模拟用户操作
- `interface/click_005.ogg`：0.01s, balanced, low HF risk, continuous；用于按钮按下、选择、模拟用户操作
- `ui/click2.ogg`：0.06s, balanced, low HF risk, continuous；用于按钮按下、选择、模拟用户操作
- `ui/rollover2.ogg`：0.06s, balanced, low HF risk, continuous；用于一般点缀
- `interface/glitch_002.ogg`：0.03s, bright, low HF risk, continuous；用于混乱点缀、喜剧式打断，仅限极小点缀
- `impact/impactSoft_heavy_003.ogg`：0.54s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/impactSoft_heavy_004.ogg`：0.50s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/impactSoft_heavy_002.ogg`：0.57s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/impactSoft_heavy_001.ogg`：0.57s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/impactSoft_heavy_000.ogg`：0.51s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/footstep_wood_004.ogg`：0.25s, warm, medium HF risk, transient；用于一般点缀
- `impact/footstep_wood_002.ogg`：0.25s, warm, medium HF risk, transient；用于一般点缀
- `impact/footstep_wood_000.ogg`：0.25s, warm, medium HF risk, transient；用于一般点缀
- `impact/footstep_wood_001.ogg`：0.25s, warm, medium HF risk, transient；用于一般点缀
- `impact/impactWood_medium_003.ogg`：0.33s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/impactWood_medium_001.ogg`：0.33s, warm, medium HF risk, transient；用于硬转场、重大揭示
- `impact/impactWood_medium_000.ogg`：0.33s, warm, medium HF risk, transient；用于硬转场、重大揭示

## 按用例分组的低风险之选

- 按钮按下：`interface/click_003.ogg`（low）、`interface/click_002.ogg`（low）、`interface/click_005.ogg`（low）、`ui/click2.ogg`（low）、`interface/click_001.ogg`（medium）
- 选择：`interface/click_003.ogg`（low）、`interface/click_002.ogg`（low）、`interface/click_005.ogg`（low）、`ui/click2.ogg`（low）、`interface/click_001.ogg`（medium）
- 开关切换：`interface/switch_007.ogg`（medium）、`interface/switch_002.ogg`（medium）、`interface/switch_006.ogg`（medium）、`interface/switch_005.ogg`（medium）、`ui/switch11.ogg`（medium）
- 卡牌揭示：`casino/card-slide-1.ogg`（medium）、`casino/card-place-1.ogg`（high）、`casino/card-fan-2.ogg`（high）、`casino/card-slide-8.ogg`（high）、`casino/card-slide-3.ogg`（high）
- 滑动：`casino/card-slide-1.ogg`（medium）、`casino/card-place-1.ogg`（high）、`casino/card-fan-2.ogg`（high）、`casino/card-slide-8.ogg`（high）、`casino/card-slide-3.ogg`（high）
- 逐项出现：`casino/card-slide-1.ogg`（medium）、`casino/card-place-1.ogg`（high）、`casino/card-fan-2.ogg`（high）、`casino/card-slide-8.ogg`（high）、`casino/card-slide-3.ogg`（high）
- 面板打开：`casino/cards-pack-open-1.ogg`（high）、`casino/cards-pack-open-2.ogg`（high）
- 柔和揭示：`casino/cards-pack-open-1.ogg`（high）、`casino/cards-pack-open-2.ogg`（high）
- 成功：`impact/impactBell_heavy_000.ogg`（medium）、`impact/impactBell_heavy_003.ogg`（medium）、`impact/impactBell_heavy_004.ogg`（medium）
- logo 落定：`impact/impactBell_heavy_000.ogg`（medium）、`impact/impactBell_heavy_003.ogg`（medium）、`impact/impactBell_heavy_004.ogg`（medium）
- 揭示确认：`impact/impactBell_heavy_000.ogg`（medium）、`impact/impactBell_heavy_003.ogg`（medium）、`impact/impactBell_heavy_004.ogg`（medium）
- 重大揭示：`impact/impactSoft_medium_001.ogg`（low）、`impact/impactSoft_medium_004.ogg`（low）、`impact/impactSoft_medium_002.ogg`（low）、`impact/impactSoft_medium_003.ogg`（low）、`impact/impactSoft_medium_000.ogg`（low）
- 硬转场：`impact/impactSoft_medium_001.ogg`（low）、`impact/impactSoft_medium_004.ogg`（low）、`impact/impactSoft_medium_002.ogg`（low）、`impact/impactSoft_medium_003.ogg`（low）、`impact/impactSoft_medium_000.ogg`（low）
- 混乱点缀：`interface/glitch_002.ogg`（low）、`interface/error_005.ogg`（medium）、`interface/error_006.ogg`（medium）、`interface/glitch_004.ogg`（medium）

## 家族概览

- `casino/`：51 个文件；HF 风险 low/medium/high = 0/10/41；平均高频能量 0.59
- `impact/`：109 个文件；HF 风险 low/medium/high = 5/104/0；平均高频能量 0.08
- `interface/`：20 个文件；HF 风险 low/medium/high = 5/14/1；平均高频能量 0.25
- `ui/`：48 个文件；HF 风险 low/medium/high = 2/14/32；平均高频能量 0.57

## 选择规则

- 重复的 UI 动作、文字节奏点和密集序列，优先用低风险音效。
- 孤立的揭示，或动效需要干净利落的边缘时，用中风险音效。
- 重复的节奏点、长序列、polished/deadpan 基调，避免高风险音效。
- 连续型明亮音效比稀疏/质感型明亮音效更致疲劳，按此对待。
- 如果用明亮音效，保持短促、轻声、孤立。
- 音效时点匹配视觉落定或视觉起始，取决于手势：点击对准按下/开始，揭示对准落定/收获时刻。
