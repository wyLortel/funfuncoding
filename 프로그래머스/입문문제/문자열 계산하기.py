def solution(my_string):
    
    num_lis = []
    oper_lis = []
    num = ""
    for i in my_string:
        if i.isdigit():
            num += i
            
        if i == " ":
            continue
        
        if i =="-" or i == "+":
            num = int(num)
            num_lis.append(num)
            oper_lis.append(i)
            num = " "
    
    num_lis.append(int(num))
    
    
    print(num_lis)
    print(oper_lis)
    
    total = num_lis[0]
    
    for k in range(len(oper_lis)):
        if oper_lis[k] == "-":
            total -= num_lis[k+1]
        else:
            total += num_lis[k+1]
    
    return total
    

solution("3 + 4")
