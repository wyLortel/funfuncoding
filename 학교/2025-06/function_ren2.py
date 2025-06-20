import random

def print_menu():
    print("""
    === 리스트 관리 프로그램 ===
    1. 각 리스트 내 데이터 출력
    2. 특정 리스트 출력
    3. 특정 리스트 삭제
    4. 프로그램 종료
          """)


def print_list(list):
    for i in range(len(list)):
        print(f"[리스트{i+1}] : {list[i]}")

def search_list(list):
    search_list = int(input("출력할 리시트 번호 (1~4)"))
    list_len = [i for i in range(1,len(list)+1)]
    if search_list not in list_len :
        print("리스트 번호가 범위를 벗어낫습니다")
        return
    for i in range(1,len(list)+1):
        if i == search_list:
            print(f"[리스트{i}] : {list[i-1]}")

def pop_list(list):
    pop_list = int(input("삭제할 리시트 번호 (1~4)"))
    list_len = [i for i in range(1,len(list)+1)]
    if pop_list not in list_len :
        print("리스트 번호가 범위를 벗어낫습니다")
        return
    list.pop(pop_list-1)




random_list = []

for i in range(20) :
    random_value = random.randint(0,100)
    random_list.append(random_value)


new_ran_list = []

for ran_list in range(0,len(random_list),5):
    new_ran_list.append(random_list[ran_list:ran_list+5])
    

while True:
    print_menu()
    user_input = int(input("메뉴 선택: "))
    
    if user_input == 1:
        print_list(new_ran_list)

    elif user_input == 2:
        search_list(new_ran_list)
    
    elif user_input == 3:
        pop_list(new_ran_list)

