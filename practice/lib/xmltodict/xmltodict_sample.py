#!/usr/bin/env python
# coding=utf-8

import xmltodict


if __name__ == '__main__':
    with open('file.xml') as fd:
        doc = xmltodict.parse(fd.read())
        print(doc['mydocument']['@has'])  # == u'an attribute'
        print(doc['mydocument']['and']['many'])  # == [u'elements', u'more elements']
        print(doc['mydocument']['plus']['@a'])  # == u'complex'
        print(doc['mydocument']['plus']['#text'])  # == u'element as well'