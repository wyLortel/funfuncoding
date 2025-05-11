import random

row = int(input("행"))
col = int(input("열"))

min = 10

for i in range(row):
    for k in range(col):
        ran = random.randint(1,9)
        print(ran , end=" ")
        if ran < min:
            min = ran
    print()


print(f"제일 작은 숫자는{min}")