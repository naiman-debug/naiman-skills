---
name: project-directory-closeout
description: 用于具名目录收口、README与各级索引同步、文档保留分类和清理资格检查；完整项目收工由project-day-closeout统筹。
metadata:
  version: "0.1.0"
---

# 项目目录收口

本技能处理具名目录的日常整理。先核对项目 AGENTS 及存在时的 profile，读取目标目录入口、父级索引和相关 Git 变化。项目规则优先，缺少具体规则时采用下方通用参考。若 AGENTS、索引或 profile 缺失，可从目标 README、用户当前请求和具名目录确定最小范围；不因缺失自动创建项目规范、索引或 profile，并在结果中说明覆盖限制。来自完整收工时复用主执行者已提供的发现范围和基准，不重复扫描整个项目。

本技能可独立调用，不强制依赖 project-day-closeout。被完整收工调用时只返回本次目录结果，不反向启动收工流程，避免递归。

只读模式仅输出建议；日常模式按实际变化维护；批量模式须有用户对目录与操作的明确授权。索引按职责发现，普通结果JSON也可能是清单入口。入口路径不变但版本、状态、数量或覆盖关系变化时，也必须检查父索引。混合文档只更新当前部分，历史段落保留。并发写入、未交接和权限不足分别记录，不代替来源接收。

完成时说明实际覆盖、对账依据、已更新、无需更新、历史保留及受阻部分。无变化不改日期，不新建每次收工记录。下方术语保留以兼容已有调用。

Use this for named directories, touched directories, or task-end entropy cleanup.

## First Read

1. `AGENTS.md`, if present.
2. `.agents/project-profile.md`, if present.
3. Target directory README, if present.
4. Direct parent README or routing index, if present.
5. Git changed-file list when invoked after work.
6. Bundled fallback reference: `references/generic-directory-closeout.md`, when the project has no stronger local rules.

## Modes

Audit mode:

- inspect only;
- list current entrypoint, current source of truth, evidence/history, risks, stale paths, and recommended README changes;
- do not edit.

Routine closeout:

- update only hit-directory README files when entrypoint, status, current truth, risk, or next action changed;
- check the direct parent index when child paths, versions, status, counts, adoption or coverage relationships change, even if the entry path is unchanged; update affected summaries and references;
- discover local index duties through links, metadata and content, including lists inside ordinary result JSON; preserve historical sections in mixed documents;
- reuse discovery and baseline evidence supplied by day-closeout; standalone invocation stays within the named directory and reports coverage gaps;
- return facts to `project-day-closeout` when invoked from day closeout.

Bulk closeout:

- only when the user explicitly authorizes a named directory and operation;
- classify files before moving or deleting;
- unclear files stay in place;
- true deletion requires explicit authority, deletion eligibility, recovery proof, and exception review for high-risk files.

## Entropy Checks

Classify task-created docs as:

- `keep_current`
- `keep_trace`
- `absorb_into_readme_or_closeout`
- `archive_candidate`
- `delete_candidate_only`
- `delete_now_with_eligibility`
- `needs_owner_review`

Use `references/generic-directory-closeout.md` for README boundaries, staged cleanup terminology, and mode-specific allowed actions when no local rule is present.

## Output

```text
目录:
模式:
读取范围:
README 影响:
父级入口影响:
文件分类:
建议动作:
已更新:
索引核对依据与覆盖限制:
checked_no_update:
必须后续处理:
返回给 day-closeout 的摘要:
```

## Forbidden

- Do not rewrite every README.
- Do not make README a second source of truth.
- Do not delete files by default.
- Do not move files outside the named scope.
- Do not edit protected project files without explicit authorization.
