# MCP / Skills Integration Catalog

> [繁體中文](./mcp-skills-catalog.md) | **English**

> Connect Claude Code (or any other CLI agent) to the apps you already use, without window-hopping. This page is a curated index of 54 MCP servers / Claude Skills / integrations grouped by use case (incl. research-workflow + multi-LLM-delegation dedicated sections).

---

## How to use this catalog

- **Looking for a specific tool's MCP**: jump to the relevant section below
- **Want to know what MCP / Skills / Plugins are**: see [README "Three core terms"](../README.en.md#three-core-terms-mcp--skills--plugins) first, then [Stage 5 — Claude Code Ecosystem](../stages/05-claude-code-ecosystem.en.md)
- **Want 動手練習s (install + test)**: see [Stage 5.2 (MCP)](../stages/05-claude-code-ecosystem.en.md#52--mcp-model-context-protocol-foundation) and [Stage 5.3 (Skills)](../stages/05-claude-code-ecosystem.en.md#53--skills-claude-code-behavior-layer)

### Inclusion criteria

- **Official first**: Anthropic / vendor-published MCP / Skill ranks higher
- **★ 100+ floor**: community repos need 100+ stars; officials get a pass
- **Verifiable**: stars / license fetched live via `gh api`; refreshed quarterly
- **Excluded**: archived, no commit in 12+ months, unclear license + non-official

### Index

1. [Notes / Knowledge Base](#1-notes--knowledge-base) (7)
2. [Office Documents (Word / Excel / PowerPoint / PDF)](#2-office-documents-word--excel--powerpoint--pdf) (6)
3. [Google Workspace](#3-google-workspace) (2)
4. [Microsoft 365](#4-microsoft-365) (3)
5. [Dev Collaboration (GitHub / Atlassian / Slack…)](#5-dev-collaboration-github--atlassian--slack) (6)
6. [Databases](#6-databases) (7)
7. [Browser Automation / Web Scraping](#7-browser-automation--web-scraping) (4)
8. [Design (Figma / Excalidraw)](#8-design-figma--excalidraw) (3)
9. [Monitoring / Observability](#9-monitoring--observability) (3)
10. [Media / Streaming (YouTube / Spotify)](#10-media--streaming-youtube--spotify) (3)
11. [Chinese-language Ecosystem](#11-chinese-language-ecosystem) (1)
12. [Other Common (Cloudflare / Stripe…)](#12-other-common-cloudflare--stripe) (2)
13. [Research Workflow Skills](#13-research-workflow-skills-academic--paper--lit) (4)
14. [Multi-LLM Delegation Skills](#14-multi-llm-delegation-skills) (3)

---

## 1. Notes / Knowledge Base

### [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 4k+ |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐⭐ (**official**) |

**What it does**: Notion's official MCP server — query pages, create pages, manipulate databases.
**Audience**: heavy Notion users for note-taking / project management / wikis — let the LLM pull data and write pages directly.
**Notes**: requires Notion integration token; supports both read-only and read-write modes.

### [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 3.5k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (community, most popular) |

**What it does**: read/write your Obsidian vault via the Obsidian REST API community plugin.
**Audience**: heavy Obsidian users wanting Claude Code to organize daily notes, auto-link, search across files.
**Notes**: requires the [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) plugin in Obsidian.

### [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 6k+ |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ |

**What it does**: a Claude Code Skill that uses browser automation to query NotebookLM, with citation-backed answers.
**Audience**: people who manage papers / research notes in NotebookLM but want to query from Claude Code in one prompt.
**Notes**: requires Google account auth.

### [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 12k+ |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ |

**What it does**: unofficial NotebookLM Python API + CLI + agentic skill; broader feature set than the skill above, including capabilities the web UI doesn't expose.
**Audience**: people doing programmatic / batch operations on NotebookLM (auto-create notebooks, bulk-import documents).
**Notes**: unofficial; may break with Google policy changes — check the issue tracker before relying on it.

### [ergut/mcp-logseq](https://github.com/ergut/mcp-logseq) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 264 |
| License | MIT |
| Rating | ⭐⭐⭐ |

**What it does**: read/write Logseq graph via Logseq's Local HTTP API.
**Audience**: Logseq users automating daily journals, cross-page links, backlink queries.
**Notes**: enable Logseq's HTTP API (Settings → Features → HTTP API).

### [skridlevsky/graphthulhu](https://github.com/skridlevsky/graphthulhu) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 147 |
| License | MIT |
| Rating | ⭐⭐⭐ (covers both Logseq + Obsidian) |

**What it does**: 39 tools across navigation, search, analysis, writing, journals, flashcards, whiteboards.
**Audience**: people using both Logseq and Obsidian who don't want two MCP servers.
**Notes**: community project; broad tool surface but each tool is relatively basic.

### [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 254 |
| License | MIT |
| Rating | ⭐⭐⭐ |

**What it does**: create / query / batch-edit Anki decks via AnkiConnect.
**Audience**: people using Anki for languages / medicine / law — let the LLM auto-generate cards from study material.
**Notes**: requires Anki Desktop + the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon.

---

## 2. Office Documents (Word / Excel / PowerPoint / PDF)

### [anthropics/skills](https://github.com/anthropics/skills) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 129k+ |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐⭐ (**official**, must-install) |

**What it does**: Anthropic's official Agent Skills repo — includes docx / xlsx / pptx / pdf processing skills.
**Audience**: every Claude Code user — `claude skill install` and Claude can read/write Office files directly.
**Notes**: this is a Skills collection, not an MCP; lives in the Stage 5.3 Skills system.

### [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 3.8k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (most popular community Excel MCP) |

**What it does**: Excel file manipulation MCP — read / write / modify cells, formulas, sheets.
**Audience**: people working with Excel reports daily who want LLM-driven data filling and cleanup.
**Notes**: Python-based, depends on openpyxl.

### [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1.7k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐ |

**What it does**: PPT manipulation via python-pptx — create decks, edit slides, insert images, change layouts.
**Audience**: people who want LLMs to auto-generate decks from outlines / Markdown (consultants, lecturers, students).
**Notes**: overlaps with `anthropics/skills`'s pptx skill; use this when the official one isn't enough.

### [SylphxAI/pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 688 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (high-throughput PDF) |

**What it does**: high-speed PDF parsing MCP, ~5-10× faster than `anthropics/skills`'s pdf skill (per their claim).
**Audience**: people doing batch reads of papers / contracts / reports.
**Notes**: parallel processing; noticeable on large PDFs.

### [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 590 |
| License | NOASSERTION |
| Rating | ⭐⭐⭐ (Office skill add-on) |

**What it does**: extends `anthropics/skills` with Office workflows it doesn't cover (automation, advanced formatting).
**Audience**: people who find the official docx/xlsx/pptx skills too coarse-grained.
**Notes**: complements `anthropics/skills`, not a replacement.

### [kreuzberg-dev/kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 8.2k+ |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ |

**What it does**: 97+ document format parser framework, Rust core. Provides MCP server + REST API + CLI.
**Audience**: cross-format batch parsing engineers who care about throughput.
**Notes**: covers obscure formats like HWP, ODT, etc., not just PDF / Office.

---

## 3. Google Workspace

### [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 2.3k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (one server, all of Google) |

**What it does**: Gmail, Calendar, Docs, Sheets, Slides, Drive, Chat, Forms, Tasks, Search — all in one MCP server.
**Audience**: heavy Google Workspace users — replying to email, scheduling, writing docs, manipulating sheets, all from one server.
**Notes**: OAuth setup is a bit involved but only needs to be done once; most complete coverage of Google's tools.

### [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 844 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (Sheets-only) |

**What it does**: focused Google Sheets / Drive integration — create sheets, edit cells, query formulas.
**Audience**: people using only Google Sheets who don't want the full Workspace MCP.
**Notes**: narrower scope than `google_workspace_mcp`, but simpler setup.

---

## 4. Microsoft 365

### [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 681 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (full M365) |

**What it does**: M365 + Office services via Microsoft Graph API — Outlook, Teams, OneDrive, SharePoint.
**Audience**: enterprise M365 users wanting LLM-driven email replies, calendar lookups, OneDrive operations.
**Notes**: requires Azure AD app registration; corporate IT policies may block this.

### [ryaker/outlook-mcp](https://github.com/ryaker/outlook-mcp) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 363 |
| License | NOASSERTION |
| Rating | ⭐⭐⭐ (Outlook only) |

**What it does**: Outlook mail / calendar via Graph API.
**Audience**: people who only need Outlook, not the rest of M365.
**Notes**: narrower scope than `ms-365-mcp-server`.

### [merill/lokka](https://github.com/merill/lokka) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 244 |
| License | MIT |
| Rating | ⭐⭐⭐ |

**What it does**: M365 + Microsoft Graph admin operations — Entra (AD), Intune, etc.
**Audience**: M365 system admins managing tenants / users / policies.
**Notes**: more useful for IT admins than end users.

---

## 5. Dev Collaboration (GitHub / Atlassian / Slack…)

### [github/github-mcp-server](https://github.com/github/github-mcp-server) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 29.5k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (**official**) |

**What it does**: GitHub's official MCP — issues / PRs / repos / Actions / Codespaces.
**Audience**: every GitHub user; once Claude Code is wired up, PR review, issue triage, release notes all work.
**Notes**: **must-install for Track A's A3 動手練習 CLI-9**.

### [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 5.1k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (most popular community Atlassian) |

**What it does**: Confluence + Jira in one MCP, more flexible than the official remote.
**Audience**: people using Atlassian who find the official remote server too restrictive.
**Notes**: pick this OR `atlassian/atlassian-mcp-server` (official) depending on your IT policy.

### [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 650+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐ (**official**) |

**What it does**: Atlassian's official Remote MCP, secure connection to Jira / Confluence.
**Audience**: companies with enterprise Atlassian + IT policies requiring official tooling.
**Notes**: remote model with official SLA.

### [korotovsky/slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1.6k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (no admin permissions needed) |

**What it does**: Slack MCP — DMs, group DMs, channel messages, with built-in history fetch logic.
**Audience**: individual users (not Slack admins) who still want LLM-Slack integration.
**Notes**: doesn't need admin tokens; uses user-level OAuth.

### [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 344 |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ |

**What it does**: Linear (issue tracker) MCP — query issues, create issues, change status.
**Audience**: developers managing sprints / backlogs in Linear.
**Notes**: requires Linear API key.

### [SaseQ/discord-mcp](https://github.com/SaseQ/discord-mcp) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 298 |
| License | MIT |
| Rating | ⭐⭐⭐ |

**What it does**: Discord MCP — read/write channel messages, manage servers.
**Audience**: maintainers running OSS / community Discord servers.
**Notes**: requires Discord bot token; watch rate limits.

---

## 6. Databases

### [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 15k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐⭐ (**Google official**, multi-DB) |

**What it does**: cross-DB MCP server — MySQL / PostgreSQL / Cloud SQL / Spanner / BigQuery.
**Audience**: engineers running databases on Google Cloud, or anyone needing multi-engine support.
**Notes**: open-source + Google-maintained; production-grade choice.

### [bytebase/dbhub](https://github.com/bytebase/dbhub) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 2.7k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (community multi-DB) |

**What it does**: zero-dependency, token-efficient multi-DB MCP — Postgres, MySQL, SQL Server, MariaDB, SQLite.
**Audience**: engineers who don't want the Google Cloud SDK and need cross-OSS-DB support.
**Notes**: overlaps with `googleapis/mcp-toolbox` but lighter weight.

### [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 2.7k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐⭐ (**Supabase official-community**) |

**What it does**: connect Supabase (Postgres, Auth, Storage, Edge Functions) to LLMs.
**Audience**: full-stack devs using Supabase as backend.
**Notes**: official community-maintained.

### [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1.7k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐ (Postgres coding aid) |

**What it does**: MCP server + Claude plugin to help LLMs write better PostgreSQL code.
**Audience**: Postgres-heavy SQL writers / DBAs.
**Notes**: focused on "LLM writes better SQL", not just query execution.

### [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1.6k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (read-only MySQL) |

**What it does**: read-only MySQL MCP — let the LLM see schemas, run queries.
**Audience**: scenarios where the LLM should analyze production DBs but never modify them.
**Notes**: read-only is a safety feature, not a limitation.

### [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐ (**MongoDB official**) |

**What it does**: MongoDB and MongoDB Atlas Cluster MCP server.
**Audience**: engineers using MongoDB / Atlas.
**Notes**: `mongodb-js` is MongoDB's official GitHub org.

### [redis/mcp-redis](https://github.com/redis/mcp-redis) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 504 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (**Redis official**) |

**What it does**: official Redis MCP — natural-language operations on Redis and Redis Stack (Vector / Search / JSON).
**Audience**: people using Redis as cache / vector DB / queue.
**Notes**: officially maintained; includes vector search.

---

## 7. Browser Automation / Web Scraping

### [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 32k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐⭐ (**Microsoft official**) |

**What it does**: Playwright MCP server — let the LLM open browsers, click buttons, fill forms, scrape pages.
**Audience**: anyone doing E2E automation, cross-site integration, scraping behind logins.
**Notes**: official Playwright; most robust. **First choice for Claude Code + web automation**.

### [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 38k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐⭐ (**Chrome official**) |

**What it does**: expose Chrome DevTools to coding agents — performance, network, console traces all available to the LLM.
**Audience**: developers debugging frontend bugs, doing web performance analysis.
**Notes**: pairs perfectly with Playwright MCP — one drives, one observes.

### [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 6.2k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (**Firecrawl official**) |

**What it does**: Firecrawl's official MCP — large-scale web scraping + search + structured extraction.
**Audience**: people scraping large amounts of web data for training / RAG / research.
**Notes**: requires Firecrawl API key (has a free tier).

### [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 3.3k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐ (**Browserbase official**) |

**What it does**: Browserbase's official MCP, paired with Stagehand for cloud-based browser automation.
**Audience**: people whose local browser automation is too heavy / who need parallel cloud sessions.
**Notes**: commercial service (free tier exists); complementary to Playwright MCP (local vs cloud).

---

## 8. Design (Figma / Excalidraw)

### [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 14.6k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (most popular Figma MCP) |

**What it does**: feed Figma layout info to coding agents — read design files, expose component structure, let Cursor / Claude Code generate matching React components.
**Audience**: front-end devs going from Figma designs to component code.
**Notes**: requires Figma access token; must-install for design-to-code workflows.

### [excalidraw/excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 4.3k+ |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐⭐ (**Excalidraw official**) |

**What it does**: streamable Excalidraw MCP — let LLMs draw architecture diagrams and flowcharts directly.
**Audience**: anyone writing design docs / system architecture / flowcharts who wants Claude to draw from text.
**Notes**: official Excalidraw; output imports straight into Excalidraw for editing.

### [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1.9k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (alternative Excalidraw) |

**What it does**: MCP server + Claude Code Skill, real-time canvas sync, create / edit / export.
**Audience**: people who need real-time canvas sync and programmatic operation.
**Notes**: complementary to the official; community-maintained.

---

## 9. Monitoring / Observability

### [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 3k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐⭐ (**Grafana official**) |

**What it does**: Grafana's official MCP — query dashboards / metrics / alerts from the LLM.
**Audience**: SREs / DevOps using Grafana for metrics.
**Notes**: "why did this dashboard line drop?" — ask, and the LLM pulls metrics for the answer.

### [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 677 |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ (**Sentry official**) |

**What it does**: query Sentry error events / issues / traces from LLMs.
**Audience**: engineers using Sentry for production errors.
**Notes**: "show me last week's stack trace for this error" works directly in Claude Code.

### [winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 142 |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐ (community Datadog) |

**What it does**: Datadog API MCP — monitors / logs / metrics.
**Audience**: Datadog users while there's no official Datadog MCP yet.
**Notes**: likely to be replaced once Datadog ships an official MCP.

---

## 10. Media / Streaming (YouTube / Spotify)

### [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 599 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ |

**What it does**: connect LLMs to Spotify — play tracks, manage playlists, query history.
**Audience**: anyone integrating playback control or text → music workflows with Claude Code.
**Notes**: requires Spotify Premium (API restriction).

### [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 534 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (YouTube transcripts) |

**What it does**: pull YouTube video transcripts into the LLM for summary / translation / RAG.
**Audience**: people using video as study material, batch-summarizing YouTube content.
**Notes**: depends on YouTube auto-captions; non-English transcripts are hit-or-miss.

### [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 510 |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ (full YouTube API) |

**What it does**: full YouTube API MCP — beyond transcripts, also video management, Shorts, analytics.
**Audience**: YouTube creators automating channel management.
**Notes**: requires YouTube Data API key + OAuth.

---

## 11. Chinese-language Ecosystem

### [leemysw/feishu-docx](https://github.com/leemysw/feishu-docx) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 193 |
| License | MIT |
| Rating | ⭐⭐⭐ |

**What it does**: bidirectional Feishu (Lark) docs / sheet / bitable ↔ Markdown, with OAuth 2.0, CLI, TUI, Claude Skills.
**Audience**: Chinese-language users on Feishu / Lark wanting to bridge Lark content with Claude Code.
**Notes**: currently one of the few MCP / Skill options in the Chinese ecosystem; WeChat / DingTalk don't have standalone MCPs yet (they live inside chatbot frameworks).

> Looking for WeChat / DingTalk integrations? Today the mainstream is chatbot frameworks (e.g., zhayujie/CowAgent), not pure MCP servers. Will add when proper MCPs emerge.

---

## 12. Other Common (Cloudflare / Stripe…)

### [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 3.7k+ |
| License | Apache-2.0 |
| Rating | ⭐⭐⭐⭐⭐ (**Cloudflare official**) |

**What it does**: Cloudflare's official MCP — Workers, Pages, R2, KV, D1, DNS, Zero Trust.
**Audience**: anyone running edge / serverless on Cloudflare.
**Notes**: officially maintained; the best edge platform MCP.

### [stripe/ai](https://github.com/stripe/ai) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 1.5k+ |
| License | MIT |
| Rating | ⭐⭐⭐⭐ (**Stripe official**) |

**What it does**: Stripe's official AI agent toolkit, includes an MCP server — handle payments, subscriptions, refunds, customers.
**Audience**: developers wiring payment / billing into agent flows.
**Notes**: ⚠️ this is real money. Test thoroughly in sandbox before going to production.

---

## 13. Research Workflow Skills (academic / paper / lit)

> ⚠️ **Maintainer's own projects**: the following are skills the repo maintainer [@WenyuChiou](https://github.com/WenyuChiou) (Lehigh CEE PhD candidate) uses daily for research and open-sourced for other researchers. **Star counts are lower than general-purpose tools** because these are niche / research-specific. The ★ 100+ inclusion floor is relaxed in this section — the only criterion here is "actually useful in the maintainer's research workflow". Evaluate fit yourself.

### [WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 47 |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ (full research workflow) |

**What it does**: 14 Claude Code skills covering common research tasks — literature triage, research design, project context, manuscript writing, multi-AI delegation. Packaged as a 5-plugin marketplace, install with one command.
**Audience**: grad students / postdocs wanting a complete "research workflow" skill set in one drop.
**Notes**: marketplace format, aligns with the plugin/marketplace concept taught in Stage 5.4.

### [WenyuChiou/academic-writing-skills](https://github.com/WenyuChiou/academic-writing-skills) ⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 2 |
| License | MIT |
| Rating | ⭐⭐⭐ (narrow but deep) |

**What it does**: rigorous academic paper writing / revision / submission skill for Claude Code. Field-agnostic, customizable per-paper via journal_format.md and style_overrides.md.
**Audience**: researchers actively writing / revising papers who want to automate banned-word audit, figure-text coupling, submission checklists.
**Notes**: one of the 5 plugins inside ai-research-skills; can also be installed standalone.

### [WenyuChiou/zotero-skills](https://github.com/WenyuChiou/zotero-skills) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 16 |
| License | NOASSERTION |
| Rating | ⭐⭐⭐⭐ |

**What it does**: Zotero CLI skill — programmatically search, add, classify, annotate references.
**Audience**: Zotero users wanting Claude Code to organize their library directly.
**Notes**: complementary to [`MuiseDestiny/zotero-gpt`](https://github.com/MuiseDestiny/zotero-gpt) — that one is a Zotero plugin (chat inside Zotero), this one is a CLI / Skill (operate Zotero from Claude Code).

### [WenyuChiou/research-hub](https://github.com/WenyuChiou/research-hub) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 14 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ |

**What it does**: AI-operable research workspace bridging Zotero + Obsidian + NotebookLM, with CLI / MCP / REST / dashboard interfaces.
**Audience**: researchers using Zotero / Obsidian / NotebookLM together, wanting to bind them into one workspace for LLMs to operate.
**Notes**: complementary to single-tool MCPs (mcp-obsidian, notion-mcp, etc.) — this is a hub that integrates multiple tools.

---

## 14. Multi-LLM Delegation Skills

> ⚠️ **Maintainer's own projects** (same as §13): delegation skills the maintainer extracted from daily workflow. Star floor is relaxed; criterion is "the Claude-planner + Codex/Gemini-executor combo runs reliably". Multi-LLM space evolves quickly — evaluate alongside the multi-agent frameworks listed in Stage 7 before adopting.

### [WenyuChiou/codex-delegate](https://github.com/WenyuChiou/codex-delegate) ⭐⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 57 |
| License | MIT |
| Rating | ⭐⭐⭐⭐⭐ |

**What it does**: Claude Code skill for using Codex CLI as an execution specialist — multi-file refactors, boilerplate generation, implementation-heavy tasks. Claude plans + reviews; Codex executes.
**Audience**: developers who want to delegate implementation work from Claude Code to Codex automatically.
**Notes**: pairs with `gemini-delegate-skill` (one for code-heavy, one for long-form / CJK). A practical implementation of the Stage 7 multi-agent concept.

### [WenyuChiou/gemini-delegate-skill](https://github.com/WenyuChiou/gemini-delegate-skill) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 34 |
| License | MIT |
| Rating | ⭐⭐⭐⭐ |

**What it does**: Claude Code skill for using Gemini CLI for large-context synthesis, English / zh-TW / CJK long-form drafting, and second-opinion review.
**Audience**: people writing long form, doing cross-language drafts, or needing a second-opinion review — researchers writing papers / Chinese reports especially.
**Notes**: complements codex-delegate — "Codex for code, Gemini for prose" division of labor.

### [WenyuChiou/agent-collab-skills](https://github.com/WenyuChiou/agent-collab-skills) ⭐⭐

| Field | Value |
|---|---|
| Stars | recently published, no stars yet |
| License | MIT |
| Rating | ⭐⭐ (experimental — treat as reference) |

**What it does**: Claude Code marketplace for multi-agent collaboration — task splitter, output reconciler, adversarial debate, shared memory, acceptance gate. Composes with codex-delegate / gemini-delegate.
**Audience**: people running 2+ delegate agents per round who want to see one way of packaging multi-agent coordination into a marketplace.
**Notes**: **experimental** — don't treat this as a production-grade framework. It's the maintainer's own setup made public as a reference. For production-grade multi-agent, see LangGraph / AutoGen / CrewAI in Stage 7.

---

## What's not here?

If your integration isn't above, check these catalogs first:

- [`wong2/awesome-mcp-servers`](https://github.com/wong2/awesome-mcp-servers) — most complete community MCP server catalog, 150+ entries by category
- [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) — another MCP server catalog, complementary
- [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) — Anthropic's official reference servers (filesystem, git, time, memory, fetch, sequential-thinking, …)
- [`travisvn/awesome-claude-skills`](https://github.com/travisvn/awesome-claude-skills) — Claude Skills catalog

### Want to add something?

1. Open an issue with the repo link, why it should be added, and which category it fits.
2. Or PR directly: add an entry under the relevant category in this format (Stars / License / Rating + What it does / Audience / Notes).
3. **Stars < 100 + non-official** typically gets rejected unless you can argue a strong niche use case.

Read [`resources/style-guide.md`](style-guide.en.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md) before submitting.

---

## Maintainer notes (for future maintainers)

- Pull stars / license via `gh api repos/<owner>/<repo>` quarterly
- Drop entries with broken links / archived repos
- Open new categories (AR/VR, IoT, etc.) only when stars-by-coverage justifies it; below 1k stars + < 3 entries, hold off
- "Chinese-language ecosystem" stays loose (Chinese-community repos collect stars more slowly)
