> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/dark--editorial-story/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 06-editorial-story（杂志编辑叙事）

## 风格概览

深蓝灰配红色强调的编辑杂志风，采用杂志网格 + 图文并排版式，适合叙事表达、品牌故事、杂志内容等场景

- **场景**：叙事表达、品牌故事、编辑杂志、内容发布
- **气质**：专业、叙事感、文艺、高级、媒体感
- **色调**：冷色调、低饱和、高对比
- **行业**：媒体、出版、广告、品牌

## 配色

| 名称           | Hex     | 用途           |
| -------------- | ------- | -------------- |
| Background     | #FFFFFF | background     |
| Primary        | #2C3E50 | primary        |
| Accent         | #E74C3C | accent         |
| Auxiliary      | #636E72 | secondary      |
| Primary Text   | #2C3E50 | text_primary   |
| Secondary Text | #666666 | text_secondary |
| Muted Text     | #999999 | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Georgia         |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial Black     |

## 设计手法

- 深蓝灰配红色强调的配色
- 杂志网格版式
- 图文并排设计
- 装饰性引号元素
- 期号标签设计
- Morph 切换动画
- 标准化装饰元素

## 页面结构（6 页）

| 页码  | 类型   | 元素数量 | 描述                                                      |
| ----- | ------ | -------- | --------------------------------------------------------- |
| S1    | hero   | 45       | 封面页：杂志封面版式 + 期号标签                           |
| S2    | story  | 50       | 故事页：左图右文版式                                      |
| S3    | quote  | 50       | 引言页：整页引言 + 装饰性引号                             |
| S4    | team   | 55       | 团队页：四宫格杂志版式                                    |
| S5    | data   | 50       | 数据页：左侧装饰 + 数据卡片                               |
| S6    | thanks | 45       | 致谢页：杂志封底风格                                      |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1（hero）**：封面页，杂志封面版式 + 期号标签

不必通读，浏览 2-3 个代表页即可。
