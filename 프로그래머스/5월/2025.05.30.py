def solution(a, d, included):
    answer = a
    for i in range(len(included)):
        if included[i]:
            answer += d
    return answer


print(solution(3,4,[True,False,False,True,True]))