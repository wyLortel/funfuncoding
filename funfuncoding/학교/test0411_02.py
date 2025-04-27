#구매금액(정수)
purchase_amount = int(input("총 구매 금액"))

#반품횟수(정수)
return_count = int(input("총 반품 횟수"))

#구매횟수(정수)
purchase_count = int(input("총 구매 횟수"))

#가입 개월수 12개월 이상
membership_months = int(input("가입 개월 수"))

#예외 처리
# → 구매 횟수 == 0이면 오류 메시지를 출력하고 프로그램 종료
if purchase_count == 0:
    print("오류! 구매 횟수가 0입니다. 반품률을 계산 할수없습니다\n프로그램을 종료합니다")

# 반품 횟수 > 구매 횟수이면 오류 메시지를 출력하고 프로그램 종료
elif return_count > purchase_count:
    print("오류! 반품횟수가 구매 횟수보다 많을 수 없습니다\n프로그램을 종료합니다")

else:
    #반품률 계산
    return_count_persent = ((return_count / purchase_count) * 100 )

# 다음 중 하나라고 해당 되면 위험고객
#1 반품률 50퍼 이상
#2 가입개월수가 3개월 이라 구매 금액이 만원 이하
#3 반품 횟수 10회 이상
    if(
        return_count_persent >= 50 or
        (membership_months <= 3 or
        purchase_amount <= 10000) or
        return_count >= 10
    ):
        result = "위험 고객"
        
        
#구매금액 200만원 이상
#반품률 10퍼 이하
#구매 횟수 30회 이상
#가입 개월수 12개월 이상 전부 만족족
    elif(
        purchase_amount >= 2000000 and
        return_count_persent <= 10 and
        membership_months >= 12 and
        purchase_count >= 30
    ):
        result = "우수 고객"
        

#그외 다 일반고객 
    else:
        result = "일반 고객"
    
    #출력력
    print(f"반품률: {round(return_count_persent,1)}%")
    print(f"결과: {result}")