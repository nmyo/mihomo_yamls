# Contributing to Mihomo YAMLs Collection

首先，非常感谢你想为本仓库做出贡献！🎉
First off, thanks for taking the time to contribute! 🎉

本仓库旨在**自动化聚合**优质的 Mihomo/Clash Meta 配置文件。为了保持仓库的整洁和高效，请在提交 Issue 或 Pull Request 前阅读以下指南。

---

## 🛑 在提交 Issue 之前 (Before Submitting an Issue)

1.  **这不是机场客服**：
    * ❌ 不要提问：“为什么连不上网？”、“为什么节点超时？”（请联系你的节点提供商）。
    * ❌ 不要提问：“哪里有免费节点？”（本仓库不提供任何节点订阅）。
2.  **检查重复**：请先搜索现有的 [Issues](https://github.com/HenryChiao/mihomo_yamls/issues) 看看是否有人提过类似问题。
3.  **阅读文档**：很多基础问题在 [README](./README.md) 或官方 [Wiki](https://wiki.metacubex.one/) 中已有解答。

---

## 🐛 提交 Bug 报告 (Reporting Bugs)

如果你发现：
* GitHub Actions 自动更新失败。
* 某个文件的下载链接失效（404）。
* README 中的表格显示错乱。

请使用 **Bug Report** 模板，并提供相关文件路径和错误日志。

---

## 🚀 提交新配置源 (Submitting New Configs)

欢迎推荐优秀的开源配置！请使用 **Submit New Config** 模板，并遵循以下标准：

* **必须开源**：原作者的仓库必须是 Public 的。
* **Mihomo 专用**：配置应使用 `rule-set`, `geox`, `listeners` 等 Meta 核心的新特性。
* **长期维护**：不接受由于长期未更新而导致无法使用的旧配置。
* **无硬编码密钥**：配置中**绝对不能**包含个人的节点信息、密钥或 Token。

---

## 🛠 开发与 Pull Request (Development)

如果你想直接修改代码（例如优化 Python 生成脚本或 GitHub Workflows）：

1.  Fork 本仓库。
2.  创建一个新的分支 (`git checkout -b feature/AmazingFeature`)。
3.  提交你的更改 (`git commit -m 'Add some AmazingFeature'`)。
4.  推送到分支 (`git push origin feature/AmazingFeature`)。
5.  提交 Pull Request。

### 脚本说明
* `.github/workflows/main.yml`: 核心调度逻辑。
* 生成 README 和 Release 的逻辑嵌入在 Workflow 的 Python 脚本步骤中，修改时请注意缩进。

---

## ⚖️ 行为准则 (Code of Conduct)

* 请使用友善、尊重的语言。
* 禁止发布任何违反中国大陆法律法规的内容。
* 禁止发布任何形式的广告或引流链接。

感谢你的理解与支持！
