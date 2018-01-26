#!/usr/bin/env python
import random
import time

def consumer_time():
    duration = random.randint(0, 200)
    for i in range(duration):
        time.sleep(0.01)
        for j in range(duration):
            x = 100.94 * 238.487*random.randint(0, 10)


if __name__ == "__main__":
    consumer_time()