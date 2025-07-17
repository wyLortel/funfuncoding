while True:
    a,b,c = map(int,input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    lis = [a,b,c]
    max_num = max(lis)
    
    lis.remove(max_num)
    
    num1 = lis[0]
    num2 = lis[1]
    
    if max_num >= num1 + num2:
        print("Invalid") 
    
    elif a == b and a == c:
        print("Equilateral")
    elif a != b and a!=c and b !=c:
        print("Scalene")
    elif a == b or a == c or b == c :
        print("Isosceles")