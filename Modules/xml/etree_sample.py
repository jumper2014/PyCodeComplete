# coding=utf-8
# 用etree读写xml

try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="22601.xml")
print tree

root = tree.getroot()
print root.tag
print root.attrib

for child in root:
    print child.tag, child.attrib

print root[0].tag
print root[0].attrib
print root[0].text

print root[0][0].tag
print root[0][0].attrib
print root[0][0].text

# 对于ElementTree对象，有一个iter方法可以对指定名称的子节点进行深度优先遍历
for ele in tree.iter(tag="book"):
    print ele.tag, ele.attrib

print

for ele in tree.iter(tag="title"):
    print ele.tag, ele.attrib, ele.text

print
# 如果不指定元素名称，就是将所有的元素遍历一边。
for ele in tree.iter():
    print ele.tag, ele.attrib

print

# 通过路径，搜索到指定的元素，读取其内容。这就是xpath
for ele in tree.iterfind("book/title"):
    print ele.text

#利用findall()方法，也可以是实现查找功能
for ele in tree.findall("book"):
    title = ele.find('title').text
    price = ele.find('price').text
    lang = ele.find('title').attrib

print

del root[1]
new_file = "22602.xml"
tree.write(new_file)



