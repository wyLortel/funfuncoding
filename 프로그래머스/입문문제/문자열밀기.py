def solution(A, B):
    answer = 0
    count = 0
    new_s = A
    
    if new_s == B:
        return 0 
    
    for i in range(len(A)):
        new_s = new_s[-1] + new_s[:-1]
        count += 1
        if new_s == B :
            break
        
        
    
    if count == 0 or count == len(A):
        count = -1
    
    return count



print(solution("apple" ,"elppa"))