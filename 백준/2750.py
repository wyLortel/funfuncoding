n = int(input())
lis = []
for _ in range(n):
    num = int(input())
    lis.append(num)

new_lis = sorted(lis)

for i in new_lis:
    print(i)