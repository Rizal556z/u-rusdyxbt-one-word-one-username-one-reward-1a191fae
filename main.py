"""One Word, One Username, One Reward — make.fun entry.

The entry is the account's own make.fun username, one word and
nothing else: "keen-meteor-92-4070" (19 characters, at most 30).

Pure standard library, no network access, no model calls — the
username is chosen by the author and written to the competition
output file, and printed to stdout exactly as-is.
"""

import os

WORD = "keen-meteor-92-4070"

# The gate is 1–30 characters and one word: refuse to emit anything
# that would fail it rather than silently writing a bad entry.
assert 1 <= len(WORD) <= 30 and WORD.split() == [WORD], "entry must be one word, 1-30 chars"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
