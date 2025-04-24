"""
사용자의 나이를 정수로 입력 받음
나이에 따라서 도서관 이용권 판별
    if age <= 12 어린이
    elif age <= 18 청소년
    else 성인
"""

# 사용자의 나이를 정수로 입력 받음
user_age = int(input("사용자의 나이를 입력해주세요: "))



result = ""
# 나이에 따라서 도서관 이용권 판별
if user_age <= 12:
    result = "어린이"
elif user_age <= 18:
    result = "청소년"
else:
    result = "성인"
    

#출력력
print(f"{result} 이용권을 사용할수 있습니다")