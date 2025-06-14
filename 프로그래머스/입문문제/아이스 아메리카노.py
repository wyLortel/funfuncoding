def solution(money):
    answer = []
    
    drink = 5500
    
    cup = money // drink
    nokori = money - drink*cup
    
    answer=[cup,nokori]
    
    return answer