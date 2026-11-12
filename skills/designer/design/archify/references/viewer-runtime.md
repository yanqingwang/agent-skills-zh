> **中文汉化版** · 上游：[tt-a1i/archify](https://github.com/tt-a1i/archify) · 原文件：`archify/references/viewer-runtime.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Viewer 运行时参考（Viewer Runtime reference）

只有当用户要求面向阅读者的能力时才读本文件。普通生成不需要实现或重新记录这些特性；它们已经内置在生成的 HTML 里。

## 探索（Exploration）

- Diagram Guide（图表指南）列出当前可用的操作与快捷键。用指南按钮或 `?` 打开；它从不自动弹出。
- Reading Depth（阅读深度）在默认 100% 缩放下从 READ 开始，175% 时揭示 FULL 细节，低于 100% 才回退到 MAP。Focus、route 与语义交互在任何缩放下都会揭示其确切事实。
- Semantic Lens（语义透镜）汇总选中的节点/关系类别，不改变已绘制的几何。
- Intent Trace（意图追踪）在提交聚焦之前预览细指针或键盘目标。
- Node Finder（节点查找器）按标签和稳定 ID 搜索。
- Semantic Passport（语义护照）在聚焦时打开，展示已绘制的上游/下游事实，支持可复制的深链接，有明确的关闭操作，在真正的外部激活和 Escape 时关闭，并且从不进入规范导出。
- Semantic Radar（语义雷达）镜像可见视口与已绘制的图，但不会成为第二个事实来源。
- Direct Relationship Pin（直接关系钉选）让唯一编译出的关系可操作，同时保留已绘制的线条和稳定的关系身份。对冲突的 source/target/label/ID 元数据必须失败即拒绝（fail-closed）。
- Route Probe（路径探针）只在已绘制的有向关系上解析恰好两个端点。它从不从几何形状推断路径。

## 内嵌阅读地址（Embedded reading addresses）

宿主页面在一个不透明 `srcdoc` 框架中展示原生阅读器时，可以在该阅读器的 `html` 元素上设置 `data-reading-link-template`。提供一个绝对 HTTP、HTTPS 或 file URL，其中恰好包含一个 `{state}` 标记，例如 `https://example.test/architecture#page=mechanism&reader={state}`。原生 Focus、Relationship、Reach、Route 和 Lens 的复制动作会把该标记替换为其百分比编码的不透明查询状态。宿主保持自己的页面身份，并把该值恢复为原生框架的 hash；它从不解析或重构查询。

未配置时保留独立链接。无效、带凭证或不受支持的 URL 模板让复制失败，且不触碰剪贴板。这个接缝只改变复制出来的地址，不改变查询解析、历史、权限、嵌入隔离或已绘制几何。它不新增任何网络或存储面。

## 动效与呈现（Motion and presentation）

每张渲染出的图默认启用由阅读者控制的 Live/Still 动效。Live 下，每条边在同一个共享周期上运行小型灯光秀：一颗彗星（辉光、光晕、尾巴、头部，外加每条边上更暗的回声）向下游级联，留下柔和的尾迹，最后以涟漪形式落在目标节点上；节点按绘制步骤错峰进入一次，之后在同一周期上发光。相位遵循绘制的步骤顺序（源节点层级；时序图中按时间先后）；流动效果运行在独立的 Viewer 覆盖层上，原始线型和箭头保持不变。紧凑的边得到更大更亮的彗星；回声保持更暗。没有已保存偏好时，新页面从 Still 开始。选择 Live 会启动持续流动并保存该偏好；选择 Still 会停止流动并清除已保存的 Live 偏好。已保存的 Still 偏好保持 Still。语义探索临时占用动效预算，该动作释放后持续流动恢复。没有连线的图保留其有界节点入场动画，不会凭空发明流动。省略 `meta.animation`；历史上的 `"trace"` 与 `"none"` 值仍为输入兼容而接受，且不改变此默认。减少动态、页面隐藏、打印与规范导出都保留完整的静态含义。Presentation Stage（演示舞台）只改变查看器外壳与取景，从不改变已绘制几何。这不是移动端产品特性；窄布局只做收容。

## 规范导出（Canonical exports）

导出菜单可以复制/下载整图 PNG、下载 JPEG/WebP、下载双主题 SVG，以及录制启用轨迹的 WebM。Viewer 状态，包括 Guide、Lens、查找器、聚焦、路径、相机、雷达、演示、动效占用与临时覆盖层，必须从规范导出中移除。

打开、关闭或完成导出会保留活动的 Focus/Reach 选择以便继续探索。导出拥有的下载激活不算外部关闭；真正的外部激活与 Escape 保持既有行为。整图 PNG/SVG 导出仍包含完整的规范图，而 Reach Share Card 传达的是活动的已绘制闭包。

### Route Share Card（路径分享卡）

真实的定向 Route Probe 解析完成后，阅读者可以使用 **Export → Route Share Card**。它复用完全一致的有序路径快照和共享的 Share Card 接缝：`format=share-card`、`variant=route`。隔离克隆只允许使用静态 `data-share-route-*` 装饰。它只支持下载，对过期/不可达/冲突的路径失败即拒绝，并且永远不会成为规范产物。

### Reach Share Card（可达分享卡）

非空的已绘制可达性查询完成后，阅读者可以使用 **Export → Reach Share Card**。它消费已解析的上游/下游节点与边集合，不重新运行遍历：`format=share-card`、`variant=reach`。隔离克隆只允许使用静态 `data-share-reach-*` 装饰。它只支持下载。称之为"已绘制可达性"，不要叫影响、波及半径、破坏或运行时因果。

## 真实性边界（Truth boundary）

Viewer 导出是沟通资产。它们不能替代已检查的 HTML、确定性的交付回执或真实的目视审查。不要为这些仅属于 Viewer 的能力添加托管服务、存储面、依赖、schema 分支或移动端产品面。
