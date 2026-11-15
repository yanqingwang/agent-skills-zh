> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/shell.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Shell 语言提示词片段

## 核心概念

- **Shebang 行**：`#!/bin/bash` 或 `#!/usr/bin/env bash` 指定解释器
- **变量**：`VAR=value` 赋值，`$VAR` 或 `${VAR}` 展开，`=` 两边不能有空格
- **函数**：`function name()` 或 `name()` 定义可复用的命令组
- **条件**：`if [[ condition ]]; then ... fi`，用 `[[ ]]` 做扩展测试
- **循环**：`for item in list`、`while condition`、`until condition` 迭代模式
- **管道与重定向**：`|` 串接命令，`>` / `>>` / `2>&1` 重定向输出
- **退出码**：`$?` 捕获上一条命令的状态，`set -e` 在任何失败时退出
- **严格模式**：`set -euo pipefail` 实现健壮的错误处理（出错即退、未定义变量报错、管道失败即退）
- **命令替换**：`$(command)` 把命令输出捕获为字符串
- **Here 文档**：`<<EOF ... EOF` 向命令提供多行字符串输入

## 重要文件模式

- `*.sh` / `*.bash`：Shell 脚本文件
- `scripts/*.sh`：项目自动化脚本（构建、部署、初始化）
- `entrypoint.sh`：Docker 容器入口脚本
- `install.sh` / `setup.sh`：环境初始化脚本
- `.bashrc` / `.bash_profile` / `.zshrc`：Shell 配置文件

## 边模式

- Shell 脚本对其调用的其他脚本或构建过程建立 `triggers` 边
- 入口脚本对其启动的应用建立 `deploys` 边
- 初始化脚本对开发环境建立 `configures` 边
- 构建脚本对其编译或打包的源文件建立 `depends_on` 边

## 摘要风格

> "构建自动化脚本：编译 TypeScript、运行测试并打包发布产物。"
> "Docker 入口脚本：处理信号转发与优雅停机。"
> "环境初始化脚本：安装依赖并配置开发工具。"
