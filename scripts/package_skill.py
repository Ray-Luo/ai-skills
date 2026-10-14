#!/usr/bin/env python3
"""Package one skill as a versioned ZIP containing a single top-level skill folder."""

import argparse
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", help="folder name under skills/")
    parser.add_argument("--version", required=True, help="semantic version, e.g. 1.0.0")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.skill):
        parser.error("skill must be a safe lowercase directory name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", args.version):
        parser.error("version must be MAJOR.MINOR.PATCH")

    source = ROOT / "skills" / args.skill
    if not (source / "SKILL.md").is_file():
        parser.error(f"missing {source / 'SKILL.md'}")

    output = ROOT / "dist" / f"{args.skill}-v{args.version}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(
        p for p in source.rglob("*")
        if p.is_file() and not p.is_symlink()
        and not any(part.startswith(".") or part == "__pycache__" for part in p.relative_to(source).parts)
    )
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, arcname=str(Path(args.skill) / path.relative_to(source)))
    with ZipFile(output) as archive:
        assert archive.testzip() is None, "ZIP checksum verification failed"
        assert f"{args.skill}/SKILL.md" in archive.namelist()
    print(f"Created {output} ({len(files)} files)")


if __name__ == "__main__":
    main()
