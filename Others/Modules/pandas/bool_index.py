#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print(df[df.A > 0])
print(df[df > 0])


df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

print(df2)

print("============= start to filter =============== ")

print(df2[df2['E'].isin(['two','four'])])