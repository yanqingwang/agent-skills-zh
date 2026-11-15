> **中文汉化版** · 上游：[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) · 原文件：`skills/creator/video/video-shotcraft/template/THEMES.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 视觉主题与配色编辑

在现有左侧边栏中打开 **主题 (Themes)** 标签页。上半部分用于选择预设；下半部分通过取色器或六位 HEX 值编辑背景、卡片表面、正文文本、次级文本、强调色、淡色填充与边框颜色。按 Enter 或移出 HEX 输入框即可应用，无效输入会被丢弃。

预设：Ink Press、Modern Light、Midnight、Sage、Coral、Iris、Deep Ocean、Obsidian Violet 和 Vintage Kraft。Sage、Coral 和 Iris 取代了此前的明亮实验配色，改用浅色表面与克制的强调色。它们既有的 ID（`solar-pop`、`coral-burst`、`color-play`）与已保存的项目保持兼容。Coral 的中性表面 / 深紫罗兰文本 / 珊瑚色强调这一方向参考了 [Happy Hues](https://www.happyhues.co/)；数值针对本 fixture 做了适配，并非对完整站点的精确复制。

- `themeId` 与可选的 `themeColors` 存储在项目 JSON 和浏览器保存中。更改支持撤销/重做。一次连续的取色器拖动只生成一步撤销记录，并保持当前片段处于选中状态。
- 选择其他预设会清除配色覆盖；**恢复预设** 只清除当前预设的覆盖。显式的逐片段编辑保持不变且优先级更高。
- Ink Press 保留其原始光栅截图，没有配色编辑器。选择其他预设即可同时给影片和它的演示 UI 素材重新上色。
- 可编辑预设保留报告页眉横带中的周报标题，并在底部附近使用紧凑的 36px 字幕。显式的逐片段文本、字号和位置编辑仍然优先。
- 主题作用于适配后的模板场景。普通 Gallery 卡片和编辑器自身的界面外观不会被全局重新上色。
- 没有主题标记的旧项目会被规范化一次；迁移之后，显式编辑永远不会被推断或丢弃。

## 单一配色来源

`src/themes/palettes.json` 为每个可编辑预设定义七种语义色。场景适配器和 `themes/ui.cjs` 都读取它。要新增一个使用同一 fixture 的预设，只需添加配色、其类型 ID 和一个 manifest 标签，无需复制场景树。

`src/themes/palette-assets.json` 包含五个可信的序列化演示页面和 27 条裁剪定义。运行时 SVG 素材用 `foreignObject` 和经过校验的 HEX 变量嵌入这些标记。预览和视频导出使用同一个渲染器，并带有有界缓存。编辑颜色不会调用截图服务，也不会用滤镜给像素重新上色。第三方截图仍需要单独适配的源。

修改 fixture 标记或几何结构后，在 `template/` 下运行 `node scripts/build-palette-assets.cjs`。它在开发环境中需要 Playwright。`SHOTCRAFT_PLAYWRIGHT` 和 `SHOTCRAFT_BROWSER` 可以指定现有的模块和 Chromium 可执行文件。编译后的 JSON 已提交入库，最终用户不需要这些工具。

manifest 的可选新增项是 `themes[].palette` 与 `paletteProp`，与 `themes`、`defaultTheme`、`themeProp` 以及每个单元的 `themeKey` 并列。props 的解析顺序为 schema 默认值 → 预设默认值 → 项目配色 → 显式片段编辑。不支持配色的 manifest 保持原有行为。

## 直接渲染

现有的 `AiflPromo` composition 接受 `theme` 和可选的 `colors`：

```json
{"theme":"coral-burst","colors":{"accent":"#2459ad","surface":"#e1ecff"}}
```

把它保存为 props JSON 并传给 `npm run render -- --props=<file>`。Workbench 导出则携带 `project.themeId` 和 `project.themeColors`。缺失或未知的预设 ID 回退到 Ink Press。

## 验证与来源

在 `workbench/` 和 `template/` 都安装依赖后，从 `workbench/` 运行 `npm run test:themes` 和 `npx tsc --noEmit`，并从 `template/` 运行 `npx tsc --noEmit`。测试覆盖自定义配色的校验与优先级、重置、编辑保留、旧版存档、无主题项目、配色历史、周报文案保留、字幕默认值，以及光/强调/阴影三种角色的分离。浏览器/导出验证结果记录在 PR #80。

该 fixture 描述的是一个虚构的研究工作区，不是已连接的服务，也不是真实的研究结果。原始素材保留其既有的署名/授权条款；新的 fixture 代码与衍生素材使用本仓库的 Apache-2.0 License。

## 保存、导入与导出配色

给配色命名并点击 **保存配色**，即可加入 **我的主题**。这些条目存放在当前浏览器的本地存储中，按当前 manifest 名称区分（最多 50 条）；它们与项目时间线相互独立。点击条目即可应用，点击其 × 按钮则移除。导出 JSON 文件可用于备份或迁移到其他浏览器。

**导入配色** 接受本面板导出的 version-1 `shotcraft-palette` JSON，校验兼容的基础主题与完整的 HEX 字段，然后应用它且不改动时间线编辑。之后点击保存即可把导入的配色加入我的主题。任意配色网站的 JSON schema 暂不支持。**导出配色** 会下载当前配色、名称和基础主题 ID。Vintage Kraft（`vintage-kraft`）在其配色被保存或导入时保留程序化纸纹理。
