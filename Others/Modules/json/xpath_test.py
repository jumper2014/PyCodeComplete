#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import xml.etree.ElementTree as ET

f = open('keys.ini', 'r')
lines = f.readlines()

tree = ET.parse('xml_input.xml')
root = tree.getroot()

for line in lines:
    line = line.strip()
    nodes = line.split('/')
    child_node = nodes[-1]
    length = len(child_node)
    father_node = line[: -(length+1)]
    print(father_node, child_node)

    for e in root.findall(father_node):
        for el in e.findall(child_node):
            e.remove(el)
            print("delete")

tree.write('output.xml')

