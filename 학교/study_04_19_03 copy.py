# msg = "hello"
# print("hello"[::-1])

# sum = 0
# for i in range(1,4+1):
#     sum += i

# print(sum)


list_1 = ["banana", " apple", "orange", "banana", "apple"]

list_2 = []

for i in list_1:
    word = i.strip() 
    if word not in list_2:
        list_2.append(word)

list_2.sort()  
print(list_2)


