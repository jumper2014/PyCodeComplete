# coding=utf-8

import os

if not os.path.exists("new_file.txt"):
    with open("new_file.txt", "wt") as fil:
        fil.write("hello")
else:
    print("file already exists")
