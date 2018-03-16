#!/usr/bin/env python
# coding=utf-8
# 通过传递numpy数组，使用datetime索引和标记列来创建DataFrame

import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
print(dates)

print("--"*16)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
