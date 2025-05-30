# def bar(msg1 , msg2):
#     print(msg1 , msg2)
    
    
# bar("hello" , "siri")



# def bar(value1 , value2):
#     sum = value1 + value2
#     avg = sum / 2
    
#     return sum , avg


# value = bar(1,3)
# print(value,type(value))


# print(id(value[0]))
# print(id(value[1]))
# print(id(value))


def calculate (a,b):
    sum_val = a + b
    avg_val = sum_val / 2
    return sum_val , avg_val , 10

result = calculate(10 , 20)
print(f"튜플 반환 {result}")
print(f"합{result[0]}")
print(f"평균{result[1]}")