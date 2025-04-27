# 세 과목 성적 입력 (정수 입력)
    #-국어 점수 입력
    #-영어 점수 입력
    #- 수학 점수 입력

#평균 점수 계산 
#-평균 = (국어 + 영어 + 수학) / 3

#합격 여부 판별 조건
    #우수합격 평균이 90점이상이고 , 세과목 모두 90점 이상인 경우
    #일반합격 평균이 70점 이상이고 , 세과목이 모두 40점 이상인 경우
    #불합격: 위 두조건에 해당하지않는 경우 

# 결과 출력
    #평균 점수 :  xxx점
    #합격 결과:우수합격 / 합격 / 불합격중 하나 출력
    
    
# 세 과목 성적 입력 (정수 입력)
score_korean = int(input("국어 점수를 입력해주세요"))
score_english  = int(input("영어 점수를 입력해주세요"))
score_math = int(input("영어 점수를 입력해주세요"))


#평균 점수 계산 
score_average = (score_korean + score_english + score_math) / 3

result = ""

#합격 여부 판별 우수 
if (
    score_average >= 90 and
    score_korean >= 90 and
    score_english >= 90 and
    score_math >= 90
):
    result = "우수합격"


#합격 여부 판별 합격
elif (
    score_average >= 70 and
    score_korean >= 40 and
    score_english >= 40 and
    score_math >= 40
):
    result = "합격"

else:
    result = "불합격"

# 결과 출력
print(f"평균: {score_average:.1f}점")
print(f"결과:{result}")