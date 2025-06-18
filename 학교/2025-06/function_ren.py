# def student_score(name, **kwags):
#     print(f"{name}의 성적: ")
#     total = 0
#     for k , v in kwags.items():
#         print(f"{k}의 성적: {v}점")
#         total += v
#     print(f"총점 {total}점")

# student_score("민수" , math = 90 , english = 85 , science = 88)



# def calc_price(product , price , tax = 0.10):
#     tax_price = (price * tax)
#     price += tax_price
#     print(f"{product}의 최종 가격은{price}원 입니다")

# calc_price("노트북" , 1000000)
# calc_price("모니터",300000, tax = 0.05)




def add_numbers(*arg , **kwargs):
    lis = [ "abs" , "only_even" , "unique"]
    
        
    for keys in kwargs:
        if keys not in lis:
            return None
    
    num = list(arg)
    
    if "abs" in kwargs and kwargs["abs"] == True:
        for i in range(len(num)):
            if num[i] < 0:
                num[i] *= -1
    
    if "only_even" in kwargs and kwargs["only_even"] == True:
        num = [even for even in num if even % 2 == 0 ]
        
    if "unique" in kwargs and kwargs["unique"] == True:
        check = []
        for kasane in num:
            if kasane not in check:
                check.append(kasane)
        num = check
    
    total = sum(num)
    
    return total




print(add_numbers(1,-2,2,-3))

print(add_numbers(1,-2,2,-3, abs=True, only_even = True))

print(add_numbers(1,2,3 ,round=True))

