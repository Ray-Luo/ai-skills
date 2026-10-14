# Installation & Usage｜安装与使用

此仓库的 **`skills/<skill-name>/` 是源文件目录**。要使用它，必须通过产品支持的 Skills 导入流程安装，或把完整目录放入 Codex 的 Skill 搜索路径。只下载单个 `SKILL.md`，并不等于安装了它引用的全部模板与参考资料。

本文以 [`paper-research-lab`](skills/paper-research-lab/) 为例。以下方式对应 **v1.1.0**。

## 1. ChatGPT：上传 Skill ZIP

**前提：** 账号/工作区已启用 Skills，且管理员允许创建或上传。当前公开说明中，ChatGPT Skills 面向符合条件的 Business / Enterprise / Healthcare / Edu 工作区；其他账号不应假定已有相同入口。

1. 下载 [**paper-research-lab-v1.1.0.zip**](dist/paper-research-lab-v1.1.0.zip)。该 ZIP 包含单个顶层目录 `paper-research-lab/` 和内部全部 Skill 文件。
2. 打开 ChatGPT，进入 **Plugins → Skills**（如该入口对你的工作区可用）。
3. 点击 **Create → Upload from your computer**，选择下载的 ZIP。
4. 根据页面完成检查与安装；上传成功与实际可调用是两个步骤，以界面确认结果为准。
5. 在聊天里键入 `@` 并选择对应 Skill（支持时），提供论文 PDF / arXiv 链接 / DOI / 标题及阅读模式。

使用示例：

```text
用 Paper Research Lab 的 standard 模式读这篇论文：
先重建研究逻辑，再逐图审计结论，最后输出 1–3 张可证伪的研究卡。
```

**安全提醒：** 第三方 Skill 可能包含执行代码或外部资源，上传前应检查来源和内容。本仓库当前发布的 Paper Research Lab 以指令、参考资料与 Markdown 模板为主。

### 没有 Skills 入口怎么办？

- 可以先手动阅读 [`SKILL.md`](skills/paper-research-lab/SKILL.md)，把它**及关联的 `assets/` 和 `references/` 文件**作为项目资料上传，要求助手遵循该工作流。这是手动使用，不等于把它安装成系统级 Skill；具体能否访问资料取决于产品的文件能力。
- 如果使用 Codex CLI / IDE，直接参考下方本地安装方式。
- 不建议把 GitHub 仓库的 **Code → Download ZIP** 当成单独的 Skill ZIP：那个压缩包顶层是整个仓库，而不是单个 `paper-research-lab/` Skill。

官方参考：[OpenAI Help Center — Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)。

## 2. Codex：用户级安装（推荐）

用户级 Skill 在个人使用的各个仓库中可被 Codex 发现。官方搜索位置为 **`$HOME/.agents/skills/`**。

**macOS / Linux**：

```bash
git clone https://github.com/Ray-Luo/ai-skills.git
mkdir -p "$HOME/.agents/skills"
cp -R ai-skills/skills/paper-research-lab "$HOME/.agents/skills/"
test -f "$HOME/.agents/skills/paper-research-lab/SKILL.md" && echo "Skill installed"
```

**Windows PowerShell**：

```powershell
git clone https://github.com/Ray-Luo/ai-skills.git
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse -Force "./ai-skills/skills/paper-research-lab" "$HOME/.agents/skills/"
Test-Path "$HOME/.agents/skills/paper-research-lab/SKILL.md"
```

然后打开 Codex CLI 或 IDE 扩展，输入 `/skills` 查看可用的 Skill，或者在提示词里输入：

```text
$paper-research-lab 用 standard 模式阅读我给你的论文 PDF。
```

Codex 可检测 Skill 改动；如果新安装或更新后没有出现，重新启动 Codex 再试。

### 项目级安装（只在某个 Repo 生效）

在**你希望使用该 Skill 的目标项目**下安装，而不是只把本仓库 clone 下来：

```bash
# 在目标项目根目录执行，假定旁边已有 ai-skills 仓库
mkdir -p .agents/skills
cp -R ../ai-skills/skills/paper-research-lab .agents/skills/
```

以上 `../ai-skills` 只是示例相对路径；请按实际目录调整。验证 `./.agents/skills/paper-research-lab/SKILL.md` 已存在。Codex 会从当前工作目录一路向 Git 仓库根目录搜索 `.agents/skills/`。

也可以在 Codex 内尝试 `$skill-installer`，让其从本 GitHub 仓库的 `skills/paper-research-lab` 路径安装；如果当前 Codex 版本不支持此操作，就使用上述复制方式。

官方参考：[OpenAI — Build skills（包括 Skill 搜索路径）](https://developers.openai.com/codex/skills)。

## 3. 更新 Skill

- **Codex**：先 `git pull` 更新你的 `ai-skills` 克隆，再用新版 `skills/paper-research-lab/` 覆盖已安装的对应目录。注意同名目录复制时某些系统可能创建嵌套目录；确保最终路径仍是 `.../.agents/skills/paper-research-lab/SKILL.md`。必要时删除旧目录后再复制，避免残留过期文件。
- **ChatGPT**：下载最新版本专用 ZIP，在可用的 Skills 管理界面更新/重新上传；不同产品和工作区的版本同步不保证自动发生。
- 每次可在 [CHANGELOG.md](CHANGELOG.md) 找到版本对应变更。一个 ZIP 发布版本不代表 GitHub 所有分支自动同步。

## 4. 维护者：重新打包发布

从仓库根目录运行（需要 Python 3 标准库，无需第三方包）：

```bash
python3 scripts/package_skill.py paper-research-lab --version 1.1.0
unzip -l dist/paper-research-lab-v1.1.0.zip
python3 scripts/validate_skill.py paper-research-lab --version 1.1.0
```

压缩包必须包含**唯一**顶层目录 `paper-research-lab/`，其中有 `SKILL.md`，且引用的 `agents/`、`assets/`、`references/` 均随包提供。每次修改 Skill 文件后，更新版本号、对应 ZIP、入口 README 和 CHANGELOG，并运行上述验证脚本检查本地引用、ZIP CRC 和 ZIP 与源码内容一致。对于领域路由，还需参考 [`tests/reading-scenarios.md`](tests/reading-scenarios.md) 手动核验实际模型行为。

## 5. Troubleshooting｜常见问题

| 现象 | 检查点 |
| --- | --- |
| ChatGPT 没有 Skills 菜单 | 当前账号/工作区的功能、管理员策略可能不支持；可手动提供 Skill 文件或改在 Codex 使用 |
| 上传后找不到 Skill | 确认已按界面完成安装；确认 ZIP 不是整个 GitHub 仓库的 ZIP |
| Codex 不能识别 `$paper-research-lab` | 检查 `SKILL.md` 路径；在 Codex 输入 `/skills`；必要时重启 |
| 能用 Skill，但看不到论文图表 | 阅读能力取决于输入 PDF/图像与运行环境；要求标记未核实内容，不能臆测 |
| 输出中没有 Markdown 笔记文件 | 所用环境可能没有文件写入能力；可要求在聊天中分段输出，或切换到具备文件能力的环境 |
