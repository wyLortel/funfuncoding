# 세개의 정수를 사용자로부터 정수로 입력받는다
# 입력받은 3개의 정수의 합을 구한뒤 3으로 나누어 평균을 구한다다 
# 출력한다


user_value1 = int(input("첫번째 정수를 입력하세요"))
user_value2 = int(input("두번째 정수를 입력하세요"))
user_value3 = int(input("세번째 정수를 입력하세요"))

print(f"첫 번째 값: {user_value1} , 타입 {type(user_value1)}")
print(f"두 번째 값: {user_value2} , 타입 {type(user_value2)}")
print(f"세 번째 값: {user_value3} , 타입 {type(user_value3)}")


user_value_sum = user_value1 + user_value2 + user_value3
user_value_aver = user_value_sum / 3
print(round(user_value_aver,2))