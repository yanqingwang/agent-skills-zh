> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/output-spec.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Draw.io 导入输出规格：格式 × 尺寸 × 细节 × 受众

四个拨盘决定一张导入图最终变成什么。重绘**之前**就设好它们：它们影响交付物、布局、字号阶梯、节点数量和用词，事后补设等于重画。

| 拨盘 | 回答的问题 | 默认值 |
|---|---|---|
| **格式（Format）** | 这份文件会落到哪里？ | `html` |
| **尺寸（Size）** | 画布多大，读者离多远？ | `doc-inline` |
| **细节级别（Detail level）** | 复现每个元素，还是压缩？ | `balanced` |
| **受众（Audience）** | 用词要多技术化？ | `mixed` |

能从请求中明确推断的选项直接推断（例如“给我的 deck 用”意味着 slide 预设）。仍然关键的歧义，问一个简短问题。用户不在意时，用上面的默认值并说明用了哪些。

---

## 1. 格式

| 格式 | 交付物 | 保留 | 丢弃 |
|---|---|---|---|
| `html` | 自包含的 `.html`（默认） | 页头、图、摘要卡片、页脚、真实字体 | 无 |
| `svg` | 源文件旁边的 `.svg` | `<svg>` 节点、矢量文本 | 编辑外层包装；离线工具里字体会被替换 |
| `png` | 按 `device_scale_factor` 输出的 `.png` | 与浏览器渲染完全一致的像素 | 矢量可编辑性 |
| `html+png` | 两者 | — | — |

总是先生成 HTML：`svg` 和 `png` 都是*从它*经 [`export.md`](export.md) 产出的。绝不要手写 SVG 文件；HTML 是唯一事实来源，也是品味关卡（SKILL.md §9）唯一针对的产物。

按用途选择：

| 用途 | 格式 | 尺寸预设 |
|---|---|---|
| 博客文章、README、文档站 | `html`（内嵌）或 `png` | `doc-inline` |
| Keynote / PowerPoint / Google Slides | `png` @2 | `slide-16x9` |
| Figma / Illustrator / 进一步编辑 | `svg` | `fit` |
| X / LinkedIn / OG 链接卡片 | `png` @2 | `social-og` |
| 打印讲义、PDF 演示稿 | `png` @3 | `print-a4-landscape` |
| Confluence / Notion / 内部 wiki | `png` @2 | `doc-wide` |

---

## 2. 尺寸

预设决定 SVG 的 `viewBox`。下面所有取值都能被 4 整除，所以 SKILL.md §7 的网格规则依然成立。

| 预设 | viewBox | 宽高比 | PNG @2 | 字号阶梯 | 用途 |
|---|---|---|---|---|---|
| `doc-inline`（默认） | `0 0 960 600` | 8:5 | 1920×1200 | standard | 文章或 README 里的正文宽度图 |
| `doc-wide` | `0 0 1280 720` | 16:9 | 2560×1440 | standard | 全宽文档、wiki 页面 |
| `slide-16x9` | `0 0 1280 720` | 16:9 | 2560×1440 | presentation | 演示文稿页面、投屏 |
| `slide-4x3` | `0 0 1024 768` | 4:3 | 2048×1536 | presentation | 旧版演示模板 |
| `social-og` | `0 0 1200 632` | ~1.9:1 | 2400×1264 | presentation | 链接预览卡片 |
| `social-square` | `0 0 1080 1080` | 1:1 | 2160×2160 | presentation | 信息流帖子、轮播图 |
| `print-a4-landscape` | `0 0 1120 792` | ~1.41:1 | @3 → 3360×2376 | print | A4 横向，96dpi 下约 10mm 边距 |
| `print-a3-landscape` | `0 0 1584 1120` | ~1.41:1 | @3 → 4752×3360 | print | A3 横向，96dpi 下约 10mm 边距 |
| `print-letter-landscape` | `0 0 1056 816` | ~1.29:1 | @3 → 3168×2448 | print | US Letter 横向 |
| `fit` | 由内容推导 | 任意 | @2 | standard | 矢量交接；无固定画框 |

### 在窄屏上稳住画布

