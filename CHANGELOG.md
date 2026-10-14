# Changelog

此仓库使用面向每个 Skill 的语义化版本（`vMAJOR.MINOR.PATCH`）。新版本应同步更新 Skill 源目录、`dist/` 安装包和各 README 中的版本链接。

## Paper Research Lab

### v1.1.0 — 2026-10-13

- 新增研究类型 × 主张类型（Research-Type / Claim-Type）的双轴路由，混合研究分别审查不同类型的核心结论。
- 新增六个按需加载的专项审查模块：理论证明、系统性能、因果推断、临床/生物医学、定性/混合方法、综述/元分析。
- 图表六问扩展为「核心证据单元六问」，支持 Theorem / Proof / Quote / Case；研究卡可提出证明、反例、负案例和合规验证，不再强制一律做实验。
- 更新笔记模板、文档与安装包；新增验证脚本 `scripts/validate_skill.py` 和**手工**路由测试场景。保留 v1.0.0 ZIP 作为历史版本。

### v1.0.0 — 2026-10-13

- 首次发布三层科研论文阅读工作流：研究路径重建、图表证据审查、可证伪研究卡。
- 提供 `quick` / `standard` / `deep` / `figure` / `math` / `compare` 模式，以及 SR / Restoration / NVS 专项检查清单和笔记模板。
- 添加公共仓库首页、ChatGPT / Codex 安装指南、可复制的使用示例、可重建的版本化 ZIP 安装包。

未来更新按版本追加条目；不把尚未实现的功能写成已支持。
