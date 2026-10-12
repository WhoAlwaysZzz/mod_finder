# 《怪物猎人：荒野》太刀逐招式自定义音效：调研报告

调研日期：2026-10-12。数据来源：Nexus Mods 公开 GraphQL API（返回 mod 描述、版本和压缩包文件列表）、GitHub 源码仓库，以及踩蘑菇社区的教程。
`nexusmods.com` 网页有 Cloudflare 拦截，云端浏览器打不开，所以本文引用的 Nexus 内容都来自 API 原文，链接仍指向网页，方便你在本地打开。

标注说明：
- **【已验证】** 在原始页面或源码里亲眼确认过，或者我在云端实际跑过。
- **【推断】** 根据已验证事实推出来的结论，还没有在你的游戏里实测。
- **【未知】** 目前没有证据。

---

## 0. 结论速览

1. **【已验证】目前不存在“打开一个工具，从招式列表里选‘大居合’，再填入自己的 wav”这样的现成工具或 mod。** 我在 Nexus 上按 sound、sfx、audio、voice、longsword、wav、mp3、custom sound、sound replacer、wem 等关键词检索了荒野分区的全部结果，找到约 250 个相关 mod，又查了 GitHub 和中文社区，都没有发现这类工具。
2. **【已验证】现有的太刀音效 mod 全部是作者做好的成品。** 它们都只替换同一个文件：`natives/STM/Sound/Wwise/Wp03_Cmn_m.sbnk.1.X64`（太刀主音效库，Wwise SoundBank）。这些 mod 不能自定义音频，**彼此之间也互相冲突**，同一时间只能启用一个。
3. **离“自己管理素材、逐招式替换”最近、且我已验证可行的路线**是同一作者 Eigeen 的两件工具组合：
   - **Sound Debugger**（REFramework 脚本）：在游戏里实时显示每次发声对应的 `Trigger ID → Event ID → WEM ID / 所在 sbnk / 序号`。用它“打一招，看一眼”，就能查到这一招对应哪个 WEM。
   - **MHWS Sound Tool**（命令行加拖放）：把 `Wp03_Cmn_m.sbnk.1.X64` 解包成文件夹，然后把你的 `wav`/`mp3`/`ogg`/`flac` 按 `<WEM ID>.wav` 命名放进 `replace/` 文件夹，再拖回去，就会打包出新的音效库。工具会调用 Wwise Console 自动转码。

   这套流程**不需要编程，也不需要会用 Wwise 编辑器**，但需要安装 Wwise（只用到它的命令行转码器）。另外，“哪个 ID 对应哪一招”要你自己在游戏里实测记下来。我在本仓库里放了一张映射表模板，以及一个按表自动放置文件的脚本（见第 4 节）。
4. **粒度限制【已验证，来自多位 mod 作者的说明】：** 有些招式共用同一个音效，换一个就会全部一起变。打击音效还存在“改一个、其余全部静音”的问题。所以**并不是每个招式都能单独换**，见第 3 节。

---

## 1. 可用方案对比

### 1.1 工具类（可以用来做“自己的”音效）

