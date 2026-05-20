#!/usr/bin/env python3
"""
Scaffold an empty .learning-notes/ directory with the standard structured note
skeleton plus a final concept-table.md, so you can start filling in Phase 4
(Structured Write-Up) without re-typing the section structure each time.

Usage:
  python3 scaffold-notes.py <repo-dir>
  python3 scaffold-notes.py <repo-dir> --target /custom/notes/path
  python3 scaffold-notes.py <repo-dir> --modules core,api,plugins   # custom module names

Produces:
  <repo-dir>/.learning-notes/
  ├── README.md                      ← index + 10 TL;DR placeholders
  ├── 01-overview.md
  ├── 02-architecture.md
  ├── 03-<module-1>.md ... 03+N-<module-N>.md  (if --modules)
  ├── M-engineering.md
  ├── M+1-design-patterns.md       [Layer 3 总集]
  ├── M+2-mindset-and-philosophy.md [Layer 4 ★ 核心:作者的 mindset]
    ├── M+3-apply-and-creation.md     [Layer 5 ★ 产出:用 mindset 创造]
    └── concept-table.md              [Final synthesis ★ 概念表 / wikilink 入口]

Each stub has a GitHub Markdown-friendly section skeleton. The four-layer iceberg model
(see SKILL.md) is reflected in the file naming, section structure, and final synthesis artifact.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

# --- Section skeletons -----------------------------------------------------

README_TMPL = """# {repo_name} 深度拆解

> Learning in Public · 仓库:`{repo_name}` · 起稿:{today}
>
> 面向读者:`<TODO: 目标读者>` · 发布位置:`<TODO: repo/docs/blog/wiki>`
>
> 目的:**穿透到冰山之下** —— 不止学"它是什么",更学作者的 mindset 与决策框架,
> 最终把学到的东西组织成可公开分享、可持续迭代的研究产物。
>
> ⚠️ 目录名保留为 `.learning-notes/`,但内容默认按可提交、可分享、可公开发布的文档来写,并纳入版本控制持续迭代。

## 学习目标分层(冰山模型)

```text
冰山之上(易学,价值低)
  L1 Knowledge — 仓库做什么
  L2 Skill — 怎么用
─── 水线 ───
冰山之下(难学,价值高)
  L3 Patterns — 设计模式与抽象  ← 多数学习停在这里
  L4 Mindset — 作者的决策框架    ← 这次重点
  L5 Creation — 用学到的创造     ← 真正的产出
```

## 你需要先理解的一句话

> **<TODO: 仓库设计的核心 metaphor 或抽象名字>** —— <TODO: 一句话>。

## 作者的 Mindset 一句话(Phase 5 后回来填)

> "<TODO: 作者的 mindset 浓缩成 1-2 句话>"

## 阅读顺序

| # | 文档 | Layer | 一句话提要 |
| --- | --- | --- | --- |
| 01 | [overview.md](./01-overview.md) | L1+L2 | 仓库做什么、为什么这样做 |
| 02 | [architecture.md](./02-architecture.md) | L3 | 整体架构 + 数据流 + 不变量 |
{module_index}| M | [engineering.md](./{M}-engineering.md) | L2+L3 | 工程脚手架 |
| M+1 | [design-patterns.md](./{M_plus_1}-design-patterns.md) | L3 | 可复用设计模式 |
| **M+2** | **[mindset-and-philosophy.md](./{M_plus_2}-mindset-and-philosophy.md)** | **L4 ★** | **作者的 mindset 与设计哲学(核心)** |
| **M+3** | **[apply-and-creation.md](./{M_plus_3}-apply-and-creation.md)** | **L5 ★** | **用 mindset 在我领域创造** |
| CT | [concept-table.md](./concept-table.md) | Synthesis | 最终概念表 + 跨文档导航 |

## 全局 TL;DR(10 条关键洞察)

<TODO: 第一轮深挖完成后填。混合 L3 模式 + L4 mindset。每条标 layer。>

1. **[L3]** <洞察 1>
2. **[L4]** <洞察 2>
...
10. **[L5]** <洞察 10>

## 概念导航

