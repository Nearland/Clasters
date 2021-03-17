#import matplotlib.pyplot as plt
#from sklearn.cluster import KMeans


#f = open('file.txt', 'r')
#x = []
#y = []

#for line in f:
  #  a, b = map(int, line.split())
  #  x.append(a)
  #  y.append(b)
  #  plt.scatter(x,y)

#plt.show()

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

f = open('kk.txt', 'r')

pts = []

for line in f:
    x, y = map(int, line.split())
    pts.append([x, y])


dbscan = DBSCAN(eps=35)
dbscan.fit(pts)
pca = PCA(n_components=2).fit(pts)
pca_2d = pca.transform(pts)

for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
plt.show()

#km = KMeans(n_clusters=2)
#km.fit(pts)
#cl = km.labels_

#for i in range(len(pts)):
   # if cl[i] == 0:
     #   plt.scatter(pts[i][0], pts[i][1], c='red')
   # if cl[i] == 1:
    #    plt.scatter(pts[i][0], pts[i][1], c='green')


