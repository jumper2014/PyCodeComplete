#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import xmltodict
import json
import json_tools


def load_json(xml_path):
    xml_file = open(xml_path, 'r')
    xml_str = xml_file.read()
    json_str = xmltodict.parse(xml_str)
    return json_str


def xml_to_json(xml_path):
    f = open(xml_path)
    xml_str = f.read()
    converted_dict = xmltodict.parse(xml_str)
    json_str = json.dumps(converted_dict, indent=1)
    # print("jsonStr=", json_str)
    return json_str


def json_to_xml(jsonstr):
    """
        demo Python conversion between xml and json
    """
    jsonstr = {"student": {'course': {'name': 'math', 'score': '90'},
                        'info': {'sex': 'male', 'name': 'name'}, 'stid': '10213'}}
    convertedXml = xmltodict.unparse(jsonstr)
    print("convertedXml=", convertedXml)


if __name__ == "__main__":
    json_str = xml_to_json("xml_input.xml")
    json_real = json.loads(json_str)
    print(json_real)
    json_file = open("json_expected.json", 'r')
    json_expected = json.load(json_file)
    print(json_expected)
    result = json_tools.diff(json_real, json_expected)
    print(result)
    # json_to_xml(json_str)