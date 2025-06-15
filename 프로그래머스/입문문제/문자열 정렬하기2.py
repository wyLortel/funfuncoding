def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i
    
    answer = list(answer)
    
    for k in range(len(answer)):
        for j in range (len(answer)-1):
            if answer[j] > answer[j+1] :
                answer[j] , answer[j+1] = answer[j+1] , answer[j]
    
    kotae = ""
    
    for i in answer:
        kotae += i
    
    return kotae



s = solution("Bcad")
print(s)