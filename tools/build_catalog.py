"""从 Nexus Mods 公开 GraphQL API 抓取《怪物猎人：荒野》全部 mod，按兴趣分类生成目录。

用法:
    python tools/build_catalog.py [--cache DIR] [--refresh]

输出:
    mhwilds-catalog/README.md   分类目录（Markdown）
    mhwilds-catalog/mods.csv    全部入选 mod 的明细（含改动的音效库文件，用于判断冲突）

只用标准库。nexusmods.com 网页有 Cloudflare，但 api.nexusmods.com/v2/graphql
与 file-metadata.nexusmods.com（压缩包内容预览）可匿名访问。
"""

import argparse
import csv
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

GAME_ID = "6993"
GAME_DOMAIN = "monsterhunterwilds"
API = "https://api.nexusmods.com/v2/graphql"
META = "https://file-metadata.nexusmods.com/file/nexus-files-s3-meta/{game}/{mod}/{uri}.json"
UA = {"User-Agent": "mod_finder/1.0 (+https://github.com/WhoAlwaysZzz/mod_finder)"}
TU4_DATE = "2025-12-16"  # Title Update 4 发布日

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "mhwilds-catalog"
# 中文译名与简介（人工/模型翻译，键为 mod ID 字符串）。新 mod 没有译文时回退到原文。
TRANSLATIONS = OUT_DIR / "translations_zh.json"
ZH = json.loads(TRANSLATIONS.read_text(encoding="utf-8")) if TRANSLATIONS.exists() else {}
CATEGORY_ZH = {"Armour": "防具", "Weapons": "武器", "Gameplay": "玩法", "Characters": "角色", "Audio": "音频",
               "Visuals": "画面", "Miscellaneous": "杂项", "Monsters": "怪物", "User Interface": "界面",
               "Utilities": "工具", "Items": "道具", "Bodyslide": "体型", "Skills": "技能"}


def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", **UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
            if "errors" in data:
                raise RuntimeError(data["errors"])
            return data["data"]
        except Exception:
            if attempt == 2:
                raise


MODS_Q = """query($o:Int,$s:[ModsSort!]){ mods(filter:{gameId:[{value:"%s",op:EQUALS}]}, sort:$s, offset:$o, count:100){
  totalCount nodes{ modId name summary version createdAt updatedAt endorsements downloads author adultContent modCategory{name} } } }""" % GAME_ID

# API 的 offset 有上限（实测约 3100），用多种排序各翻一遍再合并去重
SORTS = [{"createdAt": {"direction": d}} for d in ("ASC", "DESC")] + [
    {"endorsements": {"direction": d}} for d in ("ASC", "DESC")] + [
    {"name": {"direction": d}} for d in ("ASC", "DESC")]


def fetch_all_mods():
    mods, total = {}, None
    for sort in SORTS:
        offset = 0
        while True:
            try:
                page = gql(MODS_Q, {"o": offset, "s": [sort]})["mods"]
            except Exception:
                break  # 超出 offset 上限
            total = page["totalCount"]
            for n in page["nodes"]:
                mods[n["modId"]] = n
            offset += 100
            if not page["nodes"] or offset >= total:
                break
        if total and len(mods) >= total:
            break
    print(f"抓取 mod: {len(mods)} / {total}", file=sys.stderr)
    return list(mods.values())


def fetch_archive_paths(mod_id):
    files = gql('{ modFiles(modId:%d, gameId:"%s"){ name version category uri } }' % (mod_id, GAME_ID))["modFiles"]
    paths, previewed = [], False
    for f in files:
        if f["category"] not in ("MAIN", "OPTIONAL", "UPDATE", "MISCELLANEOUS"):
            continue
        url = META.format(game=GAME_ID, mod=mod_id, uri=urllib.parse.quote(f["uri"]))
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                tree = json.load(r)
        except Exception:
            continue  # 2026 年下半年起新上传文件的 uri 改成哈希路径，这个预览地址拿不到
        previewed = True
        stack = [tree]
        while stack:
            node = stack.pop()
            for c in node.get("children", []):
                (paths.append(c["path"]) if c["type"] == "file" else stack.append(c))
    return paths if previewed else None


# ---------- 分类规则 ----------
LS_RE = re.compile(r"long ?-?sword|\bLS\b|太刀|\biai\b|居合|helm ?-?breaker|兜割|登[龙龍]|foresight|見切|见切|"
                   r"spirit (blade|slash|release|roundslash|thrust|charge|helm|combo)|気刃|气刃", re.I)
AUDIO_RE = re.compile(r"sound|sfx|\bse\b|audio|voice|vocal|bgm|music|theme|song|jingle|roar|\bost\b|"
                      r"音效|语音|語音|ボイス|効果音|音楽|配音|曲|播放|声音|\blouder\b|\bmute|silenc|\bvolume\b", re.I)
