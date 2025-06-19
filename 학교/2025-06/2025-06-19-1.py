def selective_sum (*args , **kwargs):
    check = ["pos" , "neg" , "odd" , "even"]
    
    if len(kwargs) > len(check):
        return
    
    for k in kwargs.keys():
        if k not in check:
            return
    
    
    
    numbers = list(args)
    
    if "pos" in kwargs and kwargs["pos"] == True:
        numbers = [i for i in numbers if i > 0]
    
    if "neg" in kwargs and kwargs["neg"] == True:
        numbers = [i for i in numbers if i < 0]
    
    
    if "even" in kwargs and kwargs["even"] == True:
        numbers = [i for i in numbers if i % 2 == 0]
        
    if "odd" in kwargs and kwargs["odd"] == True:
        numbers = [i for i in numbers if i % 2 != 0]
    
    
    return sum(numbers)

print(selective_sum(1, -2, 3, 4, -5, odd=True))       # 1+3+(-5) = -1
# print(selective_sum(1, -2, 3, 4, -5, even=True, pos=True))  # 4
# print(selective_sum(1, 2, 3, 4, foo=True))            # None
