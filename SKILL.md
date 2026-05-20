---
name: repo-deep-dive
description: |
  Internalize an open-source repo by extracting all four layers — Knowledge / Skill / Patterns / Mindset —
  not just "what it does" but the author's mental models, value trade-offs, and decision frameworks.
  Produces publishable public research docs, a transferable methodology, and a seed project where you
  reuse the mindset on a different domain.

  深度内化一个开源仓库:从表层(知识/技能)穿透到冰山之下(思维模式/心智 mindset),
  不止学"它是什么",更学作者的决策框架和世界观。产出可公开发布的研究文档 + 可迁移方法论
  + 把 mindset 应用到不同业务场景的种子项目。

  **Perfect for:**
  - 想"内化"某个开源仓库的 mindset(不止"会用",而是"会创造类似的东西")
  - 评估技术选型时,理解作者的设计哲学和取舍框架
  - 学习行业标杆背后的思维模型与元认知(meta-cognition)
  - 想把 X 的方法论搬到自家不同业务场景,而非照搬代码
  - 团队培训:让团队学到的是"思考方式",不只"功能列表"

  **Not ideal for:**
  - 单纯 code review / bug 修复(用专门 review 工具)
  - 仅需阅读 README 就够的简单任务
  - 已熟悉的技术栈的常规 lookup
  - 想要"快餐式总结"而非真正内化
---

# Repo Deep Dive — 把开源仓库的 mindset 内化到你的认知里

## Why This Skill Exists

读完 README 你"知道了"这个仓库。
跟着 tutorial 跑通,你"会用"了它。
读源码看 architecture,你"懂"它的结构了。

—— 但**你还是创造不出来类似的东西**。

因为你只学到了表层。**真正决定一个伟大产品长什么样的,是作者的 mindset**——他怎么思考问题、怎么做取舍、怎么定义"好"、怎么决定不做什么。

> 你不仅仅是在学知识,更是在学知识背后的东西——它的决策方式、认知机制、思维模型。
>
> 学到了它的 **支持系统(冰山之下)**,你才能在此基础上创建独属于你自己的知识域和技能。

这个 Skill 把"读懂一个仓库"提升到"内化它的 mindset,然后用这个 mindset 在自己的领域创造"。

## The Iceberg Model — 五层学习模型

```
                  ┌──────────────────────────────────────┐
                  │  Layer 1:  Knowledge Set             │
冰山之上            │  ─ 是什么 / 有什么 / 做什么            │
(易学,价值低)     │  ─ 来源:README, docs                  │
                  │  ─ 24 小时后忘 80%                    │
                  └──────────────────────────────────────┘
                  ┌──────────────────────────────────────┐
                  │  Layer 2:  Skill Set                 │
                  │  ─ 怎么用 / 怎么搭 / 怎么部署          │
                  │  ─ 来源:examples, tutorials           │
                  │  ─ 跟着教程跑通 = 拥有                │
                  └──────────────────────────────────────┘
═══════════════════════════════════════════════════════════ 水线
                  ┌──────────────────────────────────────┐
冰山之下            │  Layer 3:  Mental Models & Patterns │
(难学,价值高)     │  ─ 为什么这样设计 / 有什么抽象        │
                  │    / 有什么不变量                    │
                  │  ─ 来源:代码组织、命名、API 边界、    │
                  │    一致性                            │
                  │  ─ 通过"对比 + 反例 + 取舍分析"提取    │
                  └──────────────────────────────────────┘
                  ┌──────────────────────────────────────┐
                  │  Layer 4:  Mindset & Meta-cognition  │  ← 这个 Skill 的真正
                  │  ─ 作者怎么思考 / 价值取舍 /            │     核心目标
                  │    决策框架 / 世界观 / 元认知          │
                  │  ─ 来源:git log, commit msg,          │
                  │    没做的事, 注释里的"why",          │
                  │    错误信息的语气                    │
                  │  ─ 通过 7 种 mindset extraction 法    │
                  │    反向推断(见 references/)          │
                  └──────────────────────────────────────┘
                              ↓
                  ┌──────────────────────────────────────┐
                  │  Layer 5:  Internalization & Creation│  ← 最终产出:不是
                  │  ─ 用学到的 mindset 在我的领域创造    │     文档,而是创造
                  │    什么?(不是抄,是用同样的思考方     │     能力
                  │    式做我自己的事)                   │
                  │  ─ 来源:你自己,用作者的 mindset 推    │
                  │    导,但场景换成你的                │
                  └──────────────────────────────────────┘
```

