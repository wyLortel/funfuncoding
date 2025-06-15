def solution(my_string):
    answer = 0
    num = ""
    
    for ch in my_string:
        if ch.isdigit():
            num += ch
        else:
            if num != "":
                answer += int(num)
                num = ""
                
    if num != "":
        answer += int(num)
    
    return answer
