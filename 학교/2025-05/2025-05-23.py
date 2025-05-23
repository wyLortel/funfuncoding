import random

random_num = int(input("난수 개수를 입력하세요"))   #랜덤 난수 개수입력
start_num = int(input("시작 범위를 입력하세요"))    #시작 범위 입력
end_num = int(input("끝 범위를 입력하세요"))    #끝 범위 입력



rand_list = [random.randint(start_num, end_num) for _ in range(random_num)] # 랜덤난수로 리스트를 만듬 


unique_list = []
freq_list = []

for num in rand_list:
    flag = False 
    for i in range(len(unique_list)):
        if unique_list[i] == num:
            freq_list[i] += 1
            flag = True
            break
    if not flag:
        unique_list.append(num)
        freq_list.append(1)


print(rand_list)

print("고유 숫자 리스트:", unique_list)
print("빈도 수 리스트:", freq_list)

print("\n가장 많이 등장한 숫자 Top 3 (동점 포함):")
# (숫자, 빈도수) 쌍으로 만들기
pairs = []
for i in range(len(unique_list)):
    pairs.append([unique_list[i], freq_list[i]])

# 빈도 기준으로 내림차순 정렬
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[i][1] < pairs[j][1]:
            pairs[i], pairs[j] = pairs[j], pairs[i]

# Top 3 동점 포함 출력
top_count = 0
used_freq = []
for i in range(len(pairs)):
    if pairs[i][1] in used_freq:
        continue
    used_freq.append(pairs[i][1])
    for p in pairs:
        if p[1] == pairs[i][1]:
            print(f"{p[0]} → {p[1]}회")
    top_count += 1
    if top_count == 3:
        break