def solution(array, n):
    answer = 0
    
    lis = []
    
    for i in array:
        lis.append(n-i)
    
    for i in range(len(lis)):
        if lis[i] < 0:
            lis[i] = lis[i] * -1
    
    min = lis[0]
    min_index = 0
    
    for k in range(len(lis)):
        if lis[k] < min:
            min = lis[k]
            min_index = k
        elif lis[k] == min:
            if array[k] < array[min_index]: 
                min_index = k


    answer = array[min_index]
    
    return answer


lis = [3, 10, 28]
print(solution(lis,20))