**关键认知**:

| 层级      | 核心判断 | 含义                                         |
| --------- | -------- | -------------------------------------------- |
| Layer 1-2 | 不值钱   | AI 往往能在 1 小时内补齐表层知识和基础操作。 |
| Layer 3   | 有价值   | 传统的“看代码”通常最多能稳定学到这一层。     |
| Layer 4   | 最稀缺   | 几乎没人会系统性提取作者的 mindset。         |
| Layer 5   | 真正产出 | 如果不能迁移到创造，学习就没有真正完成。     |

→ **AI 让 Layer 1-3 提速 10 倍,意味着你现在必须把功夫花在 Layer 4-5。**

## Critical Constraints ⚠️

| 约束                           | 必须做到                                                                                                                      | 失败信号                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------- |
| 必须穿透到 Layer 4             | 能回答“作者在和谁辩论 / 作者拒绝接受什么 / 作者眼中的世界长什么样”。                                                          | 学完只能复述“它用了 X、Y、Z 设计模式”，说明还停在 Layer 3。          |
| 必须落到 Layer 5（创造）       | 产出“我的创造 roadmap”，并至少把学到的 mindset 用一次，哪怕只是写出“如果我用这个 mindset，我会做 X”。                         | 文档停留在整理阶段，没有任何迁移或创造动作。                         |
| 运行最后必须做 Final Synthesis | 回写 README 的全局 TL;DR，并生成 `concept-table.md` 汇总高复用概念。                                                          | 只有分散文档，没有最后一份总表，读者无法快速建立整体认知。           |
| 共享概念必须可回链             | 其他 `.md` 文档第一次出现共享概念时，补 `[[concept-table#Heading                                                              | Alias]]`；若要兼容 GitHub，再并排保留普通 Markdown link。            | 有概念表但无法从上下文跳到对应条目，概念导航失效。 |
| 每个洞察都要分层标注           | 写文档时显式标注是 Knowledge / Skill / Pattern / Mindset 哪一层的发现。                                                       | 不分层，等于没真正按这个 Skill 的方法工作。                          |
| 必须有反例 / 取舍              | 不能只写“它做了 X，这很好”，必须解释“为什么不做 Y / 代价是什么 / 什么场景不适用”。                                            | 结论只有赞美，没有边界、代价和反例。                                 |
| path:line 引用是契约           | 每篇文档至少有 5 处可验证引用。                                                                                               | 结论无法回到原始证据，可信度不足。                                   |
| Markdown 输出必须 GFM 合规     | 所有最终 `.md` 文件都遵循 GitHub Markdown 最佳实践：单一 H1、代码块标语言、表格/列表/引用前后留空行、优先原生 Markdown 结构。 | 出现未标语言的代码块、滥用 ASCII 表格、标题层级混乱或依赖原生 HTML。 |
| Phase 5 不可跳过               | 把 Layer 4 的 mindset 提取放在专门 phase 中完成。                                                                             | 只做 Phase 1-4 就收工，核心产出缺失。                                |
| 学完必须内化                   | 把 Phase 6 当作目标，而不是可选项。Phase 1-5 都是在为它做准备。                                                               | 最终只有文档，没有把 mindset 真正带到自己的问题域里。                |

## The 6-Phase Workflow

每个 Phase 后括号里标注**主要提取哪些 layer**。

### Phase 1: Quick Global Scan(Layer 1+2,20-30 分钟)

**目标**:回答 5W(what/why/who/when/how)。

行动:

1. 读 `README.md` 整篇
2. 读所有顶层 manifest
3. `ls` / `find -maxdepth 2 -type d` 看目录
4. 读 1-2 个最有代表性的样本文件
5. `git log --oneline -30` 看最近演进

**输出契约**:**≤ 200 字的全局描述**回答:这个仓库是什么 / 解决什么 / 核心抽象 / 分几层。

回答不出 → 不进 Phase 2。

### Phase 2: Decompose Investigation(10-20 分钟)

