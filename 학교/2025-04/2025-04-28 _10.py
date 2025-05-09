"""
   *
  **
 ***
****
"""

row = 3
col = 3

#row 반복
for num_row in range(row , 0 , -1):
    #col 반복
    for _ in range(num_row):
        # * 출력
        print("*", end="")
    
    print()