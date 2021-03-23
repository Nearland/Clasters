import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder


f = open('laba5.txt', 'r')

pts = []

for line in f:
    x, y, z, t =  map(int, line.split())
    pts.append([x, y, z, t])

encoder = OneHotEncoder()
encoder_roles = encoder.fit_transform(pts)
newData = encoder_roles.toarray()

pca = PCA(n_components=2)
pca_2d = pca.fit_transform(newData)

dbscan = DBSCAN(eps=50)
dbscan.fit(newData)
cl = dbscan.labels_

for i in range(len(pca_2d)):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='4')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
plt.show()
