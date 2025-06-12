a,b = map(int,input().split())

if b > a:
    a,b = b,a

min = []

for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        min.append(i)

max_min = max(min)

print(max_min)


count = 1
while True:
    candidate = a * count  
    if candidate % b == 0:  
        min_max = candidate
        break
    count += 1

print(min_max)