| 工具 | 用途 | 最新版本（截至 2026-10-12） | 前置依赖 | 链接 |
|---|---|---|---|---|
| **Sound Debugger** (Eigeen) | 游戏内实时记录音效事件，显示 Trigger/Event/WEM ID、所在 bank 和序号，可以重播或停止 | **v1.0.2**（Nexus 2026-02-15 更新，GitHub 提交信息为 “update 1.0.2, TU4 database”） | REFramework、CatLib | [Nexus #3246](https://www.nexusmods.com/monsterhunterwilds/mods/3246) · [GitHub](https://github.com/paean-of-guidance/sound-debugger) |
| **MHWS Sound Tool** (Eigeen) | BNK/PCK 解包成文件夹、回包、批量转码，并通过 `replace/` 目录按 ID 或序号替换 | **v0.2.2**（Release 日期 2025-04-03）。主分支在 2025-07 合并了 PCK 修复，但还没有发新的 Release | 转码需要 Wwise Console；mp3/ogg/flac/aac 另需 ffmpeg | [GitHub Releases](https://github.com/eigeen/mhws-sound-tool/releases) · [中文文档](https://github.com/eigeen/mhws-sound-tool/blob/main/docs/README_zh-CN.md) · [踩蘑菇发布帖](https://www.caimogu.cc/post/1952570.html) |
| **REE Pak GUI** (Eigeen，即原 ree-pak-rs) | 从游戏 `.pak` 中解出原版 `Wp03_Cmn_m.sbnk.1.X64` | **v0.6.0**（ree-pak-rs 仓库说明：v0.3.0 以后改到 ree-pak-gui 发布） | 文件名表（.list） | [ree-pak-gui Releases](https://github.com/eigeen/ree-pak-gui/releases) · [ree-pak-rs](https://github.com/eigeen/ree-pak-rs) |
| RingingBloom (Silvris) | 图形界面 BNK/PCK 编辑器（替代方案） | v2.1 | .NET Core 3.1；模式选 RE8 或 MHRise | [GitHub](https://github.com/Silvris/RingingBloom) |
| wwiseutil (hpxro7) | 老牌 BNK 替换工具（替代方案） | 1.1 | — | [GitHub](https://github.com/hpxro7/wwiseutil) |
| vgmstream / foobar2000 + foo_input_vgmstream | 试听 `.wem` 或整个 bank 的内容 | r2117 | — | [GitHub](https://github.com/vgmstream/vgmstream) |
| Wwise（Audiokinetic Launcher） | WAV → WEM 转码（MHWS Sound Tool 会自动调用 `WwiseConsole`） | 教程建议用 2023 版，见下文 | 免费注册 Audiokinetic 账号 | [audiokinetic.com](https://www.audiokinetic.com/download/) |
| REFramework | 开启 Loose File Loader，让游戏读取 `natives/` 下的散件 | Nexus 版 vNightly01240（2026-02-25），GitHub nightly v1.102 | — | [Nexus #93](https://www.nexusmods.com/monsterhunterwilds/mods/93) · [GitHub nightly](https://github.com/praydog/REFramework-nightly/releases) |
| CatLib | Sound Debugger 的前置库 | v1.14.0（2026-08-21） | REFramework | [Nexus #65](https://www.nexusmods.com/monsterhunterwilds/mods/65) |
| Fluffy Mod Manager | 可选，用来一键启用或禁用 mod | — | — | [fluffyquack.com](https://www.fluffyquack.com/) |

另外两件“看起来像、其实不是”的工具：
- [StateMusic (#4628)](https://www.nexusmods.com/monsterhunterwilds/mods/4628)：可以直接把 mp3/wav/ogg/flac 放进文件夹、在菜单里选，但**只管 BGM**（按战斗状态、怪物、区域切换），不管招式音效。【已验证】
- [auto play rain love when just a life (#5078)](https://www.nexusmods.com/monsterhunterwilds/mods/5078)：用 REFramework 插件加外部播放器，在剩最后一乘时循环播放你的 WAV。这说明“REF 脚本监听事件，再播放外部音频”在技术上走得通。但目前**没有人把它做成“按太刀招式触发”的工具**。【已验证存在；用于太刀属于推断】

### 1.2 现成的太刀音效 mod（成品，不能自定义）

下表全部来自 Nexus API 的描述和压缩包文件列表。**每一个 mod 的压缩包里都只有 `natives/STM/Sound/Wwise/Wp03_Cmn_m.sbnk.1.X64` 这一个音效文件**【已验证：#929、#642、#1240、#913、#1513、#1703、#1958、#2558、#3044 的文件列表】，所以它们两两冲突。

| Mod | 版本 / 最后更新 | 替换内容（作者原话摘录） |
|---|---|---|
| [Sekiro Long Sword Sounds #929](https://www.nexusmods.com/monsterhunterwilds/mods/929) | 2.0.0 / 2025-03-24 | special sheathe click、foresight slash & spirit whirl slash、iai spirit slash、各种反击成功、focus strike 及 3 个随机后续、spirit combo、spirit helmbreaker、spirit release slash |
| [Cooler Longsword Sounds #642](https://www.nexusmods.com/monsterhunterwilds/mods/642) | 1.2 / 2025-03-22 | Sheathe、Wound Attacks、Spirit Release Slash、Spirit Thrust、Helm Breaker、Spirit Charge Progression、Spirit Slash、Iai Spirit Slash |
| [Longsword SFX Improvement #1240](https://www.nexusmods.com/monsterhunterwilds/mods/1240) | 1.21 / 2025-03-27 | GP（看破、居合）提示音混入冰原版；解放斩第三刀加入 Rise 音效 |
| [Longsword Foresight Slash And Iai Sheathe Success Ding SFX #913](https://www.nexusmods.com/monsterhunterwilds/mods/913) | 1.0 / 2025-03-18 | 看破、居合成功的“叮” |
| [MHW Tin sound for iai #1189](https://www.nexusmods.com/monsterhunterwilds/mods/1189) | 1.0 / 2025-03-24 | 居合、见切成功音（3 档音量） |
| [Long Sword with Sekiro Parry Sound #2558](https://www.nexusmods.com/monsterhunterwilds/mods/2558) | 1.0 / 2025-05-26 | 居合气刃斩、看破斩 |
| [Longsword Iai SFX - M1 Garand #3044](https://www.nexusmods.com/monsterhunterwilds/mods/3044) | 1.2 / 2025-08-12 | 特殊纳刀、居合气刃斩（另有多个可选版本） |
| [Longsword Samurai Audio Replacement #1513](https://www.nexusmods.com/monsterhunterwilds/mods/1513) | 1.0 / 2025-04-03 | 语音类，作者列出了**逐招式对照表**（见第 3 节） |
| [Longsword Jalter Audio Replacement #1703](https://www.nexusmods.com/monsterhunterwilds/mods/1703) | 1.0 / 2025-04-09 | 语音类 |
| 其它：#823 NOICE、#897 WOOOW、#1898 Vergil、#3496 BBTAG、#3910 Guilty Gear（反击音）；#781、#1033、#1413、#1231、#1958、#2565、#597 等（角色语音） | — | — |

**“当前是否仍可用”：**【未知 / 推断】这些 mod 大多是 2025 年 3～5 月发布的，之后没有更新。游戏后来又出了 TU1～TU4 以及 2026 年的小补丁。#1240 在踩蘑菇的发布帖标题写着“荒野最终更新可用”，作者原话是“只要 REF 可用并开启 LoosefileLoader，更新后仍可使用”，但没有给出具体版本号。**【推断】** 如果卡普空在某次更新里改过 `Wp03_Cmn_m` 的内容（增删 WEM 或改了 HIRC 结构），用旧 mod 的文件整个覆盖就可能导致新增的音效丢失或静音。所以**推荐的做法是从你当前版本的游戏里解出原版文件再改**，不要拿老 mod 的文件当底稿。

---

## 2. 能否“逐招式”定位？两个层次分开说

| 层次 | 结论 |
|---|---|
| A. 能不能替换太刀的音频资源 | **【已验证】能。** 太刀主音效库是 `Wp03_Cmn_m.sbnk.1.X64`，里面是几十个 WEM，可以逐个替换。上面所有 mod 都是这么做的。我在云端用 MHWS Sound Tool v0.2.2 对它仓库自带的大剑库 `Wp00_Cmn_m.sbnk.1.X64` 实测过：解包出 77 个 WEM，替换其中一个后回包，再解包核对，被替换项的 MD5 等于新文件，其余项 MD5 不变。 |
| B. 能不能在工具里“清楚地选择具体招式” | **【已验证】不能。** 没有任何工具内置“招式名 → WEM”的清单。Sound Debugger 只显示数字 ID（它的数据库 `event_sound_indexmap.json` 是 `bank → Event ID → [{wem_id, index, m_bank}]`，没有招式名）。招式和 ID 的对应关系只能**你自己在游戏里实测**，或者参考别的 mod 作者的笔记。 |

### 怎样确认某一招对应哪个 WEM（推荐流程，【已验证工具功能；在太刀上的具体结果未知】）

1. 安装 REFramework、CatLib、Sound Debugger。按 Insert 打开菜单，进入 Script Generated UI → Sound Debugger。
2. 在它的 Filter 里新建一个 Profile，打开 Whitelist Mode，加入 `Wp03`。过滤是对 bank 名做 Lua `string.find` 匹配（`database.lua:179`），所以这样能同时看到 `Wp03_Cmn_m` 和其它可能存在的 `Wp03_*` 库，方便确认某个声音到底在不在主音效库里。
3. 去训练场，一招一招地打。每发出一次声音，日志里就会出现 `Trigger ID`、`Event ID`，以及 `- <wem_id>  Wp03_Cmn_m.sbnk[<index>]`。可以点 Replay 重播确认。
4. 把 “招式 → wem_id” 记到本目录的 [`longsword_sfx_map_template.csv`](longsword_sfx_map_template.csv) 里。
5. 日志里有三类特殊情况要注意（Sound Debugger README 原文）：
   - **Random sequence**：一个事件会从几个 WEM 里随机选一个播放。想让这一招每次都是你的声音，就要把这几个 WEM 全换掉。
   - **Conditional playback**：按条件选择（例如武器材质、环境）。工具“目前取不到条件”，所以会列出所有可能。
   - **Multiple results**：同一个触发可能对应多个 bank，常见于语音。
6. 注意 Sound Debugger README 里的警告：“Playback some effect audio may crash your game”，即重播某些效果音可能导致游戏崩溃。
7. 没有 Sound Debugger 时的土办法（Suedo 的教程）：用 foobar2000 加 vgmstream 逐条试听 bank 里的音频，再把可疑的几条换成“提示音 1、2、3”，进游戏逐个出招，听听哪一招响的是哪个提示音。

---

## 3. 太刀招式能分到多细（证据汇总）

**中英日招式名对照【已验证，出自 #1513 作者列出的对照表】：**

| 中文 | 日文 | 英文 |
|---|---|---|
| 空中拔刀气刃斩 | 空中抜刀気刃斬り | Aerial Draw Spirit Blade |
| 集中突刺【无尽】 | 集中突き【無尽】 | Focus Strike: Unbound Thrust |
| 气刃突刺 | 気刃突き | Spirit Thrust |
| 气刃兜割（俗称登龙） | 兜割り | Spirit Helmbreaker |
| 练气解放无双斩 | 練気解放無双切り | Spirit Release Slash |
| 气刃蓄力 | 気刃溜め | Spirit Charge |
| 特殊纳刀 | 特殊納刀 | Special Sheathe |
| 居合拔刀气刃斩（俗称大居合） | 居合抜刀気刃斬り | Iai Spirit Slash |
| 见切 / 大居合格挡成功 | カウンターに成功 | successful counter (Foresight Slash or Iai Spirit Slash) |

关于你列出的名称：
- “大居合成功 / 失败”：游戏里的正式名称是**居合拔刀气刃斩**（Iai Spirit Slash）。成功指反击判定成立，此时有单独的“反击成功”提示音。从 #913、#1189、#2558 都能单独替换“居合 / 见切成功音”来看，**成功提示音是可以单独定位的**【已验证】。“失败”（没有判定成功、只出了斩击）是否有自己专属的音效，**【未知】**，需要用 Sound Debugger 实测。
- “居合 / 灯笼开始”：游戏里对应的是**特殊纳刀**（Special Sheathe）。#929 和 #3044 都能单独替换 “special sheathe click” 或“特殊纳刀”音【已验证】。“灯笼”应该是玩家俗称，我没有找到出处。
- “袈裟斩”：我没有在荒野的资料里找到与之对应的正式招式名。【未知】请以游戏内招式表为准，再用 Sound Debugger 实测。
- “普通攻击 / 命中 / 未命中”：Suedo（#642 作者）说：“changing a sound in the hit sfx files mutes all other hits but the one that was changed. So, no custom hit sounds.”【已验证为作者原话】。也就是说，**打击音（命中音）实际上没法自定义**。【推断】打击音所在的 bank 并不是 `Wp03_Cmn_m`，可能在 `Wp03_Cmn` 或公共 hit 库中。大剑在 Eigeen 的测试文件里就分成 `Wp00_Cmn`、`Wp00_Cmn_Effect`、`Wp00_Cmn_m` 三个 bank。另外，#349 这类 mod 改的是 `hit_hm_cmn.sbnk.1.x64`，属于全武器共用的库。
- 挥刀风声（未命中）和收刀：#642 写了替换 “Sheathe”，所以收刀音可以定位【已验证】。普通挥刀能否逐招式区分，【未知】。

**已知的共用限制【已验证，作者原话】：**
- #929 Sekiro 作者：“the spirit roundslash, spirit iai slash and spirit whirl slash all share one sound effect so replacing one affects all three. Similarly, the focus strike pre-follow up (when player pulls down sword) and the thrust share the same sound effect.” 也就是说**气刃大回旋斩、居合拔刀气刃斩、Spirit Whirl Slash 三招共用一个音效**，集中攻击的准备动作和突刺也共用一个。
- #1958 作者：“荒野的音效共用很严重”。
- 踩蘑菇 #1240 作者：太刀**语音基本和武器音效合成在一起**，所以音效 mod 和语音 mod 无法共存。

---

## 4. 操作流程（Windows，推荐路线）

> 建议你先在训练场里用一两个音效走通全流程，再批量做。

### 4.1 准备（一次性）
1. 安装 **REFramework**：把 `dinput8.dll` 放进游戏根目录（例如 `...\steamapps\common\MonsterHunterWilds`）。进游戏后按 Insert，勾选 **Enable Loose File Loader**。
2. 安装 **CatLib** 和 **Sound Debugger**：把压缩包里的 `reframework` 文件夹**合并**到游戏根目录。
3. 安装 **Wwise**：通过 Audiokinetic Launcher 安装，需要免费注册。踩蘑菇的 Silver 教程原话是“用 23 版本，24 版本默认导出文件格式错误”，所以选 **2023.x**。MHWS Sound Tool 会自动寻找 `WwiseConsole.exe`；找不到时会让你输入路径，并把路径保存到同目录的 `config.toml`。
4. （可选）安装 **ffmpeg**：这样就能直接用 mp3/ogg/flac/aac 素材。
5. 下载 **MHWS Sound Tool** 和 **REE Pak GUI**。

### 4.2 提取原版音效库
6. 用 REE Pak GUI 打开游戏目录里的 `re_chunk_000.pak` 及其 `sub`、`patch` 分包，文件名表选 Monster Hunter Wilds（STM）。搜索 `Wp03_Cmn_m.sbnk.1.X64` 并解出。
   【推断】游戏更新后，最新版本的文件可能放在 patch 分包里，要确认解出来的是最新的那份。
7. **备份**这个原版文件，例如复制一份为 `Wp03_Cmn_m.sbnk.1.X64.orig`。

### 4.3 找 ID、填表
8. 按第 2 节，用 Sound Debugger 查出每一招对应的 `wem_id`，填进 `longsword_sfx_map_template.csv`。`audio_file` 一列填你的素材路径，可以写相对路径，以表格所在目录为基准。

### 4.4 生成新音效库
9. 把 `Wp03_Cmn_m.sbnk.1.X64` 拖到 `mhws-sound-tool.exe` 上，会生成 `Wp03_Cmn_m.sbnk.1.X64.project\` 文件夹，里面是 `[序号]WEMID.wem`、`project.json` 和 `bank.json`。
10. 放入替换文件，二选一：
    - 用本目录的脚本（需要 Python 3）：
      ```
      python build_replace_dir.py longsword_sfx_map_template.csv "...\Wp03_Cmn_m.sbnk.1.X64.project" --dry-run
      python build_replace_dir.py longsword_sfx_map_template.csv "...\Wp03_Cmn_m.sbnk.1.X64.project"
      ```
      脚本会检查 ID 是否真的存在于这个 bank、文件是否存在、格式是否支持、ID 有没有重复，然后复制为 `replace\<wem_id>.<扩展名>`。
    - 或者手动操作：在 `.project` 里新建 `replace` 文件夹，把素材改名为 `<WEM ID>.wav`（不加方括号），或者 `[序号].wav`（加方括号）。
11. 把**整个 `.project` 文件夹**拖到 `mhws-sound-tool.exe` 上，会生成 `Wp03_Cmn_m.sbnk.1.X64.new`。把它改名去掉 `.new`。

### 4.5 安装、预览和恢复
12. 放到 `游戏目录\natives\STM\Sound\Wwise\Wp03_Cmn_m.sbnk.1.X64`。也可以打包成 Fluffy 用的 zip：`<mod名>\modinfo.ini` 加上 `<mod名>\natives\STM\Sound\Wwise\...`。
13. 进训练场试听。想微调就修改素材后重复第 10～12 步。
14. **恢复原音效**：删除 `natives\STM\Sound\Wwise\Wp03_Cmn_m.sbnk.1.X64` 即可，因为 Loose File Loader 只是用散件覆盖，原版文件还在 pak 里。用 Fluffy 安装的话，取消勾选即可。

### 4.6 音频格式和限制

| 项目 | 情况 |
|---|---|
| 输入格式 | wav 直接交给 Wwise Console 转码；mp3/ogg/flac/aac 先经 ffmpeg 转成 wav。也可以直接放 `.wem`。【已验证：源码 `src/project.rs`】 |
| 原版参数 | 我解析了 MHWS Sound Tool 自带的大剑库 `Wp00_Cmn_m`：77 个 WEM 全部是 **Wwise Vorbis（格式码 0xFFFF）、48 kHz**，其中 72 个单声道、5 个立体声，时长 0.33～2.63 s，中位数 0.76 s。【已验证，大剑】太刀库应该类似。【推断】 |
| 建议 | 48 kHz、单声道，时长尽量接近原音效。踩蘑菇 Silver 教程建议在 Wwise 里把 Default Conversion Settings 的格式从 PCM 改成 **Vorbis**。MHWS Sound Tool 的自动转码具体用哪种设置，【未知】：README 和源码里没写明，需要在 Windows 上实测。如果游戏里没声音，就先改用 Wwise 手动导出 Vorbis 的 .wem，再放进 replace。 |
| 时长 | 没有找到官方硬性上限。过长的音效可能被截断或和下一招重叠。【推断】 |
| 大小 | 没有找到明确上限。#1513、#1703 的成品 bank 有 3.3～3.7 MB（原版大约 0.8 MB），说明加入较长的语音也能正常工作。【已验证文件大小】 |
| 音量 | 没有专门的设置。用 Audacity 预先调整（#642 作者的建议）。 |

### 4.7 已知小坑
- 【已验证，v0.2.2 源码】`replace/` 里**只放 `.wem`** 时，工具仍然会调用 Wwise Console，没装 Wwise 就会报 `WwiseConsole path is not set`。绕过办法：直接用你的 `.wem` 覆盖工程目录里同名的 `[序号]ID.wem`，文件名保持不变。我实测过这个办法有效。
- 【已验证，Silver 教程】用 wwiseutil 替换 “Shell 类” bank（磨刀、铳枪炮击等）会导致静音。太刀的 `Wp03_Cmn_m` 属于 cmn 类，不受影响。
- 【已验证，Suedo 教程】有人遇到“改了反而静音”的情况，换用 RingingBloom（模式选 MHRise 或 RE8）重新打包可以解决。
- 【已验证】音效 mod 和太刀语音 mod 改的是同一个文件，不能同时启用。想要两者兼得，需要把语音也一起做进你自己的 `Wp03_Cmn_m`。

---

## 5. 风险提示
- 改的只是客户端本地的声音资源，不影响伤害数值。【推断】联机时其他人听不到你的音效，被检测到的风险很低，但卡普空对 mod 没有正式表态，风险请自行承担。
- 游戏更新后，REFramework 和 Sound Debugger 的数据库可能需要等作者更新。作者原话：“Please check for mod updates promptly after the game update.” 每次大版本更新后，都建议重新提取原版 bank 并重新打包。
- 重播某些效果音可能导致游戏崩溃（Sound Debugger README）。
- Nexus 上的 mod 基本都要求登录才能下载。

## 6. 仍然未知、需要你在本地实测的事项
1. 太刀各招式的具体 `wem_id`，以及“大居合失败”“普通攻击挥空”是否各有独立音效。
2. MHWS Sound Tool 自动转码出来的 wem 在当前版本游戏里能否正常发声；不行时改用 Wwise 手动导出 Vorbis。
3. 当前游戏版本的 `Wp03_Cmn_m` 与 2025 年的老 mod 文件是否一致。

## 参考来源
- Nexus Mods（通过 `https://api.nexusmods.com/v2/graphql` 读取描述和文件列表）：#929、#642、#1240、#913、#1189、#1513、#1703、#1958、#2558、#3044、#3246、#4628、#5078、#93、#65、#349
- Suedo 的音效 mod 教程（#642 描述中的链接）：https://docs.google.com/document/d/1QW4e2GIZofhZXvobccG3Cavdea5xTCoGC56UmyVhjto
- 踩蘑菇：[用 Wwiseutil/Ringingbloom 制作音效 MOD 教程](https://www.caimogu.cc/post/1914667.html) · [MHWS Sound Tool 发布帖](https://www.caimogu.cc/post/1952570.html) · [太刀音效 mod（荒野最终更新可用）](https://www.caimogu.cc/post/1940844.html)
- GitHub：[eigeen/mhws-sound-tool](https://github.com/eigeen/mhws-sound-tool) · [paean-of-guidance/sound-debugger](https://github.com/paean-of-guidance/sound-debugger) · [eigeen/ree-pak-gui](https://github.com/eigeen/ree-pak-gui) · [Silvris/RingingBloom](https://github.com/Silvris/RingingBloom) · [hpxro7/wwiseutil](https://github.com/hpxro7/wwiseutil) · [vgmstream](https://github.com/vgmstream/vgmstream)
