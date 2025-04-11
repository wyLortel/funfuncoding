#사용자에게 구매한 상품 가격을 입력받음
#조건에 맞추어 할인율을 적용
#10만원 이상 구매 0.1할인
# 5만원이상10만원 미만0.5
# 5만원 미안 할인없음음
#최종출력

#사용자에게 구매한 상품 가격을 입력받음
user_price = int(input("상품 가격을 입력하세요: "))

#조건에 맞추어 할인율을 적용
#10만원 이상 구매 10퍼퍼할인
if user_price >= 100000:
    sale = 10

# 5만원이상10만원 미만 5 퍼퍼
elif user_price >= 50000:
    sale = 5

# 5만원 미안 할인없음
else:
    sale = 0

sale_price = int(user_price * (sale / 100))
final_price = user_price - sale_price

#최종출력
print(f"할인율: {sale}%")
print(f"할인 금액: {sale_price}원")
print(f"최종 금액: {final_price}원")

