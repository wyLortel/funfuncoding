# bar = [val for val in range(10,20,4)]

# print(bar)

# bar = [i for i in range(1,10+1)]

# print(bar)


bar = [i for i in range(1,10+1) if i % 2 == 0]

print(bar)


foo = [1,2,3,4,5,6,7,8,9.10]

del foo[3]
print(foo)

foo.pop()
print(foo)

foo.remove(8)
print(foo)

foo.remove(10)


num = [10,20,30,40]

bar.remove(50) #에러
