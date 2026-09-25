#!/usr/bin/env python3
"""Check each skill's frontmatter and every relative Markdown link in the repo."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter")
        return {}
    fields, key = {}, None
    for line in match.group(1).splitlines():
        top = re.match(r"^([a-z_-]+):\s*(.*)$", line)
        if top:
            key, value = top.groups()
            fields[key] = "" if value in (">-", ">", "|", "|-") else value
        elif key and line.startswith(" "):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    fields = frontmatter(skill)
    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != skill.parent.name:
        errors.append(f"{skill}: name '{name}' does not match folder '{skill.parent.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{skill}: name must be lowercase letters, digits, and hyphens, at most 64 characters")
    if not description or len(description) > 1024:
        errors.append(f"{skill}: description must be 1 to 1024 characters (found {len(description)})")

for manifest in (ROOT / ".claude-plugin").glob("*.json"):
    try:
        json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{manifest}: invalid JSON ({exc})")

link = re.compile(r"\]\(([^)\s]+)\)")
for doc in ROOT.rglob("*.md"):
    if any(part.startswith(".") for part in doc.relative_to(ROOT).parts):
        continue
    for target in link.findall(doc.read_text(encoding="utf-8")):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        path = (doc.parent / target.split("#")[0]).resolve()
        if not path.exists():
            errors.append(f"{doc.relative_to(ROOT)}: broken link '{target}'")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All checks passed.")
