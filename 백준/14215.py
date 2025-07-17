lis = list(map(int,input().split()))

max_num = max(lis)
lis.remove(max_num)
num = lis[0] + lis[1]


if max_num >= num:
    max_num = num -1


tri = max_num + num

print(tri)