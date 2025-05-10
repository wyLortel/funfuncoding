def check(tmp):
    # 가로
    for i in range(5):
        if bingo[i] == [0] * 5:
            tmp += 1
    # 세로
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            tmp += 1
    # 대각선1
    if all(bingo[i][i] == 0 for i in range(5)):
        tmp += 1
    # 대각선2
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        tmp += 1
    return tmp

bingo = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speak[i] == bingo[x][y]:
                bingo[x][y] = 0
                cnt += 1
    if cnt >= 12:
        result = check(tmp)
        if result >= 3:
            print(i + 1)  # 배열은 0 부터 시작했으므로 
            break


# def check(arr):
#     total=0
#     #가로
#     k=[0,1,2,3,4]
#     for i in range(5):
#         if arr[i][0]==0:
#             tmp=0
#             for K in k:
#                 if arr[i][0+K]==0:
#                     tmp+=1
#             if tmp == 5:
#                 total+=1
#     #세로
#     for i in range(5):
#         if arr[0][i]==0:
#             tmp=0
#             for K in k:
#                 if arr[0+K][i]==0:
#                     tmp+=1
#             if tmp == 5:
#                 total+=1
#   #대각선1
#     tmp=0
#     for K in k:
#         if arr[0+K][0+K] == 0:
#             tmp+=1
#     if tmp == 5:
#             total+=1
#     #대각선2
#     tmp=0
#     for K in k:
#         if arr[0+K][4-K] == 0:
#             tmp+=1
#     if tmp == 5:
#             total+=1

#     if total >=3:
#         return True
#     else:
#         return

# arr=[list(map(int,input().split()))for _ in range(5)]
# call=[]
# for _ in range(5):
#     call+=map(int,input().split())
# cnt=0
# for k in range(25): #순서조심!!
#     for i in range(5):
#         for j in range(5):
#             if arr[i][j] == call[k]:
#                 arr[i][j]=0
#                 cnt+=1
#                 break
#     if cnt>=12:
#         t=check(arr)
#         if t==True:
#             print(k+1)
#             break