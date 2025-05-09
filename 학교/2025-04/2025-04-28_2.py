# 카운트 함수
i = 1

# 합계를 담을 함수
sum = 0

# 실행  3의 배수만 합계 계산
while i < 1000:
    if i % 3 == 0:
        sum += i

    i += 1

print(sum)