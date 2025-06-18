import random


def print_board(bingo_lis):
    for i in range(len(bingo_lis)):
        print(bingo_lis[i], end=" ")
        if (i+1) % N == 0:
            print()



def col (array):
    bingo = 0
    
    for i in range(N):
        count = 0
        for k in range(i,len(array),N):
            if array[k] == "*":
                count += 1
        if count == N:
            bingo += 1
            
    return bingo

def row (array):
    bingo = 0
    
    for i in range(0,len(array),N):
        count = 0
        for k in range(i,i+N):
            if array[k] == "*":
                count += 1
        if count == N:
            bingo += 1
            
    return bingo




def hidari (array):
    count = 0
    bingo = 0
    for i in range(0,len(array),N+1):
        if array[i] == "*":
            count += 1
    if count == N:
            bingo += 1
    return bingo


def migi (array):
    count = 0
    bingo = 0
    for i in range(1,N+1):
        if array[i*(N-1)] == "*":
            count += 1
    if count == N:
            bingo += 1
    return bingo


while True:
    N = user_input = int(input("3 부터 6까지의 정수를 입력하세요"))
    if not 3<= N <=6 :
        print("잘못된 입력입니다 다시 입력해주세요")
    else:
        break

bingo_lis = []

while True:
    random_num = random.randint(1,36)
    if random_num not in bingo_lis:
        bingo_lis.append(random_num)
    
    if len(bingo_lis) == N**2:
        break


count = 1
while True:
    bingo = 0
    print_board(bingo_lis)
    
    print("엔터키를 누르시면 랜덤수를 생성합니다")
    random_input_num = input()
    random_input_num = random.randint(1,36)
    count += 1
    
    print(f"{count}번째 숫자 {random_input_num}")
    
    for index in range(len(bingo_lis)):
        if bingo_lis[index] == random_input_num:
            bingo_lis[index] = "*"
    
    bingo += col(bingo_lis)
    bingo += row(bingo_lis)
    bingo += hidari(bingo_lis)
    bingo += migi(bingo_lis)

    print(bingo, "빙고갯수")

