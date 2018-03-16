#!/usr/bin/env python
# coding=utf-8
# 描述显示数据的快速统计摘要


import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
print(df.describe())
