num1 = int(input())
num2 = int(input())

lis = []

for i in range(num1,num2+1):
    for k in range(2,i):
        if i % k == 0:
            break
    else:
        lis.append(i)


if lis:
    print(sum(lis))

    for j in lis:
        if j >= num1:
            print(j)
            break
else:
    print(-1)