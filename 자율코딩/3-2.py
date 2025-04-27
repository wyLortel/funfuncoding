"""
입력
    주당 수업 시간 입력
    결석한 총 시간 입력
    지각횟수 입력

처리
    출석점수는 20점
    20 - (20 * 결석시간수 / 총 수업 시간수)
        총수업 시간수는 주당수업시간 * 15
    
    지각 처리
        지각 3회는 결석 1시간
    
    결석 시간이 총 수업 시간 1/4의 초과 하면 f처리
"""



def calculate_atteddance_score(hour_per_week , absebce_hours , tardy_count):
    absebce_hours += tardy_count // 3
    
    hours_week = hours_per_week * 15
    
    if absebce_hours > hours_week / 4:
        return "당신의 출석 점수는 F (학점 미부여) 점수입니다"
    else:
        return f"당신의 출석 점수는{20 - (20 * absebce_hours / hours_week):.2f}"

hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absebce_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

print(calculate_atteddance_score(hours_per_week ,absebce_hours , tardy_count))


