import random

random_num = int(input("난수를입력하세요"))
start_num = int(input("시작 범위를 입력하세요"))
end_num = int(input("끝 범위를 입력하세요"))

rand_list = [random.randint(start_num,end_num) for _ in range(random_num)]

print(rand_list)

uniqe_num = []
hidou_list = []

for num in rand_list:
    flag = False
    for i in range(len(uniqe_num)):
        if uniqe_num[i] == num:
            hidou_list[i] += 1
            flag = True
            break
    if not flag:
        uniqe_num.append(num)
        hidou_list.append(1)

print(uniqe_num)
print(hidou_list)


print("\n가장 많이 등장한 숫자 Top 3 (동점 포함):")
pairs = []
for i in range(len(uniqe_num)):
    pairs.append([uniqe_num[i], hidou_list[i]])

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[i][1] < pairs[j][1]:
            pairs[i], pairs[j] = pairs[j], pairs[i]

top_count = 0

#빈도수 기억 리스트
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