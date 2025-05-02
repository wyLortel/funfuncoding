import random

table_num = int(input("테이블 개수 입력: "))
row_num = int(input("행 수 입력: "))
col_num = int(input("열 수 입력: "))


# def print_star(table_num , row_num , col_num):
#     for i in range(table_num):
#         for _ in range(row_num):
#             for _ in range(col_num):
#                 print("*" , end ="")
#             print()
#         print()

def print_number(table_num , row_num , col_num):
    for i in range(table_num):
        count = 1
        print(f"\n테이블 {i+1}")
        for _ in range(row_num):
            for _ in range(col_num):
                print(count , end="\t")
                count +=1
            print()
        print()


def print_random_number(table_num, row_num, col_num):
    num = []  
    
    for i in range(table_num):
        print(f"\n테이블 {i+1}")
        for _ in range(row_num):
            for k in range(col_num):
                while True:
                    input_num = random.randint(1, 100)
                    if input_num not in num:  
                        num.append(input_num)  
                        print(input_num, end=" ") 
                        break  
            print()  
            

#1번 풀이이
# print_star(table_num , row_num , col_num)





print("""
출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1~100-- 사이 랜덤값 출력""")

user_choice = int(input("옵션 (1 또는 2) : "))


# print_random_number(table_num , row_num , col_num)

if user_choice == 1:
    print_number(table_num , row_num , col_num)
elif user_choice == 2:
    print_random_number(table_num , row_num , col_num)
else:
    print("잘못된 선택입니다")