**目标**:拆 5-10 个独立子任务。

用 `TaskCreate` 建任务清单。**至少一个任务必须是"Mindset 提取"**。

典型任务集:

```
1. 顶层架构与目录布局           [Layer 3]
2. 核心模块 A/B/C 深度解析       [Layer 3]
3. 工程基础设施                  [Layer 2+3]
4. 演进史与设计变迁              [Layer 4 — 关键]
5. "为什么 NOT" 调查              [Layer 4 — 关键]
6. 作者价值观痕迹追踪             [Layer 4 — 关键]
7. 横向对比与定位                [Layer 4]
8. 可复用 pattern 总集            [Layer 3]
9. 应用方法论 + 创造路径          [Layer 5]
```

### Phase 3: Parallel Deep Dive(Layer 3,1-3 小时)

**目标**:把每个任务从"未知"推到"有详实素材"。

策略:Explore agents 并行 + 你自己手动精读核心样本。

详细 prompt 模板:[references/explore-prompts.md](./references/explore-prompts.md)。

**这个 Phase 重点是 Layer 3**(模式/架构层)。Layer 4 的素材会在 Phase 5 用专门方法提取。

### Phase 4: Structured Write-Up(Layer 3 文档化,2-4 小时)

**目标**:8-12 篇遵循 GitHub Markdown 最佳实践的深度 markdown,每个洞察显式标 layer。

#### Markdown 输出契约(GitHub Markdown Best Practices)

所有最终产出的 `.md` 文件都必须遵守下面这组格式约束:

1. 只允许一个 `#` 一级标题;其余章节按 `##`、`###` 递进,不要跳级。
2. 标题、段落、列表、表格、引用、代码块之间留空行;列表保持平铺,只有顺序重要时才用编号列表。
3. 所有 fenced code block 必须标语言:命令用 `bash`,JSON 用 `json`,YAML 用 `yaml`,目录树/ASCII 图用 `text`,图示优先 `mermaid`。
4. 对比与枚举优先用 Markdown 表格、任务列表、编号列表;只有需要强制等宽对齐时才用 `text` 代码块。
5. 引用源码或原文时优先用 blockquote,并在相邻位置给出 `path:line`;不要大段无出处摘抄。
6. 链接优先使用相对路径 Markdown link;不要只写“见某文件某处”。
7. 除 GitHub Markdown 无法表达的场景外,不要使用原生 HTML。
8. 写完后做一次格式自检:表格可读、代码块有 language、链接可点、GitHub 预览不变形。

#### Learning in Public 输出契约

所有最终产物都默认按“可公开发布、可被陌生读者直接读懂”的标准来写,而不是按“写给未来的自己”的备忘录来写:

1. 每篇文档开头就回答 3 件事:这篇写给谁、解决什么问题、最重要的结论是什么。
2. 不假设读者知道你的上下文;首次出现的仓库术语、缩写、内部抽象都要给一句解释。
3. 章节标题要能脱离上下文独立成立,避免“补充一点”“再说一个细节”这类私聊式标题。
4. 结尾必须给出可复用 takeaway:方法论、检查单、下一步动作或公开可讨论的问题。
5. 默认把 `.learning-notes/` 视为可提交、可分享、可继续打磨成 README / docs / blog / talk 的公开产物目录,并纳入版本控制持续迭代。

标准文档集:

```
.learning-notes/
├── README.md                          [Layer 1+2 索引]
├── 01-overview.md                     [Layer 1+2]
├── 02-architecture.md                 [Layer 3]
├── 03-N-<core-module>.md              [Layer 3]
├── M-engineering.md                   [Layer 2+3]
├── M+1-design-patterns.md             [Layer 3 总集]
├── M+2-mindset-and-philosophy.md      [Layer 4 ★ 核心]
├── M+3-apply-and-creation.md          [Layer 5 ★ 产出]
└── concept-table.md                   [Final synthesis ★ 概念表 / wikilink 入口]
```

每个 finding **显式标 layer 标签**:`[L3]`、`[L4 mindset]`、`[L5 creation]` 等。

### Phase 5: Mindset Extraction(Layer 4,60-120 分钟)

**这个 Phase 是 Skill 的核心。** Phases 1-4 是认知准备,Phase 5 是认知产出。

