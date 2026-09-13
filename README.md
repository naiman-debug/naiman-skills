# naiman-skills

[中文](README.zh-CN.md) · [Installation & Updates (Chinese)](docs/安装与更新.md) · [GitHub Repository](https://github.com/naiman-debug/naiman-skills) · [Releases](https://github.com/naiman-debug/naiman-skills/releases) · [Contributing (Chinese)](CONTRIBUTING.md) · [Project Record (Chinese)](docs/项目记录.md)

This is Naiman's personal AI skills repository, sharing practical skills I made to solve real problems when working with AI on projects. This initial release is intended for people using Codex with local file access. Please note that the underlying skill definitions, templates, and per-skill documentation files remain primarily in Chinese, though you can ask Codex to converse and respond in English or your preferred language.

## Skill 1: Project Startup Standardization

When starting in an empty directory, I often struggle with where to place different files and when to formalize a project layout. As scattered ideas, draft requirements, reference notes, and demo files are added without prior conventions, AI assistants easily lose track of which reference materials to read and where new content should be written. This skill inspects existing project assets, respects your current conventions, and clarifies directory purposes, primary entry points, and reference locations along with clear maintenance guidelines. Whether starting fresh or introducing new materials mid-project, it reorganizes only the affected parts without tearing down your existing structure. Turning this workflow into a skill ensures both you and the AI immediately know where to begin, where files belong, and what indexes to update whenever directory layouts change.

## Skill 2: Project Day Closeout (Wrap-up)

Every time I finish a working session, related files have changed, but accompanying documentation, indexes, progress notes, and next steps rarely get updated at the same time. Returning to the project later, I used to waste time searching through earlier results just to recall what was completed and what was still untouched. This skill steps through recent work during wrap-up, updates documentation and indexes, and logs completed tasks alongside concrete next actions. With your explicit confirmation, it can also create a clean local Git commit for the task's stable files without pushing upstream or mixing in unrelated changes. Packaging this as a skill provides a clear handover record for your next session, saving you and the AI from reconstructing project state from scratch.

## Skill 3: Bubugao (Step-by-Step)

During technical discussions, answering a few questions does not mean key decisions have been thoroughly thought through: finding what is still missing and deciding what to discuss next usually lacks clear guidance. Existing terminology documents in a repository might also belong to an older phase or a different domain, risking confusing legacy assumptions with new requirements if referenced blindly. Bubugao is a modification of Matt Pocock's [grill-with-docs](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs), retaining its step-by-step interviewing, terminology clarification, and decision logging. It adds only two capabilities: a **Road** discussion route that tracks settled points, key gaps, immediate next priorities, and deferrable details; and a **Context suitability check** to verify whether existing documentation is relevant and current before using it. Bubugao keeps discussions moving in a clear direction, but it does not guarantee a complete requirements document and does not automatically start implementation.

## Skills List

- [Skill 1: Project Startup Standardization](skills/project-startup-standardization/README.md)
- [Skill 2: Project Day Closeout](skills/project-day-closeout/README.md)
- [Skill 3: Bubugao](skills/bubugao/README.md)

## Quick Start

After installing according to the [installation guide](docs/安装与更新.md), try these prompts in a practice project with Codex:

```text
Use $project-startup-standardization to inspect project materials and suggest
minimal directories, entry points, and indexes. Read-only; do not create files.
```

```text
Use $project-day-closeout to check today's work and resume position.
Do not modify files or Git. List completed items and missing gaps.
```

When you are ready to save the session's work:

```text
Use $project-day-closeout for a full closeout.
Organize and commit this task's deliverables, preserve others' edits, and do not push.
```

**Full closeout can create local Git commits.** Read-only audit and preparation modes will never commit; Git commits do not imply functional acceptance. The skills never delete or move files by default, never push automatically, and never schedule automated background jobs.

Shortest prompt for Bubugao:

```text
Use $bubugao to discuss this proposal. Outline key questions
and verify if existing Context is suitable. Discuss only; do not write files.
```

## Download and Installation

The first pre-release [v0.1.0 is available](https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0). Visit the release page, download **Source code (zip)** under Assets, and copy the required complete skill directories into your user skills directory (`~/.agents/skills`) or project `.agents/skills/`. Keep the downloaded root `LICENSE` file together with the package. The complete collection comprises five folders: the three main skills plus two required closeout helpers (`project-directory-closeout` and `project-git-closeout`). See [RELEASE_NOTES.md](RELEASE_NOTES.md) for full release details. Never copy the repository's root `AGENTS.md` into your workspace.

If a folder with the same name already exists in your destination directory, stop and compare it first. Avoid merging files between different versions.

Post-release verification confirmed that the downloaded v0.1.0 ZIP matches the reviewed 58-file package, and desktop tasks successfully performed read-only checks across explicit paths. Standalone CLI execution, nested automatic discovery, and other operating systems remain unverified; see the [project record](docs/项目记录.md) for full validation scope and remaining limits.

## Updates, Rollback, and Maintenance

GitHub releases do not update installed copies automatically; all updates must be performed manually. When updating, download the chosen release archive, move your existing skill folders to a backup location outside all skill-discovery directories to preserve your local edits, and replace the complete set of folders. Do not merge old and new files together. To roll back, restore the complete previous folder set from backup. Updating or removing a skill does not alter files or commits it previously created.

Public versions are maintained in this repository before being installed in personal environments. For development guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md). Our custom extensions are licensed under the [MIT License](LICENSE) (copyright naiman-debug), while bundled upstream Bubugao content retains [Matt Pocock's MIT License](skills/bubugao/LICENSE.upstream). Please report issues via [Issues](https://github.com/naiman-debug/naiman-skills/issues) or submit improvements via [Pull requests](https://github.com/naiman-debug/naiman-skills/pulls).
