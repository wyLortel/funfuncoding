def flatten(*args):
    
    lis  = []
    
    for i in args:
        if type(i) == list:
            for j in i:
                lis.append(j)
        else:
            lis.append(i)  

    new_list = []       
    for k in lis:
        if type(k) == list:
            for l in k:
                lis.append(l)
        else:
            lis.append(k) 
        
    
    print(new_list)
    


flatten(1, [2, 3], [[4, 5], 6], 7)
            
