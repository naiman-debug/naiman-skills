# naiman-skills

Practical AI skills for starting a project, wrapping up work, and discussing a plan.

[中文](README.md) · [Repository](https://github.com/naiman-debug/naiman-skills) · [Releases](https://github.com/naiman-debug/naiman-skills/releases) · [Contribution guide (Chinese)](CONTRIBUTING.md)

**Repository:** [naiman-debug/naiman-skills](https://github.com/naiman-debug/naiman-skills). **0.1.0 pre-release notes:** [RELEASE_NOTES.md](RELEASE_NOTES.md). Check [Releases](https://github.com/naiman-debug/naiman-skills/releases) for the actual availability of a version; a public repository does not by itself mean that a release exists. The initial target is Codex with local file access. Other clients are not verified. Instructions and templates are primarily Chinese; you can ask Codex to respond in your preferred language.

Static checks and controlled practice-project runs cover the selected skills, including a scoped multi-turn Bubugao test. A clean host discovered all five selected skill folders. A new Codex desktop task explicitly read the candidate paths and ran all three main skills; an independent reviewer checked the tool outputs and resulting files. The complete update and rollback exercise also checked file replacement, retained local changes, and subsequent explicit calls. Standalone CLI invocation, automatic discovery from the current nested test path, other operating systems, and download-and-install acceptance from an actual Release remain unverified; see the [project record](docs/项目记录.md) for scope and remaining limits.

## Skills

| Skill | Purpose | Required installation |
| --- | --- | --- |
| [project-startup-standardization](skills/project-startup-standardization/README.md) | Organize project materials, entry points and useful indexes | The complete skill folder |
| [project-day-closeout](skills/project-day-closeout/README.md) | Reconcile work, record the next step and make authorized local commits | This skill plus both helpers below |
| [project-directory-closeout](skills/project-directory-closeout/README.md) | Reconcile a named directory and its parent index | Standalone or as a closeout helper |
| [project-git-closeout](skills/project-git-closeout/README.md) | Commit only scoped, validated changes | The complete three-skill closeout set |
| [Bubugao — 步步高](skills/bubugao/README.md) | Guide a discussion with a compact Road and check whether existing Context documents apply | The complete bubugao folder, including bundled upstream references and license |

## Bubugao: based on grill-with-docs

Bubugao is our modification of Matt Pocock's [grill-with-docs](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs), retaining its interviewing, terminology clarification, and important decision records. It adds only two capabilities: a **Road** that tracks settled points, key gaps, the next discussion priority, and deferrable details; and a **Context suitability check** that checks document scope, currency, purpose, and conflicts before using it. Road is not a full requirements specification, and discussion does not automatically start implementation.

Invoke with `$bubugao`. Original guidance and templates are bundled with [Matt Pocock's MIT license](skills/bubugao/LICENSE.upstream); no separately installed upstream skills are required. This is a modified version, not an official upstream release.

## Manual installation

When a chosen version appears in [Releases](https://github.com/naiman-debug/naiman-skills/releases), download its tagged ZIP and extract it outside your skills directory. Copy only the required complete folders from `skills/` into your user skills directory (`~/.agents/skills`) or a practice project's `.agents/skills/`. Keep the downloaded LICENSE with the package. Never copy the repository's root AGENTS.md into your project as an installation step.

If a folder with the same name already exists, stop and compare it first. Do not merge two versions. Avoid duplicate installations in both user and project scopes. Codex detects skill changes; restart it if the update does not appear. See [official local skills guidance](https://learn.chatgpt.com/docs/build-skills).

Try this in a practice project:

```text
Use $project-startup-standardization to inspect this project and propose
the minimum useful structure. Read only; do not create or change files.
```

```text
Use $project-day-closeout in audit mode. Do not modify files or Git.
Explain completed work, missing information and the next step in English.
```

An explicit **full closeout can create local Git commits**. Audit is read-only; readiness-only does not stage or commit. These skills do not push by default, delete or move files automatically, or schedule future runs. Git must already be initialized and configured for commits.

## Updates and rollback

A GitHub release does not update installed copies. Download the chosen release, review its notes, and move the old required skill folders to a backup outside every skill discovery directory. Copy the complete new set, check `metadata.version` in each SKILL.md, and test in a practice project. If you customized a skill, compare and preserve those edits before replacing it. Restore the complete previous set to roll back. Updating or removing a skill does not undo files or commits it previously produced.

Detailed instructions: [Installation and updates (Chinese)](docs/安装与更新.md). Contributions are welcome through [Issues](https://github.com/naiman-debug/naiman-skills/issues) and [pull requests](https://github.com/naiman-debug/naiman-skills/pulls). See the [project record](docs/项目记录.md) for validation coverage and limitations.

Our extensions are licensed under [MIT](LICENSE), copyright naiman-debug. Bundled upstream content retains [Matt Pocock's MIT license](skills/bubugao/LICENSE.upstream).
