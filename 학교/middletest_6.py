"""
음료 크기 멤버쉽 여부 입력 (모두 소문자)

처리
음료 기본 가격 설정
크기별 추가 요금 계산
기본 추가 요금 계산  
멤버십 고객이면 10% 할인 적용
5.(중첩 if) 멤버십 고객이면서 커피 라떼 라지일 경우 무료샷 제공  

출력
기본가격 추가요금 할인여부
최종결제 금액
(해당될경우) 무료 샷 메세지
"""

user_drink = input("음료를 선택하세요 (coffee / latte / juice): ").lower()
user_drink_size = input("크기를 선택하세요 (small / medium / large): ").lower()
user_membership_check = input("멤버쉽인가요? (yes / no) : yes ").lower()


#기본 가격 설정정
default_price = 0

if user_drink == "coffee":
    default_price = 3000
    
elif user_drink == "latte":
    default_price = 4000

elif user_drink == "juice":
    default_price = 3500
    

# 크기 추가 요금
size_price = 0

if user_drink_size == "small":
    size_price = 0
elif user_drink_size == "medium":
    size_price = 500
elif user_drink_size == "large":
    size_price = 1000

#멤버쉽 헤택

membership_discount = 0

if user_membership_check == "yes":
    membership_discount = (default_price + size_price) * 0.1
else:
    membership_discount = 0

final_price = default_price + size_price - membership_discount

print(f"""
기본 가격: {default_price}원
크기 추가 요금: {size_price}원
최종 결제 금액: {final_price}원
""")
print("할인 적용: -{membership_discount}원" if membership_discount < 0 else "크기 추가 요금 없음")


if user_membership_check == "yes" and (user_drink == "coffee" or user_drink == "latte"):
    print("무료샷이 적용됩니다")


