#!/usr/bin/env python3
"""Dad Joke Showdown - write one dad joke to /output/entry.txt.

The joke is a single line, written to be told out loud at the dinner
table: a dad tells his kids the calendar's days are numbered, and his
son answers with the literal truth. The pun is "days are numbered"
(doomed, finished vs. literally numbered on a calendar); the punchline
lands at the end, in the son's deadpan reply.
"""

import os
import sys

JOKE = (
    "I told my kids the calendar's days are numbered. "
    "My son said, 'Dad, that's literally what a calendar is.'"
)

MAX_CHARS = 200


def render(text):
    """One line plus a single trailing newline, no stray whitespace."""
    return text.rstrip() + "\n"


def check_joke(text):
    """The gate: UTF-8 text, 1-200 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("joke is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "joke is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")
    return text


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def main():
    joke = check_joke(JOKE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(render(joke))
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == render(joke), "written entry does not match the joke"
    print("wrote %d characters to %s" % (len(joke), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
