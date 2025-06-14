def solution(sides):
    answer = 0
    
    for i in range(len(sides)):
        for k in range(len(sides)-1):
            if sides[k] > sides[k+1] :
                sides[k] ,sides[k+1] = sides[k+1] , sides[k]
    
    if sides[-1] >= sides[0] + sides[1]:
        answer = 2
    else:
        answer = 1
    
    return answer

