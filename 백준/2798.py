N,M = map(int,input().split())

lis = list(map(int,input().split()))

corr = 0

for i in range(N):
    for k in range(i+1,N):
        for j in range(k+1,N):
            card = lis[i] + lis[k] + lis[j]
            if corr < card <= M:
                corr = card

print(corr)