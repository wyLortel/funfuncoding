import random




def row_check(array,num):
    bingo_num = 0
    count = 0
    for i in range(0,len(array),num):
        for k in range(i,i+num):
            if array[k] == "*":
                count+=1
            if count == num:
                bingo_num += 1
        count = 0
        
    return bingo_num

def col_check(array,num):
    bingo_num = 0
    count = 0
    for i in range(0,num):
        for k in range(i,len(array),num):
            if array[k] == "*":
                count+=1
            if count == num:
                bingo_num += 1
        count = 0
        
    return bingo_num


def hidari_check(array, num):
    bingo_num = 0
    count = 0
    for k in range(0, num * num, num + 1):
        if array[k] == "*":
            count += 1
    if count == num:
        bingo_num += 1
    return bingo_num

def migi_check(array, num):
    bingo_num = 0
    count = 0
    for k in range(num - 1, num * num , num - 1):
        if array[k] == "*":
            count += 1
    if count == num:
        bingo_num += 1
    return bingo_num



while True:
    bingo_size = int(input("빙고사이즈를 입력하세요 3부터 6까지"))

    if not 3 <= bingo_size <= 6 :
        print("유효하지않은 입력입니다 다시 입력하세요")
        continue
    else:
        break
    
chek_list = []
    
bing_lis = []
    
for i in range(bingo_size):
    for k in range(bingo_size):
        while True:
            num = random.randint(1,36)
            if num not in chek_list:
                chek_list.append(num)
                break
        print(num, end=" ")
        bing_lis.append(num)
    print()
    
count = 0


while True:  
    bingo_num = 0 
    user_input = input()
    user_input = random.randint(1,36)
        
    for j in range(len(bing_lis)):
        if bing_lis[j] == user_input:
            bing_lis[j] = "*"

    for bing in range(len(bing_lis)):
        if bing % bingo_size == 0 and bing != 0:
            print()
        print(bing_lis[bing],end=" ")
    
    print()
        
    bingo_num += row_check(bing_lis,bingo_size)
    bingo_num += col_check(bing_lis,bingo_size)
    bingo_num += hidari_check(bing_lis,bingo_size)
    bingo_num += migi_check(bing_lis,bingo_size)
    
    count += 1
    
        

    print(bingo_num)

    
    
    print()
    print(f"{count}번째 횟수 도전입니당")   
    print()
    
    if bingo_num == 2:
        break
    
    
                

