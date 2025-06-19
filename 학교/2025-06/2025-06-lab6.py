def print_bingo(array):
    for num in range(len(array)):
        print(f"{array[num]:>3}" , end=" ")
        if (num+1) % N == 0:
            print()
            
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


def migi (array):
    bingo = 0
    count = 0
    for i in range(1,N+1):
        if array[i*(N-1)] == "*":
            count +=1
    if count == N:
        bingo += 1
    
    return bingo

def hidari (array):
    bingo = 0
    count = 0
    for i in range(N):
        if array[i*(N+1)] == "*":
            count +=1
    if count == N:
        bingo += 1
    
    return bingo



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





import random
while True:
    N = int(input("빙고 사이즈 입력"))
    
    if not 3 <= N <= 6:
        print("잘못된 범위입니다 다시 입력해세요")
    else:
        break

numbers = []

while True:
    random_num = random.randint(1,36)
    if random_num not in numbers:
        numbers.append(random_num)
    
    if len(numbers) == N * N:
        break
    

count = 1

while True:
    bingo = 0
    print_bingo(numbers)
    user_ran_num = input('엔터를 누르시면 랜덤번호가 생성됩니다')
    user_ran_num = random.randint(1,36)
    print(f"{count}번쨰 랜덤숫자{user_ran_num}")
    count += 1
    
    for check in range(len(numbers)):
        if numbers[check] == user_ran_num:
            numbers[check] = "*"
    
    bingo += row(numbers)
    bingo += col(numbers)
    bingo += migi(numbers)
    bingo += hidari(numbers)
    
    print(bingo)
    
    if bingo == 2:
        print("사용자님 축하합니다 이겻습니다")
        break
    



            

        

