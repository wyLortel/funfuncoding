# 입력 : 사용자로부터 상품 가격을 정수로 입력

#조건에 따라 할인율을 결정 
#만약 입력 금액이 100,000원이상이면 10퍼센트 할인
#그렇지 않고 입력 금액이 50,000원 이상이면 5%할인
#그렇지 않으면 할인없음(0%)

#할인 금액을 계산 
#할인 금액 = 상품 가격 * 할인율

#최종결제 금액을 계산
#최종 결제 금액 = 상품가격 - 할인 가격 

# 계산 결과를 출력
# 출력 내용:
#-할인율 : xx%
# -할인 금액 : xxx원
# -최종결제 금약 : xxxxx원







# 입력 : 사용자로부터 상품 가격을 정수로 입력
product_price = int(input("상품 가격을 입력하세요 (원): "))

#조건에 따라 할인율을 결정 
#만약 입력 금액이 100,000원이상이면 10퍼센트 할인
#그렇지 않고 입력 금액이 50,000원 이상이면 5%할인
#그렇지 않으면 할인없음(0%)
discount_rate = 0

if product_price >= 100_000 :
    discount_rate = 0.10
elif product_price >= 50_000 :
    discount_rate = 0.05
else:
    discount_rate = 0.00

#할인 금액을 계산 
discount_price = product_price * discount_rate

#최종결제 금액을 계산
final_price = product_price - discount_price

#계산결과 출력
print(f"할인율: {int(discount_rate * 100)}%")
print(f"할인금액:{int(discount_price)}원")
print(f"최종 결제 금액:{int(final_price)}원")