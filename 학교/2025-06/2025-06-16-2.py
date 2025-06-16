# bar = ["a","b","c"]


# foo = [10,20,30]
# pos = [100,200,300]


# result = zip(bar,foo,pos)


# for v1 , v2 , v3 in result:
#     print(v1,v2,v3)


# def bar(a,b,*c):
#     print(a,b)
#     print(c)
    

# foo = [val for val in range(1,10)]

# bar(*foo)


def bar(a,*b,c =10,**kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs)

foo = [val for val in range(1,10)]
pos = {"d" : 10 , "e" : 20 , "f" : 30}

bar(*foo , **pos)