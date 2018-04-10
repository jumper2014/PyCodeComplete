#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import xlwt

if __name__ == "__main__":
    # 创建工作簿
    wb = xlwt.Workbook()

    # 创建第一个sheet-'users'
    sheet1 = wb.add_sheet('users', cell_overwrite_ok=True)

    # 创建一个3列的表头作为第1行
    row0 = ['id', 'name', 'age']
    for col_num in range(len(row0)):
        sheet1.write(0, col_num, row0[col_num])

    # 行数据
    rows = [
        [1, 'Python', 30],
        [2, 'Perl', 33],
        [3, 'Ruby', 20]
    ]

    # 逐行写入
    row_num = 1
    for row in rows:
        for col_num in range(len(row)):
            sheet1.write(row_num, col_num, row[col_num])
        row_num += 1
    #
    wb.save('new.xls')




