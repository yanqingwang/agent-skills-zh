<!-- AUTO-GENERATED from qa-patterns.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`qa/sections/qa-patterns.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

# 浏览器 QA 方法论

仅为选定的浏览器表面运行。探测前把 diff 与源码对应起来；发现保持黑
盒，诊断归调用方。

共享探索循环拥有执行顺序，不是这些技术阶段。它的检查点规则覆盖基线
之后的每个探测，包括定向、链接、精确回放与额外证据。绝不跨检查点批
量执行。

## 模式

/qa 与 /qa-only 选 Full、Quick 或 Regression。深度 flag 冲突在探测前
问清楚。/review 与 /ship 保持调用方的冒烟与计划边界。Diff-aware 选
的是范围，不是另一遍。时间上限含检查点与证据。耗尽时停止探测并报告
未完成覆盖，绝不跳过检查点。

### Diff-aware（在无 URL 的 feature 分支上自动生效）

用检测到的 base 替换 `main`：

```bash
git diff main...HEAD --name-only
git log main..HEAD --oneline
```

把变更的 controller/route/view/component/model/service/style 映射到
页面。检查 commit/PR 意图；把相关 TODO bug 加进测试计划。静态页面直
接打开。浏览器表面的 API 探测：

```bash
aside repl '
const pg = await openTab("<base-url>");
const r = await fetch("<base-url>/api/...", { method: "GET" });
console.log("API_STATUS=" + r.status);
console.log("API_BODY_START"); console.log((await r.text()).slice(0, 4000)); console.log("API_BODY_END");
await closeTab(pg); console.log("GSTACK_STEP_OK");
'
```

选定并隔离浏览器表面后，URL 缺失时找本地应用：

```bash
for p in 3000 4000 8080; do curl -sI --max-time 3 "http://localhost:$p" >/dev/null 2>&1 && echo "Found app on :$p"; done
```

用提供的 URL 或第一个响应者/staging/预览；都没有就问。测试变更/相邻
页面与流程。Phase 6 报告中标出 TODOS.md 里没有的新 bug。

**无可识别页面：**用 Quick 加发现的交互，即使改的是后端/配置/基础
设施。

### Full（有 URL 时的默认）
访问每个可达页面（5-15 分钟）。打健康分；记录 5-10 个有证据的问题，
绝不编造。

### Quick（`--quick`）
3 分钟：首页 + 前 5 个导航目标。检查加载/console/死链；按健康评分标
尺打分；跳过详细问题/清单，绝不跳过共享循环的门。

### Regression（`--regression <baseline>`）
跑 Full；追加修复/新问题与分数差。保留所提供的既往基线。
基线缺失或不可读是前提缺失：阻塞的是对比，不是 Full 运行。

## 工作流

### Phase 1：初始化

复用调用方的 BROWSER SETUP 与自有产物路径：Aside READY，否则 `$B`
（`NEEDS_ASIDE`/`ASIDE_NOT_RUNNING`）。只在调用方权威内补齐缺失的
setup。把共享循环的 deadline 守卫钳到调用方的运行中 deadline。

### Phase 2：认证（如需要）

按 BROWSER SETUP 的**浏览器访问决策**走 /setup-browser-cookies 或
`$B handoff`/`$B resume`。用户登录/2FA/OTP/CAPTCHA 后重跑。绝不处
理凭证，绝不暴露 cookies/tokens/localStorage。

### Phase 3：定向

挑战之前先确立成功基线。观察页面或交互的预期结果/状态，不只是一次
成功加载。

**读取/流程：**交互时设 `flow = true` 并替换 action/wait。保持一个
脚本；标签页在脚本结束时关闭。

```bash
aside repl '
const flow = false;
const HOOK = `(() => { window.__gstackErrs = window.__gstackErrs || []; const oe = console.error; console.error = (...a) => { window.__gstackErrs.push(a.map(String).join(" ")); oe.apply(console, a); }; window.addEventListener("error", e => window.__gstackErrs.push("uncaught: " + e.message)); window.addEventListener("unhandledrejection", e => window.__gstackErrs.push("unhandledrejection: " + (e.reason && e.reason.message || e.reason))); })()`;
const pg = await openTab("about:blank");
await pg._sendToTarget("Page.addScriptToEvaluateOnNewDocument", { source: HOOK });
await pg.goto("<target-url>");
console.log((await snapshot(pg, { interactive: true })).tree);
await pg.screenshot({ path: flow ? "issue-001-step-1.jpg" : "initial.jpg", type: "jpeg", quality: 60, fullPage: !flow });
if (flow) {
  await pg.locator("e12").click();
  await sleep(500);
  console.log("DIFF_START"); console.log((await snapshot(pg)).diff); console.log("DIFF_END");
  await pg.screenshot({ path: "issue-001-result.jpg", type: "jpeg", quality: 60 });
}
console.log("URL=" + pg.url());
console.log("CONSOLE_ERRORS=" + JSON.stringify(await pg.evaluate(() => window.__gstackErrs)));
console.log("TEXT_START"); console.log((await pg.evaluate(() => document.body.innerText)).slice(0, 20000)); console.log("TEXT_END");
console.log("ASIDE_DIR=" + pwd);
await closeTab(pg); console.log("GSTACK_STEP_OK");
'
```

每张截图：`cp "<ASIDE_DIR>/initial.jpg" "$REPORT_DIR/screenshots/initial.jpg"`
（替换名字），然后 Read 它。绝不删除报告/截图。

**链接：**同源安全路径；仅本地做 HEAD（请求会带 cookies）。

```bash
aside repl '
const pg = await openTab("<target-url>");
const links = await pg.evaluate(() => [...new Set([...document.querySelectorAll("a[href]")].map(a => a.href))].filter(h => new URL(h).origin === location.origin && !/logout|signout|delete|remove|cancel|unsubscribe/i.test(h)));
const local = await pg.evaluate(() => /^(localhost|127\.0\.0\.1|0\.0\.0\.0|::1|\[::1\])$|\.(localhost|test)$/.test(location.hostname));
for (const l of links) { if (!local) { console.log("LINK ?", l); continue; } const r = await fetch(l, { method: "HEAD" }).catch(e => ({ status: "ERR " + e.message })); console.log("LINK", r.status, l); }
await closeTab(pg); console.log("GSTACK_STEP_OK");
'
```

`LINK` 4xx/5xx 或 `ERR` 是死链；`LINK ?` 是未验证。给链接里缺的 SPA
按钮/菜单拍快照。

框架识别：`__next`/`_next/data` = Next.js；`csrf-token` = Rails；
`wp-content` = WordPress；无刷新导航 = SPA。

### Phase 4：探索

从上一个结果选下一个候选。每页用读取脚本配 `page-<name>.jpg`。按
`qa/references/issue-taxonomy.md` 检查布局、控件、空/非法/边界表
单、导航与空/加载/错误/溢出状态。核心流程优先于次要页面；Quick 跳
过此清单。移动端：

```bash
aside repl '
const pg = await openTab("<page-url>");
await pg._sendToTarget("Emulation.setDeviceMetricsOverride", { width: 375, height: 812, deviceScaleFactor: 2, mobile: true });
await sleep(300);
await pg.screenshot({ path: "page-mobile.jpg", type: "jpeg", quality: 60, fullPage: true });
await pg._sendToTarget("Emulation.clearDeviceMetricsOverride", {});
console.log("ASIDE_DIR=" + pwd); await closeTab(pg); console.log("GSTACK_STEP_OK");
'
```

### Phase 5：记录

按共享循环的精确回放规则重试一次以确认每个问题，然后最小化并立即报
告截图证据。回放完成前的超时使确认保持未完成。之后的超时保留已确认
的缺陷，但证据或最小化未完成。

**交互类：**Phase 3 的 `flow = true`。备选：
`pg.fill("#email", "qa@example.com")`、
`pg.getByRole("button", { name: "Save" }).click()`、
`pg.waitForSelector("#done")`、`pg.waitForURL(/dashboard/)`。复现步
骤里链接前后截图。

**静态类**（文案/布局/图片）：一张标注截图加描述。

```bash
aside repl '
const pg = await openTab("<page-url>");
const a = await annotatedScreenshot(pg);
await fs.writeFile(path.join(pwd, "issue-002.png"), Buffer.from(a.base64Image, "base64"));
console.log("ASIDE_DIR=" + pwd); await closeTab(pg); console.log("GSTACK_STEP_OK");
'
```

### Phase 6：收尾

不做新探测，整理留存证据，用本宿主已安装 QA 目录的
`templates/qa-report-template.md` 与调用方的产物/混合报告规则。

报告分数、按严重度排序的 Top 3 Things to Fix、console 健康、严重度
计数、日期、时长、页面/截图数与框架。保存 `baseline.json`：`date`
（YYYY-MM-DD）、`url`、`healthScore`、`issues`（`id`、`title`、
`severity`、`category`）、`categoryScores`。Regression：fixed =
仅既往有、new = 仅当前有。

## 健康评分标尺

逐类计算得分（0-100），再取加权平均。

### 计数
- 跨页面按同一根因去重。用唯一主类别，按首个适用：Links（导航）、
  Accessibility（访问障碍）、Functional（行为）、Performance（速
  度）、Visual（布局）、Content（文案）、UX（摩擦）、Console（其
  余错误）。不重复扣分。
- 排除**未测试**类别；部分分数标**provisional**并注明覆盖。全都没
  测："not scored"。只比较相同覆盖。

### Console（权重 15%）
跨页面按 消息+来源 对可复现错误/异常去重。排除 warning、info 与已
在别处计分的缺陷。
- 0 个错误 → 100
- 1-3 个 → 70
- 4-10 个 → 40
- 11+ 个 → 10

### Links（权重 10%）
统计唯一的死目的地，含客户端路由：可复现的 4xx/5xx、缺失的路由/
锚点或超时。排除预期的认证重定向与资源/API 请求。
- 0 死链 → 100
- 每条死链 → -15（最低 0）

### 逐类打分（Visual、Functional、UX、Content、Performance、Accessibility）
从 100 起；按发现扣分：
- Critical → -25
- High → -15
- Medium → -8
- Low → -3
下限 0。

用最高适用严重度；记录影响/绕过方式：
- **Critical：**数据丢失、安全/隐私暴露，或核心应用对所有用户不可
  用。
- **High：**核心/主要任务被阻塞且无绕过方式。
- **Medium：**任务受损但存在绕过方式。
- **Low：**外观/文案/摩擦问题，不损失任务完成。
Console/Links 用计数替代。

### 权重
| 类别 | 权重 |
|----------|--------|
| Console | 15% |
| Links | 10% |
| Visual | 10% |
| Functional | 20% |
| UX | 15% |
| Performance | 10% |
| Content | 5% |
| Accessibility | 15% |

### 最终得分
用小数权重（15% = 0.15）：
`score = Σ (category_score × weight) / Σ tested weights`。只对最终
得分四舍五入到最近整数（0.5 进位）。

---

## 框架专属指引

- **Next.js：**hydration 错误（`Hydration failed`、`Text content did
  not match`）、`_next/data` 404、链接点击路由（不只是 `goto`）、
  动态内容 CLS。
- **Rails：**开发环境 N+1 警告、表单 CSRF、Turbo/Stimulus 过渡、
  flash 的出现与消失。
- **WordPress：**插件 JS 冲突、登录态 admin bar、`/wp-json/`、混合
  内容。
- **SPA：**快照导航、返回时的过期状态、前进/后退历史、长时间使用后
  console 的泄漏迹象。

## 重要规则

**浏览器发现期间绝不读源码。**用真实的端到端流程；每次交互后查
console。点击目标缺失时先用标注标签，再 ref/CSS 点击。

凭证用 `[REDACTED]`。遵守 BROWSER SETUP 的安全/哨兵规则：每次运行
一次 AskUserQuestion 列出非 LOCAL 变更，先问后动。LOOK 不是 ACT。

**选定浏览器表面后绝不拒绝使用浏览器**，即使改动只在后端。测试/
curl 替代不了它。API/CLI/job/worker/webhook 目标不选它。
