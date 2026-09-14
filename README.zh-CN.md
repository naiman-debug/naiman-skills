# naiman-skills：换一台电脑，继续用熟悉的 AI 技能

[English](README.md) · [安装与更新说明](docs/安装与更新.md) · [GitHub 仓库](https://github.com/naiman-debug/naiman-skills) · [Releases (v0.1.0 预发布)](https://github.com/naiman-debug/naiman-skills/releases) · [参与贡献](CONTRIBUTING.md) · [项目记录](docs/项目记录.md)

这是 Naiman 的个人 AI 技能库。主要用于在换电脑或配置新环境时，能够快速把平时用顺手的 AI 工作习惯重新装好。

## 技能快速选择

| 技能名称 | 适用场景 | 直观效果（示例） | 技能说明 |
|---|---|---|---|
| `技能 1：项目建档` | 刚建空目录，或零散笔记、草稿堆在根目录 | 理清当前入口并说明每个目录放什么，不乱挪历史文件 | [项目建档说明](skills/project-startup-standardization/README.md) |
| `技能 2：项目收工` | 准备收尾或保存阶段进展 | 同步项目原有的进度说明与索引，在授权下对本次改动作本地 Git 提交 | [项目收工说明](skills/project-day-closeout/README.md) |
| `技能 3：步步高` | 讨论技术方案或功能设计 | 先检查已有术语说明是否适合本次讨论，再逐步问清关键问题、按条件记录重要决定 | [步步高说明](skills/bubugao/README.md) |

*注：表中效果均为相应授权下的示例；仅在明确授权且准备就绪时才会执行本地 Git 提交。*

## 让 Codex 帮你安装

这是给具备文件与网络读写权限的 AI 助手的自然语言请求，不是命令行脚本或自动安装程序，执行时可能需要你确认本地权限：

```text
请从 https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0 下载 v0.1.0 源码 ZIP 并解压到技能发现目录之外的临时位置。
复制前请同时检查当前项目 `.agents/skills/` 与所有实际使用的用户技能发现路径（如 `~/.agents/skills/`）；若有同名目录请在复制前立即停止并提示比对，严禁覆盖或重复安装。
确认无同名后，将 5 个完整技能目录（`skills/project-startup-standardization`、`skills/project-day-closeout`、`skills/project-directory-closeout`、`skills/project-git-closeout`、`skills/bubugao`）复制到当前项目 `.agents/skills/` 下。
完整保留各目录内全部文件（含 agents、references、assets、模板）及下载包根目录 LICENSE，切勿复制根目录 AGENTS.md。
复制后报告实际读取的 SKILL.md 路径与 metadata.version，并执行首次只读检查，不修改任何业务文件或 Git 状态。
```

## 跨电脑使用与维护说明

- **先在练习项目试用**：推荐首选在当前项目的 `.agents/skills/` 安装；体验熟悉后，再根据需要决定是否安装到用户全局目录（`~/.agents/skills/`）。
- **哪些内容不随技能迁移**：安装技能仅复制技能指令；你的项目业务文件、开发进度、账号与登录凭据不会跟着技能迁移。
- **手动更新与回退**：对克隆仓库执行 `git pull` 不会更新已安装的副本。更新或回退时，请将本地修改备份到发现路径之外，再整体替换完整技能目录。
- **预发布版本说明**：`v0.1.0` 为预发布版本。GitHub main 分支现已更新中英双语介绍；v0.1.0 仍为现有的预发布版本，其 ZIP 下载包保留早期文档，技能实际执行行为保持不变。

## 验证与许可

已在 Codex 桌面端通过显式路径验证了受控测试场景；独立 CLI、多层嵌套目录自动发现及其他操作系统均未经验证，不承诺通用可移植性。三大核心技能均提供完整的中英文介绍，内部执行指令与配套参考文档仍以中文为主（详见[项目记录](docs/项目记录.md)）。本仓库扩展采用 [MIT 许可证](LICENSE)（版权归 naiman-debug 所有），步步高随附的上游内容保留 [Matt Pocock 的 MIT 许可证](skills/bubugao/LICENSE.upstream)。
