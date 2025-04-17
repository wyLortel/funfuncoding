# 1 입력값 받기기 
# 음료 , 크기 , 멤버십 여부 입력 (모두 소문자로)

# 2 처리 설정정
# 1. 음료 기본 가격 결정
# 2. 크기별 추가 요금계산
# 3.기본 + 추가 요금계산
# 4.멤어십 고객이면 10% 할인 적용
# 5. 멤버쉽 고객이면서 커피/라떼 라지사이즈일 경우 무료 샷 제공

# 3 출력력
# 기본가격 ,추가요금 , 할인여부
# 최종 결제 금액
# 해당될 경우 무료샷 메시지

# 1
user_drink = input("음료를 선택하세요 (coffee / latte / juice): ").strip()
user_drink_size = input("크기를 선택하세요 (small / medium / large): ").strip()
user_membership_check = input("멤버쉽인가요? (yes / no ): ").strip()

user_p_price = 0
default_price = 0
drink_size_price = 0
membership_price = 0

# 2-1
if user_drink == "coffee":
    default_price = 3000
elif user_drink == "latte":
    default_price = 4000
elif user_drink == "juice":
    default_price = 3500

user_p_price += default_price

# 2-2
if user_drink_size == "large":
    drink_size_price = 1000
elif user_drink_size == "medium":
    drink_size_price = 500
else:
    print("잘못된 크기 선택입니다.")

user_p_price += drink_size_price


# 결과 출력
print(f"기본 가격 : {int(default_price)}원")
print(f"크기 추가 요금 : {int(drink_size_price)}원")

#멤버쉽 할인인
if user_membership_check == "yes":
    membership_price = user_p_price * 0.1
    user_p_price -= membership_price
    print(f"할인 가격 = -{int(membership_price)}원")
else:
    print("없음")

print(f"최종 결제 : {int(user_p_price)}원")

# 추가 혜택
if user_membership_check == "yes" and user_drink_size == "large":
    print("무료 샷 추가!")
