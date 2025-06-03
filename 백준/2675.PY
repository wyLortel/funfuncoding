N = int(input())


for i in range(N):
    a,b = input().split()
    p = ""
    for k in b:
        p += k*int(a)
    print(p)
