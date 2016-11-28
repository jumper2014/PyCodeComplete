# coding=utf-8
"""
读取excel文件内容
"""
from openpyxl import load_workbook

wb2 = load_workbook("1234.xlsx")
print wb2.get_sheet_names()
ws_wb2 = wb2["python"]
for row in ws_wb2.rows:
    for cell in row:
        print cell.value
