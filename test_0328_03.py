#길이를 입력받습니다

#도형을 선택하세요 1번 사각형 , 2번 삼각형

#만약 1번을 선택하려면 사각형의 면적을 출력

#2번을 선택하면 정삼각형의 면적을 출력

#1번,2번이외의 값이 입력될 경우 잘못된 입력입니다

side = int(input("길이를 입력해주세요"))

user_select = int(input("도형을 선택하세요 1번 사각형 , 2번 삼각형"))

if user_select == 1:
    print(f"정사각형의 면적은{side * side}입니다")

elif user_select == 2:
    print(f"정삼각형의 면적은 {side*side/2}입니다")

else:
    print("잘못된 입력입니다.")