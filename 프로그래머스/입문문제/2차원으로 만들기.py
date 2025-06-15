def solution(num_list, n):
    answer = []
    start = 0
    for i in range(0,len(num_list)+1,n):
        if i == 0:
            continue
        num = num_list[start:i]
        start = i
        answer.append(num)
    return answer

lis = [100, 95, 2, 4, 5, 6, 18, 33, 948]
s = solution(lis,3)

print(s)