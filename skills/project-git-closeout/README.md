# Git 收口（辅助技能）：执行已授权的本地提交

> **辅助技能**：由主技能 `project-day-closeout` 组织调用。本技能需要输入本次有效的 `git_readiness` 结果以及你的明确提交授权，不会自行启动收工流程。常规用户请直接使用主技能。

## 适用场景示例

在 `project-day-closeout` 生成有效的准备结果后，对本次任务归属明确且通过检查的文件，分批执行本地 Git 提交。

## 让 Codex 帮你安装

Git 收口通常与收工套件一同安装，请在 Codex 中使用以下请求：

```text
请从 https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0 下载 v0.1.0 源码 ZIP 并解压到技能发现目录之外的临时位置。
复制前请同时检查当前项目 `.agents/skills/` 与所有实际使用的用户技能发现路径（如 `~/.agents/skills/`）中是否已有收工相关同名目录；若存在请在复制前立即停止并提示比对，严禁覆盖或重复安装。
确认无同名后，将收工所需的 3 个完整目录（`skills/project-day-closeout`、`skills/project-directory-closeout`、`skills/project-git-closeout`）复制到当前项目 `.agents/skills/` 对应目录下。
完整保留各目录全部文件（含 SKILL.md、references 等）及下载包根目录 LICENSE，切勿复制根目录 AGENTS.md。
复制后报告实际读取的 SKILL.md 路径与 metadata.version，并执行首次只读检查，不修改业务文件或 Git 状态。
```

## 日常调用指令

**在已生成有效 readiness 且授权提交时：**
```text
本次任务已完成 project-day-closeout 并生成了有效 readiness。请使用 $project-git-closeout 对已就绪的具名文件执行本地 Git 提交。检查暂存区，严禁推送远程，不要夹带其他改动。
```

## 实用边界

- **输入前提**：必须依赖本次有效的 readiness 准备数据，缺少时不自行启动收工流程；readiness 本身不代表提交许可。
- **纯本地操作**：绝不推送远程；不执行 reset、clean 或改写历史；发现未知暂存项时保留现场并退出。

详细安装说明见 [GitHub 安装指南](https://github.com/naiman-debug/naiman-skills/blob/main/docs/%E5%AE%89%E8%A3%85%E4%B8%8E%E6%9B%B4%E6%96%B0.md)。

---

## English Summary

**Project Git Closeout** is an auxiliary skill that performs scoped local Git commits based on readiness data prepared by `project-day-closeout`. It requires an existing readiness input and explicit commit authorization, and does not start day-closeout by itself. It strictly commits local files without remote push or history rewrites.
