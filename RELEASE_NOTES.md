# 0.1.0 预发布说明

[v0.1.0预发布版已上线](https://github.com/naiman-debug/naiman-skills/releases/tag/v0.1.0)。这是该版本的更新说明。公开仓库为 [naiman-debug/naiman-skills](https://github.com/naiman-debug/naiman-skills)，实际可下载状态以 [Releases](https://github.com/naiman-debug/naiman-skills/releases) 的版本页为准；只有版本页出现相应条目才表示可以从GitHub下载。

## 本次提供

1. 项目建档：整理现有入口、目录职责、重要材料的来源和维护关系，优先复用已有文档。
2. 项目收工：同步责任记录与接续位置；明确授权后只提交本任务文件，保留无关改动。必须一起安装两个收工辅助技能。
3. 步步高：基于Matt Pocock的grill-with-docs，保留访谈、术语和重要决策记录，增加Road讨论路线与Context适用性检查。上游原文和MIT许可随包保留。

此次整理还修正了步步高上游参考被误发现为额外技能的问题；试用旧候选的用户需完整替换目录。收工安装依赖由主入口统一声明，Git辅助接受本次准备结果，避免反向依赖声明混淆。

完整安装组合为project-startup-standardization、project-day-closeout、project-directory-closeout、project-git-closeout、bubugao，共五个目录。写作候选和维护用发布准备技能不在此次公开包内。

## 安装与更新

首版面向Codex本地技能。下载确定版本的完整包，按[安装与更新](docs/安装与更新.md)操作。不要只替换SKILL.md或把新文件合并到旧目录；先保留本地修改，将旧组合移出发现目录，再安装完整新组合。GitHub发布更新不会自动更新电脑上的安装副本。

## 使用边界

- 先在练习目录只读试用，明确写入范围后再运行实际整理。
- 项目收工可能创建本地Git提交，不默认推送；缺依赖或未知暂存项会阻止受影响阶段。
- 步步高不保证保存完整需求，也不自动实现方案。
- 已验证的范围包括五个选定入口的干净宿主发现、桌面新任务对候选路径的显式读取和三个主技能调用及独立复核，以及整套更新回退的文件层和后续调用。独立 CLI、当前嵌套路径的自动发现、其他操作系统尚未验证。发布后已从实际ZIP下载并核对58文件一致，独立桌面任务在单独试装目录完成三个主技能显式路径只读调用，练习文件保持不变。具体范围见[项目记录](docs/项目记录.md)。
- 版本标签固定发布时的审核内容；本文件在主分支补充实际发布后验收状态，不移动v0.1.0标签。

## English

These are the 0.1.0 pre-release notes. Check [Releases](https://github.com/naiman-debug/naiman-skills/releases) for the actual release status. The package covers three user-facing skills: project startup, day closeout, and Bubugao; install all five listed directories for the complete set. Bubugao preserves Matt Pocock's upstream attribution and MIT license, adding only a discussion Road and Context suitability check. Updates are manual; a GitHub release does not update installed copies. The v0.1.0 pre-release is now published. Its downloaded ZIP matches the reviewed package; an independent desktop task installed all five folders and made explicit-path, read-only calls to the three main skills. This does not establish automatic discovery or cross-platform compatibility.
