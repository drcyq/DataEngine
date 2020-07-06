
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:56:20 2020

@author: DongRunchao
"""


import pandas as pd
import numpy as np
from efficient_apriori import apriori

# Head=None，不将第一行作为head
dataset=pd.read_csv('./Market_Basket_Optimisation.csv',header=None)
print(dataset.shape)

# 将数据放到transactions里
transactions = []
for i in range(0,dataset.shape[0]):
    temp=[]
    for j in range(0,20):
        # print(dataset.values[i,j])
        if str(dataset.values[i,j]) !='nan':
            temp.append(str(dataset.values[i,j]))
    transactions.append(temp)

#使用efficient_apriori工具包 效率较高，但返回参数较少
# 挖掘频繁项集与关联规则
itemsets, rules = apriori(transactions,min_support=0.02,min_confidence=0.4)
print('使用efficient_apriori工具包','-'*20)
print('频繁项集：',itemsets)
print('关联规则：',rules)


#使用mlxtend.frequent_patterns工具包 效率较低，但返回参数较多
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

dataset.fillna('', inplace=True)

for i in range(0,dataset.shape[0]):
    for j in range(0,dataset.shape[1]):
        if dataset.values[i,j] != '' and j != 0:
            dataset.values[i,0] = dataset.values[i,0] + "/" + dataset.values[i,j] 
            dataset.values[i,j] = ''
transcation2 = dataset[0].str.get_dummies("/")
#transcation2.to_csv('temp2.csv')

frequent_itemsets = apriori(transcation2, min_support=0.02, use_colnames=True)
# 按照支持度从大到小
frequent_itemsets = frequent_itemsets.sort_values(by="support" , ascending=False) 
print('-'*20, '频繁项集', '-'*20)
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
print("频繁项集：", frequent_itemsets)
# 按照提升度从大到小进行排序
rules = rules.sort_values(by="lift" , ascending=False) 
#rules.to_csv('./rules.csv')
print('-'*20, '关联规则', '-'*20)
print(rules)