SVG 在手机上保持自己的可读宽度，而不是跟着屏幕缩水，所以 `min-width` 是**所用预设的 viewBox 宽度**，不是写死的数字。
设得再低一点，整张图就会缩小，字号阶梯跟着缩：
`doc-wide` 1280 viewBox 上的 12px 节点名若钉在 900，实际渲染成 8.4px，
低于本规格设定的每一档下限，而屏幕上没有任何提示。

这么宽的画布总得在某个地方滚动。把它放进一个自己会滚动的容器，否则整篇文档横向滚动，右侧节点读者想不到去找就看不见了：

```html
<div class="diagram-container">
  <svg viewBox="0 0 960 600" …> … </svg>
</div>
```

```css
.diagram-container { width: 100%; overflow-x: auto; }
svg { width: 100%; min-width: 960px; display: block; }
```

两种情形要额外当心。居中的 grid 或 flex 子项会按 SVG 的 max-content 宽度确定自身尺寸，于是容器的 `width: 100%` 以这个宽子项为基准，永远不会滚动：给该子项加 `max-width: 100%; min-width: 0`。
另外，当某个祖先元素是 `overflow: hidden`（窗口边框、被裁切的卡片）时，SVG 会被裁掉而不是滚动：没有滚动条、没有页面溢出，页面溢出检查还会报文件干净，因为内容是被销毁而不是溢出。容器必须放在该祖先**之内**。

纸面没有滚动条，所以在纸上同样这个容器会裁切而不是滚动。打印时把两者都放开，让图缩放以适配整页：小而完整胜过清晰但被裁。这条规则必须放在 `svg` 规则**之后**，因为 media query 不增加优先级，靠后的普通规则会胜出：

```css
@media print {
  .diagram-container { overflow-x: visible; }
  svg { min-width: 0; }
}
```

`scripts/lint-render.py --all` 会以 390px 渲染每个模板，页面溢出、够不着的被裁 SVG、缺少本地滚动容器、`min-width` 与 viewBox 不符（包括压根没写，那会让 SVG 缩进手机里并带走字号阶梯）都会判失败。

### 推导 `fit`

把内容包围盒**向上**取整到下一个 4 的倍数，再加上固定的外围装饰：四周各 40px 外边距，底部另有 60px 给图例条。绝不要让内容贴到 viewBox 边缘。

### 每个尺寸级别的字号阶梯

画布变大时节点名相对会变小，要顶住这种趋势。字号阶梯随预设缩放，让投屏的页面从后排也读得清。

| 角色 | standard | presentation | print |
|---|---|---|---|
| 标题（Instrument Serif） | 28 | 40 | 32 |
| 节点名（Geist 600） | 12 | 16 | 12 |
| 子标签（Geist Mono） | 9 | 12 | 9 |
| 箭头标签（Geist Mono） | 8 | 12 | 8 |
| 眉标 / 标签（Geist Mono） | 8 | 8 | 8 |
| 节点框最小高度 | 48 | 64 | 48 |
| 节点间最小间距 | 24 | 40 | 24 |

表中列出的字体家族是默认皮肤的，`scripts/verify-docs-sync.py` 就是按它们绑定每个字号的。使用自定义皮肤时，把它们读作 [`style-guide.md`](style-guide.md) 里的 `title`、`node-name`、`sublabel`、`arrow-label`、`eyebrow` 角色；字号参考文档把这些角色写成 `{node-name}` 等。

每个 `font-size` 要么是所用预设对应上面角色值之一，要么是下表列出的具名例外之一：

| 例外 | 字体 | 字号 |
|---|---|---|
| 高密度注释：图例键、坐标轴刻度、图表数据标签、来源行、框内标签 | Geist Mono 或 Geist regular | 7 到 11，允许半步 |
| 图表系列或行名：柱状分类、折线或坡度系列、甘特行、矩阵表头 | Geist 600 | 10 到 11 |
| 分组或实体标题 | Geist 600 | 14 |
| 不透明度不高于 0.08 的装饰性水印数字 | 任意 | 任意 |

例外与旁边的字体绑定，含字重：Geist 600 及更重是节点名的声部，更轻的 Geist 是注释。所以 Geist 600 的节点名不能借高密度注释下探到 7，Geist Mono 的刻度也不能借标题专用的 14。图表行以同样的 Geist 600 声部承载一个阶梯中没有对应行的名称，这正是它单列一条例外、而不是获得缩小许可的原因：`type-bar.md`、`type-gantt.md` 和 `type-line.md` 都把这个名称设在 10 或 11。

