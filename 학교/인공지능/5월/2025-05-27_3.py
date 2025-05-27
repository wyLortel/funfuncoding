import matplotlib.pyplot as plt

X = [val for val in range(-10, 11)]
Y1 = [2 *val for val in X]
Y2 = [4 * val for val in X]
Y3 = [8 * val for val in X]


plt.plot(X,Y1, label = "2x", color = "red")
plt.plot(X,Y2,  label = "4x")
plt.plot(X,Y3, label = "8x")
plt.legend

plt.title("X^2 Graph")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid(True)

plt.legend()  

plt.show()


