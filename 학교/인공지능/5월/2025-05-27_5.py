import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

X = [
    (2.0 , 1.8), (1.8 , 2.2), (2.2 , 2.0), (1.9 , 2.1), (2.1 , 1.9),
    (6.0 , 2.1), (6.2 , 1.8), (5.8 , 2.0), (6.1 , 2.2), (5.9 , 1.9),
    (2.0 , 6.0), (2.2 , 6.2), (1.8 , 5.9), (2.1 , 6.1), (1.9 , 5.8),
    (6.0 , 6.0), (5.9 , 6.2), (6.1 , 5.8), (5.8 , 5.9), (6.2 , 6.1)
]



cluster_labels = [0] * 5 + [1] * 5 + [2] * 5 + [3] * 5


x = [pt[0] for pt in X]
y = [pt[1] for pt in X]  


colors = [plt.cm.tab10(i) for i in range(4)]
custom_cmap = ListedColormap(colors)

plt.scatter(x,y, c = cluster_labels , cmap=custom_cmap, s=100 , alpha=0.8)

plt.title("4 cluster (Color mapped by ListenColormap from tab10)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()