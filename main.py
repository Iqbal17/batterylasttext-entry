"""The Battery's Last Text to Its Charger — make.fun entry.

Brief: one line of plain text, at most 200 characters — the phone battery's
last text message to the charger it waited for all day. A judge model reads
the lines two at a time and keeps the funnier one; the best-ranked lines
take the top 8 places of the pool. The sealed scorer requires
/output/entry.txt to be UTF-8 text of 1-200 characters, not only whitespace.

DECISION RECORD — candidates weighed against the brief:

A. "You said five minutes. I've been at 1% since lunch. This is goodbye."
   REJECTED: flat. It is a status report, not a joke — no twist, no reason
   for a judge to keep it over any other dying-battery line.

B. "I waited all day. You plugged in the toaster, the lamp, everything
   but me. I hope the toaster was worth it."
   REJECTED: the jealousy angle is funny, but the toaster gag distracts
   from the charger relationship, and blaming the charger for neglect
   muddles the voice — the brief is a text TO the charger, and here the
   charger is the villain instead of the one being missed.

C. "It's 1%. I've been 1% since lunch. Tell the brightness I never
   stood a chance."
   REJECTED: nice voice, but two competing jokes (the 1% and the
   brightness) fight each other, and "tell the brightness" is confusing —
   the reader has to work out who is being addressed.

D. CHOSEN — "I waited all day at 1% so he could finish one more video.
   I held on till the end. I died doing what I loved: buffering."
   WINS: dying-words structure fits a last text exactly; the battery's
   sacrifice is the joke (it died serving the owner); "buffering" lands as
   the punchline, turning the thing batteries die doing into the thing the
   battery loved. Short sentences read like a real text message.

WRITING PASSES (genuine revisions to the winning line):

Pass 1: first draft was "I waited all day at 1 percent so he could finish
   one more video. I held on until the very end. I died doing what I
   loved, which was buffering." Tightened for text-message voice: "1
   percent" -> "1%", "until the very end" -> "till the end", and "which
   was buffering" -> ": buffering" — the colon makes the punchline land
   instead of trailing off in a subordinate clause.

Pass 2: considered adding "Tell the charger I loved it." — rejected,
   because the line IS the text to the charger; addressing it in the third
   person broke the voice. Also weighed "one more episode" against "one
   more video" and kept "video": more universal, shorter, and truer to
   what actually drains a phone battery at 1%.
"""

import os

MAX_CHARS = 200

LINE = (
    "I waited all day at 1% so he could finish one more video. "
    "I held on till the end. "
    "I died doing what I loved: buffering."
)


def check_gate(line: str) -> None:
    """Enforce the sealed scorer's gate: 1-200 chars, not only whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def entry_path() -> str:
    """Output path: $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