- 运行收尾时生成 [concept-table.md](./concept-table.md),统一回收 8-20 个高复用概念
- 其他文档第一次出现共享概念时,优先补 `[[concept-table#Trust Boundary Isolation|Trust Boundary Isolation]]`
- 若这批文档会同步发布到 GitHub,再并排保留普通 Markdown link

## 我后续要公开发布的延伸内容

- [ ] 用学到的 mindset 在我领域做 1 个具体项目
- [ ] <TODO>
"""

OVERVIEW_TMPL = """# 01 · 高层概览

## 1.1 一句话定位
<TODO: 这个仓库是什么,业务 + 技术>

## 1.2 仓库结构层次
```text
<TODO: 目录树>
```
重点说"几层 / 有没有循环依赖"。

## 1.3 多部署形态(如有)
<TODO: 图示 — 核心源 → 多个 wrapper>

## 1.4 产物差异表
| 产物 | 形态 | 谁安装 | 调用方式 |
| --- | --- | --- | --- |

## 1.5 为什么这样做?(背后的商业 + 工程判断)

### 判断 A:<TODO>
<证据 + path:line>

### 判断 B:<TODO>
### 判断 C:<TODO>
### 判断 D:<TODO>

## 1.6 它的边界:不解决什么
<TODO: 诚实列出局限>

## 1.7 带着什么问题往下读
<TODO: 3 类 reader 的关注点>
"""

ARCHITECTURE_TMPL = """# 02 · 整体架构

## 2.1 全景架构图

```text
┌─────────────────────────────────────┐
│  TODO: 用户层                        │
└─────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  TODO: 应用层                        │
└─────────────────────────────────────┘
            │
            ▼
   <TODO: 完整 ASCII 架构图>
```

## 2.2 N 层栈的职责契约
| 层 | 物理位置 | 职责 | 严格不做 |
| --- | --- | --- | --- |

## 2.3 关键设计契约
<TODO: 展开讲机制,如 "One Source Two Wrappers" 这种>

## 2.4 一次完整调用的数据流
<TODO: 从用户输入 → 最终输出,每步谁在做>

## 2.5 不变量(Invariants)清单

1. <TODO>
2. <TODO>
...
10. <TODO>

→ 这些不变量是骨架,后面所有细节都是它们的实例。
"""

MODULE_TMPL = """# {n} · {module_name}

> <TODO: 这章为什么重要>

## {n}.1 关键事实:体量

| | 数字 |
| --- | --- |
| 文件数 | ... |
| 总行数 | ... |

## {n}.2 通用骨架
```text
<TODO: 这个模块所有文件遵循的骨架>
```

## {n}.3 反复出现的 Pattern

### Pattern 1:<名字>
<具体描述 + path:line>

### Pattern 2:...

## {n}.4 代表性样本对比
| 维度 | 样本 A | 样本 B | 样本 C |
| --- | --- | --- | --- |

## {n}.5 Worked Example:逐行解剖
<TODO: 挑 1 个文件,逐行注解>

## {n}.6 限制
<TODO: 诚实评估>

## {n}.7 复用 checklist
- [ ] <TODO>
"""

ENGINEERING_TMPL = """# {M} · 工程基础设施

## 1. 开发循环全景

```text
开发者 ──编辑──> <源>
                  │
                  ▼
              <sync>
                  │
                  ▼
              <lint>
                  │
                  ▼
              <pre-commit>
                  │
                  ▼
              <push + CI>
```

## 2. 每个脚本的职责

### <script-1>:<职责>
- 关键检查项
- 关键代码 ≤ 15 行
- path:line

### <script-2>:...

## 3. git hooks
<TODO>

## 4. CI workflows
<TODO>

## 5. "无聊但关键"的工程决策
- 决策 1
- 决策 2

## 6. 复用清单
- [ ] <TODO>
"""

PATTERNS_TMPL = """# {M_plus_1} · 可复用设计模式总集

> 8-12 个有名字的设计模式。每个附:出处 · 定义 · 何时用 · 如何用 · 反例 · 复用难度。

---

## 模式 1:<名字>

**出处** · <path:line>

**定义** · <一句话>

**何时用** · <场景>

**如何用** ·
- 步骤 1
- 步骤 2

```text
<伪代码示例>
```

**反例** · <错误做法>

**复用难度** · ★/★★/★★★

---

## 模式 2:<TODO>

---

