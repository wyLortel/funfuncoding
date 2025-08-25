import sys
input = sys.stdin.readline

n1 , n2 = map(int,input().split())
lis = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

cor = []

for i in lis:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(n2):
    a,b = map(int,input().split())
    cor.append(prefix_sum[b]-prefix_sum[a-1])


for k in cor:
    print(k)