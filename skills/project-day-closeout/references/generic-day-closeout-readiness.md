# 收工后的Git准备结果

沿用项目已有同义记录或当前对话即可，不新建readiness日志文件。下面保留旧调用方认识的字段，再增加模式、授权、并发核对与残余项。记录对应本次实际文件状态，不能直接复用上轮readiness。

```yaml
git_readiness:
  execution_mode: full / readiness_only / audit
  caller: 用户完整收工 / 项目主Agent / 内部调用方
  commit_authority_source: 具体请求或现行项目授权；缺失则明确写缺失
  ready_for_git_closeout: true / false
  should_commit: true / false
  base_head: 当前HEAD；无提交时明确标记
  changed_files: 本任务精确文件列表
  validation_done: 已完成的必要检查及证据
  validation_missing: 未验证项及是否阻止本批提交
  entropy_check: 受影响目录和中间文档的处理结果
  index_coverage: 已发现的职责入口、覆盖目录、排除项与未核实范围
  index_baseline: 上次核对时点、可解析Git或清单版本；缺基准时的路径对账范围
  index_results: 各入口已更新/核对后无需更新/历史保留/未核实及依据
  must_close_before_git: 暂缓项及原因
  suggested_batches: 每批精确路径、主题、ready状态、授权及验证依据
  deleted_markdown: 删除路径；没有则为空
  deletion_eligibility: 逐项资格或阻塞
  recovery_proof: 具体可恢复位置及其覆盖范围
  exception_review: 特殊对象的授权和核验结果；没有则为空
  remaining_unowned_changes: 其他任务或归属不清的变化
  checked_no_update: 已检查但无需修改的入口
  push_allowed: false
```

`ready_for_git_closeout`说明具名批次准备状态，`should_commit`另看模式、授权、是否有实际变化及是否ready。只准备模式可以ready为true、should_commit为false；无变化应明确无需提交。存在多个批次时分别判断，不能用一个批次的PASS放行其他批次。

实际暂存前再次核对HEAD、暂存区和具名文件内容；可用diff或指纹确认验证后未变化。未知暂存项不清空、不夹带提交；发现并发改动先返回主Agent处理。

以下情况本批不能提交：必需验证失败或缺失、文件仍在变化、内容/接收归属不清、受保护操作无授权、无恢复依据的删除，或混入不相关变化。仅列出“验证缺失”不等于通过。非阻塞的未验证层要与本批已验证结论分开说明。

已有删除变更时逐项记录：

```yaml
deleted_markdown:
  path:
  eligibility: eligible / blocked / needs_review
  absorbed_by:
  recovery_proof:
  exception_review:
```

普通已跟踪Markdown在项目允许时可引用具体版本作为恢复依据；敏感、受保护、外部、未跟踪、法律/支付/SEO证据、凭据和原始来源不能仅凭“有Git”认定可恢复。blocked或needs_review的删除不暂存；收工不会执行新的删除。
