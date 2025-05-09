#   *
#  **
# ***
#  **
#   *

col = 3

for i in range(1 , col + 1):
    print(" " * (col - i) + "*" * i)

for i in range(col -1 , 0 , -1):
    print(" " * (col - i) + "*" * i)