# for value in range(2):
#     print(value)

# print("------------------------")

# for value in range(3):
#     print(value)

# print("------------------------")

# for value in range(1,2):
#     print(value)

# print("------------------------")

# for value in range(1,3):
#     print(value)

# print("------------------------")

# for value in range(1,11,3):
#     print(value)

# print("------------------------")

# for value in range(10,0,-3):
#     print(value)




# for count in range(9):
#     if count == 8:
#         print(count)
#     else:
#         print(count,end=", ")



# for i in range(5, 15+1):
#     if i % 2 == 0:
#         print("짝수")
#     else:
#         print(i)


# print("---------------------------")


# for i in range(10,0,-1):
#     print(i)


# for i in range(2,9+1,2):
#     for j in range(1,9+1):
#         print(f"{i} * {j} = {i*j}")
#     print(f"---------------{i}단 종료------------------")
    
    
    

word = input("단어를 입력하세요")
count = 0

for i in word :
    count += 1
    if i == " ":
        count -= 1
print(f"입력단어 {word}의 길이는 {count}")



# for i in range(1,3+1):
#     for j in range(1,4+1):
#         print(i,j)

# for dan in range(1,10):
#     for num in range(1,10):
#         print(f"dan : {dan} , num : {num}")


# for i in range(1,5+1):
#     print(i * "*" ,  end="")
#     print()





# for index in range(1, 60):
#     value = str(index)
#     msg = ""

#     for index_char in value:
#         if index_char == "3" or index_char == "6" or index_char == "9":
#             msg += "박수"

#     if msg:  # msg가 비어있지 않으면 (박수친 경우)
#         print(msg)
#     else:
#         print(index)
