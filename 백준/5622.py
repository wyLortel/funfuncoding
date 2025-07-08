str = input()

sum = 0

one = ["A" , "B" , "C"]
two = ["D" , "E" , "F"]
three = ["G" , "H" , "I"]
four = ["J" , "K" , "L"]
five = ["M" , "N" , "O"]
six = ["P" , "Q" , "R" , "S"]
seven = ["T" , "U" , "V"]
eight = ["W" , "X" , "Y" , "Z"]





for i in str:
    if i in one:
        sum += 3
    elif i in two:
        sum += 4
    elif i in three:
        sum += 5
    elif i in four:
        sum += 6
    elif i in five:
        sum += 7
    elif i in six:
        sum += 8
    elif i in seven:
        sum += 9
    elif i in eight:
        sum += 10
    
print(sum)