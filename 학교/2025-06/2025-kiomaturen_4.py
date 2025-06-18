import random

while True:
    user_input = int(input("굴릴 주사위 수를 입력해주세요 (100 ~ 1,000,000): "))
    if not 100 <= user_input <= 1000000:
        print("잘못 입력했습니다. 다시 한번 입력해주세요.")
    else:
        break


counts = {i : 0 for i in range(1,6 +1)}


for _ in range(user_input):
    dice_roll = random.randint(1,6)
    counts[dice_roll] += 1


max_count = 0
for v in counts.values():
    if v >= max_count:
        max_count = v



def star(input_num , num):
    star = num/max_count * 10
    return star


print(f"""
주사위 히스토리:
1: {"*" * int(star(user_input,counts[1]))} ({counts[1]}times)
""")

for i in range(1,len(counts)+1):
    print(f"{i}:{"*" * int(star(user_input,counts[i]))} ({counts[i]}times , {counts[i] / user_input * 100 :.2f}%) ")