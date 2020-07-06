#lesson 4 Market Basket Analysis (Apriori) in Python
#陈老师，Python有强大的第三方库和学习社区，请问国内国外著名的学习社区有哪些？学习！

import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import networkx as nx
import matplotlib.pyplot as plt
# header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
# shape为(7501,20)
print(dataset.shape)
# 将数据存放到transactions中
transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
print(transactions)
te = TransactionEncoder ( )
# 进行 one-hot 编码
te_ary = te.fit ( transactions ).transform ( transactions )
df = pd.DataFrame ( te_ary, columns=te.columns_ )

print(df)
# 利用 Apriori 找出频繁项集
freq = apriori ( df, min_support=0.02,  use_colnames=True )
# 导入关联规则包
from mlxtend.frequent_patterns import association_rules
# 计算关联规则
rules = association_rules(freq, metric="lift", min_threshold=0.5)
print ( "频繁项集：", freq )
print ( "关联规则：", rules)
#graph plot
def draw_graph(rules, rules_to_show):
    G1 = nx.DiGraph()
    color_map=[]
    N = 50
    colors = np.random.rand(N)
    strs=['R0', 'R1', 'R2', 'R3', 'R4', 'R5']

    for i in range(rules_to_show):
        G1.add_nodes_from(["R"+str(i)])
        for a in rules.iloc[i]['antecedents']:
            G1.add_nodes_from([a])
            G1.add_edge(a, "R"+str(i), color=colors[i] , weight = 2)
        for c in rules.iloc[i]['consequents']:
            G1.add_nodes_from([c])
            G1.add_edge("R"+str(i), c, color=colors[i],  weight=2)
    for node in G1:
        found_a_string = False
        for item in strs:
            if node==item:
                found_a_string = True
        if found_a_string:
            color_map.append('yellow')
        else:
            color_map.append('green')
    edges = G1.edges()
    colors = [G1[u][v]['color'] for u,v in edges]
    weights = [G1[u][v]['weight'] for u,v in edges]
    pos = nx.spring_layout(G1, k=16, scale=1)
    nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16,
            with_labels=False)
    for p in pos:  # raise text positions
        pos[p][1] += 0.07
        nx.draw_networkx_labels(G1, pos)
        plt.show()
draw_graph (rules, 6)