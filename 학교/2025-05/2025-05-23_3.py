user_input = input("입력 문자열: ")

number_list = []

for i in user_input:
    if i.isdigit():
        number_list.append(int(i))

print("숫자 추출:", number_list)

password_list = []

for j in range(len(number_list)):
    if j % 2 == 0:
        password_list.append(1)
    else:
        password_list.append(-1)


print("변환된 리스트 (+1 / -1):", password_list)

# 합이 0인 연속 부분 수열 찾기
print("합이 0인 연속 부분 수열:")
for row in range(len(password_list)):
    for col in range(row+1, len(password_list)+1):
        if sum(password_list[row:col]) == 0:
            print(password_list[row:col])
