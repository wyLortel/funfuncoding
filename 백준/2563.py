# N = int(input()) 

# covered = set()  

# for _ in range(N):
#     x_start, y_start = map(int, input().split())
    
#     for x in range(x_start, x_start + 10):
#         for y in range(y_start, y_start + 10):
#             covered.add((x, y))  

# print(len(covered))



# N = int(input())

# array = [[0] * 100 for _ in range(100)]

# for _ in range(N):
#     y1,x1 = map(int,input().split())
#     for i in range(x1, x1+10):
#         for j in range(y1,y1+10):
#             array[i][j] = 1

# result = 0


# for k in range(100):
#     result += array[k].count(1)
    
# print(result)




N = int(input())

lis = [[0]*100 for _ in range(100)]

for _ in range(N):
    x1,y2 = map(int,(input().split()))
    
    for i in range(x1,x1+10):
        for k in range(y2,y2+10):
            lis[i][k] = 1
    

result = 0

for k in range(100):
    result += lis[k].count(1)

print(result)