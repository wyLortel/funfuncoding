# 10개의 정수 입력받기
num = []
n = set()
for q in range(10):
    num.append(int(input("q")))
    n.add(num[q] % 42)

print(len(n))

# 42로 나누었을때 서로 다른나머지 몇개 출력