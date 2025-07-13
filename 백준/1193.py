sum = 0
index = 0
x = 7
i = 1

while True:
    if sum < x:
        index = x - sum
        break
    sum += i
    i+=1

print(index)