# naiman-skills: Your familiar AI skills, ready for another computer

[中文](README.zh-CN.md) · [Installation Guide (Chinese)](docs/安装与更新.md) · [GitHub Repository](https://github.com/naiman-debug/naiman-skills) · [Releases (v0.1.0 pre-release)](https://github.com/naiman-debug/naiman-skills/releases) · [Contributing](CONTRIBUTING.md) · [Project Record](docs/项目记录.md)

This is Naiman's personal AI skills repository. I built it so I can quickly download and use my familiar AI workflows whenever I switch machines or set up a new workspace.

## Quick Selection

| Skill | When to Use | Observable Example | Documentation |
|---|---|---|---|
| `Skill 1: Project Startup` | Starting in an empty folder or organizing scattered drafts | Identifies current notes and clarifies what each folder is for, without moving legacy files | [Skill 1 README](skills/project-startup-standardization/README.en.md) |
| `Skill 2: Project Day Closeout` | Wrapping up a session or saving milestone progress | Updates the project's existing progress notes and affected indexes, and can create a scoped local Git commit for authorized files | [Skill 2 README](skills/project-day-closeout/README.en.md) |
| `Skill 3: Bubugao` | Discussing technical choices or feature designs | Checks whether existing terminology notes fit the current discussion, steps through key questions, and records major decisions under appropriate conditions | [Skill 3 README](skills/bubugao/README.en.md) |

*Note: Examples above illustrate typical outcomes under appropriate authorization; full Git commits only occur when explicitly requested and ready.*

## Ask Codex to Install

This is a natural-language request for an AI agent with file and network access, not a shell script or automated installer. It may ask you to approve local file operations:

```text
Please download the v0.1.0 source ZIP from https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0 and unpack outside skill discovery directories.
Before copying, check my project's `.agents/skills/` AND all actually used user skill discovery paths (e.g. `~/.agents/skills/`) for same-named folders; if found, STOP before any copy to compare, with no overwriting or duplicate installs.
If clear, copy the five complete skill folders (`skills/project-startup-standardization`, `skills/project-day-closeout`, `skills/project-directory-closeout`, `skills/project-git-closeout`, `skills/bubugao`) into project `.agents/skills/`.
Preserve all folder files (agents, references, assets, templates) and keep the downloaded root LICENSE; do not copy root AGENTS.md into project.
After copying, report actual SKILL.md path and metadata.version, then run a first read-only check without modifying business files or Git.
```

## Multi-Computer Setup & Maintenance

- **Start in a Practice Project**: Install skills into your current project's `.agents/skills/` first. Installing globally into your user directory (`~/.agents/skills/`) across multiple projects is optional once you are comfortable.
- **What Travels**: Installing skills only copies execution instructions. Your code, work progress, API keys, and logins do not travel with skills.
- **Manual Updates**: Running `git pull` on a cloned repository does not update installed skill folders. To update or roll back, back up your local modifications outside discovery paths and replace the complete directory set.
- **Pre-release Notice**: Version `v0.1.0` is published on GitHub as a pre-release. The GitHub main branch has been updated with bilingual introductions, while v0.1.0 remains the current prerelease and its ZIP package retains earlier documentation; skill execution behavior is unchanged.

## Support & License

Tested on Codex desktop using explicit skill paths across scoped test cases. Standalone CLI, automatic discovery in nested directories, and other operating systems are not verified; no universal portability is claimed. The three core skills provide complete Chinese and English introductions, while skill execution instructions and supporting references remain primarily in Chinese (see [Project Record](docs/项目记录.md)). Custom additions are licensed under the [MIT License](LICENSE) (copyright naiman-debug), and upstream Bubugao components retain [Matt Pocock's MIT License](skills/bubugao/LICENSE.upstream).
