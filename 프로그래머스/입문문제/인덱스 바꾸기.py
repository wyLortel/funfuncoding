def solution(my_string, num1, num2):
    answer = ""
    
    str1 = my_string[num1]
    str2 = my_string[num2]
    
    for i in range(len(my_string)):
        if i == num1:
            answer += str2
            continue
                
        if i == num2:
            answer += str1
            continue
        
        answer+=my_string[i]
    
    return answer

print(solution("hello",1,2))
    