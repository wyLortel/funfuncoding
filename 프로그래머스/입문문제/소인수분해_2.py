def solution(n):
    d = 2
    lis = []
    
    while True:
        if n % d == 0:
            n /= d
            if d not in lis:
                lis.append(d)
        else:
            d += 1
        
        if n == 1:
            break
                
    return lis


print(solution(420))