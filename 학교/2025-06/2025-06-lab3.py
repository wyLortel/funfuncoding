def star(max_count , num):
    return num / max_count * 10


import random
while True:
    dice = int(input("주사위 굴릴 횟수를 알려주세용 100 ~1,000,000 : "))
    if not 100 <= dice <= 1000000:
        print("잘못된 입력입니다")
    else:
        break


dice_dic = {i : 0 for i in range(1,6+1)}

for _ in range(dice):
    ran_num = random.randint(1,6)
    dice_dic[ran_num] += 1


max_count = 0

for v in dice_dic.values():
    if v > max_count:
        max_count = v


print("주사위 히스토리 : ")

for key , value in dice_dic.items():
    print_star = "*" * int(star(max_count , value))
    percent = value / dice * 100
    print(f"{key}: {print_star} ({value}times , {percent:.2f}%)")