#줄수
column = 5


for i in range(1,column+1):
    print(" " * (column-i) + ("*" * (i*2-1)))

for i in range(column-1 , 0 ,-1):
    print(" " * (column-i) + ("*" * (i*2-1)))