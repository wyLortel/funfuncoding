# 사용자로부터 메뉴번호를 입력받는다
#사용자에게 값을 받아 해당 도형의 면적을 계산하는 프로그램을 작성한다
#원의 면적 파이 곱하기 반지름 제곱
#삼각형의 면적 밑변 * 높이 /2
#사각형의 면적 가로 * 세오
#조건문만 사용할것

print("[도형 면적 계산기]")
print("1.원 \n2.삼각형 \n3.사각형")
user_menu = int(input("메뉴를 선택하세요:\t"))

# 원의 지름
if user_menu == 1:
    radius = int(input("반지름을 입력하세요:\t"))
    diameter = (radius * radius) * 3.14
    print(f"원의 면적은{diameter}입니다")

#삼각형의 지름
elif user_menu == 2:
    base = int(input("밑변을 입력하세요:\t"))
    height = int(input("높이를 입력하세요:\t"))
    area = (base * height) / 2
    print(f"삼각형 면적은{area}입니다")

#사각형의 지름
elif user_menu == 3:
    width = int(input("가로를 입력하세요:\t"))
    height = int(input("세로를 입력하세요:\t"))
    area = (width * height) / 2
    print(f"사각형 면적은{area}입니다")

else:
    print("잘못된 숫자 입력입니다")




