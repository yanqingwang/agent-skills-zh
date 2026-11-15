> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/ui-ux-pro-max/references/quick-reference.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 快速参考：完整规则集（全部 10 类）

做 UI 评审/审查时加载本文件，或当某个类别需要的完整清单超出 SKILL.md 的优先级表时使用。每条规则也在 `data/ux-guidelines.csv` / `data/app-interface.csv` 中原样存在，可通过 `--domain ux` / `--domain web` 搜索找到：本文件是一个静态索引，用于免一次搜索往返的快速浏览。

## 快速参考

### 1. 可访问性（CRITICAL）

- `color-contrast` - 普通文本最低 4.5:1（大文本 3:1）；Material Design
- `focus-states` - 交互元素要有可见焦点环（2–4px；Apple HIG、MD）
- `alt-text` - 有意义的图片要有描述性 alt 文本
- `aria-labels` - 纯图标按钮要有 aria-label；原生端用 accessibilityLabel（Apple HIG）
- `icon-context` - 语义取决于用途：可见文本旁的装饰图标要从无障碍树隐藏；有含义的图标要有文本替代；图标控件要有可访问名称和相应状态
- `keyboard-nav` - Tab 顺序与视觉顺序一致；完整键盘支持（Apple HIG）
- `form-labels` - 用带 for 属性的 label
- `skip-links` - 给键盘用户跳到主内容的链接
- `heading-hierarchy` - h1→h6 顺序递进，不跳级
- `color-not-only` - 不要只用颜色传达信息（加图标/文本）
- `dynamic-type` - 支持系统文字缩放；文字变大时不截断（Apple Dynamic Type、MD）
- `reduced-motion` - 尊重 prefers-reduced-motion；用户要求时减少/关闭动画（Apple Reduced Motion API、MD）
- `voiceover-sr` - 有含义的 accessibilityLabel/accessibilityHint；VoiceOver/读屏器阅读顺序符合逻辑（Apple HIG、MD）
- `escape-routes` - 弹窗和多步流程要有取消/返回（Apple HIG）
- `keyboard-shortcuts` - 保留系统和无障碍快捷键；拖放要提供键盘替代（Apple HIG）
- `focus-not-obscured` - 吸顶 UI、浮层和横幅不得遮挡键盘聚焦的控件（WCAG 2.2 AA）
- `focus-not-obscured-enhanced` - 聚焦的组件要完整可见（WCAG 2.2 AAA）
- `focus-appearance` - 核对焦点指示区域和 3:1 状态对比度；仅有可见焦点还不够（WCAG 2.2 AAA）
- `dragging-alternative` - 每个作者控制的拖拽动作都要有单指针和键盘替代（WCAG 2.2 AA）
- `web-target-size` - Web 指针目标要 24×24 CSS px，或有成文的例外；不要用原生单位替代（WCAG 2.2 AA）
- `consistent-help` - 重复出现的帮助机制在一组页面中保持相同相对顺序（WCAG 2.2 A）
- `redundant-entry` - 同一流程中复用已提供的信息，除非重填确有必要（WCAG 2.2 A）
- `accessible-authentication` - 允许密码管理器和粘贴；提供不需要认知负担的认证路径（WCAG 2.2 Minimum，AA）。Enhanced AAA 准则未收录进数据集
- `auto-rotation-controls` - 轮播和移动内容要有暂停/停止控件，获得焦点或开启减弱动效时必须停止（WAI）
- `contextual-live-badge-updates` - 数量/状态变化要以完整的上下文短语播报，不移动焦点；用一处合适的 live/状态区域，仅在需要时用原子更新

### 2. 触控与交互（CRITICAL）

