count = int(input())
scores = list(map(int,input().split()))

max_score = max(scores)
sum = 0

for i in range(count):
    sum += scores[i] / max_score * 100


aver = sum / count
print(aver)
    
    