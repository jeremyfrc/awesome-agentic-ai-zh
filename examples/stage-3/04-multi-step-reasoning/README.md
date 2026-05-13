> **繁體中文** | [简体中文](./README.zh-Hans.md) | [English](./README.en.md)

# 練習 4：多步驟推理任務

這個練習把練習 3 的 ReAct loop 延伸成 3 到 5 步的任務。題目是「查出台北人口、查出紐約人口、相除、轉成百分比」。LLM 負責規劃下一步，工具只負責可靠地執行小動作；兩者合在一起，才像一個能完成工作流的 agent。

## 執行方式

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python starter.py
python test.py
```

`starter.py` 提供四個工具：`lookup_population(city)`、`divide(a, b)`、`to_percentage(ratio)`、`round_int(x)`。`react_loop` 每輪把目前 messages、tools 送給 Claude，收到 `tool_use` 就執行本地函式，再用 `tool_result` 把 observation 放回對話。收到 `end_turn` 或沒有工具呼叫時才停止。

## 測試重點

`test.py` 用 mock 固定五輪回應：四輪工具呼叫加一輪最終回答。測試會檢查工具順序必須是人口、人口、相除、百分比，並確認最後答案包含 31%。另一個測試故意讓分母為 0，要求 `divide` 回傳安全的 `0`，讓 loop 能繼續到百分比與最終回答，而不是因 exception 中斷。

## 觀念提醒

多步任務的核心不是「模型很會算」，而是把複雜任務拆成可靠的小步。工具應該保持窄而穩定；LLM 則負責決定下一步與何時結束。`max_iter=8` 是必要的安全網，避免模型一直要求工具而沒有停下來。
