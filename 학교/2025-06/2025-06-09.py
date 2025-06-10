# def bar(a ,*b, c =20, d=30 , e=40):
#     print(a,b,c,d,e)

# bar(1,2,3,4,5,6,7,8,9)


def foo(a,b,c = 100):
    print(a,b,c)


foo(1,2,3)
foo(a=1,c=3,b=2)
foo(3,2,c=200)