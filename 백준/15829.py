L = int(input())
M = 1234567891

word = input()
lis = []
total = 0

for i in word:
    lis.append(ord(i)-96)


for k in range(len(lis)):
    total += lis[k] * (31**k)
    total %= M

print(total)    
