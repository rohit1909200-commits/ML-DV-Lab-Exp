# Experiment 9: K-Means Clustering
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
X_2d = PCA(n_components=2).fit_transform(X)
print("Cluster labels:", labels)
print("Inertia:", kmeans.inertia_)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels)
plt.xlabel("PCA component 1"); plt.ylabel("PCA component 2")
plt.title("K-Means clustering of Iris data"); plt.show()
