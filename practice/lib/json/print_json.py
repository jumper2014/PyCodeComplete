#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    import json
    your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    # 转换成Python对象
    parsed = json.loads(your_json)
    # 序列化成JSON并且打印
    print(json.dumps(parsed))
    """
    ["foo", {"bar": ["baz", null, 1.0, 2]}]
    """
    print(json.dumps(parsed, indent=4, sort_keys=True))
    """
    [
        "foo",
        {
            "bar": [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
    """
