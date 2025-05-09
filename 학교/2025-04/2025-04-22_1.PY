# for i in range(1,100 +1):
#     if i % 2 != 0:
#         print(i)


# num = int(input("숫자를 입력"))

# while num > 0:
#     digit = num % 10
#     print(digit , end="")
#     num = num // 10


low = 5

for i in range(1,low+1):
    print(" " * (low-i) , end="")
    print( "*" * ((i * 2) - 1))