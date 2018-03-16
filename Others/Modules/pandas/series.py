#!/usr/bin/env python
# coding=utf-8
# 通过传递值列表来创建一个系列，让Pandas创建一个默认的整数索引
import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])

print(s)