> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/light--training-interactive/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 10-training-interactive（互动培训）

## 风格概览

优雅活泼的配色，适合企业培训、在线课程、知识分享等互动学习场合

- **场景**：企业培训、在线课程、知识分享、技能教学
- **气质**：学习感、互动、渐进、有活力、友好
- **色调**：暖色调、中等饱和、舒适护眼
- **行业**：教育、企业培训、人力资源、咨询

## 配色

| 名称           | Hex     | 用途           |
| -------------- | ------- | -------------- |
| Background     | #FFF9E6 | background     |
| Primary        | #FF6B6B | primary        |
| Secondary      | #4ECDC4 | secondary      |
| Accent         | #FFE66D | accent         |
| Dark           | #2D3436 | dark           |
| Primary Text   | #2D3436 | text_primary   |
| Secondary Text | #636E72 | text_secondary |
| Muted Text     | #B2BEC3 | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial Black     |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial Black     |

## 设计手法

- 浅黄护眼背景
- 互动问答元素
- 进度条指示
- 卡片式模块版式
- 友好的圆角设计
- Morph 切换动画

## 页面结构（7 页）

| 页码  | 类型       | 元素数量 | 描述                                                               |
| ----- | ---------- | -------- | ------------------------------------------------------------------ |
| S1    | cover      | 59       | 封面页：课程标题 + 讲师信息 + 日程                                  |
| S2    | objectives | 54       | 学习目标页：3 张目标卡片 + 进度指示                                 |
| S3    | content1   | 60       | 内容页 1：知识点讲解 + 图示                                         |
| S4    | content2   | 69       | 内容页 2：要点清单 + 图示                                           |
| S5    | content3   | 66       | 内容页 3：核心概念 + 小结                                           |
| S6    | practice   | 58       | 练习互动页：互动问答 + 选项                                         |
| S7    | summary    | 54       | 总结页：课程总结 + 下一步                                           |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1**：封面页，课程标题 + 讲师信息 + 日程

不必通读，浏览 2-3 个代表页即可。
