import random

#랜덤 변수 받음
random_number = random.randint(1,100)

#실행
while True:
    #사용자 입력
    user_input_num = int(input("1부터 100까지의 숫자를 맞춰보세요"))
    
    # 만약 범위를 벋어나면 다시 입력받기
    if not 0 < user_input_num <= 100:
        print("잘못된 입력입니다")
        continue
    
    #정답 오답 구분
    if random_number == user_input_num:
        print("정답입니다")
        break
    else :
        if user_input_num < random_number:
            print("더 큰 숫자입니다")
        elif user_input_num > random_number:
            print("더 작은 숫자입니다")