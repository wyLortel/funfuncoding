count = 0

while count < 3:
    for value in range(1,3):
        if count == 1:
            continue
        
        print("count: " , count, ", value : " , value)
    
    count += 1