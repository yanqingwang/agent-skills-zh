<!-- AUTO-GENERATED from apple-release.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/apple-release.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

# Apple App Store 发布

<!-- Ported from time-attack/gstack (GStack 2) APPLE-RELEASE.md, refined
     across 21 live App Store releases. Portions copyright (c) 2026
     Sina Matian, time-attack/gstack, MIT. Adapted to gstack main's
     architecture: decision-store bins, the Third-Party Web Actions
     contract, and an idempotency log in place of the fork's durable-state
     wrapper. All credential examples are placeholders, never live formats. -->

发布目标是 Apple 平台应用时适用：仓库含 `.xcodeproj` 或
`.xcworkspace`，或带 app 产物的 Swift package。在 Step 1 的分支门与
任何预检之前读本节。本适配器把 ship 的判断力延伸到 App Store 全旅程，
每次上传或提交都按持久外部效果对待（下文的幂等契约）；但商店分发是
它自己的发布路径，不是仓库落地：ship 的分支/PR 仪式（feature 分支
门、commit-review-PR 流水线、合并队列）仅在用户要求落地仓库改动时适
用。发布到 App Store 或 TestFlight 的用户从所在分支直接走本适配器；
base 分支上的干净工作树是归档与上传的正常有效状态。绝不为分支拓扑
中止 App Store 发布。

**文档预检：** 归档/上传/提交之前，Read
`~/.claude/skills/gstack/ship/sections/documentation.md` 并对其审计门
以 `read-only` 模式在选定发布源上执行，base 分支上也要。本审计不授
权任何源码编辑、改变状态的 Git 操作或仓库落地仪式。分发之前解决阻塞
项或取得显式点名的文档风险例外；在最终商店发布报告里写明
`updated`/`current`/`blocked` 与任何例外。此指针不改变下文的 App
Store 权限。

一个工具跑完整场发布：机器级 fastlane。`produce`（应用记录与 bundle
ID）、`cert` 与 `sigh`（签名）、`gym`（归档与签名导出）、`pilot`
（TestFlight）、`deliver`（元数据、截图、提交审核）、`frameit`（设备
边框）。缺失时安装（`brew install fastlane`），一行宣布，不发问；发
布授权涵盖机器工具安装。绝不安装其他 App Store CLI 工具，运行期间绝
不向用户提及 API key、`.p8` 文件、会话或任何凭证格式；唯一例外是收尾
报告里一行常设凭证披露（见"商店收尾"），点名发布创建的持久 key，
让用户之后可以吊销。他们付了 99 美元是要发布的，发布本身不给用户项
目添新依赖。

只有构建环节需要 Mac。归档、签名与二进制上传走 Xcode 仅限 macOS 的
工具链，Apple 没有在别处提供，也没有工具能绕开。非 macOS 宿主上如
实说明，然后只把这几个环节路由到 macOS CI runner（GitHub Actions
的 `macos` runner 执行同样的 `gym` 与 `deliver`/`pilot` 命令，铸出的
上传 key 作为 CI secret 提供；key 认证正是 CI 想要的）；登录、key
铸造、元数据、截图、定价与提交判断是普通 API 工作，留在用户机器上。
绝不声称整场发布离开 Mac 不可能，也绝不假装构建环节在那里可行。

## 唯一的授权时刻

计划两次例行交互。真正的阻塞可能需要安全或点名的文档风险决策；为
那个决策 STOP，而不是把发布授权当豁免。

第一，开场：确认用户持有付费 Apple Developer Program 会员（99 美元/
年，App Store 与 TestFlight 都要求）并授权发布。

定价归入同一口气，每个应用只此一次：先查决策存储
（`bin/gstack-decision-search --scope repo --query "pricing"`），然
后把免费还是付费（付费则价格）放进授权问题里问，绝不作为单独的打
断；把答案持久化
（`~/.claude/skills/gstack/bin/gstack-decision-log`，scope `repo`），
之后的发布不再重问。付费答案要在当场诚实点名一次性的 Paid Apps 银
行/税务协议，因为它没签就什么都卖不了。价格是发布决策，agent 绝不
静默默认：免费发布无法撤销。

