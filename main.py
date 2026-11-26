#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt (UTF-8, 1-200 characters, one line).

Winning line (83 chars, 83 bytes, 1 sentence):
    Synchronized eye-rolling: judged on height, arc, and how loudly the
    teenager sighs.

Tournament (specificity / surprise / freshness, each 1-5):
  1. Synchronized spreadsheet: four accountants, one pivot table, and a
     gold medal for whoever finds the circular reference first. — 4/3/3 = 10
  2. Competitive IKEA assembly: two athletes, one Allen key, and a marriage
     that did not survive the heats. — 4/4/2 = 10
  3. Speed origami: fold a crane in under nine seconds or the judges
     fold you. — 5/4/4 = 13
  4. Extreme ironing on a cliff edge: one crease wrong and the shirt is
     the least of your problems. — 3/3/1 = 7
  5. The 100-metre password reset: sprint to the help desk, answer three
     security questions, and cry in front of a live audience. — 5/5/4 = 14
  6. Competitive queuing: athletes stand in line for four hours; the
     winner is whoever complains the least. — 4/3/3 = 10
  7. Underwater chess: hold your breath, move a pawn, surface, repeat;
     the first to drown loses. — 4/4/3 = 11
  8. Synchronized eye-rolling: judged on height, arc, and how loudly the
     teenager sighs. — 5/5/4 = 14 (WINNER)
  9. The marathon of holding in a sneeze: 42 kilometres, one tickle, zero
     tissues allowed. — 5/5/4 = 14
 10. Competitive Wi-Fi password sharing: shout the password across a
     stadium; first to connect wins, everyone else gets locked out. — 5/4/4 = 13

Tie-break among the three 14s: the eye-rolling line reads most like a
real broadcast event (it carries its own judging criteria: height, arc),
lands its twist on the last word, and wastes nothing at 83 characters.
The password-reset line needs more setup; the sneeze marathon leans on
the 42 km gag every marathon joke already uses.
"""

import argparse
import os
import sys

ENTRY = "Synchronized eye-rolling: judged on height, arc, and how loudly the teenager sighs."

CANDIDATES = [
    ("Synchronized spreadsheet: four accountants, one pivot table, and a gold medal for whoever finds the circular reference first.", 4, 3, 3),
    ("Competitive IKEA assembly: two athletes, one Allen key, and a marriage that did not survive the heats.", 4, 4, 2),
    ("Speed origami: fold a crane in under nine seconds or the judges fold you.", 5, 4, 4),
    ("Extreme ironing on a cliff edge: one crease wrong and the shirt is the least of your problems.", 3, 3, 1),
    ("The 100-metre password reset: sprint to the help desk, answer three security questions, and cry in front of a live audience.", 5, 5, 4),
    ("Competitive queuing: athletes stand in line for four hours; the winner is whoever complains the least.", 4, 3, 3),
    ("Underwater chess: hold your breath, move a pawn, surface, repeat; the first to drown loses.", 4, 4, 3),
    ("Synchronized eye-rolling: judged on height, arc, and how loudly the teenager sighs.", 5, 5, 4),
    ("The marathon of holding in a sneeze: 42 kilometres, one tickle, zero tissues allowed.", 5, 5, 4),
    ("Competitive Wi-Fi password sharing: shout the password across a stadium; first to connect wins, everyone else gets locked out.", 5, 4, 4),
]


def check_entry(text):
    """Gate: UTF-8, 1-200 chars, not only whitespace, single line."""
    if not text or not text.strip():
        return False, "empty or whitespace-only"
    if len(text) > 200:
        return False, f"{len(text)} chars, over the 200 limit"
    if "\n" in text.strip():
        return False, "more than one line"
    return True, "valid"


def write_entry(outdir):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rejected Olympic Sports entry")
    parser.add_argument("--check", action="store_true", help="validate the entry line")
    parser.add_argument("--self-test", action="store_true", help="write twice, compare bytes")
    parser.add_argument("--tournament", action="store_true", help="print the candidate table")
    parser.add_argument("--out", default="/output", help="output directory")
    args = parser.parse_args(argv)

    if args.tournament:
        for i, (line, spec, surp, fresh) in enumerate(CANDIDATES, 1):
            mark = " <-- WINNER" if line == ENTRY else ""
            print(f"{i:2}. {spec}/{surp}/{fresh} = {spec + surp + fresh:2}  {line}{mark}")
        return 0

    if args.check:
        ok, msg = check_entry(ENTRY)
        print(f"chars: {len(ENTRY)}, bytes: {len(ENTRY.encode('utf-8'))}, "
              f"sentences: 1, valid: {ok} ({msg})")
        return 0 if ok else 1

    if args.self_test:
        p1 = write_entry(args.out)
        with open(p1, "rb") as f:
            first = f.read()
        p2 = write_entry(args.out)
        with open(p2, "rb") as f:
            second = f.read()
        print("byte-identical" if first == second else "MISMATCH")
        return 0 if first == second else 1

    path = write_entry(args.out)
    ok, msg = check_entry(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars, valid: {ok} ({msg})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
