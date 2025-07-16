n = int(input())


lis_a = []
lis_b = []

for _ in range(n):
    a ,b =map(int,input().split())
    lis_a.append(a)
    lis_b.append(b)


num1 = max(lis_a) - min(lis_a)
num2 = max(lis_b) - min(lis_b)

print(num1 * num2)
