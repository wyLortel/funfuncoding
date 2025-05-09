#    *
#   * *
#  *   *
# *     *

col = 2

for i in range(col):
    if i == 0:
        print((" " * (col-i) )+ "*")
    else:
        print((" " * (col-i) )+ "*" + (" " * (i*2-1)) + "*" )
    