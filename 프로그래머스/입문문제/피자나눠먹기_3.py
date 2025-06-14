def solution(slice, n):
    answer = 1
    for i in range(1,n):
        if i % slice == 0:
            answer += 1
    return answer

print(solution(7,10))