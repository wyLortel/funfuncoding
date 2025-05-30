a, b = map(int,input().split()) 


if b < 45:
    a -= 1
    b += 60
    if a < 0:
        a = 23
        
b -= 45

    
print(a,b)