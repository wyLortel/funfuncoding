def solution(score):
    answer = []
    
    aver_list = []
    
    for i in score:
        total = sum(i)
        aver = total / len(i)
        aver_list.append(aver)
    
    aver_list_2 = sorted(aver_list , reverse= True)
    
    for k in aver_list:
        count = 1
        for j in aver_list_2:
            if k == j :
                answer.append(count)
                break
            count += 1
    
    print(answer)
    return answer




lis = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]

solution(lis)
