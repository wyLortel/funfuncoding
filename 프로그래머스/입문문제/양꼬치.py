def solution(n, k):
    answer = 0
    sheep = n * 12_000
    drink = k * 2000
    discount = (n // 10) * 2000
    
    answer = sheep + drink - discount
    return answer

print(solution(64,6))