其余任何字号都是图里的 bug，不是新字号。唯一长期豁免是下面的封闭清单。

### 已登记的历史字号

十六个文件里的三十三个已声明字号早于本契约。把它们登记在此，是为了让上面的规则精确可查而不是一纸愿景；同时冻结清单，防止悄悄增长。`scripts/verify-docs-sync.py` 会拿这些行去核对文件，某个文件多出一个阶梯外字号、少了一个、或从磁盘消失都会判失败。

每个字号都按承载它的字体登记，因为扫描检查的就是字体。扫描先把每个元素归类：通过样式表解析 `class` 属性、把 `var(--font-mono)` 还原到它指名的字体家族、把 `{node-name}` 记号对应到拥有它的阶梯行，然后只应用对该字体开放的例外。各角色的规范字号并成一个并集，所以凡在任一角色阶梯上的字号，出现在哪里都算合规。读不出字体的元素享受不到任何例外。它读取 `<svg>` 及其中元素所套用的 CSS 规则，因此图周围的散文不算图内文字。

| 文件 | 字号 | 是什么 |
|---|---|---|
| `assets/example-data-flow.html` | Geist Mono 5, Geist Mono 6 | 芯片文本与角色标签，都在 CSS 里设定 |
| `assets/example-data-flow-dark.html` | Geist Mono 5, Geist Mono 6 | 芯片文本与角色标签，都在 CSS 里设定 |
| `assets/example-data-flow-full.html` | Geist Mono 5, Geist Mono 6 | 芯片文本与角色标签，都在 CSS 里设定 |
| `assets/example-nested.html` | Instrument Serif 14, Instrument Serif 14 | 两处斜体衬线旁注 |
| `assets/example-nested-dark.html` | Instrument Serif 14, Instrument Serif 14 | 两处斜体衬线旁注 |
| `assets/example-nested-full.html` | Instrument Serif 14, Instrument Serif 14 | 两处斜体衬线旁注 |
| `assets/example-paved-road-animated.html` | Geist 600 13 | 边界节点名 |
| `assets/example-process.html` | Geist Mono 6 | 角色芯片 |
| `assets/example-process-dark.html` | Geist Mono 6 | 角色芯片 |
| `assets/example-process-full.html` | Geist Mono 6 | 角色芯片 |
| `assets/example-quadrant-consultant.html` | Geist 600 13 | `tspan` 里的行内圆点字形 |
| `assets/example-queue-animated.html` | Geist 600 13, Geist 600 22, Geist 600 24 | 状态说明与两个填充计数 |
| `assets/example-treemap.html` | Geist 600 7, Geist 600 7, Geist 600 13, Geist 600 13 | 两个单元格序号字形与两个单元格名 |
| `assets/example-treemap-dark.html` | Geist 600 7, Geist 600 7, Geist 600 13, Geist 600 13 | 两个单元格序号字形与两个单元格名 |
| `assets/example-treemap-full.html` | Geist 600 7, Geist 600 7, Geist 600 13, Geist 600 13 | 两个单元格序号字形与两个单元格名 |
| `references/type-treemap.md` | Geist 600 13 | 文档化模式的单元格名行 |

新图不给这里添加行。把某个历史字号迁上阶梯，是对已发布示例的视觉变更，应单独开一个 PR。

presentation 阶梯意味着节点更少：64px 框里的 16px 名字很占画布。如果 `slide-16x9` 布局放不下，那是尺寸拨盘在告诉你细节拨盘设得太高：降一级，而不是缩小字号。

### 安全区

- **所有预设：** 四周 40px 外边距；图例条占底部 60px，其他内容不得进入。
- **`social-og`：** 四周外圈 64px 保持留白：链接卡片在各平台的裁切不可预测。
- **`slide-*`：** 若演示模板有页脚条，底部 80px 保持留白；拿不准就问。

---

## 3. 细节级别

源图有多少能存活下来。这是*数量*拨盘：管多少元素通过，不管它们怎么措辞（那是 §4 的事）。

