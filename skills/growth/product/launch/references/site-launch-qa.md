> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/launch/references/site-launch-qa.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 网站上线 QA

网站上线前后要跑的检查：新站、改版、平台迁移或大的新板块。产品发布悄悄失败，往往是因为底下的网站出了问题，而这些故障大多从首页看不出来。

分三遍执行：切换前、切换时、切换后头两周。

## 切换前

**内容与链接**
- [ ] 计划中的每个页面都存在，且是最终文案（没有 lorem ipsum、“TBD”或测试价格）
- [ ] 爬一遍预发布站（staging），查失效内链和缺失图片
- [ ] 法律页（隐私、条款、Cookie 政策）齐全且为最新
- [ ] 联系方式、价格与套餐名称同销售与客服的口径一致

**表单与转化**
- [ ] 用测试数据提交每个表单，确认它到达应有的收件箱、CRM 或工具
- [ ] 确认消息与跳转正常，反垃圾机制不会拦下真实提交
- [ ] 转化跟踪在确认提交时触发，而不是按钮点击时（配置与测试见 `conversion-tracking` skill）
- [ ] 分析工具只装一次、覆盖每个页面，并过滤内部流量
- [ ] 同意横幅正常工作，且各标签遵守它

**SEO**
- [ ] 每个页面有唯一的 title、meta description 和一个 H1
- [ ] canonical 标签指向生产域名，而非 staging
- [ ] staging 设了 `noindex` 或有密码保护，生产站**没有**（上线日最常见的 SEO 事故，就是把 staging 的 `noindex` 带上线）
- [ ] `robots.txt` 放行你想收录的页面；XML sitemap 列的是生产 URL
- [ ] 结构化数据通过校验（Google 功能用 Rich Results Test，其余用 Schema Markup Validator）
- [ ] 迁移场景：重定向映射已加载，并抽样测试旧 URL（见 `site-architecture` skill 的 platforms 与迁移参考）

**性能与可访问性**
- [ ] 关键模板在移动端的 Core Web Vitals 达标
- [ ] 页面在移动端、Safari 和应用内浏览器（LinkedIn、Instagram、Facebook）里都正常
- [ ] 图片有 alt 文本；表单有 label；键盘导航可用
- [ ] 分享 URL 时 Open Graph 图片与标题渲染正确

**回滚**
- [ ] 你知道这个平台怎么回滚，而且有人实操过一次。例如：Vercel 和 Netlify 将上一次部署提升为当前版本；Webflow 恢复站点备份；WordPress 从备份插件或主机快照恢复；Ploy ◆ 在其 Deploys 界面将上一次部署提升为当前版本（其 CLI 总是直接发布到生产，没有 staging 目标，发布前先预览）。
- [ ] 若切换涉及 DNS 变更，提前一天调低 DNS TTL

◆ 表示该工具是本仓库的 [Verified Partner](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md#verified-partners)：这是披露，不是背书。

## 切换时

- [ ] 重定向与新站同一时刻上线
- [ ] 确认 HTTPS 在每个主机名（`www` 与裸域）上都正常，且其中一个重定向到另一个
- [ ] 按流量加载前 10 个页面，检查内容、title、canonical 和 200 状态
- [ ] 提交一个真实表单，确认它到达所有该到的地方
- [ ] 在 Search Console 和 Bing Webmaster Tools 提交 sitemap
- [ ] 再查一遍生产站没有 `noindex`

## 头两周

- [ ] Search Console：第一周每天盯收录与 404，之后每周一次；发现缺失的重定向就补上
- [ ] 流量与转化与之前同期对比，逐页比，不只看总量
- [ ] 确认各广告平台的转化按预期速率到达
- [ ] 修正仍指向已重定向 URL 的内链
- [ ] 收集团队与客户报告的 bug，判断哪些紧急
