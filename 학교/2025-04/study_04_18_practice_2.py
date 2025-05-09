# 사용자에게 2 부터 9 사이의 정수를 입력받는다
# 2- 9사이의 정수가 아닌경우 프로그램 종료
#결과 중 곱하는 수가 짝수인 경우만출력한다

gugudan = int(input("출력할 단을 입력하세요"))

if  2 <= gugudan <= 9 :
    for i in range(2,9+1,2):
        print(f"{gugudan} * {i} = {gugudan * i}")
    
#오류 
else:
    print("오류 : 2단부터 9단까지만 입력 가능합니다")