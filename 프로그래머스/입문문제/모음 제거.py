def solution(my_string):
    answer = ''
    un = "aiueo"
    for i in my_string:
        if i not in ["a", "i", "u", "e", "o"]:
            answer += i
    return answer

print(solution("bus"))