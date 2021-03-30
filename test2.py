from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier

data = []
res = []

f = open('laba6.txt', 'r')
for line in f:
    h, w, st, r = map(int, line.split())
    data.append([h, w, st])
    res.append(r)

neuralnet = MLPClassifier()
neuralnet.fit(data, res)

test = [[195, 78, 12000]]
pr = neuralnet.predict(test)
toch = neuralnet.score(data, res)
clf = AdaBoostClassifier()
clf.fit(data, res)
pr2 = clf.predict(test)
toch2 = clf.score(data, res)
print(pr)
print(toch)
print(pr2)
print(toch2)