| 级别 | 节点 | 边 | 子标签 | 存活内容 |
|---|---|---|---|---|
| `faithful`（忠实） | ≤24，须分区 | ≤32 | 每个端口、协议、版本 | 源图里每个独立组件。只有完全相同的重复项才合并。 |
| `balanced`（默认） | ≤12 | ≤16 | 最多 4 个节点带技术子标签 | 承载叙事的组件；叶子簇各自收敛为一个节点。 |
| `simplified`（简略） | ≤7 | ≤9 | 无 | 能力及其先后顺序。基础设施消失。 |

`balanced` 和 `simplified` 在标准复杂度预算（SKILL.md §7）之内。**`faithful` 是有意超出它的**：这就是那笔交易，附带条件如下：

1. **必须分区。** 超过 9 个节点时，每个节点都要属于一个带标签的分区（2–4 个分区、细边框、`paper-2` 填充、左上角等宽大写分区标签）。不分区的 20 节点图是接线图，不是原理图。
2. **连线规则不放松。** 24 个节点时 SKILL.md §6 的第 1–5 条依然适用。不重叠就布不通，说明已超过真实上限：拆分。
3. **超过 24 个节点就拆。** 产出一张总览图（分区作为节点，`balanced` 语法）加每个分区一张细节图。命名为 `<base>-overview.html`、`<base>-<zone>.html`。绝不交付 40 节点的单画布。
4. **强调色保持 2 个。** 节点更多从来不意味着焦点元素更多。

### 降级阶梯

源图超出该级别允许的数量时，按此顺序裁剪，一旦低于预算就停。绝不临时随意裁。

1. **装饰性单元格**：便签、游离文本、标题块、水印、源图自己的图例。（值得保留的便签转成注释标注，最多 2 个，见 [primitive-annotation.md](primitive-annotation.md)。）
2. **完全重复项**：N 个相同的 worker/副本/分片合并为一个节点，标为 `Worker ×N`。
3. **叶子簇**：子项全是叶子的容器收敛为该容器本身：`Core Services` 取代它的三个框。抽取器把这些列在*可折叠分组*之下。
4. **不影响叙事的一度汇点**：监控挂钩、日志桶、归档层。
5. **横切基础设施**：日志、指标、密钥、CI。`simplified` 级直接去掉、不用问；`balanced` 级最多保留一个，且仅当图的主题就是它。
6. **还超？** 拆成总览 + 细节。拆分胜过缩小。

第 2–6 步裁掉的内容都记入忠实度台账（§5）。第 1 步不需要报告。

---

## 4. 受众级别

与细节拨盘无关：同样 12 个节点，给平台团队的命名和给指导委员会的命名不同。细节决定*多少个*；受众决定*叫什么*。

| 受众 | 节点名 | 子标签 | 边标签 | 绝不出现 |
|---|---|---|---|---|
| `engineer` | 确切的服务 / 组件名 | 协议、端口、版本、镜像标签 | `POST /v2/orders`、`SQL`、`gRPC` | “connects to”这类含糊动词 |
| `mixed`（默认） | 组件名，缩写展开 | 只有影响决策时才写技术信息 | 平实动词：`verifies`、`writes`、`notifies` | 端口、版本、内部代号 |
| `executive` | 能力与结果 | 无 | 业务动词：`approves`、`pays out` | 厂商名、基础设施、协议 |

完整示例：同一个节点在三种受众下的写法：

| 受众 | 节点名 | 子标签 |
|---|---|---|
| `engineer` | `Auth Service` | `JWT · RS256 · :8443` |
| `mixed` | `Auth Service` | `token check` |
| `executive` | `Sign-in` | — |

在所有受众级别都成立的两条规则：

- **绝不为了填槽而编造细节。** 输入只给了 `svc-04` 而没有任何解释时，保留标识符并追问，不要猜一个业务名。
- **专有名词保留源图词汇。** 在 `executive` 级把 `Kafka` 改名为 `Message Bus` 没问题；改成 `Event Grid`（另一个产品）就是事实错误。

### 非拉丁文字标签

Geist 不含 CJK 字形。标签里出现日文、中文或韩文时，在这些 `<text>` 元素上扩展字体家族，不要整个换皮肤：

