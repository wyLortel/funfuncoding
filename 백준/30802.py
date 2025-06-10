N = int(input())
S,M,L,XL,XXL,XXXL = map(int,(input().split()))
T, P = map(int,(input().split()))


col_list = [S, M, L, XL, XXL, XXXL]

total_t = 0

for i in col_list:
    if i % T == 0:
        total_t += i // T
    else:
        total_t += (i // T) +1



print(total_t)
print(N//P , N % P)
