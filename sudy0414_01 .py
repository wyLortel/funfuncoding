#첫 흐름제어문 수업 
# if True:
#     #if문이 참인 경우
#     #실행 알고리즘
#     print("a")
#     print("b")
    
# #code block



#정수의 정수를 입력받아
# #입력 점수가 0보다 적으면
# #입력 값 오류 를 출력
# user_score = int(input("점수를 입력해주세요: \t"))

# #if문 한개만 사용되엇다 --> 단일 if문
# #최대선택 갯수는1개
# #최소 선택의 갯수는 0 또는 1
# if user_score < 0 :
#     print("입력 값 오류")


# if 조건식:
#     pass
# else:
#     pass


# user_score = int(input("점수를 입력해주세요: \t"))

# if user_score < 0 :
#     print("입력 값 오류")
# # 0보다 크면 합격 여부 판단 
# else:
#     print("합격입니다")

# #홀수 짝수 구분
# bar = 2
# if bar % 2 == 0:
#     print("짝수")
# else :
#     print("홀수")\
    
# if 조건식 1:
#     pass
# elif 조건식 2:
#     pass
# elif 조건식 3: #elif 는 갯수 상관없음
#     pass
# else:
#     pass


# user_score = int(input("점수를 입력해주세요: \t"))

# if user_score < 0:
#     print("입력값 오류 ")
# else :
#     if user_score >= 80 :
#         print("합격 입니다")
#     else:
#         print("불합격 입니다")




user_score = int(input("점수를 입력해주세요: \t"))
if user_score < 0:
    print("입력값 오류 ")
else :
    if user_score > 90:
        grade = "A"
    
    elif user_score > 80:
        grade = "B"
        
    elif user_score > 70:
        grade = "C"

    else :
        grade = "D"


#중첩 IF A등급 이면서 95점이상이면 우수상출력
#추가조건 점수가 100점이면만점 축하 출력

user_score = int(input("점수를 입력해주세요: \t"))

if grade ==  "A" and user_score == 100:
    print("만점 축하!!")
elif grade ==  "A" and user_score <= 95:
    print("우수상!")
