def solution(hp):
    answer = 0
    
    tairyoku = hp
    
    answer += tairyoku // 5
    
    answer += (tairyoku%5) // 3
    
    answer += ((tairyoku%5) % 3) // 1
    
    return answer
    
    