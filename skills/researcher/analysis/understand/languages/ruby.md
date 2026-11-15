> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/ruby.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Ruby 语言提示词片段

## 核心概念

- **Block/Proc/Lambda**：一等可调用对象：block 隐式，proc 与 lambda 显式
- **混入（include/extend）**：通过 module 在类之间共享行为，无需继承
- **元编程**：动态方法定义（`define_method`）与方法拦截（`method_missing`）
- **鸭子类型**：对象由它能做什么定义，而非它是什么类
- **DSL**：用 block 与元编程构建的领域专用语言（如 Rails 路由）
- **猴子补丁**：运行时重新打开已有类，添加或修改方法
- **Symbol**：不可变的驻留字符串（`:name`），用作标识符与哈希键
- **开放类**：任何类都可在程序任意位置重新打开并扩展
- **Enumerable 模块**：混入后为任何带 `each` 的类提供集合方法（map、select、reduce）

## 导入模式

- `require 'gem_name'`：加载 gem 或标准库模块
- `require_relative './file'`：加载相对当前文件目录的文件
- `load 'file.rb'`：加载并重新执行文件（与 require 不同，不缓存）
- `autoload :ClassName, 'path'`：首次引用时惰性加载常量

## 文件模式

- `Gemfile`：由 Bundler 管理的依赖声明
- `Rakefile`：任务定义（Ruby 的 make 等价物）
- `spec/`：RSpec 测试目录，遵循 `*_spec.rb` 约定
- `test/`：Minitest 目录，遵循 `test_*.rb` 或 `*_test.rb` 约定
- `config.ru`：Web 服务器的 Rack 应用入口
- `lib/`：按约定为主源码目录

## 常见框架

- **Rails**：遵循约定优于配置的全栈 Web 框架
- **Sinatra**：快速创建 Web 应用的极简 DSL
- **RSpec**：带表现力 DSL 的行为驱动测试框架
- **Sidekiq**：基于 Redis 队列的后台任务处理
- **Grape**：Ruby 的 REST API 微框架

## 示例语言说明

> 用 `method_missing` 把属性访问动态委托给被包装的模型对象。装饰器上
> 找不到方法时落到模型上，无需显式转发方法即提供透明委托。
>
> Rails 高度依赖约定优于配置：文件放在 `app/models/`、`app/controllers/`
> 等目录即决定行为，无需显式注册。
