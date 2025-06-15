def solution(array):
    answer = []
    max_num = 0
    max_num_index = 0
    for i in range(len(array)):
        if array[i] > max_num :
            max_num = array[i]
            max_num_index = i
    answer.append(max_num)
    answer.append(max_num_index)
    return answer