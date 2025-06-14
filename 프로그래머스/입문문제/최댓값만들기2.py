def solution(numbers):
    max_num = numbers[0] * numbers[1]
    
    for i in range(len(numbers)):
        for k in range(i+1,len(numbers)):
            m_num = numbers[i] * numbers[k]
            if m_num >= max_num:
                max_num = m_num
    return max_num


lis = [1, 2, -3, 4, -5]

s = solution(lis)

print(s)