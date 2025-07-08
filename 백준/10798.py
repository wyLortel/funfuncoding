strs = [] 

string = ""

for i in range(5):
    st = input()
    strs.append(st)

max_len = max(len(s) for s in strs)

for index1 in range(max_len):  
    for index2, value2 in enumerate(strs):  
        if index1 < len(strs[index2]): 
            string += strs[index2][index1]        

print(string)
