N , M = map(int,(input().split()))

lis = [i for i in range(1,N+1)]

for i in range(M):
    num1 , num2 = map(int,(input().split()))
    lis[num1-1] , lis[num2-1] = lis[num2-1] , lis[num1-1]

print(*lis)