import matplotlib.pyplot as plt

#값
X = [val for val in range(0,20+1)]
Y = [val *2 for val in X]

print(X)
print(Y)

#그래프 선택
plt.scatter(X,Y, color='red' , marker="*") #선현 그래프


#그래프 꾸미기
plt.xlabel("x")
plt.ylabel("y")
plt.title("graph")
plt.grid(True)

#그래프 출력
plt.show()