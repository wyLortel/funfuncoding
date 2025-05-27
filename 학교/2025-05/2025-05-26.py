# bar = [val for val in range(1,6)]

# a,b,c,d,e, = bar


# sol = 8

# foo , pos , kin =  2, 3 ,4
# print(foo , pos , kin)

# foo = [1 , 2  ,3]
# pos = [4 ,5 ,6]

# for x , y in zip(foo , pos):
#     print(f"{x},{y}")

# bar = [val for val in range(1,6)]

# # a , *b , c = bar
# # print(a,b,c)

# *a,b,c, = bar
# print(a,b,c)

bar = [1 , 2 ,3]
foo = [40 , 50, 60]

# pos = [bar , foo]
# print(pos)

sol = [*bar,*foo]
print(sol)