Apple 登录发生在同一时刻：经宿主的交互命令路径跑
`fastlane spaceauth -u <apple-id>`（Claude Code 里用户输入
`! fastlane spaceauth -u <email>`，密码与一次双因子码在会话内直达
Apple；仅当宿主没有交互路径时才退到单独终端窗口）。打印出的会话
token 不进 transcript；`~/.fastlane/spaceship/` 里的缓存 cookie 才是
fastlane 真正用的凭证。密码与 token 绝不存储、回显或记录；会话过期
就重跑同一条命令。

首次登录之后立即从会话铸造永久上传 key（"归档与上传"第 4 步）；该
key 已在 `~/.gstack/apple/api-key.json` 且不需要新应用记录时，整个
跳过登录：重复发布零登录完成授权与执行。

第二，仅当预检发现图标或截图缺失：下方的商店素材问题。

阻塞清除后，工具安装、上传、商店与提交都在授权覆盖内，不再发问。授
权菜单、工具选择题、计划确认与逐步旁白请求都是契约违规。

无会员：STOP App Store 路径。提议经 Third-Party Web Actions 契约
（本 Skill 更早处）陪同走 developer.apple.com 注册（由用户自己完成
购买；激活可能要一两天），并诚实点名免费账户的天花板：仅能在用户自
己的设备上做个人团队安装，7 天后过期，无 TestFlight、无 App Store。

## 发布预检

归档之前解析并验证。打印出的变更边界授权之内的就修；其余报告为阻塞
发现。

- 签名：app target 上的开发团队；无既有证书时 `cert` 与 `sigh` 铸造
  分发证书与 App Store 描述文件。
- 版本：用户可见的营销版本，以及严格大于该版本已上传过的任何构建的
  构建号。
- 依赖：`xcodebuild -resolvePackageDependencies` 成功；存在
  `Podfile` 或 `Cartfile` 时其安装步骤已跑、lockfile 为最新。
- App Store 校验阻塞项：完整的应用图标集（含 1024pt 营销图标）、
  启动屏、应用触碰的每个隐私受限 API 的用途描述串、必需的隐私清单、
  出口合规答案（`ITSAppUsesNonExemptEncryption`）、合理的部署目标。

## 商店素材

仅当预检发现图标或截图缺失时问一次，全程第二次也是最后一次允许的问
题，之后按选择执行不再提示。每个应用只此一次：问之前先查决策存储
（`bin/gstack-decision-search --scope repo --query "store assets"`）；
已定的选择（包括"推迟截图"或"仅 TestFlight"）静默应用，绝不重问。
用户答复后持久化
（`~/.claude/skills/gstack/bin/gstack-decision-log`，scope `repo`），
之后的运行不再问；用户改主意靠说出口，不靠被反复追问。提供：

- **应用图标**：SnapAI（`npx snapai`，应用图标 agent skill）用用户自
  己的图像生成 key 生成单张 1024×1024；Xcode 15+ 从这一张派生全部
  尺寸。
- **营销截图，免费本地无 API key**：app-store-screenshots deck 编辑
  skill。搭好脚手架，用模拟器截图与利益点标题预填其 deck JSON，导出
  覆盖全部必需 iPhone 尺寸的一套（导出可无头自动化）。营销级不要求
  图像后端；该 skill 在装时就绝不声称截图需要 API key。
- **朴素边框，免费本地**：模拟器里截取构建好的应用并用 fastlane
  `frameit` 加框；不想要设计感 deck 时的最小选项。
- **AI 增强营销截图**：aso-appstore-screenshots agent skill（利益点
  标题、拆分面板、精确 App Store 尺寸）；唯一需要用户自己图像生成
  key 的选项；在装时遵循其工作流，不重新实现。
- **用户自带文件**：永远是有效答案；校验尺寸后继续。

提问时基于对已装 skill 的**实时**检查构建选项，绝不凭记忆或更早的对
话轮。app-store-screenshots deck 编辑 skill 在装时，其免费无 key 选
项必须出现在列表里；漏掉它等同于声称截图需要 API key，是契约违规。
素材已齐则整节跳过。退出时宣布生成了什么。

