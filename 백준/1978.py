n = int(input())  
numbers = list(map(int, input().split()))

count = n


for num in numbers:
    if num == 1:
        count -= 1
        continue
    for i in range(2,num):
        if num % i == 0:
            count -= 1
            break
        

print(count)
            