- `touch-target-size` - 最小 44×44pt（Apple）/ 48×48dp（Material）；需要时把点击热区扩到视觉边界之外
- `touch-spacing` - 触控目标之间最小 8px/8dp 间距（Apple HIG、MD）
- `hover-vs-tap` - 主要交互用点击/轻点；不要只依赖悬停
- `loading-buttons` - 异步操作期间禁用按钮；显示 spinner 或进度
- `error-feedback` - 在问题附近给出清晰的错误消息
- `cursor-pointer` - 可点击元素加 cursor-pointer（Web）
- `gesture-conflicts` - 主内容避免横向滑动；优先纵向滚动
- `tap-delay` - 用 touch-action: manipulation 减少 300ms 延迟（Web）
- `standard-gestures` - 平台标准手势保持一致使用；不要重新定义（如侧滑返回、捏合缩放）（Apple HIG）
- `system-gestures` - 不要挡系统手势（控制中心、侧滑返回等）（Apple HIG）
- `press-feedback` - 按下要有视觉反馈（涟漪/高亮；MD 状态层）
- `haptic-feedback` - 确认和重要动作用触感反馈；避免滥用（Apple HIG）
- `gesture-alternative` - 不要只靠手势交互；关键动作总要有可见控件
- `safe-area-awareness` - 主要触控目标远离刘海、灵动岛、手势条和屏幕边缘
- `no-precision-required` - 避免要求在小图标或细边上精准点击
- `swipe-clarity` - 滑动操作要有清晰的可供性或提示（箭头、标签、引导）
- `drag-threshold` - 开始拖拽前设移动阈值，避免误触拖拽

### 3. 性能（HIGH）

- `image-optimization` - 用 WebP/AVIF、响应式图片（srcset/sizes），非关键资源懒加载
- `image-dimension` - 声明 width/height 或用 aspect-ratio，防止布局位移（Core Web Vitals：CLS）
- `font-loading` - 用 font-display: swap/optional 避免文字不可见（FOIT）；预留空间减少布局位移（MD）
- `font-preload` - 只预加载关键字体；不要给每个字重都用 preload
- `critical-css` - 首屏 CSS 优先（内联关键 CSS 或提前加载样式表）
- `lazy-loading` - 非首屏组件用动态导入 / 路由级分割懒加载
- `bundle-splitting` - 按路由/功能拆分代码（React Suspense / Next.js dynamic），降低首屏加载和 TTI
- `third-party-scripts` - 第三方脚本 async/defer 加载；审查并移除不必要的（MD）
- `reduce-reflows` - 避免频繁的布局读/写；先批量读 DOM 再批量写
- `content-jumping` - 给异步内容预留空间，避免布局跳动（Core Web Vitals：CLS）
- `lazy-load-below-fold` - 首屏以下的图片和大媒体用 loading="lazy"
- `virtualize-lists` - 50 项以上的列表做虚拟化，提升内存效率和滚动性能
- `main-thread-budget` - 每帧工作量控制在约 16ms 内以达 60fps；重任务移出主线程（HIG、MD）
- `progressive-loading` - 超过 1 秒的操作用骨架屏 / shimmer，不用长时间阻塞的 spinner（Apple HIG）
- `input-latency` - 点按/滚动的输入延迟控制在约 100ms 内（Material 响应标准）
- `tap-feedback-speed` - 轻点后 100ms 内给出视觉反馈（Apple HIG）
- `debounce-throttle` - 高频事件（scroll、resize、input）用 debounce/throttle
- `offline-support` - 提供离线状态提示和基本回退（PWA / 移动端）
- `network-fallback` - 慢网络提供降级模式（低分辨率图片、更少动画）

### 4. 风格选择（HIGH）

- `style-match` - 风格匹配产品类型（推荐组合用 `--design-system`）
- `consistency` - 所有页面用同一风格
- `no-emoji-icons` - 用 SVG 图标（Heroicons、Lucide），不用 emoji
- `color-palette-from-product` - 色板按产品/行业选择（搜索 `--domain color`）
- `effects-match-style` - 阴影、模糊、圆角与所选风格一致（玻璃 / 扁平 / 黏土等）
- `platform-adaptive` - 尊重平台惯例（iOS HIG 与 Material）：导航、控件、字体排印、动效
- `state-clarity` - hover/按下/禁用状态视觉可区分，同时不脱离风格（Material 状态层）
- `elevation-consistent` - 卡片、面板、弹窗用统一的层级/阴影刻度；避免随意的阴影值
- `dark-mode-pairing` - 浅色/深色变体一起设计，保证品牌、对比度和风格一致
- `icon-style-consistent` - 全产品用一套图标集/视觉语言（描边宽度、圆角）
- `system-controls` - 原生/系统控件优先于全自定义；只有品牌需要时才自定义（Apple HIG）
- `blur-purpose` - 模糊用于表达背景失效（弹窗、面板），不作装饰（Apple HIG）
- `primary-action` - 每屏只有一个主要 CTA；次级操作视觉上居从属地位（Apple HIG）

