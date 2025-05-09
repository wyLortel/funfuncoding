#검사할 단어 
my_string = "It is a great weather with you"

#첫번째 단어는 뛰어쓰기가 없으니1부터 시작 
count = 1

#공백일시 단어하나 주가가
for i in my_string:
    if i == " ":
        count += 1

print("문자열 단어 갯수: " , count)