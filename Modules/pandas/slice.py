#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[0:3])

print("========= 指定选择日期 ========")

print(df['20170102':'20170103'])