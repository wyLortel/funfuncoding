# import sys
# input = sys.stdin.readline

# n1 , n2 = map(int,input().split())
# lis = list(map(int,input().split()))
# prefix_sum = [0]
# temp = 0

# cor = []

# for i in lis:
#     temp = temp + i
#     prefix_sum.append(temp)

# for i in range(n2):
#     a,b = map(int,input().split())
#     cor.append(prefix_sum[b]-prefix_sum[a-1])


# for k in cor:
#     print(k)























import sys
input = sys.stdin.readline

n1 , n2 = map(int,input().split())

lis = list(map(int,input().split()))

temp = 0


sum_list = [0]

for i in lis:
    temp += i
    sum_list.append(temp)

print(sum_list)

new_list = []

for k in range(n2):
    num1 , num2 = map(int,input().split())
    num3 = sum_list[num2] - sum_list[num1-1]
    new_list.append(num3)


for k in new_list:
    print(k)












