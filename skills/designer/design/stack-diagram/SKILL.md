---
name: stack-diagram
description: "创建云架构风格的图表：技术栈、系统架构、基础设施布局和服务拓扑，配真实品牌 logo、分组容器和干净的正交箭头；交付形式为自包含 HTML、PNG 图片、React/TSX 组件或实时 artifact。只要用户要求 architecture / system / stack / infra diagram（架构图/系统图/技术栈图/基础设施图）、tech-stack overview（技术栈总览）、service topology（服务拓扑）、cloud-vendor-style diagram（云厂商风格图），或想把一组技术 logo 排成一张展示各服务如何连接的图，就使用本 Skill——无论用哪种语言提出，即使用户没说输出格式，即使涉及的工具不是云服务。"
license: MIT (see LICENSE); bundled fonts are SIL OFL 1.1
compatibility: Python 3.9+ and network access to fetch logos; PNG output also needs Playwright with Chromium
---

> **中文汉化版** · 上游：[caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram) · 原文件：`skills/stack-diagram/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# stack-diagram

生成工程制图风格的架构图：白色 tile 上放真实 logo，带标签的分组框（类似云厂商 VPC 图），带等宽字体标签的正交箭头，衬在清爽的坐标纸背景上。一个自包含 HTML 文件是唯一事实来源；PNG / TSX / artifact 都由它派生。

## 环境要求

- Python 3.9+（`fetch_icons.py`、`build.py` 和 `share.py` 只用标准库）
- 抓取图标时需要能访问图标源：svgl.app、raw.githubusercontent.com、cdn.jsdelivr.net、aws.amazon.com 和 d1.awsstatic.com（AWS 图标）、services.google.com（Google Cloud 图标）、learn.microsoft.com 和 arch-center.azureedge.net（Azure 图标），以及 `name=URL` 时品牌自己的站点或仓库
- `render_png.py` 需要 Playwright + Chromium：`pip install playwright && python3 -m playwright install --with-deps chromium`

## 工作流

1. 定下内容（节点、分组、连线）
2. 抓取图标 — `scripts/fetch_icons.py`
3. 规划坐标 — 读 `references/geometry.md`
4. 从 `assets/template.html` 构建 HTML — `scripts/build.py`
5. **渲染一张 PNG 并亲眼查看**，然后再交付
6. 按要求的格式交付
7. 可选：分享到公开画廊

## 第 1 步 — 内容

从用户给出的技术/服务清单里，确定：

- **节点**：每个技术 = 一个节点（名称 + 一个小写的简短角色，如 `http server`、`sqlite db`）
- **分组**：把共享同一运行时、厂商或仓库的东西框在一起（例如一个云厂商框里套一个运行时框；工具类用 monorepo 框）。嵌套一层没问题，再深就乱。分组标签按品牌自己的大小写写（`GitHub`、`npm`）；模板原样显示。
- **连线**，三种：
  - 强调色实线 = 主请求/数据流（一条连续路径最易读）
  - 中性实线 = 次要的内部连接
  - 中性虚线 = 开发期/部署期关系（CI、git hooks、IaC 部署）

如果用户只给了一份扁平的工具清单，就从工具本身的性质推断合理的分组和流向——只有当某个工具含糊到怎么画都会错时才提问。

## 第 2 步 — 图标

```bash
python3 scripts/fetch_icons.py <icons-dir> tanstack hono drizzle "betterauth:better-auth" "orpc=https://orpc.unnoq.com/logo.webp"
python3 scripts/fetch_icons.py <icons-dir> "aws:aws/AWS-Cloud-logo" "vpc:aws/vpc" "fargate:aws/fargate" "s3:aws/s3"
python3 scripts/fetch_icons.py <icons-dir> "gcp:google-cloud" "run:gcp/cloud-run" "lb:gcp/load-balancing" "sql:gcp/cloud-sql"
python3 scripts/fetch_icons.py <icons-dir> "azure:azure/Azure-A" "app:azure/app-service" "vnet:azure/vnet" "sql:azure/sql-database"
python3 scripts/fetch_icons.py <icons-dir> "k8s:kubernetes" "ing:k8s/ingress" "svc:k8s/service" "deploy:k8s/deployment" "pod:k8s/pod"
```

规格形式：`name`（名称即 slug）、`name:slug`（slug 不同）、`name=URL`（显式 URL）、`name:aws/<Name>`（官方 AWS 图标）、`name:gcp/<Product>`（官方 Google Cloud 图标）、`name:azure/<Name>`（官方 Azure 图标）、`name:k8s/<Resource>`（官方 Kubernetes 图标）。脚本按 **svgl → devicon → gilbarbara/logos** 的顺序尝试，写出图标文件和 `manifest.json`，并标记填充色为白色的图标。svgl（svgl.app）排第一，因为它收录了现代开发品牌的最新官方标志（TanStack、Better Auth、Hono…）。当 logo 有亮/暗两个版本时，亮色版存为 `<name>`（两种主题下 tile 都是白的），暗色版存为 `<name>_dark` 供分组标签使用。svgl 只按精确标题匹配，未命中就直接落到下一来源。它的 API 还提供 `wordmark` 变体：偶尔适合做很宽的分组标签，永远不要用在 tile 上。

比操作细节更重要的规则：

- **绝不给 logo 改色。** 用户看得出来。如果 logo 是白色或太浅、放不进白色 tile，就给它配深色 tile（`tile dark` 类），不要动它的填充色。manifest 的 `white_fill` 标记只是启发式判断：白色填充也可能只是彩色标志上的内部细节（tRPC、Ubuntu），所以换深色 tile 前先扫一眼 SVG。
- **只用官方标志。** 特意不把 simple-icons 当作来源：它的字形是单色重绘，用户一眼就能看出不对。当所有来源都未命中（`FAIL`）时，找到官方文件，用 `name=URL` 传入：去项目仓库找（根目录 `logo*.svg`、`docs/`、`assets/`、`public/`），也去它的站点找（`/logo.svg`、`/favicon.svg`、`/images/logo.svg`）。有些标志只存在于仓库里（Lefthook 的是 `evilmartians/lefthook` 根目录的 `logo_sign.svg`）。
- **抽象概念用图形符号，不用文字。** "dev environment"、"cron"、"queue"、"cache"、"webhook receiver" 这类节点没有品牌，用 `name:lucide/<icon>` 取一个 Lucide 线性图标（如 `devenv:lucide/terminal`、`cron:lucide/clock`；可在 lucide.dev/icons 浏览）。不要"tile 里塞文字"，不要 emoji。
- **厂商子产品**（Cloudflare D1/R2/KV…）通常没有独立 logo：tile 上直接复用厂商 logo，靠节点名称区分（"Cloudflare D1" / "sqlite db"）。
- **AWS 用 AWS 自己的图标。** 每个服务都有一个：用 `name:aws/<Name>` 抓取，运行时从 AWS 官方图标包读取（如 `lambda:aws/lambda`、`aws:aws/AWS-Cloud-logo`、`s3:aws/s3`）。`AWS-` / `Amazon-` 前缀可省略，常见缩写直接可用（`s3`、`sqs`、`sns`、`ses`、`ecs`、`eks`、`ecr`、`elb`、`alb`、`nlb`、`iam`、`kms`、`msk`、`vpc`），未命中时会打印全部可用名称。slug `aws`、`amazonwebservices` 和 `aws-*` 指向同一个包，包里没有的就 `FAIL`，不会退回第三方副本。服务一定要写 `aws/` 前缀：裸写 `dynamodb` 仍会走第三方链路。图标包和散装图标文件不要放进仓库：AWS 允许在图表中使用这些图标，再分发未获确认。
- **AWS 区域遵循 AWS 自己的画法。** 服务图标自带方形底、深浅背景都适用，所以用 `tile bare`：再套一层白色 tile 只会让框变成双层。区域内的人物和通用节点用 AWS 的通用图标（`user:aws/General-User`；还有 `General-Users`、`General-Client`、`General-Internet`、`General-Server`），放在 `tile bare res` 里并配模板的 `lt`/`dk` 对。分组用模板的 `group aws` 表示 AWS Cloud（标签里放 `aws:aws/AWS-Cloud-logo`），其余用 `region`、`az`、`vpc`、`private` 或 `public`：直角、仅描边、标签用墨色、无厂商底色，角上的图标是 30px 且紧贴角落，而非 14px。VPC 内部，当你知道或能稳妥推断公私划分时，画出公有和私有子网（面向互联网的负载均衡器放公有；应用服务器和数据库放私有）：熟悉 AWS 的人第一眼就会注意到扁平的 VPC。区域内连线只用一种颜色、开放式箭头：`<path class="aws" ... marker-end="url(#open)"/>`，开发/部署用 `aws dash`，标签用普通 `.el`，且不为它们配图例。节点命名用 `Amazon S3` / `AWS Fargate`，不要裸写 `S3` / `Fargate`；`ALB` 这类缩写放进角色行，放在全名（`Elastic Load Balancing`）下面。名称可以占两行，但 `Amazon` / `AWS` 必须和首词待在同一行：如果换行恰好落在前缀后面，就把该节点加宽（`left:<centerX-76>px; width:152px`）。
- **Google Cloud 用 Google 自己的图标。** 用 `name:gcp/<Product>` 抓取，运行时从 Google 官方包读取（如 `run:gcp/cloud-run`、`lb:gcp/load-balancing`、`memorystore:gcp/memorystore`）。只有核心产品有自己的图标（Cloud Run、Cloud SQL、Cloud Storage、BigQuery、GKE、Compute Engine、Vertex AI…）。其余产品按 Google 指南的规定使用所属类别的图标：Cloud Load Balancing 和 Cloud CDN 都用 Networking；Memorystore 和 Firestore 都用 Databases。写产品名称，脚本会选好图标。`Cloud` / `Google` 前缀可省略，部分缩写直接可用（`vpc`、`iam`、`kms`、`iap`、`gce`、`gcs`），未命中时会打印全部可用名称。`gcp/storage` 是 Storage 类别；Cloud Storage 是 `gcp/cloud-storage`。slug `gcp-*` 和 `google-cloud-*` 指向同一批包，包里没有的就 `FAIL`，不退回第三方副本：那些副本是已停用的六边形旧图标，Google 明确不让用。产品一定要写 `gcp/` 前缀：裸写 `bigquery` 仍会走第三方链路。`gcp:google-cloud` 是分组标签用的 Google Cloud 标志。Gemini 和 Firebase 不在包里：直接用裸的 `gemini` 和 `firebase`。图标包和散装图标文件不要放进仓库：Google 提供这些图标用于图表和文档，再分发未获确认。
- **Google Cloud 图保持正常风格，分组用 Google 的。** Google 自家的图（实心蓝色面板、横向卡片）特意不模仿：图标照常放在白色 tile 上，连线和图例也照常。分组用模板的 `group gcp` 表示 Google Cloud（标签里放 `gcp:google-cloud`），其余用 `vpc`、`region`、`subnet` 或 `zone`。VPC 是全局的，subnet 是区域的，所以 region 放进 VPC 里，绝不要把 VPC 放进 region。全局和无服务器服务（外部负载均衡器、Cloud Storage、Cloud Run）留在 VPC 外。图标是跨产品共享的，所以产品一定写全名（`Cloud Load Balancing`，不要 `LB`），名称会换行的节点要加宽（`left:<centerX-76>px; width:152px`）。
- **Azure 用微软自己的图标。** 每个服务都有一个：用 `name:azure/<Name>` 抓取，运行时从微软官方包读取（如 `app:azure/app-service`、`azure:azure/Azure-A`、`vault:azure/key-vault`）。`Azure-` / `Microsoft-` 前缀和复数 `s` 可省略，常见缩写直接可用（`aks`、`vm`、`vnet`、`nsg`、`waf`、`blob`、`cosmos`、`redis`、`postgres`、`functions`、`front-door`、`apim`、`ai-search`），未命中时会打印全部可用名称。slug `azure`、`microsoft-azure` 和 `azure-*` 指向同一个包，包里没有的就 `FAIL`，不退回第三方副本。服务一定要写 `azure/` 前缀：裸写 `cosmos` 仍会走第三方链路。Microsoft Entra ID 有单独的图标集：把它的官方文件用 `name=URL` 传入。微软只允许把这些图标用于架构图、培训材料和文档。不得裁剪、翻转、旋转或改形，只能用于它所代表的那个微软服务，图标包和散装图标文件也不要放进仓库。
- **Azure 图保持正常风格，分组颜色用微软的。** 微软自家的图特意不模仿：图标照常放在白色 tile 上，连线和图例也照常。分组用模板的 `group azure` 表示 Azure（标签里放 `azure:azure/Azure-A`），其余用 `rg`、`region`、`vnet`、`subnet` 或 `zone`，且 `vnet` 或 `subnet` 的标签要带上各自的图标（`vnet:azure/vnet`、`subnet:azure/subnet`）。VNet 属于单一 region，所以放进 region 里。Front Door 这类全局服务留在 region 外。App Service 放在 VNet 外，除非它跑在 App Service Environment 里；通过私有端点访问的 PaaS 服务可以放在里面，角色写 `private endpoint`。微软要求每个图标旁写服务全名（`Azure SQL Database`，不要 `SQL`），所以名称会换行的节点要加宽（`left:<centerX-76>px; width:152px`）。
- **Kubernetes 用官方社区图标。** 用 `name:k8s/<Resource>` 抓取，来自官方 kubernetes/community 图标集（如 `pod:k8s/pod`、`deploy:k8s/deployment`、`svc:k8s/service`、`ing:k8s/ingress`、`cm:k8s/configmap`、`secret:k8s/secret`、`node:k8s/node`、`api:k8s/kube-apiserver`）。资源和基础设施用无标签变体，保证图表尺度下字形干净不拥挤；控制面组件用带标签变体。常见缩写和复数都可用（`svc`/`service`/`services`、`deploy`/`deployment`/`deployments`、`po`/`pod`/`pods`、`cm`/`configmap`/`configmaps`、`sts`/`statefulset`、`ds`/`daemonset`、`node`/`nodes` 等）。未命中会打印可用名称。slug `k8s`、`kubernetes` 和 `k8s/k8s` 经由这条链路提供官方 Kubernetes 舵轮 logo。
- **Kubernetes 图默认保持正常风格。** 图标放在正常白色 tile 上，与栈里的其他技术（如 NGINX、cert-manager、外部数据库或云负载均衡器）保持统一，在坐标纸背景上也有一致的层级和对比度。要极简的独立字形时也支持 `tile bare`。分组用标准分组（`cluster`、`namespace`、`node`、`pod`）。在图表页脚注明 Kubernetes Icons Set。
- **厂商规则只覆盖它自己的区域。** AWS、Google Cloud、Azure 和 Kubernetes 的规则只在该厂商分组内部生效，即使图里没画别的东西也一样。区域之外的一切，比如旁边的一个用户、一条跨进区域的连线，都保持正常的 tile、分组、连线和图例。
- **非品牌节点**（user、browser、internet、devices、bare-metal server）：从 `assets/generic/` 复制一个字形到图标目录、以节点名命名，或用 `name:lucide/<icon>`；不要用 emoji。它们不是品牌 logo，可以染成图表的墨色（抓取脚本对 Lucide 会自动处理）。
- **分组标签图标按 14px 渲染**，需要方形的字形标志。文字标（wordmark）和宽组合标在这个尺寸下会糊成一团；如果主图标是文字标，就单独抓品牌的方形图标给标签用（svgl 通常有；否则用项目自己的图标或 favicon 文件）。
- **分组标签直接落在分组底色上，不在白色 tile 上**，所以暗色主题下带黑色部分的标志会在那里消失。如果 `fetch_icons.py` 存了 `<name>_dark`，标签里用模板的 `lt`/`dk` 对；如果没有暗色变体而标志又有黑色部分，就给标签的 `<img>` 加 `plate` 类（白色衬底，仅暗色主题）。
- 位图 logo（png/webp）也没问题；构建脚本把所有资源内嵌为 data URI，查看时不需要加载任何东西。

## 第 3 步 — 布局

读 `references/geometry.md` 了解坐标系、间距常量，以及最重要的：**防止箭头穿过标签文字的连线锚定规则**。一句话版本：节点 = tile *加上*它下面的文字；垂直连线连接的是节点框边界，绝不是穿过文字、从 tile 直接连到 tile。

## 第 4 步 — 构建

复制 `assets/template.html`，把示例的 GROUPS / EDGES / NODES / header 各段换成你自己的（模板的标记本身就是格式文档），然后内嵌资源。`<html>` 的 `lang` 设成图表标签所用语言（默认 `en`；日语用 `ja`，让浏览器选用日文字形变体）。模板已内置两个选项：一是**暗色变体**（在 `<html>` 上设 `data-theme="dark"`；tile 保持白色以保住 logo，分组标签图标遵循第 2 步规则，箭头和图例色块自动跟随 token），二是"部署到平台 X"的连线，这里 X 是分组而不是节点：把箭头指向分组*内部*最有代表性的节点，给连线标注（`deploy`），这样语义才读得通。

```bash
python3 scripts/build.py my-diagram.html <icons-dir> out.html --fonts <skill>/assets/fonts
```

图标在标记中以 `%%ICON_<name>%%` 引用；字体以 `%%FONT_DISPLAY%%`（Geist）/ `%%FONT_JBM%%`（JetBrains Mono）引用。有 token 未解析时，构建会直接报错失败。所有颜色和字体都走模板里已有的 CSS 自定义属性：调 token，不要散落着改具体值。

## 第 5 步 — 亲眼看图验证

渲染出来，真正去读这张图：

```bash
python3 scripts/render_png.py out.html check.png --selector .canvas --scale 2
```

如果图表里有日文，渲染主机需要装日文字体，否则 CJK 字符会悄悄变成中文字形变体（用户一眼就能看出来）。脚本会警告并打印修复办法；模板的字体栈已写明 Noto JP 字体。

看图时对照检查：

- 没有箭头穿过标签文字；箭头头部不落在文字里
- 连线标签可读（它们有纸色光晕，确认生效了）
- 每个图标都可见（白上白是最经典的失败 → 改用深色 tile），包括暗色渲染里的分组标签图标
- 分组标签位于其分组的左上角，不与节点和连线相撞；每个分组的左右内边距一致
- 没有东西超出所属分组框；画布边缘没有裁切

修完再渲染，直到干净为止。这个循环很便宜；把一张文字重叠的图发出去可不便宜。

## 第 6 步 — 交付

- **HTML**（默认）：构建出的文件本身。自包含，离线可用。
- **PNG**：一律用无头 Chromium 对构建出的 HTML 截图得到（`render_png.py`，`--scale 2` 让文字清晰），绝不用 matplotlib/PIL/独立 SVG 栅格化工具另画一张；HTML 是唯一事实来源，浏览器的文字/SVG 渲染才是图好看的原因。脚本默认输出两套主题（`out.png` 亮色 + `out-dark.png`），直角（圆角只在截图时去掉）；除非用户只要一种，否则两套都交付。`--single` 按文档原样截取。只截图表用 `.canvas`，整页用 `--full-page`。
- **TSX**：按 `references/tsx.md` 转换（自包含 React 组件，无依赖）。
- **Artifact**（环境提供 artifact 或页面发布工具时）：用环境的 artifact 工具发布构建出的 HTML。所有资源已内嵌为 data URI，artifact 的断网沙箱不构成问题。用户要在对话里继续迭代图表时优先用它；需要贴到别处时配一张 PNG。

如果要求多种格式，只构建一次 HTML，其余都从它派生。

在页脚注明实际用到的图标来源，即图标目录 `manifest.json` 中每条的 `source` 字段（如 `icons: svgl / devicon / Lucide`；source 为 `aws` 写 `AWS Architecture Icons`，source 为 `gcp` 写 `Google Cloud product icons`，source 为 `azure` 写 `Azure Public Service Icons`）。品牌 logo 仍为其所有者的商标。模板的 "made with stack-diagram" 链接放在致谢之后，除非用户要求去掉；默认 PNG 只截画布，所以链接不会出现在图里。

## 第 7 步 — 分享到画廊（可选）

只在能运行带网络访问的 shell 命令的环境提供这一步；否则跳过。交付之后，用用户的语言加一句提议分享的话，并附画廊链接让他们先看看。例如："如果你愿意分享这张图，我可以把它发布到公开画廊：https://stacks.caru.moe"。每次对话只说一次，之后绝不再提；没有得到用户的明确同意绝不提交。

用户同意后，要一个展示名（不要从 `gh` 或 git 里填），并询问是否附带 GitHub 登录名。登录名可选，且绝不公开显示；它的作用只是让用户以后能用该账号登录画廊删除这条帖子。如果 `gh` 已登录，提供 `gh api user -q .login` 的结果；仅在用户同意时才带上。

发送任何内容之前，把将要发送的东西原样列出来：

- 亮色和暗色两张 PNG，即 `render_png.py` 写出的 `.canvas` 对（`out.png` / `out-dark.png`），附上路径和图中的每个标签
- 标题，即使对话不是英文也用平实的英文。它描述的是这张图，不是用户的请求。图自身的标签保持原样。
- 技术栈：图中的技术，按官方名称
- 展示名
- GitHub 登录名（如有），标注为不公开

指出任何看起来属于内部的东西：主机名、IP、客户或公司名、内部服务名，并建议先去掉这些再重渲染。请用户确认这是他们自己的系统、或是可以公开展示的系统，并在这一份确切内容上拿到第二次明确同意后才发送。

```bash
python3 scripts/share.py submit out.png out-dark.png --title "..." --stack "..." --name "..." [--github LOGIN] [--icons DIR]
```

`--stack` 按官方名称列出技术，逗号分隔。写 `Name=key` 可在画廊里在该技术旁显示 logo：`key` 是它在图标目录 `manifest.json` 里的条目名，`--icons` 接那个目录（第 2 步的 `<icons-dir>`）。不带 `=` 的名称不配 logo，例如 `--stack "Next.js=nextjs,Hono=hono,Neon" --icons <icons-dir>`。画廊只展示来自 svgl、gilbarbara/logos 和 devicon 的 logo；AWS、Google Cloud 和 Azure 产品图标、Lucide 以及来自品牌自己站点或仓库的 logo 一律不配。

如果 `share.py` 以文件过大为由拒绝某张 PNG，就用更低的 `--scale` 重渲染，发送前展示新的一对。

告诉用户 URL、待审帖子要经人工审核后才会出现，以及 `share.py` 报告的删除密钥保存路径。之后删除用：`python3 scripts/share.py delete <id>`（`list` 可列出已保存的帖子）。如果画廊能确认他们提供的 GitHub 登录名，用该账号在画廊登录也能删除。
