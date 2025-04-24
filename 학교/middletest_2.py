"""
사용자에게 상품 가격을 입력받음
조건에 따라 할인율 적용
    10만원 이상 구매시 10퍼센트 할인
    5만원 이상 10만원 미만 구매시 5퍼센트 할인
    5만원 미만 구매시 할인 없음
할인율 할인 금액 최종결제금액 출력
"""
product_price = int(input("상품가격을 입력해주세요: "))

if product_price >= 100_000:
    discount = 0.1

elif product_price >= 50_000:
    discount = 0.05

else:
    discount = 0

discount_rate = discount * 100
discount_price = product_price * discount
final_price = product_price - discount_price

print(f"""
할인율: {int(discount_rate)}%
할인금액: {int(discount_price)}원
최종 결제 금액: {int(final_price)}원
"""
)