## 心法(不算 pattern,但值得记)

### 心法 A:<名字>
<段落>

---

## 模式速查表

| # | 模式 | 复用难度 | 影响范围 |
| --- | --- | --- | --- |
"""

MINDSET_TMPL = """# {M_plus_2} · 作者的 Mindset 与设计哲学  [Layer 4 ★]

> 这是 Skill 的核心产出之一。Phase 5 用 7 种 mindset extraction 方法跑完后填这里。
> 详细方法参见 _skill-repo-deep-dive/references/mindset-extraction.md

## {M_plus_2}.1 五条核心 Mindset 信条(用作者口吻陈述)

1. **<TODO: 信条 1>** — <证据 + path:line>
2. **<TODO: 信条 2>**
3. **<TODO: 信条 3>**
4. **<TODO: 信条 4>**
5. **<TODO: 信条 5>**

## {M_plus_2}.2 取舍频谱画像(10 轴)

```text
简单(simple) ────────────── 完整(complete)        ← TODO 标 ●
灵活(flexible) ────────────── 严格(strict)
显式(explicit) ────────────── 隐式(implicit)
当前(short-term) ────────────── 长期(long-term)
内部(in-house) ────────────── 外部(open ecosystem)
文档驱动 ────────────── 代码驱动
统一(uniform) ────────────── 多样(pluralistic)
约定(convention) ────────────── 配置(configuration)
新颖(novel) ────────────── 保守(boring)
通用(general) ────────────── 专用(specialized)
```

## {M_plus_2}.3 "为什么 NOT" 案例(≥ 3 个)

### NOT 案例 1:作者明显没做 <X>
- **业界默认**:<Y>
- **为什么没做** 的归因:<Z>
- **mindset 标签**:<...>

### NOT 案例 2 / 3:<TODO>

## {M_plus_2}.4 价值观痕迹

- **注释里的 "why"**:<例子 + path:line>
- **命名风格**:<例子 + 暗示的价值取向>
- **错误信息语气**:<例子 + 友好/冷酷/教育/谦逊>
- **文档篇幅分配**:<哪些详哪些简,揭示作者最在乎什么>
- **测试覆盖分配**:<哪些重测哪些不测,揭示作者认为什么易出错>

## {M_plus_2}.5 受众假设

**作者的"心智读者"画像**:<具体描述,如"金融 IT staff+ 工程师,有经验,有耐心">

**所以仓库不照顾**:<目标外的人群,如"刚入门的开发者">

## {M_plus_2}.6 第一性原理:作者拒绝接受什么

| 业界默认 | 作者拒绝? | 根本原因(mindset) |
| --- | --- | --- |
| <默认 1> | ✓/✗ | <为什么> |
| <默认 2> | ✓/✗ | <...> |
| ... 至少 7 条 | | |

## {M_plus_2}.7 综合 Mindset 信条

把 5 条信条 + 7 条拒绝 浓缩成 1-2 句话:

> "<TODO: 作者的 mindset 一句话总结>"

## {M_plus_2}.8 给我的启示

- 哪些 mindset 我想装进自己?
- 哪些 mindset 我不想抄(可能不适合我的场景)?
- 这些 mindset 对我现在的工作产生什么具体改变?
"""

CREATION_TMPL = """# {M_plus_3} · 应用 Mindset + 创造路径  [Layer 5 ★]

> Skill 的核心最终产出之一。前面所有 phase 都是为这里准备的。
> 4 种路径:用法转移 / 表层替换 / mindset 混合 / mindset 挑战。
> 详细方法参见 _skill-repo-deep-dive/references/internalization-and-creation.md

## {M_plus_3}.1 我装进自己的 5 条 Mindset 信条

(从 mindset-and-philosophy.md 复制最受用的 5 条)

1. **<信条 1>**
2. **<信条 2>**
3. **<信条 3>**
4. **<信条 4>**
5. **<信条 5>**

## {M_plus_3}.2 路径 A:用法转移(我工作中的 5 个应用)

### 问题 1:<我工作中开放的问题>
- **应用前 / 现状**:<现在怎么处理>
- **应用后 / 用 mindset 重构**:<用学到的 mindset 我会怎么处理>
- **成本 / 风险 / ROI**:<...>

### 问题 2 - 5:<TODO,至少 3 个具体应用>

