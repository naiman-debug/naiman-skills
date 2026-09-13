# 步步高

讨论一个方案时，你可能已经回答了几个问题，却不知道还有哪些关键事项没想清楚。项目里即使有术语文档，也不一定适合这次讨论。步步高是基于 **Matt Pocock 的原版 grill-with-docs 修改的版本**，保留其访谈、术语澄清和重要决策记录方式，只补充下面两项能力。

- **Road 讨论路线**：简短说明已明确内容、关键缺口、下一步和可后续处理的细节；随答案调整，不变成开发任务表。
- **Context 适用性检查**：先判断术语文档属于哪个领域、是否有效、有无冲突，再说明沿用、局部修订、仅参考或待确认，并展示实际文件位置。

## 怎样使用

复制完整 bubugao 目录到所用客户端的技能目录，在目标项目显式调用：

```text
使用 $bubugao 帮我讨论这个方案。
先说明讨论路线，并检查项目已有的 Context 是否适用。
```

需要只读时加上“这次只讨论，不写文件”。允许记录时，Road 优先复用适合本次讨论的接续位置，没有则按项目规则使用 ROAD.md 或具名专题位置。术语按原版进入 CONTEXT.md，重要取舍符合原版条件时进入 ADR。文件按需生成，不预建一整套目录。

Road 只保存必要进度，普通需求不保证全部落盘；本技能不承诺形成完整 PRD，也不自动进入实现。它没有此前讨论的三份扩展模板。

## 原版与依赖

这是我们的两项补充版本，英文技能名为 bubugao，中文显示名为“步步高”。上游原版仍叫 grill-with-docs，我们为其使用的中文显示名是“边聊边记”；两者可并存，请用英文调用名区分。包内附带原版 grilling、domain-modeling 及其 CONTEXT/ADR 模板，不要求另外安装依赖，不读取作者的个人技能源目录。

上游来源：[mattpocock/skills 固定版本](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015)，原始入口及依赖文件保存在 references/upstream 中，内容未改。三个原版入口在包内命名为 UPSTREAM-SKILL.md，避免被宿主当作额外技能自动发现；原始名称均为 SKILL.md。新增规则仅在本包 SKILL.md 中。原作者版权与许可见 [LICENSE.upstream](LICENSE.upstream)，本仓库扩展采用 MIT。

已纳入本仓库准备发布的技能列表，当前仍为本地候选，尚未在 GitHub 正式发布。静态检查与文件比对不保证真实多轮访谈不会漂移。

## English

Bubugao extends the original grill-with-docs with only a compact discussion Road and a Context suitability check. Original interviewing, glossary and ADR guidance is bundled unchanged with attribution. No separate skill dependencies are needed. Road is not a full requirements specification; implementation remains a separate task. Invoke explicitly with `$bubugao`.
