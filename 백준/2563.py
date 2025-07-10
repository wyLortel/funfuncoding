N = int(input()) 

covered = set()  

for _ in range(N):
    x_start, y_start = map(int, input().split())
    
    for x in range(x_start, x_start + 10):
        for y in range(y_start, y_start + 10):
            covered.add((x, y))  

print(covered)
print(len(covered))
