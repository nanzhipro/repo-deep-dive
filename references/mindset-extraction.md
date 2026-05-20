# Mindset Extraction — 7 种从仓库提取作者 mindset 的方法

> Phase 5 的核心技术。Layer 4 的提取是"反向工程作者的脑子"——不可能像 Layer 3 那样直接读代码就有,必须用 7 个"侧光"方法**反向推断**。
>
> 每个方法都给:**核心问题 · 执行步骤 · Worked Example · 失败模式**。所有 Worked Example 应用于 `anthropics/financial-services` 作为参考标的。

---

## 方法 1:"为什么 NOT" 法

**核心问题**:作者**明显没做**的事是什么?每个 "NOT" 背后都是一个 mindset 决策。

### 执行

1. 列 10-15 件"看似自然 / 业界默认会做"的事,问"作者做了吗?"
2. 找到 ≥ 5 件"作者没做"的
3. 对每个 "没做",反问:为什么没做?
4. 答案就是 mindset

### Worked Example

| 业界默认 / 自然选择 | Anthropic 做了吗 | 没做的话,mindset 是? |
|---|---|---|
| 用 framework(LangGraph / CrewAI / 自己造) | ❌ 纯 markdown + YAML + JSON | "**Files over frameworks**" — 不被 framework 绑架,纯文本任何编辑器都能改 |
| 给 agent 加 GUI 调试器 | ❌ 没有,console URL 而已 | "**Reference, Not Production**" — 简单示范,生产由客户补 |
| 把 orchestrator 设计成全能(可读可写) | ❌ orchestrator 几乎从不持 Write | "**Power asymmetry by design**" — 权力越大,被注入危害越大 |
| 让 sub-agent 可以再调 sub-sub-agent | ❌ depth=1 上限(test-cookbooks.sh 强制 lint) | "**Architecture simplicity over flexibility**" — 用事件总线替代深度委派 |
| 自带 LLM-as-judge 的 eval framework | ❌ 完全没有 | "**Quality from prompt + schema + human, not from eval framework**" |
| 用 ORM / DSL 描述 multi-agent 拓扑 | ❌ 纯 markdown 描述 | "**Description over abstraction**" — 让人读懂比让机器优雅更重要 |
| 给所有 agent 用同一个 system prompt 模板 | ❌ 每个 agent 单独写 | "**Prompt is a contract, not a template**" — 不复用 prompt,因为契约是独有的 |
| 内置 retry / backoff / circuit breaker | ❌ 完全没有 | "**Production concerns are customer's problem**" |
| 给 third-party plugin 提供 SDK | ❌ 只有 markdown 契约 | "**Contribution friction ≈ 0**" — 加门槛会扼杀生态 |

→ **9 个 NOT 揭示了 9 条 mindset**。比读 10 篇博客都直白。

### 失败模式

- ❌ 列的"业界默认"太笼统("没做 metrics")—— 太宽泛,无法定位 mindset
- ❌ 把"没做"归因于"还没来得及" —— 这是逃避,要相信成熟仓库的"没做"是有意识的
- ❌ 只列 1-2 个 —— 样本太少,挑出来的可能是个例

---

## 方法 2:演进史归因

**核心问题**:作者**先做哪个 / 后做哪个**?时间顺序揭示优先级 mindset。

### 执行

1. `git log --reverse --oneline | head -50` 看早期 commit
2. `git log --since="6 months ago" --pretty=format:"%h %ad %s" --date=short` 看近期节奏
3. 标记 5-10 个 milestone commit(架构重组 / 大特性上线 / 重命名)
4. 画时间线:仓库从 X 起点 演进到 Y 状态,顺序是?
5. 问:**为什么 A 先于 B?这个顺序揭示作者认为什么更重要?**

### Worked Example

时间线:
```
2026-03-08 ─── 早期:零散 skill 改进 + PE ai-readiness
2026-03-26 ─── 删 unused yfinance(关注依赖最小化)
2026-03-27 ─── ★ 首次加 claude-in-office plugin(M365 部署工具)
2026-04 ────── 大量 claude-in-office 迭代(bootstrap / RBAC / OTLP)
2026-05-05 ─── ★★★ "Restructure repo and add named agents" 一次性加 60+ 文件
2026-05-15 ─── 加 version-bump hook + CI backstop(事后补)
```

归因分析:
- **claude-in-office 早于 named agents 1.5 个月**
  → mindset:"**先解决企业接入,再做内容**"
  → "**部署摩擦 > 内容深度**" 在 GTM 顺序上
