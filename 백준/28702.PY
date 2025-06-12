n = [input() for _ in range (3)]

index = 0
cor = 0

for i in range(len(n)):
    if n[i].isdigit():
        index = i
        break
    

if index == 0:
    cor = int(n[index]) + 3
elif index == 1:
    cor = int(n[index]) + 2
elif index == 2:
    cor = int(n[index]) + 1
    

if cor % 3 == 0 and cor % 5 == 0:
    cor = "FizzBuzz"
elif cor % 5 == 0:
    cor = "Buzz"
elif cor % 3 == 0:
    cor = "Fizz"

print(cor)

    