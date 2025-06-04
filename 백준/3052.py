N = int(input())

for i in range(N):
    score = input()
    totla_score = 0
    ren_score = 0
    for index , val in enumerate(score):
        if val == "O":
            ren_score += 1
            totla_score += ren_score
        elif val == "X":
            ren_score = 0
            totla_score += ren_score
    
    print(totla_score)
            
        
        
