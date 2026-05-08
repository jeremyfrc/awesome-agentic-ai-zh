# 给开发者 — 专业分支

> [繁體中文](./for-developer.md) | **简体中文** | [English](./for-developer.en.md)

> [← 回主路线 README](../README.zh-CN.md) · 走完 **Track A 的 A3** 或 **Track B 的 Stage 7** 后从这里接续。把 agentic AI 应用到开发流程上。

## 使用场景

- AI 结对编程（Cursor、Aider、Claude Code、Cline、Continue）
- Code review 自动化
- 测试生成
- Multi-agent coding 任务（规划 + 执行）
- IDE 集成与 CI 规范

## 精选 Projects

> 6 个主流 CLI agent（Claude Code / Codex / OpenCode / Gemini CLI / goose / Aider）的并列比较见 [`resources/cli-agents-guide.zh-CN.md`](../resources/cli-agents-guide.zh-CN.md)。第一次接触 CLI agent 想要 step-by-step 入门 → [`tracks/cli/A1-cli-intro.zh-CN.md`](../tracks/cli/A1-cli-intro.zh-CN.md)（Track A 第一站）。要把 CLI 接到日常工具（GitHub、Linear、Atlassian、Postgres、Playwright、Figma 等）→ [`resources/mcp-skills-catalog.zh-CN.md`](../resources/mcp-skills-catalog.zh-CN.md)（57 个分类整理）。下面只列开发者该知道的关键 entry。

### Coding Agents

#### [Cursor](https://www.cursor.com/) ⭐⭐⭐⭐⭐
编辑器集成的 AI 结对编程工具。AI 辅助 coding 的业界标准。

#### [Aider-AI/aider](https://github.com/Aider-AI/aider) ⭐⭐⭐⭐⭐
★ 44k+ · Apache-2.0 — git-aware 的 CLI pair-programmer。直接编辑你 repo 中的文件，commit 都自动写好。**「git-native AI 编辑流程」的开源模板**。模型不限。

#### [anthropics/claude-code](https://github.com/anthropics/claude-code) ⭐⭐⭐⭐⭐
★ 120k+ — Anthropic 官方的 agentic coding 助理。有 Skills + plugin 生态系。

#### [cline/cline](https://github.com/cline/cline) ⭐⭐⭐⭐⭐
★ 61k+ · Apache-2.0 — VS Code extension，autonomous in-IDE agent：tool use、browser、step-by-step approval。**VS Code 用户想 IDE-native agentic dev 的好选项**。

#### [continuedev/continue](https://github.com/continuedev/continue) ⭐⭐⭐⭐
★ 33k+ · Apache-2.0 — source-controlled AI checks，可以在 CI 强制执行。代表「**团队 / governance**」这条角度的 coding agent。

#### [OpenHands (前身为 OpenDevin)](https://github.com/All-Hands-AI/OpenHands) ⭐⭐⭐⭐
Open source 的自主软件开发 agent。

#### [block/goose](https://github.com/block/goose) ⭐⭐⭐⭐
★ 43k+ · Apache-2.0 — 开源、可扩展的 AI agent，超出纯 code suggestion——能 install / execute / edit / test，搭配任何 LLM。同时支持多家 LLM provider 跟 MCP，提供 desktop app、CLI、API 三种接口。（repo 现指向 `aaif-goose/goose`。）

#### [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) ⭐⭐⭐⭐
★ 23k+ · Apache-2.0 — VS Code 的 coding agent，采用「**多种专业模式**」的设计，跟 Cline 的单一 agent flow 不同。VS Code 用户想 multi-mode 替代方案的选择。

### Code Review

#### [obra/superpowers](https://github.com/obra/superpowers) ⭐⭐⭐⭐
20+ 个经过实战验证的 skill，包括 TDD 模式、debug、协作模式。设计 code-review skill 时的好参考。

## 必练流程

- **AI 结对编程**：日常工作用 Claude Code、Cursor、或 Cline 任意一个
- **Git-native AI 编辑**：用 Aider 跑一周，习惯「AI 编辑 → commit → review」这个节奏
- **CI 上的 AI check**：用 Continue 把 AI 检查接到 PR pipeline
- **测试生成**：写一个 skill / prompt，从 function signature 生成 pytest 测试
- **Code review 自动化**：在每一个 PR 上呼叫 Claude API 的 GitHub Action