COMBAT_SFX_RE = re.compile(r"offset|counter|perfect (guard|dodge|evade)|parry|crit|hit ?sound|hitsound|"
                           r"stun|wound|focus|sharpen|kill|相殺|相杀|会心|弱点|打击|命中|格挡|完美", re.I)
VOICE_RE = re.compile(r"voice|vocal|语音|語音|ボイス|配音|台词|callout|shout", re.I)
MUSIC_RE = re.compile(r"bgm|music|theme|song|jingle|\bost\b|音楽|曲|主题", re.I)
BANK_RE = re.compile(r"[^/\\]+\.(?:sbnk|spck|bnk|pck)(?:\.[^/\\]*)*$", re.I)

WEAPON_BANKS = {f"wp{i:02d}": n for i, n in enumerate(
    ["大剑", "片手剑", "双刀", "太刀", "大锤", "狩猎笛", "长枪", "铳枪", "斩斧", "盾斧", "操虫棍", "轻弩", "重弩", "弓"])}
SHARED_COMBAT_BANKS = ("hit_hm_cmn", "hit_weapon_cmn", "weapon_cmn")
# 带这些前缀的 bank 才算“音效 mod”的证据；it0xxx_* 是单把武器模型自带的音效，模型 mod 常顺带打包
AUDIO_BANK_PREFIXES = ("wp", "hit_", "weapon_", "human_", "player_", "porter_", "bgm", "gui_", "em", "npc", "ot_", "cat_")


def banks_of(paths):
    return sorted({BANK_RE.search(p.replace("\\", "/")).group(0).lower() for p in paths if BANK_RE.search(p)})


def classify(m, banks):
    text = f"{m['name']} {m.get('summary') or ''}"
    cat = (m.get("modCategory") or {}).get("name") or ""
    is_ls = bool(LS_RE.search(text)) or any(b.startswith("wp03_") for b in banks)
    audio_banks = [b for b in banks if b.startswith(AUDIO_BANK_PREFIXES)]
    # 只在简介里顺带提到 sound 的不算；名称命中、Audio 分类或真的改了音效库才算
    is_audio = bool(audio_banks) or bool(AUDIO_RE.search(m["name"])) or (cat == "Audio" and bool(AUDIO_RE.search(text)))
    if is_audio and cat == "Utilities":
        return "T"  # 音频相关工具
    if is_ls and is_audio and (cat == "Audio" or any(b.startswith(("wp03_",) + SHARED_COMBAT_BANKS) for b in banks)
                               or AUDIO_RE.search(text) and not banks):
        return "A"  # 太刀音效 / 语音
    weapon_specific = [b for b in banks if b[:4] in WEAPON_BANKS]
    if is_audio and (COMBAT_SFX_RE.search(text) or (any(b.startswith(SHARED_COMBAT_BANKS) for b in banks) and not weapon_specific)):
        return "B"  # 通用战斗音效（太刀也会用到）
    if is_ls and cat in ("Gameplay", "Skills", "Utilities", "Miscellaneous", "User Interface"):
        return "C"  # 太刀玩法
    if is_ls:
        return "D"  # 太刀外观 / 模型
    if is_audio:
        if any(b.startswith(("player_", "npc", "ot_dia", "event_dia")) for b in banks) or (
                VOICE_RE.search(text) and not MUSIC_RE.search(text) and not weapon_specific):
            return "E"  # 角色 / 猎人 / 随从语音
        if any(b.startswith("bgm") for b in banks) or MUSIC_RE.search(text):
            return "F"  # BGM / 音乐
        if any(b[:4] in WEAPON_BANKS for b in banks):
            return "G"  # 其它武器音效
        return "H"  # 其它音效（道具、环境、UI…）
    if cat in POPULAR_CATEGORIES and m["endorsements"] >= POPULAR_MIN_ENDORSEMENTS:
        return "I"  # 通用热门
    return None


POPULAR_CATEGORIES = {"Utilities", "User Interface", "Gameplay", "Visuals", "Miscellaneous", "Skills", "Items", "Monsters"}
POPULAR_MIN_ENDORSEMENTS = 300

