def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    
    for k in range(len(answer)):
        for j in range(len(answer)-1):
            if answer[j] > answer[j+1]:
                answer[j],answer[j+1] = answer[j+1] , answer[j]
    
    
    return answer