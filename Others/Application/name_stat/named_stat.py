# coding=utf-8

import sys
from collections import Counter
from collections import defaultdict
import itertools

reload(sys)
sys.setdefaultencoding('utf-8')

frequencies = defaultdict(int) # 传入int()函数来初始化


for k in frequencies:
    print k, frequencies.get(k)

    # print k.decode("utf-8"), frequencies[k]

name_file = open("/Users/zyt/git/PyCodeComplete/Others/Application/name_stat/name.txt", "r")
for line in name_file.readlines():
    for char in line.decode("utf-8"):
        frequencies[char] += 1

sort_dict = sorted(frequencies.iteritems(), key=lambda d: d[1], reverse=True)

char_list = list()


for name, time in sort_dict:

    print name.decode("utf-8"), time
    if name in [u"方", u"中", u"华", u"顾", u"问",
                u"管", u"东", u"企", u"一", u"国",
                u"咨", u"询", u"零", u"医", u"南",
                u"航", u"事", u"西"]:

        continue

    if 100 > time > 0 :
        char_list.append(name)

# for k in sort_dict:
#     print k, sort_dict.get(k)

j = u"匡"



for i in char_list:
    # for j in char_list:
        print "{0}{1}".format(i.decode("utf-8"), j.decode("utf-8")),"{0}{1}".format(j.decode("utf-8"), i.decode("utf-8"))

# 上海XX企业管理咨询有限公司
# 明美,明策,明慧,明莱,明创,明睿
# 君弛,君融
# 和硕
# 维德,德铭
# 铭智