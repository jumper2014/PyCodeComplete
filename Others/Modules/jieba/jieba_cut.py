#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import jieba
import pkuseg

if __name__ == '__main__':
    text = "绿子在电话的另一头久久默然不语，如同全世界的细雨落在全世界所有的草坪上一般的沉默在持续。"
    seg_list = jieba.cut(text,  cut_all=False, HMM=True)
    print("Cut result is: " + "/".join(seg_list))

    seg = pkuseg.pkuseg()  # 以默认配置加载模型
    text = seg.cut(text)  # 进行分词
    print("Cut result is: " + "/".join(text))