# is_valid = False

# while not is_valid:
#     input_value = int(input("정수입력"))

#     if input_value > 0:
#         is_valid = True
#     else:
#         print("양의 정수를 입력하세영")

# while True:
#     input_value = int(input("정수 입력"))
    
    
#     #양의 정수인 경우 , 반복 종료
#     if input_value > 0:
#         break
    
#     print("양의 정수를 입력하세요")
        
        

# for value_1 in range(2):
#     for value_2 in range(2):
#         for value_3 in range(2):
#             print(f"{value_1} {value_2} {value_3}\t" , end="")
            
#             print()
#         print()         

for value_1 in range(2):
    for value_2 in range(2):
        
        for value_3 in range(2):
            if value_3 == 1:
                break
            print(f"{value_1} {value_2} {value_3}\t" , end="")
            
            print()
        print()        