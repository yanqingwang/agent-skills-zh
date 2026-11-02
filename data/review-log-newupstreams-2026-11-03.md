# 新上游批次校验报告（review log · 2026-11-03 第五次全量检索）

**校验日期：2026-11-03** · **范围**：10 个新上游、18 个翻译件、513 个原样件（累计 60 登记 / 59 监控 / 156 翻译件 / 4632 原样件）
**校验者**：父会话机械检查（YAML 解析 / 声明块 / 代码块字节比对 / blob SHA 全量核对）+ 10 个翻译代理自检回报
**结论：PASS（18/18 翻译件合规；513/513 原样件 blob SHA 与上游 HEAD 一致，diff=0）**

## 本批收录（10 新上游）

| 上游 | 星标 | License | 收录 |
|---|---:|---|---|
| nextlevelbuilder/ui-ux-pro-max-skill | 144,260 | MIT | ui-ux-pro-max（整目录 74 件） |
| pbakaus/impeccable | 100,404 | Apache-2.0 | impeccable（整目录 58 件） |
| cloudflare/security-audit-skill | 57,337 | MIT | security-audit（整目录 20 件，防御性安全审计） |
| kepano/obsidian-skills | 50,642 | MIT | 全部 6 skill（obsidian-cli/markdown/bases/json-canvas/defuddle/knap） |
| Nutlope/hallmark | 45,939 | MIT | hallmark（整目录 184 件） |
| zarazhangrui/frontend-slides | 31,756 | MIT | frontend-slides（整目录 79 件，取 plugins/ 路径） |
| wheresryan22/anatomy | 24,097 | MIT | anatomy（SKILL.md + references/kit/examples 90 件） |
| google/skills | 21,799 | Apache-2.0 | gcloud 旗舰（4 件） |
| muratcankoylan/Agent-Skills-for-Context-Engineering | 18,288 | MIT | context-degradation + long-horizon-prompting 旗舰（8 件） |
| greensock/gsap-skills | 17,747 | MIT | gsap-core/scrolltrigger/react（3 单文件） |

目录新增子类别：`toolbox/obsidian/`、`toolbox/cloud/`、`developer/framework/`、`creator/slides/`。

## 机械校验（全量）

- **翻译件**：18/18 frontmatter YAML 解析通过、`name` 保留英文、`description` 已译、声明块三行逐字且位置正确（frontmatter 后空行 → 声明块 → 空行 → 正文）、GLOSSARY 相对链接 `../../../../GLOSSARY.md` 有效
- **原样件**：sync_daily 首登流程对全部 513 件做本地 `git hash-object` 与上游 git tree blob SHA 比对，全部一致（verbatim刷新=0），等价逐字节一致
- **lint_zh_style**：初检 3 件触发 H1 破折号信号（defuddle / context-degradation / gsap-core），已定点改写（定义式「——」改冒号、修辞式改句式）后复检 **0 信号**
- **星标快照**：60 上游全部补 `stars_snapshot_2026-11-03`（gh api 实抓），README 登记表以新快照重排

## 文件级 License 核验（吸取第六批 ECC 事件教训）

18 件翻译前逐件核验源 frontmatter：anatomy 含 `license: MIT`（与仓库一致，译文原样保留该字段）；impeccable 源为 `license: Apache 2.0`（非 SPDX 写法，同一许可）；其余 16 件无文件级 license 字段。未发现仓库级与文件级不一致情形。

## 保留英文的功能性标记（抽样要点）

- security-audit：状态枚举（confirmed/needs_validation/deferred 等）、严重级别（critical…informational）、报告文件名（findings.json/REPORT.md 等）
- gsap-core/scrolltrigger/react：全部 API 名、vars 键、ease 名字符串、代码示例逐字节
- ui-ux-pro-max：CLI 参数、domain 枚举（ux/style/product…）、影响等级标签、规则 ID
- hallmark：Genre 枚举、sloplint 结果（FAIL/REFLEX/WARN）、流程阶段名（保留英文+括注）
- impeccable：全部子命令（craft/critique/audit/polish…）、CONTEXT_STALE 标记
- gcloud：Denylist 分类、`run_gcloud_command` MCP 工具名、归因标记 `skill:gcloud`
- context-degradation / long-horizon-prompting：claim-* 证据 ID、四桶策略名（Write/Select/Compress/Isolate + 中文注）
- obsidian 六件：CLI 命令与参数、Bases 公式/过滤器函数名、JSON Canvas 键名、格式枚举

## 过程事件

- **anatomy 误拷 .git（已修复）**：anatomy 的收录源是仓库根目录，首版拷贝脚本 rglob 未排除 `.git/`，29 件 git 内部文件混入 verbatim 并被 sync_daily 报 ⚠️。处置：删除 `skills/designer/design/anatomy/.git/`，从 manifest verbatim 移除 29 件，重置 10 新上游同步状态后重跑首登——干净通过（verbatim 全一致，无 ⚠️）。教训：**以仓库根为收录源时，rglob 必须排除 `.git/`**。
- **同步引擎顺带同步**：首登运行同时发现 5 个存量上游自 CI 2026-11-02 晨跑后又有新提交（morluto/rea、mvanhorn/last30days-skill、K-Dense-AI、garrytan/gstack 等），按设计自动刷新其原样件（逐字节），并为 gstack 13 个翻译件开重译工单（见 [data/sync-pending-retranslation.md](sync-pending-retranslation.md)）。rea / last30days 的翻译件本轮未再变化，其早前工单以 CI 持久化状态为准。
- **并发限制**：翻译代理平台并发上限，10 组分 4 批派发，全部完成。
