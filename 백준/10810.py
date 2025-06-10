N , M = map(int,input().split())

basket = [0 for _ in range(N)]

for _ in range(M):
    i,j,k = map(int,input().split())
    basket[i-1:j] = [k]* len(basket[i-1:j])

for l in basket:
    print(l , end=" ")