#### 5a. 跑 7 种 Mindset Extraction 方法

逐一对照(详见 [references/mindset-extraction.md](./references/mindset-extraction.md)):

1. **"为什么 NOT"法** — 列作者明显**没做**的事,问为什么
2. **演进史归因** — 哪个先做哪个后做,揭示优先级 mindset
3. **取舍频谱定位** — 在 10 个经典取舍轴上定位作者
4. **反事实推理** — 假设作者是 X 类型的人,会怎么写
5. **价值观痕迹** — 注释 / 命名 / 错误信息透露的价值取向
6. **受众假设** — 作者把读者想成什么样的人
7. **第一性原理痕迹** — 哪些"业界默认"作者拒绝接受

#### 5b. 写 Mindset 文档(`M+2-mindset-and-philosophy.md`)

至少包含:

- 作者的 5-7 条 mindset 信条(用作者的口吻陈述)
- 取舍频谱表(10 个轴,每个标作者位置)
- 至少 3 个"为什么 NOT"案例分析
- 作者眼中"好的设计"是什么样的(用证据)
- 作者的元认知:他怎么定义"完成"、"质量"、"够好"

#### 5c. 反思常见盲点

- [ ] 边缘 / 非核心模块覆盖了吗?
- [ ] 演进史的 mindset 含义提炼了吗?
- [ ] Runtime concerns 讨论了吗?
- [ ] 横向对比做了吗?
- [ ] 作者的"价值观痕迹"找到了吗?
- [ ] 作者的"受众假设"识别了吗?
- [ ] 至少 1 个完整 worked example 解剖了吗?

发现遗漏 → 补 1-3 篇文档,更新 README 索引。

### Phase 6: Internalization → Personal Creation(Layer 5,2-4 小时)

**这才是真正的产出**。前 5 phase 是准备。

详细方法:[references/internalization-and-creation.md](./references/internalization-and-creation.md)。

#### 4 种创造路径

1. **用法转移**:同样的 mindset,应用到我的不同场景会变成什么?
2. **表层替换 / 内核保留**:技术栈换,mindset 留
3. **mindset 混合**:当前 mindset + 另一个仓库的 mindset 组合
4. **mindset 挑战**:故意做和作者相反的选择,看产生什么

#### 产出

**`M+3-apply-and-creation.md`** 必须包含:

- 我学到的 mindset 列表(从 Phase 5b 引用)
- 至少 3 条"用法转移"的具体设想
- 30/60/90 路线图:第一个用学到 mindset 做的东西
- **一份种子项目**(可选但强烈推荐):用 mindset 做一个**完全不同领域**的小项目,证明 transferability

### Final Synthesis: Summary + Concept Table(必做,20-40 分钟)

Skill 运行结束前,必须再做一次 run closure。不要以 `M+3-apply-and-creation.md` 作为最后一步。

#### 必产物

1. 回写 `.learning-notes/README.md` 的 `全局 TL;DR`,把散落洞察压成最终版 10-15 条。
2. 生成 `concept-table.md`,作为共享概念的唯一汇总表。
3. 回扫其他 `.md` 文档,把第一次出现且会跨文档复用的概念补上回链。

#### `concept-table.md` 结构

1. `## Final Synthesis`:200-400 字,回答“这个仓库最值得带走的 3-5 个抽象 / 3-5 条 mindset / 3-5 个 transfer 机会是什么”。
2. `## Concept Index`:表格列至少包含 `概念 | Layer | 一句话定义 | 首读文档 | 相关概念`。
3. `## <Concept Heading>`:8-20 个概念卡,每个概念单独一个二级标题,至少包含:

- 定义
- 为什么重要
- 主要证据(`path:line`)
- 出现在哪些文档
- 相邻 / 易混淆概念
- 可迁移用法

#### Wikilink 约定

- `concept-table.md` 用固定文件名,不编号。这样其他文档的 wikilink 永远稳定。
- 概念标题尽量用稳定、可 slug 的短英文短语;中文解释写在正文第一段。
- 其他文档第一次出现共享概念时,补一个 wikilink:`[[concept-table#Trust Boundary Isolation|Trust Boundary Isolation]]`
- 若这批文档需要同时在 GitHub 上可读,再并排保留普通 Markdown link:`[Trust Boundary Isolation](./concept-table.md#trust-boundary-isolation)`
- 只把会在 2 篇以上文档复用的概念收入概念表,避免术语垃圾桶。

