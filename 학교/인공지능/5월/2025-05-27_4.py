import matplotlib.pyplot as plt

X = [val for val in range(-10 ,10+1)]
Y1 = [val * 2 for val in X] 
Y2 = [val * 4 for val in X] 
Y3 = [val * 8 for val in X] 


plt.plot(X,Y1, label = "2x" )
plt.plot(X,Y2, label = "4x")
plt.plot(X,Y3, label = "8x")

plt.legend()
plt.grid()

plt.title("graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()


