# 参考来源与设计选择

查阅日期：2026-09-05。以下官方资料用于说明可借鉴的实践；项目仍应按实际框架版本和需要核对官方文档。

| 官方参考 | 支持的做法 | 本技能如何使用 |
| --- | --- | --- |
| [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) | 区分原始、中间、处理后数据与报告 | 借鉴数据生命周期分区，不复制机器学习专用目录 |
| [DVC 流水线文件](https://doc.dvc.org/user-guide/project-structure/dvcyaml-files) | 明确步骤输入、输出及记录状态 | 借鉴上游依赖；项目可用已有清单或批次记录，不声称等价 DVC |
| [Next.js 项目结构](https://nextjs.org/docs/app/getting-started/project-structure) | 路由、公开资源与可选源码目录约定 | 尊重框架实际目录，避免公开中间资料 |
| [Flutter 架构指南](https://docs.flutter.dev/app-architecture/guide) | UI 层和数据层的职责划分 | 仅在应用项目需要时标注目录职责 |

本技能提供的是可裁剪的目录、索引和来源建议；外部资料与模板都不证明项目已经通过真实运行或用户验收。
