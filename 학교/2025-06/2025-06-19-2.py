# 요구사항
# - 정수 목록은 *args
# - **kwargs 처리
#   - max_only: True이면 최댓값만 출력 (합산 아님)
#   - min_only: True이면 최솟값만 출력 (합산 아님)
#   - sum_all: True이면 전체 합
# - 우선순위: max_only > min_only > sum_all
# - 정의되지 않은 옵션이 오면 None
# - 결과는 print()




def smart_sum (*arg , **kwargs):
    arrow = ["max_only" , "sum_all" , "min_only"]
    
    for key in kwargs.keys():
        if key not in arrow:
            return None
    
    
    if len(kwargs) > len(arrow):
        return None
    
    num = list(arg)
    
    max_num = num[0]
    min_num = num[0]
    total = 0
    
    if "max_only" in kwargs and kwargs["max_only"] == True:
        for max_n in arg:
            if max_n > max_num:
                max_num = max_n
        return max_num
    
    elif "min_only" in kwargs and kwargs["min_only"] == True:
        for min_n in arg:
            if min_n < min_num:
                min_num = min_n
        return min_num
    
    elif "sum_all" in kwargs and kwargs["sum_all"] == True:
        
        for sum_n in arg:
            total += sum_n
        return total
    
        
    




print(smart_sum(1,2,3,4,max_only = True))
print(smart_sum(1,2,3,min_only = True))
print(smart_sum(1,2,3,sum_all = True))
print(smart_sum(1,2,3, max_only= True , sum_all = False))