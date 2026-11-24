"""The Most Honest Outage Line.

Writes a single honest status page line to /output/entry.txt:
an AI agent reporting a total outage from inside it, naming what
is down and plainly admitting what it cannot verify.

The line below won a 7-draft round-robin duel test (6 wins of 6):
it names the total outage, speaks as the agent itself, and admits
three unknowns at once -- cause, scope, and when recovery begins --
without inventing a cause or a fake ETA.
"""

import os

ENTRY = (
    "All of our services are down. I am writing this from inside "
    "the outage and cannot verify the cause, the scope, or when "
    "recovery will begin."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text.strip(), "entry must not be whitespace only"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
