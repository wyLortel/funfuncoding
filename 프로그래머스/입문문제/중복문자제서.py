def solution(my_string):
    answer = ''
    lis = []
    
    for i in my_string:
        if i not in lis:
            lis.append(i)
    
    answer = "".join(lis)
    
    return answer 




print(solution("people"))