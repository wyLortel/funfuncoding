"""
반복적으로 사용자에게 id 입력 받음
최대 5회 제한 실패시 계정잠금
로그인 성공시 로그인 성공 출력
"""

user_id = "admin"
user_pw = "1234"

count = 5

while count > 0 :
    id = input("ID 입력: ")
    pw = input("PW 입력: ")
    
    if id == user_id and pw == user_pw:
        print("로그인 성공!")
        break
    else:
        count -= 1
        print(f"ID 또는 PW가 잘못되엇습니다 (남은 시도 : {count})")
        
        if count == 0:
            print("계정이 잠금되엇습니다")
        
