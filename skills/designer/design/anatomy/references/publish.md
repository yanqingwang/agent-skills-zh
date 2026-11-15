> **中文汉化版** · 上游：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) · 原文件：`references/publish.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 把图发布到社区图库

社区图库是仓库 `wheresryan22/anatomy-community`。人们在那里分享纯 HTML 图：一个构建脚本在自身旁边写出独立页面，与本 skill 的示例一致，主题不限。React 与 Next.js 的图不能提交。

只有当用户要求分享或发布某个图时才发布。没有得到他们明确的同意，绝不发送任何东西。

## 步骤

1. **确认图已完成。** 页面已构建且是最新的，线条检查通过，含管道、线缆或圆形部件时 `--audit` 通过，开启 reduced motion 后它能保持一个静止姿态。图库自己也会检查所有这些。
2. **向用户索要只有他们能提供的东西：**
   - 他们的 GitHub 用户名（作者）；`gh api user --jq .login` 显示 GitHub CLI 当前登录的是谁；
   - 一个标题（不超过 80 字符）和一个简短的 kebab-case id；
   - 许可证：MIT（默认）或 CC-BY-4.0；
   - 确认这是他们自己的作品且愿意分享。
   prompt 就是生成这幅图的那次请求；复用它，截到 600 字符。
3. **在本地克隆图库**（如果他们还没有）：`gh repo clone wheresryan22/anatomy-community -- --single-branch`（只要 `main`：previews 分支存放所有图片，体积会很大）。克隆主仓库没关系：提交步骤会在需要时为他们创建 fork。
4. **展示计划，** 什么都不执行：
   ```sh
   node <skill>/scripts/publish.mjs <figure folder> --into <clone> --id <kebab-id> \
     --title "..." --author <github user> --prompt "..." \
     [--agent "Claude Code"|OpenCode|Codex|Antigravity|Other] --model "..." [--minutes 45] [--tokens 1.2M] \
     [--license MIT|CC-BY-4.0] \
     [--tags a,b] [--audit] [--pages a.html,b.html] --submit --dry-run
   ```
   `--agent` 传你正在运行的 agent，`--model` 传你所用的模型（图库要求提供，如 `claude-opus-5-5` 或 `gpt-5-codex`）。在 Claude Code 里，制作耗时与 token 消耗会自动从本会话日志读取：从生成该图的请求到发布它的请求，剔除超过 10 分钟的空闲间隔，缓存读取不计入。在其他 agent 里，能看到自己会话用量时传 `--minutes` 与 `--tokens`；看不到就省略这两个参数，不要猜。把计划复述给用户：它会写明 fork（如有）、分支、新增的文件夹以及 pull request 去向。
5. **只有用户说可以之后**，用 `--yes` 替换 `--dry-run` 运行同一条命令。它只把图的源码复制进 `figures/<author>/<id>/src/`，把 kit 导入指向克隆的 `.skill/` 链接，记录 kit 指纹，检查构建，把预览保存到 `shots/<author>-<id>/preview.png`，然后只提交该文件夹、推送并打开 pull request。把它打印出的链接交给用户。
   - 如果它报告某个文件越出了图文件夹与 skill 的范围，把该文件所需的内容复制进图文件夹，重新构建，再次发布。
   - 如果它无法判断哪些页面属于这个图，传 `--pages`。
   - 以后要发送更新版本时，加 `--force` 再运行；它会更新同一个 pull request。
6. **不带 `--submit`** 时，脚本在准备好文件夹后停下，改为打印 git 与 `gh` 命令；用户想自己发送时就用这种方式。

没有终端的人也可以通过图库的 **Submit a figure** issue 表单提交，附上一个存有图源码的 GitHub Gist 链接。

## 图库会拒绝的内容

- 网络调用或外部地址；
- `eval` 或 `new Function`；
- frame、cookie，或触及图周围页面的一切；
- skill、图自身文件以及 `node:fs`、`node:path`、`node:url`、`node:crypto`、`node:process` 之外的构建导入；
- 读取环境变量；
- `src/` 下源码文本之外的文件，或提交已构建的页面；
- 构建产物超出其页面，或两次运行结果不一致的构建；
- 开启 reduced motion 后仍在持续运动的图。

如果用户打算分享，从一开始就按这些规则写图。
