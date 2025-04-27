# 사용자에게 선택지를 보여주고 정수를 입력받아 입력받은 번호의 계산을 실행

    #1번은 원적의 면적 계산 원의 면적 파이(3.14) * 반지름**2
        #사용자에게 반지름을 입력받음
        
    #2번은 삼각형의 면적 계산 (밑변 * 높이) % 2
        #사용자에게 밑변 높이를 받음
                
    #3번은 사각형의 면적 가로 * 세로
        #사용자에게 가로 세로를 입력받음
        

# 사용자에게 선택지를 보여주고 정수를 입력받아 입력받은 번호의 계산을 실행
print("""
도형을 선택하세요
1. 원의 면적을 계산
2. 삼각형의 면적 계산
3. 사각형의 면적 계산
""")

user_choice = int(input())

result = 0

 #1번은 원적의 면적 계산 원의 면적 파이(3.14) * 반지름**2
if user_choice == 1 :
    PIE = 3.14
    r = int(input("반지름을 입력하세요: "))
    result = PIE * (r**2)

 #2번은 삼각형의 면적 계산 (밑변 * 높이) / 2
elif user_choice == 2:
    base = int(input("밑변을 입력하세요: "))
    height = int(input("높이를 입력하세요: "))
    result = (base * height) / 2

#3번은 사각형의 면적 가로 * 세로
elif user_choice == 3:
    width = int(input("가로의 넓이를 입력해주세요: "))
    height = int(input("세로의 넓이를 입력해주세요: "))
    
    result = width * height

else:
    print("잘못된 입력입니다")
    exit()


print(f"원의 면적은 {result}입니다")