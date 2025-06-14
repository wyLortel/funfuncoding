def solution(price):
    answer = 0
    discount = 0
    
    if price >= 500_000:
        discount = 0.2
    elif price >= 300_000:
        discount = 0.1
    elif price >= 100_000:
        discount = 0.05
        
    answer =  int(price - (price * discount))
    
    
    return answer