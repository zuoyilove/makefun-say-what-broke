#!/usr/bin/env python3
"""One line of software error copy: the brutal truth, and a laugh.

Writes the line to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single line.
"""

LINE = (
    "Good news: the database is fine. Bad news: your query asked for every "
    "row since 2019, and it is still reading. Ask for less, like the rest "
    "of us."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
