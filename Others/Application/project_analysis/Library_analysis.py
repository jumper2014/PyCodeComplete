# -*- coding:utf-8 -*-
__author__ = 'yuetian'

import os
import os.path

# 关键字字典，关键字和出现的次数
keyword_dict = {}

file_list = []
function_num = 0

def handle_file(file_name):
    global  function_num
    for line in open(file_name):
        line = line.strip()  # 去除两端空格
        if line.find("Library  ") >=0:
            print line
            function_num = function_num + 1

def get_file_list(rootdir):

    for parent,dirnames,filenames in os.walk(rootdir): #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #for dirname in dirnames: #输出文件夹信息
            #print "parent is:" + parent
            #print "dirname is" + dirname
        for filename in filenames: #输出文件信息
            #print "parent is" + parent
            #print "filename is:" + filename
            #print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            if filename.find(".txt") >= 0:
                file_name = os.path.join(parent, filename)
                #print file_name

                file_list.append(file_name)



if __name__ == "__main__":
    #handle_file("/Users/yuetian/robotframework/search-it-automation/Library/resource/keywords/validate_records.txt")

    get_file_list("/Users/yuetian/robotframework/search-it-automation/Library/resource")


    for file_name in file_list:
        handle_file(file_name)

    print "Total function number is: ", function_num



