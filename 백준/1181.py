n = int(input())

lis = []

for i in range(n):
    str1 = input()
    if str1 not in lis:
        lis.append(str1)

sorted_words = sorted(lis,key=lambda x : (len(x),x))

for p in sorted_words:
    print(p)


# for k in range(len(lis)):
#     for j in range(len(lis)):
#         if len(lis[k]) == len(lis[j]) and lis[k] <lis[j]:
#             lis[k] , lis[j] = lis[j] , lis[k]
#         elif len(lis[k]) < len(lis[j]):
#             lis[k] , lis[j] = lis[j] , lis[k]


