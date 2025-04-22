count = 5

while count > 0:
    # 사용자로부터 id와 비밀번호 입력받기
    user_id = input("ID 입력: ")
    user_pw = input("PW 입력: ")
    
    # 입력값이 올바른 경우 -> 로그인 성공
    if user_id == "admin" and user_pw == "1234":
        print("로그인 성공")
        break  # 프로그램 종료

    else:
        count -= 1  # 실패할 때마다 횟수 줄이기
        if count == 0:
            print("계정이 잠금되었습니다.")  # 5번 틀리면 잠금
        else:
            print(f"로그인 실패. 남은 시도 횟수: {count}회")
