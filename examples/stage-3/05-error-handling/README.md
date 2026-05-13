> **繁體中文** | [简体中文](./README.zh-Hans.md) | [English](./README.en.md)

# 練習 5：錯誤處理

真實 agent 很少只遇到成功路徑。API 會 timeout、參數可能錯、第三方服務也可能暫時不可用。這個練習故意讓 `fetch_weather(city)` 第一次回傳錯誤，第二次才成功，觀察 ReAct loop 如何把錯誤 observation 交回 Claude，讓模型決定要 retry、改 query，或放棄。

## 執行方式

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python starter.py
python test.py
```

`starter.py` 裡的 `fetch_weather` 會回傳 dict。失敗時格式是 `{"error": "network timeout", "retry_hint": "try again in 1s"}`；成功時回傳城市、天氣與溫度。`react_loop` 不會把錯誤當成 Python exception，而是把 JSON observation 放進 `tool_result`，讓下一輪 LLM 看見。

## 測試重點

`test.py` 先測 failure plan：第一次失敗、第二次成功。接著 mock 三輪 Anthropic response：工具呼叫、retry 工具呼叫、`end_turn`。最後還有一個連續失敗案例，確認 loop 能把兩次錯誤都記在 trace，並讓模型用文字回答「稍後再試」，而不是 crash。

## 設計提醒

錯誤也應該是結構化資料。只回傳 `"failed"` 會讓模型不知道下一步；加入 `retry_hint`、錯誤類型與可恢復建議，模型才有足夠 context 做決策。retry 次數也要有限制，否則 agent 會在壞掉的工具前面無限打轉。
