def solution(n):
    count = 0
    for i in range(n):
        if i % 7 == 0:
            count += 1
    return count


print(solution(1))