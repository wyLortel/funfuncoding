lis = []


for i in range(9):
    a = list(map(int,(input().split())))
    lis.append(a)

max_num = 0
index = 0
m_row = 0


for i1 , row in enumerate(lis):
    for i2,col in enumerate(row):
        if col >= max_num:
            max_num = col
            m_row = i1+1
            index = i2+1

print(max_num)
print(m_row , index)
            
            

