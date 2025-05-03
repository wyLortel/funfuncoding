import random


num_tables = int(input("테이블 갯수 입력"))
num_row = int(input("행 수 입력: "))
num_cols = int(input("열수 입력: "))

print("출력 옵션을 선택하세요:")
print("1. 1부터 시작하여 열 방향으로 증가")
print("2. 1~100 사이 랜덤 값 출력")
option = int(input("옵션(1 또는 2): "))

print("출력 형태를 선택하세요: ")
print("1. 테두리만 출력")
print("2. 왼쪽 -> 오른쪽 대각선 출력")
print("3. 오른쪽-> 왼쪽 대각선 출력")
print("4. 양방향 대각선 출력")
shape = int(input("출력 형태 옵션 (1~4): "))

#테이블 생성 및 출력
for table_index in range(num_tables):
    print(f"\n테이블{table_index + 1}")
    
    current_number = 1 #순차 숫자 초기값
    
    #메트릭스 출력 num_row로 구성
    for row in range(num_row):
        # 벡터 생성 시작 num_col로 구성
        for col in range(num_cols):
            #출력 형태에 따른 조건 분기
            if shape == 1:
                #테두리만 출력
                if row == 0 or row == num_row -1 or col == 0 or col == num_cols -1:
                    print(current_number if option == 1 else random.randint(1,100) , end="\t")
                else:
                    print(" ", end="\t")

            elif shape == 2:
                #왼쪽->오른쪽 대각선만 출력
                if row == col:
                    print(current_number if option == 1 else random.randint(1,100) , end="\t")
                else:
                    print(" ", end="\t")
            
            
            elif shape == 3:
                #오른쪽->왼쪽- 대각선만 출력
                if col == num_cols - row -1:
                    print(current_number if option == 1 else random.randint(1,100) , end="\t")
                else:
                    print(" ", end="\t")
            
            elif shape == 4:
                #양방향 대각선 출력
                if row == col or col == num_cols -row - 1:
                    print(current_number if option == 1 else random.randint(1,100) , end="\t")
                else:
                    print(" ", end="\t")
            # 조건분기 종료
            
            #숫자 증가 
            current_number += 1
            
        print()