from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

f =('laba6.txt', 'r')

data = []
data2 = []


for line in f:
    x, y, = map(int, line.split())
    plt.scatter(x,y)
    print(x)

plt.show()