## The Art of Questioning(学习的关键技能)

**你能学到多深,取决于你问什么问题。**

### 不要问(表层提问)

- ❌ "这个仓库是做什么的?" — README 已经说了
- ❌ "怎么安装?" — README 已经说了
- ❌ "有哪些功能?" — 列表化产物,记不住

### 要问(穿透提问)

按 Layer 升级你的提问深度:

| Layer | 提问范式                                                         | 例                               |
| ----- | ---------------------------------------------------------------- | -------------------------------- |
| L1    | What is X?                                                       | 这个仓库做什么?                  |
| L2    | How to use X?                                                    | 怎么部署?                        |
| L3    | Why X instead of Y?                                              | 为什么用 plugin 不用 SDK?        |
| L4    | What was the author _not_ trying to do?                          | 作者刻意拒绝了什么?              |
| L4    | Who is the author arguing with?                                  | 作者在和谁的设计辩论?            |
| L4    | If the author redid this, what would they keep / cut?            | 重做一次,哪些保留哪些砍?         |
| L4    | What does the author assume the reader knows?                    | 作者假设你已经懂什么?            |
| L4    | What would make the author say "this is bad"?                    | 作者眼中"差的设计"是什么?        |
| L5    | Holding the author's mindset, what would I build in _my_ domain? | 用作者的脑子,在我领域我会做什么? |

→ **每次研究开始前,先把这些"穿透问题"列出来**,带着它们去读。

## Mindset Extraction — 7 个方法(核心技术)

具体方法看 [references/mindset-extraction.md](./references/mindset-extraction.md)。这里给一句话概览:

| #   | 方法                | 一句话                                   |
| --- | ------------------- | ---------------------------------------- |
| 1   | **"为什么 NOT" 法** | 列作者没做的事,每个"NOT"背后都有 mindset |
| 2   | **演进史归因**      | 时间顺序 = 优先级 = mindset 顺序         |
| 3   | **取舍频谱定位**    | 在 10 个经典轴上画作者位置               |
| 4   | **反事实推理**      | "如果作者是 X 风格,会怎么写"             |
| 5   | **价值观痕迹**      | 注释 / 命名 / 错误信息透露价值取向       |
| 6   | **受众假设**        | 作者把读者想成什么样的人                 |
| 7   | **第一性原理痕迹**  | 哪些"业界默认"作者拒绝接受               |

## From Mindset to Personal Creation(4 种路径)

详细见 [references/internalization-and-creation.md](./references/internalization-and-creation.md)。

| 路径                       | 一句话                      | 难度 |
| -------------------------- | --------------------------- | ---- |
| **A. 用法转移**            | 同 mindset,换场景           | ★    |
| **B. 表层替换 / 内核保留** | 换技术栈 + 行业,留思维方式  | ★★   |
| **C. mindset 混合**        | A 的 mindset + B 的 mindset | ★★★  |
| **D. mindset 挑战**        | 故意做和作者相反的选择      | ★★★★ |

**起步建议**:从 A 开始,半年后试 B,一年后试 C,有专门项目时才试 D。

## Standard Patterns to Look For(Layer 3 速查表)

进入任何代码仓库时,主动寻找(高频出现,几乎一定可抄):

| Pattern                   | 通常形态                                | 看哪里                               |
| ------------------------- | --------------------------------------- | ------------------------------------ |
| One Source, Many Wrappers | 同一份核心逻辑,不同部署形态             | 看是否多 entry / 配置引用源          |
| Workflow-as-Contract      | 关键模块用固定章节描述                  | 主 prompt / 主 config 是否短而结构化 |
| Trust Boundary Isolation  | 处理 untrusted 输入的模块能力被剪到最小 | 是否有 reader/parser 类模块          |
| Sole Write-Holder         | "持有写权"集中到一个模块                | 哪个模块有 Write / DB insert         |
| Schema as Wall            | maxLength + regex 同时做语法和注入防护  | schema 定义是否含 pattern            |
| Source-of-Truth + Sync    | 共享组件单源 + 同步脚本                 | 是否有 `sync-` 或 `vendor-` 脚本     |
| Self-Install Lint Hook    | Lint 脚本顺手装 git hook                | lint 脚本有没有 `core.hooksPath`     |
| Idempotent Version Bump   | pre-commit 自动 bump 但 idempotent      | 版本号策略                           |
| Dry-Run Body Lint         | 部署脚本有 `--dry-run` + CI 校验        | deploy 脚本是否输出"会发送的 body"   |
| Reference, Not Production | 简单示范代码,头部明说不要直接生产       | examples / reference 脚本注释        |

