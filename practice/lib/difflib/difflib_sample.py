#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import difflib

if __name__ == '__main__':
    text1 = """Python is 30 years old.
    Many people love it.
    You should learn it now."""
    text1_lines = text1.splitlines()

    text2 = """Python is 31 years old.
    Many people loves it.
    We all should learn it now.
    Just do it."""
    text2_lines = text2.splitlines()

    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    print('\n'.join(diff))

    """
- Python is 30 years old.
?            ^

+ Python is 31 years old.
?            ^

-     Many people love it.
+     Many people loves it.
?                     +

-     You should learn it now.
?     ^^^

+     We all should learn it now.
?     ^^^^^^

+     Just do it.
    """