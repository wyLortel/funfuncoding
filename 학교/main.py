# 초기 설정:
#     mode = 0
#     ret = 빈 문자열

# for idx in 0부터 code 길이 - 1까지:
#     현재 문자 = code[idx]
    
#     만약 현재 문자가 "1"이면:
#         mode를 0이면 1로, 1이면 0으로 바꿈 (토글)
    
#     그렇지 않다면:
#         mode가 0일 때:
#             만약 idx가 짝수라면 ret에 현재 문자 추가
#         mode가 1일 때:
#             만약 idx가 홀수라면 ret에 현재 문자 추가

# 만약 ret가 빈 문자열이면:
#     "EMPTY"를 return
# 그 외에는:
#     ret를 return

def solution(code):
    answer = ''
    mode = 0
    ret = ""
    for i in range(1,code-1):
        
    return answer