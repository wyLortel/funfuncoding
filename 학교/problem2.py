
#평균 계산
#합격조건 맞나 계산
#평균 점수 70점이상
#세 과목 각각의 점수가 모두 40점 이상

#우수 합격 조건 (아래 조건을 만족하면 우선 적용)
#평균점수가 90점이상
#세 과목 각각의 점수가 모두 80점이상

# 국어 영어 수학 정수로 입력받음
user_score_korean = int(input("국어 점수:\t"))
user_score_english = int(input("영어 점수:\t"))
user_score_math= int(input("수학 점수:\t"))

#평균 계산
average = (user_score_korean + user_score_english + user_score_math) / 3


#우수 합격 조건 (아래 조건을 만족하면 우선 적용)
#평균점수가 90점이상
#세 과목 각각의 점수가 모두 80점이상
if (
    average >= 90 and
    user_score_math >= 80 and
    user_score_korean >= 80 and
    user_score_english >= 80
):
    result = "우수합격"


#합격조건 맞나 계산
#평균 점수 70점이상
#세 과목 각각의 점수가 모두 40점 이상
elif(
    average >= 70 and
    user_score_math >= 40 and
    user_score_korean >= 40 and
    user_score_english >= 40
):
    result = "합격"

# 그 외에는 불합격
else:
    result = "불합격"

print(f"{average:.2f}점")
print(f"결과: {result}")


