# a = None
# print(a is None)


# def foo (arg):
    
#     if arg == 1:
#         print("arg 1 :함수종료")
#         return

#     print("arg" , arg)

#     return arg + 1

# print(foo(1) , type(foo(1)))
# print(foo(2), type(foo(2)))

def foo():
    return 1 , "hello" , 10.0

test = foo()
print(test[0] , test[1] ,test[2])

a , b, c = foo()

print(a,b,c)
