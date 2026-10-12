"""根据映射表，把自己的音频复制到 mhws-sound-tool 工程目录的 replace/ 下。

用法:
    python build_replace_dir.py <映射表.csv> <Wp03_Cmn_m.sbnk.1.X64.project 目录> [--dry-run]

映射表至少需要两列（列名固定）:
    wem_id      Sound Debugger 里看到的唯一 WEM ID（纯数字）
    audio_file  你自己的音频文件路径（相对路径以映射表所在目录为基准）
其余列（例如“招式”“备注”）会被忽略，可随意填写。wem_id 或 audio_file 为空的行会被跳过。

生成的文件名为 <wem_id>.<扩展名>，这正是 mhws-sound-tool v0.2.x 的
“按唯一ID替换”命名规则（不加方括号）。之后把整个 .project 目录拖到
mhws-sound-tool.exe 上即可打包出 <原文件名>.new。
"""

import argparse
import csv
import shutil
import sys
from pathlib import Path

SUPPORTED_EXTS = {".wem", ".wav", ".mp3", ".ogg", ".flac", ".aac"}


def load_rows(map_path: Path):
    # utf-8-sig: 兼容 Excel 另存为 CSV 时带的 BOM
    with map_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = {"wem_id", "audio_file"} - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"映射表缺少列: {', '.join(sorted(missing))}")
        for line_no, row in enumerate(reader, start=2):
            wem_id = (row.get("wem_id") or "").strip()
            audio = (row.get("audio_file") or "").strip()
            if not wem_id or not audio:
                continue
            yield line_no, wem_id, audio


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mapping", type=Path)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="只检查不复制")
    args = parser.parse_args(argv)

    project_dir = args.project_dir
    if not (project_dir / "project.json").is_file():
        raise SystemExit(f"{project_dir} 不是 mhws-sound-tool 解包出的工程目录（找不到 project.json）")
    existing_ids = {
        p.stem.split("]", 1)[1] for p in project_dir.glob("[[]*[]]*.wem") if "]" in p.stem
    }

    errors, plan, seen = [], [], {}
    for line_no, wem_id, audio in load_rows(args.mapping):
        if not wem_id.isdigit():
            errors.append(f"第{line_no}行: wem_id '{wem_id}' 不是纯数字")
            continue
        if wem_id not in existing_ids:
            errors.append(f"第{line_no}行: wem_id {wem_id} 不在这个音效库里（是不是选错了 sbnk？）")
            continue
        if wem_id in seen:
            errors.append(f"第{line_no}行: wem_id {wem_id} 与第{seen[wem_id]}行重复")
            continue
        seen[wem_id] = line_no
        src = Path(audio)
        if not src.is_absolute():
            src = args.mapping.parent / src
        if not src.is_file():
            errors.append(f"第{line_no}行: 找不到音频文件 {src}")
            continue
        ext = src.suffix.lower()
        if ext not in SUPPORTED_EXTS:
            errors.append(f"第{line_no}行: 不支持的格式 {ext}（支持 {', '.join(sorted(SUPPORTED_EXTS))}）")
            continue
        plan.append((src, project_dir / "replace" / f"{wem_id}{ext}"))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if not plan:
        print("映射表里没有可用的行（wem_id 和 audio_file 都要填）")
        return 1

    for src, dst in plan:
        print(f"{src} -> {dst}")
        if not args.dry_run:
            dst.parent.mkdir(exist_ok=True)
            shutil.copyfile(src, dst)
    print(f"{'将' if args.dry_run else '已'}放入 {len(plan)} 个替换文件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
