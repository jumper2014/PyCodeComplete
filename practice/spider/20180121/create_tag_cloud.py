#!/usr/bin/env python
# coding=utf-8

# -*- coding: utf-8 -*-
import codecs
import random
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts

wd = dict()
fp = codecs.open("rsa.txt", "r", 'utf-8')
lines = fp.readlines()
fp.close()

for line in lines:
    word = line.split(' ')
    print word
    wd[word[0]] = int(float(word[1]) * 100000)
print wd

from operator import itemgetter

swd = sorted(wd.iteritems(), key = itemgetter(1), reverse=True)
tags = make_tags(swd, minsize=50, maxsize=240, colors=random.choice(COLOR_SCHEMES.values()))
create_tag_image(tags, 'keyword_tag_cloud4.png', background=(0, 0, 0, 255), size=(2400, 1000), layout=LAYOUT_HORIZONTAL,
                 fontname="SimHei")
