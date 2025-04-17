# 고객 정보 입력 (모든 정수로 입력받음)
    #total_purchase : 총 구매 금액 (원)
    #return_count : 총 반품 횟수 (회)
    #purchase_count : 총 구매 횟구 (회)
    #join_months : 가입 개월 수 (개월)
    
# 예외 처리 
#    #purchase_count <= 0:
#        구매 횟수가 0 이하면 잘못된 입력 -> 프로그램 종료
#    #return_count > producet_count:
#        반품 횟수가 구매횟수를 초과하면 잘못된 입력 -> 프로그램 종료

#반품률 계산
    #return_rate = (return_count / purchase_count) * 100

"""
고객 분류 조건
    위험 고객 (다음 중 하나라도 해당하면 위험 고객)
        반품률이 50% 이상인 경우
            return_rate >= 50
        가입 개월수가 3개월 이하고 총 구매 금액이 10_000원 이상 
            join_ months <= 3 and total_purchase <= 10_000
        반품 횟수가 10회 이상인 경우 
            return_count >= 10
        
    우수고객 (모든 조건을 동시에 만족해야함)
        총 구매 금액이 2_000_000원 이상
            total_purchase >= 2_000_000
        반품률이 10퍼 이하
            return_rate <= 10
        총 구매 횟수가 30회 이상
            purchase_count >= 30
        가입 개월수가 12개월 이상
            join_ months >= 12
    
    일반 고객 
        위 두 조건을 만족하지않으면 일반고객
    
    결과 출력 
        반품률: xxxxx%
        고객등급 : 위험 고객 / 우수고객 / 일반 고객중 하나 출력
"""

# 고객 정보 입력 (모든 정수로 입력받음)
total_purchase = int(input("총 구매 금액 :"))
return_count = int(input("총 반품 횟수 :"))
purchase_count = int(input("총 구매 횟수 :"))
join_months = int(input("가입 개월 수 :"))

# 예외 처리 
if purchase_count <= 0:
    print("오류 : 구매 횟수가 0입니다. 반품률을 계산 할수 없습니다")
elif return_count > purchase_count :
    print("오류 : 반품 횟수가 구매 횟수보다 많을수 없습니다 ")
else:
    #반품률 계산
    return_rate = (return_count / purchase_count) * 100
    
    grade = ""

    #고객 분류 
    
    #위험 고객 
    if (
        return_rate >= 50 or
        (join_months <= 3 and total_purchase <= 10_000) or
        return_count >= 10
    ):
        grade = "위험 고객"
    
    #우수고객
    elif (
        total_purchase >= 2_000_000 and
        return_rate <= 10 and
        purchase_count >= 30 and
        join_months >= 12
    ):
        grade = "우수 고객"
    
    else:
        grade = "일반 고객"
    
    #결과 출력 
    print(f"반품률 : {return_rate:.1f}%")
    print(f"고객 등급: {grade}")