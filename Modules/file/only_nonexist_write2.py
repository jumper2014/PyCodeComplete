# coding=utf-8
# "xt" only works for python3

try:
    with open("new_file.txt", "xt") as fil:
        fil.write("hello2")
except Exception as e:
    print("file already exists")