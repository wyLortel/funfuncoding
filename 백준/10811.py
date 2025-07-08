N , M = map(int,input().split())

baket = [i for i in range(1,N+1)]

for i in range(M):
    num1 , num2 = map(int,input().split())
    baket[num1-1:num2] = baket[num1-1:num2][::-1]
    

print(*baket)
    