## 归档与上传

1. 用 `gym` 归档并导出签名的 Release 构建（它驱动 xcodebuild 与预检
   铸好的签名）。有自定义归档要求的项目可直接落
   `xcodebuild archive`；两条路产物都是 App Store 签名的 `.ipa`。
2. 上传是外部效果：在持久效果契约下跑 `pilot`（TestFlight）或
   `deliver`（App Store）：执行前把 key
   `appstore.upload.<bundle-id>.<build>` 追加到
   `$GSTACK_STATE_ROOT/projects/$SLUG/apple-effects.log`（在同一
   条读/追加命令里解析状态根与 slug）；key 已在（崩溃、重试）则视
   上传为可能已完成，绝不重跑。歧义时绝不再上传；先查 App Store
   Connect 上的构建。
3. 缓存会话、铸出的 key 与每个凭证文件都是 env 或文件级密钥：绝不进
   argv、绝不回显、绝不提交。
4. 绝不索要 app 专用密码：会话自己铸造上传 key。

   按 fastlane 文档化的认证方式，Apple 的二进制上传工具
   （iTMSTransporter，`deliver`/`pilot` 上传 `.ipa` 时 shell 调用它）
   不接受 web 会话：只收 App Store Connect API key 或 app 专用密码，
   Apple 的错误 `-22938`（"Sign in with the app-specific password"）
   就是 Transporter 在说这件事。

   那不是门也不是问题，因为 web 会话自己静默创建 key：经 fastlane
   内置的 spaceship（`Spaceship::Tunes.login(<apple-id>)` 复用缓存
   cookie，然后走原始客户端请求），
   `POST https://appstoreconnect.apple.com/iris/v1/apiKeys`，JSON:API
   请求体限定在本次发布的应用而非全部：
   `{data:{type:"apiKeys",attributes:{nickname:"gstack-upload",allAppsVisible:false,roles:["APP_MANAGER"],keyType:"PUBLIC_API"},relationships:{apps:{data:[{type:"apps",id:"<asc-app-id>"}]}}}}`，
   其中 `<asc-app-id>` 是 App Store Connect 应用 id（来自 `produce`
   的输出，或
   `GET https://appstoreconnect.apple.com/iris/v1/apps?filter[bundleId]=<bundle-id>`）。

   `allAppsVisible:false` 加显式 `apps` 关系是有意的最小权限：
   `allAppsVisible:true` 的 APP_MANAGER key 是对团队每个应用的常设权
   限，机器日后失守时是无谓的爆炸半径。`apps` 关系是必需而非可选：
   无应用关联的 key 什么也看不到，上传会报权限错误，所以把范围定到
   目标应用，而不是只翻 flag。

   应用记录存在后才铸造（新应用因此先跑 `produce`）。

   然后
   `GET .../iris/v1/apiKeys/<id>?fields[apiKeys]=privateKey`：
   `privateKey` 属性是完整 PEM 文件的 base64：恰好解码一次，立即写
   `~/.appstoreconnect/private_keys/AuthKey_<id>.p8`（0600），它只在
   创建时可供下载。issuer ID 来自
   `GET https://appstoreconnect.apple.com/olympus/v1/session` 的
   `provider.publicProviderId`。

   把 key id、issuer id 与 key 内容记为 fastlane api-key JSON，存
   `~/.gstack/apple/api-key.json`（0600），此后 `deliver`/`pilot` 一律
   用 `api_key_path`。

   该 key 永不过期，所以同一应用的后续发布全部免登录；发布另一个应用
   时把该应用关联到 key 上（`PATCH .../iris/v1/apiKeys/<id>` 加入
   `apps` 关系）或另铸一把应用限定的 key，因为 key 有意不做全应用。
   会话只在 `produce`（Apple 公开 API 建不了应用记录）、重新关联、
   key 被吊销后重铸时仍然需要。

   key 铸造尚未尝试就声称用户必须自己生成任何凭证，是契约违规。

   碰凭证之前先给错误分类：只有错误明说（401/403、会话无效或过期、
   Apple 原文的"sign in"、"app-specific password"）才是认证失败。
   `Spaceship::UnexpectedResponse`、属性缺失/无效、校验或预检错误是
   元数据问题：修载荷（例如 Apple 扩展的年龄分级属性
   `lootBox`、`ageAssurance`、`parentalControls`、`messagingAndChat`，
   在 `app_rating_config.json` 里）并从 CLI 重试。把元数据错误当成凭
   证问题处理是契约违规。
