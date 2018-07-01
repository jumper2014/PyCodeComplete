### xlutils简介
- xlutils提供一组用来操作Excel的工具，这些工具可能需要xlrd和xlwt的配合。下面是一些主要工具
- xlutils.copy 用来将xlrd.Book对象复制到xlwt.Workbook对象
- xlutils.display 用用户友好的方式显示xlrd相关对象
- xlutils.filter 分割和过滤Excel文件内容
- xlutils.save 序列化xlrd.Book对象到Excel文件

### 一个示例学会使用
```
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
```




### 代码地址
本系列文章和代码已经作为项目归档到github，仓库地址：jumper2014/PyCodeComplete。大家觉得有帮助就请在github上star一下，你的支持是我更新的动力。什么？你没有github账号？学习Python怎么可以没有github账号呢，快去注册一个啦！