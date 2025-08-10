n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]
for a, b in people:
    rank = 1
    for c, d in people:
        if c > a and d > b:
            rank += 1
    print(rank, end=' ')
