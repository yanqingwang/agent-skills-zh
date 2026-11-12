---
name: save-systems
description: >
  引擎无关的保存与加载，附 Godot 和 Python 代码：该序列化什么、存档槽与自动保存、原子写入与带版本的迁移。
  适用于实现存读档或"继续游戏"按钮，或存档在崩溃后损坏、打补丁后失效的情形。
  不适用于 Roblox DataStores（`roblox-datastores`）、数据资产（`godot-resources`、`unity-scriptableobjects`）或各品类的存档界面（`rpg`、`visual-novel`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/save-systems/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 存档系统

存档文件是游戏状态的一份序列化快照，必须能挺过崩溃、重启和版本补丁。难点在于：选好要保存的内容、让保存中途的崩溃无法毁掉存档、并在更新后读出旧存档。本 Skill 负责文件本身：格式、写入、版本管理、存档槽和存放位置。各品类 Skill 决定里面放什么。

## 适用场景

- 持久化进度：属性、物品 id、世界标志位、设置、位置、随机种子。
- 存档槽、快速存档、自动保存、崩溃安全的写入、备份。
- 代码或内容改动后旧存档失效。

**不适用本 Skill：** Roblox 云端持久化（`roblox-datastores`）、数据模型本身（`godot-resources`、`unity-scriptableobjects`）、按键重绑定的数据结构（`input-systems`）、视觉小说中的存档界面与回滚（`visual-novel`）。

## 核心工作流

1. **先摸清现状。** 用 grep 查找现有的存档代码（`FileAccess`、`ConfigFile`、`ResourceSaver`、`PlayerPrefs`、`SaveGameToSlot`、`persistentDataPath`）以及任何已发布的存档。若玩家手里已有存档，下面每一处改动都需要迁移。
2. **保存数据，而非对象。** 保存 id、数值、标志位和 RNG 种子；加载时据此重建节点与对象。活跃引用和节点路径经不起重构。
3. **从首发版本起，在每份存档里写入整数 `version`。**
4. **先用 JSON**（可读、可 diff、易迁移）；只有实测确有体积或速度需求时才改用二进制。
5. **原子写入**：写临时文件，把上一份存档留作 `.bak`，再重命名到位。
6. **防御式加载**：解析、读取版本、拒绝更新的存档、逐步迁移旧存档、校验，然后再应用。失败时回退到备份并告知玩家。
7. **在安全边界自动保存**（检查点、关卡切换），做节流，并写入独立的存档槽。
8. **运行下面的检查**，然后请用户做退出并重进的测试。

## 模式

### 1. 用纯数据表示状态


```gdscript
func capture_state() -> Dictionary:
    return {
        "version": SAVE_VERSION,
        "player": { "hp": player.hp, "pos": [player.position.x, player.position.y] },
        "inventory": player.inventory.to_array(),  # ids + counts, not Item nodes
        "flags": world.flags,
        "seed": world.seed,                        # regenerate procedural content
    }

func apply_state(data: Dictionary) -> void:        # rebuild from data; no live references
    player.hp = int(data["player"]["hp"])
    player.position = Vector2(data["player"]["pos"][0], data["player"]["pos"][1])
    player.inventory.from_array(data["inventory"])
    world.flags = data["flags"]
```


### 2. 原子、崩溃安全的写入（临时文件 + 重命名）


```gdscript
# Godot 4.7. Write a temp file, keep the previous save as .bak, then rename.
func save_atomic(path: String, data: Dictionary) -> Error:
    var tmp := path + ".tmp"
    var f := FileAccess.open(tmp, FileAccess.WRITE)
    if f == null:
        return FileAccess.get_open_error()       # disk full, read-only, no permission...
    if not f.store_string(JSON.stringify(data)):
        return ERR_FILE_CANT_WRITE
    f.close()                                    # flushes Godot's buffer to the OS
    if FileAccess.file_exists(path):
        DirAccess.rename_absolute(path, path + ".bak")   # keep the last good save
    return DirAccess.rename_absolute(tmp, path)

func load_save(path: String) -> Dictionary:      # empty = nothing loadable
    for p in [path, path + ".bak"]:              # .bak covers a crash between renames
        if FileAccess.file_exists(p):
            var data = JSON.parse_string(FileAccess.get_file_as_string(p))
            if data is Dictionary and data.has("version"):
                data["version"] = int(data["version"])   # JSON numbers load as float
                return data
    return {}
# WRONG: opening `path` directly and writing in place — a crash mid-write leaves a
# truncated, unloadable save and destroys the player's progress.
```


