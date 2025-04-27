"""
입력
    사용자로 부터 토지의 면적(제곱미터)를 입력받음
처리
    convert_to_square_feet 제곱미터를 평방비트로 변경
    1제곱미터 = 10.7639평방비트트
    
    convert_to_acres 제곱미터를 에이커로 변경
    1에이커(ac) = 4046.86 제곱미터 (m²)

조건
    입력받은 면적이 음수일 경우 , 변환대신 잘못된 입력입니다 출력

출력
    변환된 면적을 평방피트와 에이커 단위로 출력
"""

def convert_to_square_feet(squaer_meters):
    return squaer_meters * 10.7639

def conver_to_acres(squaer_meters):
    return squaer_meters / 4046.86

squaer_meters = float(input("토지의 면적을 제곱미터 단위로 입력하세요"))

if squaer_meters < 0 :
    print("잘못된 입력입니다")
else:
    print(convert_to_square_feet(squaer_meters))
    print(conver_to_acres(squaer_meters))