def solution(n):
    answer = 0
    for i in range(1,100+1):
        if (6 * i) % n == 0:
            answer = i
            break
    return answer