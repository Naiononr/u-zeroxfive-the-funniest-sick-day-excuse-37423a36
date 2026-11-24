#!/usr/bin/env python3
"""Write the sick-day excuse line to /output/entry.txt.

Standard library only, deterministic: the line is a fixed string.
Honours MAKEFUN_OUTPUT_DIR (default /output). Writes via a temp file
in the same directory, chmod 0644, then os.replace -- no trailing newline.
"""

import os

LINE = (
    "My back went out this morning \u2014 my mattress folded me in half "
    "and kept the receipt. Can't sit up, let alone sit through standup."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
