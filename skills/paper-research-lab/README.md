# Paper Research Lab｜论文深度阅读 Skill

一个可复用的 **Agent Skill**，以「研究路径重建 → 证据审查 → 研究卡」为核心，按需支持图表/公式聚焦和跨论文比较。默认中文，技术术语附英文。研究卡必须包含可检验问题、对照、指标、停止规则。

## 包内文件

- `SKILL.md`：唯一主入口，包括严格流程、证据标签、六问、输出模式与验收检查。
- `agents/openai.yaml`：可选的技能显示名称及默认调用提示。
- `references/research-type-checklists.md`：按论文类型切换的证据标准。
- `references/vision-restoration-sr.md`：SR / Restoration / NVS / RAW-sRGB 特有风险。
- `assets/brief-template.md`：研究逻辑与决策点笔记模板。
- `assets/evidence-audit-template.md`：每张图/表固定六问与核心主张矩阵。
- `assets/research-card-template.md`：可证伪研究卡及放弃条件。
- `assets/paper-index-template.md`：跨论文知识地图。

## 在 ChatGPT 使用

若你的账号/工作区显示 **Plugins → Skills**，打开 **Create → Upload from your computer**，选择 `paper-research-lab.zip`。若没有 Skills 入口，通常是当前账户或工作区尚未开放；也可以把 `SKILL.md` 放进项目文件，并明确要求“按该 SKILL.md 精读论文”。上传 ZIP 并不等于自动安装成功，以界面提示为准。

## 在 Codex 使用

将 `paper-research-lab` **整个目录**复制到 Codex 可以发现的技能位置，例如项目根目录下 `.agents/skills/paper-research-lab/`（按实际 Codex 安装版本的技能目录规则操作）。之后可直接调用 `$paper-research-lab`。

## 推荐用法

- **完整精读**：`用 $paper-research-lab 的 standard 模式读我上传的 PDF。先给结论，再重建研究过程，逐图逐表审查，并生成 1–3 张研究卡。` 
- **单图六问**：`用 $paper-research-lab 的 figure 模式讲 Figure 4（包括 panel a/b/c），严格回答固定六问。`
- **从论文到实验**：`用 $paper-research-lab 的 deep 模式检查这篇论文最薄弱的结论，并给可区分竞争解释的最小实验。`
- **跨论文综合**：`用 $paper-research-lab 的 compare 模式，比较这 3 篇论文支持同一主张的证据，并更新 paper_index。`
- **公式精讲**：`用 $paper-research-lab 的 math 模式逐步解释公式 (7)，定义符号并解释假设和直觉。`

## Skill 的边界

此包只包含审读流程和模板，不自带论文内容或联网访问能力。是否能获取全文/PDF、真实检查图像、创建笔记文件，取决于使用它的 ChatGPT/Codex 环境。未读到图表时会显式标注未核实。
