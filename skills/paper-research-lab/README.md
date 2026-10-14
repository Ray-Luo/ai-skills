# Paper Research Lab

**读论文不是只要一个摘要，而是把论文读成可检查、可复现、可继续研究的论证链。** 这个 Skill 用于科研论文阅读（paper reading / critique / research planning），默认中文解释，保留重要英文技术术语。

> **一句话工作流：** 重建研究路径 → 检查核心结论的证据 → 从未解决的证据缺口设计下一步实验。

- 当前版本：**v1.1.0**
- [下载可安装 ZIP](https://github.com/Ray-Luo/ai-skills/blob/main/dist/paper-research-lab-v1.1.0.zip) · [完整安装说明](https://github.com/Ray-Luo/ai-skills/blob/main/INSTALL.md) · [Skill 主指令](SKILL.md)
- 适用：ML / CV / NLP、SR / Restoration / NVS、理论、系统、因果、临床、定性、数据集与综述论文。先判断研究类型，再判断作者的核心主张类型。

## 三层分析方法

| 层次 | 核心问题 | 主要产物 |
| --- | --- | --- |
| **1 · Research reconstruction** | 前人知道什么？Gap 在哪里？研究假设是什么？为什么选择这些数据、模型、baseline、指标？换一种选择会怎样？ | 研究逻辑链 + 决策点账本（Decision Ledger） |
| **2 · Evidence audit** | 每个核心主张的证据在哪里？图表、证明、访谈或案例直接支持什么？作者解释是否超出证据？ | Claim–Evidence Matrix + 每个核心证据单元六问 |
| **3 · Research-to-experiment** | 证据留下的空白怎样变成可检验的假设、猜想或竞争解释？什么验证最有信息价值，什么结果应该放弃？ | 1–3 张 Research Cards |

整个分析持续区分四种标签：`[P]` 原文报告的事实、`[A]` 作者的解释、`[R]` 审读者推断、`[U]` 未核实/缺失。不把作者论文中的逻辑叙事写成其真实研究时间线，也不把未做过的反事实实验写成已有结果。

### 图表固定六问

每张可读取的 Figure / Table（必要时细到每个 panel）都回答。对于无图论文，改以 Theorem / Proof / Quote / Case 等证据单元回答同样六问：

1. **为什么做？** 要检验什么假设或排除什么解释？
2. **怎么做？** 数据、变量、对照、模型、预算和评测设置是什么？
3. **怎么看？** 图表的轴/图例/误差线、证明的量词/推导、引语的语境/编码该怎么读？
4. **发现什么？** 图表直接报告或显示了什么观察结果？
5. **支持到哪？** 哪些结论成立、在哪些条件下成立、有哪些未证明部分？
6. **为什么接下一张图/证据单元？** 当前证据还缺什么，下一项是否真正回应？

## 不同类型论文怎样使用同一个 Skill？

采用 **Research-Type + Claim-Type 双轴路由**：先识别论文属于哪种研究，再识别它具体承诺了什么。只有相应的专项清单被加载，不用 AI benchmark 一把尺子衡量所有学科。

| 研究类型 | 优先审查 | 最有用的 Research Card |
| --- | --- | --- |
| ML / CV / SR | Baseline 公平、数据/退化、Ablation、泛化 | 可区分竞争机制的消融或独立验证 |
| Theory / Algorithms | 前提、量词、Proof dependencies、反例 | 猜想、形式化证明或边界反例 |
| Systems / Efficiency | 工作负载、端到端延迟、质量约束 | 同质量的可复现性能基准 |
| Causal / Observational | 估计对象、识别假设、混杂因素 | 识别改进、安慰剂或敏感性分析 |
| Clinical / Biomedical | 研究设计、获益和伤害、适用人群 | 经伦理审查的独立验证或合规再分析 |
| Qualitative / Mixed Methods | 抽样、编码与主题、反身性、负例 | 负案例和竞争解释追踪 |
| Survey / Meta-analysis | 文献检索、方法可比性、异质性 | 证据冲突复核、新检索或比较研究 |

无图的数学/质性论文不会强行输出不存在的 Figure；没有统计实验的研究卡也不会被要求给出 p-value。**临床的 CONSORT 2025、系统综述的 PRISMA 2020 等报告规范只辅助核查信息透明度，不能自动视作研究质量评分。**

详细路由及专项清单在 [`references/research-type-checklists.md`](references/research-type-checklists.md)。

## 阅读模式

| Mode | 适合什么时候使用 | 深度 |
| --- | --- | --- |
| `quick` | 快速判断一篇 paper 是否值得精读 | 概览；**不声称已经逐图审查** |
| `standard` | 一篇论文的完整研究阅读（默认） | 三层流程；覆盖可获取的正文图表 |
| `deep` | 复现、审稿级质疑、设计 follow-up | 更严格检查 Supplement、baseline 公平性、实现细节和竞争解释 |
| `figure` | 聚焦特定 Figure / Table / Panel | 固定六问 + 与论文核心主张的联系 |
| `math` | 公式看不懂，想知道推导和直觉 | 符号、假设、推导、计算直觉、训练/推理影响 |
| `compare` | 几篇论文的方法与结果如何互相印证 | 比较任务/协议是否可比，再整理共同缺口与研究方向 |

## 复制即用的示例

**完整精读（推荐入门）：**

```text
$paper-research-lab
用 standard 模式分析我上传的 PDF。
先给可修订结论，然后重建研究路径、列出 3–5 个最重要的设计选择，
逐图逐表审查证据，最后给 1–3 张带停止条件的 Research Cards。
```

**逐图审读：**

```text
$paper-research-lab 用 figure 模式读 Figure 4 的每个 panel，严格回答六问；区分图中直接可见的证据、作者的解释和你的推断。
```

**专攻公式：**

```text
$paper-research-lab 用 math 模式解释 Eq. (7)：逐项定义符号、推导来源、隐含假设、直觉，并举一个小的数值例子。
```

**比较论文并找选题：**

```text
$paper-research-lab 用 compare 模式比较这三篇 Real-ISR 论文。先确认数据、退化、训练预算与指标是否可比，再识别证据冲突并给出最低成本的区分实验。
```

**理论论文（没有实验图）：**

```text
$paper-research-lab 用 deep 模式审读这篇算法收敛性论文：
重建前提和定理证明链、检查边界条件、寻找可能的反例；
把最值得验证的证明缺口做成 Theory Research Card。
```

**临床 / 因果 / 定性论文：**

```text
$paper-research-lab 用 standard 模式读这篇论文。先判断研究设计与主张类型；
依据相应的因果、临床或定性专项标准逐项审查，
不要机械套用 ML 的 baseline 或统计显著性要求。
```

**ChatGPT：** 如果界面支持 Skills，先输入 `@` 并选择 Paper Research Lab，然后使用相同的中文指令；`$paper-research-lab` 是 Codex 中更明确的调用方式。并非所有 ChatGPT 账号都有 Skills 功能。

## 输出文件与模板

当执行环境支持文件写入时，每篇论文拆成独立笔记，避免在单个聊天消息中反复滚动：

```text
notes/
├── paper_index.md                     # 多篇论文的综合索引（可选）
└── <paper-slug>/
    ├── 01_brief.md                     # 研究问题、路径、重要选择、修订结论
    ├── 02_evidence_audit.md            # 核心主张矩阵 + 逐图逐表六问
    └── 03_research_cards.md            # 可检验实验、对照、指标、停止规则
```

这些输出是**运行 Skill 时按论文生成的**，不是仓库中预先写好的论文分析。相应模板在 [`assets/`](assets/) 内。

## 文件目录

- [`SKILL.md`](SKILL.md)：触发条件、阅读流程、严格证据标签、研究卡验收标准。
- [`agents/openai.yaml`](agents/openai.yaml)：可选的 Codex/ChatGPT skill 元数据。
- [`references/research-type-checklists.md`](references/research-type-checklists.md)：研究类型 × 主张类型路由与共通审查准则。
- 专项规则：[`theory-and-proof.md`](references/theory-and-proof.md)、[`systems-and-benchmarking.md`](references/systems-and-benchmarking.md)、[`causal-inference.md`](references/causal-inference.md)、[`clinical-and-biomedical.md`](references/clinical-and-biomedical.md)、[`qualitative-research.md`](references/qualitative-research.md)、[`evidence-synthesis.md`](references/evidence-synthesis.md)。
- [`references/vision-restoration-sr.md`](references/vision-restoration-sr.md)：SR / Restoration / NVS / RAW-sRGB 的专项审查点。
- [`assets/brief-template.md`](assets/brief-template.md)、[`assets/evidence-audit-template.md`](assets/evidence-audit-template.md)、[`assets/research-card-template.md`](assets/research-card-template.md)、[`assets/paper-index-template.md`](assets/paper-index-template.md)：可复用的笔记模板。

## 已知边界

- 本 Skill **不是**论文 PDF 数据库、自动联网工具或真实实验运行环境；读取 PDF、Supplement、图像和代码的能力取决于使用它的 ChatGPT / Codex 环境。
- 只能看到图注时必须明确说明，不能假装看过真实曲线或 panel；缺少来源的数字标记 `[U]`。
- `standard/deep` 的逐图/证据审查只覆盖**实际可获取**的材料，且必须记录覆盖范围。
- Research Cards 是研究假设、证明或验证提案，不是论文已经验证的结论。
- 升级后的领域路由需要在具体论文上检验；[手工验收场景](https://github.com/Ray-Luo/ai-skills/blob/main/tests/reading-scenarios.md) 为测试清单，**并非已经执行的 LLM 实测结果**。
- 安装方法、版本更新与排障见 [INSTALL.md](https://github.com/Ray-Luo/ai-skills/blob/main/INSTALL.md)。
