user_list = []

print("정수 10개를 입력하세요")
for i in range(1,10+1):
    user_num = input(f"{i}번째 정수: ")
    user_list.append(user_num)

print(f"원본 리스트 \n {user_list}")


print(f"1. 처음 5개 원소 \n {user_list[:5]}")
print(f"2. 뒤에서 3개 원소 \n {user_list[-3:]}")
print(f"3. 짝수 인덱스 요소 \n {user_list[::2]}")
print(f"4. 거꾸로 뒤집은 리스트 \n {user_list[::-1]}")
