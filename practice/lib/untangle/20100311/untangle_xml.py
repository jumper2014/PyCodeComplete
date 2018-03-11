#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 使用untangle解析xml到Python对象

import untangle

if __name__ == '__main__':
    xml_str = '''
        <mydocument has="an attribute">
            <and>
                <many>elements</many>
                <many>more elements</many>
            </and>
            <plus a="complex">elements</plus>
            <plus a="simple">element as well</plus>
        </mydocument>
    '''
    obj = untangle.parse(xml_str)   # 解析字符串形式XML
    print(obj.mydocument['has'])    # 访问属性 an attribute
    print(obj.mydocument.plus[1].cdata)     # 访问文本 element as well
    # print(obj.mydocument.and)       # 报错，无法处理Python关键字


