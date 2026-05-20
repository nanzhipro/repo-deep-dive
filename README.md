# repo-deep-dive

把一个开源仓库从“看懂”推进到“内化其思维方式”。

`repo-deep-dive` 是一个用纯 Markdown 编写的通用 Skill。它帮助 LLM 或 coding agent 把一个仓库沉淀成：

- 分层研究笔记
- 可复用的设计模式与取舍
- 作者思维方式的证据化总结
- 可迁移到你自己场景的创造方案

它既可以作为 Skill 安装，也可以直接把 [SKILL.md](SKILL.md) 交给任意支持指令跟随的模型执行。

快速导航：[安装](#安装) · [快速开始](#快速开始) · [输出结果](#输出结果) · [工作流](#工作流) · [文档](#文档)

## 这是什么

大多数仓库拆解停在三层：

- 它是做什么的
- 它怎么用
- 它的代码怎么组织

这个 Skill 继续往下走，直到更难学、但更有价值的两层：

1. 知识
2. 技能
3. 模式
4. 思维方式
5. 创造

目标不是“读懂一个仓库”，而是把作者的思考方式带回你的工作里。

## 适用场景

适合在这些情况下使用：

- 想真正吃透一个仓库，而不只是做摘要
- 做技术选型，想知道作者为什么这样设计
- 想把别人的方法论迁移到自己的产品或团队
- 想产出可评审、可分享、可继续迭代的研究文档

不适合在这些情况下使用：

- 只是修 bug 或做 code review
- 只是查 API、看用法、要一个快速摘要
- 不准备做 Phase 5 和 Phase 6

## 你会得到什么

- 一套 6 阶段的仓库研究工作流
- 一套提炼设计取舍、作者哲学和 mindset 的方法
- 并行研究与结构化写作模板
- 一个生成 `.learning-notes/` 的脚手架脚本
- 一组适合提交、评审、公开分享的输出文档

## 兼容性

这个仓库按“能力”设计，不绑定具体产品：

- 如果环境支持 `skills` CLI，就直接安装为 Skill
- 如果环境支持任务清单、子代理或并行研究，就在 Phase 2 和 Phase 3 使用它们
- 如果没有这些能力，也可以在单个对话里按相同步骤串行执行
- 如果环境无法安装 Skill，直接让模型阅读 [SKILL.md](SKILL.md) 即可

## 安装

推荐使用 `skills` CLI：

```bash
npx skills add nanzhipro/repo-deep-dive
```

`skills` 支持 `<owner>/<repo>` 这种 GitHub 短格式，所以不需要再手动复制到某个工具专属目录。这个仓库本质上就是 Markdown 文档加一个 Python 辅助脚本，没有构建步骤。

如果你的 AI 工具不支持 `skills`，可以直接这样用：

```text
阅读 SKILL.md，并用其中的方法深度内化 https://github.com/OWNER/REPO。
重点关注作者的思维方式、取舍，以及哪些方法值得迁移到我的场景。
```

## 快速开始

### 已安装 Skill 的环境

```text
使用 repo-deep-dive 深度内化 https://github.com/owner/project。
重点分析作者的思维方式、决策框架，以及哪些方法值得迁移到我的产品里。
```

### 通用 LLM 或 Agent

```text
阅读 SKILL.md，并按其中的流程研究 https://github.com/owner/project。

请交付：
1. 从知识到 mindset 的分层拆解。
2. 带 path:line 引用的关键取舍分析。
3. 一份把这些思维方式迁移到其他领域的创造方案。
```

### 可选：先生成研究骨架

```bash
python3 scripts/scaffold-notes.py /path/to/target-repo --modules "core,plugins,sdk"
```

## 输出结果

运行后会得到一个 `.learning-notes/` 目录，结构大致如下：

```text
.learning-notes/
├── README.md
├── 01-overview.md
├── 02-architecture.md
├── 03-N-<core-module>.md
├── M-engineering.md
├── M+1-design-patterns.md
├── M+2-mindset-and-philosophy.md
├── M+3-apply-and-creation.md
└── concept-table.md
```

关键产物：

- `M+2-mindset-and-philosophy.md`：作者的决策框架与世界观
- `M+3-apply-and-creation.md`：把这套思维方式迁移到你自己工作中的方案
- `concept-table.md`：跨文档共享概念与导航入口

## 工作流

| 阶段 | 目标 | 主要层级 |
| --- | --- | --- |
| 1 | 快速全局扫描 | 知识 + 技能 |
| 2 | 拆解研究问题 | 任务设计 |
| 3 | 按模块或主题深入调研 | 模式 |
| 4 | 整理成结构化文档 | 模式 |
| 5 | 提炼思维方式与哲学 | 思维方式 |
| 6 | 迁移到自己的场景 | 创造 |

完整方法、约束和质量标准都在 [SKILL.md](SKILL.md) 与 [references](references) 目录中。

## 仓库结构

| 路径 | 说明 |
| --- | --- |
| [SKILL.md](SKILL.md) | 面向 LLM 或 Agent 的主契约文件 |
| [references/mindset-extraction.md](references/mindset-extraction.md) | 7 种思维方式提炼方法 |
| [references/internalization-and-creation.md](references/internalization-and-creation.md) | 从理解走向创造的 4 条路径 |
| [references/explore-prompts.md](references/explore-prompts.md) | 并行或串行研究的提示词模板 |
| [references/document-templates.md](references/document-templates.md) | 最终研究文档的写作模板 |
| [scripts/scaffold-notes.py](scripts/scaffold-notes.py) | `.learning-notes/` 目录生成脚本 |

## 文档

README 只保留高层入口，具体方法拆到独立文档里：

- [SKILL.md](SKILL.md)：完整工作流、约束和质量标准
- [references/mindset-extraction.md](references/mindset-extraction.md)：思维方式提炼方法与示例
- [references/internalization-and-creation.md](references/internalization-and-creation.md)：创造阶段的落地方法
- [references/explore-prompts.md](references/explore-prompts.md)：Phase 3 的研究提示词模板
- [references/document-templates.md](references/document-templates.md)：Phase 4 的文档结构模板

## 贡献

欢迎这些类型的改进：

- 用更多仓库验证这套方法，并分享产出的研究笔记
- 改进 prompt 或模板，但保持能力导向，不绑具体产品
- 补充有证据支撑的方法示例
- 保持小而清晰的 diff，便于评审
