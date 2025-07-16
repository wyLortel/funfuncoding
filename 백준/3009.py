lis_a = []
lis_b= []

for i in range(3):
    a,b = map(int,(input().split()))
    lis_a.append(a)
    lis_b.append(b)

check_x = []
check_y = []
c = 0
d=0

for x in lis_a:
    if x in check_x:
        c = x
    else:
        check_x.append(x)
        

for y in lis_b:
    if y in check_y:
        d = y
    else:
        check_y.append(y)

lis_a.remove(c)
lis_a.remove(c)
lis_b.remove(d)
lis_b.remove(d)

print(lis_a[0],lis_b[0])

