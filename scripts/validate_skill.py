#!/usr/bin/env python3
"""Validate a packaged Agent Skill (links, structure and ZIP/source parity)."""

import argparse
import re
import sys
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def validate(name: str, version: str) -> list[str]:
    errors = []
    source = ROOT / "skills" / name
    skill = source / "SKILL.md"
    archive = ROOT / "dist" / f"{name}-v{version}.zip"
    if not skill.is_file():
        return [f"Missing {skill}"]
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"\A---\nname: " + re.escape(name) + r"\n", text):
        errors.append("SKILL.md frontmatter name does not match folder")
    for token in ("`quick`", "`standard`", "`deep`", "`figure`", "`math`", "`compare`", "[P]", "[A]", "[R]", "[U]", "六问"):
        if token not in text:
            errors.append(f"Missing core marker in SKILL.md: {token}")
    sources = sorted(p for p in source.rglob("*") if p.is_file() and not p.is_symlink()
                     and not any(part.startswith(".") or part == "__pycache__" for part in p.relative_to(source).parts))
    for doc in [x for x in sources if x.suffix == ".md"]:
        content = doc.read_text(encoding="utf-8")
        for match in LINK.finditer(content):
            link = match.group(1).strip().split("#", 1)[0].split("?", 1)[0]
            if not link or re.match(r"^[a-zA-Z][a-zA-Z\d+.-]*:", link):
                continue
            target = (doc.parent / link).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.exists():
                errors.append(f"Broken local link: {doc.relative_to(ROOT)} -> {link}")
    if not archive.is_file():
        errors.append(f"Missing ZIP: {archive.relative_to(ROOT)}")
        return errors
    with ZipFile(archive) as zipf:
        bad = zipf.testzip()
        if bad:
            errors.append(f"CRC failure: {bad}")
        expected = {str(Path(name) / f.relative_to(source)): f for f in sources}
        actual = {f.filename for f in zipf.infolist() if not f.is_dir()}
        if expected.keys() != actual:
            errors.append(f"ZIP content mismatch: missing={sorted(expected.keys()-actual)}, extra={sorted(actual-expected.keys())}")
        for filename, local_file in expected.items():
            if filename in actual and zipf.read(filename) != local_file.read_bytes():
                errors.append(f"ZIP/source byte mismatch: {filename}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", help="Skill folder name under skills/")
    parser.add_argument("--version", required=True, help="X.Y.Z")
    args = parser.parse_args()
    errs = validate(args.skill, args.version)
    if errs:
        print("\n".join("ERROR: " + err for err in errs), file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {args.skill} v{args.version} — frontmatter, modes, local links, ZIP integrity, ZIP/source parity")


if __name__ == "__main__":
    main()
