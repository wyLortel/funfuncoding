def solution(sides):
    answer = 0

    # 최대값, 최소값 찾기
    max_num = 0
    min_num = sides[0]  # 초기값 설정
    
    total = 0
    for i in sides:
        total += i
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    
    abs_diff = max_num - min_num

    answer = (total - 1) - abs_diff

    return answer
