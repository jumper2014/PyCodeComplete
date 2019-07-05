#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 将xml某些字段删除后转换成json，和目标json做对比
# 将json某些字段删除后转换成xml，和目标xml做比对
# 单独一个目录，目录命名就是接口名称，例如2501
# python xml_json_checker.py -a 2501 -d json2xml
# python xml_json_checker.py -a 2501 -d xml2json


import xml.etree.ElementTree as ET
import xmltodict
import json
import json_tools
import optparse


key_map = {
    "Name2": "name",
    "Sex1": "sex",
    "name1": "name",
}



class XmlJsonChecker(object):
    def __init__(self, api, direction):
        self.in_format, self.out_format = direction.split('2')
        self.ini = "./{0}/{1}/node.ini".format(api, direction)
        # 中间文件，用xml统一存放中间结果
        self.trans = "./{0}/{1}/trans.xml".format(api, direction)
        self.input_file = "./{0}/{1}/input.{2}".format(api, direction, self.in_format)
        self.expected_file = "./{0}/{1}/expected.{2}".format(api, direction, self.out_format)
        self.temp_file = "./{0}/{1}/temp.xml".format(api, direction)
        self.real = None        # 经过转换后得到的实际内容
        self.expected = None    # 期望的内容

    def handle_xml_tree(self, xml_file):
        """
        公用方法，用来将xml文件指定字段删除后转存
        :param xml_file: xml文件名
        :return: None
        """
        f = open(self.ini, 'r')
        lines = f.readlines()

        tree = ET.parse(xml_file)
        root = tree.getroot()

        for line in lines:
            line = line.strip()
            nodes = line.split('/')
            child_node = nodes[-1]
            length = len(child_node)
            father_node = line[: -(length + 1)]
            print("start to handle node:", father_node, child_node)

            for e in root.findall(father_node):
                for el in e.findall(child_node):
                    e.remove(el)
                    print("find key, delete")

        tree.write(self.trans)

    def xml_trans(self):
        """
        将xml做适当处理后转存，用于比对
        :return: None
        """
        self.handle_xml_tree(self.input_file)

    def json_trans(self):
        """
        将json做适当处理后转存，用于比对
        :return:
        """
        json_file = open(self.input_file, 'r')
        json_str = json.load(json_file)
        xml = xmltodict.unparse(json_str, full_document=False)

        f = open(self.temp_file, 'w')
        f.write(xml)
        f.close()

        self.handle_xml_tree(self.temp_file)

    def xml_to_json(self):
        """
        xml转换成json
        :return: None
        """
        f = open(self.trans, 'r')
        xml_str = f.read()

        for k, v in key_map.items():
            xml_str = xml_str.replace('<{0}>'.format(k), "<{0}>".format(v))
            xml_str = xml_str.replace('</{0}>'.format(k), "</{0}>".format(v))

        converted_dict = xmltodict.parse(xml_str)
        self.real = json.dumps(converted_dict, indent=1)
        self.real = json.loads(self.real)
        print(self.real)

    def get_expected(self):
        """
        从文件中加载期望值
        :return: None
        """
        json_file = open(self.expected_file, 'r')
        if self.in_format == "xml":
            self.expected = json.load(json_file)
        else:
            f = open(self.expected_file, 'r')
            xml_str = f.read()

            for k, v in key_map.items():
                xml_str= xml_str.replace('<{0}>'.format(k), "<{0}>".format(v))
                xml_str = xml_str.replace('</{0}>'.format(k), "</{0}>".format(v))

            converted_dict = xmltodict.parse(xml_str)
            self.expected = json.dumps(converted_dict, indent=1)
            self.expected = json.loads(self.expected)
        print(self.expected)

    def verify(self):
        """
        验证实际结果和期望是否一致
        :return: 一致 True, 不一致 False
        """
        if self.in_format == "xml":
            self.xml_trans()
        else:
            self.json_trans()
        self.xml_to_json()
        self.get_expected()
        result = json_tools.diff(self.real, self.expected)
        print(result)
        if len(result) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # 解析命令行参数
    parser = optparse.OptionParser(
        usage="%prog [optons] [<arg1> <arg2> ...]",
        version="1.0"
    )
    parser.add_option('-a', '--api', dest='api',
                      type='string', help='api name')
    parser.add_option('-d', '--direction', dest='direction',
                      type='string', help='xml2json or json2xml')
    (options, args) = parser.parse_args()
    api = options.api
    direction = options.direction
    print("parameters:", api, direction)

    # 初始化，执行比较
    checker = XmlJsonChecker(api, direction)
    print(checker.verify())
