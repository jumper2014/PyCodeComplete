# coding=utf-8
# 如果列表中存在指定索引,就返回该索引的元素

def list_get(L, i, default_value=None):
    if -len(L) <= i < len(L):
        return L[i]
    else:
        return default_value