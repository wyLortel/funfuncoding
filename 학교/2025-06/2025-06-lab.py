# def print_hello():
#     return print("hello world!")

# print_hello()

# def sum_numbers(a,b):
#     return a+b

# print(sum_numbers(3,5))

# def greet_user(name):
#     print(f"hello {name}")
    
# greet_user("Alice")

# def max_of_three(a,b,c):
#     max_num = a
#     max_lis = [a,b,c]
#     for i in max_lis:
#         if i > max_num:
#             max_num = i
#     return max_num

# print(max_of_three(10,20,15))


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))
# print(is_even(5))

# def wrap_in_tag(str1,str2):
#     return f"<{str1}>{str2}</{str1}>"

# print(wrap_in_tag("p" , "hello"))
# print(wrap_in_tag("b" , "world "))


# def contains(array,num):
#     for i in array:
#         if i == num:
#             return True
#     else:
#         return False

# print(contains([1,2,3,4],3))
# print(contains([1,2,3,4],8))


# def calculate_average(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(f"""
#     입력 개수 : {len(args)}
#     총합 : {sum}
#     평균 : {sum /len(args) }
#     """)

# calculate_average(70,80,90)

# def calculate_average(*args):
#     s = 0
#     for i in args:
#         s += i
    
#     n = len(args)
    
#     avg = s / n
    
#     return s , n , avg

# s ,n , avg = calculate_average(70,80,90)

# print(f"""
# 입력 개수 : {n}
# 총합 : {s}
# 평균 : {avg }
# """)


# def calc_price (product , price , tax = 0.10):
#     tax_price = price * tax
#     return print(f"{product}의 최종 가격은 {int(price + tax_price)}원 입니다 ")

# calc_price("노트북" , 1000000)
# calc_price("노트북" , 300000 , tax=0.05)

# def add_numbers(*args , **kwargs):
#     arrow = ["abs" , "only_even" , "unique"]
    
#     if len(kwargs) > len(arrow):
#         return 
    
#     for key in kwargs.keys():
#         if key not in arrow:
#             return
    
#     numbers = list(args)
    
#     if "abs" in kwargs and kwargs["abs"] == True:
#         for abs in range(len(numbers)):
#             if numbers[abs] < 0:
#                 numbers[abs] *= -1
    
#     if "only_even" in kwargs and kwargs["only_even"] == True:
#         numbers = [i for i in numbers if i % 2 == 0]

#     if "unique" in kwargs and kwargs["unique"] == True:
#         unique_lis = []
#         for unique_num in numbers:
#             if unique_num not in unique_lis:
#                 unique_lis.append(unique_num)

#         numbers = unique_lis
    
#     total = 0
    
#     for sum_num in numbers:
#         total += sum_num
        
    
#     return print(f"출력 합계는 {total}입니다")
    

# add_numbers(1,-2,2,-3)
# add_numbers(1,-2,2,-3, abs = True , only_even = True)
# add_numbers(1,2,2,3,3,4,5, unique = True)
# add_numbers(1,2,3,round = True)

def genetate_profile (name , age , *args , gender = "미정" , **kwargs):
    print(f"""
    출력 :
    [고객 프로필]
    이름 : {name}
    나이 : {age}
    성별 : {gender}
          """)
    if args:
        print("관심사:" , end="")
        for hobby in args:
            if hobby == args[-1]:
                print(hobby)
            else:
                print(hobby ,end=",")
        print()
    
    if kwargs:
        print("추가정보:" , end=" ")
        for k , v in kwargs.items():
            print(f"{k} = {v}" ,end=" ")
        print()
    
    

genetate_profile("홍길동" , 30)
genetate_profile("지민" , 26 , *["여행","사진","독서"], gender="여성" , job = "디자이너" , country = "한국")