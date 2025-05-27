import matplotlib.pyplot as plt

X = [val for val in range(-10, 11)]
Y = [val ** 2 for val in X]

plt.scatter(X, Y, label="scatter")       # 점 그래프
plt.bar(X, Y, label="bar",)    # 막대 그래프 (약간 투명하게 겹쳐보이게)

plt.title("X^2 Graph")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid(True)

plt.legend()  

plt.show()


