"""
주문 정보 입력 (모두 문자열로 입력 받음)
    음료선택 drink 예) coffee latte juice
    사이즈 선택 size 예) small , medium , large
    멤버쉽 가입 여부 : membership (예: yes or no)
    
음료 기본 가격 설정
    if drink == coffee  -> price  = 3000
    if drink == latte -> price  = 3500
    if drink == coffee -> price  = 4000

사이즈 추가 요금 설정 
    size == medium -> extra_charge = 500
    size == large -> extra_charge = 1000
    size == small -> extra_charge = 0

할인 금액 계산
    if membership == yes
        discount = (기본 가격 + 추가요금 ) * 0.1
    else:
        discount = 0

최종 결제 금액 계산
    final_price = 기본가격 + 추가요금 - 할인 금액

무료샷 제공 여부 확인
    if (drink가 coffee or latt or size == large ) and membership == yes:
        print(무료샷이 제공됩니다)

결과 출력
    기본가격:xxxx원
    크기 추가 요금 : xxxxx원 또는 없음
    할인 적용 : xxxxx원 또는 없음
    최종 결제 금액 xxxx원
    무료샷 메세지 (해당 시)
"""

#주문 정보 입력
drink = input("음료를 선택하세요 (coffee / latte / juice)").lower()
size = input("사이즈를 선택하세요 (small / medium / large)").lower()
membership = input("멤버쉽 가입 여부를 입력하세요 (yes / no)").lower()

base_price = 0
#음료수 기본 가격 설정
if drink == "coffee":
    base_price = 3000
elif drink == "latte":
    base_price = 3500
elif drink == "juice":
    base_price = 4000

extra_charge = 0
# 사이즈 추가 요금 설정
if size == "medium":
    extra_charge = 500
elif size == "large":
    extra_charge = 1000
elif size == "small":
    extra_charge = 0

#할인금액 계산 
if membership == "yes":
    discount = (base_price + extra_charge ) * 0.1
else:
    discount = 0

#최종 결제 금액 계산
final_price = base_price + extra_charge - discount

# 무료샷 제공 여부
if (
    (drink == "coffee" or drink == "latte") and
    size == "large" and
    membership == "yes"
):
    msg = "무료 샷이 제공됩니다"
else:
    msg = ""

#결과출력력
print(f"기본 가격: {base_price}원")
print(f"크기 추가 요금: {extra_charge}원" if extra_charge > 0 else "크기 추가 요금: 없음")
print(f"할인 적용: -{int(discount)}원" if discount > 0 else "할인 적용: 없음")
print(f"최종 결제 금액: {int(final_price)}원")
if msg:
    print(msg)