# # 입력값 받기 
input_value = int(input("입력값:\t"))

# #입력값이 3의 배수 이면 3의 배수
# if input_value % 3 ==0 or input_value % 4 == 0:
#     print(f"{input_value}의 배수입니다")
# #입력값이 4의 배수이면 4의 배수
# # 그외 출력 안함함
# # else:
# #     print("")



if input_value % 3 == 0:
    print("3의 배수입니다")

if input_value % 4 == 0:
    print("4의 배수입니다")
    
