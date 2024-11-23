import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = np.array([
    [1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [8, 2], [10, 2], [9, 3]
])


kmeans = KMeans(n_clusters=3)

kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o')

plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='x', label='Centroids')

plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
