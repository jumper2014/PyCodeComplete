# coding=utf-8
# 根据指定的行号,从文本文件中读取一行数据

def getline(thefilepath, desired_line_number):
    if desired_line_number < 1:
        return ''
    for current_line_number, line in enumerate(open(thefilepath, 'rU')):
        if current_line_number == desired_line_number-1:
            return line
    return ''

thefilepath = "file.txt"
desired_line_number = 5
theline = getline(thefilepath, desired_line_number)
print theline