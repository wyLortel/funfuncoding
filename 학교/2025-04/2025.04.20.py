N, M = map(int, input().split())
lista = [0] * N 

for i in range(N):
    lista[i] = i+1

for i in range(M):
    n, m = map(int, input().split()) 
    n -= 1 
    m -= 1 
    for i in range(((abs(n-m)+1) // 2)):
        b = lista[n + i]
        lista[n + i] = lista[m - i]
        lista[m - i] = b

for i in lista:
    print(i, end = " ")