def solution(chicken):
    service_total = 0
    while chicken >= 10:
        service = chicken // 10
        service_total += service
        chicken = service + (chicken % 10)
    return service_total

print(solution(100))  
