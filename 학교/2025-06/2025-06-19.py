def add_numbers(*args , **kwargs):
    
    arrow_key = ["abs" , "only_even" , "unique"]
    
    if len(kwargs) > len(arrow_key):
        return None
    
    for k in kwargs.keys():
        if k not in arrow_key:
            return None
    
    numbers = list(args)

    if "abs" in kwargs and kwargs["abs"] == True:
        for abs in range(len(numbers)):
            if numbers[abs] < 0 :
                numbers[abs] *= -1
    
    if "only_even" in kwargs and kwargs["only_even"] == True:
        numbers = [i for i in numbers if i % 2 == 0]
    
    if "unique" in kwargs and kwargs["unique"] == True:
        set_lis = []
        
        for setnum in numbers:
            if setnum not in set_lis:
                set_lis.append(setnum)
        
        numbers = set_lis
    
    total = 0
    for s_num in numbers:
        total += s_num
    
    return total



print(add_numbers(1,-2,2,-3))
print(add_numbers(1,-2,2,-3,abs=True,only_even =True))
print(add_numbers(1,2,2,3,3,4,5,5, unique = True))
print(add_numbers(1,2,3,round=True))
