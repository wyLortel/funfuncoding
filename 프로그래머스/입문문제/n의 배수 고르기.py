# def solution(n, numlist):
#     answer = []
#     for i in numlist:
#         if i % n == 0:
#             answer.append(i)
#     return answer

def solution(n, numlist):
    answer = [i for i in numlist if i % 2 == 0]
    return answer