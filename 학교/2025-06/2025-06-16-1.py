bar = {"a" : 1 , "b" : 2 , "c" : 3}

foo = {"b" : 2 , "a" : 5 , "c" : 3 , "d" : 10}


keys = ["a" , "b"]

result = {k : value for k , value in bar.items() if k not in keys}






# merged = {**bar, **foo}

# test = foo | bar 

print(result)


