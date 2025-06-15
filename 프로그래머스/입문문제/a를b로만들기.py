def pro(lis):
    for i in range(len(lis)):
        for k in range(len(lis)-1):
            if lis[k] > lis[k+1] :
                lis[k],lis[k+1] = lis[k+1] , lis[k]
    return lis

def solution(before, after):
    answer = 0
    lis_1 = list(before)
    lis_2 = list(after)    
    
    
    lis_1 = pro(lis_1)
    lis_2 = pro(lis_2)
    
    if lis_1 == lis_2:
        answer = 1
    else:
        answer = 0
    
    return answer


print(solution("allpe" ,"apple"))