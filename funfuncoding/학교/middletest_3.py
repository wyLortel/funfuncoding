"""
국어 영어 수학 점수를 사용자에게 입력받기

평균을 구하기
점수랑 평균으로 등급 매기기
    우수
        평균 90이상 세과목 모두 80이상
    합격
        평균 70이상 세과목 모두 40점이상
    불합격
        그외에는 불합격

출력
"""

korean = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))

aver = (korean + english + math) / 3

if(
    korean >= 80 and
    english >= 80 and
    math >= 80 and
    aver >= 90
):
    grade = "우수 합격"
    
elif(
    korean >= 40 and
    english >= 40 and
    math >= 40 and
    aver >= 70
):
    grade = "합격"

else:
    grade = "불합격"
    

print(f"""
국어 점수: {korean}
영어 점수: {english}
수학 점수: {math}
평균 : {aver:.1f}점
결과: {grade}
""")