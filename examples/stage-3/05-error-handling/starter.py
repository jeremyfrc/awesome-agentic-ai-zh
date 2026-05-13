"""Stage 3 Exercise 5: return tool errors without crashing the loop."""

from __future__ import annotations

import json
import os
import sys
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import anthropic

MODEL = os.environ.get("MODEL", "claude-haiku-4-5")
_failure_plan: list[bool] = [True, False]


def set_weather_failures(plan: list[bool]) -> None:
    global _failure_plan
    _failure_plan = list(plan)


def fetch_weather(city: str) -> dict:
    should_fail = _failure_plan.pop(0) if _failure_plan else False
    if should_fail:
        return {"error": "network timeout", "retry_hint": "try again in 1s"}
    return {"city": city, "forecast": "rain", "temperature_c": 24}


TOOLS_SPEC = [
    {
        "name": "fetch_weather",
        "description": "Fetch current weather. If an error is returned, inspect retry_hint before retrying.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name"}},
            "required": ["city"],
        },
    }
]


def react_loop(question: str, max_iter: int = 5, client: Any = None) -> dict:
    client = client or anthropic.Anthropic()
    messages = [{"role": "user", "content": question}]
    trace: list[dict] = []
    for step in range(max_iter):
        resp = client.messages.create(model=MODEL, max_tokens=1024, tools=TOOLS_SPEC, messages=messages)
        text = " ".join(getattr(b, "text", "") for b in resp.content if getattr(b, "type", None) == "text")
        calls = [b for b in resp.content if getattr(b, "type", None) == "tool_use"]
        messages.append({"role": "assistant", "content": resp.content})
        if resp.stop_reason == "end_turn" or not calls:
            trace.append({"step": step, "thought": text, "tool": None, "obs": None})
            return {"final": text, "trace": trace, "steps": step + 1}
        results = []
        for call in calls:
            args = dict(call.input)
            obs = fetch_weather(args["city"]) if call.name == "fetch_weather" else {"error": "unknown tool"}
            results.append({"type": "tool_result", "tool_use_id": call.id, "content": json.dumps(obs, ensure_ascii=False)})
            trace.append({"step": step, "thought": text, "tool": call.name, "tool_input": args, "obs": obs})
        messages.append({"role": "user", "content": results})
    return {"final": None, "trace": trace, "steps": max_iter, "truncated": True}


if __name__ == "__main__":
    set_weather_failures([True, False])
    result = react_loop("Will it rain in Taipei today?")
    print(result)

    # === 自我檢查 ===
    assert result["trace"][0]["obs"]["error"] == "network timeout"
    assert result["trace"][1]["obs"]["forecast"] == "rain"
    assert result["final"] is not None
    print("Stage 3 exercise 5 starter check passed")
