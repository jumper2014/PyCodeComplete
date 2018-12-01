#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import pandas as pd
from sklearn import preprocessing

if __name__ == "__main__":
    # 读取葡萄酒数据集
    df = pd.io.parsers.read_csv(
        'wine_data.csv',
        header=None,
        usecols=[0, 1, 2]
    )

    df.columns = ['Class label', 'Alcohol', 'Malic acid']
    print(df.head())

    # 标准化
    std_scale = preprocessing.StandardScaler().fit(df[['Alcohol', 'Malic acid']])
    df_std = std_scale.transform(df[['Alcohol', 'Malic acid']])
    print("df_std:", df_std)

    # 归一化
    min_max_scale = preprocessing.MinMaxScaler().fit(df[['Alcohol', 'Malic acid']])
    df_min_max = min_max_scale.transform(df[['Alcohol', 'Malic acid']])
    print("df_min_max:", df_min_max)

    # 打印标准化后两列的平均值和标准方差
    print('Mean after standardization:\nAlcohol={:.2f}, Malic acid={:.2f}'
          .format(df_std[:, 0].mean(), df_std[:, 1].mean()))
    print('\nStandard deviation after standardization:\nAlcohol={:.2f}, Malic acid={:.2f}'
          .format(df_std[:, 0].std(), df_std[:, 1].std()))

