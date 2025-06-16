def solution(numbers, k):
    index = 0
    for _ in range(k - 1):
        index += 2
        index %= len(numbers)
    return numbers[index]


lis = [1, 2, 3, 4]
print(solution(lis,2))
    