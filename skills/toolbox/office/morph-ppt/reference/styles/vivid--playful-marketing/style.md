> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/vivid--playful-marketing/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 03-playful-marketing（青春活力营销）

## 风格概览

珊瑚橙、亮黄与薄荷绿的色彩碰撞，配大色块和斜向分割版式，适合营销活动、新品发布、促销活动等面向年轻人的场合。

- **场景**：营销活动、品牌发布、新品推广、促销活动
- **气质**：年轻、有活力、热情、有创意、大胆
- **基调**：暖色调、高饱和、高对比
- **行业**：消费品、电商、娱乐、教育、餐饮

## 配色

| 名称           | Hex     | 用途           |
| -------------- | ------- | -------------- |
| Background     | #FFFFFF | background     |
| Primary        | #FF6B6B | primary        |
| Secondary      | #FFE66D | secondary      |
| Accent         | #4ECDC4 | accent         |
| Dark           | #2C2C54 | dark           |
| Text Primary   | #2C2C54 | text_primary   |
| Text Secondary | #666666 | text_secondary |
| Text Muted     | #999999 | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial Black     |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial Black     |

## 设计手法

- 珊瑚橙、亮黄、薄荷绿的色彩碰撞
- 大色块拼装版式
- 斜向分割设计
- 动感活泼的布局
- 高对比设计
- Morph 切换动画
- 已修复坐标冲突

## 页面结构（6 页）

| 页码  | 类型      | 元素数量 | 描述                                                           |
| ----- | --------- | -------- | -------------------------------------------------------------- |
| S1    | hero      | 50       | 封面页：左侧大色块 + 右侧内容卡                                |
| S2    | statement | 45       | 宣言页：中心内容 + 数据卡片                                    |
| S3    | product   | 50       | 产品页：左图右文版式                                           |
| S4    | grid      | 55       | 网格页：2x3 卡片网格                                           |
| S5    | quote     | 40       | 引言页：大引号 + 四周见证语                                    |
| S6    | cta       | 40       | CTA 页：顶部大色块 + 底部行动区                                |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1（hero）**：封面页，左侧大色块 + 右侧内容卡

不必通读，浏览 2-3 个代表页即可。
