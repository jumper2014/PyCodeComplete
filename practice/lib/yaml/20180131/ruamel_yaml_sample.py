#!/usr/bin/env python
# coding=utf-8

from ruamel import yaml

if __name__ == "__main__":
    with open('father.yml') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)

        # output: <type 'dict'>
        print(type(content))
        print(content)

        content.update({'age': 38})
        print(content)

    with open('ruamel.yml', 'w') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)