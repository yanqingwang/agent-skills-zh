> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/save-systems/references/versioning-and-migration.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 存档版本控制、迁移与健壮性

本文内容：版本字段；迁移链；备份与回滚；格式取舍；加载时校验清单；存档的存放位置与
云同步（Godot、Unity、Unreal、Steam Cloud、主机平台）；哪些数据要存储、哪些可以重算。

存档的寿命比写它的代码更长。玩家在 v1.0 存的档，期望在更新后的 v1.4 里能继续读取。
从第一个版本起，就要为 schema 演化做好规划。

## 版本字段不可妥协

每份存档都要打上整数 `version` 标记（确有需要时，也可用结构化的 `{major, minor}`）。
加载时：

1. 读取 `version`。
2. 若比当前运行的构建**更新** → 拒绝加载，并给出明确提示（"此存档来自更新版本"）。
   对不认识的字段，不要靠猜。
3. 若**更旧** → 按顺序执行迁移，直到匹配当前版本。
4. 校验，然后实例化。

优先用单个单调递增的整数。只有当你确实要按发布线分支管理存档兼容性时，两段式语义
版本才值得用。

## 迁移链

把每一步迁移写成**纯函数** `vN -> vN+1`，按顺序依次应用。这样任何旧版本都能通过小
而可测的步骤到达当前版本，绝不会出现一个巨大的"把任意版本转成最新"函数。

```python
SAVE_VERSION = 4

MIGRATIONS = {
    1: migrate_1_to_2,   # added "flags" map
    2: migrate_2_to_3,   # split "name" into first/last
    3: migrate_3_to_4,   # inventory items gained a "durability" field
}

def upgrade(data):
    v = data.get("version", 1)
    while v < SAVE_VERSION:
        data = MIGRATIONS[v](data)
        v += 1
        data["version"] = v
    return data
```

准则：

- **增量式改动很简单**：新增字段并给默认值。迁移只需为旧存档填入默认值。
- **重命名/结构调整**：在迁移里完成搬移和转换；游戏代码绝不同时读取新旧两个名字。
- **删除字段**：在迁移里直接丢弃，让后续步骤面对干净的结构。
- **旧迁移永远保留。** 删掉 `migrate_1_to_2` 会让所有 v1 存档永远卡在旧版本。保留
  它们成本很低，且必须始终是一份忠实的记录。
- **测试迁移链**：保留每个已发布版本的真实存档语料，每次改动后断言它们仍能加载
  （这就是你的回归防护网）。

## 备份与回滚

- 覆盖之前，先把当前存档复制为 `*.bak`。主存档加载失败时，自动尝试备份。
- 自动存档用小环形轮换（autosave_0..2），避免一次坏的自动存档毁掉唯一的近期状态。
- 可考虑给数据加校验和/哈希，以检测截断或损坏（这与防篡改是两回事，决心足够的本地
  玩家总能破解防篡改）。

## 格式取舍

| 格式 | 优点 | 缺点 | 适用场景 |
|---|---|---|---|
| JSON / 文本 | 可读、易调试、可 diff、迁移容易 | 更大、更慢、轻易可被编辑 | 默认选择；适合大多数游戏 |
| 二进制（引擎） | 紧凑、快速、有一定不透明性 | 难调试/难迁移、对版本变更脆弱 | 状态量大、性能敏感 |
| 键值存储 | 简单、按键粒度健壮 | 无结构、需手工维护 schema | 设置项、少量标志位 |
| 云端 KV（如 DataStore） | 跨设备 | 配额、延迟、冲突 | 在线/跨设备存档 |

无论磁盘上用什么格式，都以**内存中的字典/结构体**作为规范形态，在边界处做（反）
序列化。迁移随后作用于这个中立形态，而不是格式专属的字节。

## 加载时校验清单

- 必需的键都在；类型正确（区分 string、number、bool）。
- 数值在合理范围内（无 NaN/Infinity；hp ≥ 0；索引不越界）。
- 枚举/id 值在当前内容中仍然存在（补丁里移除的物品 id 必须被处理：丢弃或替换，
  不能崩溃）。
- 引用可解析（任务 id 指向一个已知的任务）。
- 任何失败都要：记日志、回退到备份；全都失败时，就*醒目地*向玩家报错，而不是静默
  加载一个损坏的状态。

## 存档存放位置与云同步

把存档写到引擎提供的每用户数据目录，绝不放在可执行文件旁边（那里通常只读，而且会
被更新替换）：

- **Godot 4.7** `user://`：Windows 下是 `%APPDATA%\Godot\app_userdata\[project]`，
  macOS 下是 `~/Library/Application Support/Godot/app_userdata/[project]`，Linux 下是
  `~/.local/share/godot/app_userdata/[project]`。发布前打开
  `application/config/use_custom_user_dir`（可选配合 `custom_user_dir_name`）来去掉
  路径里的 `Godot/app_userdata` 这一段，因为之后再改会把每个玩家的存档都挪走。Web
  导出把 `user://` 存在浏览器的 IndexedDB 里。
- **Unity 6.3** `Application.persistentDataPath`：Windows 下是
  `%userprofile%\AppData\LocalLow\<company>\<product>`，Linux 下是
  `~/.config/unity3d/<company>/<product>`，macOS 玩家端是
  `~/Library/Application Support/unity.<company>.<product>`；Web 用 IndexedDB；tvOS
  返回空字符串（没有持久化目录）。改公司名或产品名，目录也会跟着变。
- **Unreal 5.8** 用 `USaveGame` 子类配合 `UGameplayStatics::SaveGameToSlot` /
  `AsyncSaveGameToSlot`；目录由平台层选定，在主机上则走平台存档 API。

**Steam Cloud。** Auto-Cloud 会同步你在 Steamworks 中配置的根路径之下的文件（例如
`WinAppDataRoaming`、`WinAppDataLocalLow`、`MacAppSupport`、`LinuxXdgDataHome`）；
需要更多控制时，可改用 ISteamRemoteStorage API。文件在游戏退出后上传、在下次启动前
下载，所以游戏运行期间写入的存档那时还没进云端。即使只发单平台，也要为每个根路径
选择 Cross-Platform OS 设置（各系统下目录不同时用 root overrides）：锁死在单一 OS
上的根路径，以后新增其他平台时不会向它们同步。先在应用管理后台设置每用户的字节与
文件数配额；没有配额，Steam Cloud 不会生效。不要把 `.tmp` 文件放进同步模式。选择
启用 Dynamic Cloud Sync（Steam Deck 挂起）的游戏，会在会话中途收到变更文件，必须
重新加载它们。发布前测试 Auto-Cloud：请用户打开 Steam 控制台（`steam://open/console`），
运行 `testappcloudpaths <AppId>` 和 `set_spew_level 4 4`，启动游戏、存档、退出，然后
把上传相关的日志行报告出来；Steam 还会把日志写到安装目录下的 `logs/cloud_log.txt`。

**主机和移动端**有平台存档 API、存储上限和认证规则；在这些平台上遵循平台文档，
而不是直接用原始文件路径。

## 存什么、重算什么

- **存储**权威、不可推导的状态：选择、解锁标志、RNG 种子、物品栏、位置。
- **重算**派生数据，在加载时进行（由基础值 + 修正算出完整属性表，由种子生成程序化
  地图）。存派生数据会在补丁改动公式时引发不同步，还会让文件膨胀。
