count = int(input())

for _ in range(count):
    k = int(input())
    n = int(input())
    
    lis = [[i for i in range(1,n+1)]]
    lis2 = []
    
    for floor in range(k):
        for room in range(n):
            lis2.append(sum(lis[:room]))
            lis = lis2
            
        
    