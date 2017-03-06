# coding=utf-8

import re

if __name__ == "__main__":

    text = "      42      46     300"
    pattern = "[0-9]+"
    match = re.search(pattern, text, flags=0)
    print match.group()
