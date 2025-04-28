#검사할 문자열 
mystring = "hello hyundai hoho"

#숫자를 세주는 카운트 함수 
count = 0

# 하나하나 문자 확인후 맞으면 카운트 추가
for i in mystring:
    if i == "h":
        count += 1

#출력
print("문자열 내 h 갯수: " , count)