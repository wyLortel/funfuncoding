def solution(i, j, k):
    answer = 0
    
    for one in range(i,j+1):
        for two in str(one):
            if two == str(k):
                answer+=1
    return answer

