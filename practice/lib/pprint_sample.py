#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    import pprint

    data = (
        "this is a string",
        [1, 2, 3, 4, {"name": "python", "age": 30}],
        ("more tuples", 1.0, 2.3, 4.5),
        "this is yet another string"
    )

    pprint.pprint(data, indent=4, width=20, depth=2)