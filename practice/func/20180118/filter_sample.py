#!/usr/bin/env python
# coding=utf-8


if __name__ == "__main__":
    adult_ages = filter(lambda x: x >= 18, range(1, 100))
    print(adult_ages)