- **named agents 是一次性整体上线(#81 一个 commit 加 60+ 文件)**
  → mindset:"**Multi-agent 架构必须 ahead-of-time 设计**,不能渐进加"
  → "跨 agent 契约不能演进出来"
- **version-bump 是事后补的**(上线 10 天后)
  → mindset:"**工程脚手架 reactive 添加**,真痛了再补"
  → 不 over-engineer

### 失败模式

- ❌ 只看"做了什么",不看"何时做"
- ❌ 把演进解释成"作者越来越聪明" —— 太傲慢,通常是"作者解决一个新问题"
- ❌ 不区分"修 bug 的迭代"和"设计变迁"

---

## 方法 3:取舍频谱定位

**核心问题**:在经典对立的取舍轴上,**作者站在哪一端**?这是 mindset 最直接的画像。

### 10 个经典取舍轴

把作者的位置画在每个轴上(用 ●):

```
简单(simple) ●────────────────── 完整(complete)
灵活(flexible) ──────●─────────── 严格(strict)
显式(explicit) ●────────────────── 隐式(implicit)
当前(short-term) ─────────●─────── 长期(long-term)
内部(in-house) ──────●─────────── 外部(open ecosystem)
文档驱动 ●────────────────── 代码驱动
统一(uniform) ──────────────●─── 多样(pluralistic)
约定(convention) ●────────────────── 配置(configuration)
新颖(novel) ──────────────────●── 保守(boring)
通用(general) ──────────●──────── 专用(specialized)
```

→ 10 个 ● 的位置 = 作者的 mindset 画像。

### Worked Example

```
简单 ●────────────────── 完整        ← 极简(30 行 prompt > 300 行)
灵活 ──────────────●──── 严格        ← 偏严格(schema + allowlist 强约束)
显式 ●────────────────── 隐式        ← 极显式(每个 leaf 权限明文列)
当前 ──────────●──────── 长期        ← 偏长期(check.py 工程投入)
内部 ──────────────●──── 外部        ← 偏外部生态(partner-built marketplace)
文档驱动 ●─────────────── 代码驱动    ← 极文档(无 build 步骤)
统一 ●────────────────── 多样        ← 统一(所有 agent 同一骨架)
约定 ●────────────────── 配置        ← 极约定(目录结构强约定)
新颖 ──────────────────● 保守        ← 极保守(stdlib only, no framework)
通用 ──────────────────● 专用        ← 偏专用(每个 agent 端到端工作流)
```

读这张画像:
- "极简 + 严格 + 显式 + 长期 + 文档驱动 + 统一 + 约定 + 保守 + 专用"
- = **"build a coherent, opinionated, low-magic system that scales by repetition not by abstraction"**
- 这就是 Anthropic FSI 的 mindset 一句话总结

### 失败模式

- ❌ 自创轴 —— 用我列的 10 个,然后**可以加自定义轴**,但先用经典的
- ❌ 把作者画在每个轴中间 —— "中庸"通常是没看清,要逼自己定位
- ❌ 只挑能说明自己观点的轴 —— 必须 10 个轴都画,看完整画像

---

## 方法 4:反事实推理

**核心问题**:**如果作者是 X 类型的人,会怎么写**?对比实际,差就是作者特点。

### 执行

设 5 个"反事实作者":
- **学院派 PhD**(注重 formalism / 证明 / 抽象)
- **大厂工程师**(注重 SLA / scale / 容错)
- **创业团队 hacker**(注重 ship fast / minimal viable)
- **safety-first 工程师**(注重 unhappy path / 边界)
- **DX 优先工程师**(注重 docs / 上手 / 错误信息)

对每个仓库的关键设计,**问 5 个反事实作者会怎么做**,实际作者最像谁?

### Worked Example

`gl-reconciler` 的三层 leaf 设计:

- **学院派 PhD 会怎么做?** → 形式化 type system 约束信任传递,可能写 paper
- **大厂工程师会怎么做?** → 加 retry / circuit breaker / metrics / SLA monitoring
- **创业 hacker 会怎么做?** → 一个 agent 走完,后面再拆
- **safety-first 工程师会怎么做?** → 这就是作者的位置 ✓(reader 完全无权限 + schema 截断)
- **DX 优先工程师会怎么做?** → 给好的 debugging UX,可视化 trace

→ **作者是 "safety-first 工程师" 风格**,但不是纯 safety(否则会更复杂),夹一点 hacker(代码量极小)。

→ Mindset 标签:**"Pragmatic safety-first"** — 安全是第一原则,但用最简单的方式实现。

### 失败模式

- ❌ 只设 2-3 个反事实,样本太少
- ❌ 反事实和实际作者太像 —— 选反事实要 contrast 足够大
- ❌ "作者全占了" —— 不可能 5 种风格都是,逼自己挑最像

---

## 方法 5:价值观痕迹

**核心问题**:作者在**注释 / 命名 / 错误信息 / 文档篇幅分配** 上透露什么价值取向?

### 执行

抓 5 类痕迹:

#### 5a. 代码注释里的"why"(不是"what")
- 看注释里有没有"我们这样做是因为 X"的话
- 这种注释是 mindset 的直接陈述

#### 5b. 命名风格
- playful(`yeet()`, `borking`)vs serious(`processTransactionAsync`)
- 命名长度 vs 命名抽象度
- 缩写 vs 全名(`ctx` vs `context`)

#### 5c. 错误信息语气
- 友好("This won't work because X. Try Y.")
- 冷酷("FATAL: invalid state")
- 教育性("Validation failed at <X>. Common causes: ...")
- 居高临下("you forgot to ...")
- 谦逊(承认 limit:"this likely won't work if ...")

#### 5d. 文档篇幅分配
- 看 `docs/` 各文件大小
- 写得长的是作者最在乎的
- 写得短的是作者觉得"不应该是问题"的

#### 5e. 测试覆盖率分配
- 哪些模块测试详细,哪些测试稀疏
- 揭示作者认为"什么容易出错"

### Worked Example

- **注释里的 "why"**:`orchestrate.py` 头部 13 行 docstring,全是 "为什么" 和 "威胁模型",**code 之前先讲设计意图**
  → mindset:**"设计意图优先于实现"**,代码是意图的载体不是核心

- **命名风格**:`gl-reconciler-reader` / `escalator` / `flagger` —— 全是**动词性 / 职责性**,不是 `XmlParser` / `ServiceImpl`
  → mindset:**"以职责而非类型组织系统"**

- **错误信息语气**:`scripts/version_bump.py:202` "no base ref found; skipping" —— 不阻塞,谦逊
  → mindset:**"工具不挡路"**,优雅降级而不是失败

- **文档篇幅**:`dcf-model/SKILL.md` 1264 行 vs `kyc-doc-parse/SKILL.md` 49 行
  → mindset:**"建模复杂度配文档密度"**,简单事不要硬塞文档

### 失败模式

- ❌ 把 "代码风格" 等同于 "mindset" —— 风格表面,要钻到 why
- ❌ 凭一两条痕迹下结论 —— 至少 5 条不同来源才靠谱
- ❌ 把作者的"个人偏好"误读为"行业标准"

---

## 方法 6:受众假设

**核心问题**:作者把**读者想成什么样的人**?这透露作者的"心智读者画像"。

### 执行

读仓库文档时,问 5 个问题:
1. **作者假设我已经懂什么?**(没解释的 jargon = 假设懂)
2. **作者假设我会从哪入门?**(README 第一段假设你已经在哪)
3. **作者假设我的目标是什么?**(写文档时心里的"用户故事")
4. **作者假设我的失败模式是什么?**(Troubleshooting 章节内容揭示)
5. **作者假设我的耐心 / 时间 / 上下文?**(文档长度 + tutorial 步骤)

### Worked Example

- **README 第一段假设你已经懂**:investment banking / equity research / private equity / wealth management 是什么 —— 不解释术语
- **入口假设**:你已经会用 Claude Code 或 Cowork
- **目标假设**:你是金融服务行业的"工程团队负责人",在评估"能否把 agent 模板落地到自家产品"
- **失败模式假设**:不假设你会被注入攻击 / 不假设你 prompt 写不对(因为这是"参考模板,客户自己处理")
- **耐心假设**:你愿意读完 README 16K 字 + 探索 ~ 60 个 cookbook 文件

→ **心智读者画像**:**"金融 IT 团队的 staff+ 工程师,有经验,有耐心,有自主性"**

→ Mindset 推论:**"我们不给小白做傻瓜化"** —— 这套体系**故意**不照顾刚入门的人,因为目标客户不是他们。

### 失败模式

- ❌ 把"我自己读不懂"等于"作者假设的读者高于我" —— 可能只是你不在目标人群
- ❌ 假设作者"应该照顾所有人" —— 这是天真的,所有产品都有 target 读者

---

## 方法 7:第一性原理痕迹

**核心问题**:作者**拒绝接受**哪些"业界默认"?这是 mindset 最深的部分。

### 执行

列 10 条"AI / 软件 / 该领域的默认假设",检查作者是否接受:

例如对 AI agent 仓库:
- 默认:agent 应该有 GUI / dashboard
- 默认:multi-agent 越深越好
- 默认:state 应该用 graph 描述
- 默认:agent 需要 retry / fallback
- 默认:framework 比 raw 文本好
- 默认:用 LLM-as-judge 评估
- 默认:state 持久化
- 默认:cost 控制要内置
- 默认:agent 间应 RPC 通信
- 默认:用 typed schema 而不是 markdown

哪条作者**拒绝**?

### Worked Example

| 业界默认 | Anthropic 拒绝? | 拒绝的根本原因(mindset) |
|---|---|---|
| Multi-agent 应支持深度委派 | ✓ 拒绝(depth=1) | "复杂度增长不线性,深委派 ROI 负" |
| Framework 比 raw markdown 好 | ✓ 拒绝 | "Framework 锁定 + 学习曲线 > marginal benefit" |
| Agent 之间应同步 RPC | ✓ 拒绝(异步 handoff) | "解耦 > 性能,事件总线胜过 RPC 树" |
| Agent 需要 GUI 调试 | ✓ 拒绝 | "console URL 够,GUI 是 over-engineering" |
| State 应该 graph 化 | ✓ 拒绝(全靠 prompt) | "短期记忆在 session 内,长期记忆是客户的事" |
| 应该有内置 eval framework | ✓ 拒绝 | "质量靠 prompt + schema + 人审,eval framework 是 LLM 时代的过度反应" |
| Plugin 系统应有 SDK | ✓ 拒绝(只有 markdown 契约) | "SDK 增加接入门槛,marketplace 起飞需要 friction ≈ 0" |

→ 7 条"拒绝"的核心 mindset 主轴:**"Resist complexity that doesn't earn its keep"**

这是个**第一性原理**:不被"行业最佳实践"绑架,只接受**为这个具体问题**有用的复杂度。

### 失败模式

- ❌ 把"拒绝"误解为"作者不懂" —— 通常是"作者懂,但故意不做"
- ❌ 没列足业界默认 —— 至少 10 条才能看出模式
- ❌ 给"拒绝"一个浅薄的归因("作者就是简洁派") —— 要深挖到具体决策逻辑

---

## 7 种方法的协同使用

不要孤立用一个方法,要**串联使用**:

```
方法 1(为什么 NOT) — 发现 "作者没做 framework"
        ↓
方法 7(第一性原理) — 这是"拒绝业界默认",根本原因是?
        ↓
方法 3(取舍频谱) — 在"灵活 vs 严格"轴上偏严格
        ↓
方法 5(价值观痕迹) — 注释里"reference, not production",印证
        ↓
方法 4(反事实推理) — 学院派会用 type system,作者用 markdown,确认 "safety-first 但 pragmatic"
        ↓
方法 6(受众假设) — 心智读者是 staff+ 工程师,所以可以省略 SDK 这类"傻瓜辅助"
        ↓
方法 2(演进史) — 这个决定从 day 1 就在,没变过 —— 是 founding mindset

→ 综合 mindset 信条:
  "Resist complexity that doesn't earn its keep,
   serve sophisticated builders directly,
   document the why."
```

→ **7 个角度交叉验证,得到 1-2 句 mindset 信条**,这是 Layer 4 工作的终点。

---

## 写到 `M+2-mindset-and-philosophy.md` 的模板

> 生成最终 `M+2-mindset-and-philosophy.md` 时,先遵守 `SKILL.md` Phase 4 的 GitHub Markdown 输出契约:一个 H1、代码块标语言、表格使用标准 GFM、只有必须等宽对齐时才用 `text` 代码块。

```markdown
# <N> · 作者的 Mindset 与设计哲学

## <N>.1 五条核心 Mindset 信条(用作者口吻陈述)

1. **<信条 1>** — <证据 + path:line>
2. **<信条 2>**
...
5. **<信条 5>**

## <N>.2 取舍频谱画像(10 轴)
<优先用 markdown 表格;若必须画频谱轴,放在 `text` 代码块里并标 ● 位置>

## <N>.3 "为什么 NOT" 案例(≥ 3 个)
### NOT 案例 1:<名字>
- 作者明显没做 X
- 业界默认是 Y
- 为什么没做的归因:Z
- mindset 标签:<...>

## <N>.4 价值观痕迹
- 注释 / 命名 / 错误信息 / 文档篇幅 各举一例

## <N>.5 受众假设
作者的心智读者是:<具体画像>
所以仓库不照顾:<目标外的人群>

## <N>.6 第一性原理:作者拒绝接受什么
表格:7 条业界默认 × 作者是否拒绝 × 根本原因

## <N>.7 综合 mindset 信条
1-2 句话浓缩 5 条信条 + 7 条拒绝 = 作者的 mindset 一句话总结

## <N>.8 给我们的启示
我应该把哪些 mindset 装进自己?(为下一篇 Apply & Creation 做铺垫)
```
