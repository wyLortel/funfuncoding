def triangle_area(base , height):
    area = (base * height) / 2
    return area

def rectangle_area(width , height):
    area = (width * height) 
    return area

def diameter(radius):
    area = (3.14 * (radius * radius)) 
    return area

print("[도형 면적 계산기]")
print("1.원 \n2.삼각형 \n3.사각형")
user_menu = int(input("메뉴를 선택하세요:\t"))

# 원의 지름
if user_menu == 1:
    radius = int(input("반지름을 입력하세요:\t"))
    area = diameter(radius)
    print(f"원의 면적은{area}입니다")
    

#삼각형의 지름
elif user_menu == 2:
    base = int(input("밑변을 입력하세요:\t"))
    height = int(input("높이를 입력하세요:\t"))
    area = triangle_area(base , height)
    print(f"삼각형 면적은{area}입니다")

#사각형의 지름
elif user_menu == 3:
    width = int(input("가로를 입력하세요:\t"))
    height = int(input("세로를 입력하세요:\t"))
    area = rectangle_area(width,height)
    print(f"사각형 면적은{area}입니다")

else:
    print("잘못된 숫자 입력입니다")