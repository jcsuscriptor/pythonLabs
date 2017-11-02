from sklearn.datasets import make_blobs
blobs, classes = make_blobs(500, centers=3)
import numpy as np
import matplotlib.pyplot as plt

rgb = np.array(['r', 'g', 'b','y'])

from sklearn.cluster import KMeans
#kmean = KMeans(copy_x=True, init='k-means++', max_iter=300, n_clusters=3, n_init=10, n_jobs=1, precompute_distances=True, random_state=None, tol=0.0001, verbose=0)
kmean = KMeans(n_clusters=3)
kmean.fit(blobs)


f, ax = plt.subplots(figsize=(7.5, 7.5))
ax.scatter(blobs[:, 0], blobs[:, 1], color=rgb[classes])
ax.scatter(kmean.cluster_centers_[:, 0],
 kmean.cluster_centers_[:, 1], marker='*', s=250,
 color='black', label='Centers')

ax.set_title("Blobs")
ax.legend(loc='best') 
 
 
 
plt.show()