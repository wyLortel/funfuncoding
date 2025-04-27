#첫재줄에는 별 1개
#둘째줄에는 별 2개 
#하지만 오른쪽을 기준으로 정렬
num = int(input("숫자입력: "))

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i)