## Examples — 各 Layer 的 ✅ vs ❌

### ❌ Layer 1 停留(没穿透)

> gl-reconciler 用 3 个 sub-agent 来做对账,这是一种好的多 agent 设计。

### ✅ Layer 3(模式)

> **gl-reconciler 的三层 leaf 拆分**:reader(`Read+Grep` only,无 MCP)、critic(用 trusted MCP 独立 re-verify)、resolver(**唯一** Write-holder)。
> 关键:Write 集中到一个 leaf,信息流 untrusted → verified → output。
> 反例:`pitch-agent` 三层是为了**并行**(researcher / modeler / writer),架构相同但**设计动机不同**。

### ✅ Layer 4(mindset 提取)

> **Anthropic 的 mindset 1:"安全靠架构,不靠模型聪明"**
>
> - 证据:每个 cookbook 都把 Write 收到一个 leaf;reader 永远没 MCP;输出 schema 加 regex 字符类。
> - 反证:Anthropic 完全可以训一个"识别注入"的分类器代替这些机制,但他们选择**架构级隔离**。
> - 暗含的世界观:"模型再强也会出错,工程纪律比 AI 能力更可靠"。
> - 这个 mindset 推到极致 = "把 AI 当成可错的工人,而不是可信的合伙人"。

### ✅ Layer 5(创造)

> **用法转移**:Anthropic 这个 mindset(把 AI 当可错工人)应用到我们 tiwenlab 的内容审核场景:
>
> - 不要训"识别违规"模型(那是 mindset:AI 是合伙人)
> - 改成:reader leaf 抽取结构化内容 → critic leaf 走规则库 → escalator 输出给人
> - 哪怕模型出现"觉得没违规但实际违规",**reader 输出有 schema**,违规 payload 字符类截断
> - 半年后再升级到 AI 主导,但**保留这套架构**作为 fallback

## Quality Rubric(分 layer 自检)

### Layer 1+2(覆盖)

- [ ] 一句话能讲清仓库定位
- [ ] 5W 都答了(what / why / who / when / how)
- [ ] 关键操作流跑通至少 1 次

### Layer 3(模式)

- [ ] 8-12 个 pattern,每个含反例 + 复用难度
- [ ] 至少 1 张架构图 / 流程图
- [ ] 关键不变量 ≥ 10 条
- [ ] 每个洞察有 `path:line` 引用

### Layer 4(mindset)★ 核心

- [ ] 7 种 mindset 提取方法都跑过
- [ ] 写下 5-7 条作者 mindset 信条(用作者口吻陈述)
- [ ] 取舍频谱图(10 个轴上定位作者)
- [ ] ≥ 3 个 "为什么 NOT" 案例
- [ ] 作者眼中"好设计 vs 坏设计"的描述
- [ ] 作者的元认知:怎么定义"完成 / 质量 / 够好"

### Layer 5(创造)★ 产出

- [ ] 至少 1 条"用法转移"具体设想
- [ ] 30/60/90 路线图(用学到的 mindset 做自己的事)
- [ ] (可选)种子项目 — 在不同领域用同 mindset

### 总体

- [ ] 每个发现显式标 layer 标签 `[L1]/[L2]/[L3]/[L4]/[L5]`
- [ ] Phase 5 (mindset extraction) 不可跳过 — 是否有 `M+2-mindset-and-philosophy.md`
- [ ] Phase 6 (创造) 至少有 `M+3-apply-and-creation.md`
- [ ] 运行收尾后有 `concept-table.md`:含 8-20 个概念卡 + 跨文档 wikilinks

## Anti-Patterns(失败模式)

