def solution(numbers):
    answer = 0
    sum = 0
    for i in numbers:
        sum += i
    aver = sum /len(numbers)
    answer = aver
    return answer