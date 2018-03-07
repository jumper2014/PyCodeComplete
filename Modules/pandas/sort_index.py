#!/usr/bin/env python
# coding=utf-8
# 通过轴排序
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)
print(df.sort_index(axis=1, ascending=False))