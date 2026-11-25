"""One-line entry: roast your fridge.

The entry is a single line roasting the fridge itself — it has one job,
staying cold, and still manages to kill the milk while the ice cream
stays perfect. Written to /output/entry.txt. Deterministic: no
randomness, no network, no clock.
"""

import os

LINE = "My fridge has one job — stay cold — and it still lets the milk die while the ice cream stays perfect."


def main():
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, cap is 200"
    assert LINE.count("\n") == 0, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
