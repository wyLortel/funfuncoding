def solution(my_str, n):
    answer = []
    
    for i in range(0,len(my_str),n):
        s= my_str[i:i+n]
        answer.append(s)
    
    return answer

print(solution("abc1Addfggg4556b",6))