a,b,c,d,e,=map(int,input().split())

def square (num):
    return num ** 2

print((square(a)+square(b)+square(c)+square(d)+square(e)) % 10 )