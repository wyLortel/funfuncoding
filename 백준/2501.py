num1 , num2 = map(int,input().split())

count = 0

for i in range(1,num1):
    if num1 % i == 0 :
        count += 1

    if count == num2:
        print(i)
        break
else:
    print(0)

