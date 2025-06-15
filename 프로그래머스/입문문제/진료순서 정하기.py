def solution(emergency):
    answer = []
    
    lis = []
    
    for i in emergency:
        lis.append(i) 
    
    for i in range(len(emergency)):
        for j in range(len(emergency)-1):
            if emergency[j] < emergency[j+1]:
                emergency[j] , emergency[j+1] = emergency[j+1] , emergency[j]
                

    for k in range(len(lis)):
        for l in range(len(emergency)):
            if lis[k] == emergency[l]:
                answer.append(l+1)
    
    
    return answer


lis = [30, 10, 23, 6, 100]
print(solution(lis))