# #1

# def print_hello():
#     print("hello, wordld")

# print_hello()


##2

# def sum_numbers(a,b):
#     sum = a+b
#     return sum

# print(sum_numbers(3,5))


#3
# def greet_user(name):
#     print(f"hello,{name}!")
    
# greet_user("Alice")

#4
# def max_of_three(a,b,c):
#     max = 0
#     lis = [a,b,c]
#     for i in lis:
#         if max < i:
#             max = i
#     print(max)

# max_of_three(10,20,15)


# #5
# def is_even(a):
#     if a % 2 == 0:
#         print("True")
#     else:
#         print("False")
        
# is_even(4)


# #6
# def wrap_in_tag(str1,str2):
#     string = f"<{str1}>{str2}</{str1}>"

#     return string

# print(wrap_in_tag("p","hello"))


# #7
# def contains(array,int):
#     for i in array:
#         if i == int:
#             print("True")
#             break
#     else:
#         print("false")

# contains([1,2,3,4,],7)


#8
# def calculate_average(*arg):
#     n = len(arg)
#     total = sum(arg)
#     aver = total/n
    
#     print(n)
#     print(total)
#     print(aver)
    
# calculate_average(70,80,90)


#9
# def student_score(name , **kwargs):
#     total = sum(kwargs.values())
#     print(f"{name}의 성적: ")
#     for k, v in kwargs.items():
#         print(f"{k}: {v}점")
#     print(f"총점: {total}점")



# student_score("민수", math=90 , english=85, science = 88)

#10
# def calc_price(product,price,tax=0.1):
#     tax = price * tax
#     price = price + tax
#     print(f"{product}의 최종 가격은{int(price)}원입니다")

# calc_price("노트북",300000,tax=0.05)

#11 // 다시풀어보기
def add_numbers(*args, **kwargs):
    allowed_keys = {"abs", "only_even", "unique"}
    for key in kwargs:
        if key not in allowed_keys:
            return None  

    numbers = list(args)


    if kwargs.get("abs", False):
        numbers = [abs(i) for i in numbers]


    if kwargs.get("only_even", False):
        numbers = [i for i in numbers if i % 2 == 0]

    
    if kwargs.get("unique", False):
        unique_numbers = []
        for i in numbers:
            if i not in unique_numbers:
                unique_numbers.append(i)
        numbers = unique_numbers 

    total = sum(numbers)
    print(f"합계는 {total}입니다.")

    
add_numbers(1, 2, 2, 3, 4, unique=True)

add_numbers(1, -2, 2, -3, abs=True, only_even=True)


add_numbers(1, 2, 3, round=True)    