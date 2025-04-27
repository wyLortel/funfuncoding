"""
입력
    세 과목을 입력받음
과정
    세과목 평균 계산
    평균에 따라 등급 계산
        a = aver >= 90
        b = aver >= 80
        c = aver >= 70
        d = aver >= 60
        f = aver < 60
출력
    각 과목 점수와 평균 등급 출력 
    함수사용
"""

def calculate_average(math_score , science_score , english_score):
    aver =  (math_score + science_score + english_score) / 3
    if aver >= 90:
        grade = "A"
    elif aver >= 80:
        grade = "B"
    elif aver >= 70:
        grade = "C"
    elif aver >= 60:
        grade = "D"
    else:
        grade = "F"

    return f"평균점수는{aver}점 이고 , 학점은{grade}입니다"


math_score = float(input("수학점수를 입력하세요"))
scince_score = float(input("과학점수를 입력하세요"))
english_score  = float(input("수학점수를 입력하세요"))


print(calculate_average(math_score , scince_score , english_score))

