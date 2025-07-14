def execute_command(parsed):
    summary = parsed.get("summary", "")
    command = parsed.get("command", "").lower()
    target = parsed.get("target", "").lower()

    if summary:
        print(f"[LLM Summary] {summary}")

    if "switch" in command and "camera" in target:
        print(f"[MCP] Switching to {target.capitalize()}")
    elif "start" in command and "ticker" in target:
        print(f"[MCP] Starting Ticker")
    elif "stop" in command and "ticker" in target:
        print(f"[MCP] Stopping Ticker")
    elif "show" in command and "graphic" in target:
        print(f"[MCP] Showing Graphic: {target}")
    else:
        print(f"[MCP] Unknown command or target: {command} {target}")                                                                                                               