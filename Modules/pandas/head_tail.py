#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.head())
print("--------------" * 10)
print(df.tail(3))