# coding=utf-8
# 一行里捕捉多个异常

try:
    # 可能出错的代码
    pass
except (ValueError, ZeroDivisionError) as e:
    pass