## {M_plus_3}.3 路径 B:表层替换(可选,中等难度)

**我的另一个完全不同的业务场景**:<场景描述>

**用同样 mindset 重构的设计**:
```text
<画出系统图,显式标注每个模块对应哪条 mindset 信条>
```

## {M_plus_3}.4 路径 C:Mindset 混合(可选,高难度)

**与我之前研究的 <仓库 Y> 的 mindset 组合**:

| 冲突点 | 我的选择 | 理由 |
| --- | --- | --- |
| ... | ... | ... |

| 互补点 | 产生的新设计 |
| --- | --- |
| ... | ... |

## {M_plus_3}.5 路径 D:Mindset 挑战(可选,最高难度)

**作者拒绝做的**(从 mindset-and-philosophy.md 拿 ≥ 3 条):
- ...

**反向设计可能是**:
- <具体设计>

**它服务谁(原作者不服务的人群)**:
- <目标用户>

## {M_plus_3}.6 我的第一个具体创造

从 A/B/C/D 选 1 个最有价值的,落地。

### 项目名:<...>

### 用到的 mindset 信条:<列编号>

### 与原仓库的关系:
- **相同**:<哪些 mindset 保留>
- **不同**:<哪些场景 / 表层 / 决策不同>

### 30 / 60 / 90 路线图

| Week | 目标 |
| --- | --- |
| 1 | <TODO> |
| 2 | <TODO> |
| ... | |
| 12 | <TODO> |

## {M_plus_3}.7 反思:这次学习让我成为了什么样的人?

(留 5-10 行让自己写,不要省略 —— 这是 internalization 的"测试")

<TODO>

## {M_plus_3}.8 12 个月后回看本文档

- 我用学到的 mindset 实际做了什么?
- 哪些 mindset 我用对了?
- 哪些 mindset 让我吃亏了?
- 我现在会怎么补充 / 修正这份文档?
"""

CONCEPT_TABLE_TMPL = """# Concept Table · 最终汇总与概念导航

> Final synthesis · 统一共享概念入口 · 其他文档通过 `[[concept-table#<Concept Heading>|<Alias>]]` 回链到这里。

## Final Synthesis

<TODO: 用 200-400 字总结这个仓库最值得带走的 3-5 个抽象 / 3-5 条 mindset / 3-5 个 transfer 机会。>

## 使用约定

- 只收录会在 2 篇以上文档复用的概念(建议 8-20 个)
- 概念标题尽量用稳定、可 slug 的短英文短语;中文解释写在正文第一段
- 其他文档第一次出现共享概念时,补 `[[concept-table#Trust Boundary Isolation|Trust Boundary Isolation]]`
- 若这批文档需要 GitHub 兼容,并排保留 `[Trust Boundary Isolation](./concept-table.md#trust-boundary-isolation)`

## Concept Index

| Concept | Layer | One-line Definition | First Doc | Related |
| --- | --- | --- | --- | --- |
| <Concept 1> | L3/L4 | <TODO> | [02-architecture.md](./02-architecture.md) | <Concept 2> |
| <Concept 2> | L4/L5 | <TODO> | [{M_plus_2}-mindset-and-philosophy.md](./{M_plus_2}-mindset-and-philosophy.md) | <Concept 1> |

## <Concept 1>

**中文解释** · <TODO>

**为什么重要** · <TODO>

**主要证据** ·
- <path:line>
- <path:line>

**出现文档** ·
- [02-architecture.md](./02-architecture.md)
- [{M_plus_2}-mindset-and-philosophy.md](./{M_plus_2}-mindset-and-philosophy.md)

**相关概念** · <Concept 2>

**容易混淆** · <TODO>

**可迁移用法** · <TODO>

## <Concept 2>

**中文解释** · <TODO>

**为什么重要** · <TODO>

**主要证据** ·
- <path:line>

**出现文档** ·
- [{M_plus_3}-apply-and-creation.md](./{M_plus_3}-apply-and-creation.md)

**相关概念** · <Concept 1>

**容易混淆** · <TODO>

