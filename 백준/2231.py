n = int(input())

col = 0

for i in range(1,1000000+1):
    s = i + sum(int(d) for d in str(i))

    if s == n:
        col = i
        break

if col >= 0 :
    print(col)
else:
    print(0)        





