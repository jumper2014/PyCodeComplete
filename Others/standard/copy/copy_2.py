# coding=utf-8
# 深度拷贝,对象中的属性和内容被分别和递归地拷贝

import copy
existing_list_of_dicts = [{"name": "hello"}, {"name": "python"}]
new_list_of_dicts = copy.deepcopy(existing_list_of_dicts)
print existing_list_of_dicts
