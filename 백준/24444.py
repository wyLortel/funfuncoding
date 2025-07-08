row = int(input())


for i in range(1,row+1):
    print(" " * (row-i),end="")
    print("*" * (i*2-1),end="")
    print()


for i in range(row-1,0,-1):
    print(" " * (row-i),end="")
    print("*" * (i*2-1),end="")
    print()