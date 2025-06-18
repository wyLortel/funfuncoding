def add_numbers (*args , **kwargs):
    
    check = ["abs" , "only_even" , "unique"]
    
    if len(kwargs) > len(check):
        return None
    
    for k in kwargs.keys():
        if k not in check:
            return None
    
    
    value = list(args)
    
    if "abs" in kwargs and kwargs["abs"] == True:
        for abs in range(len(value)):
            if value[abs] < 0 :
                value[abs] *= -1
    
    if "only_even" in kwargs and kwargs["only_even"] == True:
        value = [even for even in value if even % 2 == 0 ]
    
    if "unique" in kwargs and kwargs["unique"] == True :
        kasane = []
        for i in value:
            if i not in kasane:
                kasane.append(i)
        value = kasane
    
    
    total = sum(value)
    
    return total



print(add_numbers(1,-2,2,-3))
print(add_numbers(1,-2,2,-3,abs=True, only_even = True ))
print(add_numbers(1,2,2,3,3,4,5, unique = True))
print(add_numbers(1,2,3, round=True))