### 5. 布局与响应式（HIGH）

- `viewport-meta` - width=device-width initial-scale=1（绝不禁用缩放）
- `mobile-first` - 移动优先设计，再放大到平板和桌面
- `breakpoint-consistency` - 用系统化断点（如 375 / 768 / 1024 / 1440）
- `readable-font-size` - 移动端正文最小 16px（避免 iOS 自动放大）
- `line-length-control` - 移动端每行 35–60 字符；桌面 60–75 字符
- `horizontal-scroll` - 移动端不出现横向滚动；内容要装进视口宽度
- `spacing-scale` - 用 4pt/8dp 递增间距系统（Material Design）
- `touch-density` - 组件间距适合触控：不拥挤，也不会造成误触
- `container-width` - 桌面端容器 max-width 一致（max-w-6xl / 7xl）
- `z-index-management` - 定义分层 z-index 刻度（如 0 / 10 / 20 / 40 / 100 / 1000）
- `fixed-element-offset` - 固定导航/底栏要给底层内容预留安全 padding
- `scroll-behavior` - 避免干扰主滚动体验的嵌套滚动区域
- `viewport-units` - 移动端优先 min-h-dvh 而不是 100vh
- `orientation-support` - 横屏下布局保持可读可操作
- `content-priority` - 移动端先显示核心内容；次要内容折叠或隐藏
- `visual-hierarchy` - 用尺寸、间距、对比建立层级：不要只靠颜色
- `compact-label-overflow` - 按语义选择徽章、状态标签、筛选 chip 或可移除值；关键标签保持可达，不可避免的截断要向指针和键盘用户披露
- `chip-collection-reflow` - 先换行整组 chip 再缩小标签；`+n` 溢出摘要做成可操作的展开项，而不是把值藏起来

### 6. 字体与颜色（MEDIUM）

- `line-height` - 正文行高 1.5-1.75
- `line-length` - 每行 65-75 字符
- `font-pairing` - 标题/正文字体气质匹配
- `font-scale` - 统一字号阶梯（如 12 14 16 18 24 32）
- `contrast-readability` - 浅底用深字（如白底 slate-900）
- `text-styles-system` - 用平台文字系统：iOS 11 Dynamic Type 样式 / Material 5 文字角色（display、headline、title、body、label）（HIG、MD）
- `weight-hierarchy` - 用 font-weight 强化层级：标题 Bold（600–700），正文 Regular（400），标签 Medium（500）（MD）
- `color-semantic` - 组件里定义语义色 token（primary、secondary、error、surface、on-surface），不写裸 hex（Material 颜色系统）
- `color-dark-mode` - 深色模式用降饱和/更亮的色调变体，不是简单反色；对比度单独测试（HIG、MD）
- `color-accessible-pairs` - 前景/背景配对要达 4.5:1（AA）或 7:1（AAA）；用工具核验（WCAG、MD）
- `color-not-decorative-only` - 功能色（错误红、成功绿）必须配图标/文本；避免只靠颜色表达含义（HIG、MD）
- `truncation-strategy` - 能换行就不截断；要截断就用省略号，并通过 tooltip/展开提供全文（Apple HIG）
- `letter-spacing` - 尊重平台默认字距；正文避免过紧字距（HIG、MD）
- `number-tabular` - 数据列、价格、计时器用 tabular/等宽数字，防止布局位移
- `whitespace-balance` - 有意图地留白，聚拢相关项、分隔区块；避免视觉杂乱（Apple HIG）
- `heading-line-balance` - 短标题可用平衡换行，作为渐进的、由 user agent 控制的启发式；自然换行保持可读，绝不用一揽子不换行空格硬把结尾词并成一行
- `long-token-wrapping` - URL、ID 和用户内容用 `overflow-wrap: anywhere` 加可收缩的 flex/grid 文本子项来换行；普通散文不要用 `word-break: break-all`

### 7. 动画（MEDIUM）

