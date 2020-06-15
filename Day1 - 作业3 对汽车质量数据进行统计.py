# 对汽车投诉信息进行分析
import pandas as pd
# 数据加载
result = pd.read_csv('car_complain.csv')
# 数据数据预处理,拆分problem类型 => 多个字段
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
# 数据统计

df_brand2=result.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False)
print('品牌投诉总数：')
print(df_brand2)
df_carmodel2=result.groupby(['car_model'])['id'].agg(['count']).sort_values('count',ascending=False)
print('车型投诉总数：')
print(df_carmodel2)
df_brand_carmodel2=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False)
print('平均车型投诉最多的品牌是：')
print(df_brand_carmodel2)



'''
# df_brand=result['brand'].value_counts().index[0]
print('品牌投诉总数')
print(df_brand)
df_carmodel=result['car_model'].value_counts()
print('车型投诉总数')
print(df_carmodel)
'''


# df_brand_carmodel=result.groupby('brand')['car_model'].nunique()
# print(df_brand_carmodel)

# df4 = df_brand.sort_index()/df_brand_carmodel.sort_index()
# print(df4)

#df_brand2=result.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False)
#print(df_brand2)



'''
tags = result.columns[7:]
df_problem = result.groupby(['brand'])[tags].agg(['sum'])
print(df_problem)
'''


'''

tags = result.columns[7:]
df= result.groupby(['brand'])['car_model'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False)
print(df)
#df2= result.groupby(['brand'])[tags].agg(['sum'])
#print(df2)
'''

'''
#df3=result.groupby('brand')
#print(df3.groups)

#df2 = result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False)
#print(df2)


print(result.columns)
tags = result.columns[7:]
df= result.groupby(['brand'])['id'].agg(['count'])
#print(df)

df2= result.groupby(['brand'])[tags].agg(['sum'])
#print(df2)


df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
#df2.to_csv('temp.csv')
# 按照count从大到小进行排序
df2= df2.sort_values('count', ascending=False)
print(df2)

#print(df2.columns)
#df2.to_csv('temp.csv', index=False)
query = ('A114', 'sum')
print(df2.sort_values(query, ascending=False))
'''