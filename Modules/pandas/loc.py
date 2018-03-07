#!/usr/bin/env python
# coding=utf-8
# 使用标签获取横截面
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print(df.loc[dates[0]])
print(df.loc[:,['A','B']])
print(df.loc['20170102':'20170104',['A','B']])
print(df.loc['20170102',['A','B']])
print(df.loc[dates[0],'A'])

print(df.at[dates[0],'A'])  #快速访问标量(等同于先前的方法)
print(df.iloc[3])  # 通过传递的整数的位置选择
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])
print(df.iloc[1:3,:])
print(df.iloc[:,1:3])
print(df.iloc[1,1])
print(df.iat[1,1])  #要快速访问标量(等同于先前的方法)