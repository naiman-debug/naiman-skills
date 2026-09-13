"""Validate this repository's simple skill conventions; no third-party packages.

This is not a full YAML parser, a secret scanner, or a behavioral test runner.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote


LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
VERSION = re.compile(r"\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?\Z")


def scalar(text: str, key: str, indent: int = 0) -> str | None:
    """Read the single-line scalar convention used by this repository."""
    matches = re.findall(rf"^{' ' * indent}{re.escape(key)}: *(.+?) *$", text, re.M)
    if len(matches) != 1:
        return None
    value = matches[0]
    if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value.strip()


def validate(root: Path) -> tuple[list[str], int]:
    root = root.resolve()
    errors: list[str] = []
    skill_root = root / "skills"
    version_file = root / "VERSION"
    if not version_file.is_file():
        return ["缺少根 VERSION"], 0
    version = version_file.read_text(encoding="utf-8").strip()
    if not VERSION.fullmatch(version):
        errors.append("VERSION 不是约定的版本号")
    if not skill_root.is_dir():
        return errors + ["缺少 skills/"], 0
    skills = sorted(p for p in skill_root.iterdir() if p.is_dir())
    if not skills:
        errors.append("skills/ 中没有技能")
    names = {p.name for p in skills}
    for skill in skills:
        rel = skill.relative_to(root).as_posix()
        if not NAME.fullmatch(skill.name) or len(skill.name) > 64:
            errors.append(f"{rel}: 目录名称不符合约定")
        entry = skill / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{rel}: 缺少 SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not front:
            errors.append(f"{rel}: 缺少 frontmatter")
            continue
        meta = front.group(1)
        if scalar(meta, "name") != skill.name:
            errors.append(f"{rel}: name 与目录不一致")
        description = scalar(meta, "description")
        if not description or len(description) > 1024:
            errors.append(f"{rel}: description 应为1到1024字符的单行说明")
        nested = re.search(r"^metadata:\s*\n((?:[ \t]+[^\n]*\n?)+)", meta, re.M)
        metadata = nested.group(1) if nested else ""
        if scalar(metadata, "version", 2) != version:
            errors.append(f"{rel}: metadata.version 与根 VERSION 不一致")
        requires = scalar(metadata, "requires", 2)
        if re.search(r"^  requires:", metadata, re.M) and not requires:
            errors.append(f"{rel}: requires 应为非空逗号分隔字符串，无依赖则省略")
        for dependency in (requires or "").split(","):
            dependency = dependency.strip()
            if dependency and dependency not in names:
                errors.append(f"{rel}: 声明的依赖 {dependency} 未打包")
        if not (skill / "README.md").is_file():
            errors.append(f"{rel}: 缺少使用说明 README.md")
        ui = skill / "agents" / "openai.yaml"
        if not ui.is_file():
            errors.append(f"{rel}: 缺少 agents/openai.yaml")
        else:
            ui_text = ui.read_text(encoding="utf-8")
            for field in ("display_name", "short_description", "default_prompt"):
                if not scalar(ui_text, field, 2):
                    errors.append(f"{rel}: UI缺少单行字段 {field}")
            if f"${skill.name}" not in ui_text:
                errors.append(f"{rel}: 默认提示未引用自身技能")
        for file in skill.rglob("*"):
            if file.is_file() and file.name.lower() == "skill.md" and file != entry:
                errors.append(f"{file.relative_to(root)}: 嵌套SKILL.md会被发现为额外技能；参考原文请使用其他文件名")
            if not file.is_file() or file.suffix not in {".md", ".yaml", ".yml"}:
                continue
            body = file.read_text(encoding="utf-8")
            # Reject an author-specific path/model without echoing potentially private text.
            if re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|/(?:Users|home)/[^\s/]+/|gpt-\d[^\s`\"']*", body):
                errors.append(f"{file.relative_to(root)}: 含绝对个人路径或固定模型标识，请检查")

    for md in root.rglob("*.md"):
        if any(part in {".git", ".agents", ".claude", ".codex", "__pycache__"}
               for part in md.relative_to(root).parts):
            continue
        # Output templates may intentionally refer to future project files.
        if "templates" in md.relative_to(root).parts:
            continue
        body = md.read_text(encoding="utf-8")
        body = re.sub(r"```.*?```", "", body, flags=re.S)
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        for match in LINK.finditer(body):
            target = match.group(1).strip()
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{md.relative_to(root)}: 相对链接越出仓库")
            elif not resolved.exists():
                errors.append(f"{md.relative_to(root)}: 本地链接目标不存在: {target}")
    return errors, len(skills)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, count = validate(args.root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"静态检查未通过：{len(errors)}项；不是行为测试。")
        return 1
    print(f"静态检查通过：{count}个技能。未验证真实调用、外链或完整隐私边界。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
