def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
            
    new_lis = []
    
    for k in answer:
        if k == 1 :
            continue
        if k == 2:
            new_lis.append(k)
            continue
        
        
        
        for j in range(1,k+1):
            if j == 1 or j == k:
                continue
            if k % j == 0:
                break
        else: new_lis.append(k)  
    return new_lis


print(solution(420))