# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:04:03 2020

@author: DongRunchao
"""

from pandas import Series, DataFrame
import pandas as pd

data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print('全班各科成绩为：')
print(df)
print('全班各科平均成绩为：')
print(df.mean())
print('全班各科最差成绩为：')
print(df.min())
print('全班各科最好成绩为：')
print(df.max())
print('全班各科成绩方差为：')
print(df.var())
print('全班各科成绩标准差为：')
print(df.std())
df['sum']=df.sum(axis=1)
# df['sum']= df['语文']+df['数学']+df['英语']
print('全班各科成绩排名为：')
print(df.sort_values(by='sum',ascending = False))
