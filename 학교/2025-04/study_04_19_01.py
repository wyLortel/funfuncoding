"""
사용자로부터 정수 5개 입력받기
합계 계산
평균 계산
결과 출력
"""


#사용자로부터 정수 5개 입력받기
user_number1 = int(input("첫번째 정수를 입력해주세요 :"))
user_number2 = int(input("두번째 정수를 입력해주세요: "))
user_number3 = int(input("세번째 정수를 입력해주세요 :"))
user_number4 = int(input("네번째 정수를 입력해주세요 :"))
user_number5 = int(input("다섯번째 정수를 입력해주세요 :"))

#합계 계산
sum = user_number1 + user_number2 + user_number3 + user_number4 + user_number5

# 평균 계산
average = sum / 5

# 출력
print(f"합계{sum}")
print(f"평균{average}")

