import random


def create_list_ele(list_number):
    for _ in range(list_number):
        n = random.randint(1,100)
        ran_list.append(n)

def create_average(ran_list):
    sum = 0
    for i in ran_list:
        sum += i
    average = sum / len(ran_list)
    average = round(average , 2)
    return average

def create_deviation(ran_list , average):
    for i in ran_list:
        deviation.append(i - average)
    return deviation

def create_variance(deviation):
    sum = 0
    for i in deviation:
        sum += i **2
    average = sum / len(deviation)
    average = round(average , 2)
    return average

def create_standard_deviation(variance):
    standard_deviation = variance ** 0.5
    standard_deviation = round(standard_deviation , 2)
    return standard_deviation






ran_list = []
deviation = []

list_number = int(input("리스트의 갯수를 입력하세요"))

if not 5 <= list_number <= 20 :
    print("오류 : 리스트의 갯수는 5개 이상이 20이 하여야 합니다")
    exit()


create_list_ele(list_number)
print(f"생성된 리스트: {ran_list}")

average = create_average(ran_list)
print(f"평균: {average}")

create_deviation(ran_list , average)
print(f"편차: {deviation}")

variance = create_variance(deviation)
print(f"분산: {variance}")

standard_deviation = create_standard_deviation(variance)
print(f"표준편차: {standard_deviation}")

