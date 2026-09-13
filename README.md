# naiman-skills

这是 Naiman 的个人技能库，分享我为解决自己与 AI 协作时遇到的问题而制作的技能。

[English](README.en.md) · [安装与更新](docs/安装与更新.md) · [GitHub 仓库](https://github.com/naiman-debug/naiman-skills) · [Releases](https://github.com/naiman-debug/naiman-skills/releases) · [参与贡献](CONTRIBUTING.md) · [项目记录](docs/项目记录.md)

## 技能 1：项目建档

刚建空目录时，我经常不知道各类文件该往哪里放，也拿不准到底什么时候该开始规划结构。随着零散的想法、需求、参考资料和演示文件陆续加入，如果事先没有约定，AI 介入后就很容易分不清该读取哪份资料、又该把新内容写到哪里。

这个技能会从现有材料出发，沿用项目已有的规则，梳理出各目录的实际用途、项目入口、重要材料的位置和来源，并明确后续的维护方式。无论是项目刚起步，还是中途加入新材料、微调目录，它都只针对受影响的部分做必要整理，不需要每次推翻重来。把它固定成技能，就是为了在目录结构发生变化时，能随时让自己和 AI 知道从哪里开始、文件放在哪里、改完以后还要更新什么。

## 技能 2：项目收工（打完收工）

每次一项工作做完，虽然相关文件已经修改，但配套的说明、索引、当前进度和下一步计划往往没能同步更新。等到下次重新打开项目，我又得重新翻找上一轮的结果，逐一确认哪些已经做完、哪些还没开始。

这个技能会在准备收尾时核对这次做了什么，同步相关说明、索引和进度，明确已完成项和接下来的具体动作。在得到我的明确授权与要求后，它还可以把本任务相关的稳定文件做一次本地 Git 提交，不默认推送，也不混入无关改动。把它做成技能，是想让每次工作结束后都留下清晰的交接记录，方便下次自己或 AI 接着做，不用再从一堆文件里找进度。

## 技能 3：步步高

讨论一个方案时，回答了几个问题，并不意味着已经把关键事情想清楚：还缺什么、下一步该聊什么，往往没有明确的提示。项目里虽然有术语文档，也可能属于旧阶段或另一个业务范围，直接接着写容易把新旧理解混在一起。

步步高基于 Matt Pocock 的 [grill-with-docs](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs) 修改，保留原版逐步访谈、澄清术语和记录重要决定的方式。在此基础上只增加两项能力：**Road 讨论路线**帮助看清已明确内容、关键缺口、下一步和可后续处理的细节；**Context 适用性检查**先核实已有术语文档是否属于本次讨论、仍然有效，再说明如何使用及实际记录位置。它帮助讨论有方向地继续，但不保证保存完整需求，也不自动进入开发。

## 技能列表

- [技能 1：项目建档](skills/project-startup-standardization/README.md)
- [技能 2：项目收工（打完收工）](skills/project-day-closeout/README.md)
- [技能 3：步步高](skills/bubugao/README.md)

## 先试一次

按[教程](docs/安装与更新.md)安装后，在练习项目中向 Codex 输入：

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

## 下载和更新

首版采用下载固定 Release、复制完整技能目录的方式。公开仓库为 [naiman-debug/naiman-skills](https://github.com/naiman-debug/naiman-skills)，请从 [Releases](https://github.com/naiman-debug/naiman-skills/releases) 选择实际出现的固定版本下载。`0.1.0` 的预发布说明见 [RELEASE_NOTES.md](RELEASE_NOTES.md)，实际发布状态以版本页为准；版本页尚无该版本时，不要把候选源码或一直变化的主分支当成已发布版本。

发布后，GitHub 新版本与电脑里的安装副本分别更新：下载新版不等于安装新版，`git pull` 也不会更新另外复制出去的技能。安装、同名冲突、版本检查、升级和回退步骤见[安装与更新](docs/安装与更新.md)。

## 项目怎样维护

公开版本在本仓库维护，再按需安装到个人环境。不要把整个用户级技能目录、私人项目材料、聊天记录或真实凭据提交进来。

新增技能、修改现有技能、验证、发布与 PR 的具体步骤在[贡献指南](CONTRIBUTING.md)。当前建设进度、已确认范围和验证限制在[项目记录](docs/项目记录.md)。

本仓库扩展采用 [MIT 许可证](LICENSE)，版权署名为 naiman-debug。步步高随附的上游内容保留 Matt Pocock 的 [MIT 许可](skills/bubugao/LICENSE.upstream)。欢迎通过 [Issues](https://github.com/naiman-debug/naiman-skills/issues) 报告问题，或通过 [Pull requests](https://github.com/naiman-debug/naiman-skills/pulls) 提交改进。
