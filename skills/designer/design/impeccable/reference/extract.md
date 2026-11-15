> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/extract.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 提取流程（Extract Flow）

识别可复用的模式、组件与设计令牌（design token），然后把它们提取并整合进设计系统，供系统性复用。

## Step 1: 发现阶段的设计系统

找到设计系统、组件库或共享 UI 目录。理解其结构：组件组织方式、命名惯例、设计令牌结构、导入/导出约定。

如果尚无设计系统，先不要创建。用 AskUserQuestion 工具提问，等得到回答后再继续。先弄清偏好的位置与结构。

## Step 2: 识别模式

在目标区域寻找可提取的机会：

- **Repeated components**: 相似 UI 模式被使用 3 次以上（按钮、卡片、输入框）
- **Hard-coded values**: 应当变成令牌的颜色、间距、字体、阴影
- **Inconsistent variations**: 同一概念的多个不同实现
- **Composition patterns**: 反复出现的布局或交互模式（表单行、工具栏分组、空状态）
- **Type styles**: 重复出现的字号 + 字重 + 行高组合
- **Animation patterns**: 重复出现的缓动、时长或关键帧组合

评估价值：只提取以相同意图被使用 3 次以上的东西。过早抽象比重复更糟。

## Step 3: 规划提取

制定一个系统性的计划：

- **Components to extract**: 哪些 UI 元素要变成可复用组件？
- **Tokens to create**: 哪些硬编码值要变成设计令牌？
- **Variants to support**: 每个组件需要支持哪些变体？
- **Naming conventions**: 与现有模式一致的组件名、令牌名、prop 名
- **Migration path**: 如何把既有用法重构为使用新的共享版本

设计系统是渐进生长的。提取现在就明确可复用的东西，而不是所有将来可能可复用的东西。

## Step 4: 提取与充实

构建改进过的、可复用的版本：

- **Components**: 清晰的 props API 与合理的默认值、面向不同用例的恰当变体、内建无障碍支持（ARIA、键盘导航、焦点管理）、文档与使用示例
- **Design tokens**: 清晰的命名（primitive 与 semantic 之分）、合理的层级与组织、说明每个令牌何时使用
- **Patterns**: 何时使用该模式、代码示例、变体与组合

## Step 5: 迁移

用新的共享版本替换既有用法：

- **Find all instances**: 搜索你提取的那些模式
- **Replace systematically**: 把每处用法更新为使用共享版本
- **Test thoroughly**: 确保视觉与功能对等
- **Delete dead code**: 删除旧实现

## Step 6: 文档化

更新设计系统文档：

- 把新组件加入组件库
- 记录令牌的用法与取值
- 添加示例与指南
- 更新 Storybook 或组件目录

**Avoid**:
- 提取未经泛化的一次性、上下文特定的实现
- 创建泛化到毫无用处的组件
- 不考虑既有设计系统约定就提取
- 跳过恰当的 TypeScript 类型或 prop 文档
- 为每一个单独的值创建令牌（令牌应当有语义含义）
- 提取意图不同的东西（两个按钮看起来相似但用途不同，就应保持分离）
