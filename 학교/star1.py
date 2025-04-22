# num_lines = 5

# for i in range(1,num_lines+1):
#     print(i)

# num_lines = 5
# num_stars = 3

# for i in range(1, num_lines):
#     print(str(i) + ("*" * num_stars))


# num_lines = 5

# for i in range(num_lines , 0 , -1):
#     print( ("*" * i) , end="")
#     print()


# num_lines = 5

# for i in range(num_lines , 0 ,-1):
#     print(" " * (num_lines - i) + "*" * i ,end="")
#     print()

# num_lines = 5
# for i in range(1,num_lines+1):
#     print(" " * (num_lines-i) ,end=" ")
#     print("*" * (i*2-1))

num_lines = 5

for i in range(1, num_lines+1):
    print(" " * (num_lines - i) + "*" * (i * 2 - 1))


for i in range(num_lines-1 , 0 , -1):
    print(" " * (num_lines - i) + "*" * (i * 2 - 1))