#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import xlrd


if __name__ == "__main__":
    # id    name    age
    # 1    Python    30
    # 2    Perl    33
    # 3    Ruby    20

    workbook = xlrd.open_workbook('origin.xls')
    # 打开excel文件并获取所有sheet
    assert(workbook.sheet_names() == ['users', 'Sheet2', 'Sheet3'])

    # 根据下标获取sheet名称
    sheet1_name = workbook.sheet_names()[0]
    assert(sheet1_name == 'users')

    # 根据sheet索引或者名称获取sheet内容，同时获取sheet名称、行数、列数
    sheet1 = workbook.sheet_by_index(0)
    assert (sheet1.name, sheet1.nrows, sheet1.ncols) == ('users', 4, 3)

    # 根据sheet名获得某行或者某列的值
    sheet1 = workbook.sheet_by_name('users')
    row1 = sheet1.row_values(1)
    col_id = sheet1.col_values(0)
    assert (row1 == [1.0, 'Python', 30.0])
    assert (col_id == ['id', 1.0, 2.0, 3.0])

    # 获取指定单元格的内容
    assert(sheet1.cell(1, 0).value == 1)
    assert(sheet1.cell(1, 1).value == 'Python')
    assert(sheet1.cell(1, 2).value == 30)