发生崩溃时，留下的可能是旧存档、新存档，或（在两次重命名之间）只剩 `.bak`，而加载器接下来会尝试它。在 POSIX 的同一卷内，`rename()` 会原子地替换目标，但 Godot 在 Windows 上的 `rename_absolute` 是先删除目标再移动，因此 Windows 同样要依赖 `.bak`。`flush()` 和 `close()` 都不会调用 `fsync`，所以保存刚完成就断电仍可能丢失最新的文件。检查每个返回的 `Error`，保存失败时告知玩家。

### 3. 带版本与迁移的加载


```python
SAVE_VERSION = 3

def load_save(raw_bytes):
    data = parse(raw_bytes)                  # JSON/binary -> dict
    v = int(data.get("version", 1))          # no field = the first shipped schema
    if v > SAVE_VERSION:
        raise NewerSaveError(v)              # save is from a newer build; refuse
    while v < SAVE_VERSION:                   # apply migrations in order, v -> v+1
        data = MIGRATIONS[v](data)
        v += 1
        data["version"] = v
    validate(data)                            # check required keys / ranges
    return data

# Each migration is a pure function from one version's shape to the next.
def migrate_1_to_2(d):
    d["flags"] = {k: True for k in d.pop("completed_quests", [])}  # list -> set-map
    return d
def migrate_2_to_3(d):
    d.setdefault("difficulty", "normal")      # new field: old saves get the default
    return d
MIGRATIONS = {1: migrate_1_to_2, 2: migrate_2_to_3}
```


每一条迁移都要永久保留；删掉其中一条，就会让该版本的全部存档无处可去。

### 4. 存档槽与节流的自动保存


```gdscript
const SLOT_PATH := "user://save_%d.json"      # manual slots 0..N
const AUTOSAVE_PATH := "user://autosave.json"  # separate file: never clobbers a slot
var _autosave_cooldown := 0.0

func autosave_if_due(dt: float) -> void:
    _autosave_cooldown -= dt
    if _autosave_cooldown <= 0.0:
        save_atomic(AUTOSAVE_PATH, capture_state())
        _autosave_cooldown = 60.0             # at most once a minute; also save on checkpoints
```


### 5. 往返与损坏测试（无头模式）


```gdscript
# tools/save_roundtrip_test.gd: godot --headless --path . --script res://tools/save_roundtrip_test.gd
extends SceneTree

const PATH := "user://test_save.json"

func _initialize() -> void:
    var saver = load("res://save.gd").new()      # the game's save_atomic / load_save
    var ok := true
    var first := {"version": 3, "player": {"hp": 7, "pos": [1.5, -2.0]}, "flags": {"met_guard": true}}
    var second := first.duplicate(true)
    second["player"]["hp"] = 4
    ok = ok and saver.save_atomic(PATH, first) == OK
    ok = ok and saver.save_atomic(PATH, second) == OK  # first is now the .bak
    var loaded: Dictionary = saver.load_save(PATH)
    # Compare fields, not whole Dictionaries: JSON turned hp 4 into 4.0, and 4 != 4.0 there.
    ok = ok and loaded.get("version") is int and loaded["player"]["hp"] == 4
    ok = ok and loaded["player"]["pos"] == [1.5, -2.0] and loaded["flags"] == second["flags"]
    var f := FileAccess.open(PATH, FileAccess.WRITE)   # simulate a truncated primary
    f.store_string("{\"version\": 3, \"pla")
    f.close()
    ok = ok and saver.load_save(PATH)["player"]["hp"] == 7          # fell back to .bak
    for p in [PATH, PATH + ".bak", PATH + ".tmp"]:
        DirAccess.remove_absolute(ProjectSettings.globalize_path(p))
    print("SAVE_ROUNDTRIP ", "ok" if ok else "FAIL")
    quit(0 if ok else 1)
```


