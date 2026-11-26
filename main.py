# SPDX-License-Identifier: MIT
"""Rejected Olympic Sports — writes the winning one-liner to /output/entry.txt.

The line names a made-up event that sounds broadcast-plausible, then lands
its twist twice: Canada sweeps the podium at Competitive Apologising, then
apologises for sweeping it. One literal, so the output bytes never vary.
"""
import os

LINE = "Competitive Apologising was rejected after Canada swept the podium, then apologised for sweeping the podium."


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly here rather than
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be white space only"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        with open(target, "w", encoding="utf-8", newline="") as fh:
            fh.write(LINE)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        with open(os.path.join(fallback, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
            fh.write(LINE)


if __name__ == "__main__":
    main()
