n = int(input())

lis = []

for i in range(n):
    a = list(input().split())
    lis.append(a)

lis.sort(key=lambda x: int(x[0]))

for row in lis:
    print(' '.join(row))