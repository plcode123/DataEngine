print("Thinking&Action 1: Print even numbers from 1 to 100")

def sum ( ):
    sum = 0
    n = 1
    while n < 101:
        sum = sum + n
        n += 2
    return sum
print("result:")
print ( sum ( ) )
'''
#Thinking&Action 2: Print even numbers from 1 to 100
Basic statistic in pandas DataFrame
min,max,average,variance、Standard Deviation
姓名	语文	数学	英语
张飞	68	65	30
关羽	95	76	98
刘备	98	86	88
典韦	90	88	77
许褚	80	90	90
'''
print("Thinking&Action 2")

import pandas as pd
import numpy as np
excelFile = r'1.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
print(df)
df2=(df.describe(percentiles=[.2,.8]))
ch = df["语文"].var()
mt = df["数学"].var()
en = df["英语"].var()
print(df2)
print("var   %f %f %f" %(ch,mt,en))
df['score']=df["语文"]+df["数学"]+df["英语"]
df.sort_values(by=['score'],inplace=True,ascending = False)
print(df)

print("Thinking&Action 3")

result=pd.read_csv('car_complain.csv')
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
#print(result.columns)
df = result.groupby(['brand'])['id'].agg(['count'])
print("品牌投诉榜")
print(df.sort_values('count',ascending=False))
df1 = result.groupby(['car_model'])['id'].agg(['count'])
print("车型投诉榜")
print(df1.sort_values('count',ascending=False))
df2=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby( ['brand']).mean()
print("平均投诉榜")
print(df2.sort_values('count',ascending=False))