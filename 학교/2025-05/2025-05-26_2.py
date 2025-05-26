# def test(*args):
#     for val in args:
#         print(val, end="\t")
#     print()
    

# test(1)
# test(1,2)
# test(1,2,3)
# test(1,2,3,4)


# bar = [1,2,3]
# foo = (4,5,6)

# print(bar,type(bar),bar[1])
# print(foo,type(foo),foo[1])


def bar(*args):
    print(args[0])
    print(*args)

arg_1 = [val for val in range(2,11,2)]
arg_2 = [val for val in range(1,11,2)]


bar(*arg_1)
bar(*arg_2)
