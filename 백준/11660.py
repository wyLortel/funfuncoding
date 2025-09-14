import sys
input = sys.stdin.readline



n , m = map(int,input().split())

lis_a = [[0] * (n+1)]
lis_d = [[0] * (n+1) for _ in range(n+1)]


for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    lis_a.append(a_row)
    
    
for i in range(1 , n+1):
    for j in range(1,n+1):
        lis_d[i][j] = lis_d[i][j-1] + lis_d[i-1][j] - lis_d[i-1][j-1] + lis_a[i][j]
        
        

for _ in range(m):
    x1,y1,x2,y2= map(int,input().split())
    
    result = lis_d[x2][y2] - lis_d[x1-1][y2] - lis_d[x2][y1-1] + lis_d[x1-1][y1-1]
    print(result)
    