SECTIONS = {
    "T": ("音频相关工具 / 框架", "做或调试音效 mod 时用得到的工具，以及能播放自定义音频的框架类 mod。"),
    "A": ("太刀音效 / 语音", "全部列出。改同一个音效库的 mod 互相冲突，同一时间只能启用一个。"),
    "B": ("通用战斗音效（太刀也会触发）", "相杀、反击、完美格挡/回避、会心、命中、眩晕、伤口等。改公共库（`hit_hm_cmn`、`weapon_cmn` 等）的 mod 彼此冲突。"),
    "C": ("太刀玩法 / 判定 / 手感", "非音频，与太刀相关。"),
    "D": ("太刀外观 / 模型（含多武器共用模型）", "非音频。名称里带 LS 或太刀的武器模型 mod。"),
    "E": ("角色 / 猎人 / 随从 / NPC 语音", ""),
    "F": ("BGM / 音乐", ""),
    "G": ("其它武器音效", "按武器分组。"),
    "H": ("其它音效（道具、环境、UI、怪物等）", ""),
    "I": ("通用热门：前置 / 工具 / UI / 性能 / 玩法", f"非音频、非太刀专属。分类为工具、界面、玩法、画面、杂项、技能、道具、怪物，且点赞数 ≥ {POPULAR_MIN_ENDORSEMENTS} 的 mod，选 mod 时可作参考。"),
}


def fmt_num(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)