❌ **停在 Layer 3** — 学完只能描述设计模式,没有 mindset 文档
❌ **mindset 章节是空话** — "他追求简洁"这种没证据没反例的废话
❌ **没有"为什么 NOT"** — 只看作者做了什么,不问没做什么
❌ **没有取舍频谱** — 不在轴上定位作者,只罗列优点
❌ **没有 Phase 6** — 文档写完就停,从未"用"过 mindset
❌ **照搬代码** — 复制仓库代码到自己项目,但 mindset 没迁移
❌ **罗列功能** — 列表化产物,看似全面实则浅
❌ **过度长** — 5000 行单文件,信息密度低,没人读得完
❌ **没分层标注** — 所有发现混在一起,读者不知道什么是表层什么是深层
❌ **不留 path:line** — 引用不可 verify,文档不可信

## Source Hierarchy(信息可靠性)

引用源代码内容时,可靠性从高到低:

1. **实际代码 + 配置文件** — 最高
2. **本仓库 README / docs** — 高
3. **PR / issue / commit message** — 中(含设计意图 ★ Layer 4 关键源)
4. **官方博客 / 演讲** — 中(可能滞后 / 美化)
5. **作者 Twitter / podcast / 访谈** — 中(★ Layer 4 关键源,但要交叉验证)
6. **第三方文章** — 低(可能误读)

**Layer 4 的特殊源**:

- 不仅看做了什么,**看没做什么 / 拒绝过什么**(issue/PR 里的 "wontfix" 标签)
- 看 issue 讨论里作者的 reply 语气(Layer 4 价值观痕迹)
- 看 changelog 的措辞("breaking change" 还是 "minor adjustment"——揭示作者对稳定性的看法)

## When to Use This Skill

✅ 触发:

- "深度学习 / 拆解 / 调研 / 内化"某个开源仓库
- "想把 X 的方法论搬到自家业务"
- "评估 / 选型 / 对比"某个仓库
- "我想做类似 X 的东西,要先吃透它"
- "想学到 X 作者的思维方式"
- "学习 X 的 mindset / philosophy / design thinking"

❌ 不应触发:

- 单纯 bug 修复 / code review
- "解释这个函数做什么"(直接 Read)
- "我想用 X 库做 Y"(README + 示例就够)
- "X 库支持 Y 功能吗"(查 docs)

## Variations(根据仓库类型调整)

| 仓库类型                | Layer 重点 | 调整                                               |
| ----------------------- | ---------- | -------------------------------------------------- |
| 小型库(<50 文件)        | L2+L3      | Phase 1+4+6,精简到 5-7 篇文档                      |
| 超大仓库(>1000 文件)    | L3+L4      | Phase 3 启 5-6 个 Explore agents,文档可能 15-20 篇 |
| Multi-agent / Framework | L3+L4      | 重点提取架构 mindset + trust boundary              |
| 学习材料 / cookbook     | L4         | 重点提"作者怎么教学",而非系统设计                  |
| 商业产品开源            | L4+L5      | 重点提商业 mindset,创造路径围绕"GTM/客户分层"      |
| 个人项目 / 大佬作品     | L4         | mindset 提取是核心,价值观痕迹特别明显              |
| 基础设施 / DevOps       | L2+L3      | mindset 抽象较弱,操作流程是主                      |

## 核心前提

> **"AI 让 Layer 1-3 廉价,人的价值必须移到 Layer 4-5。"**
>
> 这不是关于"工具",而是关于"学习何以为学习"。
>
> 表层知识查 AI,中层模式让 AI 提炼,**深层 mindset 必须人来吸收并改造**。
> Mindset 不是被"记住"的,是被"成为"的。

---

详细 references:

- [references/mindset-extraction.md](./references/mindset-extraction.md) — Phase 5 的 7 种 mindset 提取方法详解
- [references/internalization-and-creation.md](./references/internalization-and-creation.md) — Phase 6 的 4 种创造路径 + 落地模板
- [references/explore-prompts.md](./references/explore-prompts.md) — Phase 3 的 Explore agent prompt 模板
- [references/document-templates.md](./references/document-templates.md) — Phase 4 每篇产出文档的章节骨架

工具:

- [scripts/scaffold-notes.py](./scripts/scaffold-notes.py) — 一键生成 `.learning-notes/` 骨架(含 mindset / creation 章节)
