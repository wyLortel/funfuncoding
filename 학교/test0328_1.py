#정사각형의 면적을 구하시오
#가로 또는 세로의 길이를 입력 받는다
square_side = int(input("정사각형의 가로를 입력해 주세요"))
if square_side <= 0:
    print("양수를 입력하세요")
else:
    print(f"정사각형의 면적은 {square_side*square_side} 입니다")