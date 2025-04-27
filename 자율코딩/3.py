"""
입력
    사용자 나이
    이벤트 코드
    예약 날자

    if == E1
        age >= 18:
        print("예약 성공")
    else:
        print("나이제한으로 인해 예약할수없습니다")
        
    elif == E2
        if reservation_date % 2 == 0:
            print("예약 성공")
        else:
            print("선택하신 날짜에는 예약하실수 없습니다")
        
    elif == E3
        if age >= 16 and reservation_date % 7 == 0:
            print("예약 성공")
        else:
            if age >= 16:
                print("선택하신 날짜에는 예약하실수 없습니다")
            else:
                print("나이제한으로 인해 예약할수없습니다")  
        
"""

age = int(input("나이를 입력하세요"))
evert_code = input("예약 하려는 이벤트를 입력하세요")
reservation_date = int(input("원하는 예약 날짜를 선택하세요"))



if not 0 < reservation_date <= 31:
    print("잘못된 입력입니다 프로그램을 종료합니다")
    exit()




if  evert_code == "E1":
    if age >= 18:
        print("예약 성공")
    else:
        print("나이제한으로 인해 예약할수없습니다")
        
elif evert_code == "E2":
    if reservation_date % 2 == 0:
        print("예약 성공")
    else:
        print("선택하신 날짜에는 예약하실수 없습니다")
        
        
elif evert_code == "E3":
        if age >= 16 and reservation_date % 7 == 0:
            print("예약 성공")
        else:
            if age >= 16:
                print("선택하신 날짜에는 예약하실수 없습니다")
            else:
                print("나이제한으로 인해 예약할수없습니다") 

else:
    print("잘못된 입력입니다 프로그램을 종료합니다")
    