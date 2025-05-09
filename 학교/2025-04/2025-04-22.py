# 로그인 정보 설정 (정답 id 와 비밀번호)
correct_id = "admin"
correct_pw = "1234"

#로그인 시도 횟수 초기화
attempt = 0

#최대 5번까지 로그인 시도 허용
while attempt < 5:
    #사용자로부터 id와 비밀 번호 입력받기
    user_id = input("ID 입력: ")
    user_pw = input("PW 입력: ")
    
    #입력값이 올바른 경우 -> 로그인 성공
    if user_id == correct_id and user_pw == correct_pw:
        print("로그인 성공")
        break #프로그램 종료
    
    else:
        attempt += 1 #실패횟수 증가
        remaining = 5 - attempt # 남은 시도 횟수 계산
        
        if attempt >= 5:
            print("계정이 잠금되엇습니다")
        else:
            #오류 메세지와 함께 남은 횟수 안내
            print(f"ID 또는 PW가 잘못되엇습니다 (남은시도: {remaining})" )