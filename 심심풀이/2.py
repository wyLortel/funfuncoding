def solution(s):
    s = s.upper()

    num_p = s.count('P')
    num_y = s.count('Y')

    if num_p == num_y :
        answer = True
    else :
        answer = False
    return answer

print(solution('yPPPyy'))