- `duration-timing` - 按距离、复杂度、平台和用户情境选共享动效 token；要测反馈是否仍然跟手，不要把一个时长区间当成万能
- `transform-performance` - 只用 transform/opacity；不要动画 width/height/top/left
- `loading-states` - 反馈要匹配预期等待时间和平台/组件指引；近即时的工作不要闪加载指示，长时间等待也不要毫无解释
- `excessive-motion` - 每屏最多动画 1-2 个关键元素
- `easing` - 进入用减速，离开用加速；真正匀速的进度或旋转才用线性
- `motion-meaning` - 每个动画都要表达因果关系，不能只是装饰（Apple HIG）
- `state-transition` - 状态变化（hover / active / 展开 / 折叠 / 弹窗）要平滑过渡，不要跳变
- `continuity` - 页面/屏幕切换保持空间连续性（共享元素、方向性滑动）（Apple HIG）
- `parallax-subtle` - 视差要克制；必须尊重减弱动效，且不能让人迷失方向（Apple HIG）
- `spring-physics` - 自然手感优先用弹簧/物理曲线，而不是线性或 cubic-bezier（Apple HIG 流畅动画）
- `exit-faster-than-enter` - 退场动画比进场短（约为进场的 60–70%）才显得跟手（MD motion）
- `stagger-sequence` - 列表/网格项进场每项错开 30–50ms；不要一次全出，也不要太慢（MD）
- `shared-element-transition` - 屏幕之间用共享元素 / hero 过渡保持视觉连续（MD、HIG）
- `interruptible` - 动画必须可打断；用户点按/手势立即取消进行中的动画（Apple HIG）
- `no-blocking-animation` - 动画期间绝不阻塞输入；UI 保持可交互（Apple HIG）
- `fade-crossfade` - 同一容器内替换内容用 crossfade（MD）
- `scale-feedback` - 可点卡片/按钮按下时轻微缩放（0.95–1.05），松开恢复（HIG、MD）
- `gesture-feedback` - 拖拽、滑动、捏合必须实时视觉响应、跟随手指（MD Motion）
- `hierarchy-motion` - 用 translate/scale 方向表达层级：从下方进入 = 更深一层，向上退出 = 返回（MD）
- `motion-consistency` - 全局统一时长/缓动 token；所有动画同一节奏、同一手感
- `opacity-threshold` - 淡出元素不要停留在 0.2 以下不透明度：要么淡干净，要么保持可见
- `modal-motion` - 弹窗/面板从触发源动效出现（scale+fade 或滑入），保留空间语境（HIG、MD）
- `navigation-direction` - 前进导航向左/上动效，后退向右/下：方向保持逻辑一致（HIG）
- `layout-shift-avoid` - 动画不得引起布局重排或 CLS；位置变化用 transform
- `cancellable-state-transitions` - 快速状态变化必须安全地取消/替换先前的微交互，显式设置新的最终状态，绝不把正确性押在 animation-end 事件上

### 8. 表单与反馈（MEDIUM）

