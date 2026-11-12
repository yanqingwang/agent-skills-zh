> **中文汉化版** · 上游：[tt-a1i/archify](https://github.com/tt-a1i/archify) · 原文件：`archify/references/brand-marks.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 品牌标识（Brand marks）

只有当真实的产品、提供商、模型家族、渠道或服务身份有助于阅读者理解时，才使用
品牌标识。语义 `type` 仍然说明节点做什么；`brand` 说明它是谁的产品。

## Agent 决策路径（Agent decision path）

1. 请求中出现可识别的品牌时，先搜索内置目录：

   ```bash
   node bin/archify.mjs brands "Claude" --json
   ```

2. 把返回的规范 ID 放进节点、参与者或状态：

   ```json
   {
     "id": "planner",
     "type": "backend",
     "label": "Claude",
     "brand": "claude"
   }
   ```

3. 目录中没有匹配、而用户提供了官方网站时，显式抓取其图标：

   ```bash
   node bin/archify.mjs brands capture "https://partner.example.com" --json
   ```

   把命令返回的摘要钉定（digest-pinned）`brand` 值放进绘制的节点：

   ```json
   {
     "id": "partner",
     "type": "external",
     "label": "Partner portal",
     "brand": {
       "url": "https://partner.example.com",
       "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
     }
   }
   ```

4. 既无匹配、也没有用户提供的 URL 时，省略 `brand`。不要凭空造一个 URL，也不
要悄悄指派一家外观相似的公司。

知名品牌的 URL 直接解析为内置矢量图，不走网络。对发现的图标 `href` 属性，抓
取操作会在 URL 解析之前做一次解码，覆盖基础命名引用 `amp`、`quot`、`apos`、
`lt`、`gt`（及其定义的大写别名），加上十进制与十六进制数字引用。因此
`/icon.png?v=1&amp;size=32` 请求的是 `/icon.png?v=1&size=32`。URL 百分号转义
保持原样；嵌套转义不递归解码。这个有界解码器不添加通用 HTML 解析器，也不支持
全部 HTML 命名实体。
HTML 读取在注释、原始文本元素和带引号属性之外遇到显式的 head 结束标记即停止
，包括这些标记跨越网络分块的情况。256 KiB 的 head 上限和抓取时限仍然适用；he
ad 之后更大的 body 不用于图标发现。
图标候选来自注释、原始文本和模板内容之外的完整 `link` 标签。属性值和形近名称
（如 `data-href`）不能充当图标声明；带引号的 `>` 字符留在其标签之内。
对 `text/html`，发现逻辑把 `noscript` 内容当作原始文本，与启用脚本的 HTML 解
析一致；抓取不执行脚本。这一排除不适用于 `application/xhtml+xml`，其中
`noscript` 内的链接仍可被发现。XHTML 空元素（如 `<script />` 和
`<template />`）不会隐藏其后的链接；同样的尾部斜杠在 `text/html` 中不会闭合
这些元素。
未知 URL 的抓取只接受有界的光栅图像格式，拒绝凭证、非标准公网端口、私有或链
路本地目标，使用有界并发和单一总时限，并返回被抓取内容的摘要。后续 render 与
 validate 操作要求与该摘要完全一致；被拒绝、不可用、已变更、超尺寸或不安全的
内容一律失败即拒绝（fail-closed），而不是悄悄改变产物。

抓取回执、节点元数据和 SVG/HTML 中的远程品牌溯源信息保留源 URL 的 HTTP(S) sc
heme、主机、端口和路径，但省略 userinfo、查询串和片段。绘制的 `brand.url` 与
全部下载/重定向 URL 保持不变，因此既有的钉定仍能复现同样的字节和摘要。带凭证
的下载 URL 仍然被拒绝。内置标识保留其记录在目录中的溯源信息。

公开的来源链接指向原始站点/路径，未必是一个可下载资产：去掉签名查询或基于查
询的页面选择器可能让该链接失效或变得不够具体。若存在稳定公开、且展示目标图标
的落地页，优先抓取它；不要在未重新抓取并验证来源的情况下编辑既有钉定的 URL。
路径会被保留，因此这种规范化不是通用的 URL 机密清洗器。

从会抓取非活动 HTML 标记（包括 `noscript`）的版本升级之后，既有 URL 钉定可能
因发现逻辑现在选中了不同图标而以 `brand/digest-mismatch` 失败。检查目标图标
，对同一 URL 重跑上面的抓取命令，并用返回的钉定值显式替换绘制的 `brand` 值。
既有钉定不会被自动改写，摘要校验仍然强制执行。

对 ICO 抓取，每个目录项都必须在完整目录之后、且在下载文件之内引用一个非空图
像范围。这项边界检查同样适用于复现既有钉定的场景。PNG/DIB 载荷、多图像、共享
或乱序范围、尾部字节仍受支持；该检查不解码像素，也不保证其他方面有界的载荷一
定可解码。某个 ICO 候选被拒绝不阻止尝试后续图标。

页面、图标和重定向请求发送 `Accept-Encoding: identity`。抓取不解压响应体：响
应声明了其他内容编码并成功返回时，连接会被关闭并显式拒绝。这使既有字节上限与
钉定摘要始终对应未编码的表示。稍后一个可用的图标仍可能成功；否则保留编码错误
，而不是被一个无关的 favicon 404 掩盖。

最终产物在打开时绝不抓取品牌资产。内置矢量与经摘要验证的抓取站点图标保持嵌入
在 SVG、PNG、WebP、JPEG、Share Card 与 WebM 导出中。

用 `node bin/archify.mjs brands --json` 检查全部规范 ID、别名、类别、域名与
溯源信息。当前类别覆盖 AI、云、工程、数据、协作、业务系统、渠道、语言与框架
。
