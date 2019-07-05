#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import jieba

if __name__ == '__main__':
    seg_list = jieba.cut("绿子在电话的另一头久久默然不语，如同全世界的细雨落在全世界所有的草坪上一般的沉默在持续。",
                         cut_all=False, HMM=True)
    print("Cut result is: " + "/".join(seg_list))

    import pkuseg

    seg = pkuseg.pkuseg()  # 以默认配置加载模型
    text = seg.cut('"绿子在电话的另一头久久默然不语，如同全世界的细雨落在全世界所有的草坪上一般的沉默在持续。')  # 进行分词
    print(text)