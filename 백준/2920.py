c,d,e,f,g,a,b,C = map(int,input().split())

my_list = [c,d,e,f,g,a,b,C ]


if my_list == list(range(1, 9)):
    print("ascending")
elif my_list == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")