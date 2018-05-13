#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    import json
    your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    parsed = json.loads(your_json)
    print(type(parsed))
    print(json.dumps(parsed, indent=4, sort_keys=True))

    import pprint

    text = pprint.pformat(parsed, indent=4)
    print(text)
