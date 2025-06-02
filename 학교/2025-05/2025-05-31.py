user_input = input("문자와 숫자가 섞인 문자열을 입력하세요: ")

num_list = [int(i) for i in user_input if i.isdigit()]


new_list = []

for i in num_list:
    if i % 2 == 0:
        new_list.append(1)
    else:
        new_list.append(-1)
        

final_list = []

for start in range(len(new_list)):
    total = 0
    for end in range(start , len(new_list)):
        total += new_list[end]
        if total == 0:
            fianl_list0 = new_list[start:end+1]
            final_list.append(fianl_list0)

print(final_list)

print(f"입력 문자열: {user_input}")
print(f"숫자 추출: {num_list}")
print(f"변환된 리스트: {new_list}")
print("합이 0인 연속 부분 수열 목록 :")

for k in final_list:
    print(k)          