n , m = map(int,(input().split()))


lis1 = []
lis2 = []


for i in range(n):
    a = list(map(int,(input().split())))
    lis1.append(a)
    

for k in range(n):
    b = list(map(int,(input().split())))
    lis2.append(b)



for row in range(n):
    for col in range(m):
        print(lis1[row][col] + lis2[row][col] , end=" ")
    print()

    