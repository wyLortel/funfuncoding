import random

# 입력
N = int(input("난수 개수를 입력하세요: "))
A = int(input("시작 범위를 입력하세요: "))
B = int(input("끝 범위를 입력하세요: "))

# 난수 생성
nums = [random.randint(A, B) for _ in range(N)]

# 고유 숫자 리스트 만들기 (중복 제거, 직접 구현)
unique_numbers = []
for n in nums:
    if n not in unique_numbers:
        unique_numbers.append(n)

# 각 숫자의 빈도 수 세기
frequency_list = []
for uniq in unique_numbers:
    count = 0
    for n in nums:
        if n == uniq:
            count += 1
    frequency_list.append(count)

# 출력
print()
print(nums)
print("고유 숫자 리스트:", unique_numbers)
print("빈도 수 리스트:", frequency_list)
print()

# Top 3 추출 (빈도수가 높은 순서로 3개)
used_counts = []
top3 = []

while len(top3) < 3:
    max_count = -1
    candidates = []

    # max_count 찾기
    for count in frequency_list:
        if count in used_counts:
            continue
        if count > max_count:
            max_count = count

    if max_count == -1:
        break

    # 해당 count에 해당하는 숫자들 모두 찾기
    for i in range(len(frequency_list)):
        if frequency_list[i] == max_count:
            top3.append((unique_numbers[i], max_count))
            if len(top3) == 3:
                break

    used_counts.append(max_count)

# Top 3 출력
print("가장 많이 등장한 숫자 Top 3 (동점 포함):")
for num, cnt in top3:
    print(f"{num} → {cnt}회")
