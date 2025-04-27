#int(), input(), print(), len(), range(), append(), randinit(),
#사용자 정의형 함수 이외의 함수 사용은 금지합니다.

#사용자에게 주사위를 던질 횟수 n 을 입력받음
#유효하지않은 값을 입력할 경우 재입력을 요청한다

#사용자가 입력한 횟수n만큼 주사위를 던진다
#주사위의 결과는 1부터 6사이의 숫자
#각 숫자의 발생 횟수 카운트

#1부터 6까지의 발생빈도를 시각화 발생빈도의 최대치에 대한 성적은 상대적인 비율이며
#최대 10개까지의 * 표시

#각 숫자별로 발생 횟수와 획률을 표시한다
#확률은 발생횟수 / 총시도 횟수로 계산

import random


dice_roll_count = int(input("DICE ROLL fraquency histogram: "))

count = [0,0,0,0,0,0]

def percent(num):
    return (num / dice_roll_count) * 100

def hosi_percent(num):
    max_count = 0
    for value in count:
        if value > max_count:
            max_count = value
    return "*" * round((num / max_count) * 10)



if not 100 <= dice_roll_count <= 1_000_000:
    print("잘못입력햇습니다 다시 입력해주세요") 
else:
    for i in range(dice_roll_count):
        roll_dice = random.randint(1,6)
        if roll_dice == 1:
            count[0] += 1
        elif roll_dice == 2:
            count[1] += 1
        elif roll_dice == 3:
            count[2] += 1
        elif roll_dice == 4:
            count[3] += 1
        elif roll_dice == 5:
            count[4] += 1
        else :
            count[5] += 1


for i in range(6):
    print(f"{hosi_percent(count[i])} {count[i]}times , {percent(count[i]):.2f}%")

