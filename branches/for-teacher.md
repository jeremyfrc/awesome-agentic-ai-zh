# 給教師 — 專業分支

> **繁體中文** | [简体中文](./for-teacher.zh-CN.md) | [English](./for-teacher.en.md)

> [← 回主路線 README](../README.md) · 走完 **Track A 的 A3** 或 **Track B 的 Stage 7** 後從這裡接續。把 agentic AI 應用到教學流程上。

## 使用情境

- 教案生成
- Quiz / 評分量表（rubric）建立
- 投影片準備
- 學生回饋整理
- 課程地圖

## 精選 Projects

### 教學流程 Skills

（大多數還沒有做成 skill marketplace。這個分支最有社群貢獻空間——見 CONTRIBUTING.md。）

### 可用的基礎元件

#### [obra/superpowers](https://github.com/obra/superpowers) ⭐⭐⭐⭐
通用的寫作 / 腦力激盪 skill。可改用在備課上。

#### [Claude Code](https://github.com/anthropics/claude-code)（搭配自訂 CLAUDE.md）⭐⭐⭐⭐⭐
★ 120k+ — 教師很適合先從這裡開始。低門檻先用 Claude.ai（網頁版）試水溫；如果是會重複的流程，再升級到 Claude Code。

### 教學課程素材（給教師備課用）

#### [huggingface/agents-course](https://github.com/huggingface/agents-course) ⭐⭐⭐⭐

| 欄位 | 內容 |
|---|---|
| Stars | ★ 28k+ |
| License | Apache-2.0 |

**教什麼**：Hugging Face 官方的 agent 課程——notebook、練習、結業認證。是一份**現成的「AI agent 教學」素材**。

**適合誰**：要在學校 / 工作坊開「AI agent 入門」課程的老師，可以直接拿來當教材或改編。

**備註**：注意這是「教 AI agent 怎麼建」的教材，不是「老師用 AI 教書」的工具。

---

#### [datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) ⭐⭐⭐⭐（中文）

| 欄位 | 內容 |
|---|---|
| 語言 | 中文（zh-CN） |
| Stars | ★ 13k+ |
| License | NOASSERTION |

**教什麼**：Datawhale 出品的中文 LLM 應用開發課程——含 RAG、agent、章節練習。中文教師備課的現成模板。

**適合誰**：中文教師要找現成可改的 LLM 教材底稿、再針對自己學生程度調整。

**備註**：跟 hf agents-course 一樣，是「教學生建 LLM 應用」的教材，不是「教師端的 AI 助教」。

---

### Prompt 素材庫

#### [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) ⭐⭐⭐⭐

| 欄位 | 內容 |
|---|---|
| Stars | ★ 161k+ |
| License | NOASSERTION（CC0 / public domain 風格，但未提供 SPDX） |

**教什麼**：社群維護的 prompt 大全——「act as X」型樣板涵蓋幾百種角色（老師、面試官、stand-up comedian、辯論者⋯）。教師可以拿來當「prompt 寫法範例」教給學生，或直接借用其中合適的當作課堂示範。

**適合誰**：要教學生「prompt engineering」的老師，找現成例子比較不同寫法的差異。

**備註**：品質不一致——當作素材庫挑選用，不是「全部直接拿去教」。

---

### 閱讀材料

#### [The Effortless Academic — Beginner Guides](https://effortlessacademic.com/claude-code-and-cowork-for-academics-beginner-guide-part-1/)
寫給學術工作者導入 Claude Code 的多篇指南，教師也適用。

## 可以建的流程

這些是模板——配合你的學科自行調整：

- **教案生成器**：用課綱 + 主題提示 → 大綱 → 投影片 → 評量
- **Rubric 建立**：學生作業樣本 + 學習目標 → rubric 草稿
- **個別化回饋**：學生作業 + rubric → 個別化文字回饋（要人工把關）

## 給教師的層級建議

大多數教師應該停在 **Tier 0（瀏覽器聊天）**或 **Tier 1（Claude Desktop）**：

- **Tier 0**：Claude.ai 網頁版聊天——複製貼上 prompt，免安裝
- **Tier 1**：Claude Desktop——可上傳檔案、保留對話歷史
- 除非你真的需要自動化，不要直接跳到 CLI / SDK

## 社群備註

這個分支目前是精選內容最少的一塊。特別歡迎以下貢獻：

- 教案生成 skill
- 學科專屬的 prompt library
- 教師專屬的 MCP server（成績冊整合、LMS 串接）

請見 [CONTRIBUTING.md](../CONTRIBUTING.md)。
