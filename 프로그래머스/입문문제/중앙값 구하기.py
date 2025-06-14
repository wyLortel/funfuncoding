def solution(array):
    answer = 0
    
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1] , array[j]
    
    index = len(array)//2
    
    answer = array[index]
    
    return answer

lis = [9,-1,0]
s = solution(lis)

print(s)