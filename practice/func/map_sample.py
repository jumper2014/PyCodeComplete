#!/usr/bin/env python
# coding=utf-8


if __name__ == "__main__":
    # 单个序列输入
    squares = map(lambda x: x**2, range(10))
    print(squares)

    # 多个序列输入
    full_names = map(lambda x, y: "{0} {1}".format(x, y), ["Zhang", "Li"], ["Yan", "Gang"])
    print(full_names)
