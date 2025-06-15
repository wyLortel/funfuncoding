def solution(n):
    answer = 0
    count = 1
    total = 1
    while True:
        total *= count
        if total == n:
            break
        elif total > n:
            count -= 1
            break
        count += 1
    return count


print(solution(7))
