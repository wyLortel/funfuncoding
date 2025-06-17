def fack (num) :
    fack_num = 1
    for i in range(1,num+1):
        fack_num *= i
    return fack_num

def solution(balls, share):
    answer = 0
    
    ball_f = fack(balls)
    
    share_f = fack(share)
    
    bs_fack = fack((balls-share))
    
    
    answer = ball_f / (bs_fack * share_f)
    return answer


print(solution(5,3))
    
    
    
        
    
    
    