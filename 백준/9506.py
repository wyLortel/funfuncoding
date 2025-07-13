def c_num(num):
    dig = []

    for i in range(1,num):
        if num % i == 0:
            dig.append(i)
    
    return dig

while True:
    num1 = int(input())

    if num1 == -1:
        break

    lis = c_num(num1)

    if num1 == sum(lis):
        print(f"{num1} = " ,end="")
        for i , num in enumerate(lis):
            if i != len(lis)-1:
                print(f"{num} + " ,end="")
            else:
                print(f"{num}")
    else:
        print(f"{num1} is NOT perfect.")