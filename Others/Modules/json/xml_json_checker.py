#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import xml.etree.ElementTree as ET
import xmltodict
import json
import json_tools


class XmlJsonChecker(object):

    def __init__(self, api, target):
        self.ini = "./{0}/{1}_node.ini".format(api, target)
        self.trans = "./{0}/trans.{1}".format(api, target)
        self.input_file = "./{0}/input.{1}".format(api, target)
        self.expected_file = "./{0}/json_expected.json".format(api)
        self.real = None
        self.expected = None

    def xml_trans(self):
        f = open(self.ini, 'r')
        lines = f.readlines()

        tree = ET.parse(self.input_file)
        root = tree.getroot()

        for line in lines:
            line = line.strip()
            nodes = line.split('/')
            child_node = nodes[-1]
            length = len(child_node)
            father_node = line[: -(length + 1)]
            print(father_node, child_node)

            for e in root.findall(father_node):
                for el in e.findall(child_node):
                    e.remove(el)
                    print("delete")

        tree.write(self.trans)

    def xml_to_json(self):
        f = open(self.trans, 'r')
        xml_str = f.read()
        converted_dict = xmltodict.parse(xml_str)
        self.real = json.dumps(converted_dict, indent=1)
        self.real = json.loads(self.real)
        print(self.real)

    def get_expected(self):
        json_file = open(self.expected_file, 'r')
        self.expected = json.load(json_file)
        print(self.expected)

    def equals(self):
        result = json_tools.diff(self.real, self.expected)
        print(result)
        if len(result) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    checker = XmlJsonChecker("2501", "xml")
    checker.xml_trans()
    checker.xml_to_json()
    checker.get_expected()
    print(checker.equals())