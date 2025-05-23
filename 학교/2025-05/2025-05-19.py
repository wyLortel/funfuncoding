bar = [val for val in range(1,11,2)]
print(bar)


pos = foo = bar

pos[0] = 10
foo[-1] = 100
print(foo)

#요소만 복사
b = pos.copy

print(id(pos))
print(id(b))