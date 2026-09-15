# naiman-skills

[English](README.md) · [安装与更新](docs/安装与更新.md) · [GitHub 仓库](https://github.com/naiman-debug/naiman-skills) · [Releases](https://github.com/naiman-debug/naiman-skills/releases) · [参与贡献](CONTRIBUTING.md) · [项目记录](docs/项目记录.md)

这是 Naiman 的个人技能库，分享我为解决自己与 AI 协作时遇到的问题而制作的技能。首版供在本地使用 Codex 的人试用。技能的 `SKILL.md` 指令和模板目前主要使用中文编写，但你也可以让 Codex 以你需要的语言进行交互。

## 技能 1：项目建档

刚建新项目时，我经常不知道各类文件该往哪里放，也拿不准到底什么时候该开始规划结构。随着零散的想法、需求、参考资料和演示文件陆续加入，如果事先没有约定，AI 介入后就很容易分不清该读取哪份资料、又该把新内容写到哪里。这个技能会从现有材料出发，沿用项目已有的规则，梳理出各目录的实际用途、项目入口、重要材料的位置和来源，并明确后续的维护方式。无论是项目刚起步，还是中途加入新材料、微调目录，它都只针对受影响的部分做必要整理，不需要每次推翻重来。把它固定成技能，就是为了在目录结构发生变化时，能随时让自己和 AI 知道从哪里开始、文件放在哪里、改完以后还要更新什么。

## 技能 2：项目收工（打完收工）

每次一项工作做完，虽然相关文件已经修改，但配套的说明、索引、当前进度和下一步计划往往没能同步更新。等到下次重新打开项目，我又得重新翻找上一轮的结果，逐一确认哪些已经做完、哪些还没开始。这个技能会在准备收尾时核对这次做了什么，同步相关说明、索引和进度，明确已完成项和接下来的具体动作。在得到我的明确授权与要求后，它还可以把本任务相关的稳定文件做一次本地 Git 提交，不默认推送，也不混入无关改动。把它做成技能，是想让每次工作结束后都留下清晰的交接记录，方便下次自己或 AI 接着做，不用再从一堆文件里找进度。

## 技能 3：步步高

讨论一个方案时，回答了几个问题，并不意味着已经把关键事情想清楚：还缺什么、下一步该聊什么，往往没有明确的提示。项目里虽然有术语文档，也可能属于旧阶段或另一个业务范围，直接接着写容易把新旧理解混在一起。步步高基于 Matt Pocock 的 [grill-with-docs](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs) 修改，保留原版逐步访谈、澄清术语和记录重要决定的方式。在此基础上只增加两项能力：**Road 讨论路线**帮助看清已明确内容、关键缺口、下一步和可后续处理的细节；**Context 适用性检查**先核实已有术语文档是否属于本次讨论、仍然有效，再说明如何使用及实际记录位置。它帮助讨论有方向地继续，但不保证保存完整需求，也不自动进入开发。

## 技能列表

- [技能 1：项目建档](skills/project-startup-standardization/README.md)
- [技能 2：项目收工（打完收工）](skills/project-day-closeout/README.md)
- [技能 3：步步高](skills/bubugao/README.md)

## 先试一次

按[安装与更新教程](docs/安装与更新.md)安装后，在练习项目中向 Codex 输入：

```text
使用 $project-startup-standardization，先看看这个项目有哪些材料，
建议最少需要的目录、入口和索引。这次先只读，不创建文件。
```

```text
使用 $project-day-closeout，只检查今天的工作和接续位置，
不修改文件，不暂存，不提交。告诉我哪些已完成，哪些还缺。
```

确认需要实际保存本段工作时，再说：

```text
使用 $project-day-closeout 完整收工。
仅整理和提交本次任务的成果，保留其他人的改动，不推送远程。
```

**完整收工可能创建本地 Git 提交。** 只检查与只准备模式不会提交；Git 提交也不等于功能已验收。技能不默认删除、迁移文件，不自动推送，不创建定时任务。

步步高的最短调用示例：

```text
使用 $bubugao 帮我讨论这个方案，先说明还有哪些关键问题，
并检查已有 Context 是否适用。这次只讨论，不写文件。
```

## 下载和安装

GitHub main 分支现已更新中英双语介绍；v0.1.0 仍为现有的预发布版本，其 ZIP 下载包保留早期文档，技能实际执行行为保持不变。

首个预发布版 [v0.1.0 已上线](https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0)。打开版本页，在 Assets 中下载 **Source code (zip)**，按教程将需要的完整技能目录复制到用户级目录（`~/.agents/skills`）或项目级目录（`.agents/skills/`）。请将下载包中的根目录 `LICENSE` 文件一并保留。全套技能共包含五个目录：三个主技能以及两个收工辅助技能（`project-directory-closeout` 与 `project-git-closeout`）；完整说明见 [RELEASE_NOTES.md](RELEASE_NOTES.md)。切勿将仓库根目录的 `AGENTS.md` 复制到你的项目中。

如果目标位置已存在同名目录，请先停止并比对差异，不要直接混叠合并两个版本。

发布后验证确认下载的 v0.1.0 ZIP 与评审过的 58 个文件一致，并在桌面任务中通过显式路径顺利完成了三主技能的只读调用验证。独立的 CLI 命令行调用、嵌套路径下的自动发现以及其他操作系统暂未验证；详见[项目记录](docs/项目记录.md)。

## 更新与维护

GitHub 的新发布不会自动更新已安装的副本，所有更新需手动进行。下载新版本后，请先将现有技能目录备份到所有技能发现路径之外以保留你的本地修改，并采用整目录替换而非新旧文件混叠合并。如需回退，从备份中恢复上一版本的完整目录即可。更新或删除技能不会撤销此前生成的文件或 Git 提交。

公开版本在本仓库维护，再按需安装到个人环境。开发与提交流程见[贡献指南](CONTRIBUTING.md)。本仓库扩展采用 [MIT 许可证](LICENSE)（版权归 naiman-debug 所有），步步高随附的上游内容保留 [Matt Pocock 的 MIT 许可](skills/bubugao/LICENSE.upstream)。欢迎通过 [Issues](https://github.com/naiman-debug/naiman-skills/issues) 报告问题或通过 [Pull requests](https://github.com/naiman-debug/naiman-skills/pulls) 提交改进。
