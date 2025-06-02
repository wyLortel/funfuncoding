import random

N = int(input("N값을 입력하세요"))

if not 1<= N <= 100:
    print("N은 1 이상 100이하의 정수여야 합니다")
    exit()

random_num_list = []

random_num_list = []

while len(random_num_list) < N:
    ranom_num = random.randint(1, 100)
    
    is_duplicate = False
    for i in range(len(random_num_list)):
        if random_num_list[i] == ranom_num:
            is_duplicate = True
            break

    if not is_duplicate:
        random_num_list.append(ranom_num)


lenth_rando_num = len(random_num_list)

print(random_num_list)

answer = int(input(f"원하는 인덱스를 입력하세요 0 ~ {lenth_rando_num-1}: "))


if not 0 <= answer <= lenth_rando_num-1:
    print("유효한 인덱스 범위를 벗어낫습니다")
    exit()

print(f"선택한 인덱스 원소 {random_num_list[answer]}")