# AI Skills

**可复用的 AI 研究工作流（Reusable research-focused Agent Skills）。** 每个 Skill 都是一个独立目录，包含 `SKILL.md`、参考资料和可复用模板。可以按需安装到 Codex；符合条件的 ChatGPT 工作区也可上传打包好的 Skill。

## Skills

| Skill | 能解决什么问题 | 版本 | 入口 |
| --- | --- | --- | --- |
| **Paper Research Lab** | 不停留在论文摘要：重建研究论证路径 → 逐图逐表审查证据 → 形成可证伪的实验方案。支持 ML、CV、SR / Restoration / NVS 等研究。 | `v1.0.0` | [介绍与示例](skills/paper-research-lab/README.md) · [SKILL.md](skills/paper-research-lab/SKILL.md) |

## Quick start｜快速开始

### 方式 A：ChatGPT（需有 Skills 功能）

1. [下载 **Paper Research Lab v1.0.0 ZIP**](dist/paper-research-lab-v1.0.0.zip)。**这是 Skill 专用 ZIP**，不是整个 GitHub 仓库的 ZIP。
2. 在可使用 Skills 的 ChatGPT 工作区进入 **Plugins → Skills → Create → Upload from your computer**，上传这个 ZIP，并按界面提示完成安装。
3. 在对话里输入 `@` 选择该 Skill（若支持），再附上论文 PDF、链接或标题并说明想使用的模式。

> **权限说明：** ChatGPT 的 Skills 功能受账号、工作区和管理员设置限制；没有 Skills 入口时不代表 ZIP 无效。可参阅 [安装指南中的替代方法](INSTALL.md#没有-skills-入口怎么办)。上传 ZIP 不会把 Skill 自动安装到所有对话或项目。

### 方式 B：Codex（macOS / Linux，用户级安装）

```bash
git clone https://github.com/Ray-Luo/ai-skills.git
mkdir -p "$HOME/.agents/skills"
cp -R ai-skills/skills/paper-research-lab "$HOME/.agents/skills/"
```

随后在 Codex CLI / IDE 中使用：

```text
$paper-research-lab 用 standard 模式读我提供的论文：先重建研究路径，再逐图逐表审查证据，最后形成 1–3 张可证伪的研究卡。
```

也可以把 Skill 装在某个项目的 `.agents/skills/` 里，仅供该项目使用。具体步骤（包括 Windows）见 [INSTALL.md](INSTALL.md)。

## What it produces｜产出什么

- **Research reconstruction**：已有认识、Gap、假设、研究选择与反事实。
- **Evidence audit**：逐图逐表回答固定六问，区分论文报告事实、作者解释、审读者推断及未核实内容。
- **Research cards**：把证据缺口转成可以验证或放弃的实验设计；明确数据、对照、指标、阈值与停止规则。
- **Short navigation + separate notes**：避免一篇论文的所有细节挤在单条长回复中；有文件能力时分文件整理。

## Documentation

- [安装、更新与故障排查](INSTALL.md)
- [Paper Research Lab：详细说明、模式和示例](skills/paper-research-lab/README.md)
- [版本记录](CHANGELOG.md)
- [MIT License](LICENSE)

## Repository layout

```text
ai-skills/
├── README.md
├── INSTALL.md
├── CHANGELOG.md
├── LICENSE
├── skills/
│   └── paper-research-lab/
│       ├── SKILL.md
│       ├── README.md
│       ├── agents/openai.yaml
│       ├── assets/                # 笔记、证据审计、研究卡、论文索引模板
│       └── references/            # 不同研究类型和 SR 专项审查清单
├── dist/
│   └── paper-research-lab-v1.0.0.zip  # 可直接上传的 Skill 包
└── scripts/
    └── package_skill.py          # 生成可复现 ZIP（Python 标准库）
```

**注意：** 本仓库的 `skills/` 是源文件分发目录，**不会仅因克隆本仓库就自动被 Codex 发现**。Codex 需要在 `.agents/skills/` 这样的技能搜索路径下找到它（见安装指南）。

## Versioning & contributions

每个 Skill 独立按 `vMAJOR.MINOR.PATCH` 管理；`skills/<name>/` 是源文件，`dist/<name>-vX.Y.Z.zip` 是对应的安装包。修改 Skill 后运行 `python3 scripts/package_skill.py <name> --version X.Y.Z` 重新生成 ZIP，并同步更新文档及 [CHANGELOG](CHANGELOG.md)。

欢迎通过 Issue / Pull Request 提交勘误、阅读案例或新 Skill。Skill 是研究辅助流程，不代替原论文阅读、事实核验或独立实验复现。
