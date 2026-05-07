# 给教师 — 专业分支

> [繁體中文](./for-teacher.md) | **简体中文** | [English](./for-teacher.en.md)

> [← 回主路线 README](../README.zh-CN.md) · 走完 **Track A 的 A3** 或 **Track B 的 Stage 7** 后从这里接续。把 agentic AI 应用到教学流程上。

## 使用场景

- 教案生成
- Quiz / 评分量表（rubric）建立
- 幻灯片准备
- 学生反馈整理
- 课程地图

## 精选 Projects

### 教学流程 Skills

（大多数还没有做成 skill marketplace。这个分支最有社群贡献空间——见 CONTRIBUTING.md。）

### 可用的基础组件

#### [obra/superpowers](https://github.com/obra/superpowers) ⭐⭐⭐⭐
通用的写作 / 头脑风暴 skill。可改用在备课上。

#### [Claude Code](https://github.com/anthropics/claude-code)（搭配自定义 CLAUDE.md）⭐⭐⭐⭐⭐
★ 120k+ — 教师很适合先从这里开始。低门槛先用 Claude.ai（网页版）试水温；如果是会重复的流程，再升级到 Claude Code。

### 教学课程素材（给教师备课用）

#### [huggingface/agents-course](https://github.com/huggingface/agents-course) ⭐⭐⭐⭐

| 栏位 | 内容 |
|---|---|
| Stars | ★ 28k+ |
| License | Apache-2.0 |

**教什么**：Hugging Face 官方的 agent 课程——notebook、练习、结业认证。是一份**现成的「AI agent 教学」素材**。

**适合谁**：要在学校 / 工作坊开「AI agent 入门」课程的老师，可以直接拿来当教材或改编。

**备注**：注意这是「教 AI agent 怎么建」的教材，不是「老师用 AI 教书」的工具。

---

#### [datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) ⭐⭐⭐⭐（中文）

| 栏位 | 内容 |
|---|---|
| 语言 | 中文（zh-CN） |
| Stars | ★ 13k+ |
| License | NOASSERTION |

**教什么**：Datawhale 出品的中文 LLM 应用开发课程——含 RAG、agent、章节练习。中文教师备课的现成模板。

**适合谁**：中文教师想找现成可改的 LLM 教材底稿、再针对自己学生程度调整。

**备注**：跟 hf agents-course 一样，是「教学生建 LLM 应用」的教材，不是「教师端的 AI 助教」。

---

### Prompt 素材库

#### [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) ⭐⭐⭐⭐

| 栏位 | 内容 |
|---|---|
| Stars | ★ 161k+ |
| License | NOASSERTION（CC0 / public domain 风格，但未提供 SPDX） |

**教什么**：社群维护的 prompt 大全——「act as X」型模板涵盖几百种角色（老师、面试官、stand-up comedian、辩论者⋯）。教师可以拿来当「prompt engineering 写法示例」教给学生，或直接借用其中合适的当作课堂示范。

**适合谁**：要教学生「prompt engineering」的老师，找现成例子比较不同写法的差异。

**备注**：品质不一致——当作素材库挑选用，不是「全部直接拿去教」。

---

### 阅读材料

#### [The Effortless Academic — Beginner Guides](https://effortlessacademic.com/claude-code-and-cowork-for-academics-beginner-guide-part-1/)
写给学术工作者導入 Claude Code 的多篇指南，教师也适用。

## 可以建的流程

这些是模板——配合你的学科自行调整：

- **教案生成器**：用课纲 + 主题提示 → 大纲 → 幻灯片 → 评估
- **Rubric 建立**：学生作业样本 + 学习目标 → rubric 草稿
- **个性化反馈**：学生作业 + rubric → 个性化文字反馈（要人工把关）

## 给教师的层级建议

大多数教师应该停在 **Tier 0（浏览器聊天）**或 **Tier 1（Claude Desktop）**：

- **Tier 0**：Claude.ai 网页版聊天——复制粘贴 prompt，免安装
- **Tier 1**：Claude Desktop——可上传文件、保留对话历史
- 除非你真的需要自动化，不要直接跳到 CLI / SDK

## 社群备注

这个分支目前是精选内容最少的一块。特别欢迎以下贡献：

- 教案生成 skill
- 学科专属的 prompt library
- 教师专属的 MCP server（成绩册集成、LMS 串接）

请见 [CONTRIBUTING.md](../CONTRIBUTING.md)。
