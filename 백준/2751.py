import sys

n = int(sys.stdin.readline())

lis = []

for i in range(n):
    num = int(sys.stdin.readline())
    lis.append(num)

lis = sorted(lis)

for k in lis:
    print(k)