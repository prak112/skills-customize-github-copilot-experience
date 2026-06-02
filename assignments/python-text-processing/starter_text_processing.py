import argparse
import collections
import re
from pathlib import Path


WORD_RE = re.compile(r"\b[\w']+\b")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def count_words(text: str):
    words = WORD_RE.findall(text.lower())
    return len(words), len(set(words)), collections.Counter(words)


def top_n(counter: collections.Counter, n: int):
    return counter.most_common(n)


def replace_text(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def main():
    p = argparse.ArgumentParser(description="Starter text processing utilities")
    p.add_argument("file", type=Path)
    p.add_argument("--count", action="store_true", help="Show total and unique word counts")
    p.add_argument("--top", type=int, default=0, help="Show top N most common words")
    p.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="Search and replace text")
    p.add_argument("--out", type=Path, help="Output file for replace operation")
    args = p.parse_args()

    if not args.file.exists():
        print(f"Error: file not found: {args.file}")
        raise SystemExit(1)

    text = read_text(args.file)

    if args.count:
        total, unique, counter = count_words(text)
        print(f"Total words: {total}")
        print(f"Unique words: {unique}")

    if args.top:
        _, _, counter = count_words(text)
        for word, freq in top_n(counter, args.top):
            print(f"{word}: {freq}")

    if args.replace:
        old, new = args.replace
        out_text = replace_text(text, old, new)
        out_path = args.out or args.file.with_name(args.file.stem + "_out" + args.file.suffix)
        out_path.write_text(out_text, encoding="utf-8")
        print(f"Wrote replaced text to {out_path}")


if __name__ == "__main__":
    main()
