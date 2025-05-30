# def bar ():
#     for _ in range(5):  #실행되는 알고리즘 선언 
#         print("hello world")


def bar():
    foo = 2
    
    if foo < 0:
        return 
    
    if foo == 1:
        return 1
    else:
        return 2


def get_input_num():
    msg = "정수를 입력하세요: "
    input_value = int(input(msg))
    
    if input_value < 0:
        print("o과 양의 정수만 입력하세여")
        return
    
    return input_value


# values = [get_input_num() for _ in range(3)]
# print(values)

print(get_input_num())

