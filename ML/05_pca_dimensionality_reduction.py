# Experiment 5: Dimensionality Reduction using PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X_scaled = StandardScaler().fit_transform(iris.data)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance retained:", pca.explained_variance_ratio_.sum())

for class_id, name in enumerate(iris.target_names):
    plt.scatter(X_pca[iris.target == class_id, 0],
                X_pca[iris.target == class_id, 1], label=name)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.title("Iris dataset after PCA"); plt.legend(); plt.show()
