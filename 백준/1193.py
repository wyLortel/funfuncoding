X = int(input())

line = 1
total = 0

while total + line < X:
    total += line
    line += 1


order = X - total


if line % 2 == 0:
    numerator = order
    denominator = line - order + 1
else:
    numerator = line - order + 1
    denominator = order

# 결과 출력
print(f"{numerator}/{denominator}")
