n = int(input())
changes = [25, 10, 5, 1]


for i in range(n):
    price = int(input())
    res = []
    for i in changes :
        res.append(price // i)
        price = price % i

    print(*res)