5. Apple 发布范围内，本适配器覆盖 Third-Party Web Actions 契约（本
   Skill 更早处）：通用的 agent 浏览器提议绝不适用于此处的 App
   Store Connect、Apple ID 或凭证工作。整场发布就是 CLI（fastlane）
   加上述例行交互与阻塞决策；本适配器允许的唯一浏览器使用，永远只有
   文末点名的付费应用协议/银行/税务残留。为此旅程中的任何其他事情
   打开浏览器，无论谁驱动，都是契约违规。

   真实错误确实逼出兜底时，先逐字引用错误，然后按此顺序升级：第一，
   按第 4 步从会话铸造（或重铸）上传 key，带 `api_key_path` 重试上
   传；磁盘无 key 的上传认证错误说明铸造被跳过，不是用户欠一个凭
   证。

   第二，铸造本身因会话错误失败时，请用户重新登录（与最初授权相同的
   `! fastlane spaceauth -u <apple-id>` 时刻），重铸，重试。

   只有全新会话仍铸不出 key 时，即登录的 Apple ID 在其团队不是
   Admin 或 Account Holder 的权限拒绝，app 专用密码路径才打开，且
   唯一形态是自助：用户在任意设备生成密码，经宿主会话内的掩码提示
   输入 macOS 钥匙串（`fastlane fastlane-credentials add --username
   <apple-id>`），然后重试上传。

   绝不提供或建议用浏览器驱动创建凭证：任何 agent 浏览器、任何密
   码、key 或 token、任何说法都不行。
6. App Review 联系信息（姓名、邮箱、电话）是提交的必需元数据：从已
   登录的 Apple ID 与 git config 推断姓名与邮箱，在授权时刻一次性收
   集电话号码，存进决策存储，永不重问。联系信息是元数据，不是运行
   中途要宣布的阻塞门。

## 商店收尾

`produce` 在运行中已建好应用记录与 bundle ID：绝不把应用记录称作手
动门。在授权时刻定下的价格经 App Store Connect 价格计划端点落实
（经会话或铸好的 key `POST /v1/appPriceSchedules`）：fastlane 的
`price_tier` 选项对现行 API 是坏的（"'prices' is not a relationship
on 'apps'"），绝不经它路由定价，也不把它的失败说成账户问题。
`deliver` 负责商店页面所需的其他一切：描述、关键词、本地化、按设备
尺寸上传截图、挂接已上传的构建、提交审核；用户要求中间轮时 `pilot`
管理 TestFlight 组与测试者。提交遵循同一持久效果契约，key 为
`appstore.submit.<bundle-id>.<version>`；歧义时先查 App Store
Connect 再重跑。之后从 CLI 监控审核状态。

永远只剩 web 的事：付费 Apple Developer Program 会员购买本身（前提，
不是发布步骤），以及仅付费应用的一次性 Paid Apps 协议（银行与税
务）；对这两件事在任何手工清单之前，按 Third-Party Web Actions 契
约提议 agent 浏览器陪同。免费应用全程不需要浏览器。提交后报告
App Review 通常一两天内答复，然后收尾；审核结果不是本工作流能 hold
住的门。在**同一份**收尾报告里披露发布创建的持久凭证，一行，每次运
行一次："This created an App Store Connect API key (`gstack-upload`,
scoped to this app) that persists for future releases; revoke it
anytime at App Store Connect → Users and Access → Integrations, or
delete `~/.gstack/apple/api-key.json` locally."这是本适配器开头
"运行中不谈凭证"规则有意的例外：否则用户永远不会知道自己的账户与
磁盘上多了一个常设凭证，它也就永远进不了他们的吊销清单。退出时披
露，不是运行中的提问，唯一授权时刻的契约因此成立。
