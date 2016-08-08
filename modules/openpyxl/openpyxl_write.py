# coding=utf-8
"""
写入excel文件
"""

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws1 = wb.create_sheet("Sheet1")
ws.title = "python"

ws01 = wb['python']
print (ws is ws01)

ws02 = wb.get_sheet_by_name("python")
print (ws is ws02)

print wb.get_sheet_names()
for sh in wb:
    print sh.title

ws['B4'] = 4444
b4 = ws['B4']
print b4.value

i = 1

for row in ws.iter_rows("A1:C3"):
    for cell in row:
        print cell
        cell.value = i
        i += 1


wb.save("1234.xlsx")
