#!/usr/bin/env python
# coding=utf-8
import random


def do_something_unreliable(retry=10):
    for i in range(retry):
        try:
            if random.randint(0, 10) > 1:
                raise IOError("Unstable status, try again")
            else:
                print("Get stable result")
                return
        except Exception as e:
            print(e.message)


if __name__ == "__main__":
    do_something_unreliable(3)