### xlrd简介
- xlrd是一个用来从Microsoft Excel读取数据的Python第三方库
- 可以在任何平台上从xls和xlsx文件里面读取数据
- 支持Python2.7和Python3.4+
- 支持Excel日期格式和Unicode

### 一个示例学会使用
```
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
```

### 代码地址
本系列文章和代码已经作为项目归档到github，仓库地址：jumper2014/PyCodeComplete。大家觉得有帮助就请在github上star一下，你的支持是我更新的动力。什么？你没有github账号？学习Python怎么可以没有github账号呢，快去注册一个啦！