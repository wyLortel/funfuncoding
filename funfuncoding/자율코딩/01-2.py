"""
사용자에게 세 변의 길이를 입력받음
만약 두변의 길이의 합이 나머지 한변의 길이보다 작거나 같다면 , 삼각형을 형성 할수없음

만약 세변의 길이가 같으면 정삼각형 
세변중 두변의 길이가 같다면 이등변 삼각형
어느 두변의 길이 합이 나머지 한변의 길이보다 작거나 같다면 삼각형을 형성할수없음
"""

# # 사용자에게 세 변의 길이를 입력받기기
# user_num1 = int(input("첫 번째 변의 길이를 입력하세요"))
# user_num2 = int(input("두 번째 변의 길이를 입력하세요"))
# user_num3 = int(input("세 번째 변의 길이를 입력하세요"))

# #삼각형을 형성할수잇나 확인
# if (
#     (user_num1 + user_num2 <= user_num3) or
#     (user_num1 + user_num3 <= user_num2) or
#     (user_num2 + user_num3 <= user_num1)
# ):
#     print("삼각형을 만들기 위해서는 어떤 두변의 길이의 합이 다른 한 변의 길이보다 커야합니다")
#     exit()

# result = ""

# if user_num1 == user_num2 == user_num3 :
#     result = "정삼각형"
# elif (
#     (user_num1 == user_num2) or
#     (user_num1 == user_num3) or
#     (user_num2 == user_num3)
# ):
#     result = "이등변 삼각형"
# else:
#     result = "부등변 삼각형"
    
# #출력
# print(f"입력하신 변의 길이로는 {result}를 만들수 있습니다.")


#삼각형 가능 여부
def is_triangle(a ,b ,c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# 삼각형 판별별
def triangle_type(a,b,c):
    if a == b == c:
        return "정삼각형"
    elif a == b or a == c or b == c:
        return "이등변 삼각형" 
    else:
        return "부등변 삼각형"

#사용자 입력
user_num1 = int(input("첫 번째 변의 길이를 입력하세요"))
user_num2 = int(input("두 번째 변의 길이를 입력하세요"))
user_num3 = int(input("세 번째 변의 길이를 입력하세요"))

#유효성 검사
if not is_triangle(user_num1 , user_num2 ,user_num3):
    print("삼각형을 만들기 위해서는 어떤 두변의 길이의 합이 다른 한 변의 길이보다 커야합니다")
else:
    result = triangle_type(user_num1 , user_num2 , user_num3)
    print(f"입력하신 변의 길이로는 {result}를 만들수 있습니다.")