N = int(input())
count = 1
n = 1


while(True):
    if n >= N:
        print(count)
        break
    n += (6*count)
    count += 1