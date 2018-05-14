#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    # 赋值，同一个对象的引用
    old_list = [1, 2, 3, 4]
    new_list = old_list
    new_list.append(5)
    print("new_list items : ", new_list)
    # [1, 2, 3, 4, 5]
    print("old_list items : ", old_list)
    # [1, 2, 3, 4, 5]

    # 浅拷贝
    import copy
    old_list = [1, 2, 3, 4]
    new_list = copy.copy(old_list)
    new_list.append(5)
    print("new_list items : ", new_list)
    # [1, 2, 3, 4, 5]
    print("old_list items : ", old_list)
    # [1, 2, 3, 4]

    # 浅拷贝
    old_list = [[1, 2], [3, 4]]
    new_list = copy.copy(old_list)
    new_list[0].append(10)
    print("new_list items : ", new_list)
    # [[1, 2, 10], [3, 4]]
    print("old_list items : ", old_list)
    # [[1, 2, 10], [3, 4]]

    # 深拷贝
    list_of_list = [[1, 2], [3, 4], ["A", "B"]]
    new_list_of_list = copy.deepcopy(list_of_list)
    new_list_of_list[0].append(10)
    new_list_of_list[1].remove(3)
    list_of_list[2].append("C")
    print("list_of_list items : ", list_of_list)
    # [[1, 2], [3, 4], ['A', 'B', 'C']]
    print("new_list_of_list items : ", new_list_of_list)
    # [[1, 2, 10], [4], ['A', 'B']]

