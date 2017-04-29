# coding=utf-8

import sys
from collections import Counter
from collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf-8')

frequencies = defaultdict(int) #传入int()函数来初始化


for k in frequencies:
    print k, frequencies.get(k)
    # print k.decode("utf-8"), frequencies[k]

name_file = open("name.txt", "r")
for line in name_file.readlines():
    for char in line.decode("utf-8"):
        frequencies[char] += 1

sort_dict = sorted(frequencies.iteritems(), key=lambda d: d[1], reverse=True)

for name, time in sort_dict:
    print name.decode("utf-8"), time
# for k in sort_dict:
#     print k, sort_dict.get(k)
