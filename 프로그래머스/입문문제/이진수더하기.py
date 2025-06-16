def solution(bin1, bin2):
    bin1 = int(bin1,2)
    bin2 = int(bin2,2)
    
    bin3 = bin1 + bin2
    
    bin3 = bin(bin3)[2:]
    
    
    return str(bin3)



print(solution("10" ,"11"))

