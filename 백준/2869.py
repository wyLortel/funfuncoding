A ,B ,V = map(int,input().split())


s1 = (V-B) / (A-B)



if (V-B) % (A-B) == 0:
    print(int(s1))
else:
    print(int(s1)+1)