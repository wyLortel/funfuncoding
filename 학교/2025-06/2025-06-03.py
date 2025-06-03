user_input = input("문자와 숫자가 섞인 문자열을 입력하세여: ")

print(f"입력 문자열 {user_input}")

num_list = []

for i in user_input:
    if i.isdigit():
        num_list.append(int(i))

print(f"숫자 추출{num_list}")

new_num_list = []

for k in num_list:
    if k % 2 == 0:
        new_num_list.append(1)
    else:
        new_num_list.append(-1)
        
print(f"변환된 리스트{new_num_list}")

fainal_list = []
for start in range(len(new_num_list)):
    total = 0
    for end in range(start ,len(new_num_list)):
        total += new_num_list[end]
        if total == 0:
            fainal_list.append(new_num_list[start:end+1])

print(fainal_list)
