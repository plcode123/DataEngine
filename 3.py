import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans
from sklearn import preprocessing
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import pandas as pd
import numpy as np
# elbow method, which is used to determine the optimal value of K to perform the K-Means clustering Algorithm
data=pd.read_csv('car_data.csv', encoding="gbk")
train_x=data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]
sse = []
#1 to 11 randeom initializatin method
# the number of time, with which the k_means algorithm will be run, is limited to 1000
for k in range(1, 11):
	kmeans = KMeans(n_clusters=k,max_iter=1000)
	kmeans.fit(train_x)
	# calculates squared error for the clustered points
	sse.append(kmeans.inertia_)
x = range(1, 11)
# label the axes
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-',color='r',linewidth='1')
# add title of label to X axis
plt.xlabel("Value of K")
# add title of label to X axis
plt.ylabel("Sqaured Error (sse)")
# show most optimal value for choosing k in plot
plt.show()
#clear the figure
plt.clf()

#LableEncoder
from sklearn.preprocessing import LabelEncoder
# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
print(train_x)
#pd.DataFrame(train_x).to_csv('temp.csv',index=False)
kmeans = KMeans(n_clusters=5)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("customer_cluster_result.csv",index=False)
