# 1. 목표 정하기	
	# 무엇을 구해야 하는가?	
	# "점수를 등급으로 바꾸는 것"
# 2. 재료 정리	문제에서 어떤 정보가 주어졌는가?	
	# "점수(0~100), 점수 구간, 등급"
# 3. 변환 흐름 설계	주어진 재료로 목표를 얻기 위한 절차는?	
	# "점수를 이용해 어느 구간에 속하는지 판단 → 그에 맞는 등급 출력"

# 1단계: 목표 파악
# "점수(score)를 받아서 그에 맞는 등급(A~F)을 출력하라"

# 2단계: 재료 추출
# 입력값: 정수형 점수 (0~100)

# 등급 조건: 

# A: 90 이상

# B: 80 이상

# C: 70 이상

# D: 60 이상

# F: 그 외

a = int(input())
result = ""
if a >= 90:
    result = "A"
elif a >= 80:
    result = "B"
elif a >= 70:
    result = "C"
elif a >= 60:
    result = "D"
else :
    result = "F"

print(result)