**可迁移用法** · <TODO>
"""


# --- Generator -------------------------------------------------------------

def write(path: Path, content: str) -> None:
    if path.exists():
        print(f"  ↻ skipped (exists): {path.name}", file=sys.stderr)
        return
    path.write_text(content)
    print(f"  ✓ wrote {path.name}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold .learning-notes/ skeleton")
    ap.add_argument("repo_dir", help="path to the target repository")
    ap.add_argument("--target", help="custom notes directory (default: <repo>/.learning-notes/)")
    ap.add_argument("--modules", help="comma-separated module names (e.g. core,api,plugins)")
    args = ap.parse_args()

    repo = Path(args.repo_dir).resolve()
    if not repo.is_dir():
        print(f"ERROR: {repo} is not a directory", file=sys.stderr)
        return 1

    notes_dir = Path(args.target) if args.target else (repo / ".learning-notes")
    notes_dir.mkdir(parents=True, exist_ok=True)

    modules = [m.strip() for m in args.modules.split(",")] if args.modules else []
    repo_name = repo.name
    today = date.today().isoformat()

    # Compute file numbering (now includes mindset + creation)
    module_count = len(modules)
    M = 3 + module_count                # engineering file number
    M_plus_1 = M + 1                    # design-patterns        [L3]
    M_plus_2 = M + 2                    # mindset-and-philosophy [L4 ★]
    M_plus_3 = M + 3                    # apply-and-creation     [L5 ★]

    # Build module index for README
    module_index_lines = []
    for i, m in enumerate(modules, start=3):
        slug = m.lower().replace(" ", "-")
        module_index_lines.append(f"| {i:02d} | [{slug}.md](./{i:02d}-{slug}.md) | L3 | <模块 `{m}` 深度解析> |\n")
    module_index = "".join(module_index_lines)

    print(f"Scaffolding into {notes_dir}/  ({module_count} module file(s) + L3+L4+L5 trio + concept table)")

    write(notes_dir / "README.md", README_TMPL.format(
        repo_name=repo_name, today=today,
        module_index=module_index,
        M=f"{M:02d}",
        M_plus_1=f"{M_plus_1:02d}",
        M_plus_2=f"{M_plus_2:02d}",
        M_plus_3=f"{M_plus_3:02d}",
    ))
    write(notes_dir / "01-overview.md", OVERVIEW_TMPL)
    write(notes_dir / "02-architecture.md", ARCHITECTURE_TMPL)

    for i, m in enumerate(modules, start=3):
        slug = m.lower().replace(" ", "-")
        write(notes_dir / f"{i:02d}-{slug}.md", MODULE_TMPL.format(n=f"{i:02d}", module_name=m))

    write(notes_dir / f"{M:02d}-engineering.md", ENGINEERING_TMPL.format(M=f"{M:02d}"))
    write(notes_dir / f"{M_plus_1:02d}-design-patterns.md",
          PATTERNS_TMPL.format(M_plus_1=f"{M_plus_1:02d}"))
    write(notes_dir / f"{M_plus_2:02d}-mindset-and-philosophy.md",
          MINDSET_TMPL.format(M_plus_2=f"{M_plus_2:02d}"))
    write(notes_dir / f"{M_plus_3:02d}-apply-and-creation.md",
          CREATION_TMPL.format(M_plus_3=f"{M_plus_3:02d}"))
    write(notes_dir / "concept-table.md",
          CONCEPT_TABLE_TMPL.format(M_plus_2=f"{M_plus_2:02d}", M_plus_3=f"{M_plus_3:02d}"))

    print("\nDone. Next:")
    print(f"  Phase 1 (L1+L2):全局扫描后,填 README.md 的'一句话定位'")
    print(f"  Phase 3-4 (L3):按章节骨架填 01/02/03-X-<module>/{M:02d}/{M_plus_1:02d} 文档")
    print(f"  Phase 5 (L4 ★):用 7 种 mindset 提取方法填 {M_plus_2:02d}-mindset-and-philosophy.md")
    print(f"               (见 _skill-repo-deep-dive/references/mindset-extraction.md)")
    print(f"  Phase 6 (L5 ★):4 种创造路径填 {M_plus_3:02d}-apply-and-creation.md")
    print(f"               (见 _skill-repo-deep-dive/references/internalization-and-creation.md)")
    print("  Final Synthesis:回写 README 的 TL;DR,并完善 concept-table.md 与跨文档 wikilinks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
