# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn.cluster import DBSCAN
# from sklearn.decomposition import PCA
#
# f = open('laba3.txt', 'r')
# x = []
# y = []
# z = []
# e = []
# g = []
#
# for line in f:
#     a, b, p, k = map(int, line.split())
#     x.append(a)
#     y.append(b)
#     z.append(p)
#     e.append(k)
#     plt.scatter(x, y)
#     plt.scatter(z, e)
#
# g = [x, y, z, e]
# print(g)
# dbscan = DBSCAN(eps=50)
# dbscan.fit(g)
# pca = PCA(n_components=2).fit(g)
# pca_2d = pca.transform(g)
#
# for i in range(0, pca_2d.shape[0]):
#     if dbscan.labels_[i] == 0:
#         c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='4')
#     elif dbscan.labels_[i] == 1:
#         c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
#     elif dbscan.labels_[i] == -1:
#         c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
#
# plt.show()
#
#
# dbscan = DBSCAN(eps=50)
# dbscan.fit(g)
# pca = PCA(n_components=2).fit(g)
# pca_2d = pca.transform(g)
#
# pca = PCA(n_components=2).fit(g)
# pca_2d = pca.transform(g)
#
# for i in range(0, pca_2d.shape[0]):
#     if dbscan.labels_[i] == 0:
#         c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='4')
#     elif dbscan.labels_[i] == 1:
#         c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
#     elif dbscan.labels_[i] == -1:
#         c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
#
# plt.show()

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

f = open('laba3.txt', 'r')

pts = []

for line in f:
    x, y, z, t = map(int, line.split())
    pts.append([x, y, z, t])
pca = PCA(n_components=2)
pca_2d = pca.fit_transform(pts)

dbscan = DBSCAN(eps=50)
dbscan.fit(pca_2d)

for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='4')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
plt.show()
#
# #km = KMeans(n_clusters=2)
# #km.fit(pts)
# #cl = km.labels_
#
# #for i in range(len(pts)):
#    # if cl[i] == 0:
#      #   plt.scatter(pts[i][0], pts[i][1], c='red')
#    # if cl[i] == 1:
#     #    plt.scatter(pts[i][0], pts[i][1], c='green')