- `input-labels` - 每个输入框有可见标签（不要只放 placeholder）
- `error-placement` - 具体错误显示在相关字段下方，并用 aria-describedby 关联
- `submit-feedback` - 提交时先 loading，再显示成功/错误状态
- `ime-composition-enter` - Web 自定义 Enter 快捷键要先取消已处理 Enter 的默认行为，再做 isComposing/229 守卫；IME 确认与提交分开，保留换行/修饰键策略，并提供显式提交按钮
- `required-indicators` - 标出必填字段（如星号）
- `empty-states` - 无内容时给出有用的提示和动作
- `toast-dismiss` - toast 3-5 秒自动消失
- `confirmation-dialogs` - 破坏性操作前先确认
- `input-helper-text` - 复杂输入框下方给常驻帮助文本，不要只放 placeholder（Material Design）
- `disabled-states` - 禁用元素用降低不透明度（0.38–0.5）+ 光标变化 + 语义属性（MD）
- `progressive-disclosure` - 复杂选项渐进展开；不要一上来就压垮用户（Apple HIG）
- `inline-validation` - 失焦时校验（不是每敲一键）；用户输完才显示错误（MD）
- `input-type-keyboard` - 用语义 input 类型（email、tel、number）唤起正确的移动键盘（HIG、MD）
- `password-toggle` - 密码框提供显示/隐藏切换（MD）
- `autofill-support` - 用 autocomplete / textContentType 属性让系统可自动填充（HIG、MD）
- `undo-support` - 破坏性或批量操作允许撤销（如“撤销删除”toast）（Apple HIG）
- `success-feedback` - 完成的操作用简短视觉反馈确认（对勾、toast、颜色闪烁）（MD）
- `error-recovery` - 错误消息必须带清晰的恢复路径（重试、修改、帮助链接）（HIG、MD）
- `multi-step-progress` - 多步流程显示步骤指示器或进度条；允许后退（MD）
- `form-autosave` - 长表单自动存草稿，防止误关丢数据（Apple HIG）
- `sheet-dismiss-confirm` - 有未保存改动的面板/弹窗关闭前先确认（Apple HIG）
- `error-clarity` - 错误消息要说明原因 + 怎么改（不能只说“输入无效”）（HIG、MD）
- `field-grouping` - 相关字段按逻辑分组（fieldset/legend 或视觉分组）（MD）
- `read-only-distinction` - 只读状态在视觉和语义上都与禁用不同（MD）
- `focus-management` - 提交失败且多处出错时，聚焦错误摘要；没有摘要时聚焦第一个无效字段
- `error-summary` - 提交失败后在顶部放可聚焦的摘要，每项链接到对应无效字段，并保留字段内联错误
- `touch-friendly-input` - 移动端输入框高度 ≥44px，满足触控目标要求（Apple HIG）
- `destructive-emphasis` - 破坏性操作用语义危险色（红），并与主要操作视觉分离（HIG、MD）
- `toast-accessibility` - toast 不得抢焦点；用 aria-live="polite" 向读屏器播报（WCAG）
- `aria-live-errors` - 表单错误用 aria-live 区域或 role="alert" 通知读屏器（WCAG）
- `contrast-feedback` - 错误与成功状态色要达 4.5:1 对比度（WCAG、MD）
- `timeout-feedback` - 请求超时要给出清晰反馈和重试选项（MD）

### 9. 导航模式（HIGH）

- `bottom-nav-limit` - 底部导航最多 5 项；图标配文字标签（Material Design）
- `drawer-usage` - 抽屉/侧栏放次级导航，不放主要操作（Material Design）
- `back-behavior` - 返回导航必须可预期且一致；保留滚动/状态（Apple HIG、MD）
- `deep-linking` - 所有关键页面可通过深链 / URL 到达，供分享和通知使用（Apple HIG、MD）
- `tab-bar-ios` - iOS：顶层导航用底部 Tab Bar（Apple HIG）
- `top-app-bar-android` - Android：主结构用带导航图标的 Top App Bar（Material Design）
- `nav-label-icon` - 导航项要有图标和文字标签；纯图标导航损害可发现性（MD）
- `nav-state-active` - 当前位置在导航中要视觉高亮（颜色、字重、指示器）（HIG、MD）
- `nav-hierarchy` - 主导航（tabs/底栏）与次级导航（抽屉/设置）清晰分开（MD）
- `modal-escape` - 弹窗和面板要有清晰的关闭/消失可供性；移动端下滑关闭（Apple HIG）
- `search-accessible` - 搜索要容易到达（顶栏或 tab）；提供最近/建议查询（MD）
- `breadcrumb-web` - Web：3 层以上的层级用面包屑帮助定位（MD）
- `state-preservation` - 返回时要恢复之前的滚动位置、筛选状态和输入（HIG、MD）
- `gesture-nav-support` - 支持系统手势导航（iOS 侧滑返回、Android 预测性返回）且不冲突（HIG、MD）
- `tab-badge` - 导航项上的徽章少用，只标未读/待处理；用户访问后清除（HIG、MD）
- `overflow-menu` - 操作超出可用空间时用溢出/更多菜单，不要硬塞（MD）
- `bottom-nav-top-level` - 底部导航只放顶层页面；绝不在其中嵌套子导航（MD）
- `adaptive-navigation` - 大屏（≥1024px）优先侧栏；小屏用底部/顶部导航（Material Adaptive）
- `back-stack-integrity` - 绝不悄悄重置导航栈，也不要意外跳回首页（HIG、MD）
- `navigation-consistency` - 导航位置在所有页面保持一致；不随页面类型改变
- `avoid-mixed-patterns` - 同一层级不要混用 Tab + 侧栏 + 底部导航
- `modal-vs-navigation` - 弹窗不用于主导航流程；它会打断用户路径（HIG）
- `focus-on-route-change` - 页面切换后把焦点移到主内容区，服务读屏器用户（WCAG）
- `persistent-nav` - 核心导航在深层页面仍要可达；不要在子流程里完全藏起来（HIG、MD）
- `destructive-nav-separation` - 危险操作（删号、登出）要与普通导航项视觉和空间分离（HIG、MD）
- `empty-nav-state` - 导航目的地不可用时说明原因，不要悄悄隐藏（MD）

