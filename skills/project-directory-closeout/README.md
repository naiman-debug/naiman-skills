# 项目目录收口（辅助技能）：整理单个具名目录

> **辅助技能**：由主技能 `project-day-closeout` 统筹调用。常规用户日常收尾请直接使用主技能；若只需精细整理某个具名目录，可独立调用本技能。

## 适用场景示例

例如刚更新完 `docs/reports`，需要核对该目录的 README 是否指向最新报告，并检查直接父级索引是否需要同步。

## 让 Codex 帮你安装

本技能可单独安装，也可作为收工套件的一部分安装：

```text
请从 https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0 下载 v0.1.0 源码 ZIP 并解压到技能发现目录之外的临时位置。
复制前请同时检查当前项目 `.agents/skills/` 与所有实际使用的用户技能发现路径（如 `~/.agents/skills/`）中是否已有 `project-directory-closeout`；若存在请在复制前立即停止并提示比对，严禁覆盖或重复安装。
确认无同名后，将 `skills/project-directory-closeout` 完整目录复制到当前项目 `.agents/skills/project-directory-closeout`。
保留目录内全部文件（含 SKILL.md、references 等）及下载包根目录 LICENSE，切勿复制根目录 AGENTS.md。
复制后报告实际读取的 SKILL.md 路径与 metadata.version，并执行首次只读检查，不修改业务文件或 Git 状态。
```

## 日常调用指令

**1. 只读检查（audit）：**
```text
使用 $project-directory-closeout 检查 docs/reports 目录：确认 README 是否指向当前报告，父级索引是否受影响。本次只读，不修改文件。
```

**2. 目录收口（routine）：**
```text
使用 $project-directory-closeout 对 docs/reports 目录进行收口，同步本次改动影响到的 README 与直接父级索引。
```

## 实用边界

- 只读模式不修改任何文件；日常收口仅更新目标目录及其直接父级索引，不扫描整个项目。
- 不默认删除文件；批量移动或归档需要明确授权。

详细安装说明见 [GitHub 安装指南](https://github.com/naiman-debug/naiman-skills/blob/main/docs/%E5%AE%89%E8%A3%85%E4%B8%8E%E6%9B%B4%E6%96%B0.md)。

---

## English Summary

**Project Directory Closeout** is an auxiliary skill for updating READMEs and direct parent indexes in a specific named folder. It is normally orchestrated by `project-day-closeout`, but can also run independently for focused cleanups. It never deletes files by default and does not rewrite unrelated project files.
