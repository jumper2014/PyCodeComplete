# -*- coding:utf-8 -*-
# robot framework库关键字数量

import os
import os.path

# 关键字字典，关键字和出现的次数
keyword_dict = {}

rootdir = "/Users/yuetian/robotframework/search-it-automation/testcase/" # 指明被遍历的文件夹
keyword_num = 0
file_list = []


def handle_file(file_name):
    for line in open(file_name):
        line = line.strip()  # 去除两端空格
        words_list = line.split("  ")
        #print(words_list)
        for word in words_list:
            if not keyword_dict.has_key(word):
                keyword_dict[word] = 1
            else:
                keyword_dict[word] += 1


def get_file_list(rootdir):
    for parent,dirnames,filenames in os.walk(rootdir):
        # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # for dirname in dirnames: #输出文件夹信息
            # print "parent is:" + parent
            # print "dirname is" + dirname
        for filename in filenames: # 输出文件信息
            # print "parent is" + parent
            # print "filename is:" + filename
            # print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            file_name = os.path.join(parent, filename)
            # print file_name
            file_list.append(file_name)



if __name__ == "__main__":
    # handle_file("/Users/yuetian/robotframework/search-it-automation/Library/resource/keywords/validate_records.txt")
    get_file_list("/Users/yuetian/robotframework/search-it-automation/testcase")
    get_file_list("/Users/yuetian/robotframework/search-it-automation/indexCase")
    get_file_list("/Users/yuetian/robotframework/search-it-automation/Library/resource")

    for file_name in file_list:
        handle_file(file_name)

    keyword_list = sorted(keyword_dict.iteritems(), key=lambda asd: asd[1], reverse=True)
    for word_list in keyword_list[0: 4000]:
        word = word_list[0]
        word = word.strip()
        if word.find(" ") < 0:
            continue
        # print word
        # continue
        if len(word) <= 7 \
                or word[0] == '$' \
                or word[0] == "*" \
                or word[0] == "[" \
                or word[0] == ":" \
                or word[0].islower() \
                or word[0] == "/" \
                or word[0] == "'" \
                or word[0] == " " \
                or word[0] == "#" \
                or ord(word[0]) > 256 \
                or word.find("TEST FAIL,") == 0:
            pass
        else:
            keyword_num += 1
            print word_list
    print "Total Keyword number is: ", keyword_num