### 10. 图表与数据（LOW）

- `chart-type` - 图表类型匹配数据类型（趋势 → 折线，比较 → 柱状，占比 → 饼图/环图）
- `color-guidance` - 用可访问色板；避免只用红/绿配对，照顾色觉障碍用户（WCAG、MD）
- `data-table` - 提供表格替代以保证可访问性；只有图表对读屏器不友好（WCAG）
- `pattern-texture` - 用图案、纹理或形状补充颜色，让数据不靠颜色也能区分（WCAG、MD）
- `legend-visible` - 始终显示图例；放在图附近，不要脱节到滚动折叠线下方（MD）
- `tooltip-on-interact` - 悬停（Web）或轻点（移动端）时提供 tooltip/数据标签，显示精确值（HIG、MD）
- `axis-labels` - 坐标轴标明单位和可读刻度；移动端避免截断或旋转标签
- `responsive-chart` - 小屏幕上图表要重排或简化（如横向柱状代替纵向、减少刻度）
- `empty-data-state` - 无数据时显示有意义的空状态（“暂无数据” + 引导），不要空白图表（MD）
- `loading-chart` - 图表数据加载中用骨架或 shimmer 占位；不要显示空坐标轴框
- `animation-optional` - 图表进场动画必须尊重 prefers-reduced-motion；数据要能立即读取（HIG）
- `large-dataset` - 1000+ 数据点先聚合或抽样；细节用下钻提供，不要全部渲染（MD）
- `number-formatting` - 轴和标签上的数字、日期、货币用本地化格式（HIG、MD）
- `touch-target-chart` - 可交互图表元素（点、段）要有 ≥44pt 点击区域，或触按时放大（Apple HIG）
- `no-pie-overuse` - 超过 5 个类别避免饼图/环图；改用柱状图更清晰
- `contrast-data` - 数据线/柱对背景 ≥3:1；数据文本标签 ≥4.5:1（WCAG）
- `legend-interactive` - 图例应可点击，切换系列可见性（MD）
- `direct-labeling` - 小数据集直接在图上标值，减少视线移动
- `tooltip-keyboard` - tooltip 内容要键盘可达，不能只靠悬停（WCAG）
- `sortable-table` - 数据表要支持排序，用 aria-sort 标示当前排序状态（WCAG）
- `axis-readability` - 轴刻度不能拥挤；保持可读间距，小屏自动跳隔
- `data-density` - 单图信息密度要有限，避免认知过载；需要时拆成多张图
- `trend-emphasis` - 强调数据趋势而不是装饰；避免遮蔽数据的重渐变/重阴影
- `gridline-subtle` - 网格线用低对比（如 gray-200），不与数据抢注意力
- `focusable-elements` - 可交互图表元素（点、柱、扇区）必须键盘可导航（WCAG）
- `screen-reader-summary` - 提供文字摘要或 aria-label，向读屏器描述图表的关键结论（WCAG）
- `error-state-chart` - 数据加载失败要显示带重试的错误消息，不要残缺/空白图表
- `export-option` - 数据密集产品提供图表数据的 CSV/图片导出
- `drill-down-consistency` - 下钻交互要保持清晰返回路径和层级面包屑
- `time-scale-clarity` - 时间序列图要清楚标明时间粒度（日/周/月）并允许切换
