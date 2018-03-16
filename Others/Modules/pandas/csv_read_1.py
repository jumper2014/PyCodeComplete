# coding=utf-8
# read local csv file

import pandas as pd

df = pd.read_csv('tips.csv')
# df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" )

print df


