import random

# table_num = int(input("테이블 갯수 입력: "))
# row_num = int(input("행 수 입력: "))
# col_num = int(input("열 수 입력: "))

# for table in range(table_num):
#     for rows in range(row_num):
#         for col in range(col_num):
#             print("*" , end="")
#         print()
#     print()
    
    

# table_num = int(input("테이블 갯수 입력: "))
# row_num = int(input("행 수 입력: "))
# col_num = int(input("열 수 입력: "))

# random_num_list = []

# for table in range(table_num):
#     print()
#     print(f"테이블{table+1}")
#     for rows in range(row_num):
#         for col in range(col_num):
#             while True:
#                 random_num = random.randint(1,100)
#                 if random_num not in random_num_list:
#                     random_num_list.append(random_num)
#                     print( random_num, end=" ")
#                     break
#         print()





# #테두리 구현 성공 
# table_num = int(input("테이블 갯수 입력: "))
# row_num = int(input("행 수 입력: "))
# col_num = int(input("열 수 입력: "))

# for table in range(table_num):
#     count = 1
#     for rows in range(row_num):
#         for col in range(col_num):
#             if (rows == 0) or (rows == row_num -1) or (col == 0) or (col == col_num-1):
#                 print(count , end="\t")
#             else:
#                 print("\t" , end="")
#             count += 1
#         print()
#     print()


# 왼쪽 대각선공 성공
# table_num = int(input("테이블 갯수 입력: "))
# row_num = int(input("행 수 입력: "))
# col_num = int(input("열 수 입력: "))

# for table in range(table_num):
#     count = 1
#     for rows in range(row_num):
#         for col in range(col_num):
#             if rows == col:
#                 print(count , end="\t")
#             else:
#                 print("\t" , end="")
#             count += 1
#         print()
#     print()
    


#오른쪽 대각선 구현 완완
# table_num = int(input("테이블 갯수 입력: "))
# row_num = int(input("행 수 입력: "))
# col_num = int(input("열 수 입력: "))

# for table in range(table_num):
#     count = 1
#     for rows in range(row_num):
#         for col in range(col_num):
#             if col == (col_num-1) - rows:
#                 print(count , end="\t")
#             else:
#                 print("\t" , end="")
#             count += 1
#         print()
#     print()


#양쪽 
table_num = int(input("테이블 갯수 입력: "))
row_num = int(input("행 수 입력: "))
col_num = int(input("열 수 입력: "))

for table in range(table_num):
    count = 1
    for rows in range(row_num):
        for col in range(col_num):
            if rows == col or col == (col_num-1) - rows:
                print(count , end="\t")
            else:
                print("\t" , end="")
            count += 1
        print()
    print()