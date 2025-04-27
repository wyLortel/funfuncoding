"""
총 구매 금액
반품횟수
구매횟수
가입개월 수를 입력받음

구매횟수가 0이면 반품률 계산 불가 오류메세지 출력후 프로그램 종료
반품횟수가 구매횟수보다 크면 오류메세지 출력후 프로그램 종료료


고객등급 분류
    위험 고객 다음조건 중 하나
        반품률 >= 50
        가입 개월수 3개월이하 그리고 구매금액 10_000이하
        반품횟수 10회 이상
    
    우수고객 다음 조건 모두 만족
        구매 금액 200만원 이상
        반품율 <= 10
        구매횟수 >= 30
        가입개월수 >= 12
    
    그외 일반고객
    
"""

# 입력값 받기
purchase_price = int(input("총 구매금액: "))
return_num = int(input("총 반품횟수"))
purchase_num = int(input("총 구매횟수"))
signup_month = int(input("가입 개월 수: "))


#예외 처리
if purchase_num <= 0:
    print("오류 구매횟수가 0입니다 반품률을 계산할수 없습니다 \n 프로그램을 종료합니다")
    exit()

if return_num > purchase_num:
    print("오류: 반품 횟수가 구매 횟수보다 많을수 없습니다 \n 프로그램을 종료합니다 ")
    exit()

# 반품률 계산
return_percent = (return_num / purchase_num) * 100


# 고객 분류
grade = ""

# 위험 고객 
if (
    return_percent >= 50 or
    (signup_month <= 3 and purchase_price <= 10_000 or
    return_num >= 10)
):
    grade = "위험 고객"

#우수 고객
elif(
    purchase_price >= 200_000_0 and
    return_percent <= 10 and
    purchase_num >= 30 and
    signup_month >= 12
):
    grade = "우수 고객"

#일반고객
else:
    grade = "일반 고객"
    

#출력
print(f"""
반품률: {return_percent:.1f}%
결과: {grade}
""")