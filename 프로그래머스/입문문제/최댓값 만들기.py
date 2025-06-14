def solution(numbers):
    
    for i in range(len(numbers)):
        for k in range(len(numbers)-1):
            if numbers[k] > numbers[k+1]:
                numbers[k] ,numbers[k+1] = numbers[k+1], numbers[k]
    
    num = len(numbers)
    mzx_num = numbers[-1] * numbers[-2]
    
    return mzx_num
    
