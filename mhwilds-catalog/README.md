# 《怪物猎人：荒野》现成 mod 大全（太刀与音频方向）

数据抓取日期：2026-10-12。来源：Nexus Mods 公开 API。荒野分区共 3869 个 mod，其中非成人 2865 个，本目录收录 599 个。成人内容已排除。
由 [`tools/build_catalog.py`](../tools/build_catalog.py) 自动生成，重新运行即可更新。完整明细见 [`mods.csv`](mods.csv)，可以用 Excel 打开筛选。

**先看精选：** [PICKS.md](PICKS.md)，是人工挑出的太刀和音效方向推荐。

**怎么看：**
- 最后更新带 ✅ 表示在 TU4（2025-12-16）之后更新过，在当前版本可用的概率更高；没有 ✅ 的不代表不能用，但要看评论区确认。
- “改动的音效库”是从压缩包文件列表读出来的音效库文件名（Wwise 音频包，位于 `natives/STM/Sound/Wwise/`）。**同一个音效库只能有一个 mod 生效**，后装的会覆盖先装的。
- 几乎所有音频 mod 都需要 [REFramework](https://www.nexusmods.com/monsterhunterwilds/mods/93) 并在其菜单中勾选 Enable Loose File Loader（散件加载）；推荐用 [Fluffy Mod Manager](https://www.fluffyquack.com/) 管理。
- “（无法预览）”：Nexus 对较新上传的文件换了存储路径，公开接口读不到压缩包内容，改了哪个库只能下载后自己看。
- 每节内按点赞数从高到低排序。

## 目录
- [T. 音频相关工具 / 框架（1）](#t)
- [A. 太刀音效 / 语音（43）](#a)
- [B. 通用战斗音效（太刀也会触发）（57）](#b)
- [C. 太刀玩法 / 判定 / 手感（20）](#c)
- [D. 太刀外观 / 模型（含多武器共用模型）（115）](#d)
- [E. 角色 / 猎人 / 随从 / NPC 语音（35）](#e)
- [F. BGM / 音乐（72）](#f)
- [G. 其它武器音效（71）](#g)
- [H. 其它音效（道具、环境、UI、怪物等）（42）](#h)
- [I. 通用热门：前置 / 工具 / UI / 性能 / 玩法（143）](#i)
- [冲突速查：热门音效库被哪些 mod 改动](#conflicts)

<a id="t"></a>
## T. 音频相关工具 / 框架（1）

做或调试音效 mod 时用得到的工具，以及能播放自定义音频的框架类 mod。

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [声音调试器：游戏音效事件记录](https://www.nexusmods.com/monsterhunterwilds/mods/3246)<br><sub>Sound Debugger - game sound event logging</sub> | 1.0.2 | 2026-02-15 ✅ | 7 / 408 |  | 基于REFramework的模组，可在怪物猎人荒野中实时监控并调试声音事件。 |

<a id="a"></a>
## A. 太刀音效 / 语音（43）

全部列出。改同一个音效库的 mod 互相冲突，同一时间只能启用一个。

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [只狼太刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/929)<br><sub>Sekiro Long Sword Sounds</sub> | 2.0.0 | 2025-03-24  | 88 / 3.9k | `wp03_cmn_m` | 将太刀的多个音效替换为只狼中的音效。 |
| [更酷的太刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/642)<br><sub>Cooler Longsword Sounds</sub> | 1.2 | 2025-03-22  | 86 / 4.1k | `wp03_cmn_m` | 将太刀大部分招式的音效替换为（作者认为）更酷的音效。 |
| [太刀音效改进](https://www.nexusmods.com/monsterhunterwilds/mods/1240)<br><sub>Longsword SFX Improvement</sub> | 1.21 | 2025-03-27  | 85 / 4.6k | `wp03_cmn_m` | 改进太刀的格挡（GP）及练气解放无双斩音效。 |
| [太刀看破斩与居合纳刀成功提示音](https://www.nexusmods.com/monsterhunterwilds/mods/913)<br><sub>Longsword Foresight Slash And Iai Sheathe Success Ding SFX</sub> | 1.0 | 2025-03-18  | 84 / 2.9k | `wp03_cmn_m` | 将太刀看破斩与居合纳刀成功时的提示音替换为从怪物猎人世界提取的原版音效。 |
| [异度神剑2 光 太刀语音（日语）](https://www.nexusmods.com/monsterhunterwilds/mods/781)<br><sub>Xenoblade Chronicles 2 Mythra Long Sword Voice (Janpanese)</sub> | 1.0.0 | 2025-03-16  | 65 / 2.4k | `wp03_cmn_m` | 用异度神剑2中光（Mythra）的日语语音替换太刀语音。 |
| [碧蓝幻想Relink 娜尔梅亚语音替换（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/1413)<br><sub>GBFR-Narmaya's voice Replacement (Long Sword)</sub> | 1.0 | 2025-03-30  | 54 / 1.5k | `wp03_cmn_m` | 将太刀音效替换为碧蓝幻想Relink中娜尔梅亚（Narmaya）的语音。 |
| [太刀黑贞语音替换（FGO）](https://www.nexusmods.com/monsterhunterwilds/mods/1703)<br><sub>Longsword Jalter Audio Replacement (Jeanne d'Arc-Alter) (FGO)</sub> | 1.0 | 2025-04-09  | 39 / 1.7k | `wp03_cmn_m` | 为太刀的多个动作添加FGO中黑贞（贞德Alter）的配音。 |
| [街霸3.3格挡音效替换完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/1264)<br><sub>3rd Strike Parry over Perfect Guards</sub> | 1.2 | 2025-04-07  | 39 / 1.4k | `hit_hm_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp03_cmn_m` … | 将完美格挡音效替换为街头霸王3.3的格挡音效，适用于片手剑、大剑、太刀、长枪、铳枪、斩击斧、盾斧、重弩及相杀。 |
| [阿尔托莉雅语音替换太刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1231)<br><sub>Altria Pendragon voice replace longsword sound effects</sub> | 1.0.0 | 2025-03-25  | 38 / 1.5k | `wp03_cmn_m` | 用阿尔托莉雅·潘德拉贡的语音替换太刀部分技能的音效。 |
| [异度神剑2 焰 太刀语音（日语）](https://www.nexusmods.com/monsterhunterwilds/mods/1033)<br><sub>Xenoblade Chronicles 2 Pyra Long Sword Voice (Janpanese)</sub> | 1.0.0 | 2025-03-21  | 33 / 1.0k | `wp03_cmn_m` | 用异度神剑2中焰（Pyra）的日语语音替换太刀语音。 |
| [Osoi 回避音效](https://www.nexusmods.com/monsterhunterwilds/mods/1965)<br><sub>Osoi Dodge Sound</sub> | 1.0 | 2025-04-19  | 28 / 860 | `wp02_cmn_m`<br>`wp03_cmn_m`<br>`wp11_cmn_m` | 将太刀、弓和双刀的完美回避音效替换为“Osoi!（太慢了）”。 |
| [太刀居合音效：M1加兰德](https://www.nexusmods.com/monsterhunterwilds/mods/3044)<br><sub>Longsword Iai SFX - M1 Garand</sub> | 1.2 | 2025-08-12  | 28 / 1.2k | `wp03_cmn_m` | 将特殊纳刀和居合拔刀气刃斩的音效替换为M1加兰德步枪弹夹弹出声与枪声。 |
| [鸣潮 女漂泊者及其镰刀与语音](https://www.nexusmods.com/monsterhunterwilds/mods/1911)<br><sub>Female Rover and her scythe_sword_voice lines (Wuthering Waves)</sub> | v1.1 | 2025-06-12  | 25 / 691 | `player_actvoice_f03`<br>`wp03_cmn_m` | 用鸣潮中带湮灭之翼的女漂泊者替换男性Quematrice套装，并用其镰刀等替换满级绚辉太刀和Lala Barina太刀。 |
| [碧蓝幻想Relink 夏洛特语音替换（大剑和太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/1292)<br><sub>GBFR-Charlotta's voice Replacement (Great Sword and Long Sword)</sub> | 1.0 | 2025-04-11  | 23 / 673 | `wp00_cmn_m`<br>`wp03_cmn_m` | 将大剑音效替换为碧蓝幻想Relink中夏洛特（Charlotta）的语音。 |
| [太刀只狼弹刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/2558)<br><sub>Long Sword with Sekiro Parry Sound</sub> | 1.0 | 2025-05-26  | 22 / 1.4k | `wp03_cmn_m` | 将太刀居合拔刀气刃斩与看破斩的原版音效替换为只狼的弹刀音效。 |
| [罪恶装备Counter音效：太刀看破斩](https://www.nexusmods.com/monsterhunterwilds/mods/3910)<br><sub>Guilty Gear Counter for Longsword Foresight Slash</sub> | 1.0 | 2026-02-07 ✅ | 20 / 613 | `wp03_cmn_m` | 将太刀看破斩音效替换为罪恶装备Strive的Counter音效。 |
| [Where's Your Motivation（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/1898)<br><sub>Where's Your Motivation (Long Sword)</sub> | 1.0.1 | 2025-04-17  | 19 / 969 | `wp03_cmn_m` | 将太刀反击音效替换为鬼泣中维吉尔的名台词“Where's your motivation”。 |
| [明日方舟 令 太刀语音](https://www.nexusmods.com/monsterhunterwilds/mods/597)<br><sub>ARKNIGHTS_LING long sword voice</sub> | V3S | 2025-03-12  | 17 / 679 | `wp03_cmn_m` | 用明日方舟干员令的语音替换游戏中的太刀音效。 |
| [世界版居合“叮”音效](https://www.nexusmods.com/monsterhunterwilds/mods/1189)<br><sub>MHW Tin sound for iai</sub> | 1.0 | 2025-03-24  | 17 / 478 |  | 将太刀居合与看破斩成功的音效替换为怪物猎人世界中的“叮~”声。 |
| [Gawr Gura 相杀/反击/完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1303)<br><sub>Replace Offset-Counter-Perfect Guard SFX with Gawr Gura</sub> | 1.0a | 2025-03-31  | 15 / 1.1k | `hit_hm_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp03_cmn_m` … | 将相杀、太刀反击和完美格挡的提示音替换为Gawr Gura的语音。 |
| [勇气太刀气刃斩GP音效](https://www.nexusmods.com/monsterhunterwilds/mods/1801)<br><sub>Valor LS Spirit Slash GP SFX</sub> | 1.0 | 2025-04-12  | 15 / 406 | `hit_hm_cmn` | 将相杀音效替换为XX中勇气太刀气刃斩1 GP的音效。 |
| [太刀NOICE反击音效](https://www.nexusmods.com/monsterhunterwilds/mods/823)<br><sub>Longsword NOICE counter sound replacement</sub> | 1.0 | 2025-03-17  | 14 / 699 | `wp03_cmn_m` | 将太刀完美反击音效替换为Michael Rosen经典的“noice”语音（去掉了咂舌声）。 |
| [音乃瀬奏 相杀/反击/完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1308)<br><sub>Replace Offset-Counter-Perfect Guard SFX with Otonose Kanade</sub> | 1.0a | 2025-03-31  | 14 / 773 | `hit_hm_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp03_cmn_m` … | 将相杀、太刀反击和完美格挡的提示音替换为音乃瀬奏的语音。 |
| [绮々罗々薇薇 相杀/反击/完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1302)<br><sub>Replace Offset-Counter-Perfect Guard SFX with Kikirara Vivi</sub> | 1.0a | 2025-03-31  | 14 / 591 | `hit_hm_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp03_cmn_m` … | 将相杀、太刀反击和完美格挡的提示音替换为Kikirara Vivi的语音。 |
| [太刀武士语音替换（荣耀战魂/FGO）](https://www.nexusmods.com/monsterhunterwilds/mods/1513)<br><sub>Longsword Samurai Audio Replacement (For Honor) (FGO)</sub> | 1.0 | 2025-04-03  | 13 / 331 | `wp03_cmn_m` | 为太刀的多个动作添加荣耀战魂与FGO中女武士角色的配音。 |
| [牢大太刀登龙MAN](https://www.nexusmods.com/monsterhunterwilds/mods/1016)<br><sub>Kobe LS Helmbreaker MAN</sub> | 1.0.1 | 2025-03-20  | 10 / 303 | `wp03_cmn_m` | 将科比（牢大）梗混入太刀气刃兜割（登龙）的音效中。 |
| [爱丽丝太刀语音](https://www.nexusmods.com/monsterhunterwilds/mods/1958)<br><sub>AL_1s Longsword mod</sub> | ver1.0 | 2025-04-19  | 10 / 523 | `wp03_cmn_m` | 作者参考世界时的习惯，制作了一套较为干净简洁的爱丽丝（AL-1S）太刀语音。 |
| [Chiikawa乌萨奇太刀攻击音效](https://www.nexusmods.com/monsterhunterwilds/mods/2685)<br><sub>Longsword Sound Chiikawa Usagi's attack sound effect</sub> | 2.0 | 2025-06-07  | 9 / 424 | `wp03_cmn_m` | 为太刀添加乌萨奇更加疯癫的攻击音效，让你听起来更像太刀侠。 |
| [女神异闻录5 Joker 太刀语音（日语）](https://www.nexusmods.com/monsterhunterwilds/mods/751)<br><sub>Persona 5 Joker Long Sword Voice (Japanese)</sub> | 1.0.0 | 2025-03-15  | 8 / 392 | `wp03_cmn_m` | 用女神异闻录5中Joker的日语语音替换太刀音效。 |
| [太刀WOOOW反击音效](https://www.nexusmods.com/monsterhunterwilds/mods/897)<br><sub>Longsword WOOOW Counter Sound</sub> | v1.0 | 2025-03-18  | 8 / 524 | `wp03_cmn_m` | 将太刀反击音效替换为“WOOOW”的声音。 |
| [马保国音效](https://www.nexusmods.com/monsterhunterwilds/mods/1004)<br><sub>mabaoguo   Sound</sub> | 1.0 | 2025-03-20  | 8 / 334 | `player_actvoice_f03`<br>`wp03_cmn_m` | 将太刀音效替换为马老师（马保国）的语音。 |
| [MLG 格挡/完美格挡/完美回避/相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1353)<br><sub>MLG Parry Perfect Guard Perfect Dodge and Offset</sub> | 2.0 | 2026-07-27 ✅ | 8 / 574 | （无法预览） | 将多种武器的完美格挡、格挡、完美回避和相杀音效替换为“Mom get the camera”梗音效。 |
| [太刀反击：Show Me A Good Time Jack](https://www.nexusmods.com/monsterhunterwilds/mods/2217)<br><sub>LS counter - Show Me A Good Time Jack</sub> | 1 | 2025-04-30  | 8 / 294 | `wp03_cmn_m` | 将太刀反击音效替换为“Show Me A Good Time, Jack!”。 |
| [时乃空 相杀/反击/完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1305)<br><sub>Replace Offset-Counter-Perfect Guard SFX with Tokino Sora</sub> | 1.0a | 2025-03-31  | 7 / 462 | `hit_hm_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp03_cmn_m` … | 将相杀、太刀反击和完美格挡的提示音替换为时乃空的语音。 |
| [Gigi Murin 相杀/反击/完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1304)<br><sub>Replace Offset-Counter-Perfect Guard SFX with Gigi Murin</sub> | 1.0a | 2025-03-31  | 7 / 560 | `hit_hm_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp03_cmn_m` … | 将相杀、太刀反击和完美格挡的提示音替换为Gigi Murin的语音。 |
| [Deadlock Yamato太刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1387)<br><sub>DeadLock Yamato SFX for Long sword</sub> | 1.0 | 2025-03-29  | 6 / 247 | `wp03_cmn_m` | 将部分太刀音效替换为Deadlock中Yamato相关的音效。 |
| [女猎人语音（日语 太刀和大剑）](https://www.nexusmods.com/monsterhunterwilds/mods/2822)<br><sub>Female Hunter's Voice (JPN Long sword and Great swrod)</sub> | 1.0 | 2025-07-05  | 6 / 280 | `hit_hm_cmn`<br>`weapon_cmn`<br>`wp00_cmn_m`<br>`wp03_cmn_m` | 为大剑和太刀音效加入女猎人语音，仅限日语3号语音。 |
| [曼城茶座语音替换太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1429)<br><sub>Manhattan Cafe replace Long Sword sound</sub> | 1.0.0 | 2025-03-30  | 6 / 256 | `human_common_effect`<br>`player_actvoice_f03`<br>`player_common_foley`<br>`wp03_cmn_m` | 用赛马娘曼城茶座的语音替换太刀语音，部分语音适用6号角色语音。 |
| [太刀居合与看破斩Vine Boom音效](https://www.nexusmods.com/monsterhunterwilds/mods/2624)<br><sub>Vine Boom for Longsword IAI and Foresight</sub> | 1 | 2025-06-03  | 5 / 427 | `wp03_cmn_m` | 将看破斩与居合拔刀气刃斩反击成功的音效替换为Vine Boom音效。 |
| [Ginka太刀语音](https://www.nexusmods.com/monsterhunterwilds/mods/1856)<br><sub>Ginka long sword</sub> | V1.1 | 2025-04-15  | 4 / 267 | `hit_weapon_cmn`<br>`wp03_cmn_m` | 用Ginka的语音替换太刀的部分音效。 |
| [艾瑞莉娅与菲奥娜语音（韩语）](https://www.nexusmods.com/monsterhunterwilds/mods/4280)<br><sub>Irelia and Fiora's Voice (Korean)</sub> | 1 | 2026-04-13 ✅ | 3 / 281 | `hit_hm_cmn`<br>`weapon_cmn`<br>`wp00_cmn_m`<br>`wp03_cmn_m` | 用英雄联盟中艾瑞莉娅与菲奥娜的韩语语音替换大剑和太刀音效。 |
| [樱小路露娜太刀语音](https://www.nexusmods.com/monsterhunterwilds/mods/4137)<br><sub>Sakurakouji Luna Longsword Voicemod</sub> | 2.14 | 2026-03-15 ✅ | 2 / 290 | `wp03_cmn_m` | 用樱小路露娜的语音替换太刀音效。 |
| [BBTAG太刀反击音效](https://www.nexusmods.com/monsterhunterwilds/mods/3496)<br><sub>BBTAG Longsword Counter</sub> | 1.0 | 2025-10-30  | 1 / 176 | `wp03_cmn_m` | 为太刀反击加入苍翼默示录Cross Tag Battle的Counter音效。 |

<a id="b"></a>
## B. 通用战斗音效（太刀也会触发）（57）

相杀、反击、完美格挡/回避、会心、命中、眩晕、伤口等。改公共库（`hit_hm_cmn`、`weapon_cmn` 等）的 mod 彼此冲突。

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [磨刀完成音效替换 - Nice.](https://www.nexusmods.com/monsterhunterwilds/mods/156)<br><sub>Sharpening Complete Sound Replacement - Nice.</sub> | 1.0.1 | 2025-03-06  | 273 / 9.4k | `human_common_effect` | 将磨刀完成音效替换为Michael Rosen“Hot Food”视频中经典的“Nice.”。 |
| [经典怪物猎人音效 v1.1.0 - 道具](https://www.nexusmods.com/monsterhunterwilds/mods/1349)<br><sub>Classic Monster Hunter SFX v1.1.0 - Items</sub> | v1.1.0 | 2025-05-08  | 217 / 6.7k | `[mh1-fu gather only]-gui_cmn`<br>`[mh1-fu gather]-gui_cmn`<br>`[mh3-gu gather only]-gui_cmn`<br>`[mh3-gu gather]-gui_cmn` … | 逐步将游戏中大部分音效改为经典版本，每次更新侧重不同部分。 |
| [BONK - 眩晕音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/349)<br><sub>BONK - Stun Sound Replacement</sub> | 1 | 2025-03-09  | 180 / 6.5k | `hit_hm_cmn` | 将眩晕音效替换为BONK敲头声。 |
| [PERFECT完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/1209)<br><sub>PERFECT Perfect Guard</sub> | 1.1 | 2025-03-26  | 142 / 4.7k | （无法预览） | 为完美格挡添加格斗游戏式的“PERFECT!”音效。 |
| [罪恶装备Counter相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1339)<br><sub>Offset COUNTER from ggst</sub> | 1.0 | 2025-03-28  | 131 / 3.9k | `hit_hm_cmn` | 将相杀成功的音效替换为罪恶装备Strive的Counter音效。 |
| [会心音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/2088)<br><sub>Critical Sound Replacer</sub> | 1.2 | 2026-01-13 ✅ | 123 / 4.7k | `hit_hm_cmn`<br>`hit_hm_cmn` | 将会心音效替换为7种不同选项之一。 |
| [完美格挡音效替换 - 冰原攻守势](https://www.nexusmods.com/monsterhunterwilds/mods/327)<br><sub>Perfect Guard Sound Replacement - Offensive Guard from MHWi</sub> | 1.0 | 2025-03-16  | 78 / 3.4k | `human_skill`<br>`wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m` … | 将完美格挡音效替换为怪物猎人世界冰原中攻势防御（Offensive Guard）的发动音效。 |
| [罪恶装备Counter完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/1335)<br><sub>Guilty Gear Counters Wilds</sub> | 1 | 2025-03-30  | 78 / 2.6k | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 为完美格挡加入罪恶装备的“Counter”音效。 |
| [玩家受击音量修复](https://www.nexusmods.com/monsterhunterwilds/mods/1025)<br><sub>Player hit sound volume fix</sub> | 1.0 | 2025-03-21  | 55 / 1.2k | `human_common_effect` | 原本战斗中几乎听不到的玩家受击提示音，此模组将其音量调高。 |
| [皇家护卫完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1896)<br><sub>Perfect Royal Guard SFX</sub> | 1.0.0 | 2025-04-17  | 47 / 1.6k | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为鬼泣5中皇家护卫（Royal Guard）精准格挡的音效。 |
| [蒸汽与歌谣1.4 - 盾斧铳枪音效重制](https://www.nexusmods.com/monsterhunterwilds/mods/1952)<br><sub>Ballad Of Steam and Song 1.4 - CB GL audio overhaul and hitsounds</sub> | 1.4 | 2026-04-03 ✅ | 45 / 1.8k | `wp07_cmn_m`<br>`wp07_shell`<br>`wp09_cmn_m` | 重制盾斧及铳枪的音效与命中音效，改善荒野中这两种武器的听感。 |
| [斩服少女 DON'T LOSE YOUR WAY 角力](https://www.nexusmods.com/monsterhunterwilds/mods/3748)<br><sub>Kill la Kill DONT LOSE YOUR WAY Power Clash</sub> | 1.0 | 2026-01-05 ✅ | 40 / 1.5k | `weapon_cmn` | 在角力获胜时播放斩服少女的《Before My Body is Dry》。 |
| [Shing sparkle sparkle 磨刀音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/383)<br><sub>Shing sparkle sparkle - Sharpen Audio Replacement</sub> | 1.0.1 | 2026-09-22 ✅ | 39 / 789 | （无法预览） | 将磨刀完成时的闪光音效替换为痞老板的“Shing, sparkle sparkle”。 |
| [角力成功时播放RULES OF NATURE](https://www.nexusmods.com/monsterhunterwilds/mods/2977)<br><sub>Play RULES OF NATURE when you succeed in a Power Clash</sub> | 1.1 | 2025-07-27  | 35 / 1.7k | `weapon_cmn` | 角力成功时播放《RULES OF NATURE》。 |
| [完美格挡与斩击斧反击斩改为崛起音效](https://www.nexusmods.com/monsterhunterwilds/mods/3204)<br><sub>Replace Perfect Guard and Switch AXE CounterSlash SFX to RISE Perfect Guard SFX</sub> | 1.0 | 2025-09-05  | 35 / 1.7k | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡与斩击斧反击斩的音效替换为崛起的完美格挡音效。 |
| [瞬间移动完美回避](https://www.nexusmods.com/monsterhunterwilds/mods/2508)<br><sub>Instant Transmision Perfect Dodge</sub> | 1.1 | 2025-05-26  | 35 / 1.3k | `wp02_cmn_m`<br>`wp11_cmn_m` | 将弓和双刀的完美回避音效替换为龙珠的瞬间移动音效。 |
| [军团要塞2会心音效](https://www.nexusmods.com/monsterhunterwilds/mods/1336)<br><sub>TF2 Critical hits</sub> | 1.0.0 | 2025-03-27  | 32 / 1.3k | `hit_hm_cmn`<br>`hit_weapon_cmn` | 将会心音效替换为军团要塞2（TF2）的暴击音效。 |
| [完美回避 I'm Not Gonna Sugar Coat It音效](https://www.nexusmods.com/monsterhunterwilds/mods/762)<br><sub>Perfect Dodge I'm Not Gonna Sugar Coat It Sound Effect</sub> | 1.0 | 2025-03-17  | 28 / 1.2k | `wp02_cmn_m`<br>`wp11_cmn_m` | 将弓和双刀的完美回避音效替换为“I'm not gonna sugar coat it”梗音效。 |
| [Live Mas - 塔可钟眩晕音效](https://www.nexusmods.com/monsterhunterwilds/mods/1865)<br><sub>Live Mas - Taco Bell Stun Damage Sound</sub> | 1.0 | 2025-04-15  | 28 / 1.1k | `hit_hm_cmn` | 将眩晕伤害音效替换为塔可钟（Taco Bell）的提示音。 |
| [全武器相杀DAMN音效](https://www.nexusmods.com/monsterhunterwilds/mods/1700)<br><sub>Non-sugarcoated Offsets for All Weapons (DAMN)</sub> | 2 | 2025-04-16  | 26 / 989 | `hit_hm_cmn` | 为所有武器的相杀加入响亮的“DAMN”音效。 |
| [狩猎笛自定义旋律](https://www.nexusmods.com/monsterhunterwilds/mods/3119)<br><sub>Hunting Horn Customize Music</sub> | 1.2 | 2026-01-02 ✅ | 25 / 852 |  | 自定义狩猎笛的旋律技能、按键与增益效果。 |
| [塔可钟完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/1990)<br><sub>Tacobell on Perfect guard</sub> | 1.1 | 2025-04-21  | 22 / 778 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为经典的塔可钟（Taco Bell）提示音。 |
| [只狼弹刀音效替换完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/4167)<br><sub>Replace Perfect Guard SFX with Sekiro weapon deflect SFX</sub> | 1.0 | 2026-03-19 ✅ | 21 / 672 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为只狼中的弹刀音效。 |
| [大剑完美格挡DAMN](https://www.nexusmods.com/monsterhunterwilds/mods/1187)<br><sub>Great Sword Pefect Guard DAMN</sub> | 1.0 | 2025-03-26  | 19 / 852 | `wp00_cmn_m` | 将相杀和完美格挡音效替换为“I'm not gonna sugarcoat it DAMN!”梗音效。 |
| [宇泽玲纱完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1367)<br><sub>Uzawa Reisa Perfect Guard Sound</sub> | 1.0 | 2025-03-28  | 19 / 522 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为蔚蓝档案宇泽玲纱的“HOHO~”。 |
| [冰原攻势防御音效替换完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/3219)<br><sub>Replace Perfect Guard SFX to ICEBORNE Offiensive Guard</sub> | 1.0 | 2025-10-11  | 19 / 710 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为冰原的攻势防御（Offensive Guard）音效。 |
| [九日格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/3460)<br><sub>Nine Sols Parry sound</sub> | 1.0 | 2025-10-24  | 19 / 2.3k | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 完美格挡时播放九日（Nine Sols）的格挡音效，适用于所有可防御武器。 |
| [ULTRAKILL格挡音效相杀](https://www.nexusmods.com/monsterhunterwilds/mods/1901)<br><sub>Offset Counter but ULTRAKILL's one</sub> | 1.0.0 | 2025-04-16  | 18 / 783 | `hit_hm_cmn` | 将相杀成功的音效替换为ULTRAKILL的格挡音效。 |
| [宇泽玲纱相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1368)<br><sub>Uzawa Reisa Offset Attack Sound</sub> | 1.0 | 2025-03-28  | 15 / 368 | `hit_hm_cmn` | 将相杀音效替换为蔚蓝档案宇泽玲纱的“Toryaa~”。 |
| [猎天使魔女风完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/1892)<br><sub>Beautiful Perfect Guard MH Wilds X Bayonetta</sub> | 1 | 2025-04-16  | 15 / 579 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为猎天使魔女风格的音效。 |
| [片手剑只狼弹刀音效替换完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/2379)<br><sub>SnS - Sekiro Parry SFX replaces Perfect Guard SFX</sub> | Latest | 2025-05-11  | 15 / 712 | `wp01_cmn_m` | 将片手剑完美格挡音效替换为只狼的弹刀音效。 |
| [Doink相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1564)<br><sub>Doink Offset</sub> | 1 | 2025-04-04  | 14 / 501 | `hit_hm_cmn` | 为相杀添加DOINK音效。 |
| [长枪反击与完美格挡 - DAMN](https://www.nexusmods.com/monsterhunterwilds/mods/1712)<br><sub>Lance Charge Counter and Perfect Guard - I'm Not Gonna Sugarcoat it</sub> | 1.0 | 2025-04-09  | 13 / 377 | `wp06_cmn_m` | 将长枪蓄力反击与完美格挡音效替换为“I'm not gonna sugarcoat it”梗中的“DAMN!”。 |
| [移除命中音效中的“啾”声](https://www.nexusmods.com/monsterhunterwilds/mods/478)<br><sub>No pew hit sounds</sub> | 2.0 | 2025-05-08  | 12 / 411 | `hit_hm_cmn`<br>`hit_weapon_cmn` | 移除部分命中音效中的鸟鸣般“啾”声。 |
| [蔚蓝档案 陆八魔亚瑠语音](https://www.nexusmods.com/monsterhunterwilds/mods/4232)<br><sub>Blue Archive Aru Voice Mod</sub> | 1.1 | 2026-04-07 ✅ | 11 / 698 | `human_common_effect`<br>`player_actvoice_f03`<br>`player_chatactionvoice_f03`<br>`weapon_cmn` | 用陆八魔亚瑠的语音替换6号（日语）语音。 |
| [狩猎音乐祭 - 荒野版](https://www.nexusmods.com/monsterhunterwilds/mods/1001)<br><sub>Shuryou Ongakusai -  Wilderness Edition</sub> | 1.0 | 2025-04-17  | 10 / 242 | `bgm_01_00_jukebox_m`<br>`bgm_01_00_jukebox_m`<br>`bgm_jukebox_1st_m`<br>`bgm_jukebox_1st_m` … | 将游戏乐曲替换为管弦乐音乐会中的对应版本。 |
| [小雪相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/1362)<br><sub>Koyuki Offset Attack Sound</sub> | 1.0 | 2025-03-28  | 9 / 255 | `hit_hm_cmn` | 用蔚蓝档案小雪的“Nihaha”替换相杀音效。 |
| [Yukari完美格挡音效](https://www.nexusmods.com/monsterhunterwilds/mods/1364)<br><sub>Yukari Sound for Perfect Guard</sub> | 1.0 | 2025-03-28  | 9 / 343 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为Yukari的声音。 |
| [艾尔登法环破韧音效替换完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/4713)<br><sub>Elden Ring Poise Break Perfect Guard Replacement</sub> | 1 | 2026-08-10 ✅ | 7 / 228 | （无法预览） | 将完美格挡音效替换为艾尔登法环中的破韧音效。 |
| [S4 League会心音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/272)<br><sub>S4 League Critical hit SFX replacement</sub> | 1.0 | 2025-03-06  | 6 / 303 | `hit_hm_cmn` | 将会心音效替换为S4 League中的暴击提示语音。 |
| [Make it Out Alive（角力）](https://www.nexusmods.com/monsterhunterwilds/mods/4164)<br><sub>Make it Out Alive (Power Clash)</sub> | 1 | 2026-03-22 ✅ | 6 / 375 | `weapon_cmn` | 角力获胜时播放ONE OK ROCK的《Make it Out Alive》。 |
| [我操冰磨刀音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/904)<br><sub>wocao-bin-sharpening sound replacement</sub> | 1.00 | 2025-03-18  | 5 / 188 | `human_common_effect` | 将磨刀音效替换为“我操冰”梗语音。 |
| [Ado相杀音乐](https://www.nexusmods.com/monsterhunterwilds/mods/4478)<br><sub>Ado Music for Offsets</sub> | 1.1 | 2026-08-09 ✅ | 5 / 494 | （无法预览） | 相杀时播放Ado的音乐。 |
| [魔女时间完美格挡](https://www.nexusmods.com/monsterhunterwilds/mods/2013)<br><sub>Witchtime Perfect guard</sub> | V1.0 | 2025-04-21  | 4 / 247 | `wp00_cmn_m`<br>`wp01_cmn_m`<br>`wp06_cmn_m`<br>`wp07_cmn_m` … | 将完美格挡音效替换为猎天使魔女的魔女时间音效。 |
| [我的世界Steve“Oof”会心音效](https://www.nexusmods.com/monsterhunterwilds/mods/2169)<br><sub>Minecraft Steve Oof Crits</sub> | v1.0 | 2025-04-27  | 4 / 312 | `hit_hm_cmn` | 将所有武器的会心音效替换为我的世界Steve旧版的“oof”受伤声。 |
| [Zoio“Toma seu Mardito”相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/4499)<br><sub>Zoio Toma seu Mardito Offset Sound</sub> | 1 | 2026-06-03 ✅ | 4 / 187 | `hit_hm_cmn` | 将相杀音效替换为Zoio说“Toma seu Mardito”的语音。 |
| [相杀时播放Animals](https://www.nexusmods.com/monsterhunterwilds/mods/4919)<br><sub>Play Animals when you offset</sub> | 1.2 | 2026-10-11 ✅ | 4 / 661 | （无法预览） | 你或队友相杀怪物时自动播放《Animals》高潮片段，可在REF界面设置音量及是否升调。 |
| [角力成功时播放UNICORN](https://www.nexusmods.com/monsterhunterwilds/mods/2976)<br><sub>Play UNICORN when you succeed in a Power Clash</sub> | 1.0 | 2025-07-25  | 3 / 175 | `weapon_cmn` | 角力成功时播放《UNICORN》。 |
| [Cút ra ngoài 角力音效](https://www.nexusmods.com/monsterhunterwilds/mods/4158)<br><sub>Cut Ra Ngoai Power Clash SFX</sub> | 1.0 | 2026-03-18 ✅ | 3 / 93 | `weapon_cmn` | 角力成功时播放越南语梗“Cút ra ngoài”。 |
| [De Vai Lon 相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/4168)<br><sub>De Vai Lon Offset SFX</sub> | 1.0 | 2026-03-19 ✅ | 3 / 98 | `hit_hm_cmn` | 相杀成功时播放“de vai lon”梗音效。 |
| [ReoNa相杀音乐](https://www.nexusmods.com/monsterhunterwilds/mods/4473)<br><sub>ReoNa Music for Offsets</sub> | 1.0 | 2026-05-25 ✅ | 3 / 100 | `hit_hm_cmn` | 每次相杀时播放ReoNa的歌曲。 |
| [佐科维“saya akan lawan”角力与相杀音效](https://www.nexusmods.com/monsterhunterwilds/mods/4688)<br><sub>Power Clash and offset Replace With Jokowi saya akan lawan</sub> | 1.0 | 2026-08-03 ✅ | 3 / 58 | （无法预览） | 将角力和相杀音效替换为“saya akan lawan”语音。 |
| [小狗幽默曲：异常状态音乐](https://www.nexusmods.com/monsterhunterwilds/mods/4445)<br><sub>HUMORESQUE OF A LITTLE DOG Jingle for Impaired Statuses</sub> | 1.1 | 2026-06-18 ✅ | 2 / 84 | `human_common_effect` | 在眩晕、麻痹、被蛛网缠住或冰冻异常时播放《Humoresque of a Little Dog》。 |
| [Excellent 大剑真蓄力斩](https://www.nexusmods.com/monsterhunterwilds/mods/2945)<br><sub>Excellent GS TCS</sub> | 1.0 | 2025-07-22  | 2 / 141 | `wp00_cmn_m` | 将大剑真蓄力斩与完美格挡音效替换为李超狼的“Excellent”语音。 |
| [边狱公司 雷横 斩击斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/4088)<br><sub>Limbus company leiheng  Switch Axe Sound Effect</sub> | 1.1 | 2026-03-07 ✅ | 1 / 350 | `wp08_cmn_m` | 用边狱公司雷横的台词替换斩击斧属性解放、零距离解放斩及完美格挡等音效。 |
| [光环主题曲相杀](https://www.nexusmods.com/monsterhunterwilds/mods/4454)<br><sub>HALO Theme for Offsets</sub> | 1.0 | 2026-05-23 ✅ | 0 / 147 | `hit_hm_cmn` | 相杀时播放光环（HALO）的主题音乐。 |
| [Aimer《LAST STARDUST》或《Brave Shine》相杀](https://www.nexusmods.com/monsterhunterwilds/mods/4469)<br><sub>Aimer LAST STARDUST or Brave Shine for Offsets</sub> | 1.0 | 2026-05-24 ✅ | 0 / 130 | `hit_hm_cmn` | 相杀时播放Aimer的《LAST STARDUST》或《Brave Shine》。 |

<a id="c"></a>
## C. 太刀玩法 / 判定 / 手感（20）

非音频，与太刀相关。

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [自动看破与居合：更好的太刀体验](https://www.nexusmods.com/monsterhunterwilds/mods/287)<br><sub>Auto Foresight Slash and Auto IAI just Better LS Experience</sub> | 1.1.3 | 2025-04-04  | 724 / 51.3k |  | 自动触发看破斩与居合，并调整太刀数据以优化太刀体验。 |
| [移除居合延迟](https://www.nexusmods.com/monsterhunterwilds/mods/83)<br><sub>Remove Iai Delay</sub> | 1.0 | 2025-02-28  | 497 / 23.3k |  | 移除太刀居合拔刀气刃斩5帧的输入延迟。 |
| [太刀无限强化](https://www.nexusmods.com/monsterhunterwilds/mods/274)<br><sub>LongSword InfiniteEnhancement</sub> | 1.0.0 | 2025-03-06  | 215 / 8.7k |  | 让太刀的练气强化状态无限持续。 |
| [太刀刃色持续时间延长](https://www.nexusmods.com/monsterhunterwilds/mods/413)<br><sub>Longsword aura duration increase</sub> | 1.0 | 2025-12-25 ✅ | 178 / 7.0k |  | 将太刀刃色（练气等级）持续时间延长为2/4/8分钟。 |
| [更快的居合纳刀](https://www.nexusmods.com/monsterhunterwilds/mods/2118)<br><sub>Faster Iai Sheath</sub> | V1.0 | 2025-06-01  | 113 / 5.7k |  | 加快太刀的纳刀速度。 |
| [太刀居合与看破斩判定窗口加宽（TU4可用）](https://www.nexusmods.com/monsterhunterwilds/mods/3484)<br><sub>Increased Success Windows for Longsword IAI Counter and Foresight Slash (work TU 4)</sub> | 2 | 2026-02-21 ✅ | 58 / 4.5k |  | 延长居合反击与看破斩的成功判定时间，可选版本还增加反击后的无敌帧。 |
| [太刀DualSense扩展支持（自适应扳机与触觉反馈）](https://www.nexusmods.com/monsterhunterwilds/mods/2330)<br><sub>Long Sword Extended DualSense Support (Adaptive Trigger and Haptic Feedback) - LS</sub> | v2.3 | 2026-02-21 ✅ | 33 / 1.1k |  | 为居合拔刀气刃斩和气刃蓄力添加自适应扳机反馈，并在蓄力时加入触觉震动。 |
| [太刀相杀](https://www.nexusmods.com/monsterhunterwilds/mods/3230)<br><sub>Longsword Offsets</sub> | v1.0.8 | 2025-11-17  | 28 / 1.6k |  | 让太刀也拥有相杀攻击。 |
| [更好的太刀体验 - 修复与精简版](https://www.nexusmods.com/monsterhunterwilds/mods/4568)<br><sub>Better LS Experience - Fixed and Streamlined Editions</sub> | 3.5 | 2026-06-30 ✅ | 17 / 1.9k | （无法预览） | Better LS Experience模组的优化与修复分支，并附带多个重构的太刀框架。 |
| [太刀兜割增强](https://www.nexusmods.com/monsterhunterwilds/mods/1212)<br><sub>Longsword Helm Buff</sub> | 1.0 | 2025-03-24  | 13 / 718 |  | 将练气解放无双斩动作值恢复为荒野测试版数值，红刃兜割动作值恢复为冰原数值。 |
| [居合自适应扳机](https://www.nexusmods.com/monsterhunterwilds/mods/2264)<br><sub>Iai Adaptive Trigger</sub> | v1.0 | 2025-05-04  | 12 / 346 |  | 为居合拔刀气刃斩添加自适应扳机反馈。 |
| [Arsh的太刀姿势包 第1部分](https://www.nexusmods.com/monsterhunterwilds/mods/4254)<br><sub>Arsh's Longsword Pose Pack-Part 1</sub> | 1.0 | 2026-04-08 ✅ | 12 / 211 |  | 一些用于EMV Engine的太刀架势姿势包。 |
| [太刀动作值恢复冰原](https://www.nexusmods.com/monsterhunterwilds/mods/1059)<br><sub>Longsword MV back to Iceborne</sub> | 1.01 | 2025-03-23  | 10 / 470 |  | 参考冰原数值调整太刀动作值，动作值决定每次攻击造成的伤害比例。 |
| [历战王太刀 y](https://www.nexusmods.com/monsterhunterwilds/mods/4457)<br><sub>Arch-Tempered LongSword y</sub> | 4.0.2 | 2026-09-02 ✅ | 7 / 445 | （无法预览） | 提升武器响应，可取消硬直动画，修复原版回避后摇延迟，并可选不耗耐力翻滚。 |
| [勇气风格太刀](https://www.nexusmods.com/monsterhunterwilds/mods/4795)<br><sub>Valor Style Long Sword</sub> | 1 | 2026-08-29 ✅ | 4 / 290 | （无法预览） | 大幅重做太刀招式机制，并融入勇气风格（Valor Style）的理念。 |
| [移除太刀移动气刃斩](https://www.nexusmods.com/monsterhunterwilds/mods/3840)<br><sub>Remove Directional Spirit Slash - LongSword</sub> | 1.2 | 2026-01-26 ✅ | 3 / 253 |  | 移除太刀带方向的移动气刃斩。 |
| [双持太刀](https://www.nexusmods.com/monsterhunterwilds/mods/5025)<br><sub>Dual Longswords</sub> | 1 | 2026-10-03 ✅ | 3 / 171 | （无法预览） | 添加第二把太刀，第二击延迟可自定义，并拥有可开关的独立伤害判定。 |
| [太刀兜割后看破取消](https://www.nexusmods.com/monsterhunterwilds/mods/3600)<br><sub>Longsword - Helm Foresight Cancel</sub> | 1.0 | 2025-12-11  | 2 / 206 |  | 气刃兜割后可在空中连按看破斩，落地后立即作为第一个动作发出，免去额外延迟。 |
| [自动居合](https://www.nexusmods.com/monsterhunterwilds/mods/4975)<br><sub>autoIai</sub> | 1 | 2026-10-02 ✅ | 1 / 542 | （无法预览） | 为怪物猎人荒野制作，核心功能是自动居合拔刀斩与自动看破斩。 |
| [太刀红刃时斩味变红](https://www.nexusmods.com/monsterhunterwilds/mods/5089)<br><sub>Long Sword Red Spirit Level Sharpness Color</sub> | 1 | 2026-10-09 ✅ | 0 / 18 | （无法预览） | 当练气槽达到红刃等级时，太刀的斩味显示变为红色。 |

<a id="d"></a>
## D. 太刀外观 / 模型（含多武器共用模型）（115）

非音频。名称里带 LS 或太刀的武器模型 mod。

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [黑色武士刀合集](https://www.nexusmods.com/monsterhunterwilds/mods/2723)<br><sub>Black Katana Collection</sub> | 2 | 2026-08-05 ✅ | 396 / 17.9k | （无法预览） | 为太刀、大剑、长枪、片手剑、斩击斧、操虫棍和双刀提供黑色武士刀外观。 |
| [祝福之剑合集](https://www.nexusmods.com/monsterhunterwilds/mods/3622)<br><sub>Blessed Sword Collection</sub> | 1.2 | 2026-08-05 ✅ | 306 / 15.4k | （无法预览） | 将斩击斧、太刀、片手剑、盾斧、大剑、双刀替换为祝福之剑（Blessed Sword）。 |
| [绚辉太刀替换](https://www.nexusmods.com/monsterhunterwilds/mods/328)<br><sub>Artian Long Sword Replace</sub> | 0.2-fix | 2025-03-07  | 265 / 9.5k | `it0900_0001_m`<br>`it0900_0003_m`<br>`it0900_0004_m`<br>`it0900_0005_m` … | 将绚辉太刀模型替换为另一把武器。 |
| [异度神剑2 普纽玛的天之圣杯剑](https://www.nexusmods.com/monsterhunterwilds/mods/1054)<br><sub>Pneuma's Aegis Sword from Xenoblade Chronicles 2 (CB LS GS SNS SA)</sub> | 1.0 | 2026-08-06 ✅ | 224 / 9.1k | （无法预览） | 将满级绚辉盾斧、太刀、大剑、片手剑、斩击斧替换为异度神剑2中普纽玛的圣杯之剑。 |
| [异度神剑2 光的天之圣杯剑](https://www.nexusmods.com/monsterhunterwilds/mods/1013)<br><sub>Mythra's Aegis Sword from Xenoblade Chronicles 2 (LS GS SNS SA)</sub> | 1.0 | 2026-08-06 ✅ | 211 / 8.1k | （无法预览） | 将铠龙与绚辉的太刀、大剑、片手剑、斩击斧替换为异度神剑2中光的圣杯之剑。 |
| [紫泡狐龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1120)<br><sub>Violet Mizutsune Long Sword</sub> | 1.4 | 2025-03-24  | 209 / 8.8k |  | 用纯剑一文字替换绚辉太刀。 |
| [最终幻想14 彼岸此岸（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/1719)<br><sub>FFXIV Higan Shigan(LS)</sub> | 1.0 | 2026-02-24 ✅ | 196 / 9.6k |  | 将希望太刀替换为最终幻想14中的彼岸此岸（Higan Shigan）。 |
| [梦咒之剑合集（太刀 片手剑 双刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3453)<br><sub>Dreamspell Sword Collection (LS SNS DB)</sub> | 1.1 | 2026-08-08 ✅ | 194 / 5.8k | （无法预览） | 将太刀、双刀、片手剑替换为梦咒之剑（Dreamspell Sword）。 |
| [祖·西亚太刀 - 无刀鞘替代版](https://www.nexusmods.com/monsterhunterwilds/mods/2772)<br><sub>Zoh Shia Longsword - No sheath Alternative versions</sub> | 2 | 2026-08-05 ✅ | 190 / 8.8k | （无法预览） | 移除祖·西亚太刀的刀鞘，或将刀鞘替换为新版本。 |
| [神斩刀](https://www.nexusmods.com/monsterhunterwilds/mods/809)<br><sub>Divine Slasher</sub> | 2.0 | 2026-08-28 ✅ | 188 / 7.8k | （无法预览） | 将绚辉太刀替换为世界中的Divine Slasher。 |
| [异度神剑2 焰的天之圣杯剑](https://www.nexusmods.com/monsterhunterwilds/mods/965)<br><sub>Pyra's Aegis Sword from Xenoblade Chronicles 2 (LS GS SNS SA)</sub> | 1.01 | 2026-08-06 ✅ | 173 / 6.6k | （无法预览） | 将守护铠龙与绚辉的太刀、大剑、片手剑、斩击斧替换为异度神剑2中焰的圣杯之剑。 |
| [黄泉 -Naught- 太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2834)<br><sub>Acheron -Naught- Longsword</sub> | 2.1 | 2026-08-09 ✅ | 167 / 7.7k | （无法预览） | 将希望太刀替换为崩坏：星穹铁道中黄泉的武器。 |
| [艾尔登法环 罗刹大太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3211)<br><sub>Elden Ring_Rakshasa's Great Katana</sub> | 2 | 2026-08-07 ✅ | 164 / 7.4k | （无法预览） | 将太刀、大剑、斩击斧替换为艾尔登法环的罗刹大太刀。 |
| [最终幻想14 阿斯福德洛斯武士刀](https://www.nexusmods.com/monsterhunterwilds/mods/2653)<br><sub>FFXIV Asphodelos Samurai Blade</sub> | 1.0 | 2026-02-25 ✅ | 161 / 6.7k |  | 将希望太刀替换为最终幻想14中的Asphodelos Samurai Blade。 |
| [绚辉太刀替代外观（幻化武器）](https://www.nexusmods.com/monsterhunterwilds/mods/1277)<br><sub>Alternative Artian Longsword look. Layered Weapon.</sub> | 0.1 | 2025-03-26  | 154 / 5.2k |  | 将绚辉太刀原版外观替换为自定义外观，基础版和5级强化版各有一个文件。 |
| [赤月之形太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2315)<br><sub>Crimson Moon's Semblance Longsword</sub> | 4.1 | 2026-08-09 ✅ | 153 / 6.6k | （无法预览） | 将绚辉太刀替换为原神中阿蕾奇诺的镰刀。 |
| [艾尔登法环 血之溪流太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2428)<br><sub>Elden Ring Rivers of Blood Longsword</sub> | Ver.1.042.00.0 | 2026-08-11 ✅ | 133 / 4.7k | （无法预览） | 将火龙太刀（Wyvern Blade "Maple"）替换为艾尔登法环中的血之溪流。 |
| [太刀 - tachi](https://www.nexusmods.com/monsterhunterwilds/mods/3267)<br><sub>Longsword - tachi</sub> | 1.0.0 | 2026-02-25 ✅ | 128 / 7.2k |  | 替换Dosha Fatecleaver太刀的外观。 |
| [绚辉光剑（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/2965)<br><sub>Artian Lightsaber (Long Sword)</sub> | 1.0 | 2026-08-07 ✅ | 125 / 4.1k | （无法预览） | 将绚辉太刀（Dimensius）替换为光剑外观。 |
| [终焉星太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3309)<br><sub>Omega Long Sword</sub> | 1.1 | 2026-08-08 ✅ | 117 / 4.9k | （无法预览） | 将低阶绚辉太刀替换为终焉星（Omega Planetes）太刀。 |
| [WpSeries 太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3744)<br><sub>WpSeries-LongSword</sub> | V1.0 | 2026-04-13 ✅ | 116 / 5.1k |  | 涵盖所有核心机制与功能的完整太刀模组。 |
| [鸣潮 芙露德莉斯及其剑](https://www.nexusmods.com/monsterhunterwilds/mods/1664)<br><sub>Fleurdelys and her sword (Wuthering Waves)</sub> | 1.0 | 2025-07-07  | 114 / 5.7k |  | 用鸣潮的芙露德莉斯替换女性Lala Barina套装，并用其剑替换希望太刀/大剑，暂无面部表情。 |
| [白之契约（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3877)<br><sub>Virtuous Treaty (Longsword)</sub> | 1.14 | 2026-02-22 ✅ | 114 / 4.8k |  | 将Cosmoloid Edge、铁刀与锐刀替换为尼尔：机械纪元中的白之契约。 |
| [融合超光速刃（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3433)<br><sub>Fusion Tachyon Blade (Long Sword)</sub> | 1.1 | 2026-08-08 ✅ | 112 / 3.7k | （无法预览） | 将千刃龙（Seregios）太刀替换为剑星中的Fusion Tachyon Blade。 |
| [境井武士刀（片手剑 太刀 斩击斧）](https://www.nexusmods.com/monsterhunterwilds/mods/3528)<br><sub>Sakai Katana (Sword and Shield Long Sword Switch Axe )</sub> | 1.1 | 2026-08-08 ✅ | 109 / 6.9k |  | 将太刀、片手剑、斩击斧替换为对马岛之魂中的境井武士刀。 |
| [戈尔玛太刀替代外观](https://www.nexusmods.com/monsterhunterwilds/mods/3681)<br><sub>Alternate Gogma Longsword</sub> | 1.0 | 2026-08-16 ✅ | 108 / 4.0k | （无法预览） | 为戈尔玛镰刀太刀提供替代外观，含带刀鞘与不带刀鞘两个版本。 |
| [村雨替换绚辉太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2506)<br><sub>Murasama over Artian Longsword</sub> | 1.0.5 | 2026-03-19 ✅ | 107 / 3.2k |  | 将1级和5级绚辉太刀替换为合金装备崛起：复仇中的村雨（Murasama）。 |
| [樱潮武士刀（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/2516)<br><sub>Sakuratide Katana (Long sword)</sub> | 1.0 | 2026-08-09 ✅ | 103 / 4.0k | （无法预览） | 将希望太刀替换为樱潮武士刀（Sakuratide Katana）。 |
| [艾尔登法环 黑曜石薄刃（操虫棍和太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3272)<br><sub>Elden Ring_Obsidian Lamina (IG and Long Sword)</sub> | 1.2 | 2026-03-05 ✅ | 102 / 4.2k |  | 将太刀和操虫棍替换为艾尔登法环的黑曜石薄刃（Obsidian Lamina）。 |
| [青龙偃月刀（操虫棍与太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3202)<br><sub>Azure Dragon Crescent Glaive (Insect Glaive and Long Sword)</sub> | 1.1 | 2026-08-08 ✅ | 100 / 4.0k | （无法预览） | 将Doshaguma太刀和希望操虫棍替换为青龙偃月刀。 |
| [太刀 - 武士刀模组](https://www.nexusmods.com/monsterhunterwilds/mods/2958)<br><sub>LongSword - KatanaMod</sub> | 1.0.0 | 2026-02-26 ✅ | 98 / 4.2k |  | 替换飞龙刀（Holly）的外观。 |
| [冰原 公会宫殿太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3106)<br><sub>MHWI_Guild Palace Long Sword</sub> | 2 | 2026-08-07 ✅ | 95 / 3.7k | （无法预览） | 将Quematrice太刀（Lima）替换为公会宫殿太刀。 |
| [剑（双刀与太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3083)<br><sub>Jian Sword (Dual Blades and Long Sword)</sub> | 1.0 | 2026-08-08 ✅ | 94 / 3.5k | （无法预览） | 将护龙蛮颚龙太刀和Doshaguma双刀替换为中国剑。 |
| [卡利亚法师剑 - 太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3458)<br><sub>Carian Spellblade - Long Sword</sub> | 1.0 | 2026-08-07 ✅ | 92 / 4.1k | （无法预览） | 将Zoh Shia太刀替换为艾尔登法环中的卡利亚法师剑（Carian Spellblade）。 |
| [布莱泽的王室大剑（艾尔登法环）](https://www.nexusmods.com/monsterhunterwilds/mods/366)<br><sub>Blaidd's Royal Greatsword (Elden Ring)</sub> | 3.1 | 2025-05-07  | 90 / 4.1k |  | 艾尔登法环中的王室大剑，适用于大剑、太刀和斩击斧。 |
| [艾尔登法环 蕾拉娜之剑（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3242)<br><sub>Elden Ring_Rellana's Blade (Long Sword)</sub> | 1.1 | 2026-08-07 ✅ | 86 / 3.1k | （无法预览） | 将Lala Barina太刀或护龙铠龙太刀替换为蕾拉娜之剑。 |
| [Zeph的阔剑合集（绚辉与希望）](https://www.nexusmods.com/monsterhunterwilds/mods/537)<br><sub>Zeph's Broadsword Collection for Artian and Hope (incompatible)</sub> | 1.2 | 2025-03-19  | 84 / 3.3k |  | 包含4款阔剑，可替换绚辉双刀、片手剑和太刀，以及对应的希望系列武器。 |
| [太刀 - Tenran](https://www.nexusmods.com/monsterhunterwilds/mods/3478)<br><sub>Longsword - Tenran</sub> | 1.0.0 | 2026-02-25 ✅ | 84 / 3.2k |  | 替换Fatecleaver Kimkemush太刀的外观。 |
| [阎魔刀（带特效）](https://www.nexusmods.com/monsterhunterwilds/mods/4899)<br><sub>Yamato - with FX</sub> | 7 | 2026-09-30 ✅ | 83 / 6.9k | （无法预览） | 将太刀、片手剑、双刀替换为鬼泣5中的阎魔刀，并附带特效。 |
| [Rompopolo武士刀（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/2982)<br><sub>Rompopolo Katana (Long Sword)</sub> | 1.1 | 2026-08-09 ✅ | 79 / 2.0k | （无法预览） | Rompopolo太刀的武士刀版本。 |
| [HCL - 龙神（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/4982)<br><sub>HCL - Ryujin (Longsword)</sub> | 1.2 | 2026-09-29 ✅ | 79 / 4.4k | （无法预览） | 原创设计的引擎驱动式太刀。 |
| [Uth Duna太刀替代版](https://www.nexusmods.com/monsterhunterwilds/mods/2949)<br><sub>Uth Duna Long Sword Alt Ver</sub> | 1.1 | 2026-08-09 ✅ | 73 / 2.0k | （无法预览） | Uth Duna太刀的替代外观版本。 |
| [Cosmoloid太刀替代版](https://www.nexusmods.com/monsterhunterwilds/mods/3726)<br><sub>Alternate Cosmoloid Long Sword</sub> | 1.0 | 2026-08-06 ✅ | 72 / 3.6k | （无法预览） | Cosmoloid太刀的替代外观版本。 |
| [煌雷龙绚辉太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1208)<br><sub>Rey dau Artian Long Sword</sub> | 1.1 | 2025-05-14  | 71 / 2.5k |  | 以煌雷龙（Rey Dau）翼刺为素材，更改绚辉太刀的外观。 |
| [Xu Wu太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2941)<br><sub>Xu Wu Long Sword</sub> | 1.1 | 2026-08-09 ✅ | 68 / 1.8k | （无法预览） | 将护龙Doshaguma太刀（Gravecleaver Urkemush）替换为Xu Wu太刀。 |
| [最终幻想14 春之幻影（太刀/大剑）](https://www.nexusmods.com/monsterhunterwilds/mods/1110)<br><sub>FFXIV Figment of Spring  (LS GS)</sub> | 1.4 | 2025-05-29  | 68 / 3.1k |  | 将绚辉太刀替换为最终幻想14中的Figment of Spring。 |
| [只狼「危」字特效（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/1257)<br><sub>Sekiro's (Danger) Perilous Strike VFX for Longsword</sub> | 1.0 | 2025-03-26  | 68 / 2.7k |  | 完美时机的看破斩和居合拔刀气刃斩触发时，显示只狼标志性的红色「危」字特效。 |
| [太刀 - 大蛇](https://www.nexusmods.com/monsterhunterwilds/mods/4077)<br><sub>Longsword - Orochi</sub> | 1.0.0 | 2026-03-04 ✅ | 67 / 3.2k |  | 替换Dosha Gravecleaver太刀的外观。 |
| [星见雅的武士刀「无尾」（多武器，带特效）](https://www.nexusmods.com/monsterhunterwilds/mods/4707)<br><sub>Tailless - Miyabi's Katana (LS GS SA CB SnS DB) with FX</sub> | 5 | 2026-08-14 ✅ | 67 / 4.4k | （无法预览） | 将大剑、太刀、斩击斧、盾斧、片手剑、双刀替换为无尾，附带刀光特效。 |
| [最终幻想7 破坏剑](https://www.nexusmods.com/monsterhunterwilds/mods/530)<br><sub>FFVII Buster Sword</sub> | 1.0 | 2025-03-14  | 67 / 4.1k | （无法预览） | 将希望大剑和希望太刀替换为最终幻想7的破坏剑（最终版）。 |
| [Jin Dahaad太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2924)<br><sub>Jin Dahaad Long Sword</sub> | 1.1 | 2026-08-09 ✅ | 65 / 1.9k | （无法预览） | 将铁刀或影蜘蛛太刀替换为Jin Dahaad太刀。 |
| [破坏剑（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3696)<br><sub>Buster Sword (Longsword)</sub> | 1.22 | 2026-02-18 ✅ | 63 / 2.3k |  | 将Dimensius替换为最终幻想7重制版/重生中的破坏剑。 |
| [艾尔登法环 大太刀（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3213)<br><sub>Elden Ring_Great Katana (Long Sword)</sub> | 1.1 | 2026-08-07 ✅ | 62 / 1.9k | （无法预览） | 将雌火龙太刀替换为艾尔登法环中的大太刀。 |
| [艾尔登法环 月隐（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3185)<br><sub>Elden Ring_Moonveil (Long Sword)</sub> | 1.0 | 2026-08-07 ✅ | 62 / 2.1k | （无法预览） | 将护龙火龙太刀替换为月隐。 |
| [星天鱼 - 骸龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1466)<br><sub>Astral Pisces - Nakarkos Longsword</sub> | 3.1 | 2026-08-09 ✅ | 59 / 2.3k | （无法预览） | 将绚辉太刀替换为经过高清化和重新设计的Astral Pisces。 |
| [High Noon Dusthowler](https://www.nexusmods.com/monsterhunterwilds/mods/3038) | 2.5 | 2026-08-16 ✅ | 59 / 2.1k | （无法预览） | 将Keen Edge太刀替换为SongjoArts设计的High Noon Dusthowler。 |
| [长剑](https://www.nexusmods.com/monsterhunterwilds/mods/2706)<br><sub>Longsword</sub> | 1.1 | 2026-08-09 ✅ | 57 / 1.7k | （无法预览） | 将希望太刀替换为一把真正的长剑。 |
| [Shadowbringer太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3317)<br><sub>Shadowbringer Long Sword</sub> | 1.1 | 2026-08-08 ✅ | 56 / 2.3k | （无法预览） | 将5级绚辉太刀替换为Shadowbringer太刀。 |
| [冰原 Shara Ishvalda太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3218)<br><sub>MHWI_Shara Ishvalda Long Sword</sub> | 1.0 | 2026-08-08 ✅ | 53 / 1.6k | （无法预览） | 将骨系太刀替换为Shara Ishvalda太刀（行云流水·和光）。 |
| [玉龙武士刀（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3547)<br><sub>Jade Dragon Katana (Long Sword)</sub> | 1.0 | 2026-08-08 ✅ | 53 / 1.8k | （无法预览） | 将Quematrice太刀替换为玉龙武士刀（Jade Dragon Katana）。 |
| [沙海龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2942)<br><sub>Balahara Long Sword</sub> | 1.1 | 2026-08-09 ✅ | 52 / 1.5k | （无法预览） | 将护龙火龙太刀（Wyvern Blade Lily）替换为沙海龙太刀。 |
| [大太刀（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3199)<br><sub>Odachi (Long Sword)</sub> | 1.0 | 2026-08-08 ✅ | 51 / 1.7k | （无法预览） | 将Hirabami太刀替换为仁王2中的大太刀。 |
| [源氏龙刃太刀](https://www.nexusmods.com/monsterhunterwilds/mods/827)<br><sub>Genji Dragonblade Longsword</sub> | 1.0 | 2025-03-16  | 50 / 1.5k |  | 将绚辉太刀替换为源氏的龙刃（仅适用于5级绚辉武器）。 |
| [欧米茄太刀 - 最终幻想14](https://www.nexusmods.com/monsterhunterwilds/mods/3580)<br><sub>Omega Longsword - FFXIV</sub> | 2.1 | 2026-08-09 ✅ | 49 / 2.0k | （无法预览） | 将护龙铠龙太刀替换为移植改造自最终幻想14的欧米茄长剑。 |
| [世界 苍星龙之舞（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3207)<br><sub>MHWI_Azure Star Dragon Dance (Long Sword)</sub> | 1.0 | 2026-02-21 ✅ | 47 / 1.1k |  | 将雪狮子太刀替换为怪物猎人世界中的Azure Star Dragon Dance。 |
| [最终幻想14 Avatar之镰](https://www.nexusmods.com/monsterhunterwilds/mods/2389)<br><sub>FFXIV Avatar's Scythe</sub> | 1.0 | 2025-06-30  | 46 / 1.9k |  | 将绚辉太刀替换为最终幻想14中的Avatar's Scythe。 |
| [略微纤细的海龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2795)<br><sub>Slightly Slimmer Lagiacrus Long Sword</sub> | 1.0.0 | 2026-02-25 ✅ | 38 / 949 |  | 让海龙太刀的外形略微变细。 |
| [天上天下天地无双刀（抢先版）](https://www.nexusmods.com/monsterhunterwilds/mods/1328)<br><sub>Hellish Slasher Early Access</sub> | 1.0.0 | 2025-03-27  | 37 / 1.5k |  | 将绚辉太刀替换为天上天下天地无双刀（Hellish Slasher）。 |
| [露帕（鸣潮）](https://www.nexusmods.com/monsterhunterwilds/mods/2733)<br><sub>Lupa (Wuthering Waves)</sub> | 1.1.1 | 2026-05-29 ✅ | 37 / 1.5k |  | 将女性沙海龙防具替换为鸣潮的露帕，并将希望太刀/操虫棍替换为她的长枪，暂无面部表情。 |
| [Wild Hunter阔剑](https://www.nexusmods.com/monsterhunterwilds/mods/3775)<br><sub>Wild Hunter Claymore</sub> | 1.0 | 2026-08-16 ✅ | 36 / 1.6k | （无法预览） | 外观更朴素写实的大剑/太刀武器，替换希望系列武器，太刀和大剑均可用。 |
| [艾尔登法环 十字薙刀](https://www.nexusmods.com/monsterhunterwilds/mods/4410)<br><sub>Elden Ring_Cross-Naginata</sub> | 2 | 2026-08-07 ✅ | 31 / 1.0k | （无法预览） | 将太刀、操虫棍、长枪替换为十字薙刀。 |
| [太刀模组 新Stahlfakt](https://www.nexusmods.com/monsterhunterwilds/mods/4034)<br><sub>LongswordMod_New_Stahlfakt</sub> | 1.0.0 | 2026-02-25 ✅ | 30 / 937 |  | 替换Stahlfakt太刀的外观。 |
| [誓约胜利之剑太刀 - Fate/stay night](https://www.nexusmods.com/monsterhunterwilds/mods/2158)<br><sub>Excalibur Longsword - Fate Stay Night (Saber - Artoria Pendragon)</sub> | 1.04 | 2025-04-27  | 29 / 1.1k |  | 将Keen Edge替换为Fate/stay night中Saber（阿尔托莉雅）的誓约胜利之剑。 |
| [艾尔登法环 双手大剑（斩击斧与太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3248)<br><sub>Elden Ring_Zweihander (Switch Axe and Long Sword)</sub> | 1.0 | 2026-08-07 ✅ | 29 / 1.3k | （无法预览） | 将太刀和斩击斧替换为双手大剑（Zweihander）。 |
| [只狼 不死斩（无特效）](https://www.nexusmods.com/monsterhunterwilds/mods/1857)<br><sub>Sekiro Shadows Die Twice Mortal Blade(No special effects)</sub> | v1.0 | 2025-04-14  | 28 / 902 |  | 将飞龙刀「血」太刀替换为只狼中的不死斩。 |
| [鸣潮 千咲（盾斧/太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3486)<br><sub>WutheringWaves Chisa(CB LS)1.042</sub> | 1.0 | 2026-08-20 ✅ | 27 / 3.3k | （无法预览） | 替换Blossom防具为鸣潮的千咲，支持骨骼系统。 |
| [樱花太刀](https://www.nexusmods.com/monsterhunterwilds/mods/4825)<br><sub>Sakura Longsword</sub> | 1 | 2026-09-15 ✅ | 26 / 3.0k | （无法预览） | 替换Lala Barina太刀的外观。 |
| [老山龙太刀（来自MHO）](https://www.nexusmods.com/monsterhunterwilds/mods/657)<br><sub>Lao-Shan Long Sword from MHO</sub> | 1 | 2026-02-22 ✅ | 25 / 620 |  | 将铁刀替换为怪物猎人Online中的老山龙太刀。 |
| [太刀狂暴加速](https://www.nexusmods.com/monsterhunterwilds/mods/2374)<br><sub>GO NUTS WITH LONG SWORD</sub> | v.01 | 2025-05-11  | 25 / 931 |  | 为太刀提供攻击速度倍率调整。 |
| [蓝龙剑](https://www.nexusmods.com/monsterhunterwilds/mods/894)<br><sub>Blue Dragon Sword</sub> | 1 | 2025-03-18  | 24 / 875 |  | 将骨系太刀派生的模型替换为蓝龙剑。 |
| [冥界武士刀](https://www.nexusmods.com/monsterhunterwilds/mods/2767)<br><sub>Nether Katana</sub> | 2.1 | 2026-08-09 ✅ | 23 / 800 | （无法预览） | 将骨系太刀替换为深渊海龙太刀（Abyssal Lagiacrus）。 |
| [最终幻想7 合体剑](https://www.nexusmods.com/monsterhunterwilds/mods/2385)<br><sub>final fantasy 7 fusion sword</sub> | 1.0 | 2025-05-14  | 21 / 953 |  | 将绚辉太刀替换为最终幻想7的合体剑，新增大剑和斩击斧版本。 |
| [EMV姿势 - 男性猎人包](https://www.nexusmods.com/monsterhunterwilds/mods/2748)<br><sub>EMV Pose - Male Hunter Pack</sub> | 1.0 | 2025-06-20  | 19 / 462 |  | 为男性猎人提供3个EMV姿势，姿势1适合太刀等武器，可用滑块调整，不改变面部。 |
| [先锋之刃](https://www.nexusmods.com/monsterhunterwilds/mods/4320)<br><sub>Vanguard Blade</sub> | 1.3 | 2026-08-16 ✅ | 19 / 1.1k | （无法预览） | 为公会资深猎人打造的刀刃，提供大剑和太刀版本。 |
| [霸龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2418)<br><sub>Akantor Longsword</sub> | 2.3 | 2026-08-09 ✅ | 17 / 569 | （无法预览） | 将黑蚀龙太刀替换为霸龙太刀。 |
| [太刀外观的大剑](https://www.nexusmods.com/monsterhunterwilds/mods/2415)<br><sub>Great Sword with Long Sword Look</sub> | 1.1 | 2026-02-23 ✅ | 16 / 475 |  | 将五把不同大剑的外观替换为太刀模型。 |
| [可琳的链锯（盾斧/太刀/斩击斧）- 绝区零](https://www.nexusmods.com/monsterhunterwilds/mods/4808)<br><sub>Corin's Chainsaw (Charge Blade - Long Sword - Switch Axe) - ZZZ</sub> | 3 | 2026-09-02 ✅ | 16 / 1.2k | （无法预览） | 将绚辉盾斧、太刀、斩击斧替换为可琳的链锯。 |
| [鬼泣5 绯红女皇 绚辉太刀（原型）](https://www.nexusmods.com/monsterhunterwilds/mods/3235)<br><sub>DMC5 Red Queen Artian LS (Proto)</sub> | 1.0 | 2025-09-13  | 15 / 672 |  | 将绚辉太刀（原型）替换为鬼泣5中尼禄的绯红女皇。 |
| [浮空龙太刀 - 重制版](https://www.nexusmods.com/monsterhunterwilds/mods/3946)<br><sub>Namielle Long Sword - RE-Edits -</sub> | RE1.0.01 | 2026-02-21 ✅ | 15 / 430 | `it0300_0003_m` | 从怪物猎人世界移植的浮空龙（Namielle）太刀。 |
| [护龙铠龙大剑替换为铠龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1554)<br><sub>Replace GS - G. Veldian Gladius with LS - Righteous Lancelot</sub> | 1 | 2025-04-04  | 14 / 569 |  | 将大剑G. Veldian Gladius替换为太刀Righteous Lancelot。 |
| [村正替换两种绚辉太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2144)<br><sub>Muramasa over Both Artian Long Swords</sub> | 2.0 | 2026-10-02 ✅ | 14 / 397 | （无法预览） | 将两种绚辉太刀的外观替换为村正。 |
| [铠龙双刀替换为铠龙太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1527)<br><sub>Replace Arkveld DB with Arkveld LS</sub> | 1 | 2025-04-03  | 13 / 311 |  | 将双刀G. Inspired Ywain替换为太刀Righteous Lancelot。 |
| [Lala Barina太刀 盾斧版](https://www.nexusmods.com/monsterhunterwilds/mods/671)<br><sub>LS Lala Barina CB vers.</sub> | v1 | 2025-03-13  | 13 / 428 |  | 将Lala Barina太刀及其武士刀替换为Lala Barina盾斧的剑。 |
| [Ikemen盾斧 - 太刀外观](https://www.nexusmods.com/monsterhunterwilds/mods/3245)<br><sub>Ikemen Charge Blade - Longsword Look</sub> | 1.3 | 2026-08-20 ✅ | 12 / 1.3k | （无法预览） | Ikemen系列：19把盾斧变为对应的太刀外观，并隐藏盾牌。 |
| [正宗](https://www.nexusmods.com/monsterhunterwilds/mods/3399)<br><sub>Masamune</sub> | 1.0 | 2026-10-02 ✅ | 12 / 318 | （无法预览） | 单翼天使的正宗刀，替换海龙太刀。 |
| [Shatterseal太刀](https://www.nexusmods.com/monsterhunterwilds/mods/4563)<br><sub>Shatterseal Long Sword</sub> | 1 | 2026-08-07 ✅ | 12 / 922 | （无法预览） | 将鹤嘴锄（太刀）替换为Shatterseal太刀。 |
| [煌雷龙随从武器替换铁刀太刀](https://www.nexusmods.com/monsterhunterwilds/mods/523)<br><sub>Palico Weapon Rey Dau Over Iron Katana LS</sub> | v1 | 2025-03-10  | 12 / 407 |  | 将煌雷龙随从艾露猫武器变为太刀。 |
| [镰刀与太刀](https://www.nexusmods.com/monsterhunterwilds/mods/1909)<br><sub>Sickle and Long Sword</sub> | v1.0 | 2025-05-11  | 11 / 939 |  | 将飞龙刀「灰」替换为镰刀。 |
| [隐形刀鞘完全版 - 太刀](https://www.nexusmods.com/monsterhunterwilds/mods/2803)<br><sub>Invisible Sheaths Complete Edition - Long Swords</sub> | 1.0 | 2025-07-03  | 11 / 388 |  | 让（几乎）所有太刀刀鞘隐形。 |
| [Slipstream军刀（太刀）](https://www.nexusmods.com/monsterhunterwilds/mods/3774)<br><sub>Slipstream Saber (Longsword)</sub> | 1.22 | 2026-02-18 ✅ | 11 / 414 |  | 将Cosmoloid太刀替换为最终幻想7重生中的Slipstream Saber。 |
| [Lala Barina太刀隐形刀鞘](https://www.nexusmods.com/monsterhunterwilds/mods/2792)<br><sub>Lala Barina Longsword Invisible Sheath</sub> | 1.0 | 2025-07-03  | 10 / 168 |  | 让Lala Barina太刀的刀鞘隐形。 |
| [缩小太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3672)<br><sub>Smaller Long Swords</sub> | 1.0 | 2026-02-09 ✅ | 9 / 557 |  | 将太刀尺寸缩小15%。 |
| [太刀 Ramlethal](https://www.nexusmods.com/monsterhunterwilds/mods/4309)<br><sub>LS Ramlethal</sub> | 1 | 2026-04-19 ✅ | 7 / 293 |  | 将黑蚀龙太刀替换为Ramlethal的剑。 |
| [雨果的镰刀太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3336)<br><sub>Hugo's Scythe Longsword</sub> | 2.1 | 2026-08-09 ✅ | 5 / 304 | （无法预览） | 将Zoh Shia太刀替换为绝区零中雨果的镰刀。 |
| [Ikemen武器姿势 - 太刀套组01](https://www.nexusmods.com/monsterhunterwilds/mods/3415)<br><sub>Ikemen Weapon Poses - Longsword Set 01</sub> | 1 | 2026-03-08 ✅ | 5 / 282 |  | Ikemen系列实验作品，包含三把太刀武器和三个适配EMV Engine的玩家姿势。 |
| [雪狮子武器合集](https://www.nexusmods.com/monsterhunterwilds/mods/5068)<br><sub>Blango Weapon Collection</sub> | 1 | 2026-10-06 ✅ | 5 / 217 | （无法预览） | 将太刀、斩击斧、大剑、长枪替换为雪狮子武器。 |
| [镐化太刀](https://www.nexusmods.com/monsterhunterwilds/mods/3341)<br><sub>Pickedaxe</sub> | 1.0.1 | 2026-02-19 ✅ | 4 / 190 |  | 仿佛某个太刀使用者想用刀去挖矿，替换骨系大锤（Bone Bludgeon）。 |
| [玛莲妮亚之手 - 太刀](https://www.nexusmods.com/monsterhunterwilds/mods/4524)<br><sub>Hand Of Malenia - Long Sword</sub> | 1 | 2026-06-11 ✅ | 4 / 196 |  | 将Rompopolo太刀（Rompo Hacker）替换为艾尔登法环中的玛莲妮亚之手。 |
| [Death Stench随从武器太刀](https://www.nexusmods.com/monsterhunterwilds/mods/614)<br><sub>LS Death Stench Palico</sub> | v1 | 2025-03-12  | 3 / 115 |  | 将Death Stench随从艾露猫武器变为太刀，替换骨刀。 |
| [鬼泣5 叛逆之刃太刀](https://www.nexusmods.com/monsterhunterwilds/mods/4880)<br><sub>DMC 5 - Rebellion Long Sword</sub> | 1 | 2026-09-14 ✅ | 2 / 246 | （无法预览） | 将鬼泣5的叛逆之刃移植为太刀，替换绚辉太刀（原型），其他绚辉版本可能有贴图问题。 |
| [双雪狮子王太刀双刀](https://www.nexusmods.com/monsterhunterwilds/mods/519)<br><sub>DB Double LS Blangonga Over Bone DB</sub> | 1 | 2025-03-10  | 1 / 147 |  | 将骨系双刀替换为两把雪狮子王太刀。 |
| [噬血代码 刺客之镰太刀](https://www.nexusmods.com/monsterhunterwilds/mods/5032)<br><sub>Code Vein Assassin's Sickle Longsword</sub> | 1 | 2026-10-04 ✅ | 0 / 39 | （无法预览） | 将入侵处刑人的武器刺客之镰替换到太刀上。 |
| [Lala Barina太刀无刀鞘](https://www.nexusmods.com/monsterhunterwilds/mods/5110)<br><sub>No Sheath for Lala Barina LS</sub> | 1 | 2026-10-11 ✅ | 0 / 13 | （无法预览） | 移除Lala Barina太刀的刀鞘。 |
| [Lala Ornithocton太刀无刀鞘](https://www.nexusmods.com/monsterhunterwilds/mods/5111)<br><sub>No Sheath for Lala Ornithocton LS</sub> | 1 | 2026-10-11 ✅ | 0 / 16 | （无法预览） | 移除Lala Ornithocton太刀的刀鞘。 |
| [骨太刀](https://www.nexusmods.com/monsterhunterwilds/mods/4101)<br><sub>Bone Long Sword</sub> | 1.0.0 | 2026-03-14 ✅ | 0 / 60 |  | 将希望太刀的外观替换为经典的骨系太刀。 |

<a id="e"></a>
## E. 角色 / 猎人 / 随从 / NPC 语音（35）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [可能是你听过最迷人的语音模组](https://www.nexusmods.com/monsterhunterwilds/mods/1060)<br><sub>This might be the most captivating voice mod you've ever heard.</sub> | 1.0 | 2025-03-21  | 196 / 5.8k | `player_actvoice_f03` | 将崛起：曙光中歌姬NPC Leaparis的声音移植到荒野，主要替换日语第六号语音。 |
| [尼尔：自动人形 2B角色语音模组](https://www.nexusmods.com/monsterhunterwilds/mods/1457)<br><sub>MHWS NieR Automata YoRHa No 2 Type B (2B) Character Voice Mod</sub> | 1.0 | 2025-03-31  | 186 / 6.8k | `player_actvoice_f03` | 将尼尔：自动人形中2B的语音移植到怪物猎人荒野。 |
| [娜塔闭嘴](https://www.nexusmods.com/monsterhunterwilds/mods/1045)<br><sub>Shut Up Nata</sub> | 1.0 | 2025-03-29  | 179 / 5.4k | `npc101_00_004_m` | 根据版本移除娜塔部分烦人的台词或完全禁用其全部语音（仅限英语语音）。 |
| [AI女声替换娜塔](https://www.nexusmods.com/monsterhunterwilds/mods/1772)<br><sub>AI female voices replacing Nata</sub> | v1.0 | 2025-04-11  | 111 / 3.2k | `npc101_00_004_m` | 用AI生成的女声替换娜塔的全部语音（含过场动画和营地）。 |
| [艾尔玛闭嘴](https://www.nexusmods.com/monsterhunterwilds/mods/1202)<br><sub>Shut Up Alma</sub> | 1.0 | 2025-04-05  | 104 / 2.8k |  | 根据版本移除艾尔玛部分烦人的台词或完全禁用其全部语音。 |
| [蔚蓝档案 鬼方佳代子语音替换娜塔](https://www.nexusmods.com/monsterhunterwilds/mods/1697)<br><sub>Blue Archive-Onikata Kayoko's voice replacing Nata</sub> | 1.0 | 2025-04-18  | 103 / 4.2k | `npc101_00_004_m` | 用GPT-SoVITS生成的佳代子语音替换娜塔的营地语音。 |
| [队伍晕倒Fah音效](https://www.nexusmods.com/monsterhunterwilds/mods/4030)<br><sub>Fah faint sfx chat team</sub> | 1.01 | 2026-02-26 ✅ | 101 / 5.7k | `player_chatactionvoice_f01`<br>`player_chatactionvoice_f01`<br>`player_chatactionvoice_f02`<br>`player_chatactionvoice_f02` … | 在任务中你或队友晕倒时更换角色音效。 |
| [先祖艾露猫](https://www.nexusmods.com/monsterhunterwilds/mods/233)<br><sub>Ancestor Palico</sub> | 1.1 | 2025-03-07  | 53 / 1.5k | `ot_dia_type01_m`<br>`ot_dia_type02_m` | 将大部分随从艾露猫的喊话替换为暗黑地牢1/2中先祖和学者的台词。 |
| [杰玛闭嘴](https://www.nexusmods.com/monsterhunterwilds/mods/1286)<br><sub>Shut Up Gemma</sub> | 1.0 | 2025-03-26  | 50 / 1.0k |  | 根据版本移除杰玛部分烦人的台词或完全禁用其全部语音。 |
| [猎天使魔女 贝优妮塔语音模组](https://www.nexusmods.com/monsterhunterwilds/mods/2369)<br><sub>MHWilds - Bayonetta Voice Mod</sub> | 2.0 | 2025-05-10  | 44 / 1.1k | `player_actvoice_f03`<br>`player_chatactionvoice_f03` | 将女性角色语音3（即第6号语音）替换为猎天使魔女系列中贝优妮塔的声音。 |
| [静音部分台词](https://www.nexusmods.com/monsterhunterwilds/mods/1755)<br><sub>Mute Some Lines</sub> | 1.1.1 | 2025-04-20  | 43 / 858 |  | 在播放烦人台词时自动静音，或静音指定NPC/音效，配置简便，可将最近台词加入触发列表。 |
| [哲学♂盾斧](https://www.nexusmods.com/monsterhunterwilds/mods/1002)<br><sub>Gachi Charge Blade</sub> | 2.0 | 2025-03-30  | 42 / 1.6k | `hit_weapon_cmn`<br>`human_common_effect`<br>`player_actvoice_f01`<br>`player_actvoice_f02` … | 为盾斧攻击加入强有力♂的音效。 |
| [姬塔语音替换](https://www.nexusmods.com/monsterhunterwilds/mods/1521)<br><sub>Djeeta's Actvoice replacement</sub> | 1.0 | 2025-04-06  | 39 / 1.8k | `player_actvoice_f03` | 将玩家6号语音替换为碧蓝幻想Relink中姬塔的声音。 |
| [初音未来语音替换](https://www.nexusmods.com/monsterhunterwilds/mods/711)<br><sub>Hatsune Miku Voice Replacement</sub> | 1.0 | 2025-03-14  | 36 / 1.6k | `event_dia_player_f03_1st_m`<br>`event_dia_player_f03_m`<br>`player_actvoice_f03`<br>`player_chatactionvoice_f03` … | 用初音未来的各种语音片段替换猎人语音。 |
| [娜塔变声](https://www.nexusmods.com/monsterhunterwilds/mods/3493)<br><sub>Nata Voice Change</sub> | 1.04 | 2025-12-22 ✅ | 34 / 1.4k | `npc101_00_004_02_00_m`<br>`npc101_00_004_02_00_m`<br>`npc101_00_004_02_00_m`<br>`npc101_00_004_m` … | 将娜塔的声音改为女孩声音，支持英语、中文和日语。 |
| [惠惠盾斧](https://www.nexusmods.com/monsterhunterwilds/mods/2329)<br><sub>Megumin Charge Blade</sub> | 1.0 | 2025-05-09  | 32 / 2.3k | `player_actvoice_f01`<br>`player_actvoice_f02`<br>`player_actvoice_f03`<br>`player_actvoice_m01` … | 为盾斧加入惠惠的「Explosion！」语音。 |
| [AI空崎日奈语音](https://www.nexusmods.com/monsterhunterwilds/mods/1414)<br><sub>AI HINA VOICE</sub> | 1.0 | 2025-03-30  | 32 / 1.7k | `event_dia_player_f03_1st_m`<br>`event_dia_player_f03_m`<br>`event_dia_player_f03_m`<br>`pl_dia_f03_1st_m` … | 用AI生成的空崎日奈语音替换06号语音（女性03）。 |
| [大剑与至暗之夜的誓约胜利之剑语音](https://www.nexusmods.com/monsterhunterwilds/mods/4040)<br><sub>EXCALIBUR Voice for Great Sword and The Blackest Night</sub> | 1.2 | 2026-06-02 ✅ | 21 / 2.0k | `player_foley_clb_gesture_03_00`<br>`wp00_cmn_m` | 为大剑真蓄力斩和至暗之夜（The Blackest Night）加入Saber或Alter的「Excalibur！」语音。 |
| [BBTAG 布蕾克战斗语音（日语）](https://www.nexusmods.com/monsterhunterwilds/mods/3527)<br><sub>Character battle voice Blaze Belladonna from BBTAG (JP)</sub> | 1 | 2025-11-11  | 18 / 588 | `player_actvoice_f03` | 将女性3号的日语战斗语音替换为BBTAG中布蕾克·贝拉多娜的声音（仅战斗语音）。 |
| [惠惠爆裂魔法与炭治郎「别跑胆小鬼」语音](https://www.nexusmods.com/monsterhunterwilds/mods/3746)<br><sub>Megumin EXPLOSION and Tanjiro DON'T RUN YOU COWARD Voice</sub> | 2.1 | 2026-03-23 ✅ | 17 / 1.2k | `gm200_000_00`<br>`gm200_000_02`<br>`gm200_000_06`<br>`gm200_000_07` … | 为大桶爆弹加入惠惠语音，并将诱导弹的定型文替换为炭治郎的台词。 |
| [绚辉狩猎笛初音未来](https://www.nexusmods.com/monsterhunterwilds/mods/1272)<br><sub>Hatsune Miku on artian horn</sub> | 1.0 | 2025-03-26  | 13 / 444 | `it0500_0014_m` | 更改Omiltika LV5的音效，语音取自MGSPW中的日语AI武器语音。 |
| [队友晕倒时播放Happy Wheels胜利音效](https://www.nexusmods.com/monsterhunterwilds/mods/3931)<br><sub>Happy Wheels VICTORY Jingle When Teammates Faint</sub> | 1.0 | 2026-02-22 ✅ | 11 / 316 | `player_chatactionvoice_f01`<br>`player_chatactionvoice_f01`<br>`player_chatactionvoice_f02`<br>`player_chatactionvoice_f02` … | 队友晕倒/猫车时播放Happy Wheels的VICTORY音效。 |
| [黑神话：悟空 寅虎大剑音效（中文）](https://www.nexusmods.com/monsterhunterwilds/mods/1035)<br><sub>Black Myth Wukong Yin Tiger GS sound(chinese)</sub> | 1.0 | 2025-03-21  | 9 / 239 | `hit_hm_cmn`<br>`player_actvoice_f03`<br>`wp00_cmn_m` | 用黑神话：悟空中寅虎的音效替换大剑音效。 |
| [为民主而战的艾露猫 - 绝地潜兵2语音](https://www.nexusmods.com/monsterhunterwilds/mods/3904)<br><sub>Palicos for Democracy - Helldiver 2 Voicelines for Palico Companion</sub> | 1.0 | 2026-02-06 ✅ | 6 / 325 | `ot_dia_type02_m` | 将随从艾露猫大部分战斗及野外语音替换为绝地潜兵2角色的俏皮话和喊话。 |
| [鸣潮日语战斗语音（弗洛洛/千咲/Mornye）](https://www.nexusmods.com/monsterhunterwilds/mods/4716)<br><sub>Wuthering Waves JP combat voice mod(Phrolova Chisa Mornye)</sub> | 1.3 | 2026-08-16 ✅ | 5 / 820 | （无法预览） | 将日语女性6号战斗语音替换为弗洛洛、千咲和Mornye的语音。 |
| [蔚蓝档案 星野语音模组](https://www.nexusmods.com/monsterhunterwilds/mods/4679)<br><sub>Blue Archive Hosino Voice mod</sub> | 1 | 2026-09-14 ✅ | 5 / 441 | （无法预览） | 将6号语音（日语）替换为小鸟游星野。 |
| [军团要塞2 医生语音（男性1号）](https://www.nexusmods.com/monsterhunterwilds/mods/1099)<br><sub>Team Fortress 2 Medic for Male voice 1</sub> | 1 | 2025-03-22  | 4 / 130 | `player_actvoice_m01` | 将英语男性猎人1号语音替换为军团要塞2中医生的声音。 |
| [最终幻想7 爱丽丝语音](https://www.nexusmods.com/monsterhunterwilds/mods/4914)<br><sub>Final Fantasy VII Aerith Voice</sub> | 1 | 2026-09-19 ✅ | 4 / 416 | （无法预览） | 将女性角色日语6号语音替换为最终幻想7中爱丽丝的声音。 |
| [Mumble插件（位置语音聊天）](https://www.nexusmods.com/monsterhunterwilds/mods/1020)<br><sub>MHWI Mumble Plugin (Positional Voice Chat)</sub> | v1.0.2 | 2025-03-20  | 3 / 64 |  | 为好友之间启用基于位置的语音聊天。 |
| [雪花菈米铳枪音效](https://www.nexusmods.com/monsterhunterwilds/mods/1352)<br><sub>Yuki Noa Gun Lance sound effect</sub> | 1.0 | 2025-03-28  | 3 / 201 | `player_common_foley`<br>`weapon_cmn`<br>`wp07_cmn_m`<br>`wp07_shell` | 替换铳枪的奇袭和角力音效。 |
| [灾厄启示录 力巴尔角色语音模组](https://www.nexusmods.com/monsterhunterwilds/mods/1474)<br><sub>MHWS Age Of Calamity Revali Character Voice Mod</sub> | 1.0 | 2025-04-01  | 3 / 67 | `player_actvoice_m03` | 将塞尔达无双：灾厄启示录中力巴尔的奇特叫声和语音移植到荒野。 |
| [被压制与异常时喊「I'M IN DANGER」](https://www.nexusmods.com/monsterhunterwilds/mods/3875)<br><sub>I'M IN DANGER for Pinned and Impaired Shoutouts</sub> | 1.0 | 2026-02-22 ✅ | 3 / 280 | `player_chatactionvoice_f01`<br>`player_chatactionvoice_f01`<br>`player_chatactionvoice_f02`<br>`player_chatactionvoice_f02` … | 将被压制和异常状态的喊话替换为Ralph的「Haha, I'm in danger!」。 |
| [成田大进语音替换操虫棍](https://www.nexusmods.com/monsterhunterwilds/mods/1285)<br><sub>Narita Taishin replace Insect glaive sound</sub> | 1.0.0 | 2025-03-26  | 2 / 197 | `human_common_effect`<br>`player_actvoice_f03`<br>`wp10_cmn_m` | 用赛马娘成田大进的语音替换操虫棍相关的部分语音，适用于6号角色语音。 |
| [升龙拳手势改为超级马里奥跳跃音效](https://www.nexusmods.com/monsterhunterwilds/mods/3882)<br><sub>Super Mario Jump SFX for Shoryuken Gesture</sub> | 2.0 | 2026-03-18 ✅ | 2 / 64 | `player_actvoice_clb_gesture`<br>`player_actvoice_clb_gesture`<br>`player_actvoice_clb_gesture`<br>`player_actvoice_clb_gesture` … | 将升龙拳手势语音替换为超级马里奥的跳跃音效。 |
| [绝地潜兵2 重弩（重制）](https://www.nexusmods.com/monsterhunterwilds/mods/3358)<br><sub>HelldiverII heavy bowgun(remake)</sub> | 1.0 | 2025-10-08  | 0 / 12 |  | 将重弩的众多音效替换为绝地潜兵2男性潜兵1号的语音，并加入多种该作武器音效。 |

<a id="f"></a>
## F. BGM / 音乐（72）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [铠龙BGM替换为护龙铠龙二阶段](https://www.nexusmods.com/monsterhunterwilds/mods/940)<br><sub>Replace Arkveld BGM with Guardian Arkveld Phase 2</sub> | 1.5 | 2026-02-20 ✅ | 82 / 4.5k | `bgm_resident_ev`<br>`bgm_resident_m` | 将铠龙的BGM替换为护龙铠龙第二阶段使用的曲目。 |
| [主菜单BGM - 英雄的证明](https://www.nexusmods.com/monsterhunterwilds/mods/135)<br><sub>Main Menu BGM Music - Proof of a Hero</sub> | 1.0 | 2025-03-01  | 76 / 3.1k | `fate` | 在启动画面猎人走出帐篷时播放英雄的证明。 |
| [泡狐龙BGM 崛起版](https://www.nexusmods.com/monsterhunterwilds/mods/1674)<br><sub>Mizutsune BGM Rise.ver</sub> | 1.0 | 2025-04-10  | 74 / 2.2k | `bgm_01_00_m` | 将泡狐龙BGM替换为崛起版本。 |
| [MH3任务完成曲替换](https://www.nexusmods.com/monsterhunterwilds/mods/846)<br><sub>MH3 Quest Complete Replacement Theme</sub> | 1.22 | 2025-03-23  | 74 / 2.4k | `bgm_resident_1st_m`<br>`bgm_resident_1st_m` | 将任务完成曲替换为怪物猎人3/3G的胜利曲。 |
| [任务完成曲合集](https://www.nexusmods.com/monsterhunterwilds/mods/875)<br><sub>Quest Clear Compliation</sub> | 1.0 | 2026-02-27 ✅ | 52 / 2.6k |  | 替换任务完成曲（不含3代版本）。 |
| [GTA圣安地列斯任务完成曲](https://www.nexusmods.com/monsterhunterwilds/mods/1357)<br><sub>GTASA replace the quest complete theme</sub> | 1.0.0 | 2025-03-28  | 50 / 3.1k | `bgm_resident_1st_m` | 用GTA圣安地列斯的任务完成小曲替换任务完成曲。 |
| [进击的巨人双刀BGM](https://www.nexusmods.com/monsterhunterwilds/mods/2442)<br><sub>Attack on Titan Bgm for Dual Blades</sub> | 1.1 | 2025-05-19  | 42 / 1.6k | `wp02_cmn_m` | 为双刀加入进击的巨人原声音乐。 |
| [StateMusic - 自定义所有主题曲与BGM](https://www.nexusmods.com/monsterhunterwilds/mods/4628)<br><sub>StateMusic - Change all the theme and BGM as you want</sub> | 1 | 2026-10-02 ✅ | 42 / 2.6k | （无法预览） | 根据区域、战斗状态、怪物等条件播放你选择的mp3音乐。 |
| [荒野任务完成曲替换合集（精简版）](https://www.nexusmods.com/monsterhunterwilds/mods/1197)<br><sub>MHWs Quest Clear Theme Replacement Compilation (lite ver)</sub> | 1.0 | 2025-03-26  | 40 / 2.0k | `bgm_resident_1st_m` | 将荒野的任务结算音乐替换为其他曲目的合集，持续更新。 |
| [煌雷龙合成波主题曲替换](https://www.nexusmods.com/monsterhunterwilds/mods/3560)<br><sub>Earth-Piercing Bolt - Rey Dau Synthwave Theme replacement (from CthulhuSeeker feat Moonlapse)</sub> | 1.1 | 2025-12-29 ✅ | 36 / 1.3k | `bgm_resident_ev`<br>`bgm_resident_m` | 将煌雷龙的主题曲替换为CthulhuSeeker编曲的合成波（Synthwave）版本。 |
| [女神异闻录5胜利曲替换任务完成曲](https://www.nexusmods.com/monsterhunterwilds/mods/1159)<br><sub>Persona 5 victory theme replace the quest complete theme</sub> | 1.0.0 | 2025-03-26  | 30 / 1.3k | `bgm_resident_1st_m` | 用女神异闻录5的胜利小曲替换任务完成曲。 |
| [荒野营地BGM替换为冰原赛利纳BGM](https://www.nexusmods.com/monsterhunterwilds/mods/1162)<br><sub>Wilds Base Camp BGM Replaced with Iceborne Base Camp BGM</sub> | 1.0 | 2025-03-23  | 29 / 887 | `bgm_resident_1st_m` | 将冰原赛利纳据点的BGM移植到荒野，替换五个主要据点的白天背景音乐。 |
| [莫加村营地主题曲替换](https://www.nexusmods.com/monsterhunterwilds/mods/1029)<br><sub>Moga Village Camp Theme Replacement</sub> | 1.0 | 2025-03-21  | 28 / 807 | `bgm_resident_1st_m`<br>`bgm_resident_1st_m` | 将营地昼夜主题曲替换为怪物猎人3中莫加村的昼夜主题曲。 |
| [女神异闻录5 BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/1494)<br><sub>BGM Replacement P5 Theme</sub> | 1.0.0 | 2025-04-02  | 27 / 868 | `bgm_jukebox_1st_m`<br>`bgm_resident_1st_m` | 将大本营昼夜、帐篷和结算音乐替换为女神异闻录5的BGM。 |
| [泡狐龙BGM XX版](https://www.nexusmods.com/monsterhunterwilds/mods/1705)<br><sub>Mizutsune BGM X(GU).ver</sub> | 1.0 | 2025-04-08  | 26 / 927 | `bgm_01_00_m` | 将泡狐龙BGM替换为XX版本。 |
| [普通铠龙使用护龙铠龙主题曲](https://www.nexusmods.com/monsterhunterwilds/mods/3325)<br><sub>Guardian Arkveld Theme for regular Arkveld</sub> | 1.1 | 2025-10-04  | 23 / 780 |  | 将铠龙的主题曲替换为护龙铠龙的版本，通过修改游戏内引用实现，文件极小。 |
| [崛起泡狐龙BGM（无崩溃版）](https://www.nexusmods.com/monsterhunterwilds/mods/3803)<br><sub>MHRise Mizutsune BGM (No Diva Crash)</sub> | 1.0 | 2026-02-20 ✅ | 23 / 798 | `bgm_01_00_m`<br>`bgm_resident_ev` | 将泡狐龙BGM（常规与追逐）替换为崛起版本，无崩溃且循环配置正确。 |
| [女神异闻录5 Beneath The Mask替换集会所BGM](https://www.nexusmods.com/monsterhunterwilds/mods/1763)<br><sub>Persona 5-Beneath The Mask replacing The Gathering Hub BGM</sub> | 1.0 | 2025-04-11  | 22 / 984 | `bgm_01_00_m`<br>`bgm_resident_ev` | 将集会所的BGM替换为女神异闻录5的Beneath The Mask。 |
| [更换终焉星主题曲](https://www.nexusmods.com/monsterhunterwilds/mods/3340)<br><sub>Change Theme of Omega</sub> | 1.04.01 | 2026-02-20 ✅ | 22 / 928 | `bgm_03_00_m`<br>`bgm_jukebox_clb_m_03_00`<br>`bgm_jukebox_ev`<br>`bgm_resident_ev` | 更换终焉星（Omega Planetes）极难战斗曲，并同时更换帐篷点唱机BGM。 |
| [晕倒时播放黑暗之魂YOU DIED音效](https://www.nexusmods.com/monsterhunterwilds/mods/3995)<br><sub>Dark Souls YOU DIED Sound When Fainting</sub> | 1 | 2026-02-21 ✅ | 21 / 669 | `bgm_resident_1st_m` | 将晕倒时的鼓声音效替换为黑暗之魂的死亡音效。 |
| [猎天使魔女章节通关曲合集](https://www.nexusmods.com/monsterhunterwilds/mods/1765)<br><sub>Bayonetta Chapter Clear Collection</sub> | 1 | 2025-04-11  | 20 / 540 | `bgm_resident_1st_m` | 将任务完成/胜利曲替换为猎天使魔女的章节通关曲。 |
| [荒野音乐自动减弱](https://www.nexusmods.com/monsterhunterwilds/mods/852)<br><sub>MHWs Music Attenuation</sub> | 1.0.0 | 2025-03-17  | 19 / 445 |  | 在外部音乐播放时将游戏BGM静音。 |
| [极难终焉星二阶段BGM替换 A Long Fall](https://www.nexusmods.com/monsterhunterwilds/mods/3713)<br><sub>(BGM Replace for Savage Omega phase 2) A Long Fall (FF14 ost ver and Primals cover)</sub> | V1.0.2B | 2026-01-01 ✅ | 19 / 829 | `bgm_03_00_m`<br>`bgm_resident_ev` | 将第二阶段主题曲替换为The Primals翻唱的最终幻想14曲目A Long Fall。 |
| [JoJo 飙马野郎 赛克雷特](https://www.nexusmods.com/monsterhunterwilds/mods/4185)<br><sub>JoJo Steel Ball Run Seikret</sub> | 1.041.03.00 | 2026-03-23 ✅ | 18 / 697 | `bgm_03_00_ev`<br>`bgm_03_00_m` | 将陆行鸟赛克雷特皮肤的音乐替换为飙马野郎主题曲。 |
| [泡狐龙BGM 三版混合（XX/崛起/荒野）](https://www.nexusmods.com/monsterhunterwilds/mods/1829)<br><sub>Mizutsune BGM Ver.Tri-Mix (GU RS WS)</sub> | v1.0 | 2025-04-13  | 17 / 489 | `bgm_01_00_m` | 将泡狐龙主题曲替换为荒野、崛起与XX版本的三合一混音。 |
| [FATE BGM大改](https://www.nexusmods.com/monsterhunterwilds/mods/4183)<br><sub>FATE BGM Overhaul</sub> | 1.2 | 2026-05-13 ✅ | 17 / 985 | `bgm_02_00_m`<br>`bgm_04_00_m`<br>`bgm_resident_1st_m`<br>`bgm_resident_ev` … | 以轻奇幻风格全面替换游戏音乐。 |
| [合金装备4胜利曲替换任务完成曲](https://www.nexusmods.com/monsterhunterwilds/mods/1074)<br><sub>MGS4 Victory Theme for Quest Complete</sub> | 1.1 | 2025-03-23  | 16 / 579 | `bgm_resident_1st_m`<br>`bgm_resident_1st_m` | 将任务完成曲替换为合金装备4的胜利曲。 |
| [任务完成曲替换 - MH Dos](https://www.nexusmods.com/monsterhunterwilds/mods/3800)<br><sub>Quest Clear Theme Replacement - MH Dos</sub> | 1.0.1 | 2026-01-16 ✅ | 16 / 453 | `bgm_resident_1st_m` | 将任务完成BGM替换为怪物猎人2（Dos）的Praising Success。 |
| [泡狐龙混合BGM三合一版](https://www.nexusmods.com/monsterhunterwilds/mods/1720)<br><sub>Mizutsune Mix BGM 3in1.ver</sub> | 1.0 | 2025-04-09  | 16 / 463 | `bgm_01_00_m` | 将荒野中泡狐龙的BGM替换为荒野、崛起与X的混音版本。 |
| [绚辉狩猎笛演奏《春日影》](https://www.nexusmods.com/monsterhunterwilds/mods/1313)<br><sub>Play Haruhikage on Artian Horns</sub> | 1.5 | 2025-03-29  | 15 / 498 | `it0500_0014_m`<br>`it0510_0003_m` | 替换绚辉狩猎笛（Omiltika）的音频，使其演奏真正好听的歌曲。 |
| [泡狐龙双版混音BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/1695)<br><sub>Mizutsune Dual Mix BGM Replacement</sub> | 1.2 | 2025-04-09  | 14 / 707 | `bgm_01_00_m`<br>`bgm_01_00_m` | 将泡狐龙主题曲及追击曲替换为崛起与XX版本的混音版。 |
| [蔚蓝档案任务完成BGM](https://www.nexusmods.com/monsterhunterwilds/mods/1894)<br><sub>Blue Archive Quest Clear BGM</sub> | 1.0.0 | 2025-04-16  | 14 / 475 | `bgm_resident_1st_m` | 将任务完成BGM替换为蔚蓝档案的胜利BGM。 |
| [鬼泣×神之手 巨戟龙战斗音乐](https://www.nexusmods.com/monsterhunterwilds/mods/3676)<br><sub>DMCxGodHand Music For Gog</sub> | 1.2 | 2025-12-30 ✅ | 14 / 347 | `bgm_04_00_m` | 将巨戟龙的战斗音乐改为Abyssal Time、Cavaliere Angelo与Broncobuster依次衔接，过渡相当自然。 |
| [光与影：33号远征队 歌姬BGM](https://www.nexusmods.com/monsterhunterwilds/mods/2462)<br><sub>MHWilds - Clair Obscur - Diva - BGM Mod</sub> | 2.0 | 2025-08-01  | 13 / 647 | `bgm_01_00_ev`<br>`bgm_01_00_m` | BGM合集模组，将歌姬的《生命之地》替换为《光与影：33号远征队》的音乐。 |
| [Frontier交易酒馆BGM替换集会所](https://www.nexusmods.com/monsterhunterwilds/mods/1737)<br><sub>Frontier Exchange Tavern BGM Over Hub</sub> | 1.1 | 2025-07-01  | 13 / 609 | `bgm_resident_ev`<br>`bgm_resident_m` | 将集会所/大集会所的昼夜BGM替换为Frontier交易酒馆的昼夜主题曲。 |
| [终焉星二阶段异度神剑BGM《You Will Know Our Names》](https://www.nexusmods.com/monsterhunterwilds/mods/3506)<br><sub>(BGM Mod) Omega PHASE 2 Xenoblade - You Will Know Our Names</sub> | 1.0.1 | 2026-01-02 ✅ | 12 / 457 | `bgm_03_00_m`<br>`bgm_resident_ev` | 将终焉星（极）第二阶段音乐替换为异度神剑的《You Will Know Our Names》。 |
| [主菜单音乐](https://www.nexusmods.com/monsterhunterwilds/mods/3584)<br><sub>Main Menu Music</sub> | 1.0 | 2025-12-08  | 12 / 691 | `bgm_01_00_m`<br>`bgm_jukebox_1st_m`<br>`bgm_resident_1st_m` | 更换主菜单的背景音乐。 |
| [P3结云村音乐替换据点BGM](https://www.nexusmods.com/monsterhunterwilds/mods/1462)<br><sub>Replace MHWS Basecamp Music with MHP3 Pieces (Yukumo Village)</sub> | 1.0 | 2025-04-01  | 11 / 466 | `bgm_resident_1st_m`<br>`bgm_resident_1st_m`<br>`bgm_resident_ev` | 将荒野据点营地音乐替换为P3结云村的四首曲目。 |
| [冰原任务完成曲替换（轻量版）](https://www.nexusmods.com/monsterhunterwilds/mods/1168)<br><sub>MHWI Quest Clear Theme Replacement (lite ver)</sub> | 1.0 | 2025-03-23  | 10 / 286 | `bgm_resident_1st_m` | 将荒野任务完成BGM替换为冰原的任务完成曲《寒空に響く凱歌》。 |
| [Fender火龙Telecaster手势Ado音乐](https://www.nexusmods.com/monsterhunterwilds/mods/3871)<br><sub>Ado Music for Fender Rathalos Telecaster Gesture</sub> | 1.0 | 2026-03-06 ✅ | 10 / 863 | `human_gesture_music_02_00` | 将Fender火龙Telecaster吉他手势的音乐替换为Ado的歌曲。 |
| [宝可梦与塞尔达回复及稀有素材音效](https://www.nexusmods.com/monsterhunterwilds/mods/4545)<br><sub>Healing and Rare Material Sounds from Pokemon and Zelda</sub> | 1.0 | 2026-08-10 ✅ | 10 / 390 | （无法预览） | 将回复与获得稀有素材的音效替换为宝可梦和塞尔达的经典提示音。 |
| [浴血黑帮主题曲](https://www.nexusmods.com/monsterhunterwilds/mods/1724)<br><sub>Peaky Blinders Theme Song</sub> | 1.0 | 2025-04-09  | 10 / 233 | `bgm_resident_1st_m` | 将原版胜利音乐替换为《浴血黑帮》主题曲。 |
| [杀戮都市（Gantz）主题](https://www.nexusmods.com/monsterhunterwilds/mods/2295)<br><sub>Gantz theme for MHWilds</sub> | V1 | 2025-05-07  | 9 / 188 |  | 受奥浩哉漫画《杀戮都市》启发的主题模组，作者认为组队狩猎怪物与组队猎杀外星人十分相似。 |
| [弱势怪物轻主题自定义任务（ScarletStar）](https://www.nexusmods.com/monsterhunterwilds/mods/3328)<br><sub>Lightly themed custom quests for the underdogs (ScarletStar)</sub> | y26mar5 | 2026-03-05 ✅ | 9 / 447 |  | 逐个调整难度的自定义活动任务，让原版后期缺乏强度的怪物重新具有挑战价值。 |
| [幻想乡的狂野音乐](https://www.nexusmods.com/monsterhunterwilds/mods/4372)<br><sub>Wild Music of Gensokyo</sub> | 3 | 2026-06-09 ✅ | 9 / 486 | （无法预览） | 将游戏中约90%的音乐替换为东方Project音乐；歌姬曲目在集会所会导致崩溃。 |
| [尼尔《Song of the Ancients》Xu Wu狩猎笛](https://www.nexusmods.com/monsterhunterwilds/mods/3540)<br><sub>Song of the Ancients (NieR) Xu Wu Hunting Horn</sub> | y25nov15 | 2025-11-15  | 9 / 889 | `it0500_0020_m` | 以迷你吉他版配合Emi Evans人声，替换Xu Wu狩猎笛的旋律。 |
| [P3任务完成BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/1382)<br><sub>MHWs_QuestClear_p3_BGM_Replacement</sub> | 1.0 | 2025-03-29  | 8 / 251 | `bgm_resident_1st_m` | 将荒野任务完成音乐替换为P3结云村的任务完成曲。 |
| [关羽之歌替换巨戟龙任务BGM](https://www.nexusmods.com/monsterhunterwilds/mods/3633)<br><sub>Guan Yu's Song for Gogmazios</sub> | 1.0 | 2025-12-23 ✅ | 8 / 211 | `bgm_04_00_m`<br>`bgm_resident_ev` | 用关羽之歌替换巨戟龙任务中的《英雄之证》。 |
| [巨戟龙任务4G任务完成曲](https://www.nexusmods.com/monsterhunterwilds/mods/3801)<br><sub>(BGM Mod) MH4U Quest Clear Theme for GOGMAZIOS</sub> | 1.0.1 | 2026-01-17 ✅ | 8 / 431 | `bgm_resident_ev`<br>`bgm_resident_m` | 将巨戟龙活动任务的任务完成曲替换为MH4G的任务完成曲。 |
| [终焉星战斗曲替换](https://www.nexusmods.com/monsterhunterwilds/mods/3422)<br><sub>Omega Battle Theme Changed</sub> | 1.0 | 2025-10-19  | 7 / 187 | `bgm_03_00_m` | 更换终焉星的战斗主题曲。 |
| [终焉星二阶段异度神剑BGM《An Obstacle in our Path》](https://www.nexusmods.com/monsterhunterwilds/mods/3500)<br><sub>(BGM Mod) Omega PHASE 2 Xenoblade - An Obstacle in our Path</sub> | 1.0.2 | 2026-01-02 ✅ | 7 / 199 | `bgm_03_00_m`<br>`bgm_resident_ev` | 将终焉星第二阶段音乐替换为异度神剑原声《An Obstacle in our Path》。 |
| [Wilder State of Music](https://www.nexusmods.com/monsterhunterwilds/mods/4652) | 1.1 | 2026-08-01 ✅ | 7 / 211 | （无法预览） | 基于State of Music模组的音乐预设，为环境区域与战斗添加主题曲，并力求无缝循环与氛围贴合。 |
| [荒野特殊任务完成曲替换（轻量版）](https://www.nexusmods.com/monsterhunterwilds/mods/1170)<br><sub>MHWs Special Quest Clear Theme Replacement (lite ver)</sub> | 1.0 | 2025-03-23  | 6 / 202 | `bgm_resident_1st_m` | 将普通任务完成BGM替换为狂界、护锁刃龙、白炽龙等特殊任务的完成BGM。 |
| [黑蚀龙狩猎笛音频重制](https://www.nexusmods.com/monsterhunterwilds/mods/3084)<br><sub>Reimagined Hunting Horn (audio) Gore Magala</sub> | y25aug17 | 2025-08-17  | 6 / 769 | `it0500_0011_m` | 受合成器乐器和黑蚀龙变种启发，手工重制黑蚀龙狩猎笛的旋律。 |
| [任天堂明星大乱斗锤子音乐用于大锤蓄力](https://www.nexusmods.com/monsterhunterwilds/mods/3819)<br><sub>Super Smash Bros. Hammer Jingle for Hammer's Mighty Charge</sub> | 1.0 | 2026-01-22 ✅ | 6 / 384 | `wp04_cmn_m` | 将大乱斗的锤子道具音乐用于大锤的蓄力（Mighty Charge）。 |
| [毁灭战士龙击炮（铳枪）](https://www.nexusmods.com/monsterhunterwilds/mods/3968)<br><sub>DOOM Wyvernfire - Gunlance</sub> | 1.0 | 2026-02-16 ✅ | 6 / 368 | `wp07_cmn_m` | 将铳枪龙击炮的蓄力音效替换为DOOM主题曲。 |
| [弓看破回避音效替换为自在极意](https://www.nexusmods.com/monsterhunterwilds/mods/2580)<br><sub>Bow Discerning Dodge SFX replacemet Ultra Instinct</sub> | 1.0 | 2025-05-29  | 5 / 972 | `wp11_cmn_m` | 将弓的看破回避（Discerning Dodge）音效替换为自在极意主题曲的第一个音。 |
| [《空より現れし者》替换巨戟龙《英雄之证》](https://www.nexusmods.com/monsterhunterwilds/mods/3779)<br><sub>From the Heavens replace Proof of a Hero for Gogmazios</sub> | 1.0 | 2026-01-10 ✅ | 5 / 182 | `bgm_04_00_m`<br>`bgm_resident_ev` | 用终焉星使出三角攻击后的曲目《空より現れし者》替换巨戟龙任务中的《英雄之证》。 |
| [冲击星替换任务完成曲](https://www.nexusmods.com/monsterhunterwilds/mods/945)<br><sub>dashstar replace the quest complete theme</sub> | 1.0.0 | 2025-03-26  | 3 / 202 | `bgm_resident_1st_m` | 用《dashstar*》替换任务结算小曲。 |
| [旧作主题曲混音](https://www.nexusmods.com/monsterhunterwilds/mods/3118)<br><sub>Remix Old Theme mod</sub> | v0.30-TU4.5 | 2026-02-21 ✅ | 3 / 188 | `bgm_02_00_m`<br>`bgm_04_00_m`<br>`bgm_resident_ev`<br>`bgm_resident_m` | 将荒野中复刻的BGM与旧作对应BGM进行混音。 |
| [史诗级巨戟龙BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/3613)<br><sub>Epic Gogmazios BGM replacer</sub> | 1.3 | 2026-02-09 ✅ | 3 / 327 | `bgm_04_00_m`<br>`bgm_resident_ev` | 更换巨戟龙的战斗背景音乐。 |
| [FATE 煌雷龙BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/4138)<br><sub>FATE Rey Dau BGM Replacer</sub> | 1.0 | 2026-03-15 ✅ | 3 / 155 | `bgm_resident_ev`<br>`bgm_resident_m` | 用FATE系列音乐替换煌雷龙（Rey Dau）BGM，属于全游戏BGM替换计划的一部分。 |
| [FATE 铠龙BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/4144)<br><sub>FATE Arkveld BGM Replacer</sub> | 1.0 | 2026-03-16 ✅ | 3 / 176 | `bgm_resident_ev`<br>`bgm_resident_m` | 用FATE系列音乐替换铠龙（Arkveld）BGM，属于全游戏BGM替换计划的一部分。 |
| [Fender火龙Telecaster手势结束乐队音乐](https://www.nexusmods.com/monsterhunterwilds/mods/4605)<br><sub>Kessoku Band Music for Fender Rathalos Telecaster Gesture</sub> | 1.0 | 2026-07-06 ✅ | 3 / 338 | （无法预览） | 将吉他手势音乐替换为《孤独摇滚！》中结束乐队的歌曲。 |
| [FATE 黑蚀龙BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/4147)<br><sub>FATE Gore Magala BGM Replacer</sub> | 1.0 | 2026-03-16 ✅ | 2 / 129 | `bgm_resident_ev`<br>`bgm_resident_m` | 用FATE系列音乐替换黑蚀龙BGM，属于全游戏BGM替换计划的一部分。 |
| [FATE Uth Duna BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/4148)<br><sub>FATE Uth Duna BGM Replacer</sub> | 1.0 | 2026-03-18 ✅ | 2 / 86 | `bgm_resident_ev`<br>`bgm_resident_m` | 用FATE系列音乐替换Uth Duna的BGM，属于全游戏BGM替换计划的一部分。 |
| [FATE 海龙BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/4162)<br><sub>FATE Lagiacrus BGM Replacer</sub> | 1.0 | 2026-03-18 ✅ | 1 / 96 | `bgm_02_00_m`<br>`bgm_resident_ev` | 用FATE系列音乐替换海龙BGM，属于全游戏BGM替换计划的一部分。 |
| [FATE 标题画面BGM替换](https://www.nexusmods.com/monsterhunterwilds/mods/4169)<br><sub>FATE Title Theme BGM Replacer</sub> | 1.0 | 2026-03-19 ✅ | 1 / 164 | `bgm_resident_1st_m` | 用FATE系列音乐替换开场标题主题曲，属于全游戏BGM替换计划的一部分。 |
| [索尼克 State of Music预设](https://www.nexusmods.com/monsterhunterwilds/mods/4691)<br><sub>Sonic Wilds State of Music</sub> | 1B | 2026-08-15 ✅ | 1 / 98 | （无法预览） | State Music预设，更换集会所、探索与战斗音乐。 |
| [绝地潜兵2撤离曲替换任务完成曲](https://www.nexusmods.com/monsterhunterwilds/mods/4412)<br><sub>Helldivers 2 Extraction over Quest Complete</sub> | 1 | 2026-05-12 ✅ | 0 / 120 | `bgm_resident_1st_m` | 将任务完成音乐替换为《绝地潜兵2》撤离主题曲的结尾部分。 |
| [State Music怪物逃跑音乐](https://www.nexusmods.com/monsterhunterwilds/mods/4686)<br><sub>State of monster rannin a_wav music</sub> | 1 | 2026-08-03 ✅ | 0 / 33 | （无法预览） | 配合State Music使用的音频文件，在怪物逃跑时播放。 |
| [The Emptiness Machine（角力）](https://www.nexusmods.com/monsterhunterwilds/mods/4723)<br><sub>The Emptiness Machine (Power Clash)</sub> | 1 | 2026-08-14 ✅ | 0 / 70 | （无法预览） | 将角力音乐替换为林肯公园的《The Emptiness Machine》。 |

<a id="g"></a>
## G. 其它武器音效（71）

按武器分组。

### 大剑（15）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [荒野Dark Sword音效](https://www.nexusmods.com/monsterhunterwilds/mods/1471)<br><sub>Dark Sword wilds</sub> | 1 | 2025-12-14  | 86 / 2.6k | `weapon_cmn`<br>`wp00_cmn_m` | Dark Sword武器音效，金属类武器音效较全，骨质类武器可能缺失部分音效。 |
| [大剑音效 - 嘿嘿哈语音](https://www.nexusmods.com/monsterhunterwilds/mods/712)<br><sub>Sound Giant sword _  Voice heiheihaa</sub> | 1.0 | 2025-03-14  | 64 / 1.9k | `wp00_cmn_m` | 将大剑音效替换为“嘿嘿哈”语音。 |
| [更酷的大剑音效](https://www.nexusmods.com/monsterhunterwilds/mods/979)<br><sub>Cooler Greatsword Sounds</sub> | 1.2 | 2025-03-22  | 58 / 2.9k | `wp00_cmn_m` | 将大剑的大部分音效提示替换为更酷的声音。 |
| [假面骑士Kabuto大剑/弓/片手剑/斩击斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/995)<br><sub>Kamen Rider Kabuto GS BOW SNS SWAXE sound Mod</sub> | V2.2 | 2025-04-09  | 38 / 1.2k | `hit_hm_cmn`<br>`weapon_cmn`<br>`wp00_cmn_m`<br>`wp01_cmn_m` … | 将大剑、弓、片手剑和斩击斧的音效替换为假面骑士Kabuto的音效。 |
| [黑神话悟空蓄力与铜头铁臂大剑音效](https://www.nexusmods.com/monsterhunterwilds/mods/719)<br><sub>BMW Stick Charging and Bronze Head Metal Arm For GS</sub> | 1.0 | 2025-03-16  | 28 / 813 | `wp00_cmn_m` | 将大剑音效替换为《黑神话：悟空》的棍法蓄力与铜头铁臂格挡音效。 |
| [大剑CLANG音效（剑风传奇2016）](https://www.nexusmods.com/monsterhunterwilds/mods/988)<br><sub>Great Sword make CLANG (Berserk-2016)</sub> | 2.0 | 2025-03-20  | 27 / 943 | `wp00_cmn_m` | 将大剑音效替换为2016版动画《剑风传奇》中的“CLANG”音效。 |
| [祐天寺若麦大剑语音](https://www.nexusmods.com/monsterhunterwilds/mods/1598)<br><sub>Yuutenji Nyamu voice replacement for Greatsword</sub> | 1.0 | 2025-04-14  | 14 / 656 | `weapon_cmn`<br>`wp00_cmn_m` | 将部分大剑音效替换为《Ave Mujica》中祐天寺若麦的语音。 |
| [荒野Dark Sword](https://www.nexusmods.com/monsterhunterwilds/mods/1764)<br><sub>MHWS Dark sword</sub> | 1.0 | 2025-04-11  | 14 / 552 | `weapon_cmn`<br>`wp00_cmn_m` | Dark Sword音效，替换所有大剑音效。 |
| [星际战士大剑音效](https://www.nexusmods.com/monsterhunterwilds/mods/1210)<br><sub>Space Marines great sword sound effects</sub> | 1.0 | 2025-03-26  | 11 / 360 | `weapon_cmn`<br>`wp00_cmn_m` | 大剑音效取自《星际战士》，为作者自行录制，可能存在瑕疵。 |
| [Mortis大剑语音](https://www.nexusmods.com/monsterhunterwilds/mods/1718)<br><sub>Mortis voice for Greatsword</sub> | 1.10 | 2025-04-12  | 11 / 499 | `weapon_cmn`<br>`wp00_cmn_m` | 用Mortis的语音替换大剑音效。 |
| [漫画英雄VS卡普空3播报员大剑蓄力音效](https://www.nexusmods.com/monsterhunterwilds/mods/2585)<br><sub>MvC3 Announcer over Greatsword Charge SFX</sub> | 1.1 | 2025-05-30  | 10 / 240 | `wp00_cmn_m` | 将大剑蓄力音效替换为MvC3的男性播报员语音。 |
| [异度神剑2 焰大剑语音（日语）](https://www.nexusmods.com/monsterhunterwilds/mods/1906)<br><sub>Xenoblade Chronicles 2 Pyra Great Sword Voice (Janpanese)</sub> | 1.0.0 | 2025-04-17  | 8 / 287 | `wp00_cmn_m` | 用异度神剑2中焰（Pyra）的日语语音替换大剑音效。 |
| [荒野otto大剑音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/944)<br><sub>MHWs otto sfx Greatgreatsword replace</sub> | 1 | 2025-03-19  | 3 / 122 | `weapon_cmn`<br>`wp00_cmn_m` | 用otto音效替换大剑音效。 |
| [企鹅盖伦大剑音效](https://www.nexusmods.com/monsterhunterwilds/mods/2041)<br><sub>Penguin Garen Great Sword Sound</sub> | 1.0 | 2025-04-22  | 3 / 105 | `hit_weapon_cmn`<br>`human_common_effect`<br>`weapon_cmn`<br>`wp00_cmn_m` | 将大剑音效替换为英雄联盟企鹅盖伦及一段B站视频中的语音。 |
| [碧蓝幻想Relink伊德语音（大剑）](https://www.nexusmods.com/monsterhunterwilds/mods/2622)<br><sub>GBFR  Id's voice Replacement  Great Sword</sub> | 1.0 | 2025-06-02  | 1 / 92 | `wp00_cmn_m` | 将大剑音效替换为《碧蓝幻想Relink》中伊德的语音。 |

### 片手剑（5）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [樱潮太刀与短刀（片手剑）](https://www.nexusmods.com/monsterhunterwilds/mods/2527)<br><sub>Sakuratide Katana and Dagger (SnS)</sub> | 1.1 | 2026-02-21 ✅ | 88 / 3.3k | `wp01_cmn_m` | 将希望之剑替换为樱潮太刀与短刀，并使用只狼的格挡音效。 |
| [碧蓝幻想Relink姬塔语音（片手剑）](https://www.nexusmods.com/monsterhunterwilds/mods/1076)<br><sub>GBFR-Djeeta's voice Replacement (Sword And Shield)</sub> | 1.0 | 2025-03-23  | 34 / 1.2k | `hit_weapon_cmn`<br>`human_common_effect`<br>`weapon_cmn`<br>`wp01_cmn_m` | 将片手剑音效替换为《碧蓝幻想Relink》中姬塔的语音。 |
| [Mortis片手剑音效](https://www.nexusmods.com/monsterhunterwilds/mods/609)<br><sub>Mortis Sword And Shield Sound</sub> | 1.0 | 2025-03-12  | 25 / 1.4k | `hit_weapon_cmn`<br>`human_common_effect`<br>`weapon_cmn`<br>`wp01_cmn_m` | 将片手剑音效替换为动画《Ave Mujica》中Mortis的语音。 |
| [异度神剑2 焰英文语音（片手剑）](https://www.nexusmods.com/monsterhunterwilds/mods/1449)<br><sub>XC2- Pyra's EN Voice Replacement (Sword And Shield)</sub> | 1.0 | 2025-03-31  | 4 / 169 | `hit_weapon_cmn`<br>`human_common_effect`<br>`human_common_foley`<br>`human_slinge_shell` … | 将片手剑及部分道具音效替换为异度神剑2中焰的英文语音。 |
| [希斯克利夫片手剑音效](https://www.nexusmods.com/monsterhunterwilds/mods/967)<br><sub>Heathcliff Sword And Shield Sound</sub> | 1.0 | 2025-03-19  | 3 / 299 | `wp01_cmn_m` | 将片手剑音效替换为《边狱巴士》中魔王希斯克利夫的语音。 |

### 双刀（6）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [更酷的双刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/628)<br><sub>Cooler Dual Blades Sounds</sub> | 1.2 | 2025-03-22  | 49 / 2.2k | `wp02_cmn_m` | 将鬼人化相关音效替换为更酷的声音。 |
| [悟空自在极意完美回避](https://www.nexusmods.com/monsterhunterwilds/mods/1899)<br><sub>Goku UI Perfect Dodging</sub> | 1.0.1 | 2025-04-17  | 25 / 1.5k | `wp02_cmn_m`<br>`wp11_cmn_m` | 双刀与弓的回避音效替换为悟空自在极意的经典音效。 |
| [风灵月影与只狼双刀音效](https://www.nexusmods.com/monsterhunterwilds/mods/885)<br><sub>FLiNG Trainer Sekiro Dual Blades Sound</sub> | 1.0 | 2025-03-18  | 15 / 843 | `wp02_cmn_m` | 将双刀音效替换为风灵月影修改器及只狼的音效。 |
| [鼓棒双刀](https://www.nexusmods.com/monsterhunterwilds/mods/1956)<br><sub>Drumsticks Dual Blades</sub> | 1.0 | 2025-04-19  | 4 / 179 | `it0200_0014_m`<br>`wp02_cmn_m` | 将绚辉双刀替换为鼓棒，可选将攻击音效改为鼓声。 |
| [明日方舟 麒麟R夜刀与缄默德克萨斯双刀语音](https://www.nexusmods.com/monsterhunterwilds/mods/911)<br><sub>ARKNIGHTS Kirin R Yato and Texas the Omertosa twin sword voice</sub> | V2 | 2025-03-19  | 2 / 266 | `wp02_cmn_m` | 用德克萨斯和夜刀的语音替换双刀语音。 |
| [神驹斑（新春）双刀音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/4220)<br><sub>Madara-xinchun Dual Blades SFX Replacement</sub> | 1.0 | 2026-04-01 ✅ | 2 / 419 | `wp02_cmn_m` | 将双刀部分音效替换为神驹斑（新春）的语音。 |

### 大锤（1）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [漫画英雄VS卡普空3播报员大锤蓄力音效](https://www.nexusmods.com/monsterhunterwilds/mods/2600)<br><sub>MvC3 Announcer over Hammer Charge SFX</sub> | 1.0 | 2025-05-30  | 5 / 254 | `wp04_cmn_m` | 将大锤蓄力音效替换为MvC3的男性播报员语音。 |

### 狩猎笛（4）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [狩猎笛集中攻击替换为Free Bird](https://www.nexusmods.com/monsterhunterwilds/mods/1239)<br><sub>Replace the concentrated attack of Hunting Horn with Free Bird</sub> | 1.0 | 2025-03-25  | 25 / 900 | `wp05_cmn_m` | 将狩猎笛集中攻击替换为Free Bird并卡准节拍点，便于打出完美集中攻击。 |
| [曼波狩猎笛1](https://www.nexusmods.com/monsterhunterwilds/mods/1173)<br><sub>Mambo hunting flute 1</sub> | 1.0 | 2025-03-23  | 23 / 628 | `wp05_cmn_m`<br>`wp05_shell` | 曼波狩猎笛音效，需配合REFramework使用，修改了6种音符、响周波、响玉与集中攻击。 |
| [狩猎笛音效（笛子）](https://www.nexusmods.com/monsterhunterwilds/mods/870)<br><sub>Sound FOR Hunting Horn(flute)</sub> | 1.0 | 2025-03-17  | 3 / 130 | `wp05_cmn_m` | 替换狩猎笛音效为笛子声音。 |
| [祥子狩猎笛音效替换](https://www.nexusmods.com/monsterhunterwilds/mods/1976)<br><sub>Sakiko hunting horn sound effect replace</sub> | 1.02 | 2025-04-21  | 2 / 98 | `it0500_0000_m`<br>`it0500_0001_m`<br>`it0500_0002_m`<br>`it0500_0003_m` … | 替换狩猎笛部分音效。 |

### 长枪（2）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [长枪韩语语音](https://www.nexusmods.com/monsterhunterwilds/mods/1943)<br><sub>Lance with Korean voice</sub> | 1.1 | 2025-04-18  | 7 / 251 | `wp06_cmn_m` | 为长枪添加韩语女声语音音效。 |
| [长枪音效 otto鬼叫](https://www.nexusmods.com/monsterhunterwilds/mods/2015)<br><sub>Monster Hunter Wild  Long Spear Sound Effect  Otto's Ghost Howl</sub> | 1.01 | 2025-04-21  | 2 / 88 | `wp06_cmn_m`<br>`wp06_cmn_m` | 将长枪反击音效替换为otto鬼叫，仿佛与怪物对吼；此为初版。 |

### 铳枪（7）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [铳枪装填音效替换 - M1加兰德](https://www.nexusmods.com/monsterhunterwilds/mods/167)<br><sub>Gunlance Reload SFX Replacement - M1 Garand</sub> | 1.0.1 | 2025-03-08  | 154 / 5.0k | `wp07_cmn_m` | 将铳枪的装填音效替换为M1加兰德的弹夹“叮”声。 |
| [重炮铳枪 荒野版](https://www.nexusmods.com/monsterhunterwilds/mods/890)<br><sub>Heavy Artillery Gunlance Wilds</sub> | 1.0 | 2025-03-18  | 64 / 1.6k | `wp07_cmn_m`<br>`wp07_shell` | 铳枪音效模组的荒野版本。 |
| [超燃铳枪音效](https://www.nexusmods.com/monsterhunterwilds/mods/1080)<br><sub>Insane Gunlance Sounds</sub> | 1.0 | 2025-03-21  | 60 / 2.4k | `wp07_cmn_m`<br>`wp07_shell` | 将铳枪的爆炸声及部分提示音替换为更酷的声音。 |
| [惠惠爆裂魔法铳枪（龙击炮）](https://www.nexusmods.com/monsterhunterwilds/mods/3501)<br><sub>Megumin Explosion Gunlance (Wyvern's Fire)</sub> | 1.0 | 2025-11-01  | 29 / 1.1k | `wp07_cmn_m`<br>`wp07_shell` | 将铳枪龙击炮替换为惠惠的爆裂魔法音效。 |
| [尖叫龙击炮（铳枪音效）](https://www.nexusmods.com/monsterhunterwilds/mods/1452)<br><sub>Screaming Wyvern's Fire(gunlance sound mod)</sub> | 1.0 | 2025-03-31  | 28 / 1.1k | `wp07_cmn_m`<br>`wp07_shell` | 为龙击炮音效加入野兽先辈的叫声。 |
| [天童爱丽丝铳枪语音](https://www.nexusmods.com/monsterhunterwilds/mods/1741)<br><sub>Alice Tendo voice for Gun Lance</sub> | 0.01 | 2025-04-10  | 20 / 787 | `wp07_cmn_m` | 用天童爱丽丝的语音替换铳枪音效。 |
| [打火石（武器音效）](https://www.nexusmods.com/monsterhunterwilds/mods/1862)<br><sub>FLINT AND STEEL (WeaponnSound Effect)</sub> | 1.5 | 2026-10-02 ✅ | 5 / 287 | `wp07_shell` | 将武器音效替换为打火石（Flint and Steel）音效。 |

### 斩斧（8）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [超燃斩击斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/874)<br><sub>Insane Switch Axe Sounds</sub> | 1.2 | 2025-03-22  | 94 / 3.7k | `wp08_cmn_m` | 将斩击斧的大部分招式音效替换为更酷的声音。 |
| [斩击斧惠惠语音](https://www.nexusmods.com/monsterhunterwilds/mods/584)<br><sub>Switch Axe Megumin voice</sub> | 1.0.0 | 2025-03-12  | 91 / 2.5k | `wp08_cmn_m` | 为斩击斧加入惠惠的“Explosion!”爆裂魔法语音。 |
| [斩击斧全解放斩音效](https://www.nexusmods.com/monsterhunterwilds/mods/1068)<br><sub>SwitchAxe FullReleaseSlash SFX</sub> | 2.1 | 2025-03-23  | 52 / 1.7k | `wp08_cmn_m` | 将斩击斧全解放斩音效替换为高达光剑音效，现已支持所有瓶类型。 |
| [阿尔托莉雅语音替换斩击斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/1161)<br><sub>Altria Pendragon voice replace switch axe sound effects</sub> | 1.0.0 | 2025-03-24  | 26 / 1.3k | `hit_hm_cmn`<br>`wp08_cmn_m` | 将斩击斧部分技能音效替换为阿尔托莉雅·潘德拉贡的语音。 |
| [约翰·塞纳全解放斩音效](https://www.nexusmods.com/monsterhunterwilds/mods/2111)<br><sub>JOHN CENA Full Release Slash Sound Effect</sub> | 1.0 | 2025-04-25  | 22 / 738 | `wp08_cmn_m` | 将斩击斧全解放斩音效替换为约翰·塞纳的“And His Name is JOHN CENA”。 |
| [星际战士斩击斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/1427)<br><sub>Space Marines switchaxe sound effects</sub> | 1.0 | 2025-03-30  | 9 / 405 | `hit_hm_cmn`<br>`wp08_cmn_m` | 因斩击斧音效文件零散，仅替换了一小部分，但效果仍不错。 |
| [斩击斧蓄力音效 - 忍者龙剑传隼龙](https://www.nexusmods.com/monsterhunterwilds/mods/426)<br><sub>Switch Axe Charge SFX - Ninja Gaiden Ryu Hayabusa</sub> | 1.0 | 2025-03-08  | 8 / 431 | `wp08_cmn_m` | 将斩击斧蓄力音效替换为《忍者龙剑传》隼龙的音效。 |
| [火之神神乐 炭治郎语音（斩击斧）](https://www.nexusmods.com/monsterhunterwilds/mods/3513)<br><sub>Hinokami Kagura Tanjiro Voice (Switch Axe)</sub> | 1.0 | 2025-11-05  | 5 / 324 | `wp08_cmn_m` | 将斩击斧音效替换为《鬼灭之刃》炭治郎的语音。 |

### 盾斧（5）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [超燃盾斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/725)<br><sub>Insane Charge Blade Sounds</sub> | 1.2 | 2025-03-22  | 128 / 5.0k | `wp09_cmn_m` | 将盾斧的大部分招式音效替换为更酷的声音。 |
| [盾斧但丁语音](https://www.nexusmods.com/monsterhunterwilds/mods/1917)<br><sub>Charge Blade with Dante voice</sub> | 1.0 | 2025-05-05  | 22 / 740 | `weapon_cmn`<br>`wp09_cmn_m` | 使用盾斧时播放鬼泣5中但丁的语音。 |
| [假面骑士极狐Boost盾斧音效](https://www.nexusmods.com/monsterhunterwilds/mods/1529)<br><sub>Kamen Rider Geats Boost SFX for CB (CHARGE BLADE)</sub> | 1.1 | 2025-04-05  | 19 / 601 | `wp09_cmn_m`<br>`wp09_cmn_m` | 将盾斧充能、属性强化回旋斩（Condensed Element Slash）与属性解放斩音效改为极狐Boost扣带音效。 |
| [超燃盾斧音效 电锯版](https://www.nexusmods.com/monsterhunterwilds/mods/3354)<br><sub>Insane Charge Blade Sounds Chainsaw Edit</sub> | 1 | 2025-11-04  | 7 / 302 | `wp09_cmn_m` | 基于原超燃盾斧音效模组，加入电锯音效。 |
| [明日方舟 煌](https://www.nexusmods.com/monsterhunterwilds/mods/4470)<br><sub>Arknights-blaze</sub> | 1 | 2026-05-24 ✅ | 3 / 213 | `wp09_cmn_m` | 明日方舟煌的盾斧音效。 |

### 操虫棍（9）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [阿拉妮雅·海温德（最终幻想15）语音包](https://www.nexusmods.com/monsterhunterwilds/mods/3864)<br><sub>Aranea Highwind (Final Fantasy XV) Voice Pack</sub> | 1.2 | 2026-08-26 ✅ | 45 / 1.8k | `wp10_cmn_m` | 最终幻想15中阿拉妮雅·海温德的语音包。 |
| [操虫棍螺旋上升斩 Helikopter音效](https://www.nexusmods.com/monsterhunterwilds/mods/658)<br><sub>Helikopter Helikopter for Insect Glaive Rising Spiral Slash attack</sub> | 1 | 2025-03-13  | 42 / 1.0k | `wp10_cmn_m` | 将操虫棍螺旋上升斩（消耗三灯的那招）的音效改为Helikopter Helikopter梗音。 |
| [更酷的操虫棍音效](https://www.nexusmods.com/monsterhunterwilds/mods/538)<br><sub>Cooler Glaive Sounds</sub> | 1.2 | 2025-03-22  | 41 / 3.1k | `wp10_cmn_m`<br>`wp10_insect_cmn_m` | 将操虫棍大部分招式音效替换为更酷的声音。 |
| [碧蓝幻想Relink姬塔与泽塔语音（操虫棍）](https://www.nexusmods.com/monsterhunterwilds/mods/1523)<br><sub>GBFR-Djeeta and Zeta's voice Replacement (Insect Glaive)</sub> | 1.0 | 2025-04-05  | 19 / 971 | `wp10_cmn_m` | 将操虫棍音效替换为《碧蓝幻想Relink》中姬塔与泽塔的语音。 |
| [煌雷龙操虫棍 - 重制版](https://www.nexusmods.com/monsterhunterwilds/mods/4114)<br><sub>Rey Dau Glaive - RE-Edits -</sub> | RE1.0.00 | 2026-03-14 ✅ | 14 / 405 | `it1000_0007_m`<br>`wp10_cmn_7` | 以煌雷龙（Rey Dau）外观与特质为灵感的自定义操虫棍，附带自定义音效。 |
| [铁拳8播报计数操虫棍蓄力音](https://www.nexusmods.com/monsterhunterwilds/mods/832)<br><sub>Tekken 8 announcer count for Insect Glaive charge sound</sub> | 1 | 2025-03-21  | 13 / 308 | `wp10_cmn_m` | 将操虫棍的两段蓄力音效替换为铁拳8播报员的“1、2”计数。 |
| [神鹰哥操虫棍语音](https://www.nexusmods.com/monsterhunterwilds/mods/1394)<br><sub>EaglemanVoices for Insect Glaive</sub> | 1.51 | 2025-03-29  | 11 / 319 | `wp10_cmn_m` | 使用操虫棍蓄力和攻击时，神鹰哥会为你提供强大的精神（语音）支持。 |
| [NIKKE爱丽丝操虫棍语音](https://www.nexusmods.com/monsterhunterwilds/mods/2557)<br><sub>Nikke  Alice voice effects for Insect Glaive</sub> | 1.0 | 2025-05-26  | 8 / 217 | `wp10_cmn_m` | 将NIKKE爱丽丝的语音用于操虫棍。 |
| [操虫棍音效 堂吉诃德（拉·曼却领经理）](https://www.nexusmods.com/monsterhunterwilds/mods/3913)<br><sub>Glaive SFX Don Quixote The Manager of La Manchaland</sub> | 1.0 | 2026-02-07 ✅ | 2 / 233 | `wp10_cmn_m` | 将操虫棍部分音效替换为拉·曼却领经理堂吉诃德的语音。 |

### 轻弩（4）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [冰原弓音效](https://www.nexusmods.com/monsterhunterwilds/mods/1262)<br><sub>MHWI Bow SFX</sub> | 0.3.0 | 2025-04-20  | 49 / 1.9k | `hit_weapon_cmn`<br>`wp11_cmn_m` | 个人用模组，尝试将冰原的弓音效移植回荒野（制作中）。 |
| [拉克丝弓语音](https://www.nexusmods.com/monsterhunterwilds/mods/2012)<br><sub>Lux's voice for Bow</sub> | 1.0 | 2025-04-23  | 17 / 545 | `wp11_cmn_m` | 为弓添加拉克丝（Lux）的语音。 |
| [Tetrad弓音效](https://www.nexusmods.com/monsterhunterwilds/mods/3781)<br><sub>Tetrad Bow Sounds</sub> | 1.0 | 2026-01-11 ✅ | 9 / 485 | `wp11_cmn_m` | 将所有刚射音效替换为“Tetrad Shot”音效。 |
| [Jewelry Hearts Academia的mea语音替换弓](https://www.nexusmods.com/monsterhunterwilds/mods/1237)<br><sub>mea voice from Jewelry hearts academia   change Archer voice</sub> | 17637685 | 2025-03-25  | 4 / 160 | `wp11_cmn_m` | 将弓的语音替换为mea的语音。 |

### 重弩（2）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [Apex英雄重弩音效](https://www.nexusmods.com/monsterhunterwilds/mods/2299)<br><sub>Apex Legends HBG sound</sub> | 1.0 | 2025-05-07  | 26 / 595 | `wp12_cmn_m` | 将重弩的机枪音效替换为三种Apex英雄枪械音效。 |
| [NIKKE爱丽丝重弩语音](https://www.nexusmods.com/monsterhunterwilds/mods/2567)<br><sub>Alice nikke  voice for Heavy Bowgun</sub> | 1.0 | 2025-05-27  | 8 / 271 | `wp12_cmn_m` | 将NIKKE爱丽丝的语音用于重弩。 |

### 弓（3）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [弩装填音效替换 - M1加兰德](https://www.nexusmods.com/monsterhunterwilds/mods/182)<br><sub>Bowguns Reload SFX Replacement - M1 Garand</sub> | 1.0.1 | 2025-03-08  | 176 / 7.8k | `wp13_cmn_m` | 将轻弩与重弩的装填音效替换为M1加兰德的弹夹“叮”声，轻重弩文件分开提供。 |
| [明日方舟维什戴尔轻弩语音](https://www.nexusmods.com/monsterhunterwilds/mods/687)<br><sub>ARKNIGHTS_Wisadel light crossbow voice</sub> | V2 | 2025-03-14  | 12 / 509 | `wp13_cmn_m` | 将轻弩语音替换为明日方舟维什戴尔的语音。 |
| [NIKKE爱丽丝轻弩语音](https://www.nexusmods.com/monsterhunterwilds/mods/2510)<br><sub>Alice nikke light bowgun voice</sub> | 1.0 | 2025-06-11  | 7 / 385 | `wp13_cmn_m` | 将NIKKE爱丽丝的语音用于轻弩。 |

<a id="h"></a>
## H. 其它音效（道具、环境、UI、怪物等）（42）

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [桃毛兽混响放屁](https://www.nexusmods.com/monsterhunterwilds/mods/381)<br><sub>Congalala Fart with Reverb</sub> | 2 | 2025-03-18  | 227 / 9.0k | `em0021_00_0_shell` | 将桃毛兽默认的放屁音效替换为带混响的放屁声。 |
| [静音楔甲虫铃声](https://www.nexusmods.com/monsterhunterwilds/mods/232)<br><sub>Silence Wedge Beetle Chime</sub> | 1.0 | 2025-03-05  | 214 / 4.9k | （无法预览） | 关闭楔甲虫（Wedge Beetle）发出的叮铃声。 |
| [MH3采集音效](https://www.nexusmods.com/monsterhunterwilds/mods/522)<br><sub>MH3 Gather Sound</sub> | 1.0 | 2025-03-10  | 179 / 4.0k | `gui_cmn` | 将采集音效替换为MH3至XX时代的采集音效。 |
| [呼叫赛克雷特音效替换 - 钥匙与遥控解锁声](https://www.nexusmods.com/monsterhunterwilds/mods/844)<br><sub>Call Seikret Sound Replacement - Jingling Keys and Keyless Entry Chirp</sub> | 2.0.0-no-keys | 2025-03-18  | 162 / 6.5k | `human_common_foley` | 将呼叫赛克雷特的音效替换为车钥匙晃动声加遥控解锁提示音。 |
| [更柔和的赛克雷特口哨](https://www.nexusmods.com/monsterhunterwilds/mods/150)<br><sub>Softer Seikret Whistle Signal</sub> | 1.0 | 2025-03-26  | 103 / 2.3k | `human_common_foley`<br>`porter_cmn_voice` | 让呼叫赛克雷特的长短口哨声更柔和。 |
| [汽水罐回复药（含音效）](https://www.nexusmods.com/monsterhunterwilds/mods/1789)<br><sub>Soda can potions (Now With Sound)</sub> | 1.0 | 2026-08-12 ✅ | 95 / 5.0k | `acc002_010` | 将回复药变为各种汽水罐。 |
| [大粪臭弹替换为放屁音效](https://www.nexusmods.com/monsterhunterwilds/mods/326)<br><sub>LargeDung To LargeFart SFX Replacement</sub> | 1.0 | 2025-03-07  | 68 / 3.3k | `human_slinge_shell` | 将大粪臭弹的发射音效替换为经典带混响的放屁梗音效。 |
| [盾斧装填音效替换 - M1加兰德](https://www.nexusmods.com/monsterhunterwilds/mods/1440)<br><sub>Charge Blade Reload SFX Replacement - M1 Garand</sub> | 1.0 | 2025-03-30  | 64 / 1.8k | （无法预览） | 将盾斧装填（瓶充能）音效替换为M1加兰德的弹夹“叮”声。 |
| [弓装填（瓶）音效替换 - M1加兰德](https://www.nexusmods.com/monsterhunterwilds/mods/208)<br><sub>Bow Reload (Coating) SFX Replacement - M1 Garand</sub> | 1.0.1 | 2025-03-08  | 57 / 2.4k | （无法预览） | 将弓装填瓶的音效替换为M1加兰德的弹夹“叮”声。 |
| [终焉星与巨戟龙的Miku Miku Beam](https://www.nexusmods.com/monsterhunterwilds/mods/3893)<br><sub>MIKU MIKU BEAM for Omega and Gogmazios</sub> | 2.0 | 2026-05-12 ✅ | 55 / 2.3k | `em0166_00_0`<br>`em0166_00_shell`<br>`gm577_000_00` | 为终焉星和巨戟龙加入初音未来的“Miku Miku Beam”。 |
| [吹雪呼喊FuwaMoco替换口哨](https://www.nexusmods.com/monsterhunterwilds/mods/1140)<br><sub>Replace Hunter Whistle With Fubuki Yelling FuwaMoco</sub> | 1.1a | 2025-03-23  | 50 / 1.4k | `human_common_foley` | 将呼叫赛克雷特与快速旅行翼龙的口哨替换为白上吹雪呼喊FuwaMoco的语音。 |
| [昴呼喊奏替换口哨](https://www.nexusmods.com/monsterhunterwilds/mods/952)<br><sub>Replace Hunter Whistle With Subaru Yelling Kanade</sub> | 1.1a | 2025-03-23  | 48 / 1.6k | `human_common_foley` | 将呼叫赛克雷特与快速旅行翼龙的口哨替换为大空昴呼喊音乃濑奏的语音。 |
| [狩猎笛正义 - 提高狩猎笛音量](https://www.nexusmods.com/monsterhunterwilds/mods/3070)<br><sub>JusticeForHuntingHorns - Make Hunting Horns Louder</sub> | 4.0.1 | 2025-12-25 ✅ | 44 / 1.8k | `it0500_0000_m`<br>`it0500_0001_m`<br>`it0500_0002_m`<br>`it0500_0003_m` … | 所有狩猎笛旋律音量提高15dB。 |
| [火龙与雌火龙咆哮替换 - 世界与旧世代版](https://www.nexusmods.com/monsterhunterwilds/mods/528)<br><sub>Rathalos and Rathian Roar Replacement - MH World and Pre 5th Gen</sub> | 1.0 | 2025-03-16  | 37 / 1.1k | `em0001_00_0`<br>`em0002_50_0` | 将火龙与雌火龙的咆哮替换为世界版或第五世代之前的旧版咆哮，分文件提供。 |
| [比利王 Get Your Ass Back Here 赛克雷特呼叫](https://www.nexusmods.com/monsterhunterwilds/mods/1515)<br><sub>Van Darkholme - Get Your Ass Back Here - Seikret call</sub> | 1.0.0 | 2025-04-03  | 36 / 1.0k | `human_common_foley` | 将呼叫赛克雷特的声音替换为Van Darkholme的“Get Your Ass Back Here”语音。 |
| [绚辉与希望狩猎笛初音未来音效](https://www.nexusmods.com/monsterhunterwilds/mods/898)<br><sub>Hatsune Miku on artian and hope hunting horn</sub> | 1 | 2025-03-18  | 34 / 1.7k | `it0500_0004_m`<br>`it0500_0014_m` | 将绚辉和/或希望狩猎笛的音效替换为Frontier联动的初音未来音效。 |
| [曼波回复药（音效）](https://www.nexusmods.com/monsterhunterwilds/mods/4180)<br><sub>Mambo potion (sound)</sub> | 1.0 | 2026-03-22 ✅ | 30 / 1.5k | `acc002_010` | 饮用任何药剂时加入“曼波”音效。 |
| [Biboo呼喊Kaela替换口哨](https://www.nexusmods.com/monsterhunterwilds/mods/1142)<br><sub>Replace Hunter Whistle With Biboo Yelling Kaela</sub> | 1.1a | 2025-03-23  | 29 / 677 | `human_common_foley` | 将呼叫赛克雷特与快速旅行翼龙的口哨替换为Biboo呼喊Kaela的语音。 |
| [Faint.mp3](https://www.nexusmods.com/monsterhunterwilds/mods/1154) | 1.0 | 2025-03-23  | 28 / 1.8k | `fate`<br>`fate` | 一组猫车（力尽）音效合集。 |
| [关闭烟花音效](https://www.nexusmods.com/monsterhunterwilds/mods/4058)<br><sub>No Fireworks Sound</sub> | 1.0 | 2026-03-01 ✅ | 25 / 929 | `gm253_00x_cmn`<br>`gm253_00x_cmn_02_00` | 静音所有节庆烟花音效。 |
| [黑蚀龙路易吉惨叫咆哮](https://www.nexusmods.com/monsterhunterwilds/mods/430)<br><sub>Gore Magala Luigi Wega Roar</sub> | 1.0 | 2025-03-09  | 22 / 784 | `em0071_00_0` | 将黑蚀龙的咆哮替换为路易吉洋馆的惨叫梗音。 |
| [Mecha的怪物音频微调](https://www.nexusmods.com/monsterhunterwilds/mods/2018)<br><sub>Mecha's Minute Monster Audio Tweaks</sub> | Update-1 | 2026-09-12 ✅ | 22 / 693 | （无法预览） | 按个人喜好调整游戏音频，目前仅包含怪物音频调整。 |
| [多种怪物狩猎笛初音未来音效](https://www.nexusmods.com/monsterhunterwilds/mods/975)<br><sub>Hatsune Miku on various monster hunting horn from mh frontier</sub> | v1 | 2025-03-19  | 19 / 1.1k | `it0500_0011_m`<br>`it0500_0012_m`<br>`it0500_0024_m` | 将黑蚀龙、铠龙和Ajarakan狩猎笛音效替换为Frontier联动的初音未来音效。 |
| [终焉星梗音效](https://www.nexusmods.com/monsterhunterwilds/mods/4149)<br><sub>Memes for Omega Planetes</sub> | 2.1 | 2026-05-12 ✅ | 18 / 976 | `em0166_00_0`<br>`em0166_00_shell`<br>`gm577_000_00` | 为终焉星加入各种梗，让战斗不那么紧张。 |
| [梗咆哮替换音爆弹、闪光弹与大粪臭弹](https://www.nexusmods.com/monsterhunterwilds/mods/1101)<br><sub>Meme roar replace Screamer Pod Flash Pod and Large Dung Pod</sub> | 1.0 | 2025-03-22  | 16 / 636 | `human_slinge_shell` | 用野兽先辈或otto的吼叫替换功能弹音效，增添趣味。 |
| [海龙咆哮更改](https://www.nexusmods.com/monsterhunterwilds/mods/2905)<br><sub>Lagiacrus's Roar Change Mod</sub> | TU2-v1.0 | 2025-07-17  | 15 / 311 | （无法预览） | 将海龙的咆哮改为MH3与荒野版本的混合。 |
| [Korone Eekum Bokum采集音效](https://www.nexusmods.com/monsterhunterwilds/mods/2339)<br><sub>Korone Eekum Bokum Gather Sound</sub> | 1.0 | 2026-07-27 ✅ | 14 / 398 | （无法预览） | 用Korone的班卓熊与卡祖伊音效替换采集音效。 |
| [怪物咆哮更改 by Blacktuna13](https://www.nexusmods.com/monsterhunterwilds/mods/4630)<br><sub>Monster Roar Change by Blacktuna13</sub> | v1.1 | 2026-07-21 ✅ | 13 / 765 | （无法预览） | 修改部分大型怪物的咆哮，目前包括雌火龙/火龙、千刃龙、G.Fluger蛮颚龙和G.火龙。 |
| [WhatsApp赛克雷特口哨](https://www.nexusmods.com/monsterhunterwilds/mods/1234)<br><sub>Whatsapp Seikret Whistle</sub> | 1.0.0 | 2025-03-25  | 11 / 630 | `human_common_foley` | 将呼叫赛克雷特等游戏内口哨替换为WhatsApp通知音。 |
| [回复药与狩猎笛回复耳鸣减弱](https://www.nexusmods.com/monsterhunterwilds/mods/2058)<br><sub>Monster Hunter Potion and Regen Ringing sound dampening</sub> | 1.0 | 2025-04-23  | 10 / 185 | `human_common_effect` | 减弱饮用回复药或狩猎笛回复旋律后出现的高频鸣响声。 |
| [Baelz呼喊Bijou替换口哨](https://www.nexusmods.com/monsterhunterwilds/mods/1141)<br><sub>Replace Hunter Whistle With Hakos Baelz Yelling Koseki Bijou</sub> | 1.1a | 2025-03-23  | 9 / 448 | `human_common_foley` | 将呼叫赛克雷特与快速旅行翼龙的口哨替换为Hakos Baelz呼喊古石Bijou的语音。 |
| [静音吉他与水枪](https://www.nexusmods.com/monsterhunterwilds/mods/3150)<br><sub>Mute Guitar and Watergun</sub> | 0.3 | 2025-11-20  | 6 / 140 | `human_gesture_music_02_00`<br>`human_gesture_shell_02_00` | 静音Fender吉他与水枪的手势音效。 |
| [恢复斩击斧属性解放斩与零距离解放音效特效](https://www.nexusmods.com/monsterhunterwilds/mods/2234)<br><sub>restore SFX and VFX on Switch Axe ED and ZSD</sub> | 1.0 | 2025-07-03  | 5 / 242 |  | 恢复斩击斧属性解放斩与零距离属性解放斩被卡普空改动的音效和特效。 |
| [终焉星小型机皮克敏音效](https://www.nexusmods.com/monsterhunterwilds/mods/4635)<br><sub>Pikmin Sounds for Omega Micros</sub> | 1.0 | 2026-07-14 ✅ | 5 / 208 | （无法预览） | 将Omega Micros的生成、攻击和死亡音效替换为皮克敏的音效。 |
| [耻辱之钟](https://www.nexusmods.com/monsterhunterwilds/mods/926)<br><sub>Shame Bell</sub> | 1 | 2025-03-18  | 4 / 69 | `it0500_0009_m` | 为铃铛狩猎笛加入《权力的游戏》经典场景中的“Shame”钟声。 |
| [大金刚国度2过关曲替换Ajarakan狩猎笛](https://www.nexusmods.com/monsterhunterwilds/mods/2798)<br><sub>Donkey Kong Country 2 Stage Clear fanfare over Ajarakan Hunting Horn</sub> | 1.0 | 2025-07-03  | 4 / 103 | `it0500_0012_m` | 将Ajarakan狩猎笛音频替换为大金刚国度2的过关号角曲。 |
| [烦人音效去除](https://www.nexusmods.com/monsterhunterwilds/mods/2247)<br><sub>Begone Annoying Sounds</sub> | 0.5 | 2025-05-09  | 3 / 158 |  | 一组杂项音频模组，移除游戏中吸溜声等令人烦躁的噪音。 |
| [Bennett - 我拿了10万金币PON](https://www.nexusmods.com/monsterhunterwilds/mods/3573)<br><sub>Bennett - I got 100000 Zenny PON</sub> | TU3-v1.0 | 2025-11-26  | 2 / 101 | `gui_cmn` | 恶搞音频模组，梗源自《魔鬼司令》中约翰·马特里克斯的台词“你从Arius那拿了多少钱？”。 |
| [Hero的枪管与消音器切换](https://www.nexusmods.com/monsterhunterwilds/mods/3813)<br><sub>Hero's Barrel and Silencer Swapper</sub> | 1.0.0 | 2026-01-18 ✅ | 2 / 59 |  | 游戏中轻弩有消音器却无法显示，本模组可在枪管与消音器外观之间切换。 |
| [赛克雷特汽车音效](https://www.nexusmods.com/monsterhunterwilds/mods/3851)<br><sub>Seikret Car Sounds</sub> | 1.11 | 2026-01-28 ✅ | 0 / 1.4k | `porter_cmn_voice_m` | 为赛克雷特(坐骑)添加汽车音效，用于搭配QuirklessStoner的Seikret Forklift模组。 |
| [仅剩一命时自动播放Rain Love](https://www.nexusmods.com/monsterhunterwilds/mods/5078)<br><sub>auto play rain love when just a life</sub> | 1 | 2026-10-07 ✅ | 0 / 1 | （无法预览） | 参考B站@Arcueid_Ciel的视频，当只剩最后一次猫车机会时循环播放歌曲Rain Love。 |
| [钢管落地音效](https://www.nexusmods.com/monsterhunterwilds/mods/5095)<br><sub>Steel pipe dropping sound</sub> | 1 | 2026-10-09 ✅ | 0 / 33 | （无法预览） | 将弹刀音效替换为钢管落地的声音。 |

<a id="i"></a>
## I. 通用热门：前置 / 工具 / UI / 性能 / 玩法（143）

非音频、非太刀专属。分类为工具、界面、玩法、画面、杂项、技能、道具、怪物，且点赞数 ≥ 300 的 mod，选 mod 时可作参考。

| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |
|---|---|---|---|---|---|
| [REFramework](https://www.nexusmods.com/monsterhunterwilds/mods/93) | Nightly01240 | 2026-02-25 ✅ | 29.3k / 2824.3k |  | 带强大Lua脚本API的模组框架，附带DLL/ReShade崩溃修复、性能修复、自由视角、时间缩放、FOV、超宽屏及开发工具。 |
| [CatLib](https://www.nexusmods.com/monsterhunterwilds/mods/65) | 1.14.0 | 2026-08-21 ✅ | 16.0k / 1756.8k |  | 作者模组共用的实用脚本合集。 |
| [绚辉武器编辑器](https://www.nexusmods.com/monsterhunterwilds/mods/196)<br><sub>Artian Editor</sub> | 2.3.0 | 2026-08-21 ✅ | 8.5k / 598.1k | （无法预览） | 可编辑绚辉武器。 |
| [商店调整 - 商店售卖全部道具](https://www.nexusmods.com/monsterhunterwilds/mods/30)<br><sub>Shop Tweaks - All Items in the Shop</sub> | 1.11 | 2026-02-18 ✅ | 7.8k / 704.9k |  | 提供多种不同商品列表，调整商店售卖的道具。 |
| [怪物弱点图标提示](https://www.nexusmods.com/monsterhunterwilds/mods/367)<br><sub>Monster Weakness Icon Indicator</sub> | 1.042.00.02 | 2026-09-06 ✅ | 7.8k / 610.1k | （无法预览） | 以图标显示怪物的属性弱点。 |
| [MHWilds 信息覆盖层](https://www.nexusmods.com/monsterhunterwilds/mods/81)<br><sub>MHWilds Overlay</sub> | 1.14 | 2026-02-24 ✅ | 7.2k / 705.0k |  | 显示首领血量、DPS、统计数据和技能报告的覆盖层界面。 |
| [持续增益光效移除](https://www.nexusmods.com/monsterhunterwilds/mods/141)<br><sub>Persistent Buff Glow Removal</sub> | 2.0.3 | 2025-07-08  | 4.9k / 279.5k |  | REFramework脚本，可配置地屏蔽猎人身上由道具/技能/武器产生的发光效果及其他碍眼特效。 |
| [无限次角色与随从艾露猫编辑](https://www.nexusmods.com/monsterhunterwilds/mods/133)<br><sub>Unlimited Character and Palico Edits</sub> | 1.0 | 2025-03-01  | 4.7k / 228.3k |  | 可无限次修改角色和随从艾露猫的外观。 |
| [DirectStorage 1.2.3升级 - IO卡顿修复](https://www.nexusmods.com/monsterhunterwilds/mods/127)<br><sub>DirectStorage 1.2.2 Upgrade to 1.2.3 - IO Stutter Fix</sub> | 1 | 2025-03-01  | 4.6k / 233.1k |  | （已不再需要）将DirectStorage DLL替换为1.2.3版本，解决资源与贴图解压加载导致的严重I/O卡顿。 |
| [禁用后处理效果](https://www.nexusmods.com/monsterhunterwilds/mods/221)<br><sub>Disable Post-Processing Effects</sub> | 2.1.0 | 2026-09-06 ✅ | 4.1k / 290.2k | （无法预览） | 禁用或调整TAA、色彩校正、锐化、胶片颗粒等各类后处理效果。 |
| [自动补充道具袋](https://www.nexusmods.com/monsterhunterwilds/mods/38)<br><sub>Auto Item Pouch Restock</sub> | 1.6 | 2025-07-03  | 4.0k / 240.0k |  | 自动按上次道具组合补充道具袋和弹药袋，或仅补满当前道具袋与弹药袋。 |
| [荒野优化器 - FPS提升与稳定性增强](https://www.nexusmods.com/monsterhunterwilds/mods/91)<br><sub>Wilds OPTIMIZER FPS BOOST LOW CPU CLEANER VISUALS AND BETTER STABILITY</sub> | 1.0 | 2025-03-02  | 4.0k / 260.7k |  | 提升游戏性能，降低CPU占用，使画面更干净并增强稳定性。 |
| [道具价格调整 - 1z买入99999z卖出](https://www.nexusmods.com/monsterhunterwilds/mods/26)<br><sub>Item Cost Tweaks - Buy for 1z sell for 99999z</sub> | 1.9 | 2026-02-18 ✅ | 3.7k / 264.3k |  | 提供多种道具买入与卖出价格的调整方案。 |
| [自动领取](https://www.nexusmods.com/monsterhunterwilds/mods/589)<br><sub>Auto Collect</sub> | 2.01 | 2025-10-16  | 3.5k / 174.1k |  | 自动领取素材采集委托、祭典分享、巢中杂物、普吉及食料配给所的物品。 |
| [Wilds Rehydrated 画面增强](https://www.nexusmods.com/monsterhunterwilds/mods/50)<br><sub>Wilds Rehydrated</sub> | 5.0 | 2026-09-08 ✅ | 3.1k / 232.2k | （无法预览） | 为荒野带来更浓郁的色彩、真实的阴影和更生动的画面效果。 |
| [跳过开场Logo](https://www.nexusmods.com/monsterhunterwilds/mods/72)<br><sub>Skip Intro Logos</sub> | 1.0 | 2025-02-28  | 3.1k / 129.4k |  | 跳过游戏启动时的开场Logo。 |
| [无制作需求](https://www.nexusmods.com/monsterhunterwilds/mods/29)<br><sub>No Crafting Requirements</sub> | 1.11 | 2026-08-04 ✅ | 2.9k / 227.9k | （无法预览） | 移除多种物品的制作需求。 |
| [道具编辑器](https://www.nexusmods.com/monsterhunterwilds/mods/114)<br><sub>Item Editor</sub> | 1.3.1 | 2025-12-26 ✅ | 2.9k / 205.3k |  | 可添加金钱、点数、券、道具和装饰品，并支持无限道具或修改道具袋上限。 |
| [3倍怪物素材掉落](https://www.nexusmods.com/monsterhunterwilds/mods/170)<br><sub>3x Monster Drops</sub> | 1.23-TU3 | 2026-01-04 ✅ | 2.7k / 165.0k |  | 使怪物素材掉落变为2倍或3倍。 |
| [只出皇冠](https://www.nexusmods.com/monsterhunterwilds/mods/152)<br><sub>Crown Only</sub> | 1.2 | 2025-03-13  | 2.6k / 116.3k |  | 使怪物只生成最大或最小尺寸，即金冠与小冠。 |
| [护石编辑器](https://www.nexusmods.com/monsterhunterwilds/mods/3067)<br><sub>Charm Editor</sub> | 1.3.0 | 2026-08-21 ✅ | 2.5k / 210.7k | （无法预览） | 可编辑护石。 |
| [轻松钓大鱼 - 钓鱼作弊](https://www.nexusmods.com/monsterhunterwilds/mods/199)<br><sub>Easy Big Game - Be a True Master Angler - Fishing Cheats</sub> | 1.1 | 2025-03-12  | 2.3k / 75.9k |  | 让钓大鱼变得轻松，提供无限钓线张力，并可选快速收杆。 |
| [禁用镜头畸变](https://www.nexusmods.com/monsterhunterwilds/mods/245)<br><sub>Disable Lens Distortion</sub> | 1.3 | 2025-12-19 ✅ | 2.1k / 105.0k |  | 禁用镜头畸变效果的REFramework脚本。 |
| [REFramework Direct2D](https://www.nexusmods.com/monsterhunterwilds/mods/142) | 1.4.1 | 2025-04-07  | 2.0k / 99.1k |  | 为REFramework添加Direct2D脚本API的插件，需要REFramework 1.5.4及以上版本。 |
| [HunterPie - 覆盖层与辅助工具](https://www.nexusmods.com/monsterhunterwilds/mods/1945)<br><sub>HunterPie - Overlay and Companion</sub> | 2.14.0.415 | 2026-02-16 ✅ | 1.8k / 129.2k |  | 现代、稳定、简洁的怪物猎人系列覆盖层工具，集成Discord动态状态显示。 |
| [禁用近距离虚化与镜头拉近](https://www.nexusmods.com/monsterhunterwilds/mods/984)<br><sub>Disable Near Fade and Camera Zoom In</sub> | 1.2.1 | 2025-04-18  | 1.8k / 65.9k |  | 禁用敌人/地形/NPC近距离虚化隐形，以及战斗中的镜头拉近。 |
| [任务报酬2倍](https://www.nexusmods.com/monsterhunterwilds/mods/200)<br><sub>Quest Reward Up 2x</sub> | 1.7-TU4-ATArkveld | 2026-02-25 ✅ | 1.8k / 111.6k |  | 将任务报酬提升为2倍或5倍。 |
| [无限调查任务](https://www.nexusmods.com/monsterhunterwilds/mods/212)<br><sub>Infinite Investigations</sub> | 1.0 | 2025-04-04  | 1.8k / 84.3k |  | 接取调查任务后不再消耗该任务。 |
| [更佳镜头距离](https://www.nexusmods.com/monsterhunterwilds/mods/431)<br><sub>Better Camera Distance</sub> | 3.6 | 2025-04-16  | 1.8k / 88.2k |  | 为REFramework添加镜头距离和FOV调节滑块。 |
| [MHWilds 皇冠助手](https://www.nexusmods.com/monsterhunterwilds/mods/475)<br><sub>MHWilds CrownHelper</sub> | v1.0.0 | 2025-04-19  | 1.8k / 68.7k |  | 提示怪物皇冠与尺寸，并显示皇冠成就进度概览的简易UI工具。 |
| [免费午餐](https://www.nexusmods.com/monsterhunterwilds/mods/228)<br><sub>Free Lunch</sub> | 1.1 | 2025-04-04  | 1.7k / 65.8k |  | 总能收到村民的用餐邀请，且大集会所食堂餐点免费。 |
| [任意武器幻化](https://www.nexusmods.com/monsterhunterwilds/mods/496)<br><sub>Layer Any Weapon</sub> | 1.4 | 2025-08-13  | 1.6k / 71.0k |  | 可将任意武器设为幻化武器。 |
| [自动冷却衣装](https://www.nexusmods.com/monsterhunterwilds/mods/80)<br><sub>Auto Cooldown Mantles</sub> | 1.0 | 2025-02-28  | 1.6k / 60.5k |  | 完成任务后自动重置衣装冷却时间。 |
| [MHWs 贴图解压工具](https://www.nexusmods.com/monsterhunterwilds/mods/951)<br><sub>MHWs Tex Decompressor Tool</sub> | 0.3.0 | 2026-02-19 ✅ | 1.5k / 76.5k |  | 生成未压缩贴图的补丁pak，可能提升帧率稳定性，但会占用更多磁盘空间。 |
| [道具箱编辑器](https://www.nexusmods.com/monsterhunterwilds/mods/102)<br><sub>Item Box Editor</sub> | v2.0.2 | 2026-03-09 ✅ | 1.5k / 143.3k |  | 怪物猎人荒野的道具箱编辑器。 |
| [跳过道具袋替换提示（已弃用）](https://www.nexusmods.com/monsterhunterwilds/mods/157)<br><sub>Deprecated - Skip Pouch Replace Prompt</sub> | 1.0.2 | 2025-04-04  | 1.5k / 52.3k |  | REFramework脚本，道具袋已满时拾取新道具会直接放入野外道具袋，不再弹出提示。 |
| [自动跳过击杀镜头（快速返回）](https://www.nexusmods.com/monsterhunterwilds/mods/617)<br><sub>Auto Skip Kill Cam (Fast Return)</sub> | 2.4.7 | 2026-09-13 ✅ | 1.5k / 74.6k | （无法预览） | 跳过完成任务后重复播放的演出画面。 |
| [伤害调整器](https://www.nexusmods.com/monsterhunterwilds/mods/34)<br><sub>Damage Adjuster</sub> | 1.01 | 2025-12-30 ✅ | 1.4k / 102.7k |  | 通过倍率调整你造成的伤害。 |
| [精简环境 OGU - 老显卡性能模组（停止支持）](https://www.nexusmods.com/monsterhunterwilds/mods/234)<br><sub>(End of Support) Lite Environment - OGU (Old Gens Unbloat) - Performance mod</sub> | 2.2.2 | 2025-12-16 ✅ | 1.4k / 90.1k |  | REFramework脚本，禁用风模拟、全局光照和体积雾，解决老旧显卡的严重性能问题。 |
| [Buffer 全能增益](https://www.nexusmods.com/monsterhunterwilds/mods/299)<br><sub>Buffer</sub> | v1.1.6 | 2026-09-03 ✅ | 1.4k / 113.1k | （无法预览） | 提供满血、满耐力、无敌、即时冷却、无限道具与弹药，并强化武器、充能槽及解除各武器限制。 |
| [_ScriptCore](https://www.nexusmods.com/monsterhunterwilds/mods/87) | 1.2.02 | 2025-10-14  | 1.4k / 56.5k |  | 脚本模组的实用函数合集，如用于跨脚本管理热键的hotkeys.lua。 |
| [合法极限怪物尺寸 - 金冠银冠](https://www.nexusmods.com/monsterhunterwilds/mods/28)<br><sub>Min-Max Legal Random Monster Sizes - Gold - Silver Crowns</sub> | 1.7 | 2025-12-22 ✅ | 1.4k / 57.2k |  | 修改游荡怪物的随机尺寸，保证以五五开概率出现合法范围内的最大或最小尺寸。 |
| [隐形衣装](https://www.nexusmods.com/monsterhunterwilds/mods/18)<br><sub>Invisible Mantles</sub> | 1.1.0 | 2026-01-05 ✅ | 1.3k / 54.5k |  | REFramework脚本，装备衣装时隐藏其常驻模型。 |
| [免费制作](https://www.nexusmods.com/monsterhunterwilds/mods/154)<br><sub>Free Craft</sub> | 1.0 | 2025-03-02  | 1.3k / 70.3k |  | 免费制作、强化防具、炼金和熔炼。 |
| [调整游戏内体积雾](https://www.nexusmods.com/monsterhunterwilds/mods/455)<br><sub>Tweak In-Game Volumetric Fog(s)</sub> | 1.0.0 | 2025-03-16  | 1.2k / 58.6k |  | REFramework脚本，可调整游戏内体积雾的多项参数，而非直接禁用。 |
| [RenoDX - HDR与SDR修复 - 色调映射与调色](https://www.nexusmods.com/monsterhunterwilds/mods/202)<br><sub>RenoDX - HDR and SDR Fix - Tonemap - Color Grade</sub> | 4.4.2 | 2026-08-04 ✅ | 1.2k / 84.7k | （无法预览） | 重写调色管线以修复SDR/HDR，并添加色调映射、纸白、UI亮度和调色控制。 |
| [更好的装饰品掉落](https://www.nexusmods.com/monsterhunterwilds/mods/283)<br><sub>Better Decoration Drops Wilds</sub> | 1.1 | 2025-03-06  | 1.1k / 48.2k |  | 简单调整装饰品掉落率，使高稀有度装饰品整体上更容易获得。 |
| [任务结束慢动作](https://www.nexusmods.com/monsterhunterwilds/mods/864)<br><sub>End slow motion</sub> | 1.2 | 2026-03-15 ✅ | 1.1k / 41.2k |  | 完成任务后触发持续数秒、可配置的慢动作效果。 |
| [调查任务报酬合法最大化](https://www.nexusmods.com/monsterhunterwilds/mods/661)<br><sub>Legal Max Roll Investigations</sub> | 1.0.10 | 2025-12-27 ✅ | 1.0k / 55.2k |  | 使调查任务始终拥有合法范围内的最大报酬次数。 |
| [自动跳过重复过场](https://www.nexusmods.com/monsterhunterwilds/mods/573)<br><sub>Auto-Skip Repetitive Cutscenes</sub> | 0.3.1 | 2025-04-06  | 1.0k / 42.9k |  | 默认自动跳过工房动画和帐篷/烤肉烹饪动画，还可自定义添加其他条目。 |
| [血条显示](https://www.nexusmods.com/monsterhunterwilds/mods/16)<br><sub>Health Bars</sub> | 0.1.1 | 2025-02-27  | 1.0k / 63.6k |  | 为怪物猎人荒野显示怪物血条的覆盖层。 |
| [自动使用增益道具](https://www.nexusmods.com/monsterhunterwilds/mods/1317)<br><sub>Auto Itembuff</sub> | 1.3 | 2025-12-24 ✅ | 1.0k / 47.9k |  | 接受任务时自动使用增益道具。 |
| [更多安全营地 - 营地永不被破坏](https://www.nexusmods.com/monsterhunterwilds/mods/153)<br><sub>More Safe Spaces - More Camps and They Never Break</sub> | 1.8 | 2026-02-18 ✅ | 945 / 51.7k |  | 使所有营地区域都安全，并可选提高营地基础数量上限。 |
| [道具增益持续时间](https://www.nexusmods.com/monsterhunterwilds/mods/147)<br><sub>Item Buff Duration</sub> | Title-Update-4.1 | 2026-02-18 ✅ | 940 / 48.2k |  | 将寿司鱼、肉干、强走药、鬼人药、硬化药、怪力种子等大部分增益道具持续时间延长至1小时。 |
| [永久活动任务与自定义任务加载器](https://www.nexusmods.com/monsterhunterwilds/mods/1096)<br><sub>Permanent Event Quests and Custom Quest Loader</sub> | v1.12.0 | 2026-09-17 ✅ | 930 / 65.9k |  | 使所有活动任务永久可用，并可创建和加载自定义地图、怪物、天气及报酬的任务。 |
| [隐藏收刀武器](https://www.nexusmods.com/monsterhunterwilds/mods/3)<br><sub>Hide Sheathed Weapons</sub> | 1.5 | 2025-12-28 ✅ | 923 / 41.9k | （无法预览） | 自动隐藏玩家收起状态下的武器。 |
| [高亮敌人伤口与弱点](https://www.nexusmods.com/monsterhunterwilds/mods/67)<br><sub>Highlight Enmey Wounds and Weak Points</sub> | 1.0 | 2025-02-28  | 923 / 47.6k |  | 无需集中模式即可高亮显示敌人的伤口/疤痕和弱点。 |
| [任务窃取者](https://www.nexusmods.com/monsterhunterwilds/mods/899)<br><sub>Quest Stealer</sub> | 1.21 | 2025-05-29  | 913 / 40.4k |  | 加入其他猎人的调查任务后，将该任务添加到你的现地调查任务记录中。 |
| [中文字体支持](https://www.nexusmods.com/monsterhunterwilds/mods/159)<br><sub>Chinese Fonts Support</sub> | 1.1 | 2025-03-04  | 898 / 35.9k |  | 为REFramework添加中文字体支持，解决中文显示为问号的问题。 |
| [荒野GPU与CPU性能优化](https://www.nexusmods.com/monsterhunterwilds/mods/88)<br><sub>optimization for MonsterHunterWilds GPU AND CPU Performance FPS Optimizer</sub> | 0.1 | 2025-03-16  | 871 / 64.2k |  | 优化GPU和CPU占用，适用于6GB显存显卡。 |
| [最大孔位与技能 - 防具武器护石](https://www.nexusmods.com/monsterhunterwilds/mods/23)<br><sub>Max Slots and Skills - Armor and Weapons and Talismans</sub> | 1.11 | 2026-02-18 ✅ | 855 / 133.2k |  | 提供多种选项，使防具/武器的孔位和技能达到最大。 |
| [更快的弹出消息](https://www.nexusmods.com/monsterhunterwilds/mods/520)<br><sub>Faster Popup Messages</sub> | 1.0 | 2025-03-10  | 855 / 33.0k |  | 缩短保存、发布任务等提示消息的显示时间。 |
| [自动用餐](https://www.nexusmods.com/monsterhunterwilds/mods/64)<br><sub>Auto Meal</sub> | 1.4 | 2025-12-25 ✅ | 854 / 54.4k |  | 任务前根据武器类型或装备组合自动食用套餐/村庄料理，并支持无限食物。 |
| [无限烹饪食材](https://www.nexusmods.com/monsterhunterwilds/mods/347)<br><sub>Infinite Cooking Ingredients</sub> | 1.8.1 | 2026-03-05 ✅ | 848 / 45.9k |  | 像其他怪猎作品一样，烹饪食材无限。 |
| [自动关闭推荐弹窗](https://www.nexusmods.com/monsterhunterwilds/mods/446)<br><sub>Auto Close The Recommendation Dialog</sub> | v1.3.4 | 2025-03-16  | 847 / 41.4k |  | 自动关闭游戏中的推荐弹窗。 |
| [提高皇冠怪物出现率](https://www.nexusmods.com/monsterhunterwilds/mods/439)<br><sub>Increased crown monster spawn chance</sub> | 1.0 | 2025-03-11  | 833 / 32.0k |  | 提高皇冠尺寸怪物的出现几率，便于获取金冠成就。 |
| [无色彩滤镜](https://www.nexusmods.com/monsterhunterwilds/mods/516)<br><sub>No Color Filters</sub> | 1.1 | 2025-03-11  | 833 / 37.2k |  | 通过替换LUT文件禁用游戏后处理的色彩滤镜。 |
| [MDF-XL](https://www.nexusmods.com/monsterhunterwilds/mods/125) | 1.5.36 | 2025-10-17  | 822 / 32.2k |  | 强大的实时材质编辑器，带完善的预设系统，可自定义防具和武器外观。 |
| [非战斗时暂停用餐计时](https://www.nexusmods.com/monsterhunterwilds/mods/84)<br><sub>Pause Meal Out of Battle</sub> | 1.0 | 2025-02-28  | 783 / 28.8k |  | 非战斗状态下暂停用餐效果计时，可自由探索世界。 |
| [重洗绚辉武器加成](https://www.nexusmods.com/monsterhunterwilds/mods/1397)<br><sub>Reroll Artian Bonus</sub> | 1.0.4 | 2026-01-18 ✅ | 739 / 31.8k |  | 可重新随机绚辉武器的加成，可单条重洗或以较低价格全部重洗。 |
| [合法极限鱼类尺寸 - 金冠银冠](https://www.nexusmods.com/monsterhunterwilds/mods/27)<br><sub>Min-Max Legal Fish Sizes - Gold - Silver Crowns</sub> | 1.3 | 2025-12-22 ✅ | 738 / 24.4k |  | 修改鱼的尺寸，保证以五五开概率出现合法范围内的最大或最小尺寸。 |
| [无限消耗品](https://www.nexusmods.com/monsterhunterwilds/mods/77)<br><sub>Infinity Consumables</sub> | 1.0 | 2025-02-28  | 736 / 31.5k |  | 使消耗品无限，或修改道具袋中的最大携带数量。 |
| [假玩家光源移除（适用1.042）](https://www.nexusmods.com/monsterhunterwilds/mods/1745)<br><sub>Fake Player Light Remover (Working for 1.042)</sub> | 1.5 | 2026-02-20 ✅ | 735 / 33.1k |  | 移除黑暗处或夜晚时从地面发出的难看光源。 |
| [自动选择最近营地](https://www.nexusmods.com/monsterhunterwilds/mods/3030)<br><sub>Auto-Select Nearest Camp</sub> | 1.0.1 | 2025-08-18  | 728 / 31.7k |  | 接受任务时自动选择最近的出发地点。 |
| [免费休息](https://www.nexusmods.com/monsterhunterwilds/mods/435)<br><sub>Free Rest</sub> | 1.0 | 2025-03-13  | 724 / 24.4k |  | 休息无需支付费用。 |
| [双刀与弓自动闪避攻击](https://www.nexusmods.com/monsterhunterwilds/mods/290)<br><sub>Dual Blades and Bow auto dodge attacks</sub> | 3.3 | 2025-03-13  | 722 / 46.6k |  | 双刀和弓自动触发完美回避（蓝闪）攻击，大剑版本已移至其他模组。 |
| [武器 - 最大紫斩味](https://www.nexusmods.com/monsterhunterwilds/mods/31)<br><sub>Weapons - Max Purple Sharpness</sub> | 1.8 | 2026-02-18 ✅ | 708 / 36.6k |  | 使所有武器拥有满紫色斩味。 |
| [仅出R8护石](https://www.nexusmods.com/monsterhunterwilds/mods/3068)<br><sub>R8 Charm Only</sub> | 1.0 | 2025-08-13  | 689 / 25.4k |  | 怪物报酬中的R9护石全部改为R8。 |
| [无限角色编辑券](https://www.nexusmods.com/monsterhunterwilds/mods/106)<br><sub>infinite character make ticked</sub> | ver1.0 | 2025-03-02  | 675 / 32.1k |  | 角色编辑券无限，需要REFramework。 |
| [怪物无视营地](https://www.nexusmods.com/monsterhunterwilds/mods/162)<br><sub>Monster Ignore Camp</sub> | 1.02 | 2025-03-13  | 648 / 24.6k |  | 怪物将无视你的营地。 |
| [超强支援猎人](https://www.nexusmods.com/monsterhunterwilds/mods/2361)<br><sub>very powerful support Hunters</sub> | Ver.1.042.00.02 | 2026-03-02 ✅ | 648 / 44.6k |  | NPC不再是累赘，能像真实玩家一样战斗。 |
| [自动补给](https://www.nexusmods.com/monsterhunterwilds/mods/66)<br><sub>Auto Restock</sub> | 1.3 | 2025-12-25 ✅ | 627 / 37.9k |  | 任务前根据武器类型或装备组合自动补充道具。 |
| [武器与防具编辑器](https://www.nexusmods.com/monsterhunterwilds/mods/115)<br><sub>Weapon and Armor Editor</sub> | 1.0 | 2025-03-01  | 590 / 30.2k |  | 武器和防具编辑器，还支持全局加值与倍率。 |
| [禁用镜头重叠透明](https://www.nexusmods.com/monsterhunterwilds/mods/1047)<br><sub>Disable Camera Overlap Transparency</sub> | 1.5.3 | 2025-03-25  | 590 / 19.9k |  | 禁用镜头近距离重叠导致的透明、淡出、模糊或隐形效果。 |
| [更多素材采集](https://www.nexusmods.com/monsterhunterwilds/mods/392)<br><sub>More Material Retrieval</sub> | 1.0 | 2026-02-21 ✅ | 584 / 25.4k |  | 娜塔的素材采集数量提升为2倍/3倍/5倍。 |
| [大工房更多道具](https://www.nexusmods.com/monsterhunterwilds/mods/387)<br><sub>More Items from Large Workshop</sub> | 1.0 | 2025-12-25 ✅ | 566 / 22.3k |  | 大工房（祭典分享）给予的道具变为2倍/5倍/10倍。 |
| [自动修复营地](https://www.nexusmods.com/monsterhunterwilds/mods/70)<br><sub>Auto Fix Camps</sub> | 1.0 | 2025-02-28  | 563 / 27.4k |  | 打开地图时自动修复所有营地。 |
| [所有营地可快速移动](https://www.nexusmods.com/monsterhunterwilds/mods/1041)<br><sub>All Campsite Fast Travelable</sub> | 1.1 | 2025-03-21  | 560 / 18.2k |  | 使所有已发现的营地设置候选地都可快速移动。 |
| [荒野Reshade - 自然增强](https://www.nexusmods.com/monsterhunterwilds/mods/53)<br><sub>WILDS Reshade - Natural Enhancements</sub> | 3.1 | 2025-09-20  | 556 / 38.4k |  | 注重可玩性的Reshade预设，性能损耗约1-3%，细微增强色彩平衡、对比度和清晰度，画面更自然。 |
| [MHWs Lua骨骼系统](https://www.nexusmods.com/monsterhunterwilds/mods/2112)<br><sub>LUA Bone System for MHWs</sub> | 1.42 | 2026-08-25 ✅ | 555 / 35.6k | （无法预览） | 分离自定义骨骼与面部网格的脚本，可同时安装多个改骨骼和改脸模组。 |
| [精确技能描述](https://www.nexusmods.com/monsterhunterwilds/mods/2307)<br><sub>Accurate Skill Descriptions</sub> | 1.46 | 2026-06-01 ✅ | 545 / 28.3k |  | 修改文本，使套装/系列加成、技能、衣装、料理技能和道具的描述更准确详细。 |
| [过时模组检测器（黑屏修复）](https://www.nexusmods.com/monsterhunterwilds/mods/1651)<br><sub>Obsolete Mod Detector (Blackscreen Fixer)</sub> | 1.4.3.0 | 2026-08-04 ✅ | 538 / 25.1k | （无法预览） | 检测与当前MHWS版本不兼容的旧版/过时模组文件。 |
| [自动隐藏衣装](https://www.nexusmods.com/monsterhunterwilds/mods/78)<br><sub>Auto Hide Mantles</sub> | 1.1 | 2025-12-22 ✅ | 534 / 20.9k |  | 自动隐藏角色身上的衣装。 |
| [烹饪不消耗食材](https://www.nexusmods.com/monsterhunterwilds/mods/433)<br><sub>Cook Without Using Ingredients</sub> | 1.1 | 2025-04-04  | 534 / 19.8k |  | 烹饪时不消耗食材，现已包含食堂餐券。 |
| [道具增益延长](https://www.nexusmods.com/monsterhunterwilds/mods/76)<br><sub>Item Buff Extender</sub> | 1.0 | 2025-02-28  | 523 / 23.1k |  | 延长道具增益效果的最大持续时间。 |
| [4倍猎人等级点数（HR）](https://www.nexusmods.com/monsterhunterwilds/mods/460)<br><sub>4x Hunting Rank Points (HR)</sub> | 1.00 | 2025-03-09  | 521 / 33.2k |  | 大多数狩猎获得约4倍的HR点数。 |
| [替换DirectStorage DLL文件](https://www.nexusmods.com/monsterhunterwilds/mods/2003)<br><sub>Replace Direct Storage DLL Files</sub> | 1.3.0 | 2026-03-12 ✅ | 521 / 20.7k |  | 将DirectStorage DLL替换为1.3.0版本，改善I/O卡顿并提升帧数。 |
| [TU4.2.0.2 一体化性能包](https://www.nexusmods.com/monsterhunterwilds/mods/2881)<br><sub>TU4.2.0.2 All in one (DirectStorage 1.3.2 DLSS 310.9.1 SL 2.14.1 FSR 4.1.1 XeSS 2.0.2.68) Updated Reframework</sub> | 3.9.1 | 2026-09-16 ✅ | 520 / 56.3k |  | 整合DirectStorage 1.3.2、DLSS、XeSS、FSR 4.1.1及更新版REFramework，修复部分卡顿并改进超分，兼容Linux。 |
| [无按键延迟](https://www.nexusmods.com/monsterhunterwilds/mods/689)<br><sub>No KeyLag</sub> | 1.1.1 | 2025-09-30  | 518 / 21.6k |  | 移除或自定义回避和攻击的按键延迟。 |
| [YURI 覆盖层](https://www.nexusmods.com/monsterhunterwilds/mods/62)<br><sub>YURI Overlay</sub> | 1.5.7 | 2026-03-07 ✅ | 511 / 48.6k |  | 展示怪物、环境生物、玩家和伤害等内部数据的覆盖层模组，界面高度可自定义。 |
| [自定义自由任务](https://www.nexusmods.com/monsterhunterwilds/mods/464)<br><sub>CustomFreeQuest</sub> | 1.0.0 | 2025-03-19  | 502 / 24.1k |  | 自定义自由任务和调查任务的内容与报酬，支持联机。 |
| [无限弩弹药（无脚本）](https://www.nexusmods.com/monsterhunterwilds/mods/214)<br><sub>Infinite Bowgun ammo(no script)</sub> | 1.8 | 2026-02-18 ✅ | 501 / 27.9k |  | 像通常弹、贯通弹、散弹那样，使所有弹药无限。 |
| [一颗装饰品满级技能](https://www.nexusmods.com/monsterhunterwilds/mods/161)<br><sub>One Deco to Max Skill</sub> | 1.3 | 2025-12-22 ✅ | 500 / 23.4k |  | 一颗装饰品即可使技能达到满级。 |
| [增强伤害数字](https://www.nexusmods.com/monsterhunterwilds/mods/262)<br><sub>Enhanced Damage Numbers</sub> | 1.6 | 2025-12-22 ✅ | 500 / 28.0k |  | 根据实际肉质及弱点特效、心眼触发改变伤害数字颜色，并显示物理+属性伤害详情等。 |
| [EasyPatcher](https://www.nexusmods.com/monsterhunterwilds/mods/169) | 1.0 | 2025-03-03  | 495 / 22.9k |  | 提升游戏性能并减少卡顿。 |
| [REFramework 添加中文字体](https://www.nexusmods.com/monsterhunterwilds/mods/226)<br><sub>REFramework Add Chinese Fonts</sub> | 1.0 | 2025-03-05  | 482 / 15.6k |  | 为REFramework添加简体中文字体支持。 |
| [一颗珠子满级技能](https://www.nexusmods.com/monsterhunterwilds/mods/151)<br><sub>1 Gem Max Skill</sub> | 1.0 | 2025-04-05  | 468 / 21.1k |  | 单颗装饰品即可使技能达到满级。 |
| [自动限时悬赏](https://www.nexusmods.com/monsterhunterwilds/mods/1381)<br><sub>Auto Limited Bounties</sub> | 1.11 | 2026-01-11 ✅ | 466 / 17.3k |  | 自动接取并报告限时配信悬赏。 |
| [更好的营地](https://www.nexusmods.com/monsterhunterwilds/mods/155)<br><sub>Better Camps</sub> | 1.0 | 2025-03-02  | 461 / 21.2k |  | 增加营地数量上限，并更快修复损坏的营地。 |
| [1小时衣装](https://www.nexusmods.com/monsterhunterwilds/mods/201)<br><sub>1 Hour Mantles</sub> | 1.0 | 2025-03-06  | 461 / 21.2k |  | 使所有衣装持续1小时且冷却仅10秒，支持Fluffy Mod Manager。 |
| [DLC检查性能修复（已弃用）](https://www.nexusmods.com/monsterhunterwilds/mods/3796)<br><sub>DLC Check Performance Fix (Deprecated - Fixed in v1.040.03.01)</sub> | 1.0 | 2026-01-15 ✅ | 453 / 18.5k |  | 原生C++补丁，缓存DLC检查结果以减少每帧数百次检查、提升性能，v1.040.03.01已官方修复。 |
| [自动支援船](https://www.nexusmods.com/monsterhunterwilds/mods/1380)<br><sub>Auto Support Ship</sub> | 1.01 | 2025-04-23  | 443 / 12.7k |  | 自动购买支援船的道具和武器。 |
| [更多画面选项](https://www.nexusmods.com/monsterhunterwilds/mods/816)<br><sub>More graphics options</sub> | 2.0 | 2026-04-22 ✅ | 441 / 31.1k |  | REFramework脚本，可调整包括环境细节在内的多种画面选项以提升性能。 |
| [瞬间钩爪采集与改良捕获网](https://www.nexusmods.com/monsterhunterwilds/mods/2152)<br><sub>Instant Hook Slinger and Better Capture Net</sub> | 2.1 | 2025-07-03  | 431 / 13.8k |  | 使钩爪弹射器瞬间完成采集，并改良捕获网。 |
| [MHWS-Editor](https://www.nexusmods.com/monsterhunterwilds/mods/32) | 1.6.3.0 | 2026-08-11 ✅ | 414 / 27.4k | （无法预览） | 用于编辑游戏资源中各类用户数据文件的工具。 |
| [卸下所有装饰品](https://www.nexusmods.com/monsterhunterwilds/mods/1343)<br><sub>Remove All Decorations</sub> | 1.0 | 2025-03-28  | 413 / 8.0k |  | 一键卸下所有装备和防具上的装饰品。 |
| [最大化所有回避动作](https://www.nexusmods.com/monsterhunterwilds/mods/130)<br><sub>Maximize All Evade Actions</sub> | 1.0 | 2025-03-19  | 413 / 19.9k |  | 将所有回避动作的无敌帧窗口最大化。 |
| [抑制导虫](https://www.nexusmods.com/monsterhunterwilds/mods/19)<br><sub>Suppressed Scoutflies</sub> | 1.0.1 | 2025-07-01  | 403 / 10.3k |  | REFramework脚本，追踪目标及高亮附近环境物件时隐藏部分或全部导虫效果。 |
| [REFramework Direct2D（HDR支持）](https://www.nexusmods.com/monsterhunterwilds/mods/4033)<br><sub>REFramework Direct2D with HDR Support</sub> | 1.5.0 | 2026-10-11 ✅ | 402 / 47.0k | （无法预览） | 支持HDR的Direct2D插件。 |
| [减少DLC检查（已过时）](https://www.nexusmods.com/monsterhunterwilds/mods/3798)<br><sub>(Obsolete) Less DLC Checks</sub> | 1.0 | 2026-01-15 ✅ | 398 / 18.0k |  | 减少游戏每秒多达数千次的DLC检查以提升性能。 |
| [无需豪鬼防具使用豪鬼招式](https://www.nexusmods.com/monsterhunterwilds/mods/2596)<br><sub>Akuma moveset without Akuma</sub> | 1.0.0 | 2025-08-25  | 393 / 13.5k |  | 无需装备豪鬼防具即可使用豪鬼招式，并附带完整套装增益和视觉效果。 |
| [成就进度追踪](https://www.nexusmods.com/monsterhunterwilds/mods/721)<br><sub>Achievement Progress Tracker</sub> | 1.3.0 | 2026-08-24 ✅ | 390 / 14.2k | （无法预览） | 追踪并显示含皇冠在内的21项成就进度，部分可显示缺少内容，支持多语言。 |
| [炼成变异武具（已弃用）](https://www.nexusmods.com/monsterhunterwilds/mods/3626)<br><sub>Meld Mutated Armaments (Deprecated)</sub> | 1.0 | 2025-12-22 ✅ | 390 / 19.1k |  | 将“变异武具”(Mutated Armaments)加入炼成遗物菜单。 |
| [超级怪力种子](https://www.nexusmods.com/monsterhunterwilds/mods/131)<br><sub>Super Might Seed</sub> | 1.2 | 2025-03-02  | 388 / 15.8k |  | 强化怪力种子的效果。 |
| [LuckyDog - 无限幸运券](https://www.nexusmods.com/monsterhunterwilds/mods/1100)<br><sub>LuckyDog - Infinite Lucky Vouchers</sub> | 1.0 | 2025-03-23  | 386 / 14.6k |  | 幸运券无限并自动使用。 |
| [自动磨刀](https://www.nexusmods.com/monsterhunterwilds/mods/79)<br><sub>Auto Sharpen Weapons</sub> | 1.0 | 2025-02-28  | 377 / 20.1k |  | 完成直接攻击怪物开始的任务后或非战斗时自动研磨武器。 |
| [智能营地选择](https://www.nexusmods.com/monsterhunterwilds/mods/4036)<br><sub>Smart Camp Picker</sub> | 1.2.0 | 2026-07-22 ✅ | 376 / 22.3k | （无法预览） | 接受任务时基于导航网格计算地形、高度和实际路径，自动选择最近的营地。 |
| [荒野 Mod Organizer 2 支持](https://www.nexusmods.com/monsterhunterwilds/mods/993)<br><sub>Wilds Mod Organizer 2 Support</sub> | 1.0.0 | 2025-03-20  | 371 / 12.5k |  | 为Mod Organizer 2添加荒野支持，并提供支持PAK排序和Fluffy安装器的插件链接。 |
| [更好的赛克雷特](https://www.nexusmods.com/monsterhunterwilds/mods/2546)<br><sub>Better Seikret</sub> | 1.2 | 2026-01-03 ✅ | 364 / 13.6k |  | 赛克雷特全速奔跑时，猎人进行任何动作都不会使其减速。 |
| [拍照模式增强](https://www.nexusmods.com/monsterhunterwilds/mods/1148)<br><sub>PhotoMode Plus</sub> | 1.01 | 2025-03-23  | 359 / 11.2k |  | 对拍照模式进行优化调整。 |
| [荒野 MO2 LOOT Pak文件排序](https://www.nexusmods.com/monsterhunterwilds/mods/1037)<br><sub>Wilds Mod Organizer 2  LOOT Pak Files</sub> | 7 | 2025-04-10  | 354 / 13.9k |  | 按MO2左侧面板的加载顺序一键自动重命名Pak文件，防止模组冲突。 |
| [轮盘自动重置](https://www.nexusmods.com/monsterhunterwilds/mods/1535)<br><sub>Auto Radial Reset</sub> | 2.3.1-Hotfix | 2025-12-18 ✅ | 348 / 18.5k |  | 每次打开或在特定游戏事件后，将轮盘菜单选择重置到自定义位置，便于依靠肌肉记忆。 |
| [移除贴图压缩](https://www.nexusmods.com/monsterhunterwilds/mods/853)<br><sub>Texture Decompresion Removal</sub> | 1.0 | 2025-03-17  | 347 / 15.7k |  | 移除贴图压缩，使游戏不再消耗资源进行解压。 |
| [血液特效](https://www.nexusmods.com/monsterhunterwilds/mods/3879)<br><sub>Blood FX</sub> | 1.3 | 2026-03-15 ✅ | 342 / 21.8k |  | 将所有血液和命中特效放大为2倍、3倍或4倍。 |
| [炼成所有装饰品 - 可选费用与解锁调整](https://www.nexusmods.com/monsterhunterwilds/mods/3593)<br><sub>Meld All Decorations - Optional Cost and Unlock Tweaks</sub> | 1.2 | 2026-02-18 ✅ | 325 / 26.0k |  | 将所有装饰品加入装饰品炼成列表。 |
| [镜头光源移除](https://www.nexusmods.com/monsterhunterwilds/mods/4022)<br><sub>Camera Light Remover</sub> | 1.0.1 | 2026-03-08 ✅ | 323 / 12.1k |  | 移除难看的镜头补光，找回角色阴影。 |
| [一体化菜单](https://www.nexusmods.com/monsterhunterwilds/mods/839)<br><sub>All in One Menu</sub> | 1.6.0 | 2025-12-23 ✅ | 322 / 18.2k |  | 为游戏主菜单添加多种功能以便快速访问。 |
| [荒野色彩校正 LCPD15](https://www.nexusmods.com/monsterhunterwilds/mods/341)<br><sub>ColorCorrection_MonsterHunterWilds_LCPD15</sub> | 1.0 | 2026-05-01 ✅ | 315 / 15.0k |  | 调整游戏色彩校正，使画面观感更舒适。 |
| [调查任务掉落升级与最大报酬](https://www.nexusmods.com/monsterhunterwilds/mods/941)<br><sub>Upgraded Drops and Max Loot Rolls from Investigations</sub> | 1.1.0 | 2025-04-05  | 315 / 11.5k |  | 装饰品掉落从稀有度4/5升为6，绚辉武器部件从5/6升为7，调查报酬均为最大数量。 |
| [性能提升模型重制](https://www.nexusmods.com/monsterhunterwilds/mods/2232)<br><sub>Performance Booster Re-Model</sub> | v6.5 | 2025-05-14  | 315 / 19.2k |  | 优化3D模型以提升性能，同时不牺牲画面质量。 |
| [道具袋扩容](https://www.nexusmods.com/monsterhunterwilds/mods/187)<br><sub>Item Pouch Upgrade</sub> | Title-Update-4.1 | 2026-02-18 ✅ | 311 / 14.7k |  | 将道具袋中物品（含弹药）的携带上限通常提升至两倍。 |
| [更好的猎人亮点](https://www.nexusmods.com/monsterhunterwilds/mods/2561)<br><sub>Better Hunter Highlights</sub> | 1.6.3 | 2026-02-07 ✅ | 305 / 20.1k |  | 为每位玩家在子菜单中添加更多猎人亮点数据，并在REFramework界面中加入概览表格。 |
| [无畏之鱼](https://www.nexusmods.com/monsterhunterwilds/mods/582)<br><sub>Fearless Fish</sub> | 1.0.0 | 2025-03-12  | 304 / 6.9k |  | 还原1.000.05.00版本的修复，使鱼不再因捕获网等落水冲击而逃跑。 |

<a id="conflicts"></a>
## 冲突速查：热门音效库被哪些 mod 改动

| 音效库 | 说明 | 改动它的 mod 数 | mod ID |
|---|---|---|---|
| `wp00_cmn_m.sbnk.1.x64` | 大剑主音效库 | 40 | [1471](https://www.nexusmods.com/monsterhunterwilds/mods/1471), [1335](https://www.nexusmods.com/monsterhunterwilds/mods/1335), [327](https://www.nexusmods.com/monsterhunterwilds/mods/327), [712](https://www.nexusmods.com/monsterhunterwilds/mods/712), [979](https://www.nexusmods.com/monsterhunterwilds/mods/979), [1896](https://www.nexusmods.com/monsterhunterwilds/mods/1896), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [995](https://www.nexusmods.com/monsterhunterwilds/mods/995), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [719](https://www.nexusmods.com/monsterhunterwilds/mods/719), [988](https://www.nexusmods.com/monsterhunterwilds/mods/988), [1292](https://www.nexusmods.com/monsterhunterwilds/mods/1292), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [4040](https://www.nexusmods.com/monsterhunterwilds/mods/4040), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [3460](https://www.nexusmods.com/monsterhunterwilds/mods/3460), [3219](https://www.nexusmods.com/monsterhunterwilds/mods/3219), [1187](https://www.nexusmods.com/monsterhunterwilds/mods/1187), [1367](https://www.nexusmods.com/monsterhunterwilds/mods/1367), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1892](https://www.nexusmods.com/monsterhunterwilds/mods/1892), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1598](https://www.nexusmods.com/monsterhunterwilds/mods/1598), [1764](https://www.nexusmods.com/monsterhunterwilds/mods/1764), [1718](https://www.nexusmods.com/monsterhunterwilds/mods/1718), [1210](https://www.nexusmods.com/monsterhunterwilds/mods/1210), [2585](https://www.nexusmods.com/monsterhunterwilds/mods/2585), [1035](https://www.nexusmods.com/monsterhunterwilds/mods/1035), [1364](https://www.nexusmods.com/monsterhunterwilds/mods/1364), [1906](https://www.nexusmods.com/monsterhunterwilds/mods/1906), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [2822](https://www.nexusmods.com/monsterhunterwilds/mods/2822), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013), [944](https://www.nexusmods.com/monsterhunterwilds/mods/944), [4280](https://www.nexusmods.com/monsterhunterwilds/mods/4280), [2041](https://www.nexusmods.com/monsterhunterwilds/mods/2041), [2945](https://www.nexusmods.com/monsterhunterwilds/mods/2945), [2622](https://www.nexusmods.com/monsterhunterwilds/mods/2622) |
| `wp03_cmn_m.sbnk.1.x64` | 太刀主音效库 | 40 | [929](https://www.nexusmods.com/monsterhunterwilds/mods/929), [642](https://www.nexusmods.com/monsterhunterwilds/mods/642), [1240](https://www.nexusmods.com/monsterhunterwilds/mods/1240), [913](https://www.nexusmods.com/monsterhunterwilds/mods/913), [781](https://www.nexusmods.com/monsterhunterwilds/mods/781), [1413](https://www.nexusmods.com/monsterhunterwilds/mods/1413), [1703](https://www.nexusmods.com/monsterhunterwilds/mods/1703), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [1231](https://www.nexusmods.com/monsterhunterwilds/mods/1231), [1033](https://www.nexusmods.com/monsterhunterwilds/mods/1033), [1965](https://www.nexusmods.com/monsterhunterwilds/mods/1965), [3044](https://www.nexusmods.com/monsterhunterwilds/mods/3044), [1911](https://www.nexusmods.com/monsterhunterwilds/mods/1911), [1292](https://www.nexusmods.com/monsterhunterwilds/mods/1292), [2558](https://www.nexusmods.com/monsterhunterwilds/mods/2558), [3910](https://www.nexusmods.com/monsterhunterwilds/mods/3910), [1898](https://www.nexusmods.com/monsterhunterwilds/mods/1898), [597](https://www.nexusmods.com/monsterhunterwilds/mods/597), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [823](https://www.nexusmods.com/monsterhunterwilds/mods/823), [1513](https://www.nexusmods.com/monsterhunterwilds/mods/1513), [1958](https://www.nexusmods.com/monsterhunterwilds/mods/1958), [1016](https://www.nexusmods.com/monsterhunterwilds/mods/1016), [2685](https://www.nexusmods.com/monsterhunterwilds/mods/2685), [897](https://www.nexusmods.com/monsterhunterwilds/mods/897), [2217](https://www.nexusmods.com/monsterhunterwilds/mods/2217), [1004](https://www.nexusmods.com/monsterhunterwilds/mods/1004), [751](https://www.nexusmods.com/monsterhunterwilds/mods/751), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [2822](https://www.nexusmods.com/monsterhunterwilds/mods/2822), [1429](https://www.nexusmods.com/monsterhunterwilds/mods/1429), [1387](https://www.nexusmods.com/monsterhunterwilds/mods/1387), [2624](https://www.nexusmods.com/monsterhunterwilds/mods/2624), [1856](https://www.nexusmods.com/monsterhunterwilds/mods/1856), [4280](https://www.nexusmods.com/monsterhunterwilds/mods/4280), [4137](https://www.nexusmods.com/monsterhunterwilds/mods/4137), [3496](https://www.nexusmods.com/monsterhunterwilds/mods/3496) |
| `hit_hm_cmn.sbnk.1.x64` | 公共命中音 | 31 | [349](https://www.nexusmods.com/monsterhunterwilds/mods/349), [1339](https://www.nexusmods.com/monsterhunterwilds/mods/1339), [2088](https://www.nexusmods.com/monsterhunterwilds/mods/2088), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [995](https://www.nexusmods.com/monsterhunterwilds/mods/995), [1336](https://www.nexusmods.com/monsterhunterwilds/mods/1336), [1865](https://www.nexusmods.com/monsterhunterwilds/mods/1865), [1161](https://www.nexusmods.com/monsterhunterwilds/mods/1161), [1700](https://www.nexusmods.com/monsterhunterwilds/mods/1700), [1901](https://www.nexusmods.com/monsterhunterwilds/mods/1901), [1801](https://www.nexusmods.com/monsterhunterwilds/mods/1801), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1368](https://www.nexusmods.com/monsterhunterwilds/mods/1368), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1564](https://www.nexusmods.com/monsterhunterwilds/mods/1564), [478](https://www.nexusmods.com/monsterhunterwilds/mods/478), [1035](https://www.nexusmods.com/monsterhunterwilds/mods/1035), [1427](https://www.nexusmods.com/monsterhunterwilds/mods/1427), [1362](https://www.nexusmods.com/monsterhunterwilds/mods/1362), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [2822](https://www.nexusmods.com/monsterhunterwilds/mods/2822), [272](https://www.nexusmods.com/monsterhunterwilds/mods/272), [4499](https://www.nexusmods.com/monsterhunterwilds/mods/4499), [2169](https://www.nexusmods.com/monsterhunterwilds/mods/2169), [4280](https://www.nexusmods.com/monsterhunterwilds/mods/4280), [4168](https://www.nexusmods.com/monsterhunterwilds/mods/4168), [4473](https://www.nexusmods.com/monsterhunterwilds/mods/4473), [4454](https://www.nexusmods.com/monsterhunterwilds/mods/4454), [4469](https://www.nexusmods.com/monsterhunterwilds/mods/4469) |
| `wp07_cmn_m.sbnk.1.x64` | 铳枪主音效库 | 27 | [167](https://www.nexusmods.com/monsterhunterwilds/mods/167), [1335](https://www.nexusmods.com/monsterhunterwilds/mods/1335), [327](https://www.nexusmods.com/monsterhunterwilds/mods/327), [890](https://www.nexusmods.com/monsterhunterwilds/mods/890), [1080](https://www.nexusmods.com/monsterhunterwilds/mods/1080), [1896](https://www.nexusmods.com/monsterhunterwilds/mods/1896), [1952](https://www.nexusmods.com/monsterhunterwilds/mods/1952), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [3501](https://www.nexusmods.com/monsterhunterwilds/mods/3501), [1452](https://www.nexusmods.com/monsterhunterwilds/mods/1452), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [1741](https://www.nexusmods.com/monsterhunterwilds/mods/1741), [3460](https://www.nexusmods.com/monsterhunterwilds/mods/3460), [3219](https://www.nexusmods.com/monsterhunterwilds/mods/3219), [1367](https://www.nexusmods.com/monsterhunterwilds/mods/1367), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1892](https://www.nexusmods.com/monsterhunterwilds/mods/1892), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1364](https://www.nexusmods.com/monsterhunterwilds/mods/1364), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [3968](https://www.nexusmods.com/monsterhunterwilds/mods/3968), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013), [1352](https://www.nexusmods.com/monsterhunterwilds/mods/1352) |
| `wp09_cmn_m.sbnk.1.x64` | 盾斧主音效库 | 26 | [725](https://www.nexusmods.com/monsterhunterwilds/mods/725), [1335](https://www.nexusmods.com/monsterhunterwilds/mods/1335), [327](https://www.nexusmods.com/monsterhunterwilds/mods/327), [1896](https://www.nexusmods.com/monsterhunterwilds/mods/1896), [1952](https://www.nexusmods.com/monsterhunterwilds/mods/1952), [1002](https://www.nexusmods.com/monsterhunterwilds/mods/1002), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [2329](https://www.nexusmods.com/monsterhunterwilds/mods/2329), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [1917](https://www.nexusmods.com/monsterhunterwilds/mods/1917), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [3460](https://www.nexusmods.com/monsterhunterwilds/mods/3460), [3219](https://www.nexusmods.com/monsterhunterwilds/mods/3219), [1367](https://www.nexusmods.com/monsterhunterwilds/mods/1367), [1529](https://www.nexusmods.com/monsterhunterwilds/mods/1529), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1892](https://www.nexusmods.com/monsterhunterwilds/mods/1892), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1364](https://www.nexusmods.com/monsterhunterwilds/mods/1364), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [3354](https://www.nexusmods.com/monsterhunterwilds/mods/3354), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013), [4470](https://www.nexusmods.com/monsterhunterwilds/mods/4470) |
| `wp01_cmn_m.sbnk.1.x64` | 片手剑主音效库 | 25 | [2527](https://www.nexusmods.com/monsterhunterwilds/mods/2527), [1335](https://www.nexusmods.com/monsterhunterwilds/mods/1335), [327](https://www.nexusmods.com/monsterhunterwilds/mods/327), [1896](https://www.nexusmods.com/monsterhunterwilds/mods/1896), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [995](https://www.nexusmods.com/monsterhunterwilds/mods/995), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [1076](https://www.nexusmods.com/monsterhunterwilds/mods/1076), [609](https://www.nexusmods.com/monsterhunterwilds/mods/609), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [3460](https://www.nexusmods.com/monsterhunterwilds/mods/3460), [3219](https://www.nexusmods.com/monsterhunterwilds/mods/3219), [1367](https://www.nexusmods.com/monsterhunterwilds/mods/1367), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [2379](https://www.nexusmods.com/monsterhunterwilds/mods/2379), [1892](https://www.nexusmods.com/monsterhunterwilds/mods/1892), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1364](https://www.nexusmods.com/monsterhunterwilds/mods/1364), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [1449](https://www.nexusmods.com/monsterhunterwilds/mods/1449), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013), [967](https://www.nexusmods.com/monsterhunterwilds/mods/967) |
| `weapon_cmn.sbnk.1.x64` | 武器公共音 | 22 | [1471](https://www.nexusmods.com/monsterhunterwilds/mods/1471), [1002](https://www.nexusmods.com/monsterhunterwilds/mods/1002), [3748](https://www.nexusmods.com/monsterhunterwilds/mods/3748), [995](https://www.nexusmods.com/monsterhunterwilds/mods/995), [2977](https://www.nexusmods.com/monsterhunterwilds/mods/2977), [1076](https://www.nexusmods.com/monsterhunterwilds/mods/1076), [609](https://www.nexusmods.com/monsterhunterwilds/mods/609), [1917](https://www.nexusmods.com/monsterhunterwilds/mods/1917), [1598](https://www.nexusmods.com/monsterhunterwilds/mods/1598), [1764](https://www.nexusmods.com/monsterhunterwilds/mods/1764), [4232](https://www.nexusmods.com/monsterhunterwilds/mods/4232), [1718](https://www.nexusmods.com/monsterhunterwilds/mods/1718), [1210](https://www.nexusmods.com/monsterhunterwilds/mods/1210), [2822](https://www.nexusmods.com/monsterhunterwilds/mods/2822), [4164](https://www.nexusmods.com/monsterhunterwilds/mods/4164), [1449](https://www.nexusmods.com/monsterhunterwilds/mods/1449), [2976](https://www.nexusmods.com/monsterhunterwilds/mods/2976), [944](https://www.nexusmods.com/monsterhunterwilds/mods/944), [4280](https://www.nexusmods.com/monsterhunterwilds/mods/4280), [4158](https://www.nexusmods.com/monsterhunterwilds/mods/4158), [1352](https://www.nexusmods.com/monsterhunterwilds/mods/1352), [2041](https://www.nexusmods.com/monsterhunterwilds/mods/2041) |
| `bgm_resident_1st_m.sbnk.1.x64` | BGM | 22 | [846](https://www.nexusmods.com/monsterhunterwilds/mods/846), [1357](https://www.nexusmods.com/monsterhunterwilds/mods/1357), [1197](https://www.nexusmods.com/monsterhunterwilds/mods/1197), [1159](https://www.nexusmods.com/monsterhunterwilds/mods/1159), [1162](https://www.nexusmods.com/monsterhunterwilds/mods/1162), [1029](https://www.nexusmods.com/monsterhunterwilds/mods/1029), [1494](https://www.nexusmods.com/monsterhunterwilds/mods/1494), [3995](https://www.nexusmods.com/monsterhunterwilds/mods/3995), [1765](https://www.nexusmods.com/monsterhunterwilds/mods/1765), [4183](https://www.nexusmods.com/monsterhunterwilds/mods/4183), [1074](https://www.nexusmods.com/monsterhunterwilds/mods/1074), [3800](https://www.nexusmods.com/monsterhunterwilds/mods/3800), [1894](https://www.nexusmods.com/monsterhunterwilds/mods/1894), [3584](https://www.nexusmods.com/monsterhunterwilds/mods/3584), [1462](https://www.nexusmods.com/monsterhunterwilds/mods/1462), [1168](https://www.nexusmods.com/monsterhunterwilds/mods/1168), [1724](https://www.nexusmods.com/monsterhunterwilds/mods/1724), [1382](https://www.nexusmods.com/monsterhunterwilds/mods/1382), [1170](https://www.nexusmods.com/monsterhunterwilds/mods/1170), [945](https://www.nexusmods.com/monsterhunterwilds/mods/945), [4169](https://www.nexusmods.com/monsterhunterwilds/mods/4169), [4412](https://www.nexusmods.com/monsterhunterwilds/mods/4412) |
| `wp06_cmn_m.sbnk.1.x64` | 长枪主音效库 | 21 | [1335](https://www.nexusmods.com/monsterhunterwilds/mods/1335), [327](https://www.nexusmods.com/monsterhunterwilds/mods/327), [1896](https://www.nexusmods.com/monsterhunterwilds/mods/1896), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [3460](https://www.nexusmods.com/monsterhunterwilds/mods/3460), [3219](https://www.nexusmods.com/monsterhunterwilds/mods/3219), [1367](https://www.nexusmods.com/monsterhunterwilds/mods/1367), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1892](https://www.nexusmods.com/monsterhunterwilds/mods/1892), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1712](https://www.nexusmods.com/monsterhunterwilds/mods/1712), [1364](https://www.nexusmods.com/monsterhunterwilds/mods/1364), [1943](https://www.nexusmods.com/monsterhunterwilds/mods/1943), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013), [2015](https://www.nexusmods.com/monsterhunterwilds/mods/2015) |
| `bgm_resident_ev.sbnk.1.x64` | BGM | 21 | [940](https://www.nexusmods.com/monsterhunterwilds/mods/940), [3560](https://www.nexusmods.com/monsterhunterwilds/mods/3560), [3803](https://www.nexusmods.com/monsterhunterwilds/mods/3803), [3340](https://www.nexusmods.com/monsterhunterwilds/mods/3340), [1763](https://www.nexusmods.com/monsterhunterwilds/mods/1763), [3713](https://www.nexusmods.com/monsterhunterwilds/mods/3713), [4183](https://www.nexusmods.com/monsterhunterwilds/mods/4183), [1737](https://www.nexusmods.com/monsterhunterwilds/mods/1737), [3506](https://www.nexusmods.com/monsterhunterwilds/mods/3506), [1462](https://www.nexusmods.com/monsterhunterwilds/mods/1462), [3633](https://www.nexusmods.com/monsterhunterwilds/mods/3633), [3801](https://www.nexusmods.com/monsterhunterwilds/mods/3801), [3500](https://www.nexusmods.com/monsterhunterwilds/mods/3500), [3779](https://www.nexusmods.com/monsterhunterwilds/mods/3779), [3613](https://www.nexusmods.com/monsterhunterwilds/mods/3613), [4138](https://www.nexusmods.com/monsterhunterwilds/mods/4138), [3118](https://www.nexusmods.com/monsterhunterwilds/mods/3118), [4144](https://www.nexusmods.com/monsterhunterwilds/mods/4144), [4147](https://www.nexusmods.com/monsterhunterwilds/mods/4147), [4148](https://www.nexusmods.com/monsterhunterwilds/mods/4148), [4162](https://www.nexusmods.com/monsterhunterwilds/mods/4162) |
| `wp08_cmn_m.sbnk.1.x64` | 斩斧主音效库 | 20 | [874](https://www.nexusmods.com/monsterhunterwilds/mods/874), [584](https://www.nexusmods.com/monsterhunterwilds/mods/584), [1068](https://www.nexusmods.com/monsterhunterwilds/mods/1068), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [995](https://www.nexusmods.com/monsterhunterwilds/mods/995), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [1161](https://www.nexusmods.com/monsterhunterwilds/mods/1161), [2111](https://www.nexusmods.com/monsterhunterwilds/mods/2111), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1427](https://www.nexusmods.com/monsterhunterwilds/mods/1427), [426](https://www.nexusmods.com/monsterhunterwilds/mods/426), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [3513](https://www.nexusmods.com/monsterhunterwilds/mods/3513), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013), [4088](https://www.nexusmods.com/monsterhunterwilds/mods/4088) |
| `wp12_cmn_m.sbnk.1.x64` | 重弩主音效库 | 19 | [1335](https://www.nexusmods.com/monsterhunterwilds/mods/1335), [1896](https://www.nexusmods.com/monsterhunterwilds/mods/1896), [1264](https://www.nexusmods.com/monsterhunterwilds/mods/1264), [3204](https://www.nexusmods.com/monsterhunterwilds/mods/3204), [2299](https://www.nexusmods.com/monsterhunterwilds/mods/2299), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [4167](https://www.nexusmods.com/monsterhunterwilds/mods/4167), [3460](https://www.nexusmods.com/monsterhunterwilds/mods/3460), [3219](https://www.nexusmods.com/monsterhunterwilds/mods/3219), [1367](https://www.nexusmods.com/monsterhunterwilds/mods/1367), [1303](https://www.nexusmods.com/monsterhunterwilds/mods/1303), [1892](https://www.nexusmods.com/monsterhunterwilds/mods/1892), [1302](https://www.nexusmods.com/monsterhunterwilds/mods/1302), [1308](https://www.nexusmods.com/monsterhunterwilds/mods/1308), [1364](https://www.nexusmods.com/monsterhunterwilds/mods/1364), [2567](https://www.nexusmods.com/monsterhunterwilds/mods/2567), [1304](https://www.nexusmods.com/monsterhunterwilds/mods/1304), [1305](https://www.nexusmods.com/monsterhunterwilds/mods/1305), [2013](https://www.nexusmods.com/monsterhunterwilds/mods/2013) |
| `human_common_effect.sbnk.1.x64` |  | 14 | [156](https://www.nexusmods.com/monsterhunterwilds/mods/156), [1349](https://www.nexusmods.com/monsterhunterwilds/mods/1349), [1025](https://www.nexusmods.com/monsterhunterwilds/mods/1025), [1002](https://www.nexusmods.com/monsterhunterwilds/mods/1002), [1076](https://www.nexusmods.com/monsterhunterwilds/mods/1076), [609](https://www.nexusmods.com/monsterhunterwilds/mods/609), [4232](https://www.nexusmods.com/monsterhunterwilds/mods/4232), [2058](https://www.nexusmods.com/monsterhunterwilds/mods/2058), [1429](https://www.nexusmods.com/monsterhunterwilds/mods/1429), [904](https://www.nexusmods.com/monsterhunterwilds/mods/904), [1449](https://www.nexusmods.com/monsterhunterwilds/mods/1449), [2041](https://www.nexusmods.com/monsterhunterwilds/mods/2041), [1285](https://www.nexusmods.com/monsterhunterwilds/mods/1285), [4445](https://www.nexusmods.com/monsterhunterwilds/mods/4445) |
| `player_actvoice_f03.sbnk.1.x64.ja` | 猎人语音 | 13 | [1060](https://www.nexusmods.com/monsterhunterwilds/mods/1060), [1457](https://www.nexusmods.com/monsterhunterwilds/mods/1457), [1002](https://www.nexusmods.com/monsterhunterwilds/mods/1002), [1521](https://www.nexusmods.com/monsterhunterwilds/mods/1521), [1414](https://www.nexusmods.com/monsterhunterwilds/mods/1414), [2329](https://www.nexusmods.com/monsterhunterwilds/mods/2329), [1911](https://www.nexusmods.com/monsterhunterwilds/mods/1911), [3527](https://www.nexusmods.com/monsterhunterwilds/mods/3527), [4232](https://www.nexusmods.com/monsterhunterwilds/mods/4232), [1035](https://www.nexusmods.com/monsterhunterwilds/mods/1035), [1004](https://www.nexusmods.com/monsterhunterwilds/mods/1004), [1429](https://www.nexusmods.com/monsterhunterwilds/mods/1429), [1285](https://www.nexusmods.com/monsterhunterwilds/mods/1285) |
| `human_common_foley.sbnk.1.x64` |  | 10 | [1349](https://www.nexusmods.com/monsterhunterwilds/mods/1349), [844](https://www.nexusmods.com/monsterhunterwilds/mods/844), [150](https://www.nexusmods.com/monsterhunterwilds/mods/150), [1140](https://www.nexusmods.com/monsterhunterwilds/mods/1140), [952](https://www.nexusmods.com/monsterhunterwilds/mods/952), [1515](https://www.nexusmods.com/monsterhunterwilds/mods/1515), [1142](https://www.nexusmods.com/monsterhunterwilds/mods/1142), [1234](https://www.nexusmods.com/monsterhunterwilds/mods/1234), [1141](https://www.nexusmods.com/monsterhunterwilds/mods/1141), [1449](https://www.nexusmods.com/monsterhunterwilds/mods/1449) |
| `wp02_cmn_m.sbnk.1.x64` | 双刀主音效库 | 10 | [628](https://www.nexusmods.com/monsterhunterwilds/mods/628), [2442](https://www.nexusmods.com/monsterhunterwilds/mods/2442), [2508](https://www.nexusmods.com/monsterhunterwilds/mods/2508), [1965](https://www.nexusmods.com/monsterhunterwilds/mods/1965), [762](https://www.nexusmods.com/monsterhunterwilds/mods/762), [1899](https://www.nexusmods.com/monsterhunterwilds/mods/1899), [885](https://www.nexusmods.com/monsterhunterwilds/mods/885), [1956](https://www.nexusmods.com/monsterhunterwilds/mods/1956), [911](https://www.nexusmods.com/monsterhunterwilds/mods/911), [4220](https://www.nexusmods.com/monsterhunterwilds/mods/4220) |
| `wp11_cmn_m.sbnk.1.x64` | 轻弩主音效库 | 10 | [1262](https://www.nexusmods.com/monsterhunterwilds/mods/1262), [995](https://www.nexusmods.com/monsterhunterwilds/mods/995), [2508](https://www.nexusmods.com/monsterhunterwilds/mods/2508), [1965](https://www.nexusmods.com/monsterhunterwilds/mods/1965), [762](https://www.nexusmods.com/monsterhunterwilds/mods/762), [1899](https://www.nexusmods.com/monsterhunterwilds/mods/1899), [2012](https://www.nexusmods.com/monsterhunterwilds/mods/2012), [3781](https://www.nexusmods.com/monsterhunterwilds/mods/3781), [2580](https://www.nexusmods.com/monsterhunterwilds/mods/2580), [1237](https://www.nexusmods.com/monsterhunterwilds/mods/1237) |
| `bgm_resident_m.sbnk.1.x64` | BGM | 10 | [940](https://www.nexusmods.com/monsterhunterwilds/mods/940), [3560](https://www.nexusmods.com/monsterhunterwilds/mods/3560), [4183](https://www.nexusmods.com/monsterhunterwilds/mods/4183), [1737](https://www.nexusmods.com/monsterhunterwilds/mods/1737), [3801](https://www.nexusmods.com/monsterhunterwilds/mods/3801), [4138](https://www.nexusmods.com/monsterhunterwilds/mods/4138), [3118](https://www.nexusmods.com/monsterhunterwilds/mods/3118), [4144](https://www.nexusmods.com/monsterhunterwilds/mods/4144), [4147](https://www.nexusmods.com/monsterhunterwilds/mods/4147), [4148](https://www.nexusmods.com/monsterhunterwilds/mods/4148) |
| `hit_weapon_cmn.sbnk.1.x64` | 公共命中音 | 9 | [1262](https://www.nexusmods.com/monsterhunterwilds/mods/1262), [1002](https://www.nexusmods.com/monsterhunterwilds/mods/1002), [1076](https://www.nexusmods.com/monsterhunterwilds/mods/1076), [1336](https://www.nexusmods.com/monsterhunterwilds/mods/1336), [609](https://www.nexusmods.com/monsterhunterwilds/mods/609), [478](https://www.nexusmods.com/monsterhunterwilds/mods/478), [1856](https://www.nexusmods.com/monsterhunterwilds/mods/1856), [1449](https://www.nexusmods.com/monsterhunterwilds/mods/1449), [2041](https://www.nexusmods.com/monsterhunterwilds/mods/2041) |
| `wp10_cmn_m.sbnk.1.x64` | 操虫棍主音效库 | 9 | [3864](https://www.nexusmods.com/monsterhunterwilds/mods/3864), [658](https://www.nexusmods.com/monsterhunterwilds/mods/658), [538](https://www.nexusmods.com/monsterhunterwilds/mods/538), [1523](https://www.nexusmods.com/monsterhunterwilds/mods/1523), [832](https://www.nexusmods.com/monsterhunterwilds/mods/832), [1394](https://www.nexusmods.com/monsterhunterwilds/mods/1394), [2557](https://www.nexusmods.com/monsterhunterwilds/mods/2557), [1285](https://www.nexusmods.com/monsterhunterwilds/mods/1285), [3913](https://www.nexusmods.com/monsterhunterwilds/mods/3913) |
| `bgm_01_00_m.sbnk.1.x64` | BGM | 8 | [1674](https://www.nexusmods.com/monsterhunterwilds/mods/1674), [1705](https://www.nexusmods.com/monsterhunterwilds/mods/1705), [3803](https://www.nexusmods.com/monsterhunterwilds/mods/3803), [1763](https://www.nexusmods.com/monsterhunterwilds/mods/1763), [1829](https://www.nexusmods.com/monsterhunterwilds/mods/1829), [1720](https://www.nexusmods.com/monsterhunterwilds/mods/1720), [1695](https://www.nexusmods.com/monsterhunterwilds/mods/1695), [3584](https://www.nexusmods.com/monsterhunterwilds/mods/3584) |
| `wp07_shell.sbnk.1.x64` |  | 7 | [890](https://www.nexusmods.com/monsterhunterwilds/mods/890), [1080](https://www.nexusmods.com/monsterhunterwilds/mods/1080), [1952](https://www.nexusmods.com/monsterhunterwilds/mods/1952), [3501](https://www.nexusmods.com/monsterhunterwilds/mods/3501), [1452](https://www.nexusmods.com/monsterhunterwilds/mods/1452), [1862](https://www.nexusmods.com/monsterhunterwilds/mods/1862), [1352](https://www.nexusmods.com/monsterhunterwilds/mods/1352) |
| `player_chatactionvoice_f03.sbnk.1.x64.en` | 猎人语音 | 6 | [4030](https://www.nexusmods.com/monsterhunterwilds/mods/4030), [2369](https://www.nexusmods.com/monsterhunterwilds/mods/2369), [711](https://www.nexusmods.com/monsterhunterwilds/mods/711), [3746](https://www.nexusmods.com/monsterhunterwilds/mods/3746), [3931](https://www.nexusmods.com/monsterhunterwilds/mods/3931), [3875](https://www.nexusmods.com/monsterhunterwilds/mods/3875) |
| `bgm_03_00_m.sbnk.1.x64` | BGM | 6 | [3340](https://www.nexusmods.com/monsterhunterwilds/mods/3340), [3713](https://www.nexusmods.com/monsterhunterwilds/mods/3713), [4185](https://www.nexusmods.com/monsterhunterwilds/mods/4185), [3506](https://www.nexusmods.com/monsterhunterwilds/mods/3506), [3500](https://www.nexusmods.com/monsterhunterwilds/mods/3500), [3422](https://www.nexusmods.com/monsterhunterwilds/mods/3422) |
| `player_chatactionvoice_f03.sbnk.1.x64.ja` | 猎人语音 | 6 | [4030](https://www.nexusmods.com/monsterhunterwilds/mods/4030), [1414](https://www.nexusmods.com/monsterhunterwilds/mods/1414), [3746](https://www.nexusmods.com/monsterhunterwilds/mods/3746), [4232](https://www.nexusmods.com/monsterhunterwilds/mods/4232), [3931](https://www.nexusmods.com/monsterhunterwilds/mods/3931), [3875](https://www.nexusmods.com/monsterhunterwilds/mods/3875) |
| `it0500_0014_m.sbnk.1.x64` |  | 5 | [3070](https://www.nexusmods.com/monsterhunterwilds/mods/3070), [898](https://www.nexusmods.com/monsterhunterwilds/mods/898), [1313](https://www.nexusmods.com/monsterhunterwilds/mods/1313), [1272](https://www.nexusmods.com/monsterhunterwilds/mods/1272), [1976](https://www.nexusmods.com/monsterhunterwilds/mods/1976) |
| `bgm_04_00_m.sbnk.1.x64` | BGM | 5 | [4183](https://www.nexusmods.com/monsterhunterwilds/mods/4183), [3676](https://www.nexusmods.com/monsterhunterwilds/mods/3676), [3633](https://www.nexusmods.com/monsterhunterwilds/mods/3633), [3779](https://www.nexusmods.com/monsterhunterwilds/mods/3779), [3613](https://www.nexusmods.com/monsterhunterwilds/mods/3613) |
| `wp13_cmn_m.sbnk.1.x64` | 弓主音效库 | 4 | [182](https://www.nexusmods.com/monsterhunterwilds/mods/182), [1990](https://www.nexusmods.com/monsterhunterwilds/mods/1990), [687](https://www.nexusmods.com/monsterhunterwilds/mods/687), [2510](https://www.nexusmods.com/monsterhunterwilds/mods/2510) |
| `wp05_cmn_m.sbnk.1.x64` | 狩猎笛主音效库 | 4 | [1239](https://www.nexusmods.com/monsterhunterwilds/mods/1239), [1173](https://www.nexusmods.com/monsterhunterwilds/mods/1173), [870](https://www.nexusmods.com/monsterhunterwilds/mods/870), [1976](https://www.nexusmods.com/monsterhunterwilds/mods/1976) |
| `it0500_0011_m.sbnk.1.x64` |  | 4 | [3070](https://www.nexusmods.com/monsterhunterwilds/mods/3070), [975](https://www.nexusmods.com/monsterhunterwilds/mods/975), [3084](https://www.nexusmods.com/monsterhunterwilds/mods/3084), [1976](https://www.nexusmods.com/monsterhunterwilds/mods/1976) |
