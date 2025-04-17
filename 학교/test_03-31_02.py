# 두개의 수를 사용자에게 입력받는다 하나는 정수 하나는 실수
#두수의 차를 자료형과 같이 출력한다
#왜 자료형이 float인지 확인하고 이해한다

user_value1 = int(input("정수를 입력해주세요"))
user_value2 = float(input("실수를 입력해주세요"))

#테스트 코드
# print(f"첫번째 입력받은 수는{user_value1} 타입은{type(user_value1)}")
# print(f"두번째 입력받은 수는{user_value2} 타입은{type(user_value2)}")


user_value_result = user_value1 - user_value2
print(f"두수의 차는 {user_value_result}입니다 타입형은{type(user_value_result)}입니다")
# 왜 결과의 타입은 float일까?
# 자료형끼리 연산을 할 때는 보통 두 자료형이 같아야 한다.
# 하지만 int와 float은 서로 다른 숫자형이다.
# 여기서 int형과 float형을 함께 연산할 경우 묵시적 형변환이 일어난다다
# 자동으로 int가 float으로 변환
# 이는 float형이 int형보다 더 넓은 표현 범위를 가지기 때문에
# 더 정밀한 결과를 보장하기 위해 연산 결과로 float형이 사용되는 것이다.
