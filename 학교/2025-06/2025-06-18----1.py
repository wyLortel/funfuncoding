import random

while True:
    input_user_num = int(input("100에서 1,000,000 사이의 숫자를 입력하세요"))
    if not 100 <= input_user_num <= 1000000:
        print("잘못된 입력입니다")
    else:
        break

dice_num = {i:0 for i in range(1,6+1)}    


for i in range(input_user_num):
    roll = random.randint(1,6)
    dice_num[roll] +=1


max_count = 0

for v in dice_num.values():
    if v > max_count:
        max_count = v

def make_stars(max_num, num):
    return (num / max_num) * 10




print(" 다이스 롤 히스토그램 ")
for key, value in dice_num.items():
    star_print = "*" * int(make_stars(max_count, value))
    kakuritu = value / input_user_num * 100  
    print(f"{key}: {star_print} ({value} times, {kakuritu:.2f}%)")

    