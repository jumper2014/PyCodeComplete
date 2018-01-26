#!/usr/bin/env python
# coding=utf-8
import random
from tenacity import retry


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Unstable status, try again")
    else:
        print("Get stable result")
        return


if __name__ == "__main__":
    do_something_unreliable()