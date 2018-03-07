#!/usr/bin/env python
# coding=utf-8

# 通过传递可以转换为类似系列的对象的字典来创建DataFrame

import pandas as pd
import numpy as np

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20170102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)