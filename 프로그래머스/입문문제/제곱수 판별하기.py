def solution(n):
    answer = 0
    for i in range(n):
        if i * i == n:
            answer = 1
            break
    else:
        answer = 2
    return answer

print(solution(144))