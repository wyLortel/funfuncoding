def solution(num, k):
    answer = 0
    
    num = str(num)
    count = 1
    
    for i in num:
        if i == str(k):
            answer = count
            break
        count += 1
    else:
        answer = -1
    
    return answer



