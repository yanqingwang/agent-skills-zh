> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/light--project-proposal/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 12-project-proposal（项目提案）

## 风格概览

浅灰蓝配深蓝与金的专业配色，适合项目启动、商业提案、方案演示等专业场合

- **场景**：项目启动、商业提案、方案演示、投标演示
- **气质**：专业、可信、高效、严谨
- **色调**：冷色、低饱和、商务灰蓝
- **行业**：咨询服务、科技公司、金融投资、政府项目

## 配色

| 名称           | Hex     | 用途           |
| -------------- | ------- | -------------- |
| Background     | #E8EEF4 | background     |
| Primary        | #1E3A5F | primary        |
| Secondary      | #D4A84B | secondary      |
| Accent         | #3498DB | accent         |
| Dark           | #2C3E50 | dark           |
| Primary Text   | #2C3E50 | text_primary   |
| Secondary Text | #666666 | text_secondary |
| Muted Text     | #95A5A6 | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial           |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial           |

## 设计手法

- 浅灰蓝配深蓝与金的专业配色
- 专业文档式版式
- 信息卡片展示
- 数据可视化图表
- 横向时间轴
- Morph 切换动画
- 风险分析展示
- 已修复坐标冲突
- 增强内容卡的视觉层级

## 页面结构（8 页）

| 页码  | 类型       | 元素数量 | 描述                                                         |
| ----- | ---------- | -------- | ------------------------------------------------------------ |
| S1    | cover      | 29       | 封面页：项目标题 + 提案信息 + 左侧装饰                        |
| S2    | background | 33       | 背景页：三张痛点卡片 + 市场分析                              |
| S3    | solution   | 24       | 方案页：解决方案 + 策略卡片                                  |
| S4    | timeline   | 24       | 时间轴页：横向里程碑 + 节点卡片                              |
| S5    | budget     | 16       | 预算页：饼图 + 预算分配卡片                                  |
| S6    | team       | 24       | 团队页：成员卡片 + 联系方式                                  |
| S7    | risks      | 32       | 风险页：四类风险分析卡片                                     |
| S8    | thanks     | 16       | 致谢页：感谢 + 联系方式                                      |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 4（timeline）**：时间轴页，横向里程碑 + 节点卡片

不必通读，浏览 2-3 个代表页即可。