```svg
<text font-family="'Geist', 'Hiragino Sans', 'Noto Sans JP', 'Yu Gothic', sans-serif">認証サービス</text>
<text font-family="'Geist', 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif">인증 서비스</text>
<text font-family="'Geist', 'PingFang SC', 'Noto Sans SC', 'Microsoft YaHei', sans-serif">认证服务</text>
<text font-family="'Geist', 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif">認證服務</text>
```

这些字体栈以默认皮肤的无衬线体开头。使用自定义皮肤时，改为以 `node-name` 家族开头，CJK 回退字体排在其后。Hiragino/Yu Gothic 栈不含谚文字形，所以韩文标签要用韩文栈，不要复用日文栈。Noto Sans KR 随皮肤的字体链接一起提供，所以它排在韩文栈首位，本地家族跟在后面；韩文在字体之外需要的语域、下限和标题规则在 [`style-guide.md`](style-guide.md#korean-labels)。日文字体也只覆盖汉字集的一个子集，且简体字形会以日文变体渲染，所以中文标签要用中文栈；简体和繁体出于同样原因各用各的栈。Noto Sans TC 现在也随链接提供，排在繁体栈首位，本地家族跟在后面；繁体中文在字体之外需要的语域、下限和标题规则在 [`style-guide.md`](style-guide.md#traditional-chinese-labels)。等宽子标签用 `'Geist Mono', 'Noto Sans Mono CJK JP', monospace`（日文）、`'Geist Mono', 'Noto Sans Mono CJK KR', monospace`（韩文），或 `'Geist Mono', 'Noto Sans Mono CJK SC', monospace` / `'Geist Mono', 'Noto Sans Mono CJK TC', monospace`（中文）。按**每个全角 CJK 字符 1em** 预留宽度，不要只按平均拉丁字符加一小点百分比；`verify-treemap.py` 对 Unicode 宽/全角字符就采用这个保守契约，并把组合附加符视为不占宽。CJK 标签宁可要 12px 的名字，不要 8px 的子标签；谚文和汉字低于 12px 会发糊，所以下限按 12px 算，不是 10px。实际宽度仍随回退字体而变，翻译标签之后要跑一遍相应的几何校验器。

---

## 5. 忠实度台账

只要产出小于输入（每次 `balanced` 和 `simplified` 都是，多数 `faithful` 也是），就在聊天里、文件路径之后报告你裁掉了什么。要短、要具体：

```
Detail: balanced · 18 source nodes → 9 drawn
Merged:  worker-01..06 → "Ingest Worker ×6"
Collapsed: "Observability" group (Grafana, Loki, Tempo) → one node
Dropped: 2 sticky notes, CI pipeline (cross-cutting)
Kept in full: the request path (Client → Gateway → Orders → Postgres)
```

看图的人看不见缺了什么。提需求的人必须知道。

---

## 6. 检查清单

与 SKILL.md §9 品味关卡一起执行。

- [ ] 四个拨盘都已设定：显式要求、按用途推断，或用默认并已说明？
- [ ] `viewBox` 与尺寸预设完全一致，取值可被 4 整除？
- [ ] `min-width` 等于预设的 viewBox 宽度，且 SVG 位于本地 `overflow-x: auto` 容器之内（该容器在任何 `overflow: hidden` 祖先之内）？
- [ ] `@media print` 放开 `min-width` 和 `overflow-x`，且位于 `svg` 规则之后？
- [ ] 字号阶梯与尺寸级别匹配：投屏页面上没有错用 standard 阶梯？
- [ ] 40px 外边距得到遵守（`social-og` 为 64px）？
- [ ] 节点数在细节级别的上限之内？
- [ ] `faithful` 超 9 节点已分区，超 24 已拆分？
- [ ] 节点名、子标签、边标签处于同一受众级别？
- [ ] CJK 标签已配置字体回退？
- [ ] 所有裁剪都已报告忠实度台账？
- [ ] 图的 `<svg>` 带 `role="img"`、可解析的 `aria-labelledby`、非空的第一个子元素 `<title>`、非空的 `<desc>`，以及按图/变体加前缀的 ID？
- [ ] 要求的非 HTML 格式经 [`export.md`](export.md) 产出，而非手写？