把 `res://save.gd` 指向游戏自己的存档脚本。被截断的文件会让 Godot 打印 `Parse JSON failed`；这一行在这里是预期出现的，只有 `.bak` 能成功加载，测试才算通过。

## 检查

1. 运行往返测试：必须打印 `SAVE_ROUNDTRIP ok`。
2. 在 fixtures 目录里为每个已发布版本保留一份真实存档，每次改动数据结构后，都在测试中让它们逐一走一遍迁移链。
3. 加载一份标记为更新版本的存档，确认它被拒绝并附带提示信息，而不是加载到一半。
4. 在存档路径里 grep 检查引擎对象（`Node`、`Resource`、`var_to_str`、允许对象的 `store_var`）；结果应当为空。
5. 请用户在关卡中途存档、完全退出游戏、重新启动、加载，并报告任何不一致之处（位置、物品、标志位、任务状态）。若用了 Steam Cloud，请他们在第二台机器上重复一遍，并报告存档是否同步到位。

## 常见陷阱

- **没有版本字段。** 第一个补丁就会把所有现存存档变成靠猜的对象。
- **序列化引擎对象或节点路径** 会把存档绑死在场景结构上；一次重命名就废掉所有旧存档。
- **就地写入** 会在崩溃或断电时损坏存档。要写临时文件，并保留 `.bak`。
- **Godot 的 JSON 会把每个数字都变成浮点数**：`version` 为 3 会读成 `3.0`，于是 `MIGRATIONS.has(data["version"])` 为 false，整个 Dictionary 与原值做 `==` 会失败，而超过 2^53 的整数（64 位 id、大随机种子）会丢位。用 `int()` 转换，把大 id 存成字符串，或者用 `JSON.from_native()` / `JSON.to_native()` 包住状态。
- **对损坏文件调用 `JSON.parse_string`** 会记录一条引擎错误并返回 `null`。若需要把出错行和信息给玩家或写进日志，就改用 `JSON` 实例和 `parse()`。
- **从存档文件加载对象。** Godot 中允许对象的 `str_to_var` 或 `get_var`、装有对象的 `ConfigFile`，或对玩家可替换的 `.tres` 使用 `ResourceLoader`，都会创建一个脚本在加载过程中就运行的对象。存档会被放到网上分享；保持为纯数据。
- **浮点数与区域设置。** 手工拼的文本格式在某些区域设置下会写出逗号小数。改用引擎自带的 JSON，或其他不受区域设置影响的序列化器。
- **自动保存覆盖手动存档**，或在战斗中触发、存下不一致的状态。改用专用存档槽和安全边界。
- **把存档放在可执行文件旁边**：那里往往只读，还会被更新覆盖。改用引擎提供的每用户目录（见参考资料）。
- **线上轻信客户端存档。** 本地存档由玩家掌控；绝不要把它当作多人游戏或经济状态的权威来源。

## 参考资料

- `references/versioning-and-migration.md`：在演进数据结构（新增、重命名与删除字段的迁移）、维护存档样本集、轮转备份、在 JSON 与二进制之间取舍、编写加载时校验、确定各引擎的存档位置，或配置 Steam Cloud 时阅读。

## 相关 Skill

- `roblox-datastores`：云端持久化、请求限额、会话锁定。
- `godot-resources`、`unity-scriptableobjects`：被序列化的数据模型。
- `procedural-gen`：保存种子和生成器版本，而非整个世界。
- `rpg`、`survival-crafting`、`visual-novel`：各品类往存档里放什么。
- `steam-publish`：配置 Steam Cloud 的 Steamworks 应用管理页面。

## 版本说明

最后验证：2026-11-11。

- Godot 4.7：`FileAccess.store_string` 返回 `bool`；存在 `JSON.from_native`/`to_native`；Windows 的 `DirAccess.rename` 会在移动前删除目标（`drivers/windows/dir_access_windows.cpp`）。上面的往返测试在 4.7.2 无头模式下运行。
- Steam Cloud：文件在游戏退出后、下次启动前同步；必须先设好字节配额和文件配额才能生效；对 Auto-Cloud 根目录，推荐的操作系统设置是 Cross-Platform；Dynamic Cloud Sync 可在会话中途改动文件（https://partner.steamgames.com/doc/features/cloud）。
