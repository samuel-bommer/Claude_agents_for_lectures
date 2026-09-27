#!/usr/bin/env python3
"""
Stop hook: mirror Claude's latest answer to scratch/live.md and a per-session log.
Only fires when the explain skill was invoked in the current turn.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path


def parse_entries(transcript: Path) -> list:
    entries = []
    for line in transcript.read_text(encoding="utf-8").splitlines():
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return entries


def find_anchor(entries: list, last_msg: str) -> int:
    """Return the index of the assistant entry whose text matches last_msg.
    Falls back to the last assistant entry if no exact match found."""
    probe = last_msg[:80].strip()
    fallback = None
    for i in range(len(entries) - 1, -1, -1):
        e = entries[i]
        if e.get("type") != "assistant":
            continue
        for block in e.get("message", {}).get("content", []):
            if block.get("type") == "text":
                if fallback is None:
                    fallback = i
                if probe and probe in block.get("text", ""):
                    return i
    return fallback if fallback is not None else len(entries) - 1


def used_explain_skill(entries: list) -> bool:
    """Walk backwards from the current response looking for explain skill usage.

    Two invocation paths:
    - User typed /explain: <command-name>/explain</command-name> in user str message.
    - Claude called Skill tool programmatically: tool_use block in assistant entry.
    """
    for entry in reversed(entries):
        if entry.get("isSidechain"):
            continue
        if entry.get("type") == "user":
            content = entry.get("message", {}).get("content")
            if isinstance(content, str):
                if "<command-name>/explain</command-name>" in content:
                    return True
                break  # real user message without explain tag
        if entry.get("type") == "assistant":
            for block in entry.get("message", {}).get("content", []):
                if (
                    block.get("type") == "tool_use"
                    and block.get("name") == "Skill"
                    and block.get("input", {}).get("skill") == "explain"
                ):
                    return True
    return False


def main() -> None:
    data = json.load(sys.stdin)

    last_msg = data.get("last_assistant_message", "").strip()
    if not last_msg:
        return

    entries = parse_entries(Path(data["transcript_path"]))

    # Cut off at the current response to avoid the race where the next user
    # message is already appended to the transcript when the hook reads it.
    anchor = find_anchor(entries, last_msg)
    entries = entries[: anchor + 1]

    if not used_explain_skill(entries):
        return

    root = Path(os.environ.get("CLAUDE_PROJECT_DIR", data.get("cwd", ".")))
    scratch = root / "scratch"
    scratch.mkdir(exist_ok=True)

    (scratch / "live.md").write_text(last_msg + "\n", encoding="utf-8")

    session_id = data.get("session_id") or data.get("sessionId", "unknown")
    log = scratch / f"session-{session_id[:8]}.md"
    with log.open("a", encoding="utf-8") as f:
        f.write(f"\n\n---\n## {datetime.now():%H:%M}\n\n{last_msg}\n")


if __name__ == "__main__":
    main()
