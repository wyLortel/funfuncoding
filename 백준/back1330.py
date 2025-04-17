#1. 사용자에게 값을 입력받음
#2. 만약 a 보다 b 가 크면 > 출력
#3. #만약 a 보다 b 가 작으면 < 출력
#4. #만약 A와 B가 같은 경우에는 '=='를 출력한다.

a = int(input("a"))
b = int(input("b"))
if a < b :
    print(">")
elif a > b :
    print("<")
else:
    print("==")