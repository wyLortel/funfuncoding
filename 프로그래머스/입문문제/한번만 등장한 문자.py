def solution(s):
    answer = ''
    
    lis = []
    chu_list = []
    
    for i in s:
        if i in lis:
            lis.remove(i)
            chu_list.append(i)
            continue
        
        if i not in chu_list:
            lis.append(i)
            
    
    for k in range(len(lis)):
        for j in range(len(lis)-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1] , lis[j]
            
            
    
    return answer.join(lis)



print(solution("abdc"))