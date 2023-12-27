import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("D:/амгс/titanic.csv")

features = data[['Sex', 'Age', 'Pclass']]

features['Sex'] = features['Sex'].astype('category')
features['Sex'] = features['Sex'].cat.codes  

features['Age'].fillna(features['Age'].mean(), inplace=True)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(scaled_features)

data['Cluster'] = kmeans.labels_

plt.figure(figsize=(10, 6))

for cluster in range(3): 
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Age'], cluster_data['Pclass'], label=f"Cluster {cluster}", alpha=0.5)

plt.title('Кластеризация методом KMeans')
plt.xlabel('Возраст')
plt.ylabel('Класс')
plt.legend()
plt.show()
