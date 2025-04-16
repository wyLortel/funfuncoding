"""
# 사용자에게 3 <= n <=6 의 정수를 입력받음
 #만약 다른숫자이면 올바른 숫자가 나올때까지 재입력
 
n * n 의 빙고보드를 만들기 위해 1차원 리스트를생성
안은 1에서 36사이의 중복되지 않은 정수로 채워짐

생성된 리스트 를 사용하려 n * n형태의 빙고보드 출력 

사용자가 엔터키를 누르면 1부터 36의 사이의 난수를 발생 시키고 화면에 출력
화면에 출력된 난수화 일치하는 보드상의 숫자는 *로 대체됨
매 난수 발생시 게임 실행 횟수를 출력

보드에서 가로 세로 또는 대각성을 포함해 최소 2개이상의 줄에서 모든 숫자가 *이되면 
빙고성립으로 사용자 승

int(), input(), list(), list.append(), list.pop(), list.remove(),
len(), print(), random.randint(), range(), 사용자 정의형 함수
만 사용 가능

보드의 난수 값을 구성하기 위해 반드시 1차원 리스트 사용, 2차원 또는 다른
자료구조 사용 시 감점


"""

import random

bingo_list1 = []
bingo_list2 = []
bingo_list3 = []



def creat_list(num):
    for i in range(num):
        
    
#1
while True:
    bingo_num = int(input("Enter the size of the bingo board (3 to 6): "))



