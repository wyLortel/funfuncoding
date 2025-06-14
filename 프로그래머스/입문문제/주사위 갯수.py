def solution(box, n):
    lis = [i//n for i in box]
    answer = lis[0] * lis[1] * lis[2]
    return answer