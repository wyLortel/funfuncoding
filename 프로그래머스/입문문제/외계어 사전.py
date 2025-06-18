def solution(spell, dic):
    answer = 0
    
    for i in dic:
        count = 0
        count_lis = []
        for k in i:
            if k in spell and k not in count_lis:
                count += 1
                count_lis.append(k)
            if count == len(spell):
                answer = 1
    
    
    if answer == 0:
        answer = 2
    
    
    return answer


s = ["z", "d", "x"]
d = ["def", "dww", "dzx", "loveaw"]
print(solution(s,d))