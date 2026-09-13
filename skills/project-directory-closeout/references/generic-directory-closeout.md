# 通用目录收口参考

以下默认规则用于项目没有更具体约定时。目录入口应说明用途、当前项、证据与历史、恢复位置和采用边界；不把长决策、原始聊天或删除清单复制进 README。状态标签和输出语言遵循项目或用户约定，兼容已有调用接口。

当前保留指仍有效的入口、规则和真值；追溯保留指唯一恢复或审核依据；待吸收指有用结论仍困在过程文档；归档候选与删除候选都只是建议，不产生真实操作授权。身份或用途未知时留在原位，等待责任人确认。先分类和核引用，再按具体授权移动或归档。删除须明确已获准、无有效引用或未知已披露、无未保留的唯一价值、有相应恢复位置。普通Markdown可按项目规则引用Git；原始证据、敏感材料、法律支付与未跟踪文件不能仅凭Git认定可删。

目录名称、文件名或被忽略状态不能证明文件可删除。每次收口不自动创建备份副本或一删一份记录，也不借目录治理重新验证所有业务内容。当前事实和历史记录分清，混合文档仅维护当前段落；无法核实的条件如实列出，不能把候选写成已执行。以下保留操作术语供精确映射。

Use this fallback when a project has no stronger local directory or document lifecycle rule.

## README Boundary

README files should answer:

- what this directory is for;
- what is current;
- what is evidence or history;
- where the next agent should start;
- what must not be treated as current truth.

Do not copy long decision records, chat history, deletion ledgers, or source-of-truth content into README.

## File Lifecycle Labels

| Label | Use for | Default action |
|---|---|---|
| `keep_current` | Current entrypoint, current rule, active source of truth | Keep or update |
| `keep_trace` | Final closeout, review verdict, unique recovery evidence | Keep with lifecycle |
| `absorb_into_readme_or_closeout` | Useful conclusion trapped in a process doc | Absorb then reassess |
| `archive_candidate` | Historical value, not active | Archive only with authority |
| `delete_candidate_only` | No active value, recoverable | Candidate, not deletion |
| `delete_now_with_eligibility` | Explicitly authorized, recoverable, no active refs | Delete only after checks |
| `needs_owner_review` | Ambiguous value or authority | Hold |

## Staged Cleanup Pattern

- `classify`: list files, target disposition, reason, active refs, and recovery path.
- `move_or_group`: move or group files only inside the named scope.
- `hold`: keep ambiguous files with a named exit condition.
- `delete`: treat true deletion as explicit authority plus eligibility, recovery proof, and exception review. Do not turn it into automatic backup or one-delete-one-trace.

## Deletion Readiness

A deletion candidate can move to true deletion only when:

- the user or project rule clearly authorizes deletion;
- active references are checked or declared unknown;
- the content is absorbed, obsolete, or has no unique value;
- ordinary tracked Markdown has a VCS recovery path if the project allows that;
- protected, sensitive, legal, payment, SEO, credential, external, untracked, or source-evidence files are blocked or manually reviewed.
