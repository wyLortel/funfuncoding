# x
# y
# w - x
# h - y

a , b, c, d = map(int,input().split())

c -= a
d -= b

lis = [a,b,c,d]

print(min(lis))



