#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import xlrd
from xlutils import copy

if __name__ == "__main__":
    # id    name    age
    # 1    Python    30
    # 2    Perl    33
    # 3    Ruby    20

    # 打开要读的xls
    rd_book = xlrd.open_workbook('origin.xls')
    # 复制为新的xls
    wt_book = copy.copy(rd_book)
    # 修改新的xls
    wt_sheet = wt_book.get_sheet(0)
    wt_sheet.write(1, 1, 'Python3')

    # 保存修改
    wt_book.save('copy.xls')

    # id    name    age
    # 1    Python3    30
    # 2    Perl    33
    # 3    Ruby    20
