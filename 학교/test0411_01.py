# if 3 < 2 and 3 < 3: and 문은 앞에서 부터 검사해서 앞에것이 거짓일 경우 바로 다음것은 검사안함 어차피 거짓이기 때문에 
#     print("T 1") 
    
# if 3 > 2 and 3 < 3:
#     print("T 2") 
    

# if 3 < 2 and 3  >= 3:
#     print("T 3") 

# if 3 > 2 and 3 >= 3:
#     print("T 4")

# if 1 and 0:
#     print("true")

# if 3 < 2 or 3 < 3:
#     print("T 1")

# if 3 > 2 or 3 < 3:
#     print("T 2")

# if 3 < 2 or 3 >= 3:
#     print("T 3")

# if 3 > 2 or 3 >= 3:
#     print("T 4")

# if not (2 > 3):
#     print("T 1")
# else:
#     print("F 1")

# if not (2 < 3):
#     print("T 1")
# else:
#     print("F 2")

# def returnNum(argNum):
#     print("arg: " , argNum , "\treturnNum() is invoked")
#     return argNum

# returnNum(1)

# if True and returnNum(2) == 2:
#     print("True")

# if False and returnNum(3) ==2:
#     print("True")

# if False or returnNum(4) ==4:
#     print("True")
    
# if False or returnNum(5) ==4:
#     print("True")

# value = 1

# value += 1
# print(value)

# value *= 3
# print(value)

# value /= 3
# print(value)

# value **= 10
# print(value)

# value //= 1000
# print(value)

# bar, foo , pos = 1 , 2, 3

# print(bar , foo , pos)

# bar = foo = pos = kin = 2
# print(bar , foo , pos , kin)


result = "참" if 3 > 2 else "거짓"
print(result)