def md_escape(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").replace("\r", " ").strip()


def row(m, banks):
    url = f"https://www.nexusmods.com/{GAME_DOMAIN}/mods/{m['modId']}"
    upd = m["updatedAt"][:10]
    fresh = "✅" if upd >= TU4_DATE else ""
    zh = ZH.get(str(m["modId"]), {})
    summary = md_escape(zh.get("summary_zh") or m.get("summary"))
    if len(summary) > 140:
        summary = summary[:137] + "…"
    name_zh = md_escape(zh.get("name_zh"))
    name = md_escape(m["name"])
    title = f"[{name_zh}]({url})<br><sub>{name}</sub>" if name_zh and name_zh != name else f"[{name}]({url})"
    bank_s = "<br>".join(f"`{b.split('.')[0]}`" for b in banks[:4]) + (" …" if len(banks) > 4 else "")
    if not m.get("_preview", True):
        bank_s = "（无法预览）"
    return (f"| {title} | {md_escape(m['version'])} | {upd} {fresh} | "
            f"{fmt_num(m['endorsements'])} / {fmt_num(m['downloads'])} | {bank_s} | {summary} |")


HEADER = "| 名称（中文 / 原名） | 版本 | 最后更新 | 点赞 / 下载 | 改动的音效库 | 简介 |\n|---|---|---|---|---|---|"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=Path, default=ROOT / ".cache")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    args.cache.mkdir(exist_ok=True)

    mods_cache = args.cache / "mods.json"
    if args.refresh or not mods_cache.exists():
        mods_cache.write_text(json.dumps(fetch_all_mods(), ensure_ascii=False))
    all_mods = json.loads(mods_cache.read_text())
    mods = [m for m in all_mods if not m["adultContent"]]

    # 先用文本粗筛候选，只给候选拉压缩包文件列表
    cand = [m for m in mods if ((m.get("modCategory") or {}).get("name") in POPULAR_CATEGORIES
                                and m["endorsements"] >= POPULAR_MIN_ENDORSEMENTS) or LS_RE.search(f"{m['name']} {m.get('summary') or ''}")
            or AUDIO_RE.search(f"{m['name']} {m.get('summary') or ''}")
            or (m.get("modCategory") or {}).get("name") == "Audio"]
    paths_cache = args.cache / "paths.json"
    paths = json.loads(paths_cache.read_text()) if paths_cache.exists() and not args.refresh else {}
    todo = [m["modId"] for m in cand if str(m["modId"]) not in paths]
    with ThreadPoolExecutor(8) as ex:
        for mid, p in zip(todo, ex.map(fetch_archive_paths, todo)):
            paths[str(mid)] = p
    paths_cache.write_text(json.dumps(paths, ensure_ascii=False))

    groups = defaultdict(list)
    bank_users = defaultdict(list)
    for m in cand:
        p = paths.get(str(m["modId"]))
        banks = banks_of(p or [])
        m["_preview"] = p is not None
        sec = classify(m, banks)
        if sec:
            groups[sec].append((m, banks))
            for b in banks:
                bank_users[b].append(m["modId"])

    OUT_DIR.mkdir(exist_ok=True)
    with (OUT_DIR / "mods.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["节", "节名", "mod_id", "中文名", "原名", "版本", "首发日期", "最后更新", "点赞", "下载", "作者",
                    "Nexus分类", "改动的音效库", "可预览压缩包", "链接", "中文简介", "原文简介"])
        for sec in SECTIONS:
            for m, banks in sorted(groups[sec], key=lambda x: -x[0]["endorsements"]):
                zh = ZH.get(str(m["modId"]), {})
                cat_en = (m.get("modCategory") or {}).get("name") or ""
                w.writerow([sec, SECTIONS[sec][0], m["modId"], zh.get("name_zh", ""), m["name"], m["version"],
                            m["createdAt"][:10], m["updatedAt"][:10], m["endorsements"], m["downloads"], m["author"],
                            CATEGORY_ZH.get(cat_en, cat_en), " ".join(banks), "是" if m["_preview"] else "否",
                            f"https://www.nexusmods.com/{GAME_DOMAIN}/mods/{m['modId']}", zh.get("summary_zh", ""),
                            (m.get("summary") or "").replace("\n", " ")])

    total = sum(len(v) for v in groups.values())
    lines = [
        "# 《怪物猎人：荒野》现成 mod 大全（太刀与音频方向）",
        "",
        f"数据抓取日期：{date.today().isoformat()}。来源：Nexus Mods 公开 API。荒野分区共 {len(all_mods)} 个 mod，"
        f"其中非成人 {len(mods)} 个，本目录收录 {total} 个。成人内容已排除。",
        f"由 [`tools/build_catalog.py`](../tools/build_catalog.py) 自动生成，重新运行即可更新。完整明细见 [`mods.csv`](mods.csv)，可以用 Excel 打开筛选。",
        "",
        "**先看精选：** [PICKS.md](PICKS.md)，是人工挑出的太刀和音效方向推荐。",
        "",
        "**怎么看：**",
        f"- 最后更新带 ✅ 表示在 TU4（{TU4_DATE}）之后更新过，在当前版本可用的概率更高；没有 ✅ 的不代表不能用，但要看评论区确认。",
        "- “改动的音效库”是从压缩包文件列表读出来的音效库文件名（Wwise 音频包，位于 `natives/STM/Sound/Wwise/`）。**同一个音效库只能有一个 mod 生效**，后装的会覆盖先装的。",
        "- 几乎所有音频 mod 都需要 [REFramework](https://www.nexusmods.com/monsterhunterwilds/mods/93) 并在其菜单中勾选 Enable Loose File Loader（散件加载）；推荐用 [Fluffy Mod Manager](https://www.fluffyquack.com/) 管理。",
        "- “（无法预览）”：Nexus 对较新上传的文件换了存储路径，公开接口读不到压缩包内容，改了哪个库只能下载后自己看。",
        "- 每节内按点赞数从高到低排序。",
        "",
        "## 目录",
    ]
    for sec, (title, _) in SECTIONS.items():
        lines.append(f"- [{sec}. {title}（{len(groups[sec])}）](#{sec.lower()})")
    lines += ["- [冲突速查：热门音效库被哪些 mod 改动](#conflicts)", ""]

    for sec, (title, note) in SECTIONS.items():
        lines += [f'<a id="{sec.lower()}"></a>', f"## {sec}. {title}（{len(groups[sec])}）", ""]
        if note:
            lines += [note, ""]
        items = sorted(groups[sec], key=lambda x: -x[0]["endorsements"])
        if sec == "G":
            by_weapon = defaultdict(list)
            for m, banks in items:
                key = next((WEAPON_BANKS[b[:4]] for b in banks if b[:4] in WEAPON_BANKS), "未识别")
                by_weapon[key].append((m, banks))
            for wname in list(WEAPON_BANKS.values()) + ["未识别"]:
                if by_weapon.get(wname):
                    lines += [f"### {wname}（{len(by_weapon[wname])}）", "", HEADER]
                    lines += [row(m, b) for m, b in by_weapon[wname]]
                    lines.append("")
        else:
            lines.append(HEADER)
            lines += [row(m, b) for m, b in items]
            lines.append("")

    lines += ['<a id="conflicts"></a>', "## 冲突速查：热门音效库被哪些 mod 改动", "",
              "| 音效库 | 说明 | 改动它的 mod 数 | mod ID |", "|---|---|---|---|"]
    by_id = {m["modId"]: m for m in mods}
    for b, users in sorted(bank_users.items(), key=lambda x: -len(x[1]))[:30]:
        prefix = b.split(".")[0]
        desc = (f"{WEAPON_BANKS[prefix[:4]]}主音效库" if prefix[:4] in WEAPON_BANKS and prefix.endswith("_cmn_m") else
                "公共命中音" if prefix.startswith("hit_") else
                "武器公共音" if prefix == "weapon_cmn" else
                "BGM" if prefix.startswith("bgm") else
                "猎人语音" if prefix.startswith("player_") else "")
        ids = ", ".join(f"[{i}](https://www.nexusmods.com/{GAME_DOMAIN}/mods/{i})" for i in
                        sorted(set(users), key=lambda i: -by_id[i]["endorsements"]))
        lines.append(f"| `{b}` | {desc} | {len(set(users))} | {ids} |")
    lines.append("")

    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"收录 {total} 个 mod -> {OUT_DIR}", file=sys.stderr)
    print(Counter({k: len(v) for k, v in groups.items()}), file=sys.stderr)


if __name__ == "__main__":
    main()
